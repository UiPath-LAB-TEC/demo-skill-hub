---
name: uipath-reference-solution-planner
description: "Plan a new UiPath demo from an existing Studio Web solution reference. Use when the user wants to base a new use case on a known-good UiPath demo, provides or needs to provide a solution ID, asks to download/export and inspect a UiPath solution, or needs detailed SPEC.md and PLAN.md artifacts plus exact builder kickoff instructions. Produces planning artifacts only; do not build, upload, publish, or deploy the target demo."
metadata:
  author: "James Dickson"
  version: "1.0.0"
  ownerEmail: "jms.dcksn88@gmail.com"
  changeSummary: "Added marketplace metadata for the existing reference solution planning skill."
  isBreaking: false
  category: "Sales Engineering"
  tags:
    - uipath
    - studio-web
    - solution
    - planning
    - demo
  platforms:
    - OpenAI
    - UiPath Automations
  businessUseCases:
    - "Plan new UiPath demos from existing Studio Web reference solutions"
---

# UiPath Reference Solution Planner

Use an existing UiPath Studio Web solution as the reference for a new demo use case. Download the reference solution, inspect its artifacts deeply, interview the user from evidence, then write build-ready `SPEC.md` and `PLAN.md` files that another AI can implement with the relevant UiPath specialist skills.

This is a planning workflow. Do not create or modify the target demo artifacts unless the user explicitly moves from planning into build work.

## Required Skill Routing

Before running UiPath commands or making claims:

- Use `uipath-solution` for solution download/export behavior and solution lifecycle constraints.
- Use `uipath-platform` for login status, tenant/folder context, Orchestrator resources, Integration Service connections, and other live platform checks.
- Use artifact-specific skills after inspection: `uipath-maestro-flow`, `uipath-maestro-bpmn`, `uipath-rpa`, `uipath-agents`, `uipath-coded-apps`, `uipath-api-workflow`, `uipath-maestro-case`, `uipath-data-fabric`, `uipath-human-in-the-loop`, and others as needed.

Verify against the actual repo, generated metadata, installed CLI behavior, and current auth target. Do not invent resource availability, IDs, connector names, or CLI syntax.

## Workflow

1. Clarify only the download blockers.
   - If no solution ID is provided, ask for the Studio Web solution ID before doing anything else.
   - If the target local folder is ambiguous, default to `reference-solutions/<solution-id-or-slug>/` under the current repo and state that assumption.
   - Do not run a full requirements interview before inspecting the reference solution. The question list must be informed by the actual downloaded artifacts.

2. Download and extract the reference solution.
   - Check auth first:

```bash
uip login status --output json
```

   - Probe the solution CLI surface before solution commands:

```bash
uip solution init --help --output json
```

   - Download and extract:

```bash
uip solution download "$SOLUTION_ID" -d ./reference-solutions -n "$REFERENCE_SLUG" --extract --output json
```

   - If the CLI returns only a `.uis` archive, unzip it into the reference folder and record the archive path and extracted path.
   - Never publish, deploy, upload, activate, or mutate the cloud solution in this planning workflow.

3. Inspect the solution before interviewing.
   - Read `references/solution-inspection-checklist.md`.
   - Inventory every artifact, resource, binding, data contract, AI prompt, human review step, UI surface, trigger, fixture, and validation clue.
   - Map what can be reused, what must be renamed or adapted, and what must be newly created for the new use case.
   - Use specialist UiPath skills based on detected artifacts before drawing conclusions.

4. Ask evidence-based clarification questions.
   - Ask only after reference inspection, except for the solution ID and local download blockers.
   - Include a recommended answer for each question.
   - Cover target use case, audience, demo story, reuse boundaries, inputs/outputs, systems, mock-vs-real integrations, AI responsibilities, HITL/UI choices, tenant/folder expectations, validation, and deployment scope.
   - If a question blocks a buildable spec, stop for the answer. If it is non-blocking, label the assumed default in the spec.

5. Produce the planning artifacts.
   - Read `references/planning-output-contract.md`.
   - Write `SPEC.md` as the build contract.
   - Write `PLAN.md` as the implementation sequence another AI should follow.
   - Include a final response with exact kickoff steps for the builder AI.

## Planning Rules

- Treat the reference solution as "what good looks like," not as a source to blindly copy.
- Preserve proven demo patterns, story beats, validation approach, and artifact composition when they still serve the new use case.
- Do not copy tenant-specific IDs, credentials, user emails, generated binding IDs, connection IDs, or environment-specific URLs into reusable instructions.
- Prefer the smallest demo-grade artifact set that carries the new story.
- Clearly separate verified facts from assumptions and open questions.
- Make the builder's next action obvious without requiring the builder to rediscover the reference solution from scratch.

## Completion Contract

The planning run is complete only when:

- the reference solution has been downloaded and extracted locally, or the download blocker is clearly reported
- the extracted solution has been inventoried across artifacts, resources, bindings, data, AI, HITL, UI, validation, and deployment expectations
- the user has answered required clarifying questions, or unresolved blockers are listed explicitly
- `SPEC.md` and `PLAN.md` exist and name the relevant UiPath specialist skills for the builder
- the final response tells the user exactly how to start the build with another AI
