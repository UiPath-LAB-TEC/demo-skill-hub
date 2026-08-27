---
name: uipath-se-scale-maestro-demo
description: Scale and operate an existing deployed UiPath Maestro BPMN process. Use when a user asks to start a Maestro process a parameterized number of times, create controlled demo or test instances, list or open individual runs, or safely retry, migrate, or goto selected Maestro process instances. Use UiPath CLI and documented APIs first, installed UiPath skills for lifecycle and diagnosis when available, and Playwright only when the required operation has no supported CLI or API path.
---

# Scale A Maestro SE Demo

Operate an existing Maestro BPMN process; do not redesign or rebuild it unless required runtime artifacts are missing.

## Collect The Operation Contract

Resolve these inputs before any cloud mutation:

- Existing demo or project workspace root containing the BPMN, fixtures, and deployment evidence.
- Operation: `scale-run`, `list`, `open`, `retry`, `migrate`, or `goto`.
- Organization, tenant, environment, and Orchestrator folder.
- Deployed BPMN process key and version discovered from the target environment.
- For `scale-run`: positive run count, fixture/input source, maximum concurrency, and start delay.
- For lifecycle work: exact instance IDs and folder key.
- For `migrate`: explicit target version.
- For `goto`: explicit source and target BPMN element IDs for every transition.

Infer local paths and safe defaults from the demo. Never infer a cloud target, process key, version, instance ID, or BPMN element ID.

## Route To Canonical Skills

1. Read the local demo artifacts. If the workspace was produced by `uipath-se-end-to-end-demo` and that skill is installed, read its relevant contracts.
2. Use `uipath-maestro-bpmn` when installed for BPMN validation, process discovery, run, instance inspection, retry, migrate, and goto behavior. Read its operate and diagnose references before acting.
3. Load `uipath-platform` when installed before calling a UiPath Cloud or Orchestrator API directly. If it is unavailable, do not improvise API endpoints; use current official documentation or remain on the CLI.
4. Use `uipath-troubleshoot` when installed if a run or lifecycle action fails or the cause is unclear.
5. Route `.flow` and `caseplan.json` artifacts to their owning skills. Do not claim BPMN instance lifecycle operations work for another orchestration type.

Treat installed skills and current `uip ... --help` output as canonical. Do not preserve copied command syntax when the installed CLI disagrees.

## Inspect Before Running

Use `rg --files` to locate `.bpmn`, solution, package, fixture, input, validation, and deployment evidence. Confirm that:

- The BPMN artifact is non-empty and locally validated.
- The deployed process and version correspond to the intended demo.
- Every input file matches the process input contract and contains synthetic, demo-safe data.
- The active authentication context and folder match the approved target.
- The planned run count and concurrency fit the expected downstream side effects and available runtime capacity.

Use `scripts/prepare_run_plan.py` to materialize a deterministic, auditable input plan. Execute it with `scripts/run_maestro_batch.py`; do not hand-roll a sequential shell loop. Read [references/runtime-contract.md](references/runtime-contract.md) for the exact runner command, resume behavior, and evidence contract.

## Get Bounded Consent

Default to read-only discovery. Before a mutation, show the user:

- Target organization, tenant, folder, process, and version.
- Operation, run count, maximum concurrency, delay, and fixture mapping.
- Known connector, queue, task, message, robot, or external-system side effects.
- Exact instance IDs for retry, migrate, or goto.
- Target version or source-to-target element transitions when applicable.
- Stop conditions and rollback or recovery path.

Ask for explicit approval of that bounded batch. One approval may cover an exact batch and an optional canary continuation rule; it does not authorize later batches or different lifecycle actions.

## Execute API First

Use this order:

1. Prefer the current `uip` Maestro commands through `uipath-maestro-bpmn`; they are the supported API client and return structured identifiers.
2. If the CLI lacks the operation, use a documented UiPath API through `uipath-platform` with the same target and consent boundary.
3. Use Playwright only when neither supported path exposes the required action and an authorized browser session is available.

Do not use Playwright to bypass permissions, MFA, consent, validation, or an API error. Inspect the live page before choosing selectors, verify the instance ID and folder in the UI, perform only the approved action, and capture the resulting state. Do not persist screenshots containing sensitive runtime data unless requested.

For a scale run:

1. Start one canary when the approved plan includes a canary rule.
2. Verify that its process, folder, instance ID, and initial status are correct.
3. Run the materialized plan with `scripts/run_maestro_batch.py`. It sorts immutable ordinals, starts each bounded wave concurrently, and records results in ordinal order.
4. Resume with the same plan, target arguments, and evidence directory. The runner skips only successfully submitted client run IDs whose target fingerprint matches exactly.
5. Treat `delayMs` as the pause between parallel waves. Increase `maxConcurrency` only by creating a newly approved, unexecuted plan; the runner never silently overrides it.
6. Stop on authentication or target drift, canary failure, repeated configuration errors, rate limiting that exceeds the approved retry policy, or evidence of unintended side effects.
7. Do not convert a failed start into an automatic instance retry. The runner never retries a start.

## Manage Selected Instances

Resolve instances by stable instance ID, not display name or list position. Show a selection preview before requesting mutation approval.

- `retry`: diagnose first; retry only a transient, idempotent failure with valid unchanged inputs.
- `migrate`: confirm the target version exists, input/output compatibility is understood, and rollback is possible.
- `goto`: inspect current cursor/element executions and deployed BPMN; use only user-approved source and target element IDs.
- `open`: use a returned deep link when available; otherwise navigate through the authenticated UI and verify the instance ID before presenting it.

After every action, fetch the instance again and record the resulting status. Never treat retry, migrate, or goto as a generic repair.

## Preserve Evidence

Create a new timestamped evidence directory, preferably `<demo-root>/dist/maestro-scale/<batch-id>/`, for each batch. Preserve:

- `run-plan.json` and materialized `run-inputs/`.
- `instances.jsonl` with one normalized record per start or lifecycle action.
- Sanitized raw CLI/API results under `logs/`.
- `summary.json` with requested, started, failed-to-start, and state counts.

Never store access tokens, cookies, credentials, private tenant URLs, or unredacted sensitive payloads. Keep UTC timestamps and stable process, version, job, run, and instance identifiers. Use the ledger schema in [references/runtime-contract.md](references/runtime-contract.md).

## Completion Gate

Report the approved target, plan parameters, tools and skills used, started instance IDs, lifecycle results, stop conditions reached, evidence paths, and any operation that fell back to Playwright. Distinguish successfully submitted starts from completed business outcomes.
