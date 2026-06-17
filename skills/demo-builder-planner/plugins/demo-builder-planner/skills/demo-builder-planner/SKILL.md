---
name: demo-builder-planner
description: "Create demo-grade SPEC.md files for UiPath demos across any UiPath artifact surface. Use when the user asks to design, scope, propose, or specify a UiPath demo; provides a customer/account name; provides a use-case brief; or mentions UiPath demo artifacts such as Maestro Flow, BPMN, RPA, agents, coded apps, API workflows, case management, Data Fabric, human review, platform resources, or solution packaging. Produces a SPEC.md only, not implementation artifacts or handoff prompts."
metadata:
  author: "James Dickson"
  version: "1.0.0"
  ownerEmail: "jms.dcksn88@gmail.com"
  changeSummary: "Added marketplace metadata for the existing UiPath demo SPEC builder skill."
  isBreaking: false
  category: "Sales Engineering"
  tags:
    - uipath
    - demo
    - spec
    - presales
    - planner
  platforms:
    - Claude
    - OpenAI
    - UiPath Automations
  businessUseCases:
    - "Create build-ready SPEC.md files for UiPath demo artifacts"
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch, AskUserQuestion, Agent
---

# UiPath Demo SPEC Builder

Turn rough UiPath demo ideas into a precise `SPEC.md` that another AI can use to build the demo artifacts.

Only write the demo specification. Do not create Flow, BPMN, RPA, agent, app, case, API workflow, fixture, platform, solution, or deployment artifacts.

## Not For

- Building demos.
- Production automation design.
- Writing PDDs or full enterprise SDDs.
- Creating implementation task lists, `/goal` prompts, or agent handoff prompts.
- Running existing automations unless the user explicitly asks to debug or run them.

## Inputs

Ideal:

- Use case title and one-paragraph business goal.
- Industry/domain.
- Known UiPath products, systems, connectors, documents, user roles, and tenant/folder constraints.
- Happy path and one exception path.
- Must-show demo moments or capabilities.

Minimum:

- Customer/account name or vague use case. Research then propose 2-3 demo options before writing `SPEC.md`.

## Workflow

1. Ideate: turn a vague brief into 2-3 demo options.
2. Route: read `references/uipath-demo-artifact-map.md` and map the demo requirements to the relevant UiPath artifact surfaces and specialist skills.
3. Interview: IMPORTANT - ask the user targeted questions about any ambiguous requirement to get the details needed to make the spec buildable. Include a recommended answer for each question.
4. Specify: write `SPEC.md` as the authoritative build contract.
5. Check: run `references/spec-quality-checklist.md` before finalizing.

Research the use case with web searches to frame your understanding of the use case, industry, artifact selection, and system choices.

Write from the perspective of the builder who will use the UiPath specialist skills. Do not assume unspecified tenant/folder targets, connector availability, real system access, deployment scope, or artifact type.

Keep the spec simple and demo-grade. Prefer the smallest set of artifacts that clearly illustrates the concept. Add complexity only when it makes the demo stronger or the user explicitly asks for it.

## Interview (MUST DO)

**IMPORTANT**: You must conduct an interview with the user to ensure your thinking, your research and any assumptions about the build are aligned with what the user wants. DO NOT proceed with SPEC.md without clarifying details with the user first. Ask questions about absolutely any ambiguous aspect of the specification or demo requirements.  After you have informed yourself and have a mental model of what needs to be built - interview the user to get mutual agreement on all details necessary to create a tight SPEC.md to build the demo.

The interview must confirm:

- demo scope, audience, and industry context
- input/output contract
- happy path and one exception path
- selected UiPath artifact surfaces and specialist skills
- systems of record, mock-vs-real integration choices, connectors, and test data
- AI, document extraction, or agent responsibilities when applicable
- human review, Action Center, coded app, or task behavior when applicable
- UI and visual presentation requirements when applicable
- platform resources, deployment, solution packaging, and tenant/folder expectations when applicable
- validation expectations

For each question you ask, provide your best recommendation based on your research, the UiPath skills and the user's original request.

When human review is in scope and the task type is unclear, recommend the simplest option that fits:

- Native Flow/HITL quick form for simple approve/reject, missing-field capture, or lightweight data correction (only applicable for Maestro Flow demos)
- Coded action app when the review needs a richer UI, document preview, complex correction controls, or reusable Action Center experience.
- Complete coded process app for a full user experience to manage the flow or case system. Coded Process Apps are most often used with Case Management demos.

## Artifact Routing

Use `references/uipath-demo-artifact-map.md` before finalizing product selection. The spec must name the specialist UiPath skill another AI should open for each artifact or resource.

Common choices:

- Maestro Flow for visual orchestration, connector nodes, Flow tools, inline agents, and simple human checkpoints.
- BPMN or Case Management for process/case stories with stages, milestones, long-running work, or operational governance.
- RPA when the demo must operate desktop/web apps, documents, Excel, email, queues, or legacy systems.
- Agents when reasoning, tool use, natural language interaction, or autonomous decisioning is the featured component.
- Coded Apps or Coded Action Apps when the demo needs a user-facing web UI or rich review screen.
- API Workflows when the demo needs a reusable API-first workflow or explicit HTTP/connector activity composition.
- Data Fabric, queues, assets, buckets, Integration Service connections, Test Manager, or Solution packaging only when those resources support the demo story or validation.

Mock external systems by default for demo clarity unless the user requests real connectors, APIs, tenant resources, or existing assets.

## Outputs

- Write `SPEC.md`.
- Do not write `TIGHTEN-SPEC-PROMPT.md`.
- Do not write `CODEX-GOAL-PROMPT.md`.
- Do not write `/goal` prompts or generic implementation prompts.
- Add supporting files only when the user explicitly asks for them.

Do not write `DEMO-BUILD-PLAN.md`.

`SPEC.md` must include:

- title, one-line demo promise, business goal, audience, and domain context
- demo story, must-show moments, happy path, and exception path
- assumptions, explicit non-goals, and open questions or blockers
- artifact inventory: artifact name/path, UiPath surface, owning specialist skill, purpose, inputs, outputs, and dependencies
- selected UiPath skill routing and why each skill is needed
- end-to-end process shape: stages, steps, handoffs, routing, and responsibility boundaries
- input contract, output contract, and ready-to-paste sample inputs
- data model, fixtures, expected outputs, and mock-vs-real integration contracts
- AI, agent, document extraction, or HITL contracts when applicable
- UI/visual presentation requirements when applicable
- platform resources, deployment, packaging, tenant/folder, and connection assumptions when applicable
- validation checklist with concrete commands or evidence another AI can use
- build order at a high level, without turning the spec into a task runner prompt

Before finalizing, use `references/spec-quality-checklist.md`.
