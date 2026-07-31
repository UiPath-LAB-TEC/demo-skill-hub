---
name: uipath-se
description: Use this skill as the top-level UiPath sales-engineering router for account research, discovery, demo build, demo readiness, and executive artifact requests. Route build, implement, scaffold, runnable demo, prototype, package, deploy, validate, automation, agent, solution, generate solution, or end-to-end demo requests to uipath-se-end-to-end-demo. Do not satisfy build-oriented requests with generic Markdown.
---

# UiPath SE Router

Use this skill to route UiPath sales-engineering requests to the narrowest specialist skill.

## Routing Rule

This skill is a sales-engineering router. It should not directly satisfy build-oriented requests with generic Markdown.

Route requests as follows:

- Account research, account hypotheses, buyer context, discovery prep, prepare questions, or demo idea: use `uipath-se-account-research`.
- Discovery notes, current-state process, pain mapping, qualification, summarize a customer conversation, or summarize discovery evidence: use `uipath-se-discovery`.
- Build, implement, scaffold, create runnable demo, create prototype, package, deploy, validate, create solution, generate solution, create automation, create agent, or end-to-end demo: use `uipath-se-end-to-end-demo`.
- Demo validation, rehearsal, troubleshooting, readiness review: use `uipath-se-demo-readiness`.
- Slides, executive one-pagers, executive summary, talk tracks, talk track only, value summaries, demo scripts: use `uipath-se-executive-artifacts`.

For any build-oriented request, `uipath-se-end-to-end-demo` is the canonical owning skill.

## Operating Rules

- Keep research and discovery outputs as planning inputs unless the user explicitly asks for build work.
- Treat the UiPath CLI (`uip`) and official UiPath product skills as required dependencies for implementation, validation, packaging, publishing, deployment, and troubleshooting.
- If a build request also needs executive materials, complete or coordinate artifact-first build work before executive artifacts replace or summarize it.
- If live tenant actions are blocked, identify the blocker as authorization, tenant, folder, credential, permission, target-selection, approval, or governance related.
