---
name: uipath-se-demo-readiness
description: Use this skill to inspect, validate, rehearse, troubleshoot, and prepare an existing UiPath demo for presentation. It should review actual source artifacts, data, tests, scripts, packages, validation logs, and setup instructions when present. If the user asks to build or implement the demo from scratch, route to uipath-se-end-to-end-demo.
---

# UiPath SE Demo Readiness

Use this skill after a demo has files, deployed components, or a planned presentation. The goal is to prove the demo can be run live and that the presenter knows what is real, mocked, risky, and recoverable.

## Workflow

### 1. Inventory The Demo

Inspect the repo, solution folder, deployment notes, package versions, app folders, test data, and scripts before making claims.

Capture:

- Solution, orchestration, RPA, agent, app, IXP, connector, Data Fabric, queue, asset, and storage components.
- Tenant, folder, package names, process names, app names, and trigger entry points.
- Local and deployed test paths.
- Demo fixtures, sample documents, recipients, reset steps, and manual actions.
- Known mocked surfaces, gaps, or fragile dependencies.

## Artifact-Aware Readiness

When reviewing demo readiness, inspect actual artifacts when present:

- source files
- RPA projects
- agent definitions
- coded-agent files
- solution manifests
- Orchestrator resource definitions
- sample data
- fixtures
- tests
- scripts
- packages
- validation logs
- setup guides
- demo scripts

If the user asks to fix, prepare, or make the demo ready, update artifacts when appropriate instead of producing only a readiness checklist.

If the demo needs to be built from scratch or substantially implemented, route to `uipath-se-end-to-end-demo`.

### 2. Validate Locally And In Cloud

Use specialist skills and CLIs for the artifact type:

- `uipath-solution` for package and deployment lifecycle.
- `uipath-maestro-flow`, `uipath-maestro-case`, or `uipath-maestro-bpmn` for orchestration validation.
- `uipath-agents` for agent validation and evals.
- `uipath-rpa` for workflow validation and build.
- `uipath-coded-apps` for Action App build/test/deploy.
- `uipath-platform` for folder, package, process, job, asset, queue, and trace checks.
- `uipath-troubleshoot` when a validation or run fails.

Always run `npm test` after modifying JavaScript files.

Read `references/readiness-checklist.md` for command patterns and acceptance criteria.

### 3. Rehearse Primary Paths

Run the happy path and one exception path end to end. For demos with human review, leave at least one task open when the presenter needs to show the reviewer experience.

Capture:

- Scenario id and input payload.
- Process key, version, folder, and job id.
- Action Center task id.
- Reviewer decision used or left pending.
- Final business status.
- Outbound message or ticket evidence.
- Document preview evidence.
- Screenshots or logs needed for fallback.

Read `references/rehearsal-runbook.md` before a customer session.

### 4. Produce Readiness Report

Output:

- Ready or not-ready decision.
- What was validated.
- What still needs manual setup.
- Demo run order and reset steps.
- Known gaps and fallback talk track.
- Links or identifiers for tenant, folder, processes, jobs, apps, tasks, and artifacts.

## Quality Bar

Do:

- Report failed checks plainly.
- Distinguish local success from deployed success.
- Confirm outbound messages go only to approved recipients.
- Keep demo-grade simplicity; do not add production hardening unless required for the demo to run.

Do not:

- Complete human-review tasks by CLI unless the user explicitly asks.
- Mark a demo ready because files exist but deployed paths have not been exercised.
- Hide stale resources, wrong folder targets, old package versions, or connector binding issues.
