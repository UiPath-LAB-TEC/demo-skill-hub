# Enterprise Workbench Pattern

## Contents

- Mental Model
- Application Shell and Visual System
- Queue / Inbox
- Case Header
- Summary and Review
- Domain Detail and Terms
- Evidence / Documents
- Activity and Collaboration
- Disposition Flow
- Data Quality
- Demo Readiness Checklist

## Mental Model

Build a command center for human review. Let the user quickly determine what the case is, why it is prioritized, which evidence supports the recommendation, what remains unresolved, and which action to take.

Treat speed, clarity, trust, and control as the visual priorities. The interface should feel designed for repeated daily use, not arranged for a single screenshot.

## Application Shell and Visual System

Build a stable application shell before styling individual panels.

Include:

- A compact persistent top bar with product/workbench identity, current environment or business context when relevant, global search only when it works, and user/help controls.
- A clear page title and breadcrumb or back-to-queue path. Do not rely on browser Back as the only return path.
- A constrained content grid that uses widescreen space intentionally without leaving large decorative margins.
- Stable regions for queue controls, case header, tab navigation, content, and primary actions so selection and loading changes do not shift the page.

Use the host product's design tokens first. When no design system exists, use a restrained baseline:

- An 8 px spacing rhythm with compact 4 px adjustments.
- Low-radius surfaces, generally 4-8 px, with 1 px neutral borders and minimal shadow.
- Compact controls suitable for repeated work, while preserving accessible target sizes and focus rings.
- A small type scale with clear hierarchy: page title, section title, label, value, helper text. Do not use hero typography.
- One brand accent for primary action and active navigation; semantic status colors for success, attention, risk, and neutral state.
- Familiar icons from the installed icon library, with tooltips and accessible names for icon-only controls.

Avoid nested cards, decorative gradients, floating page sections, oversized KPI cards, and a different color for every status. Use full-width sections, dividers, tables, accordions, and split panes to organize dense information.

## Queue / Inbox

Use the queue for triage and workload management.

Include:

- Top analytics band only when operationally useful: open volume, ready/attractive count, needs review count, blocked/decline count, average age/SLA, or capacity risk.
- Default all-view with filters for priority/status. Do not force a narrow default filter unless the user's operating model requires it.
- Table rows with entity/request name, product/type, score/status, recommended posture, premium/value/amount if relevant, received/created date, and key blocker counts.
- Clean status language: `Ready`, `Needs review`, `Referral`, `Blocked`, `Closed`, or domain equivalents.
- Management affordances: search, status and priority filters, saved views when useful, visible sort, pagination or virtualized scrolling, and bulk actions only when the workflow truly supports them.
- A default sort that places the most urgent or valuable work first and remains understandable to the user.
- Row selection that is keyboard accessible, visually persistent, and reflected in the URL or workspace state when possible.
- Loading, empty, filtered-empty, error, and permission-limited states that preserve the table footprint and provide a valid next action.

Avoid:

- Owner fields unless ownership is real and meaningful.
- Placeholder people names.
- Debug badges, data-source caveats, or synthetic/demo disclaimers.
- Redundant tabs such as `All open` and `Needs decision` if they show effectively the same set.
- Dashboard charts that repeat what the table already communicates.
- Multiple unlabeled icon actions in each row. Prefer one row-opening action and an overflow menu for secondary commands.

## Case Header

Anchor the reviewer with the case header.

Include:

- Entity/customer/account name.
- Request type/product/coverage/service being reviewed.
- Requested amount/premium/value and effective/requested date where applicable.
- Score or recommendation tile with a clickable rationale popover.
- Confidence/readiness tile.
- Blockers/gaps/external checks tile with click-through details.
- Primary action button for disposition or next workflow step.
- Last updated or data-freshness context when a stale recommendation could change the decision.

Use compact metric tiles only for decision-critical values. Tiles can open popovers for scoring rationale, external checks, or gap details. Keep the page calm, and do not make non-interactive tiles look clickable.

## Summary Tab

Use this as the executive review surface.

Recommended layout:

1. Full-width automation/pre-audit summary across the top.
2. Two side-by-side panels under it: entity/company profile and request/coverage/terms summary.
3. Short evidence highlights and open questions only if they improve the decision.

The summary should answer: Who is this? What are they asking for? What did automation conclude? What should the human verify?

## Review Tab

Use this as the deeper adjudication surface.

Recommended layout:

- Full-width review brief first.
- Stacked full-width accordions for risk/appetite, gaps/conflicts, external checks, score rationale, and next steps.
- Keep recommended next steps in one place only. If the disposition panel repeats them, remove the duplicate section.
- Keep source-specific detail available but collapsed until needed.

Use this tab for reasoning, not raw extracted fields.

Separate sourced facts, deterministic rules, model interpretation, and unresolved questions. Show the recommendation as assistance with provenance and an override path, not as an unexplained AI verdict.

## Profile / Exposure Tab

Use this tab to explain the operating profile or business context.

Include domain-specific exposure fields such as operations, locations, receipts/revenue, payroll/headcount, states, subcontracting, safety controls, loss/incident history, or customer segment. Rename the tab for the domain if `Exposure` is not natural.

Make the copy factual and sourced. Avoid AI-sounding filler such as "comprehensive evaluation indicates". Prefer concrete statements like "Three-state footprint across TX, OK, and NM" or "$11.8M projected receipts."

## Terms / Request Tab

Use this tab for what the user is asking the business to approve, quote, fund, or process.

Include requested product/service, limits/amount, deductible/retention, effective date, target price/premium, expiring/current value, deadline, and source. Put this near the front of the app when it drives the decision.

## Evidence / Documents Tab

Establish credibility through visible, source-linked evidence.

Recommended layout:

- Document switcher as a top banner or compact horizontal list.
- Large document/PDF viewer on one side.
- Compact extracted fields on the other side.
- Editable extracted field values when the workflow includes human validation.
- Source labels, page numbers, confidence, and conflicts.

The reviewer should be able to click a document, see the PDF, and inspect the extracted fields without leaving the page. Avoid tiny PDF viewers and avoid a separate disconnected field table.

Keep the split pane usable: preserve a practical minimum width for both the source and extracted detail, make the divider adjustable when the framework supports it, and stack or switch views at narrower widths. Keep the selected document and page stable while fields are edited.

For an explicitly demo-only sample case, a real PDF may be replaced with a realistic generated or static fixture whose page references, source snippets, and extraction values match. Disclose to stakeholders outside the product UI that the case uses generated fixtures, and classify the result as `Demo-ready only`. In a production workflow, show an unavailable-source state and block evidence-dependent decisions instead of fabricating a document. Never show a blank viewer, broken download, unrelated placeholder image, or extraction table that cannot be tied back to visible evidence.

## Activity and Collaboration

Add activity only when the workflow includes handoffs, comments, follow-up, or audit requirements.

Include:

- A chronological history of meaningful business events, not raw system logs.
- Actor, action, timestamp, and status change for decisions and overrides.
- Notes, mentions, assignments, due dates, or requests for information when users genuinely collaborate in the workbench.
- Links from an event to the affected document, field, task, or disposition when possible.

Keep activity secondary to the decision workspace. Use a side panel, drawer, or focused tab rather than permanently compressing the main content.

## Disposition Flow

Close the loop with the disposition screen.

Include:

- Recommended action.
- Human decision.
- Agreement/override marker if relevant.
- Rationale field.
- Broker/customer response draft or internal note where applicable.
- Submit/complete action that updates the system status.
- Pending, success, and failed-write feedback that cannot be mistaken for a completed decision.

Ask only for fields that a real reviewer would own. Do not make them edit every automation result unless the business process requires validation.

Disable duplicate submission while pending. Confirm irreversible or externally visible actions. Preserve rationale through validation and failed writes, then update the case header and queue row after success.

## Data Quality

Do not let a polished UI depend on placeholder data.

For each case type, ensure:

- Scores, bands, recommendation, and rationale align.
- Counts match the visible blockers/gaps/triggers.
- Positive, referral, and decline cases tell meaningfully different stories.
- Source fields use real labels and values.
- Missing fields are either intentionally omitted, pre-populated for demo, or marked as backlog outside the UI.
- Currency, dates, capitalization, and business terminology are consistent.

## Demo Readiness Checklist

- Queue has enough records to feel alive.
- Records are varied but realistic.
- The top three rows are intentionally curated.
- At least one approve, one referral, and one decline case have complete data.
- Every visible tab has meaningful content for the showcased cases.
- Document/evidence view does not flash broken states or download instead of displaying.
- No `object Object`, null, undefined, placeholder owner, synthetic wording, or internal debug text appears.
- The story can be narrated in 3-5 minutes from queue to decision.
- Keyboard focus, active tab, selected row, and primary action remain visually clear.
- Loading, filtered-empty, error, failed-write, and completed states look intentional and do not shift the layout.
- Queue selection, tab switching, document switching, and disposition work at the primary demo width and a narrower laptop width.
- Any simulated persistence, authorization, data source, or integration limitation is described outside the product UI and is not represented as production-ready behavior.

For production readiness rather than demo readiness, apply every gate in `production-readiness.md`.
