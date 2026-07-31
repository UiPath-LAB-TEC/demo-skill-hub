---
name: uipath-se-discovery
description: Use this skill for UiPath sales-engineering discovery, current-state process mapping, pain analysis, qualification, stakeholder questions, and demo-shaping inputs. This is a discovery and planning skill. If the user asks to create a runnable demo, prototype, automation, agent, solution, package, deployment, or implementation, hand off to uipath-se-end-to-end-demo.
---

# UiPath SE Discovery

Use this skill before demo design when the source material is messy, conversational, or incomplete. The goal is to convert what the customer said into evidence-backed SE discovery that another SE or builder can trust.

## Workflow

### 1. Gather Evidence

Read source artifacts directly when files exist. Use transcripts, notes, emails, Teams messages, diagrams, screenshots, PDFs, sample documents, and existing repo artifacts.

Extract:

- Customer, division, industry, and business function.
- Personas, teams, reviewers, customers, patients, members, suppliers, or employees.
- Triggers, inputs, outputs, documents, messages, systems, portals, queues, and reports.
- Current process stages, handoffs, statuses, exceptions, delays, rework, approvals, and escalations.
- Pain points and business outcomes in the customer's words.
- Metrics stated by the customer: volume, frequency, staffing, SLA or KPI targets, AHT, backlog, exception or rework, savings, quality, revenue, and risk.
- Open questions, implied assumptions, and likely SME-review items.

Extract operational metrics before writing any summary. Do not turn a captured metric into a discovery question; ask only about values that are missing, ambiguous, or require validation.

Read `references/conversation-evidence.md` for extraction rules.

### 2. Map Current State

Create a concise current-state snapshot and as-is process map with:

- Start and end events.
- Actor lanes or responsibilities.
- Channels, systems, documents, records, queues, and messages.
- Systems and records touched.
- Decision points and exception paths.
- Controls, compliance points, bottlenecks, manual work, waiting time, rework, and approvals.
- Captured metrics and only unresolved metric questions.

Read `references/current-state-map.md` for the output contract.

### 3. Identify UiPath Opportunities

Map each business challenge to likely UiPath capability candidates:

- IXP or IDP for complex documents and extraction.
- Specialized AI Agents for reasoning, summarization, policy interpretation, prioritization, or recommendations.
- RPA or connectors for deterministic system work.
- Apps and human-in-the-loop for review, approval, correction, and exception handling.
- Maestro Flow, Case Management, or BPMN for orchestration.
- Data Fabric, queues, assets, or storage buckets for durable state and configuration.

Include strategic value themes and demo-worthy moments that map pains to UiPath capabilities without over-designing the future state. Do not design the full future state unless the user asks. Hand off to `uipath-se-end-to-end-demo` when discovery is ready for artifact-first demo design or build work.

## Handoff To Build Skill

Discovery artifacts are inputs to a future build, not the build itself.

This skill may produce discovery briefs, current-state maps, pain analysis, value hypotheses, qualification notes, and demo-shaping inputs.

When the user asks to turn discovery into a runnable demo, prototype, automation, agent, solution, package, deployment, or implementation, hand off to `uipath-se-end-to-end-demo`.

### 4. Produce The Discovery Brief

Output a brief that includes:

- Executive summary.
- Current-state snapshot and process.
- Evidence table with source references or transcript snippets.
- Operational metrics with value, unit, frequency, source phrase, confidence, and remaining questions.
- Pain points and impact, kept distinct from description and expected benefits.
- Candidate UiPath capability map.
- Strategic value themes.
- Demo-worthy moments.
- Data and document inventory.
- Open questions and assumptions.
- Recommended next skill: account research, demo design, solution planning, or executive artifacts.

Read `references/discovery-brief-contract.md` for the full output shape.

## Quality Bar

Do:

- Preserve customer terminology where it matters.
- Quote sparingly and only to anchor important evidence.
- Label facts, inferences, and assumptions separately.
- Return a best-fit process classification when source signals are strong, even if details are incomplete.
- When inputs are thin, still produce known facts, a lightweight classification, and prioritized clarification questions.
- Keep PHI, PII, credentials, and proprietary details out of reusable examples unless explicitly approved.

Do not:

- Invent process steps or business rules to make the demo prettier.
- Skip current-state mapping because the future state seems obvious.
- Fail only because taxonomy or context grounding is unavailable; use evidence and mark uncertainty.
- Repeat the same text as description, pain, impact, and expected benefits.
- Treat one anecdote as a universal rule unless the customer confirms it.
