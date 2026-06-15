# AGENTS.md

## Purpose
This repository provides a minimalist **UiPath demo SPEC builder skill** for presales work.

Use this skill to help sales engineers turn a customer name, use case, or short brief into a robust `SPEC.md` that can be handed to another AI for implementation.

## Intent and Positioning
- Treat this repo as a **planning layer**, not a build system.
- The planner creates an implementation-ready `SPEC.md` only.
- Codex plus the core UiPath skills remain responsible for building, validating, uploading, and debugging UiPath artifacts.
- Keep the planner focused on interviewing, demo storytelling, scope control, artifact selection, skill routing, and build-contract clarity.

## What to Optimize For
- Fast path from customer use case -> precise `SPEC.md` -> builder handoff.
- Demo-grade scope: clear happy path plus one exception path.
- Clear assumptions, inputs, outputs, artifact inventory, skill routing, data and integration contracts, fixtures, and validation checks.
- Outputs that are practical for a coding agent to implement without re-discovering the use case.

## Working Expectations
- Keep this repo as simple as possible: one planner skill and its direct reference material.
- Do not reintroduce companion build skills, plugin wrappers, slash commands, or marketplace packaging unless explicitly requested.
- Do not create Flow, BPMN, RPA, agent, coded app, API workflow, case, fixture, solution, or upload artifacts from the planner skill.
- The planner output should be `SPEC.md` only.
- Do not add supporting files unless the user explicitly asks for them.
- Ask about deployment, upload, and tenant/folder targets only when they matter to the demo.
- Cross-reference requirements with the UiPath specialist skills before choosing artifact surfaces.
- Keep changes concise, practical, and aligned to the existing repository conventions.
- When in doubt, preserve simplicity and plan quality over build automation.
