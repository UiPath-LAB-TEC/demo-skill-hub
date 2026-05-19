# Goal Prompt Template

Use this shape for `CODEX-GOAL-PROMPT.md`.

```text
/goal

<goal>
Build the UiPath demo described in SPEC.md. Produce the requested local artifacts and validate them against the contracts in the spec.
</goal>

<context>
Read these first:
- SPEC.md
- any supporting files under demo-build-plan/
- AGENTS.md
- relevant project files and generated metadata
- relevant UiPath skill instructions for Flow, agents, coded action apps when applicable, and platform upload
</context>

<constraints>
- Preserve the scope in SPEC.md.
- Do not add production hardening unless required for the demo to run.
- Use the agent mode selected in SPEC.md.
- Use mock script payload, connector, native Flow node, human review, and explicitly requested API Workflow contracts exactly as specified.
- Default mock system interactions to script nodes that create deterministic payloads. Do not create API Workflow artifacts unless SPEC.md explicitly requires them.
- If SPEC.md selects coded action app review, build, publish, and deploy that coded action app separately to the specified Orchestrator folder, then reference the published app from the Maestro Flow. Do not add the coded action app as a project inside the Studio Web solution.
- Keep the Flow visually clean with grouped nodes and sticky notes, but do not block completion on rendered-canvas inspection.
- Ask before changing Studio Web upload scope.
</constraints>

<done_when>
- All required artifacts in SPEC.md exist.
- Flow, agent, mock script payload, fixture, coded action app when applicable, and solution validation checks pass or have documented blockers.
- Happy-path and exception-path fixtures produce the expected outputs.
- Studio Web upload is completed only if SPEC.md requests it.
- Final response reports changed files, validation results, blockers, and any Studio Web URL.
</done_when>

<workflow>
1. Read all context files before editing.
2. Inspect actual repo state, generated metadata, installed CLI behavior, and auth target before making claims.
3. Build in small checkpoints: project scaffold, Flow, agents, mock script payloads/connectors, coded action app if selected, fixtures, validation, optional upload.
4. After each checkpoint, run the relevant validation and update the remaining work.
5. Stop when done_when is satisfied or a real blocker prevents completion.
</workflow>

<verification_loop>
After each major change, run the narrowest useful validation. Before completion, run the full validation list from SPEC.md.
</verification_loop>

<execution_rules>
- Use rg for search.
- Use apply_patch for manual edits.
- Preserve unrelated user changes.
- Use uv for Python package management. Never use pip.
- Run npm test after JavaScript edits.
- Open relevant UiPath skills before UiPath build, validation, upload, or debugging work.
- Keep final output concise.
</execution_rules>

<output_contract>
When complete, summarize artifacts created, validations run, upload status, URLs, and unresolved blockers.
</output_contract>
```

Use this shape for `TIGHTEN-SPEC-PROMPT.md`.

```text
Read SPEC.md. Identify ambiguous, unverifiable, risky, or missing requirements.

For each issue, explain the ambiguity, give two practical interpretations, and recommend the one that produces the most buildable demo without adding scope.

Then tighten SPEC.md in place. Preserve decisions that are already clear. Remove or label anything that cannot be verified. Do not build the demo yet.
```
