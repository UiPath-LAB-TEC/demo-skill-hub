---
name: uipath-bpmn-to-flow-conversion
description: "Use when converting existing UiPath Maestro BPMN / Process Orchestration demos into UiPath Maestro Flow demos, especially for Sales Engineer demo migration where the goal is a close 1:1 conversion that reuses existing RPA, API workflow, connector, and AI agent resources. Covers agent inline-conversion decisions and HITL/action-app conversion to Flow-native quick forms or coded action apps."
---

# UiPath BPMN To Maestro Flow Conversion

Convert an existing UiPath Maestro BPMN demo into an equivalent UiPath Maestro Flow demo. The default target is a close 1:1 replica: preserve the business process, sequencing, input/output contract, node intent, dependencies, and demo behavior unless the user explicitly asks for a redesign.

This skill is for Sales Engineers converting existing UiPath BPMN demos to Flow. Keep the implementation demo-grade and composable. Do not add production hardening unless it is required for the demo to work.

## Required Skill Routing

Before making claims or changes, use the relevant UiPath skills:

- Use `uipath-maestro-bpmn` to inspect source BPMN, project layout, variables, entry points, bindings, diagrams, and referenced resources.
- Use `uipath-maestro-flow` to author, validate, upload, publish, deploy, or diagnose the target Flow.
- Use `uipath-human-in-the-loop` when converting Action Center, HITL, or action-app steps into Flow-native human tasks.
- Use `uipath-coded-apps` only when the user chooses a coded action app path.
- Use `uipath-platform` when checking tenant auth, folder targets, packages, published resources, connectors, connections, or deployment state.

Verify against the actual repo, generated metadata, installed CLI behavior, and current auth target. Do not invent resource availability or CLI syntax.

## Conversion Defaults

Map BPMN to Flow as directly as possible:

- Preserve the source process name, intent, milestone order, and demo story.
- Preserve input/output names and payload shapes where practical.
- Preserve variable names unless Flow requires a compatible adjustment.
- Preserve existing RPA/API/connector/agent calls as resource invocations when those resources exist.
- Preserve gateway decisions, script logic, retries, escalations, and terminal outcomes when Flow supports them.
- Keep node names recognizable so the BPMN and Flow can be compared side by side.
- Prefer simple Flow-native nodes over custom code when they express the same behavior.
- Do not add new business steps, integrations, policy rules, or production controls unless needed for the converted demo to run.

Resource reuse order:

1. Inspect the local solution and BPMN metadata.
2. Search the tenant registry when auth and folder context are available.
3. Reuse existing published or same-solution resources when found.
4. Ask before mocking, replacing, or creating missing resources.

## Required Clarification Gates

Ask only for missing information that blocks a faithful conversion.

Agent conversion:

- Ask whether existing BPMN AI agent calls should remain external resource calls or whether any should be converted into inline Flow agents.
- Default: keep agents as existing external resources for the closest 1:1 conversion.
- Create inline agents only when the user explicitly chooses that path.

HITL/action-app conversion:

- For each BPMN human task, Action Center step, or low-code action app, ask whether it should become a Flow-native quick form or a coded action app.
- Default: use a Flow-native quick form when the app is simple data review, approval, or correction.
- Do not attempt to directly replicate BPMN Action Center or action-app internals as-is.

Coded action app path:

- If the user chooses coded action app, ask for an image file, screenshot, or export of the existing low-code action app UI to replicate.
- Ask which UiPath folder should receive the published and deployed coded action app.
- Offer to build the coded action app with `uipath-coded-apps`, then publish and deploy it to the selected folder.

Resource binding:

- If a referenced RPA process, API workflow, connector, or agent cannot be found locally or in the tenant, ask whether to mock it, create a placeholder, or stop for the missing resource.

## Workflow

1. Inspect the source BPMN project.
   - Identify the entry point, trigger, variables, input/output contract, ordered process steps, referenced resources, human tasks, action apps, and unsupported or ambiguous BPMN features.

2. Produce a concise conversion plan.
   - Include BPMN node to Flow node mapping, resources to reuse, resources to create/mock/bind, agent conversion decisions, HITL/action-app decisions, validation commands, and deployment target if applicable.

3. Ask required clarification questions.
   - Ask only the questions needed to proceed.
   - If the repo or user request already answers a question, state the assumption and move forward.

4. Build the Flow.
   - Create or update the Flow project in the correct solution layout.
   - Add Flow nodes and edges that match the BPMN process.
   - Bind existing resources after local and tenant discovery.
   - Convert human work to quick forms or coded action apps according to the user choice.
   - Add inline agents only when explicitly requested.
   - Keep generated artifacts and package metadata consistent with CLI guidance.

5. Validate.
   - Run relevant local validation commands.
   - Report results clearly.
   - Do not run debug or deployed process execution unless the user explicitly approves real side effects.

6. Upload, publish, or deploy only when requested.
   - Verify current auth target first.
   - Confirm target tenant and folder.
   - Return Studio Web URL, published package, deployed process, or coded action app deployment details as applicable.

## Completion Contract

The conversion is complete only when:

- the target `.flow` exists in a valid UiPath solution layout
- the Flow represents the BPMN process as a close 1:1 demo conversion
- referenced RPA/API/connector/agent resources are bound, intentionally mocked, or listed as unresolved blockers
- BPMN human tasks/action apps are converted to Flow-native quick forms or coded action apps according to user choice
- local validation has been run and the result is reported
- requested upload, publish, or deployment is complete and the resulting URL or deployment target is reported

## Response Contract

Return:

- conversion summary
- decisions made and assumptions used
- unresolved blockers, if any
- validation commands and results
- files changed
- Studio Web, package, process, or coded action app deployment links when applicable
