# Feature Guide

## Deterministic Planning

`prepare_run_plan.py` validates the demo root, fixture source, count, concurrency, delay, and output location. It creates:

- A versioned JSON plan.
- Contiguous ordinals from 1 through the requested count.
- A stable fixture-to-ordinal mapping inside that plan.
- One immutable JSON input file per planned start.
- Public-safe relative source paths when files share a volume.

Directory fixtures are sorted by filename. `cycle` distributes them in order; `first` selects only the first fixture.

## Bounded Parallel Starts

`run_maestro_batch.py` starts each ordinal wave concurrently up to `maxConcurrency`. It commits normalized records in ordinal order, then waits `delayMs` before the next wave.

Parallelism reduces CLI process latency while preserving:

- A fixed upper bound on simultaneous starts.
- Deterministic wave membership.
- Deterministic ledger ordering.
- A clear stop boundary after a failed wave.

The runner does not silently override plan concurrency.

## CLI Portability

The runner supports:

- `uip.cmd` on Windows when available on `PATH`.
- `uip` on macOS or Linux when available on `PATH`.
- `--uip <executable>` for a custom global CLI path or name.
- `--cli-entry <dist/index.js>` for a pinned `@uipath/cli` installation.
- `--node <executable>` for a non-default Node runtime used with `--cli-entry`.

## Dry Run

`--dry-run` performs complete local validation and writes `execution-preview.json` without invoking UiPath CLI. Use it to review target, count, ordinals, concurrency, delay, and resume behavior before approval.

## Canary Execution

`--canary-only` selects the first eligible ordinal. After verification, rerun the full command with the same plan and evidence directory. A successful canary is skipped on resume.

## Safe Resume

The runner reads `instances.jsonl` and skips only records where:

- `operation` is `start`.
- `result` is `submitted`.
- `clientRunId` matches the plan.
- `targetFingerprint` matches the exact process, folder, release, and feed.

Failed starts are not silently marked complete. Changing the target produces a different fingerprint.

## Bounded Slices

- `--start-at <ordinal>` begins selection at a specific plan ordinal.
- `--limit <count>` restricts selection to a bounded number of ordinals.

Use slices only when the user approved that exact subset. Resume protection still applies.

## Failure Handling

The runner:

- Never automatically retries a failed start.
- Records CLI launch, nonzero exit, and malformed result failures distinctly.
- Defaults to stopping new waves after three consecutive failed results.
- Preserves all already-started instances and evidence.
- Returns a nonzero exit code when any start fails.

`--max-consecutive-failures` may change the stop threshold only within an explicitly approved failure policy.

## Evidence

Each execution directory contains:

- `execution-preview.json`: resolved target and pending ordinals.
- `instances.jsonl`: normalized durable start ledger.
- `summary.json`: selected, skipped, submitted, failed, and unattempted counts.
- `logs/<ordinal>-<clientRunId>.stdout.log`: raw CLI JSON.
- `logs/<ordinal>-<clientRunId>.stderr.log`: CLI diagnostic output.

For a `MaestroJobStarted` response, current CLI output names the instance UUID `JobKey`; the runner keeps `jobKey` and normalizes the same observed value as `instanceId`.

## Instance Discovery and Selection

The skill guides listing and selecting instances by stable ID, process/version, folder, time, status, current element, and incident context. It rejects row-number or display-name-only selection and calls out partial pagination.

## Open

Use a supported deep link when one is returned. Otherwise, use the authenticated UI only after verifying the exact instance ID and folder. Browser automation is a fallback, not a way around access controls.

## Retry

Retry requires diagnosis first. The skill checks the incident cause, current inputs, process version, and side-effect idempotency. It rejects mixed-cause bulk retries and does not treat a failed start as an instance retry.

## Migrate

Migration requires an explicit target version and compatibility review for active BPMN elements, bindings, variables, and outputs. The skill previews exact instance IDs and reports rollback limitations.

## Goto

Goto requires current cursor inspection plus exact source and target BPMN element IDs from the deployed definition. It rejects labels, screenshots, guessed IDs, stale cursors, and cross-process targets.

## API and Browser Fallback

Execution priority is:

1. Current UiPath CLI.
2. Documented UiPath API with the same target and consent boundary.
3. Playwright for a genuinely UI-only operation in an authorized session.

The skill never uses browser automation to bypass MFA, permissions, validation, or an API error.

## Supported Scope

The scripts start Maestro BPMN Process Orchestration processes. Lifecycle guidance is BPMN-specific. Route `.flow`, Case Management, RPA, or Agent operations to their owning UiPath tools or skills.

