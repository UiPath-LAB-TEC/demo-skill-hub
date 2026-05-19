# ~/.codex/AGENTS.md

  ## Working Agreements

  - Always run `npm test` after modifying JavaScript files.
  - Always use `uv` for Python package management. Never use `pip`.
  - Keep README files concise.
  - Do not use emojis in documentation.

  ## UiPath Work

  Most work in this workspace is for UiPath demo artifacts: Python and Low Code AI agents, coded apps, Maestro Flows, Case
  Management, API workflows, and related solution packaging.

  For UiPath work:
  - Open the relevant UiPath skill before making changes or giving workflow guidance.
  - Inspect the actual repo, generated metadata, installed CLI behavior, and current auth target before making claims.
  - Prefer simple demo-grade implementations that illustrate the concept.
  - Avoid production hardening unless it is required for the demo to work.

  ## Clarification Standard

  Before writing code or drafting a plan, check whether the request has enough information to proceed.

  Ask clarifying questions when any of these are unclear:
  - target repo, folder, artifact, or environment
  - expected input/output contract
  - UiPath product surface or skill to use
  - validation command or deployment target
  - a conflict between the request, repo state, CLI behavior, or skill guidance

  If the task is clear, briefly state the assumption and proceed.

  ## Response Style

  - Be concise and direct.
  - Flag gaps, contradictions, and risky assumptions early.
  - Do not be overly agreeable.
  - Prefer evidence from the actual repo, CLI output, or artifact state.