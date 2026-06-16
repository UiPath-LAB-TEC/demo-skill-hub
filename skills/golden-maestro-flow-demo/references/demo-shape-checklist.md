# Maestro Flow Demo Shape Checklist

Use this checklist before building, reviewing, or improving a Maestro Flow demo.

## Required Shape

- A clear story: one inbound item, one business decision, one outcome.
- Left-to-right graph: ingestion -> preprocessing/extraction -> agentic reasoning/actions -> HITL -> routing/close.
- At least one human task, preferably after agent reasoning and before final execution.
- At least one document processing moment for document-centric demos. Prefer IXP extraction over RPA extraction when available.
- At least one inline agent with a visible tool and either context grounding or a second tool.
- Advanced logic beyond a straight line: decision, merge, loop, retry, escalation, or exception branch.
- Sticky notes used as large section bands with short labels and varied colors.

## Actor Mix

Aim for at least five distinct actor categories:

- Trigger: manual, Data Fabric, connector trigger, or other business event.
- UiPath execution: RPA process, API workflow, or coded workflow.
- Document processing: IXP extraction, DU, or RPA-based extraction fallback.
- AI agents: inline agent plus one published, coded, external, or low-code agent.
- Agent resources: connector tool, web search, index, data source, or MCP tool.
- Human control: Quick Form or coded action app.
- System action: connector activity, HTTP action, script, queue, or data update.

## Visual Design

- Arrange sections left to right with generous horizontal spacing.
- Put sticky notes behind or near groups, not between connected nodes.
- Keep sticky-note text short: `Ingestion`, `Multi-Agent Validation`, `Human in the Loop`, `Close`.
- Use color to draw attention to concept areas: green for ingestion, blue for agentic reasoning, yellow for HITL, white or neutral for close.
- Prefer labels that describe business intent over implementation detail.
- Keep any external-agent showcase branch visually present even if it is not always executed.

## Validation

- Load `uipath-maestro-flow` for file-format and CLI details before editing `.flow` files.
- Use registry and connection discovery before assuming a resource exists.
- Validate with `uip maestro flow validate ... --output json`.
- Do not run `flow debug` or any live invocation without explicit user consent.
- If live dependencies are missing, leave a coherent local scaffold and state the exact gaps.
