# Current-State Map

Use this structure to create an as-is process map.

## Required Sections

- Process name and scope.
- Start event and end state.
- Actor lanes or role responsibilities.
- Channels, queues, portals, and intake sources.
- Systems and records touched.
- Documents, messages, files, forms, and attachments.
- Step-by-step process.
- Decision points.
- Exception paths.
- Manual work, waiting, rework, approvals, and escalations.
- Bottlenecks, quality checks, compliance controls, and audit requirements.
- Control, compliance, or audit requirements.
- Known metrics first, then unverified or missing metrics.

## Current-State Snapshot

Before the step-by-step map, include a compact snapshot covering actors, channels, systems, core steps, exceptions, controls, metrics, and bottlenecks. Use customer terminology and mark assumed lane names as assumptions.

## Mermaid Guidance

Use Mermaid only when it makes the process clearer. Keep diagrams business-readable.

Use actor or system labels that match customer terminology. Do not invent lane names when the source is unclear; mark them as assumptions.

## Output Rule

End with "automation opportunity candidates" rather than a full future-state architecture unless the user asks for design.

Do not let future-state ideas overwrite the as-is map. Keep expected benefits and opportunity candidates separate from current-state facts.
