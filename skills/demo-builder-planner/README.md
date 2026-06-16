# UiPath Demo SPEC Builder

`demo-builder-planner` is a Claude Code plugin and Codex skill for creating demo-grade `SPEC.md` files for UiPath demos. It turns a customer name, use case, or short brief into a build contract that another AI can use with the relevant UiPath specialist skills.

The skill plans the demo only. It does not build, validate, upload, or deploy UiPath artifacts.

Use this skill when you need to plan a large demo build (think Maestro BPMN or Case, a few agents, a few APIWF etc.) - if not at this scale, the planning and SPEC generation are probably overkill.

Repository: https://github.com/jms-dcksn/demo-skill-hub/tree/main/demo-builder

## Install

### Claude Code Plugin

Add the marketplace from the published `demo-builder` package:

```
/plugin marketplace add https://raw.githubusercontent.com/jms-dcksn/demo-skill-hub/main/demo-builder/.claude-plugin/marketplace.json
```

Or from the CLI:

```bash
claude plugin marketplace add https://raw.githubusercontent.com/jms-dcksn/demo-skill-hub/main/demo-builder/.claude-plugin/marketplace.json
```

If you previously installed the old standalone marketplace, remove it first:

```bash
claude plugin marketplace remove uipath-demo-builder
```

Install the plugin:

```
/plugin install demo-builder-planner@uipath-demo-builder
```

Or from the CLI:

```bash
claude plugin install demo-builder-planner@uipath-demo-builder
```

Use the skill:

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
        "source": "url",
        "url": "https://raw.githubusercontent.com/jms-dcksn/demo-skill-hub/main/demo-builder/.claude-plugin/marketplace.json"
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
Install the Codex skill at https://github.com/jms-dcksn/demo-skill-hub/tree/main/demo-builder/plugins/demo-builder-planner/skills/demo-builder-planner
```

Restart Codex after the install finishes.

### Option B: Install from terminal

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo jms-dcksn/demo-skill-hub --path demo-builder/plugins/demo-builder-planner/skills/demo-builder-planner
```

## Companion Skills

Install the relevant UiPath skills too. The SPEC should name which ones the builder must open, such as:

- `uipath-maestro-flow`
- `uipath-maestro-bpmn`
- `uipath-rpa`
- `uipath-agents`
- `uipath-coded-apps`
- `uipath-api-workflow`
- `uipath-maestro-case`
- `uipath-platform`
- `uipath-solution`

## How To Use

Start a conversation and describe the demo you want:

```text
Create a UiPath demo SPEC.md for commercial insurance claims triage.
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
- Preferred UiPath artifact surfaces, if known
- Deployment or tenant/folder expectation, if known

The planner writes:

- `SPEC.md`

It does not write `/goal` prompts, implementation handoff prompts, or supporting files unless explicitly requested.

## Repository Layout

```text
.claude-plugin/marketplace.json                                          # Marketplace catalog
plugins/demo-builder-planner/.claude-plugin/plugin.json                  # Plugin manifest
plugins/demo-builder-planner/skills/demo-builder-planner/SKILL.md        # Skill definition
plugins/demo-builder-planner/skills/demo-builder-planner/references/
```
