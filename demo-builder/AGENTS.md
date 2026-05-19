# AGENTS.md

## Purpose
This repository provides a minimalist **demo-builder planner skill** for presales work.

Use this skill to help sales engineers turn a customer name, use case, or short brief into a robust `SPEC.md` and `/goal` prompt that can be handed off to Codex for implementation.

## Intent and Positioning
- Treat this repo as a **planning layer**, not a build system.
- The planner creates implementation-ready Markdown artifacts only.
- Codex plus the core UiPath skills remain responsible for building, validating, uploading, and debugging UiPath artifacts.
- Keep the planner focused on ideation, demo storytelling, scope control, architecture, handoff clarity, and repeatability.

## What to Optimize For
- Fast path from customer use case -> precise spec -> structured `/goal` prompt -> Codex handoff.
- Demo-grade scope: clear happy path plus one exception path.
- Clear assumptions, inputs, outputs, Flow architecture, agent roles, mock script payload contracts, fixtures, and validation checks.
- Outputs that are practical for a coding agent to implement without re-discovering the use case.

## Working Expectations
- Keep this repo as simple as possible: one planner skill and its direct reference material.
- Do not reintroduce companion build skills, plugin wrappers, slash commands, or marketplace packaging unless explicitly requested.
- Do not create Flow, agent, coded action app, fixture, solution, or Studio Web upload artifacts from the planner skill.
- The planner output should be `SPEC.md`, `TIGHTEN-SPEC-PROMPT.md`, and `CODEX-GOAL-PROMPT.md`.
- Use supporting files under `demo-build-plan/` only when needed for larger demos.
- Ask the user about Studio Web upload during the interview if they did not specify it up front.
- Ask the user to choose the agent mode: inline Flow agents, coded agents, low-code agents, or mixed.
- Keep changes concise, practical, and aligned to the existing repository conventions.
- When in doubt, preserve simplicity and plan quality over build automation.
