# Capability Blueprint

Use this reference when choosing which UiPath capability should own each part of a demo.

## Capability Map

| Need | Preferred capability | Demo evidence |
|---|---|---|
| Intake from email, fax, form, portal, or API | Connector, RPA, Integration Service, trigger, or mock intake | Multiple intake examples and stable intake payload |
| Classify documents or messages | IXP, IDP, or mock IXP contract | Document class, confidence, missing docs, field confidence |
| Extract structured data | IXP, IDP, forms, OCR, or mock extractor | Extracted field payload and raw extraction JSON |
| Summarize, reason, recommend, prioritize | AI Agent | Summary, rationale, next action, tool results, evidence |
| Query or update systems of record | RPA or connector | Deterministic output and audit log |
| Check availability, eligibility, policy, or status | AI Agent with tool, RPA, connector, or mock service | Tool payload plus recommendation rationale |
| Human correction or approval | Action App or task | Reviewer decision, notes, corrections, approval |
| Reviewer needs source evidence | Action App document viewer plus storage/attachment contract | Document renders locally and in deployed task |
| Reviewer decision changes communication | Action App decision model plus draft generation | Draft message updates when reviewer changes decision |
| Durable work tracking | Data Fabric, queue, Case Management, or process variables | Status history and case record |
| Long-running case with owners and SLAs | Case Management | Stage, owner, SLA, exception path |
| Defined service-like orchestration | Maestro Flow | Node graph, branch conditions, reusable flow inputs |
| Formal cross-team process | BPMN | Lanes, gateways, events, business-readable model |
| Outbound next step | Outlook, Teams, SharePoint, ticketing, or mock communication | Sent message, ticket id, or draft preview |

## Branch Design

Build at least two runnable branches:

- Happy path: complete input, high confidence, approval or straight-through processing, outbound confirmation.
- Exception path: missing information, low confidence, authorization required, escalation, or cancellation.
- Delayed-response path: model a later external response as a second flow, case stage, or event-driven branch.

Name entry points after the real world even when the implementation uses controlled manual payloads for rehearsal.

## AI Agent Versus RPA Rule

Use AI Agents for interpretation, tradeoff reasoning, summarization, prioritization, and recommendations.

Use RPA for deterministic system work: open a system, download a file, query a record, upload an attachment, update a field, send a structured transaction, or run repeatable UI/API steps.

Use both when needed: RPA gathers facts, the AI Agent reasons over them, and RPA applies an approved deterministic update.
