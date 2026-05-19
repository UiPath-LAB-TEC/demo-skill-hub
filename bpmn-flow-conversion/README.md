# BPMN Flow Conversion Skill

`uipath-bpmn-to-flow-conversion` is a local Codex skill for Sales Engineers who need to convert an existing UiPath Maestro BPMN demo into a UiPath Maestro Flow demo.

Install it into the local repo where you are doing the conversion. Do not install it globally unless you want it available in every Codex workspace.

## What You Need

- A local repo for the demo you want to convert
- Codex running from that repo
- Access to this skill folder:

```text
bpmn-flow-conversion/uipath-bpmn-to-flow-conversion
```

The skill folder must include:

```text
SKILL.md
agents/openai.yaml
```

## Add It To A Local Repo

From the repo where you want to use the skill, create a local skills folder:

```bash
mkdir -p .agents/skills
```

Copy the skill folder into that repo:

```bash
cp -R /path/to/demo-skill-hub/bpmn-flow-conversion/uipath-bpmn-to-flow-conversion .agents/skills/
```

After copying, the target repo should look like this:

```text
.agents/
  skills/
    uipath-bpmn-to-flow-conversion/
      SKILL.md
      agents/
        openai.yaml
```

Restart Codex from the target repo so it picks up the new local skill.

## Verify The Install

In the target repo, confirm the files exist:

```bash
ls .agents/skills/uipath-bpmn-to-flow-conversion
```

Expected output includes:

```text
SKILL.md
agents
```

Then ask Codex something that matches the skill:

```text
Use the uipath-bpmn-to-flow-conversion skill to inspect this BPMN project and create a conversion plan for a Maestro Flow version.
```

Codex should load the local skill and use the UiPath BPMN, Flow, HITL, coded apps, and platform skills as needed.

## When To Use It

Use this skill when the goal is a close 1:1 conversion from Maestro BPMN or Process Orchestration to Maestro Flow.

It is intended to preserve:

- process sequence
- input and output contract
- node names and intent
- RPA, API workflow, connector, and AI agent dependencies
- human review or approval behavior
- demo story and expected outcomes

It is not intended for redesigning the process from scratch.

## Recommended First Prompt

After installing the skill, open Codex in the target repo and start with:

```text
Use the uipath-bpmn-to-flow-conversion skill.

Inspect the BPMN project in this repo and create a concise conversion plan for a close 1:1 Maestro Flow version. Identify required clarification questions before making changes.
```

If you already know the target folder or deployment expectation, include it:

```text
Target tenant and folder: <tenant/folder>
Upload to Studio Web after local validation: yes/no
```

## Notes For Sales Engineers

- Keep the conversion demo-grade and simple.
- Reuse existing resources when possible.
- Ask before mocking or replacing missing resources.
- Convert simple human tasks to Flow-native quick forms unless a coded action app is required.
- Keep AI agents as external resource calls unless the demo explicitly needs inline Flow agents.
