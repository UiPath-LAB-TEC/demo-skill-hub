#!/usr/bin/env python3
"""Start a materialized Maestro run plan with deterministic bounded parallelism."""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    cli = parser.add_mutually_exclusive_group()
    cli.add_argument("--cli-entry", type=Path, help="Path to @uipath/cli dist/index.js")
    cli.add_argument("--uip", help="UiPath CLI executable; defaults to uip.cmd on Windows or uip elsewhere")
    parser.add_argument("--process-key", required=True, help="Deployed process key including version")
    parser.add_argument("--folder-key", required=True)
    parser.add_argument("--release-key", required=True)
    parser.add_argument("--feed-id", required=True)
    parser.add_argument("--node", default="node", help="Node executable used to run the UiPath CLI")
    parser.add_argument("--evidence-dir", type=Path)
    parser.add_argument("--canary-only", action="store_true")
    parser.add_argument("--start-at", type=int, default=1)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-consecutive-failures", type=int, default=3)
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc


def compact_target(args: argparse.Namespace) -> dict[str, str]:
    return {
        "processKey": args.process_key,
        "folderKey": args.folder_key,
        "releaseKey": args.release_key,
        "feedId": args.feed_id,
    }


def target_fingerprint(target: dict[str, str]) -> str:
    encoded = json.dumps(target, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()[:16]


def validate_plan(plan: Any, plan_path: Path) -> list[dict[str, Any]]:
    if not isinstance(plan, dict):
        raise ValueError("Run plan must be a JSON object")
    if plan.get("schemaVersion") != "1.0":
        raise ValueError(f"Unsupported plan schemaVersion: {plan.get('schemaVersion')!r}")
    runs = plan.get("runs")
    if not isinstance(runs, list) or not runs:
        raise ValueError("Run plan must contain a non-empty runs array")
    if plan.get("count") != len(runs):
        raise ValueError("Run plan count does not match the runs array length")
    concurrency = plan.get("maxConcurrency")
    delay_ms = plan.get("delayMs")
    if not isinstance(concurrency, int) or not 1 <= concurrency <= len(runs):
        raise ValueError("Run plan maxConcurrency must be between 1 and count")
    if not isinstance(delay_ms, int) or delay_ms < 0:
        raise ValueError("Run plan delayMs must be a non-negative integer")

    ordinals: set[int] = set()
    client_ids: set[str] = set()
    normalized: list[dict[str, Any]] = []
    for item in runs:
        if not isinstance(item, dict):
            raise ValueError("Every run plan entry must be an object")
        ordinal = item.get("ordinal")
        client_id = item.get("clientRunId")
        input_file = item.get("inputFile")
        if not isinstance(ordinal, int) or ordinal < 1 or ordinal in ordinals:
            raise ValueError(f"Invalid or duplicate ordinal: {ordinal!r}")
        if (
            not isinstance(client_id, str)
            or not re.fullmatch(r"[A-Za-z0-9._-]+", client_id)
            or client_id in client_ids
        ):
            raise ValueError(f"Invalid or duplicate clientRunId: {client_id!r}")
        if not isinstance(input_file, str) or not input_file:
            raise ValueError(f"Missing inputFile for ordinal {ordinal}")
        resolved_input = (plan_path.parent / input_file).resolve()
        if not resolved_input.is_file():
            raise ValueError(f"Input file does not exist for ordinal {ordinal}: {resolved_input}")
        payload = read_json(resolved_input)
        if not isinstance(payload, dict):
            raise ValueError(f"Input file must contain a JSON object: {resolved_input}")
        ordinals.add(ordinal)
        client_ids.add(client_id)
        normalized.append({**item, "resolvedInputFile": str(resolved_input)})

    normalized.sort(key=lambda item: item["ordinal"])
    expected = list(range(1, len(normalized) + 1))
    if [item["ordinal"] for item in normalized] != expected:
        raise ValueError("Run plan ordinals must be contiguous from 1 through count")
    return normalized


def parse_cli_json(stdout: str) -> dict[str, Any]:
    text = stdout.strip()
    if not text:
        raise ValueError("UiPath CLI returned empty stdout")
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        candidates = re.findall(r"(?m)^\s*(\{.*\})\s*$", text)
        if not candidates:
            raise ValueError("UiPath CLI stdout did not contain a JSON object")
        value = json.loads(candidates[-1])
    if not isinstance(value, dict):
        raise ValueError("UiPath CLI JSON result must be an object")
    return value


def successful_client_ids(ledger: Path, target_hash: str) -> set[str]:
    successful: set[str] = set()
    if not ledger.exists():
        return successful
    for line_number, line in enumerate(ledger.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid ledger JSON at line {line_number}: {exc}") from exc
        if (
            record.get("operation") == "start"
            and record.get("result") == "submitted"
            and record.get("targetFingerprint") == target_hash
            and isinstance(record.get("clientRunId"), str)
        ):
            successful.add(record["clientRunId"])
    return successful


def write_json(path: Path, value: Any) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def cli_prefix(args: argparse.Namespace) -> list[str]:
    if args.cli_entry:
        return [args.node, str(args.cli_entry.resolve())]
    return [args.uip or ("uip.cmd" if os.name == "nt" else "uip")]


def validate_cli(args: argparse.Namespace) -> None:
    if args.dry_run:
        return
    if args.cli_entry:
        if not args.cli_entry.resolve().is_file():
            raise ValueError(f"UiPath CLI entry does not exist: {args.cli_entry.resolve()}")
        return
    executable = args.uip or ("uip.cmd" if os.name == "nt" else "uip")
    if Path(executable).parent != Path("."):
        if not Path(executable).expanduser().is_file():
            raise ValueError(f"UiPath CLI executable does not exist: {executable}")
    elif shutil.which(executable) is None:
        raise ValueError(f"UiPath CLI executable was not found on PATH: {executable}")


async def start_one(
    run: dict[str, Any], args: argparse.Namespace, logs_dir: Path, target_hash: str
) -> dict[str, Any]:
    ordinal = run["ordinal"]
    client_id = run["clientRunId"]
    command = [
        *cli_prefix(args),
        "maestro",
        "bpmn",
        "process",
        "run",
        args.process_key,
        args.folder_key,
        "--release-key",
        args.release_key,
        "--feed-id",
        args.feed_id,
        "--inputs",
        f"@{run['resolvedInputFile']}",
        "--output",
        "json",
    ]
    started_at = utc_now()
    environment = os.environ.copy()
    environment["UIPATH_CLI_DISABLE_VERSION_SYNC"] = "1"
    try:
        process = await asyncio.create_subprocess_exec(
            *command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=environment,
        )
        stdout_bytes, stderr_bytes = await process.communicate()
    except OSError as exc:
        return {
            "timestampUtc": utc_now(),
            "startedAtUtc": started_at,
            "ordinal": ordinal,
            "clientRunId": client_id,
            "operation": "start",
            "processKey": args.process_key,
            "folderKey": args.folder_key,
            "releaseKey": args.release_key,
            "feedId": args.feed_id,
            "fixtureSource": run.get("fixtureSource"),
            "targetFingerprint": target_hash,
            "source": "uip-cli",
            "exitCode": None,
            "jobKey": None,
            "runId": None,
            "instanceId": None,
            "status": None,
            "result": "failed",
            "errorCategory": "cli-launch",
            "error": str(exc),
        }
    stdout = stdout_bytes.decode("utf-8", errors="replace")
    stderr = stderr_bytes.decode("utf-8", errors="replace")
    log_prefix = logs_dir / f"{ordinal:04d}-{client_id}"
    log_prefix.with_suffix(".stdout.log").write_text(stdout, encoding="utf-8")
    log_prefix.with_suffix(".stderr.log").write_text(stderr, encoding="utf-8")

    base: dict[str, Any] = {
        "timestampUtc": utc_now(),
        "startedAtUtc": started_at,
        "ordinal": ordinal,
        "clientRunId": client_id,
        "operation": "start",
        "processKey": args.process_key,
        "folderKey": args.folder_key,
        "releaseKey": args.release_key,
        "feedId": args.feed_id,
        "fixtureSource": run.get("fixtureSource"),
        "targetFingerprint": target_hash,
        "source": "uip-cli",
        "exitCode": process.returncode,
    }
    if process.returncode != 0:
        return {
            **base,
            "jobKey": None,
            "runId": None,
            "instanceId": None,
            "status": None,
            "result": "failed",
            "errorCategory": "cli-exit",
        }

    try:
        response = parse_cli_json(stdout)
        data = response.get("Data") if isinstance(response.get("Data"), dict) else {}
        if response.get("Result") != "Success":
            raise ValueError(f"CLI Result was {response.get('Result')!r}")
        job_key = data.get("JobKey") or data.get("jobKey")
        instance_id = data.get("InstanceId") or data.get("instanceId")
        if not instance_id and response.get("Code") == "MaestroJobStarted":
            instance_id = job_key
        return {
            **base,
            "jobKey": job_key,
            "runId": data.get("RunId") or data.get("runId"),
            "instanceId": instance_id,
            "status": data.get("State") or data.get("state"),
            "result": "submitted",
            "errorCategory": None,
        }
    except (json.JSONDecodeError, ValueError) as exc:
        return {
            **base,
            "jobKey": None,
            "runId": None,
            "instanceId": None,
            "status": None,
            "result": "failed",
            "errorCategory": "invalid-cli-result",
            "error": str(exc),
        }


async def execute(args: argparse.Namespace) -> int:
    plan_path = args.plan.resolve()
    if not plan_path.is_file():
        raise ValueError(f"Plan does not exist: {plan_path}")
    validate_cli(args)
    if args.start_at < 1:
        raise ValueError("--start-at must be at least 1")
    if args.limit is not None and args.limit < 1:
        raise ValueError("--limit must be at least 1")
    if args.max_consecutive_failures < 1:
        raise ValueError("--max-consecutive-failures must be at least 1")

    plan = read_json(plan_path)
    runs = validate_plan(plan, plan_path)
    evidence_dir = (
        args.evidence_dir.resolve()
        if args.evidence_dir
        else plan_path.parent / f"{plan_path.stem}.execution"
    )
    evidence_dir.mkdir(parents=True, exist_ok=True)
    logs_dir = evidence_dir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    ledger = evidence_dir / "instances.jsonl"

    target = compact_target(args)
    target_hash = target_fingerprint(target)
    completed = successful_client_ids(ledger, target_hash)
    selected = [run for run in runs if run["ordinal"] >= args.start_at]
    if args.canary_only:
        selected = selected[:1]
    elif args.limit is not None:
        selected = selected[: args.limit]
    pending = [run for run in selected if run["clientRunId"] not in completed]

    preview = {
        "plan": str(plan_path),
        "target": target,
        "targetFingerprint": target_hash,
        "requestedInPlan": plan["count"],
        "selected": len(selected),
        "alreadySubmitted": len(selected) - len(pending),
        "pending": len(pending),
        "maxConcurrency": plan["maxConcurrency"],
        "delayMsBetweenWaves": plan["delayMs"],
        "cliMode": "node-entry" if args.cli_entry else "uip-executable",
        "ordinals": [run["ordinal"] for run in pending],
        "dryRun": args.dry_run,
    }
    write_json(evidence_dir / "execution-preview.json", preview)
    print(json.dumps(preview, separators=(",", ":")), flush=True)
    if args.dry_run:
        return 0
    if not pending:
        summary = {
            "finishedAtUtc": utc_now(),
            "plan": str(plan_path),
            "target": target,
            "targetFingerprint": target_hash,
            "requestedInPlan": plan["count"],
            "selected": len(selected),
            "skippedPreviouslySubmitted": len(selected),
            "submittedThisExecution": 0,
            "failedThisExecution": 0,
            "notAttemptedThisExecution": 0,
            "maxConcurrency": plan["maxConcurrency"],
            "delayMsBetweenWaves": plan["delayMs"],
            "stopReason": None,
        }
        write_json(evidence_dir / "summary.json", summary)
        print(json.dumps(summary, separators=(",", ":")), flush=True)
        return 0

    submitted = 0
    failed = 0
    consecutive_failures = 0
    stop_reason: str | None = None
    concurrency = plan["maxConcurrency"]
    delay_seconds = plan["delayMs"] / 1000

    for wave_start in range(0, len(pending), concurrency):
        wave = pending[wave_start : wave_start + concurrency]
        results = await asyncio.gather(
            *(start_one(run, args, logs_dir, target_hash) for run in wave)
        )
        with ledger.open("a", encoding="utf-8", newline="\n") as stream:
            for record in results:
                stream.write(json.dumps(record, separators=(",", ":")) + "\n")
                if record["result"] == "submitted":
                    submitted += 1
                    consecutive_failures = 0
                else:
                    failed += 1
                    consecutive_failures += 1
                print(
                    json.dumps(
                        {
                            "ordinal": record["ordinal"],
                            "clientRunId": record["clientRunId"],
                            "result": record["result"],
                            "jobKey": record["jobKey"],
                            "status": record["status"],
                        },
                        separators=(",", ":"),
                    ),
                    flush=True,
                )
        if consecutive_failures >= args.max_consecutive_failures:
            stop_reason = f"{consecutive_failures} consecutive start failures"
            break
        if wave_start + concurrency < len(pending) and delay_seconds:
            await asyncio.sleep(delay_seconds)

    summary = {
        "finishedAtUtc": utc_now(),
        "plan": str(plan_path),
        "target": target,
        "targetFingerprint": target_hash,
        "requestedInPlan": plan["count"],
        "selected": len(selected),
        "skippedPreviouslySubmitted": len(selected) - len(pending),
        "submittedThisExecution": submitted,
        "failedThisExecution": failed,
        "notAttemptedThisExecution": len(pending) - submitted - failed,
        "maxConcurrency": concurrency,
        "delayMsBetweenWaves": plan["delayMs"],
        "stopReason": stop_reason,
    }
    write_json(evidence_dir / "summary.json", summary)
    print(json.dumps(summary, separators=(",", ":")), flush=True)
    return 1 if failed or stop_reason else 0


def main() -> int:
    args = parse_args()
    try:
        return asyncio.run(execute(args))
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
