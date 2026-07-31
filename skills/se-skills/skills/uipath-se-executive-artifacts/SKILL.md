---
name: uipath-se-executive-artifacts
description: Use this skill to create UiPath sales-engineering executive artifacts such as one-pagers, slide outlines, value summaries, executive summaries, demo scripts, talk tracks, talk-track-only outputs, and customer-facing summaries. This skill is document-focused and must not be used to satisfy build, implementation, package, deploy, runnable demo, automation, agent, or solution requests without the artifact-first demo build skill.
---

# UiPath SE Executive Artifacts

Use this skill to turn SE discovery and demo work into customer-ready communication. The output should explain the business problem, UiPath perspective, future-state solution, demo proof, and value story without exposing internal build noise.

## Boundary From Build Work

This skill creates executive-facing documents such as one-pagers, slide outlines, talk tracks, value summaries, and demo scripts.

It must not be used to satisfy build, implementation, package, deployment, runnable demo, automation, agent, or solution requests by creating executive documents only.

When a request includes both implementation and executive artifacts, the build must be handled by `uipath-se-end-to-end-demo` first or in parallel. Executive artifacts should describe actual built or planned artifacts and should not replace the build.

## Workflow

### 1. Ground The Artifact

Read available source material:

- Discovery brief, transcript, account research, process map, or SDD.
- Demo design, artifact inventory, scenario matrix, and validation report.
- Screenshots, run logs, Action App views, orchestration diagrams, and sample documents.
- Existing slides or customer formatting guidance when provided.

Separate customer-confirmed facts from assumptions and directional estimates.

### 2. Choose Artifact Type

Use the right format:

- Executive brief for account teams or senior stakeholders.
- Slide deck or single-slide PowerPoint for discovery readout, demo setup, post-demo recap, or executive explainer.
- One-pager for leave-behind value summary.
- Architecture diagram for technical buyers.
- Demo script for presenter handoff.
- Current-state/future-state artifact for process alignment.

If the user asks for a slide, deck, PowerPoint, PPT, PPTX, or presentation-ready slide, use the `presentations` skill and create an actual editable `.pptx`. Markdown may be produced as source notes, talk track, or backup, but it is not sufficient as the slide deliverable unless the user explicitly asks for Markdown only.

Use the `presentations` skill for PowerPoint slides/decks, `documents` for Word-style briefs, and `spreadsheets` for quantified tables when needed.

### 3. Tell The SE Story

Cover:

- Customer context and business challenge.
- Current-state process and pain.
- UiPath future-state architecture.
- Capability map: orchestration, IXP or IDP, AI Agents, RPA, Apps/HITL, integrations, data layer, platform operations.
- Demo storyline with scenes and visible proof.
- Modeled outcomes, assumptions, and what would need validation.
- What is real, mocked, deployed, or future integration.
- Recommended next steps.

Read `references/artifact-contracts.md` for output shapes.

### 4. Make It Presentation-Ready

Use concise language, realistic customer terminology, and simple diagrams. Do not over-explain implementation details unless the audience is technical.

For PowerPoint slides/decks:

- Put the business challenge before the architecture.
- Use one capability map slide.
- Use one current-state/future-state slide.
- Use one demo storyline slide.
- Use appendix slides for build details, assumptions, and validation evidence.
- Export an editable `.pptx` and render or generate a preview image for QA when tooling permits.
- Inspect the preview for readable text, no clipping, and no overlaps before final response.
- In the final response, include the `.pptx` path, preview path if created, and any rendering/QA limitations.

Read `references/slide-story-patterns.md` for deck patterns.

## Quality Bar

Do:

- Keep artifacts concise and customer-safe.
- Cite external research when used.
- Label assumptions and directional estimates.
- Include presenter notes or talk track when the user needs to deliver the demo.
- Treat `.pptx` as the primary output whenever the user asks for a slide/deck.

Do not:

- Substitute a Markdown slide outline for an actual slide/deck when the user asks for a slide, PowerPoint, or presentation.
- Show raw logs, internal package names, or unfiltered build issues in executive artifacts.
- Overstate ROI or operational savings without verified inputs.
- Present mocked integrations as live production integrations.
