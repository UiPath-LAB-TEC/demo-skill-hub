# Validation Checklist

Use this checklist before calling a UiPath demo ready.

Use official UiPath product skills and `uip` command help as the canonical source for exact command syntax. This checklist names validation areas and evidence to capture; it does not replace product-specific instructions.

## Local Validation

Confirm the active authentication context, then run the applicable product validation, build, test, and packaging commands for the artifact types in the demo. Use official product skills and `uip <area> --help` to confirm syntax.

Only run JavaScript commands where JavaScript or TypeScript app code exists. Always run `npm test` after modifying JavaScript files.

For native orchestration artifacts, inspect the artifact content in addition to running product validation:

- Flow: verify more than a trigger-only scaffold, non-zero edges, and business-readable node labels for the advertised demo sequence.
- BPMN: verify lanes/tasks/gateways represent the advertised process, not an empty process shell.
- Case: verify stages, tasks, transitions, and review points exist for the advertised case lifecycle.
- Capture counts and labels in `dist/validation/` or `dist/logs/`.

For Action Apps with document viewers, test:

- Local fixture rendering.
- Deployed `task.data` normalization.
- Complete packet, incomplete packet, and exception-review modes.
- Missing or unavailable document messaging.
- Warning display for missing information, low confidence, urgency, or out-of-window choices.

## Solution Lifecycle

Prefer the existing solution and folder unless the user asks for a new deployment target.

Use `uipath-solution` and current `uip solution` help for resource refresh, pack, publish, upload, and deploy-prep commands. Inspect pack and deploy output for stale resources, wrong folders, old package versions, and connector binding errors.

## End-To-End Acceptance

For each primary branch, capture:

- Scenario id and source document or input.
- Started process key, version, folder, and job id.
- Action Center task id, if applicable.
- Human decision used.
- Final job state.
- Final business status or terminal node.
- Outbound message or ticket evidence.
- Document preview evidence.
- Entry point used, including manual stand-in triggers for event-driven paths.

Leave at least one Action Center task open when the user wants to interact with the app manually.

## Demo Rehearsal

Before presenting:

- Run happy path and one exception path in the deployed environment.
- Run every advertised entry point at least once.
- Confirm document previews render in Action Center.
- Confirm in-app copy does not expose mock or internal labels unless intentional.
- Confirm sample data is realistic and safe.
- Confirm outbound communications go only to demo-approved recipients.
- Prepare a reset plan and fallback talk track.
- Separate confirmed facts from directional volume or savings assumptions.
