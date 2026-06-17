# Demo Skill Hub

This repo is a hub for reusable skills, prompts, and setup patterns that help Sales Engineers use coding agents to build and present customer demos.

The content is focused on practical demo work: planning UiPath demos, converting existing assets, setting up coding-agent workspaces, and giving agents clear prompts for repeatable builds.

## Structure

- `skills/` - reusable Codex and Claude skills for demo planning and build guidance.
  - `skills/demo-builder-planner/` - plugin and Codex skill for writing UiPath demo `SPEC.md` files.
  - `skills/uipath-reference-solution-planner/` - Codex skill for planning a new UiPath demo from a downloaded reference solution.
  - `skills/bpmn-flow-conversion/` - local skill for converting Maestro BPMN demos into Maestro Flow demos.
  - `skills/skill-marketplace-metadata/` - Codex skill for adding Marketplace metadata to skill `SKILL.md` files.
- `demos/` - one-shot prompts and exercises that demonstrate coding-agent demo patterns.
  - `demos/flow-multi-agent/` - prompt example for a multi-agent Maestro Flow demo.
  - `demos/two-agent-demo/` - prompt example for a two-agent demo pattern.
  - `demos/langchain-agent-exercise/` - guided build, deploy, and evaluation exercise for a LangChain-based agent.
- `codex-setup/` - workspace instructions for demo-building projects.

## How To Use

Start with the folder that matches the job:

- use `skills/demo-builder-planner/` when you need a buildable UiPath demo `SPEC.md`
- use `skills/` when you need reusable agent behavior in another repo
- use `demos/` when you need an example prompt or exercise
- use `codex-setup/` when preparing a demo-building workspace

Copy the relevant prompt, skill, or setup instructions into the demo repo you are working in. Keep the target demo simple, make the agent instructions explicit, and validate the resulting artifact before presenting it to a customer.

Most examples here are designed for demo-grade delivery rather than production hardening.
