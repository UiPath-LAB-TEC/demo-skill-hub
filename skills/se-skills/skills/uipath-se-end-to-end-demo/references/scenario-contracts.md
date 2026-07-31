# Scenario Contracts

Define these contracts before building screens, prompts, or orchestration branches.

## Scenario Input

Include:

- `scenarioId`
- `branchType`
- `intakeChannel`
- `sourceFiles`
- `customerContext`
- `expectedRoute`
- `expectedFinalStatus`
- `mockedSurfaces`

## Extraction Output

Include:

- Document class and confidence.
- Extracted fields and field confidence.
- Documents present and missing.
- Low-confidence or conflicting fields.
- Raw payload or trace reference.

## AI Agent Output

Include:

- Summary.
- Rationale.
- Risk, priority, or readiness score.
- Recommended next action.
- Confidence.
- Tool results.
- Citations or evidence references when available.

## RPA Output

Include:

- System lookup results.
- Deterministic status.
- Record ids.
- File upload or download references.
- Error code and retryability when a system action fails.

## Action App Payload

Include:

- `reviewMode`
- Normalized case data.
- Document metadata, preview URL, storage path, fixture fallback path, unavailable reason, and content type.
- Extracted fields.
- AI recommendations and rationale.
- Decision options.
- Reviewer notes and corrections.
- Outbound draft text when applicable.

Normalize inbound `task.data` before rendering. Do not rely on a shallow merge of local fixture data into deployed task data.

## Completion Payload

Include:

- Reviewer decision.
- Notes.
- Field corrections.
- Selected downstream option, date, or route when applicable.
- Approval flags.
- Rework or escalation reason.

## Case Status

Include:

- Durable status.
- Owner.
- Branch.
- Current stage.
- Outbound communication status.
- Activity log.
- Terminal outcome.
