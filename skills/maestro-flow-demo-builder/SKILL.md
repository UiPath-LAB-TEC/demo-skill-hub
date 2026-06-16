---
name: maestro-flow-demo-builder
description: "Opinionated guidance for designing, building, improving, or reviewing customer-ready UiPath Maestro Flow demos. Use when Codex is asked for a Flow demo, Maestro Flow demo, Studio Web Flow demo, `.flow` artifact, demo narrative, or demo-grade Flow scaffold that should show end-to-end orchestration, visual appeal, diverse actors, agents, document processing, HITL, connectors, API workflows, RPA, and durable execution."
---

# Maestro Flow Demo Builder

Use this skill as a demo-shape overlay on top of the normal UiPath skills. For actual `.flow` authoring, first load `uipath-maestro-flow` and follow its CLI, node-ownership, resource-discovery, and validation rules. This skill defines what a great customer demo should communicate.

## Demo Goal

Build a Flow that looks and feels like a serious business process running across many actors and systems, not a tiny automation chain. The customer should leave with these ideas:

- Maestro Flow orchestrates large end-to-end processes as a directed graph.
- A Flow can span UiPath and non-UiPath actors: API workflows, AI agents, RPA, IDP or IXP, connectors, external agents, and human tasks.
- Agentic systems can be controlled with first-class HITL checkpoints.
- The runtime is durable and observable, including end-to-end tracing with OTEL spans.
- Studio Web can present this complexity in a developer-friendly and visually appealing way.

## Build Workflow

1. Start with a concrete process story: one inbound item, one business decision, and one visible business outcome.
2. Shape the graph left-to-right: ingestion, preprocessing and document extraction, agentic reasoning and actions, HITL, then routing to close.
3. Add actor diversity deliberately. Prefer a mix of manual or Data Fabric trigger, IXP document extraction, API workflow, inline agent, published or coded agent, external agent or connector, RPA, script or HTTP action, and HITL.
4. Give the inline agent at least one tool. Better: give it one tool plus one context grounding source, or two tools. The agent should visibly reason with resources, not just transform text.
5. Add advanced workflow logic: decisions, merges, loops, retry or exception-style branches where appropriate. Keep one side branch available for non-critical external-agent or notification demos if the live dependency is risky.
6. Add at least one human task using a Quick Form or coded action app. Place it after agentic reasoning and before final action so it proves control over AI-driven automation.
7. Use sticky notes as visual section headers, not documentation dumps. Use 3-5 large, color-coded notes such as `Ingestion`, `Document Extraction`, `Multi-Agent Validation`, `Human in the Loop`, and `Close`.
8. Validate locally with the installed UiPath CLI. Do not run debug or invoke live systems without explicit user consent.

## Demo Standards

- Prefer demo-grade completeness over production hardening.
- Prefer live tenant resources when they exist and are healthy. Verify auth, registry, connections, and model availability before claiming a live integration works.
- If a dependency cannot be bound, keep the graph coherent with a placeholder or safe non-executing branch and document the gap in the final answer or a build note.
- Prefer an IXP document extraction node for document demos. Use RPA extraction only when IXP is unavailable or the existing demo already uses RPA.
- Manual triggers are acceptable. Data Fabric triggers are also strong when the story starts from a business object or record.
- Keep labels customer-readable: `Download Invoice`, `Extract Invoice Data`, `PO Validation Agent`, `Human Approval`, `Create Payment`.
- Keep the layout legible from a zoomed-out canvas: section bands, clear branching, and no dense piles of nodes.

## References

Read [demo-shape-checklist.md](references/demo-shape-checklist.md) before building or reviewing a Flow demo.

Read [example-flow-pattern.md](references/example-flow-pattern.md) when you need a concrete pattern for actor diversity, layout, branch shape, and sticky-note usage.

Read [sanitized-example-flow.md](references/sanitized-example-flow.md) when you need a node-and-edge-level example without tenant-specific IDs, connection details, or generated connector payloads.
