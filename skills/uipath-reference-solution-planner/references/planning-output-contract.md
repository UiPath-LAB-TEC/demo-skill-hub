# Planning Output Contract

Write `SPEC.md` and `PLAN.md` in the working directory for the new demo plan. They must stand alone for another AI builder.

## SPEC.md

Include:

- title, one-line demo promise, target use case, audience, and business goal
- reference solution summary: source solution ID, extracted path, artifact inventory, and reusable demo pattern
- explicit assumptions and open blockers
- non-goals and scope boundaries
- happy path and one exception path
- must-show demo moments
- artifact inventory for the target demo: path/name, UiPath surface, owning specialist skill, purpose, inputs, outputs, dependencies, reuse decision, and validation evidence
- artifact-by-artifact mapping from reference to target: reuse, adapt, replace, create, or drop
- input contract, output contract, and ready-to-paste sample payloads or records
- data model and fixture requirements
- AI, agent, IXP/document extraction, prompt, or evaluation contracts when applicable
- human review, Action Center, coded app, or UI contracts when applicable
- Integration Service, Data Fabric, queue, asset, bucket, folder, package, trigger, or connection assumptions when applicable
- validation checklist with concrete local commands or evidence the builder can produce
- deployment or Studio Web upload expectations, if in scope

## PLAN.md

Include:

- build phases in dependency order
- exact specialist skills to open in each phase
- files or folders the builder is expected to create or modify
- live tenant checks the builder must perform before binding resources
- fixture creation and seed-data steps
- validation commands and expected evidence per phase
- blockers that should stop implementation
- decisions already made and assumptions the builder may use without re-asking

Keep the plan implementation-oriented, but do not build the target artifacts during this skill run.

## Final Builder Kickoff Instructions

End with exact steps the user can follow. Tailor paths and filenames to the actual run:

```text
1. Open a fresh AI coding-agent session in <target-demo-repo>.
2. Tell it: "Read SPEC.md and PLAN.md first. Use the UiPath specialist skills named in PLAN.md. Build the demo exactly to this contract, verifying uip login status and CLI behavior before any live UiPath commands. Stop for the blockers listed in SPEC.md before making assumptions."
3. Point it at the extracted reference solution at <reference-solution-path> for comparison only.
4. After implementation, ask it to run the validation checklist in SPEC.md and summarize files changed, validation evidence, and any live-tenant gaps.
```

If the user wants a reusable handoff file, put these steps in `PLAN.md` under `Builder Kickoff`.
