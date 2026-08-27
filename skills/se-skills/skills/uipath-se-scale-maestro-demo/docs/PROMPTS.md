# Prompt Library

Replace angle-bracket placeholders before use. For mutation requests, the skill should still present a bounded preview before acting.

## Plan Only

> Use `$uipath-se-scale-maestro-demo` with the existing Maestro workspace at `<demo-root>`. Target `<organization> / <tenant> / <folder>`. Discover and confirm the deployed process key and version. Prepare, but do not execute, a deterministic plan for `<count>` instances from `<fixture-path>` with maximum concurrency `<n>` and `<delay>` ms between waves. Show the fixture distribution, exact target, expected side effects, canary rule, stop conditions, and evidence path.

## Start a Canary and Continue

> Use `$uipath-se-scale-maestro-demo` to execute `<plan-path>` against `<organization> / <tenant> / <folder>`. Dry-run first. Start one canary and verify its exact instance ID, package version, folder, variables, current element, and side effects. If it matches `<expected-state>`, resume the same plan and evidence directory without duplicating the canary. Do not retry failed starts automatically.

## Long-Running Cohort

> Use `$uipath-se-scale-maestro-demo` with my deployed `<process-name>` BPMN process. Prepare `<count>` synthetic long-running instances using `<fixtures>`, maximum concurrency `<n>`, and `<delay>` ms between waves. The expected outcome is that every instance is running at `<wait-element-id>`. Show the exact cloud target and side effects before mutation, run one canary, then continue only after verifying the wait state.

## Completed Cohort

> Use `$uipath-se-scale-maestro-demo` to create `<count>` completed instances of `<process-name>` from `<fixture-path>`. Use fixture strategy `<cycle-or-first>`, maximum concurrency `<n>`, and `<delay>` ms between waves. Preserve deterministic evidence and verify completion by fetching the exact ledger instance IDs; do not treat accepted starts as completed outcomes.

## Mixed Scenario Cohort

> Use `$uipath-se-scale-maestro-demo` to prepare `<count>` instances of `<process-name>` across the process-compatible scenarios in `<fixture-directory>`. Materialize the plan and show the exact ordinal-to-fixture distribution before mutation. Use maximum concurrency `<n>`, run one canary for each materially different side-effect class if needed, and report submitted and final-state counts separately.

## List a Batch

> Use `$uipath-se-scale-maestro-demo` to inspect all exact instance IDs from `<instances.jsonl>`. Report process version, folder, current status and element, timestamps, and incidents. Keep pagination warnings explicit and make no cloud changes.

## Open an Instance

> Use `$uipath-se-scale-maestro-demo` to open Maestro instance `<instance-id>` in folder `<folder-key>`. Verify the exact ID and folder first. Prefer a supported deep link; use the authenticated browser only if opening is UI-only. Do not modify the instance.

## Diagnose and Retry

> Use `$uipath-se-scale-maestro-demo` to diagnose Maestro instances `<instance-ids>` in folder `<folder-key>`. Fetch incidents, variables, current elements, versions, and relevant side-effect evidence. If and only if the failures share a transient, idempotent cause, show me a retry preview and request explicit approval. Do not retry during diagnosis.

## Migration Preview

> Use `$uipath-se-scale-maestro-demo` to assess migrating `<instance-ids>` from their current version to `<target-version>`. Compare active elements, bindings, variables, outputs, and wait semantics. Identify unsafe instances and rollback constraints. Show the exact migration preview, but do not migrate until I approve it.

## Goto Preview

> Use `$uipath-se-scale-maestro-demo` to assess a goto operation for `<instance-ids>`. Fetch current cursors and the deployed BPMN, then resolve exact source and target element IDs. Explain skipped or repeated side effects and show every proposed transition. Do not execute goto until I approve it.

## Resume an Interrupted Batch

> Use `$uipath-se-scale-maestro-demo` to resume `<plan-path>` with evidence directory `<execution-path>`. Confirm the authenticated organization, tenant, folder, process version, release, and feed still match the prior target fingerprint. Show already submitted and pending ordinals, then request approval before starting only the pending instances.
