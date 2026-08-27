# Runtime Contract

Use this reference for input planning, selection, API fallback, and evidence normalization.

## Scale-Run Inputs

Require:

- `demo_root`: existing demo workspace.
- `count`: integer from 1 through 10,000.
- `fixtures`: one JSON object, an array of JSON objects, or a directory of JSON object files.
- `max_concurrency`: integer from 1 through `count`; default to the smaller of 3 or `count` only when the user does not specify it.
- `delay_ms`: non-negative pause between completed parallel waves; default to 1000 only when the user does not specify it.
- `fixture_strategy`: `cycle` or `first`; default to `cycle`.

Treat the count as the number of requested starts, not guaranteed completed process instances. Preserve fixture payloads exactly; do not inject a correlation property the BPMN input schema may reject. Store demo and fixture paths relative to the batch directory when they share a filesystem volume so plans remain portable and public-safe.

Run:

```text
python scripts/prepare_run_plan.py --demo-root <path> --fixtures <path> --count <n> --output <batch>/run-plan.json
```

Add `--max-concurrency`, `--delay-ms`, or `--strategy first` as required. The script creates one immutable input file per planned start next to the plan. Use `--force` only when the user explicitly wants to replace an unexecuted local plan. Never overwrite evidence from an executed batch.

## Deterministic Parallel Runner

Run the plan with the same immutable inputs and exact approved deployment target:

```text
python scripts/run_maestro_batch.py \
  --plan <batch>/run-plan.json \
  --process-key <process-key:version> \
  --folder-key <folder-key> \
  --release-key <release-key> \
  --feed-id <feed-id> \
  --evidence-dir <batch>/execution
```

The runner uses `uip.cmd` on Windows and `uip` elsewhere when the CLI is on `PATH`. Use `--uip <executable>` for a different global executable. For a repository-pinned Node CLI, add `--cli-entry <workspace>/.uipath-tools/node_modules/@uipath/cli/dist/index.js`; use `--node <executable>` only when that entry must run with a non-default Node executable.

On PowerShell, put the command on one line or replace the displayed backslashes with PowerShell continuation syntax. Run first with `--dry-run`, then with `--canary-only` when the approval includes a canary. After verifying the canary, repeat the full command without `--canary-only`; the same ledger causes that successful ordinal to be skipped.

The runner validates every input before mutation, sorts contiguous ordinals, and starts up to `maxConcurrency` CLI processes in each wave. It waits `delayMs` between waves, writes raw stdout and stderr per ordinal, then writes normalized ledger records in ordinal order. It does not retry failed starts. By default it stops new waves after three consecutive failed results; change this only inside the approved failure policy.

For a successful `MaestroJobStarted` result, the current CLI names the new process-instance UUID `JobKey`; the runner preserves it as `jobKey` and also normalizes it as `instanceId`. It never derives an instance ID for another response code.

Resume only with the same plan, target arguments, and evidence directory. A successful start is skipped only when its ledger record has the same target fingerprint. A different process, version, folder, release, or feed produces a different fingerprint and is not silently treated as complete. Use `--start-at` and `--limit` only for a bounded approved slice.

## Canary And Stop Contract

Express canary behavior in the approval summary:

- Start one instance.
- Continue the remaining `count - 1` only if the start returns a stable job or instance identifier in the approved folder and an initial state that matches the expected non-terminal or terminal state.
- Stop without continuing when the target differs, no stable instance ID is returned, validation/authentication fails, or the canary produces an unintended external effect.

For a running batch, stop submission on target/auth drift, persistent throttling, repeated configuration errors, or unexpected side effects. Preserve already-started instances; do not cancel them unless separately approved.

## API And Browser Fallback

Use the current installed UiPath skills and CLI help to discover supported operations. If direct API work is necessary:

1. Load `uipath-platform` before writing or sending the request.
2. Use only documented endpoints and required folder/tenant headers.
3. Reuse the active supported authentication mechanism; never print or persist tokens.
4. Preserve request IDs, HTTP status, and sanitized response bodies in batch logs.
5. Treat each mutating API request as part of the approved batch only when its target and action match the approval preview.

Use Playwright only for a UI-only operation or when both CLI and documented API surfaces are unavailable. Record why the fallback was necessary. Reuse an authorized interactive session, do not automate credential or MFA entry, locate the instance by exact ID, re-check the visible target before clicking, and verify the resulting state through API/CLI when possible.

## Instance Selection

Prefer instance IDs from the current batch ledger. When selecting existing instances, query with the narrowest supported server-side filters, preserve pagination status, and show:

- Instance ID.
- Process and version.
- Folder/environment.
- Current status and element.
- Created and last-updated UTC timestamps.
- Incident summary when retry is proposed.

Never select by row number, display name alone, or a partially loaded browser table.

## Lifecycle Preconditions

### Retry

- Fetch instance, incidents, variables needed for diagnosis, and deployed definition correlation.
- Classify the failure as transient and verify that repeated side effects are idempotent or compensatable.
- Reject batch retry when instances have different unexplained causes.

### Migrate

- Verify the target version exists in the approved folder.
- Compare active element compatibility, bindings, variables, and expected outputs.
- State rollback constraints and identify instances that are not safe to migrate.

### Goto

- Fetch current cursor or element executions.
- Resolve source and target IDs from the deployed BPMN, not a screenshot or guessed label.
- Preview every `{sourceElementId, targetElementId}` transition.
- Reject ambiguous, stale, or cross-process element IDs.

## Ledger Schema

Write one JSON object per line to `instances.jsonl` after every start or lifecycle action:

```json
{
  "timestampUtc": "2026-08-07T15:00:00Z",
  "clientRunId": "demo-20260807T150000Z-0001-a1b2c3d4",
  "operation": "start",
  "processKey": "discovered-process-key",
  "processVersion": "1.2.0",
  "folderKey": "discovered-folder-key",
  "fixtureSource": "data/fixtures/happy-path.json",
  "jobKey": "returned-job-key",
  "runId": "returned-run-id",
  "instanceId": "returned-instance-id",
  "status": "Running",
  "result": "submitted",
  "errorCategory": null,
  "source": "uip-cli"
}
```

Use `operation` values such as `start`, `retry`, `migrate`, `goto`, `open`, or `inspect`. Use `source` values such as `uip-cli`, `uipath-api`, or `playwright`. Omit or set unavailable fields to null; never fabricate identifiers.

## Summary Contract

Keep submitted and completed counts separate. At minimum record:

- Requested starts.
- Submitted starts.
- Failed starts.
- Unique instance IDs.
- Current state counts.
- Lifecycle actions attempted and succeeded.
- Stop reason.
- Partial pagination or inaccessible folder warnings.
