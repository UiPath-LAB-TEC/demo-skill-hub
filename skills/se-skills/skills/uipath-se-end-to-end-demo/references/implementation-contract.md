# Implementation Contract

Use this contract to turn an approved `uipath-se-end-to-end-demo` plan into runnable demo assets.

This contract is for build-oriented requests. It is incomplete unless at least one non-Markdown source, configuration, data, test, script, validation, package, or deployment-ready artifact is created or updated.

## Required Deliverables

Every implementation must produce or update:

- A solution folder with docs, orchestration, app, agent, RPA, data, tests, and deployment areas.
- Supporting README or runbook content that explains local run, fixture selection, test execution, and cloud deployment.
- Generic data contracts for the case or work item, scenario profile, evidence package, agent recommendation, human review decision, and downstream result.
- Three to five reusable scenario fixtures from the same organization/division.
- An orchestration artifact or simulation that coordinates trigger, source-system lookup, evidence gathering, agent analysis, human review, downstream submission, source-system update, and audit close.
- If the implementation creates a native UiPath Flow, Case, or BPMN project, that native artifact must be presenter-visible and non-empty: include business-labeled steps and edges/stages for the key sequence. A Flow with only a trigger, no edges, or no visible demo steps is a scaffold, not an implementation deliverable.
- A human review action app or task schema wired to the orchestration.
- Agent and RPA boundary definitions that use normalized inputs.
- Tests or test scripts for the reusable scenario matrix.
- Deployment notes covering solution assets and coded app assets separately.

## Scenario Configuration Model

The implementation must keep scenario values in data/config files. Include fields appropriate to the process, such as:

- Organization, division, region, team, and actor roles.
- Service line or work type.
- Item, procedure, request, or transaction code.
- Description, category, quantity/unit basis, period, dollar/risk basis, and modifiers.
- Payer, policy, provider, portal route, submission method, and follow-up SLA.
- Required documents, freshness rules, extraction fields, and evidence thresholds.
- Review rules, confidence thresholds, approval roles, exception types, and rework outcomes.

Implementation logic should consume this model. It should not branch on one sample payer, one sample code, one sample quantity, one sample portal route, or one sample customer/patient type.

## Standard End-to-End Flow

Adapt names to the use case, but preserve the business sequence:

1. Incoming transaction or report-change trigger.
2. Durable case/work item creation.
3. Source-system lookup by RPA.
4. Preliminary facts and evidence download.
5. IXP/IDP or document/evidence extraction when relevant.
6. AI Agent readiness analysis using scenario profile rules.
7. Optional agent tool call to RPA for missing information.
8. Human review action with summary, evidence, recommendation, and decision fields.
9. RPA/agent downstream submission.
10. Source-system update.
11. Audit, follow-up, close, or rework loop.

## Human Review Requirements

The action app or task must:

- Render from local fixtures and deployed `task.data`.
- Normalize inbound data before display.
- Default missing arrays to empty arrays.
- Default missing nested objects to safe placeholders.
- Emit a complete review decision payload.
- Preserve reviewer comments, missing information requests, and override reasons.
- Avoid auto-submit unless explicitly requested.

Required review decisions:

- Approve and submit.
- Request missing information.
- Route to alternate path, such as initial authorization or specialist review.
- Cancel or no longer needed, when relevant to the process.

## Reusable Test Matrix

Include at least three scenario tests. A strong matrix usually includes:

| Scenario type | Expected behavior |
|---|---|
| Ready renewal or ready transaction | Agent recommends submit; reviewer approves; downstream submission and source update complete. |
| Missing or stale evidence | Agent flags missing fields; reviewer requests documentation; case remains open. |
| Changed quantity, therapy, or scope | Agent routes to human review or alternate workflow; no hard-coded branch is required. |
| High-risk or high-dollar case | Agent recommends human review with risk reason; downstream action waits for review. |
| Portal or downstream exception | RPA captures exception; case routes to rework or follow-up. |

## Acceptance Criteria

- A new scenario from the same organization/division can be tested by editing fixture/config data only.
- The orchestration, agent, human review, RPA interface, and app structure remain unchanged across test scenarios.
- Native orchestration artifacts used in the demo have visible business labels and non-zero connectivity or stages; capture node/edge/stage counts in validation evidence.
- The action app is referenced by the human-review orchestration step.
- The reviewer can submit a decision and the downstream flow can continue from that decision.
- Local tests pass for at least three fixtures.
- At least one primary artifact exists outside Markdown.
- Any cloud deployment limitation is stated plainly.
