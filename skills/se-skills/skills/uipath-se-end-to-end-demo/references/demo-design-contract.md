# Demo Design Contract

Use this structure when producing the end-to-end demo design.

Use this contract only for planning-only or design-stage requests. For build-oriented requests, use `artifact-first-build-contract.md` and create or update non-Markdown artifacts before producing supporting design documents.

## 1. Demo Header

- Demo title.
- Customer or industry.
- Division or team.
- Business process.
- Primary value proposition.
- Source artifacts reviewed.
- External research sources used.

## 2. Source-Derived Understanding

Separate facts from assumptions.

Facts should come from the user's artifact or cited research. Assumptions should be marked `[ASSUMPTION]`. Business gaps that need the customer should be marked `[SME REVIEW]`.

Capture:

- Trigger.
- Actors.
- Systems.
- Documents and data inputs.
- Decisions.
- Outputs.
- Exception paths.
- Current pain points.

## 3. As-Is Process

Describe the current process in 6 to 12 steps. Include handoffs, wait states, rework, and manual research.

## 4. Challenge-to-Technology Map

Use a table with these columns:

- Process challenge.
- Evidence from source.
- UiPath capability.
- Demo component.
- Expected business impact.

Always include rows for orchestration, RPA, AI Agent, and human-in-the-loop. Include IXP/IDP when the process involves documents or unstructured input.

## 5. Scenario Configuration Model

Define the configurable fields that let the same demo run multiple examples from the same organization or division.

Include:

- Organization, division, region, team, actor roles.
- Work type, service line, item/procedure code, item description, quantity or unit basis, requested period, risk/dollar category.
- Payer, payer profile, portal route, provider identity rules, submission method, status-check method, follow-up SLA.
- Required documents, document freshness rules, extraction fields, evidence thresholds.
- Review rules, confidence thresholds, approval role, exception type, rework outcome.

State which values are sample data and which are reusable logic. Do not let the demo depend on one fixed payer, code, quantity, patient type, or portal reference.

## 6. To-Be Architecture

Describe the target UiPath solution as a coordinated system:

- Orchestration layer and why it fits.
- Intake and document understanding.
- AI Agent responsibilities.
- RPA responsibilities.
- Human review experience.
- Data stores, queues, and integration points.
- Reporting or audit trail.

Use Mermaid when a diagram helps. Keep node labels business-readable.

## 7. Demo Artifact Inventory

List every artifact needed to build the demo.

Use this format:

| Artifact | UiPath product or skill | Responsibility | Inputs | Outputs | Demo status |
|---|---|---|---|---|---|

Demo status should be one of:

- Build.
- Mock for demo.
- Use existing.
- Optional.

## 8. Demo Storyboard

Write a presenter-ready sequence with 5 to 8 scenes.

Each scene should include:

- What the audience sees.
- What UiPath capability is being demonstrated.
- What business challenge it solves.
- The handoff to the next scene.

Include at least two visible "wow" moments, such as an agent explaining a recommendation, a document being classified and extracted, a human reviewer approving an exception, or orchestration resuming work automatically after review.

## 9. Reusable Demo Test Matrix

Provide 3 to 5 scenario examples from the same organization or division.

Use this format:

| Scenario | Config/data changes | Expected route | Capability demonstrated |
|---|---|---|---|

At least one scenario should be happy path, one should require human review, and one should trigger rework or an alternate route.

## 10. Data and Evidence Pack

Define the parameterized data needed:

- Scenario records.
- Example documents or document templates.
- Policy or guideline snippets.
- Portal or system records.
- Expected outputs.
- Human-review AppTask payload examples for local fixtures and deployed orchestration payloads.

Do not include real PHI, PII, credentials, or customer secrets. Use synthetic records for demos unless the user explicitly provides sanitized data. Sample records must be swappable without changing orchestration, agent, HITL, or RPA logic.

For coded action apps, require a normalization layer that accepts configured scenario fields and deployed task records even when labels, document lists, guidelines, or citations differ from local fixture field names.

## 11. Build Plan

Give a dependency-aware build plan.

Each task should name the specialist skill that owns it. Do not inline the specialist skill's internal instructions.

Recommended order:

1. Solution design and artifact decomposition.
2. Orchestration scaffold.
3. Agent.
4. Human review app or task.
5. RPA workflows.
6. Platform resources and deployment.
7. Testing and demo rehearsal.

## 12. Validation and Rehearsal Checklist

Include:

- Build or validation commands where known.
- End-to-end happy path.
- One exception path.
- Human review path.
- Human review app referenced correctly by the orchestration step.
- Real Action Center task creation, assignment, app rendering, and manual reviewer submission.
- Reset steps for repeated demos.
- Known demo assumptions.

## 13. Acceptance Criteria

Include criteria proving the same orchestration, agent, human review experience, and RPA structure can run multiple examples by changing configuration or data only.

At minimum:

- No hard-coded payer, item/procedure code, quantity, patient type, portal reference, or document bundle in reusable logic.
- At least three synthetic scenarios from the same organization or division pass through the demo.
- Scenario-specific differences are visible in the agent recommendation, human review context, RPA inputs, and case audit trail.
- The deployed AppTask can render the orchestration payload and complete through the human review app without changing the app for each scenario.
- Manual-review tests leave the task pending for the user unless the user explicitly asks Codex to submit the review.
