---
name: uipath-se-end-to-end-demo
description: Use this skill when the user asks to build, implement, scaffold, package, validate, deploy, generate solution artifacts, or prepare a runnable end-to-end UiPath presales demo, customer prototype, demo workspace, or solution showcase. This is an artifact-first sales-engineering orchestration skill. It must create or update local UiPath artifacts, sample data, configuration, tests, validation outputs, and package/deployment-ready files. It must use the official UiPath product skills and UiPath CLI as required dependencies for product-specific implementation. Do not satisfy build-oriented requests with Markdown-only planning, analysis, or design documents.
---

# UiPath SE End-To-End Demo

Use this skill to turn real customer process context into a credible, reusable UiPath demo. The outcome should be a scenario-driven framework that an SE can present, rehearse, modify, and eventually connect to live systems.

This is the canonical build skill for UiPath sales-engineering demo work.

## Required Contract For Build-Oriented Requests

For any build-oriented request, read and follow `references/artifact-first-build-contract.md`.

This skill is successful only when it creates or updates executable, buildable, package-ready, or deployable UiPath demo artifacts on disk.

Do not satisfy build-oriented requests with Markdown-only planning, analysis, architecture, checklists, implementation plans, or demo scripts.

Use official UiPath product skills and the UiPath CLI (`uip`) as required dependencies for product-specific implementation.

If a live operation is blocked, keep building local artifacts and describe the blocker as authorization, tenant, folder, credential, permission, target-selection, approval, or governance related.

## Operating Modes

Start by choosing the narrowest mode that satisfies the request.

- **Discovery/design**: produce the narrative, current-state map, capability map, target architecture, artifact inventory, scenario model, build plan, and validation plan when the request is planning-only.
- **Implementation**: build or update runnable local and cloud-ready source, configuration, sample data, fixtures, tests, validation output, and package-ready structures from an approved plan or clear target process.
- **Demo readiness**: validate local and deployed paths, verify Action Center/HITL behavior, record run steps, and prepare rehearsal evidence from actual artifacts.
- **Executive artifacts**: create concise customer-facing slides, talk tracks, value story, demo storyline, and decision-oriented summaries after build artifacts exist or when the user asks only for documents.

If the user asks to build, implement, scaffold, make a runnable demo, upgrade a demo, package, deploy, validate, create a solution, generate solution artifacts, create automation, create an agent, or gives a target project folder, proceed beyond design and create non-Markdown artifacts. If intent is unclear and the request lacks build-oriented language, use discovery/design first.

## Required Inputs

Proceed when the user provides at least one of:

- A business-process description.
- A call transcript, discovery note, PDD, SDD, diagram, screenshot, whiteboard capture, sample document, or customer artifact.
- A target organization, industry, division, and process name.
- A target solution folder or existing repo to upgrade.

If the target use case, source artifact, or target folder is missing and cannot be inferred from repo context, ask before writing code. If a source artifact exists as a file, read it directly and ground the design or implementation in that evidence.

## Core Principles

- Build reusable demos, not one hard-coded transcript path.
- Separate reusable process logic from scenario data and fixtures.
- Use the right UiPath product for each job: orchestration for coordination, IXP/IDP for complex inputs, AI Agents for reasoning, RPA for deterministic system work, Action Apps/HITL for review, and Data Fabric/queues/assets for state and configuration.
- Keep demo-grade implementations simple and credible. Avoid production hardening unless required for the demo to run.
- Label facts, assumptions, mocked surfaces, SME-review items, and unsupported claims.
- Inspect actual repo files, generated metadata, installed CLI behavior, current auth target, and deployment folder before making claims.

## Workflow

### 1. Ground The Demo

Read source artifacts before designing or changing files. Capture:

- Triggering events and intake channels.
- Users, customers, patients, members, employees, reviewers, and systems.
- Business states, decisions, handoffs, delays, exceptions, approvals, and compliance needs.
- Documents, messages, forms, attachments, portals, queues, and fields.
- Current-state pain and future-state operating model.
- Measurable anchors such as volume, SLA, effort, backlog, rework, conversion, quality, or risk.
- The top two or three branches that must work live, plus visible mock branches for v1.

Research the industry, account, division, or process when current external context would materially improve the demo. Use credible sources and cite them in customer-facing outputs.

If the process naturally has two stages, split it into separate event-driven orchestrations instead of forcing one long flow. Use a manual trigger as a rehearsal stand-in when the real event source is unavailable.

### 2. Map Work To UiPath Capabilities

Assign responsibilities deliberately:

- **Orchestration**: Case Management, Maestro Flow, or BPMN for state, routing, retries, SLAs, auditability, and invoking the right capability at the right step.
- **IXP/IDP/document understanding**: classification, extraction, confidence, missing fields, and evidence completeness for forms, PDFs, faxes, emails, notes, or screenshots.
- **AI Agents**: summarization, prioritization, recommendations, policy interpretation, exception reasoning, case comparison, and next-best-action.
- **RPA**: deterministic source-system work, portal entry, file handling, downloads/uploads, status checks, and record updates.
- **Human-in-the-loop**: Action Apps, tasks, validation station, approval gates, exception review, corrections, and reviewer decisions.
- **Data layer**: Data Fabric, queues, assets, storage buckets, or fixture files for cases, scenarios, logs, documents, and configuration.
- **Connectors**: Outlook, Teams, SharePoint, EHR, CRM, ERP, ticketing, third-party systems, or explicit mocked equivalents.

Every end-to-end demo should include orchestration, an AI Agent, RPA, and human review. Include IXP/IDP when the process has meaningful document, email, fax, screenshot, clinical-note, or unstructured-input work. If IXP/IDP is not central, explicitly explain the alternate intake pattern.

Read `references/capability-blueprint.md` when choosing capability boundaries.

### 3. Define Scenario Contracts

Define data contracts before building UI, prompts, RPA, or orchestration branches. Keep local fixtures and deployed payloads compatible, especially Action Center `task.data`.

At minimum define:

- Intake or case record.
- Work item or line detail.
- Payer, policy, customer, provider, site, or rules profile.
- Document or evidence package.
- Extraction output.
- Agent recommendation.
- RPA lookup/submission/update result.
- Review task payload and `ReviewDecision`.
- Outbound communication and final status/audit event.

Treat payer, service line, item/procedure code, quantity, route, portal path, required documents, SLA, exception type, and review outcome as data/configuration. Do not make prompts, screens, selectors, workflows, or branches depend on one fixed example unless it is clearly marked as sample fixture data.

Read `references/scenario-contracts.md` for payload patterns and `references/action-app-handoff-checklist.md` before wiring or debugging a human review Action App.

### 4. Design The Demo

For design-only requests, produce:

- Demo title and one-sentence value proposition.
- Source summary with facts, assumptions, and SME-review gaps.
- Industry/account/division context.
- As-is process and pain points.
- To-be UiPath architecture.
- Capability map across orchestration, IXP/IDP, AI Agent, RPA, HITL, data, and connectors.
- Scenario configuration model and reusable test matrix with at least three scenario examples from the same organization or division.
- Artifact inventory for every solution/app/agent/workflow/process/data asset.
- Presenter storyline with scenes, visible proof moments, and rehearsal beats.
- Exception paths and human-review moments.
- Build plan with specialist skill handoffs.
- Validation plan and demo rehearsal checklist.
- Customer-facing value story with modeled benefits and labeled assumptions.

Read `references/demo-design-contract.md` for the full output shape.

### 5. Implement In UiPath Order

When implementing, preserve the approved design unless repo evidence or CLI behavior contradicts it. Open specialist UiPath skills before editing their owned assets.

Use the official product skills as the implementation layer. Do not copy their command syntax or detailed product instructions into this skill; inspect their current guidance and `uip` help for the selected artifact type.

Preferred order:

1. `uipath-solution` for solution shell, resources, package lifecycle, and SDD-ready structure.
2. `uipath-data-fabric`, queues, assets, or fixture files for the data layer.
3. `uipath-rpa` for deterministic workflows and normalized RPA interfaces.
4. `uipath-agents` for AI Agent prompts, tools, schemas, evaluation, and deployment.
5. `uipath-coded-apps` and `uipath-human-in-the-loop` for Action Apps, task schemas, and reviewer decisions.
6. `uipath-maestro-flow`, `uipath-maestro-case`, or `uipath-maestro-bpmn` for orchestration.
7. `uipath-platform` for Integration Service, Orchestrator, folders, packages, assets, processes, jobs, and traces.
8. `uipath-test`, `uipath-review`, and `uipath-troubleshoot` for validation, review, and fault isolation.

If a native Flow, Case, or BPMN project is created as a demo artifact, do not leave it as a validated empty scaffold. Add visible, business-labeled orchestration steps and edges that mirror the scenario sequence, even when live systems are represented by mock or script stand-ins. A valid Flow with only a trigger and no edges does not satisfy the orchestration deliverable; either wire the native canvas or explicitly omit the native orchestration project and use a non-native simulation artifact instead.

Keep upgrades in the existing solution folder unless the user asks for a new solution. When a folder already contains assets, inspect first and make additive, scoped changes.

Read `references/implementation-contract.md` for required implementation deliverables.

### 6. Build Mock-First, Replaceable Components

Use controlled mocks when external systems, live calendars, IXP projects, EHRs, portals, payer systems, or customer APIs are unavailable. Make each mock explicit and replaceable by contract.

Good mock-first patterns:

- Generate safe sample documents and fixture JSON.
- Mock IXP with stable classification and extraction payloads.
- Mock tool-backed AI Agent calls for policy, eligibility, inventory, risk, availability, or routing lookup.
- Mock RPA integrations with clear input and output payloads.
- Route outbound messages to approved demo recipients only.
- Store documents where the Action App can display them, such as storage bucket references, attachment URLs, or fixture fallback paths.

### 7. Make The Demo Legible

Design for both the viewer and the presenter:

- Add business-readable labels and descriptions to orchestration nodes.
- Verify native orchestration canvases are not empty: they must contain visible business steps, edges, and labels for intake, lookup/extraction, agent analysis, human review, downstream update, and close when those capabilities are in scope.
- Make at least two branches runnable to final states.
- Show optional branches as visible, honest mockups when they are not fully functional.
- Make the Action App look like the customer process, not a generic form.
- Include document preview, extracted data, confidence, AI rationale, decision controls, reviewer notes, warnings, and outbound preview in one coherent experience.
- Put warnings near the affected evidence or decision.
- Separate AI recommendations from deterministic RPA system tasks.
- Use realistic statuses and terminology from the source artifact or customer process.

Read `references/artifact-inventory.md` before declaring the demo designed or ready to build.

### 8. Validate And Rehearse

Run local validations before packaging. Then run deployed end-to-end cases through Action Center when the demo includes human review and the user has confirmed the tenant, folder, credential, permission, and live action target.

Minimum proof:

- Flow, Case, BPMN, Agent, RPA, and Action App validations pass for the artifacts used.
- JavaScript tests pass after Action App changes.
- At least two primary branches complete from intake to final state.
- Human-review tasks render real deployed payloads, including documents.
- Reviewer decisions, not CLI shortcuts, resume downstream orchestration unless the user explicitly asks to auto-complete tasks.
- Outbound communication goes only to approved demo recipients.
- Test data, manual run steps, fixture reset steps, and presenter beats are recorded.

Read `references/validation-checklist.md` for validation evidence and acceptance criteria.

## Completion Gate For Build Requests

Before final response on any build-oriented request:

- Verify at least one non-Markdown artifact was created or updated.
- Verify source, configuration, data, tests, scripts, package-ready files, validation logs, or command outputs exist in the workspace.
- If a native Flow, Case, or BPMN artifact is included, inspect it before final response and verify it is not just a scaffold. Capture node/edge or stage counts, visible labels, and validation output.
- Capture important validation, packaging, or inspection output under `dist/validation/`, `dist/packages/`, or `dist/logs/` when the demo workspace uses that structure.
- List concrete files and directories changed, UiPath capability areas or product skills used, `uip` commands run, validation or package results, how to run or inspect the demo, and any blocked live operations.

If no non-Markdown artifact exists for a build-oriented request, continue building instead of answering.

## Quality Bar

Do:

- Ground every design or build claim in source artifacts, repo state, CLI output, or clearly labeled assumptions.
- Choose Case Management, Maestro Flow, or BPMN by process fit rather than defaulting to Flow.
- Design for at least three scenario examples and implement at least two runnable end-to-end branches when building.
- Make native orchestration artifacts presenter-visible; do not rely on sidecar contracts or local scripts while the Flow/BPMN/Case canvas remains empty.
- Normalize deployed Action Center payloads and local fixtures before rendering Action Apps.
- Validate document preview and warning states in deployed review tasks, not only local app preview.
- Leave manual review tasks pending when the user wants to test the reviewer experience.

Do not:

- Create generic slideware with no build path.
- Collapse all work into one bot, agent, app, or flow.
- Hard-code one sample into prompts, flows, UI state, or orchestration branch conditions.
- Invent business rules, selectors, portal fields, payer policies, or customer policies.
- Hide failed validation, stale resources, wrong-folder deployment, or connector limitations.
- Report cloud deployment complete when only local files were created.
