---
name: uipath-se-account-research
description: Use this skill for UiPath sales-engineering account research, buyer context, account hypotheses, discovery preparation, demo hooks, opportunity-specific research summaries, and artifact-backed research packs.
---

# UiPath SE Account Research

Use this skill to enrich SE discovery with current, sourced context. Research should improve demo relevance, not replace customer evidence.

## Workflow

### 1. Define Research Scope

Identify:

- Organization and relevant division or business unit.
- Industry and process area.
- Geography, customer segment, or operational context.
- Known systems, documents, channels, or partner ecosystem.
- Demo or sales motion this research should support.

If the organization, division, or process area is current or likely to have changed, browse current sources and cite them.

### 2. Research With Source Discipline

Prefer:

- Company websites, annual reports, investor materials, public filings, press releases, and official product/service pages.
- Government, regulator, payer, provider, industry association, or standards-body sources.
- Credible industry publications for market context.

Avoid weak sourcing for specific claims. Use news and blogs only when they add useful current context.

Separate externally sourced facts from process hypotheses. Do not infer internal volumes, staffing, SLAs, system usage, or business rules from industry context; list those as operational metrics to validate in discovery.

Read `references/source-policy.md` before producing customer-facing research.

### 3. Build The Account Brief

Produce:

- Account snapshot.
- Division or operating-unit context.
- Industry perspective relevant to the process area.
- Best-fit process classification when source signals are strong, even if details are incomplete.
- Relevant process and business terminology.
- Likely systems, channels, documents, and data sources.
- Operational pain hypotheses.
- Likely operational metrics to validate, not invented customer-specific volumes or staffing.
- Strategic value themes that can feed an executive brief.
- UiPath relevance map across orchestration, IXP, Specialized AI Agents, RPA, Apps, Integration Service, Data Fabric, and platform operations.
- Discovery questions to validate assumptions.
- Demo hooks and proof points.
- Cited source list.

Read `references/account-research-contract.md` for the output shape.

## Standalone Artifact Behavior

This skill may produce research summaries, account hypotheses, demo hooks, and discovery questions.

When the user asks for artifacts, create account-research artifacts such as source registries, account profiles, hypothesis registers, relevance maps, discovery-question banks, validation scripts, sample research data, and tests. Do not convert the request into a demo build unless the user explicitly asks for a separate demo-building skill in a later turn.

It must not claim to have built a runnable demo, automation, agent, or solution package unless the produced artifacts actually provide that runtime surface.

### 4. Route The Research Output

Route the result:

- Into the user's current workspace as source-backed research artifacts when they request files or local artifacts.
- Into concise written findings when they request a brief, meeting prep, or discovery prep.
- Into customer-facing slide, one-pager, or talk-track inputs when they ask for executive artifact content.

## Quality Bar

Do:

- Separate externally verified facts from sales hypotheses.
- Label source confidence for important external claims.
- Use exact dates for time-sensitive findings.
- Cite sources in customer-facing outputs.
- Produce lightweight classification, known facts, and prioritized discovery questions even when account context is thin.
- Keep research concise enough for an SE to use before a meeting.

Do not:

- Claim internal systems, volumes, staffing, or process rules unless the customer or a source supports them.
- Fail only because taxonomy or customer-specific context is unavailable; mark assumptions and continue with best-fit research.
- Over-index on generic industry trends when customer-specific context is available.
