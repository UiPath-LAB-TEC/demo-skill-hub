# Artifact-First Build Contract

## Dependency Boundary

This skill is not a replacement for official UiPath product skills.

Official UiPath product skills are assumed to be installed, available, and updated independently. Use them as the canonical source for:

- exact `uip` command syntax
- supported artifact structures
- RPA project implementation
- Agent implementation
- coded-agent implementation
- Solution packaging
- Orchestrator resource management
- Integration Service configuration
- Maestro or Flow implementation
- Apps or Action Center implementation
- test and validation behavior
- troubleshooting command failures

This skill owns only the sales-engineering orchestration layer:

- converting a customer scenario into a demo storyline
- choosing which UiPath capabilities to showcase
- selecting artifact types
- sequencing the build
- enforcing artifact-first delivery
- requiring demo data, tests, validation, packaging, and runbooks
- producing a demo script and executive-ready explanation
- ensuring the output is usable by a UiPath sales engineer

Do not duplicate lower-level product-skill instructions in this skill.

## Artifact-First Output Contract

This skill is successful only when it creates or updates executable, buildable, package-ready, or deployable UiPath demo artifacts on disk.

For build-oriented requests, do not stop after creating Markdown, analysis, design notes, implementation plans, readiness checklists, architecture descriptions, folder READMEs, storyboards, or recommendations.

Markdown files are allowed only as supporting documentation after source artifacts exist.

For every build-oriented request, produce at least one primary artifact category:

1. UiPath automation project artifacts
   - Studio or RPA project files
   - workflows
   - configuration
   - dependencies
   - tests or validation evidence

2. UiPath Agent or coded-agent artifacts
   - agent definitions
   - prompts or instructions
   - tool contracts
   - input and output schemas
   - evaluation fixtures
   - tests

3. UiPath Solution artifacts
   - solution folder structure
   - manifest or configuration
   - included components
   - environment configuration
   - package-ready output where supported

4. Orchestration artifacts
   - queues
   - assets
   - folders
   - processes
   - triggers
   - actions
   - human-in-the-loop schemas
   - resource definitions

5. Demo support artifacts
   - sample data
   - mock payloads
   - test fixtures
   - API stubs
   - simulated system responses
   - validation scripts
   - run scripts

6. Packaging or validation artifacts
   - dist output
   - package files
   - validation logs
   - test results
   - command output summaries

A final response is valid only if it lists:

- files and directories created or changed
- commands run
- validation or packaging results
- artifacts that are ready to run, validate, package, or deploy
- blocked live operations caused by missing approval, target selection, credentials, tenant permissions, folder configuration, or governance constraints

## No Markdown-Only Completion

For any request containing or implying words such as build, create, implement, scaffold, package, deploy, runnable, working demo, prototype, solution, automation, agent, validate, or end-to-end demo:

- Do not answer with only Markdown.
- Do not create only `.md` files.
- Do not treat a design contract, implementation plan, demo script, architecture description, checklist, or README as the primary deliverable.
- Do not stop after producing a build plan.
- Continue until at least one buildable artifact exists outside Markdown.

Before final response, inspect the workspace and verify that at least one non-Markdown artifact was created or updated.

Acceptable evidence includes one or more of:

- project files
- workflow files
- JSON, YAML, or XML configuration
- agent definition files
- solution manifests
- test fixtures
- sample data files
- scripts
- package files
- dist output
- validation logs
- command output files

If no non-Markdown artifact exists, the task is incomplete. Continue building.

## Required Workspace Structure For Build Requests

For end-to-end demo builds, create or update a workspace using this structure unless the existing repository already has a better structure:

```text
demo/
  README.md
  demo-script.md
  architecture.md

src/
  rpa/
  agents/
  coded-agents/
  apps/
  flows/
  orchestrations/
  integrations/

solution/
  manifest/
  resources/
  environments/

data/
  sample-input/
  sample-output/
  fixtures/
  mock-systems/

tests/
  unit/
  integration/
  demo-validation/

scripts/
  setup/
  validate/
  run-demo/

dist/
  packages/
  validation/
  logs/

docs/
  setup-guide.md
  operator-runbook.md
  assumptions.md
```

Rules:

- `docs/`, `demo/`, and Markdown files are supporting outputs.
- `src/`, `solution/`, `data/`, `tests/`, `scripts/`, and `dist/` are the primary build outputs.
- If using an existing UiPath project layout, preserve the native layout and map the same concepts into that layout.

## CLI And Product-Skill Behavior

The UiPath CLI (`uip`) and official UiPath product skills are required platform dependencies and must be treated as available.

For build-oriented requests:

1. Use the official UiPath product skills as the canonical implementation layer.
   - Do not duplicate their detailed command syntax.
   - Do not copy their instructions into this SE skill.
   - Do not maintain product-specific implementation guidance here unless it is specific to presales demo orchestration.

2. Use `uip` to create, validate, package, publish, deploy, inspect, or operate UiPath artifacts whenever the selected artifact type requires platform execution.

3. Use command help to discover or confirm command syntax:
   - `uip --help`
   - `uip <area> --help`
   - `uip <area> <command> --help`

4. Do not invent unsupported `uip` commands. If unsure, use CLI help and official UiPath product skills.

5. Prefer creating and validating local artifacts before performing live publish or deploy actions.

6. Do not publish, deploy, overwrite tenant resources, or make live tenant changes unless the user has provided or confirmed:
   - target tenant or organization
   - target folder or environment
   - deployment action
   - credential or authentication context
   - permission to perform the live action

7. If a live operation is blocked by missing confirmation, credentials, tenant access, folder configuration, or permissions, continue creating all local artifacts and mark only the live operation as blocked.

8. Capture important command outputs in:
   - `dist/logs/`
   - `dist/validation/`
   - `dist/packages/`

9. The final response must include:
   - UiPath skills or capability areas used
   - `uip` commands run
   - artifacts created
   - validation or package results
   - blocked live operations, if any

## Artifact Selection Matrix

When building a demo, select artifact types based on the use case:

- Use RPA artifacts when the demo includes UI automation, legacy systems, repetitive task execution, attended or unattended work, or system-of-record updates.
- Use Agent artifacts when the demo includes reasoning, natural language intake, decision support, summarization, recommendations, or autonomous task handling.
- Use coded-agent artifacts when the demo requires deterministic code-backed tool logic, API calls, structured transformations, or repeatable custom functions.
- Use Solution artifacts when the demo should be packaged as a deployable business solution with multiple components.
- Use Orchestrator resource artifacts when the demo needs queues, assets, processes, triggers, folders, credentials, or operational configuration.
- Use human-in-the-loop artifacts when approvals, exceptions, reviews, or business decisions are part of the story.
- Use Integration Service or API artifacts when the demo connects to external applications or mock systems.
- Use test artifacts for every build so the demo can be validated before presentation.

A build request should normally include:

- at least one runtime artifact under `src/`
- sample data under `data/`
- validation or test artifacts under `tests/`
- packaging or validation output under `dist/`
- supporting documentation under `docs/` or `demo/`

## Execution Workflow For Build Requests

Follow this order:

1. Understand the demo objective:
   - industry
   - buyer persona
   - pain point
   - business outcome
   - systems involved
   - desired wow moment

2. Decide whether the request is planning-only or build-oriented.
   - If planning-only, planning Markdown is acceptable.
   - If build-oriented, artifact-first rules apply.

3. Produce a minimal build plan internally or in a short `docs/assumptions.md`, but do not stop there.

4. Select artifact types using the artifact selection matrix.

5. Create or update the workspace structure.

6. Create source artifacts, configuration, sample data, fixtures, tests, and scripts.

7. Use installed official UiPath product skills and `uip` CLI for product-specific implementation.

8. Run validation, tests, packaging, or static checks where possible.

9. Place logs, validation output, or package output in `dist/`.

10. Create supporting Markdown:
    - README
    - setup guide
    - demo script
    - operator runbook
    - assumptions and blockers

11. Final response must summarize actual build outputs, not just the plan.

## Completion Gate For Build-Oriented Requests

Before final response, verify all of the following:

1. At least one non-Markdown artifact was created or updated.
2. Official UiPath product skills were used for product-specific implementation decisions.
3. `uip` was used for applicable creation, validation, packaging, inspection, publish, or deploy actions.
4. Source, configuration, data, tests, scripts, package-ready files, or validation outputs exist in the workspace.
5. Supporting Markdown exists only as explanation, setup guidance, runbook content, or demo script, not as the primary deliverable.
6. The final response lists concrete file paths.
7. The final response lists commands run.
8. The final response lists validation, packaging, or deployment results.
9. Any blocked live action is clearly identified as a tenant, credential, permission, target, approval, or governance blocker.

If these conditions are not met, continue building instead of answering.

## Examples

### Bad Example

User: Build a claims intake demo.

Wrong behavior:

- Create only `demo-brief.md`, `architecture.md`, and `implementation-plan.md`.

Why wrong:

- No runnable, buildable, package-ready, or deployable artifacts were created.

### Good Example

User: Build a claims intake demo.

Correct behavior:

Create or update files such as:

- `src/agents/claims-intake-agent/`
- `src/rpa/claims-system-update/`
- `solution/manifest/`
- `data/sample-input/claims.csv`
- `data/fixtures/claim-payloads.json`
- `tests/demo-validation/`
- `scripts/validate/run-validation.sh`
- `dist/validation/results.json`
- supporting `demo/README.md`
- supporting `demo/demo-script.md`

Then run available validation commands and report file paths, command results, validation output, and any live deployment blockers.

## Final Response Template For Build Requests

Use this structure:

```text
Built artifacts:
- path: purpose

UiPath capability areas used:
- area: reason

Commands run:
- command: result

Validation/package results:
- result or blocker

How to run or demo:
- steps

Supporting docs:
- path: purpose

Blocked live operations:
- blocker and required user action
```

Do not use this final response if only Markdown was created for a build request.
