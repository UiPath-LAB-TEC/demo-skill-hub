---
name: uipath-bpmn-to-flow-conversion
description: "Use when converting existing UiPath Maestro BPMN / Process Orchestration demos into UiPath Maestro Flow demos, especially for Sales Engineer demo migration where the goal is a close 1:1 conversion that reuses existing RPA, API workflow, connector, and AI agent resources. Requires explicit user choices for agent representation and HITL/action-app conversion before planning or building those parts."
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

Nested BPMN process calls:

- If a BPMN node calls another BPMN process that is part of the same source solution, convert that called BPMN process into its own Flow in the target solution.
- The parent Flow must invoke the converted child Flow with a Flow node, preserving the original BPMN call contract.
- If a BPMN node calls an external BPMN process outside the source solution, do not convert that external process by default.
- For external BPMN process calls, keep the node contract as-is and represent it with a Flow node that calls the external BPMN process.

## Required Clarification Gates

Do not treat agent representation or HITL/action-app representation as implementation details. They are required user-choice gates because they change the target Flow shape, validation work, and demo handoff.

Before producing a final conversion plan or making Flow changes, ask the user to choose an approach whenever the BPMN contains AI agent calls, human tasks, Action Center steps, or action apps. Do this even when one option looks like the closest 1:1 conversion.

If a required choice is unanswered, stop after asking the question. Do not continue with a recommended default, assumed preference, or provisional plan for that surface.

Agent conversion:

- If the BPMN contains AI agent calls, ask whether each agent should remain an external resource call or be converted into an inline Flow agent.
- Do not default to external resource calls solely because they are more faithful to the BPMN.
- Do not create inline agents unless the user chooses that path.
- If the user has already specified an agent approach in the prompt or repo-local spec, restate that choice and proceed.

HITL/action-app conversion:

- For each BPMN human task, Action Center step, or low-code action app, ask whether it should become a Flow-native quick form, a coded action app, or a placeholder/manual handoff.
- Do not default to a quick form solely because the task is simple review, approval, or correction.
- Do not directly replicate BPMN Action Center or low-code action-app internals unless the user chooses a coded action app path and provides enough UI/schema evidence.
- If the user has already specified the HITL approach in the prompt or repo-local spec, restate that choice and proceed.

Other blockers:

- Ask only for other missing information that blocks a faithful conversion.

Coded action app path:

- If the user chooses coded action app, ask for an image file, screenshot, or export of the existing low-code action app UI to replicate.
- Ask which UiPath folder should receive the published and deployed coded action app.
- Offer to build the coded action app with `uipath-coded-apps`, then publish and deploy it to the selected folder.

Resource binding:

- If a referenced RPA process, API workflow, connector, agent, or external BPMN process cannot be found locally or in the tenant, ask whether to mock it, create a placeholder, or stop for the missing resource.

## Workflow

1. Inspect the source BPMN project.
   - Identify the entry point, trigger, variables, input/output contract, ordered process steps, nested or external BPMN process calls, referenced resources, human tasks, action apps, and unsupported or ambiguous BPMN features.

2. Ask required clarification questions.
   - Ask the agent and HITL/action-app choice questions before finalizing the plan or building.
   - Ask only the other questions needed to proceed.
   - If the repo or user request already answers a question, state the assumption and move forward.

3. Produce a concise conversion plan.
   - Include BPMN node to Flow node mapping, same-solution BPMN processes to convert into child Flows, external BPMN process calls to preserve as call nodes, resources to reuse, resources to create/mock/bind, confirmed agent conversion decisions, confirmed HITL/action-app decisions, validation commands, and deployment target if applicable.

4. Build the Flow.
   - Create or update the Flow project in the correct solution layout.
   - Add Flow nodes and edges that match the BPMN process.
   - Convert same-solution BPMN subprocesses into separate Flows and call them from the parent Flow with Flow nodes.
   - Preserve external BPMN process calls as Flow nodes that keep the original call contract.
   - Bind existing resources after local and tenant discovery.
   - Convert human work to quick forms, coded action apps, or placeholder/manual handoffs according to the user choice.
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
- same-solution BPMN process calls are converted into child Flows and invoked by Flow nodes
- external BPMN process calls remain explicit call nodes with the original contract preserved
- referenced RPA/API/connector/agent resources are bound, intentionally mocked, or listed as unresolved blockers
- BPMN human tasks/action apps are converted to Flow-native quick forms, coded action apps, or placeholder/manual handoffs according to user choice
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
