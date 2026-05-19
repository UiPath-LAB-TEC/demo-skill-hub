# Spec Quality Checklist

Use this before finalizing `SPEC.md`.

- The spec is demo-grade and avoids production hardening unless required for the demo to run.
- The user has chosen agent mode: inline Flow agents, coded agents, low-code agents, or mixed.
- System-of-record interactions default to mock script nodes that create deterministic payloads unless the user explicitly requested real API Workflow artifacts or existing API Workflow references.
- If human review is in scope, the user has chosen native Maestro Flow quick form review or coded action app review.
- If coded action app review is selected, the spec requires a separately built, published, and folder-deployed coded action app that the Flow references by published resource. It is not added as a Studio Web solution project.
- Studio Web upload is either explicitly requested or explicitly out of scope.
- The spec defines business goal, audience, demo story, happy path, exception path, and non-goals.
- The Flow section defines solution shape, node sequence, routing, start input contract, output contract, and sample manual-start input.
- Agent responsibilities, inputs, output schema, and examples are clear.
- Mock script payloads, connectors, native Flow nodes, and explicitly requested API Workflows have concrete contracts.
- Human review is included only when it improves judgment, approval, missing-information, or data-quality handling.
- Visual Flow design is specified: clean layout, readable groups, sticky note zones, varied note colors, and no overlapping nodes.
- Fixtures include at least one happy path and one exception path with expected final outputs.
- Validation checks are measurable and do not depend on subjective visual inspection as a hard completion gate.
- No requirement depends on an unverified capability unless it is labeled as an assumption or blocker.
