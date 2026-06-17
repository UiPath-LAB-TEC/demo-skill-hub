# Reference Solution Inspection Checklist

Use this checklist after the Studio Web solution has been downloaded and extracted.

## First Pass

Record:

- solution ID, downloaded archive path, extracted directory, CLI version behavior, auth target, tenant, and folder if known
- top-level files and generated briefing docs such as `AGENTS.md`, `CLAUDE.md`, `.uipx`, `project.json`, or package descriptors
- project directories and artifact types present in the solution
- resource directories and debug overwrite files

Useful commands:

```bash
find "$EXTRACTED_DIR" -maxdepth 4 -type f | sort
rg -n "SolutionId|ProjectId|Connection|Queue|Asset|Bucket|DataFabric|Trigger|Process|Agent|Action|Task|IXP|Document" "$EXTRACTED_DIR"
```

Prefer structured parsing for JSON, XML, and YAML when practical. Do not rely only on filename guesses.

## Artifact Inventory

For each artifact, capture:

- path and artifact type
- owning UiPath specialist skill the builder must open
- role in the reference demo
- trigger and entry point
- input contract and sample payloads
- output contract and terminal states
- dependencies on other projects or platform resources
- validation command or evidence in the reference
- whether to reuse, adapt, replace, mock, or create new for the target use case

Common files and likely skills:

| Evidence | Inspect with |
|---|---|
| `.flow` | `uipath-maestro-flow` |
| `.bpmn`, `project.uiproj`, `entry-points.json`, `operate.json`, `bindings_v2.json` | `uipath-maestro-bpmn` |
| `.xaml`, coded workflow `.cs`, RPA `project.json` | `uipath-rpa` or `uipath-rpa-legacy` |
| `agent.json`, Python agent project | `uipath-agents` |
| API workflow JSON with `document.dsl` or `do[]` | `uipath-api-workflow` |
| `caseplan.json` | `uipath-maestro-case` |
| `app.config.json`, `action-schema.json` | `uipath-coded-apps` |
| queues, assets, buckets, folders, connections, triggers, packages | `uipath-platform` |
| Data Fabric schema or records | `uipath-data-fabric` |
| HITL, Action Center, review forms, approval tasks | `uipath-human-in-the-loop` and sometimes `uipath-coded-apps` |

## Demo Pattern Analysis

Identify the reference demo's reusable pattern:

- business story and audience
- must-show moments
- happy path and exception path
- stage or node sequence
- AI or document extraction responsibilities
- human review responsibilities
- system-of-record interactions
- mock data strategy and fixtures
- UI screens or review experiences
- deployment, packaging, and validation approach

Then classify each part:

- **Reuse unchanged**: keep the pattern or artifact as-is for the target.
- **Adapt**: rename, change fields, change prompts, change routing, or change data while preserving the structure.
- **Replace**: swap to a different product surface, connector, model, UI, or artifact type.
- **Create new**: build a new artifact or platform resource not present in the reference.
- **Drop**: omit reference complexity that does not help the new demo.

## Clarification Question Sources

Ask questions from evidence, not generic preference. Good questions come from:

- a reference artifact with domain-specific names that need target-domain equivalents
- a connector or resource that may be unavailable in the target tenant
- a human task whose target UI or approval behavior is unclear
- an agent prompt whose target decisions, tools, or output schema need new domain details
- a data model whose fields need new names, examples, or validation rules
- a validation path that requires live systems, seeded records, or deployment choices
- a reference feature that may be overbuilt for the new demo

Every question should include a recommended answer and the consequence of choosing differently.
