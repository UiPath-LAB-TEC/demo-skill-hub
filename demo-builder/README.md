# UiPath Demo Builder Planner

`demo-builder-planner` is a Claude Code plugin for planning demo-grade UiPath Maestro Flow builds. It turns a customer name, use case, or short brief into a precise `SPEC.md`, a short spec-tightening prompt, and a structured `/goal` prompt for long-running demo builds.

The skill plans the demo. It does not build or upload UiPath artifacts by itself. The resulting artifacts are meant to be handed to a coding agent with the core UiPath skills installed.

## Install

### Step 1 — Add the marketplace

Run this inside Claude Code (or in a Claude Code terminal session):

```
/plugin marketplace add jms-dcksn/uipath-demo-builder
```

Or from the CLI:

```bash
claude plugin marketplace add jms-dcksn/uipath-demo-builder
```

### Step 2 — Install the plugin

```
/plugin install demo-builder-planner@uipath-demo-builder
```

Or from the CLI:

```bash
claude plugin install demo-builder-planner@uipath-demo-builder
```

### Step 3 — Use the skill

```
/demo-builder-planner:demo-builder-planner
```

Or just describe a demo in natural language — Claude Code will pick up the skill automatically when the context matches.

### Update

To get the latest version:

```
/plugin marketplace update uipath-demo-builder
/plugin update demo-builder-planner@uipath-demo-builder
```

### Auto-install for your team

Add to your project's `.claude/settings.json` to have teammates prompted to install automatically:

```json
{
  "extraKnownMarketplaces": {
    "uipath-demo-builder": {
      "source": {
        "source": "github",
        "repo": "jms-dcksn/uipath-demo-builder"
      }
    }
  },
  "enabledPlugins": {
    "demo-builder-planner@uipath-demo-builder": true
  }
}
```

## Install as a Codex Skill

### Option A: Ask Codex to install it

Open Codex and paste:

```text
Install the Codex skill at https://github.com/jms-dcksn/uipath-demo-builder/tree/main/plugins/demo-builder-planner/skills/demo-builder-planner
```

Restart Codex after the install finishes.

### Option B: Install from terminal

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo jms-dcksn/uipath-demo-builder --path plugins/demo-builder-planner/skills/demo-builder-planner
```

## Companion Skills

Install the core UiPath skills too. The planner depends on them for product-specific build guidance:

- `uipath-maestro-flow`
- `uipath-agents`
- `uipath-platform`

## How To Use

Start a conversation and describe the demo you want:

```text
Plan a UiPath Maestro Flow demo for commercial insurance claims triage.
```

Minimum input:

- Customer or account name
- Use case title
- Short use-case brief

Better input:

- Industry or domain
- Known systems or connectors
- Must-show UiPath capabilities
- Happy path and one exception path
- Preferred agent mode, if known
- Studio Web upload expectation, if known

The planner writes:

- `SPEC.md`
- `TIGHTEN-SPEC-PROMPT.md`
- `CODEX-GOAL-PROMPT.md`
- Optional supporting files under `demo-build-plan/` for larger demos

## Workflow

![Demo Builder Planner workflow](docs/planner-workflow.svg)

After the interview, the planner creates a first draft `SPEC.md`. Then ask the agent to tighten the spec:

```text
@SPEC.md
@TIGHTEN-SPEC-PROMPT.md
```

When the spec is ready, start the implementation handoff:

```text
/goal
@SPEC.md
@CODEX-GOAL-PROMPT.md
```

## Repository Layout

```text
.claude-plugin/marketplace.json                                          # Marketplace catalog
plugins/demo-builder-planner/.claude-plugin/plugin.json                  # Plugin manifest
plugins/demo-builder-planner/skills/demo-builder-planner/SKILL.md        # Skill definition
plugins/demo-builder-planner/skills/demo-builder-planner/references/
docs/planner-workflow.excalidraw
docs/planner-workflow.svg
```
