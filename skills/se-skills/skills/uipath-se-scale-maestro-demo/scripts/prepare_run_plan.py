#!/usr/bin/env python3
"""Materialize a deterministic Maestro demo run plan from JSON fixtures."""

from __future__ import annotations

import argparse
import json
import os
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo-root", required=True, type=Path)
    parser.add_argument("--fixtures", required=True, type=Path)
    parser.add_argument("--count", required=True, type=int)
    parser.add_argument("--max-concurrency", type=int)
    parser.add_argument("--delay-ms", type=int, default=1000)
    parser.add_argument("--strategy", choices=("cycle", "first"), default="cycle")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc


def load_fixtures(source: Path) -> list[tuple[str, dict[str, Any]]]:
    if source.is_dir():
        paths = sorted(path for path in source.glob("*.json") if path.is_file())
        if not paths:
            raise ValueError(f"No JSON fixture files found in {source}")
        values = [(str(path.resolve()), read_json(path)) for path in paths]
    elif source.is_file():
        value = read_json(source)
        if isinstance(value, list):
            values = [(f"{source.resolve()}#{index}", item) for index, item in enumerate(value)]
        else:
            values = [(str(source.resolve()), value)]
    else:
        raise ValueError(f"Fixture source does not exist: {source}")

    if not values:
        raise ValueError("Fixture array must not be empty")
    for label, value in values:
        if not isinstance(value, dict):
            raise ValueError(f"Fixture must be a JSON object: {label}")
    return values


def relative_label(label: str, base: Path) -> str:
    path_label, separator, fragment = label.partition("#")
    try:
        relative = Path(os.path.relpath(Path(path_label), base)).as_posix()
    except ValueError:
        relative = Path(path_label).as_posix()
    return f"{relative}{separator}{fragment}" if separator else relative


def validate_args(args: argparse.Namespace) -> None:
    if not args.demo_root.is_dir():
        raise ValueError(f"Demo root is not a directory: {args.demo_root}")
    if not 1 <= args.count <= 10_000:
        raise ValueError("--count must be between 1 and 10000")
    if args.max_concurrency is None:
        args.max_concurrency = min(3, args.count)
    if not 1 <= args.max_concurrency <= args.count:
        raise ValueError("--max-concurrency must be between 1 and --count")
    if args.delay_ms < 0:
        raise ValueError("--delay-ms must be non-negative")
    if args.output.exists() and not args.force:
        raise ValueError(f"Output already exists: {args.output}; pass --force to replace it")


def main() -> int:
    args = parse_args()
    try:
        validate_args(args)
        fixtures = load_fixtures(args.fixtures)
        generated_at = datetime.now(timezone.utc).replace(microsecond=0)
        timestamp = generated_at.strftime("%Y%m%dT%H%M%SZ")
        output = args.output.resolve()
        input_dir = output.parent / f"{output.stem}.run-inputs"
        output.parent.mkdir(parents=True, exist_ok=True)
        input_dir.mkdir(parents=True, exist_ok=True)

        runs = []
        for index in range(args.count):
            fixture_index = 0 if args.strategy == "first" else index % len(fixtures)
            fixture_source, payload = fixtures[fixture_index]
            client_run_id = f"demo-{timestamp}-{index + 1:04d}-{uuid.uuid4().hex[:8]}"
            input_path = input_dir / f"{client_run_id}.json"
            if input_path.exists() and not args.force:
                raise ValueError(f"Input already exists: {input_path}")
            input_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
            runs.append(
                {
                    "ordinal": index + 1,
                    "clientRunId": client_run_id,
                    "fixtureSource": relative_label(fixture_source, output.parent),
                    "inputFile": input_path.relative_to(output.parent).as_posix(),
                }
            )

        plan = {
            "schemaVersion": "1.0",
            "generatedAtUtc": generated_at.isoformat().replace("+00:00", "Z"),
            "demoRoot": Path(os.path.relpath(args.demo_root.resolve(), output.parent)).as_posix(),
            "count": args.count,
            "maxConcurrency": args.max_concurrency,
            "delayMs": args.delay_ms,
            "fixtureStrategy": args.strategy,
            "runs": runs,
        }
        output.write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"output": str(output), "runs": len(runs)}, separators=(",", ":")))
        return 0
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
