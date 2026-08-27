# Operations Guide

## Scale Run

Required inputs:

- Demo root and fixture source.
- Organization, tenant, and folder.
- Process key with version, release key, feed ID, and folder key.
- Requested count, maximum concurrency, delay, and fixture strategy.
- Expected initial or terminal state.
- Known downstream side effects.
- Canary continuation rule and stop conditions.

Workflow:

1. Inspect the BPMN and fixture schema.
2. Confirm login and discover the deployed process.
3. Materialize a plan.
4. Review the target and side-effect preview.
5. Obtain bounded approval.
6. Run locally with `--dry-run`.
7. Start one canary.
8. Inspect the canary by exact instance ID.
9. Resume the same plan and evidence directory.
10. Reconcile exact instance states and report submitted versus completed counts separately.

## List Instances

Prefer server-side folder, process, status, and time filters. Preserve pagination information and make partial results explicit.

For every candidate show:

- Instance ID.
- Process package ID and version.
- Folder key or path.
- Latest status.
- Current element or cursor when available.
- Created, started, updated, and completed UTC timestamps.
- Incident summary.

When the list endpoint repeats pages or ignores filters, do not infer a total. Reconcile exact IDs from the batch ledger with per-instance reads.

## Open an Instance

Opening is read-oriented but may expose runtime data.

1. Resolve the exact instance ID and folder.
2. Prefer a supported deep link.
3. If navigation is UI-only, reuse an authenticated browser session.
4. Verify the visible instance ID and folder before presenting the page.
5. Do not persist screenshots containing sensitive variables unless requested.

## Retry an Instance

Retry is a cloud mutation and needs explicit approval.

Before approval:

1. Fetch the instance, latest run, incidents, current element, and relevant variables.
2. Classify the originating failure.
3. Decide whether the failure is transient.
4. Confirm repeated connector, queue, robot, notification, and external writes are idempotent or compensatable.
5. Confirm the deployed definition and bindings have not changed unexpectedly.
6. Preview the exact instance IDs.

Reject bulk retry when instances have different unexplained causes. After retry, fetch every instance again and record the new run ID and status.

## Migrate Instances

Migration requires exact instance IDs plus an explicit target version.

Before approval:

1. Verify that the target version exists in the same approved folder.
2. Compare the active source element with the target BPMN definition.
3. Compare bindings, variable names and types, expected outputs, and wait semantics.
4. Identify unsafe instances individually.
5. State rollback constraints and any irreversible side effects.
6. Preview the source version, target version, and instance IDs.

After migration, fetch each instance and record its package version, status, cursor, and incidents.

## Goto a BPMN Element

Goto is precise cursor manipulation, not a generic repair.

Before approval:

1. Fetch each instance's current cursor or element executions.
2. Read the deployed BPMN definition.
3. Resolve exact source and target element IDs.
4. Confirm the target is reachable and semantically safe.
5. Evaluate skipped or repeated side effects.
6. Preview every `{instanceId, sourceElementId, targetElementId}` transition.

Reject display labels, screenshots, guessed identifiers, stale cursors, ambiguous gateways, and cross-process element IDs. Verify every resulting cursor after the action.

## Stop or Recover a Batch

Stop new submissions when authentication or target changes, rate limiting persists, configuration errors repeat, or unexpected external effects appear.

The runner preserves its ledger after interruption. To recover:

1. Resolve the cause without editing the plan or ledger.
2. Confirm the original target is still intended.
3. Inspect already-submitted instances.
4. Repeat the same runner command and evidence directory.
5. Confirm the preview lists only genuinely pending ordinals.

Do not cancel already-started instances unless cancellation receives separate approval.

