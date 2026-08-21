# Troubleshooting

## `uip` or `uip.cmd` Is Not Found

- Confirm the UiPath CLI is installed and on `PATH`.
- On Windows, try `uip.cmd` because PowerShell execution policy may block the `.ps1` shim.
- Pass `--uip C:\full\path\to\uip.cmd`.
- For a repository-pinned CLI, pass `--cli-entry <workspace>/.uipath-tools/node_modules/@uipath/cli/dist/index.js`.

## Login Is Valid but the Target Is Wrong

Run `uip login status --output json` and inspect both organization and tenant. Log into the explicitly intended target before discovery. Do not proceed with a similarly named or historically approved tenant.

## Plan Creation Rejects Fixtures

- Ensure the source exists.
- Ensure every fixture is a JSON object.
- For a JSON array source, ensure every array item is an object.
- For a directory, ensure it contains `.json` files.
- Compare field names and types with the deployed start-event schema.

## Plan Output Already Exists

Plans are intended to be immutable. Choose a new batch directory. Use `--force` only to replace a local plan that has never been executed and whose replacement is explicitly intended.

## Runner Says the CLI Entry Does Not Exist

Use a global CLI by omitting `--cli-entry`, or correct the path to `@uipath/cli/dist/index.js`. `--node` changes only the Node executable, not the CLI entry location.

## Dry Run Passes but Starts Fail

Dry run validates local files and parameters, not cloud access. Check:

- Current login and token validity.
- Folder access.
- Process version, release key, and feed ID.
- Input schema compatibility.
- Tenant service availability.
- Raw stderr and stdout for the first failed ordinal.

## Resume Wants to Start Everything Again

Confirm you used the same:

- Plan file.
- Evidence directory.
- Process key and version.
- Folder key.
- Release key.
- Feed ID.

A changed target fingerprint intentionally prevents a silent skip. Do not copy a ledger between targets.

## Resume Skips an Instance

Inspect its `instances.jsonl` record. The runner skips only a `submitted` start record with the same `clientRunId` and target fingerprint. If the process later faulted, use diagnosis and the retry workflow; do not delete the start record and submit a duplicate blindly.

## Starts Are Slow

- CLI startup and tenant acknowledgment often dominate runtime.
- Use bounded concurrency greater than one in a newly approved plan.
- Reduce `delayMs` only after considering tenant and downstream limits.
- Do not spawn an unbounded process per fixture.
- Use a pinned local CLI to avoid unintended update checks.

## Rate Limiting or Throttling Appears

Stop new waves when throttling persists beyond the approved policy. Preserve the ledger, reduce concurrency in a new plan only with approval, and confirm downstream service health before resuming or starting another batch.

## The List Command Repeats Pages or Ignores Filters

Do not multiply page sizes into a claimed total. Prefer exact instance IDs from `instances.jsonl` and fetch them individually with bounded read concurrency. Record that list pagination was incomplete or unreliable.

## Submitted Does Not Mean Completed

`summary.json` reports accepted starts. Fetch the exact instance IDs and count current runtime states. Inspect terminal elements and outputs when the business outcome matters.

## An Instance Reached the Wrong Route

Inspect start inputs, global variables, script or activity outputs, gateway conditions, bindings, and deployed package version. Fix and validate the source definition before launching another scale batch.

## Retry Is Unsafe

Do not retry until the originating fault and partial external side effects are understood. Split mixed failures into homogeneous groups or handle them individually.

## Migration Is Rejected

Compare the current active element to the target version, along with bindings, variables, outputs, and wait semantics. Some instances may be incompatible even when the target package deploys successfully.

## Goto Cannot Resolve an Element

Use IDs from the deployed BPMN, not labels from the UI or source files for another version. Refresh the current cursor immediately before the action.

## Browser Fallback Fails

Stop. Do not weaken selectors, bypass access controls, or automate credential entry. Reconfirm that the operation is truly unavailable through CLI and documented APIs, then inspect the current authorized page before any further UI action.

