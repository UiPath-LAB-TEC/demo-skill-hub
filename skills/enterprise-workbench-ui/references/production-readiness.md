# Production Readiness Contract

Use this contract when implementing, reviewing, or declaring an enterprise workbench ready. Treat every `Must` item as a release gate unless the product's explicit requirements exclude it.

## Contents

- Product and workflow contract
- Interaction and state contract
- Accessibility and responsive contract
- Data, AI, and security contract
- Agent execution protocol
- Verification contract
- Release verdict

## Product and Workflow Contract

Must:

- Define each role's default landing surface, primary task, decision authority, and escalation path.
- Make the queue's default sort and filters match the operating model, not arbitrary sample-data order.
- Provide a complete path from queue selection to final disposition and visible queue/status update.
- Preserve user-entered rationale and edits across validation errors and recoverable request failures.
- Distinguish saved, submitted, pending, failed, and stale states with plain language.
- Keep audit-relevant facts such as actor, action, timestamp, source, prior value, and override reason available to the workflow even when they are not all prominent on screen.

Should:

- Support deep links to a case or task when the host platform permits it.
- Preserve useful queue state such as search, filters, sort, page, and selected record when navigating back.
- Show workload analytics only when they support prioritization, capacity, SLA, or exception management.

## Interaction and State Contract

Implement and verify these states for every data-heavy surface:

- Initial loading: use a stable skeleton or loader without collapsing the previous layout.
- Empty: explain what is empty and provide the next valid action when one exists.
- Filtered empty: state that no records match and provide `Clear filters`.
- Partial data: show available facts, identify unavailable sections, and preserve usable actions.
- Error: use plain language, retain user work, and provide retry or recovery where valid.
- Permission denied: explain the access boundary without leaking restricted data.
- Success: confirm the completed action and reflect the new status in the header and queue.
- Stale or concurrent update: prevent silent overwrite; refresh or ask the user to reconcile.
- Superseded request: cancel stale reads or ignore responses that no longer match the active case, document, or filter state.

For actions:

- Use one primary action for the current decision state.
- Disable or make submissions idempotent while a write is pending.
- Validate close to the field and provide an error summary for long forms.
- Confirm destructive, irreversible, or externally visible actions with the consequence and record identity.
- Keep dialogs focused, keyboard-operable, dismissible when safe, and returned to the invoking control on close.
- Announce asynchronous success and failure through accessible status messaging, not color alone.
- Track dirty state and preserve a recoverable draft where supported. Warn before row switches, back navigation, refresh, session expiry, or close would discard edits.

## Accessibility and Responsive Contract

Target WCAG 2.2 AA and the host design system's accessibility contract.

Must:

- Use semantic headings, landmarks, tables, forms, buttons, links, tabs, and dialogs.
- Provide accessible names for icon-only controls and visible labels for business inputs.
- Support keyboard operation with logical focus order and a visible focus indicator.
- Implement tabs with `tablist`, `tab`, and `tabpanel` semantics plus arrow-key navigation.
- Give tables a descriptive name, scoped headers, announced sort state, and accessible row actions.
- Maintain at least 4.5:1 text contrast and 3:1 meaningful non-text contrast unless a valid WCAG exception applies.
- Avoid communicating status, priority, confidence, or validation by color alone.
- Allow text wrapping and zoom without clipping controls, hiding content, or requiring two-dimensional page scrolling.

Verify at the product's supported widths. When unspecified, inspect at least:

- 1440 x 900 for the primary enterprise workflow.
- 1280 x 800 for a narrower laptop.
- 1024 x 768 to identify stacking, tab overflow, and table pressure.

At narrower widths, preserve decision context and actions before secondary analytics. Stack evidence panes or provide an explicit document/details switcher rather than shrinking either pane below usability.

## Data, AI, and Security Contract

Must:

- Render business fields from typed or validated data. Never expose raw objects, null, undefined, stack traces, internal IDs without meaning, or unsanitized markup.
- Apply locale-aware date, time, currency, number, and percentage formatting consistently.
- Show source, page or location, retrieval time or freshness, and confidence when these affect a recommendation.
- Separate sourced facts, deterministic rules, model-generated interpretation, and unresolved questions.
- Allow an authorized human to override an AI recommendation and capture the rationale.
- Never invent evidence, document content, completed checks, or writeback success.
- Enforce authorization and field visibility in the service/data layer; hidden controls are not access control.
- Avoid placing secrets, unnecessary personal data, or restricted document content in logs, URLs, analytics events, or client-side fixtures.

Apply the document availability and demo-fixture rule in `workbench-pattern.md`. Any generated source fixture limits the verdict to `Demo-ready only`; a production workflow must block evidence-dependent decisions when the source is unavailable.

When an AI agent or assistant is part of the workbench, verify capability and context parity:

- Map the records the user can inspect and the actions they can take to the agent's authorized read and write tools.
- Give the agent the same current case, document, identity, permissions, and workflow state needed for the task; do not rely on hidden screen context.
- Use primitive, inspectable tools whose inputs and outputs identify the affected record and action.
- Return the updated record state or an actionable error after every mutation so the UI and agent cannot silently diverge.
- Preserve the same authorization, audit, provenance, confirmation, and override rules for human-initiated and agent-initiated actions.

## Agent Execution Protocol

Before implementation or review, the acting agent must:

1. Read applicable repository guidance and inspect package scripts, framework configuration, and existing component-library usage.
2. Identify the real and simulated data sources, write paths, authorization boundaries, supported viewports, and target runtime.
3. Select the repository's existing build, test, server, and browser tooling. Do not invent a parallel harness when a working path exists.
4. Start or locate the local/deployed target and record the exact URL used for verification.
5. Exercise the required scenarios in a real browser, recording screenshot paths and relevant console or failed-network evidence.
6. Report every command and check that materially supports the verdict, along with pass/fail status.
7. Mark unavailable tools, fixtures, permissions, environments, or scenarios as skipped with a reason. A skipped `Must` gate prevents a `Production-ready` verdict.

The final verification report must include:

- Target URL and viewport set.
- Build, typecheck, lint, test, and browser-check results.
- Scenarios exercised and screenshot or artifact paths.
- Console errors and unexplained failed requests, or an explicit statement that none were observed.
- Simulated dependencies and skipped gates.
- Final verdict with blocking items.

## Verification Contract

Before release:

1. Run the app using its normal local or deployed path.
2. Run build, typecheck, lint, unit, integration, and end-to-end checks that exist for the changed surface.
3. Walk the primary path from queue to disposition using realistic data.
4. Verify at least one normal, referral/exception, blocked/decline, empty, loading, failed-write, and permission-limited scenario.
5. Test keyboard-only operation through queue controls, tabs, evidence, form fields, dialogs, and disposition.
6. Inspect browser console and network failures; resolve application errors and unexplained failed requests.
7. Capture screenshots at primary and narrower widths for queue, case summary, evidence/documents, validation error, and completed disposition.
8. Compare screenshots for clipping, overflow, layout shifts, inconsistent spacing, weak hierarchy, empty regions, accidental nested cards, and competing primary actions.
9. Refresh and deep-link into a case. Confirm the selected record and persisted state remain accurate.
10. Submit twice, simulate a slow response, and simulate a failed response. Confirm no duplicate action, silent data loss, or false success.
11. Verify authorization with at least two roles against the deployed or production-equivalent service. Request a forbidden case, restricted evidence field, and prohibited write directly; confirm the service returns the appropriate denial without restricted payload, then confirm the authorized role still works.
12. Open the same case in two authenticated sessions. Save a change in session A, submit a conflicting change in session B, and confirm B receives a conflict/reconciliation path with its draft retained, no silent overwrite, and an auditable final record.
13. After disposition, reload in a fresh session or query the supported read API. Confirm the server-backed status, rationale, actor, timestamp, prior value or override reason, and queue row match the completed action.
14. Render untrusted document names, extracted values, source snippets, and model output containing markup-like content. Confirm it remains inert text and does not leak into logs, URLs, analytics, or executable DOM sinks.
15. Run the repository's automated accessibility checks when available, then manually verify keyboard focus, names, tab navigation, table sort announcements, asynchronous status announcements, contrast, and 200 percent zoom at supported widths.
16. Rapidly switch cases and documents while introducing delayed, out-of-order responses. Confirm stale responses cannot replace the active record or its evidence.
17. Edit a disposition or evidence field, then switch rows, navigate back, refresh, expire the session, and close the surface. Confirm the user is warned or the recoverable draft is restored according to the host platform's policy.

## Release Verdict

- `Production-ready`: all Must gates pass; supported workflows and failure states are verified in the browser.
- `Demo-ready only`: the polished primary story works, but persistence, authorization, accessibility, failure recovery, or full state coverage remains simulated or incomplete.
- `Not ready`: the primary path breaks, data or evidence is misleading, actions can duplicate or lose work, restricted content can leak, or required browser verification has not occurred.

Report the verdict explicitly. Do not use `production-ready` as a synonym for visually polished.
