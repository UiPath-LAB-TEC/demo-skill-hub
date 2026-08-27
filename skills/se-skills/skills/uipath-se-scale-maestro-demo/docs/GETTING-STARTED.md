# Getting Started

## Contents

- [1. Install the skill](#1-install-the-skill)
- [2. Verify prerequisites](#2-verify-prerequisites)
- [3. Identify the process target](#3-identify-the-process-target)
- [4. Prepare fixtures](#4-prepare-fixtures)
- [5. Materialize a plan](#5-materialize-a-plan)
- [6. Dry run](#6-dry-run)
- [7. Canary and resume](#7-canary-and-resume)
- [8. Verify outcomes](#8-verify-outcomes)

## 1. Install the Skill

Copy this skill folder into the directory that directly contains your installed skill folders, for example `~/.codex/skills/`:

```powershell
Copy-Item -Recurse skills/se-skills/skills/uipath-se-scale-maestro-demo "$env:USERPROFILE/.codex/skills/"
```

Restart or refresh the agent so it discovers `$uipath-se-scale-maestro-demo`. Do not overwrite an existing copy accidentally; rename or remove the old one deliberately first.

The scripts are also usable without installation:

```powershell
python skills/se-skills/skills/uipath-se-scale-maestro-demo/scripts/prepare_run_plan.py --help
python skills/se-skills/skills/uipath-se-scale-maestro-demo/scripts/run_maestro_batch.py --help
```

## 2. Verify Prerequisites

Confirm Python and UiPath CLI:

```powershell
python --version
uip.cmd --version
uip.cmd login status --output json
```

On macOS or Linux, use `uip` instead of `uip.cmd`.

Before any mutation, verify that login status names the intended organization and tenant. Do not proceed merely because the session says “logged in.”

The process must already be deployed and accessible in a known Orchestrator folder. The skill operates BPMN Process Orchestration instances; it does not treat `.flow` or Case Management instances as BPMN.

## 3. Identify the Process Target

You need four stable identifiers:

- Process key including the package version for starts.
- Folder key.
- Release key.
- Feed ID.

Use current CLI help and process discovery rather than copying identifiers from another tenant:

```powershell
uip.cmd maestro bpmn process list --folder-key <folder-key> --output json
```

Confirm the returned name, package version, release key, folder key, and feed ID. The runner fingerprints these values together; a different target will not inherit another target's resume state.

## 4. Prepare Fixtures

Every fixture must be a JSON object accepted by the deployed start event. A fixture source can be:

- One JSON object file.
- A JSON array containing objects.
- A directory of `.json` object files.

The planner sorts directory filenames and cycles through them deterministically. It preserves payloads exactly and does not inject a correlation field that might violate the start schema.

Use [Process-Agnostic Fixture Patterns](../examples/FIXTURE-PATTERNS.md) to derive fixtures from the deployed start-event contract. The bundle deliberately ships no executable process-specific fixtures.

Keep fixtures synthetic unless the approved demo explicitly permits protected data. Remember that scale multiplies every connector, queue item, email, task, robot job, and external write in the process.

## 5. Materialize a Plan

Create a new evidence directory and plan:

```powershell
python skill/uipath-se-scale-maestro-demo/scripts/prepare_run_plan.py --demo-root C:\path\to\demo --fixtures C:\path\to\fixtures --count 100 --max-concurrency 5 --delay-ms 500 --output C:\path\to\demo\dist\maestro-scale\batch-001\run-plan.json
```

Planner options:

- `--count`: requested starts, from 1 through 10,000.
- `--max-concurrency`: maximum simultaneous CLI starts.
- `--delay-ms`: pause between completed parallel waves.
- `--strategy cycle`: rotate through all fixtures.
- `--strategy first`: use only the first fixture.
- `--force`: replace an unexecuted local plan only when explicitly intended.

Treat the plan and its generated input directory as immutable after approval.

## 6. Dry Run

With a global CLI on `PATH`:

```powershell
python skill/uipath-se-scale-maestro-demo/scripts/run_maestro_batch.py --plan C:\path\to\batch-001\run-plan.json --process-key <process-key:version> --folder-key <folder-key> --release-key <release-key> --feed-id <feed-id> --evidence-dir C:\path\to\batch-001\execution --dry-run
```

For a pinned repository CLI, add:

```text
--cli-entry <workspace>/.uipath-tools/node_modules/@uipath/cli/dist/index.js
```

Review `execution-preview.json`. It shows the target fingerprint, selected ordinals, concurrency, delay, and whether prior successful starts will be skipped. A dry run performs no cloud mutation.

## 7. Canary and Resume

Start one planned instance:

```powershell
python skill/uipath-se-scale-maestro-demo/scripts/run_maestro_batch.py <same-target-arguments> --canary-only
```

Verify the returned instance by exact ID. Confirm its folder, package version, initial status, variables, current element, and side effects.

Then repeat the same command without `--canary-only`. Use the same plan and evidence directory. The runner recognizes the successful canary by `clientRunId` plus target fingerprint and skips it.

Do not create a second plan merely to continue a successful canary. Do not change a plan's concurrency after execution begins.

## 8. Verify Outcomes

The runner proves start submission, not final business completion. Reconcile exact ledger instance IDs through `uip maestro bpmn instance get` or the current supported API.

Verify:

- Returned instance count and uniqueness.
- Package version and folder.
- Expected status distribution.
- Expected wait element for live cohorts.
- Expected terminal elements and outputs for completed cohorts.
- Incidents, throttling, or unexpected side effects.

Keep final verification results beside `instances.jsonl` and `summary.json`.
