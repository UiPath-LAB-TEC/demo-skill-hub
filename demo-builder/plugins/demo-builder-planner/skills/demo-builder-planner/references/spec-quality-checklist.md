# Spec Quality Checklist

Use this before finalizing `SPEC.md`.

- The spec is demo-grade and avoids production hardening unless required for the demo to run.
- The spec defines the business goal, audience, demo story, must-show moments, happy path, exception path, and non-goals.
- Every planned artifact has a UiPath surface, owning specialist skill, purpose, inputs, outputs, dependencies, and validation evidence.
- Product selection is justified and does not default to Maestro Flow unless Flow is the best fit.
- The spec uses the smallest artifact set that can deliver the demo story.
- Mock-vs-real integration choices are explicit. Mocked systems include deterministic payloads and expected responses.
- Real connectors, tenant resources, folders, assets, queues, buckets, Data Fabric entities, packages, and deployment targets are listed as assumptions unless verified.
- Agents, AI prompts, IXP/document extraction, and HITL steps include clear responsibilities, input fields, output schema, and example outputs when applicable.
- UI, coded app, Action Center, Flow, BPMN, or case-management presentation requirements are concrete enough for another AI to build.
- Fixtures include at least one happy path and one exception path with expected final outputs.
- Validation checks are measurable and name the relevant artifact or skill surface.
- No requirement depends on an unverified capability unless it is labeled as an assumption or blocker.
- The file stands alone as the build contract and does not require `TIGHTEN-SPEC-PROMPT.md`, `CODEX-GOAL-PROMPT.md`, `/goal`, or a separate implementation prompt.
