---
name: enterprise-workbench-ui
description: Build, refine, and review production-quality enterprise workbench and system-of-work UIs. Use for operational apps with a queue or inbox, case or record workspace, evidence or documents, AI-assisted recommendations, human decisioning, workload analytics, disposition and writeback, or a production-readiness assessment. Apply across domains where labels and data change but the interaction pattern must remain accessible, responsive, credible, and professional.
---

# Enterprise Workbench UI

## Purpose

Build enterprise workbench UIs that behave like real systems of work. Preserve the domain's vocabulary, data model, design system, and framework conventions. Apply the reusable layout pattern only where it serves the workflow: operational queue, focused case workspace, progressive detail, evidence-first review, and explicit human disposition.

## Core Workflow

1. Identify the operational roles, their most common task, the decision they own, and the evidence required to defend it.
2. Inventory the real data and actions. Separate available, derived, pending, unavailable, and writeback fields before designing the screen.
3. Shape the app around a queue/inbox for prioritization and a case workspace for adjudication. Add workload analytics only when they change triage or staffing decisions.
4. Put the most important decision context above the fold: entity, request, status, urgency or SLA, recommendation, confidence, blockers, and primary action.
5. Use progressive disclosure. A strong starting order is `Summary`, `Review`, domain detail, `Evidence/Documents`, and `Disposition`; rename, combine, or omit tabs based on the workflow.
6. Pair automation output with source evidence, freshness, and unresolved gaps. Make AI assistance inspectable and overridable instead of presenting it as authority.
7. Implement the complete path from queue selection through decision, validation, persistence or writeback, and visible status update.
8. Exercise loading, empty, filtered-empty, partial-data, error, permission, success, and repeat-submission states.
9. Run the app, inspect it in a browser, and iterate from screenshots before calling it ready.

## Screen Pattern

- Read `references/workbench-pattern.md` for the reusable information architecture, visual system, queue, workspace, evidence, and disposition patterns.
- Read `references/production-readiness.md` whenever implementing, reviewing, or declaring a workbench production-ready. It defines interaction, accessibility, responsive, state, security, and verification gates.

## Design Rules

- Make it an operational app, not a landing page.
- Reuse the product's existing component library, tokens, icons, and interaction conventions before adding custom styling.
- Use a restrained enterprise palette with one brand accent, neutral surfaces, and status colors only where they communicate state. Never rely on color alone.
- Favor dense but breathable layouts: compact panels, tables, tabs, accordions, and side-by-side evidence panes. Avoid decorative card grids and nested cards.
- Avoid placeholder language, audit/debug commentary, synthetic-data labels, and internal implementation notes in the UI.
- Use validated real data or explicitly isolated demo fixtures. Keep fixtures internally identifiable and separate from production records; never imply that simulated checks or writebacks occurred.
- Put explanation behind interactions where possible: clickable score/status tiles, info icons, popovers, and expandable sections.
- Use consistent typography. Avoid random bold text, mixed casing, and one-off font sizes.
- Format business data correctly: use the record's currency and the user's locale, show an ISO currency code when the symbol is ambiguous, omit unnecessary timestamps, include percentage units, and use consistent label casing.
- Preserve layout dimensions while data loads or changes so tables, viewers, tabs, and headers do not jump.
- Keep one clear primary action per decision state. Place secondary actions near the content they affect and destructive actions behind confirmation.

## Validation

Before calling the UI ready:

- Walk through the queue as a manager: can they understand workload, priority, and filtering in under 30 seconds?
- Walk through one case as a reviewer: can they understand the entity, request, recommendation, evidence, open concerns, and next action without hunting?
- Open a good case, a referral case, and a decline/blocked case. Confirm the screens tell different stories.
- Inspect the documents/evidence view. Confirm source documents and extracted fields are visible together and the user can switch documents without layout jump.
- Omit unavailable fields only when they are not required by the workflow or decision. Render decision-relevant missing fields with an explicit unavailable state, impact, and recovery action.
- Run the project's build, typecheck, lint, and relevant tests. Do not hide failed checks.
- Inspect the primary workflow in a real browser at the target widescreen and narrower laptop widths. Add tablet/mobile coverage when those viewports are in scope.
- Capture and inspect screenshots of the queue, a normal case, a referral/blocked case, the evidence view, and the disposition result.
- Check keyboard navigation, visible focus, text overflow, contrast, zoom, table semantics, dialog focus, and screen-reader labels for icon-only controls.
- Confirm refresh, deep-link, duplicate-submit, failed-write, and permission-denied behavior do not lose work or create misleading state.
- Use the full release gate in `references/production-readiness.md`; unresolved blockers mean the UI is not production-ready.
