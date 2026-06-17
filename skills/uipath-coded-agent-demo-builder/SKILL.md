---
name: uipath-coded-agent-demo-builder
description: "Build demo-grade UiPath coded agent demos using a prescribed LangGraph + LangChain architecture. Use when the user asks to create, scaffold, repair, or guide a UiPath coded agent demo that should use LangGraph, LangChain create_agent(), Context Grounding semantic search, guardrail middleware, structured inputs/outputs, and optional extra tools."
metadata:
  author: "James Dickson"
  version: "1.0.0"
  ownerEmail: "jms.dcksn88@gmail.com"
  changeSummary: "Initial opinionated coded agent demo builder skill."
  isBreaking: false
  category: "Sales Engineering"
  tags:
    - uipath
    - coded-agents
    - langgraph
    - langchain
    - context-grounding
    - guardrails
  platforms:
    - OpenAI
  businessUseCases:
    - "Build best-practice UiPath coded agent demos"
---

# UiPath Coded Agent Demo Builder

Build a concise, demo-grade UiPath coded agent with one opinionated pattern:

- outer LangGraph workflow: `START -> run_agent -> END`
- one LangGraph node that owns the agent run
- a LangChain `create_agent()` agent inside that node
- Context Grounding exposed as a retriever-backed LangChain tool
- harmful-content guardrails applied as LangChain middleware
- structured Pydantic input and output models
- optional additional tools only when the user provides them

Do not turn every capability into a separate LangGraph node. Let the LangChain agent choose when to call Context Grounding and any optional tools.

## Required Inputs

Before writing code or a build plan, require these user-provided details:

- Context Grounding index name.
- Context Grounding folder path or folder key.
- Context Grounding index description: what knowledge is in it and how the agent should use it.
- System prompt guidance: demo role, tone, decision policy, and must-use evidence rules.
- Input contract: field names, types, and representative values.
- Output contract: field names, types, and how the demo will judge success.

If any required detail is missing, ask only for the missing blocker. If the user provides optional target tools, require each tool's purpose, auth/resource details, input/output shape, and folder or connection binding data before implementing it.

## Required Routing

Use the `uipath-agents` skill before making UiPath coded-agent claims or edits. For coded-agent builds, read its coded quickstart plus the relevant references for LangGraph, Context Grounding, guardrails, bindings, running, and evaluations.

Use `uipath-platform` when checking tenant auth, folders, resources, connections, or live Context Grounding index availability. Use other UiPath skills only when optional tools require them.

Verify the actual repo, generated metadata, installed `uip` CLI behavior, and current auth target. Do not invent index names, folder paths, model names, guardrail availability, connection keys, or deployment targets.

## Build Workflow

1. Inspect project state.
   - Detect greenfield, existing coded-agent, or Studio Web local workspace from the actual files.
   - Use `uv` for Python package management.
   - Use `uip codedagent`, not direct `uv run uipath`, for coded-agent run/init/deploy commands.
   - Keep `UiPath()`, `UiPathChat`, `UiPathAzureChatOpenAI`, retrievers, and other auth-dependent clients out of module scope.

2. Scaffold or reuse the coded-agent project.
   - Prefer LangGraph with `uipath-langchain`.
   - Keep `langgraph.json` mapped to `./main.py:graph` unless the existing project already uses another valid runtime file.
   - Do not add a Python `[build-system]` section.

3. Implement the agent architecture.
   - Define Pydantic `GraphInput` and `GraphOutput`.
   - Define state only as needed to pass the prompt, messages, and final result through the single node.
   - Build `StateGraph(..., input_schema=GraphInput, output_schema=GraphOutput)`.
   - Add one node, normally `run_agent`.
   - Add only `START -> run_agent -> END`.
   - Compile to a module-level variable named `graph`.

4. Add Context Grounding as a tool.
   - Use `ContextGroundingRetriever` from `uipath_langchain.retrievers`.
   - Pass the exact user-provided index name and folder path or folder key.
   - Wrap retrieval in an async LangChain tool with a clear docstring explaining what the index contains.
   - Return concise retrieved excerpts and source metadata when available.
   - Treat empty results as a first-class demo outcome, not an exception to hide.

5. Add harmful-content guardrails as middleware.
   - Before writing guardrail code, follow the current `uipath-agents` guardrails guidance and fetch current UiPath guardrail docs.
   - Check `uip agent guardrails list --output json` for built-in AI validator availability before adding an AI-backed validator.
   - For LangChain or LangGraph agents, import guardrail symbols from `uipath_langchain.guardrails`, not `uipath.platform.guardrails`.
   - Use the docs-current harmful-content middleware class and spread it into `create_agent(..., middleware=[...])`.
   - Prefer block behavior for harmful content in demos unless the user asks for logging-only behavior.
   - Verify the LangChain guardrail adapter is registered and the guarded object is actually wrapped.

6. Build the LangChain agent inside the node.
   - Instantiate the UiPath-backed chat model inside `run_agent`.
   - Create the Context Grounding tool and optional tools inside `run_agent` or inside short helper factories called by it.
   - Call `create_agent(model=..., tools=[context_tool, *optional_tools], system_prompt=..., middleware=[...])`.
   - Use structured response support when available; otherwise validate the final answer into `GraphOutput` explicitly.
   - Return the full output object from the terminal node. Do not rely on LangGraph reducers for final output fields.

7. Sync coded-agent metadata and bindings.
   - Run `uip codedagent init` after schema, entrypoint, or graph configuration changes.
   - Sync `bindings.json` after any UiPath SDK or LangChain resource call, especially Context Grounding indexes, buckets, connections, processes, apps, MCP servers, queues, and assets.
   - Treat dynamic resource names or folder paths as blockers unless the user confirms a manual binding strategy.

8. Add demo evidence.
   - Create or update a representative `input.json` unless the repo already has an equivalent fixture.
   - Add a smoke evaluation set with two or three primary-path cases.
   - Keep test data realistic enough to show Context Grounding and guardrails, but do not include credentials or tenant-specific secrets.

9. Validate.
   - Run local import/schema checks through `uip codedagent init`.
   - Run the agent with `uip codedagent run <entrypoint> --input-file input.json` or equivalent JSON input.
   - Inspect the output JSON, not only streamed terminal text.
   - Run the smoke eval with `uip codedagent eval <entrypoint> evaluations/eval-sets/smoke-test.json --no-report` when evaluations are in scope.
   - If JavaScript files are modified, run `npm test`.
   - Follow the `uipath-agents` delivery/deployment fork; do not push, upload, or deploy unless the user chooses that path.

## Demo Defaults

- Prefer one clear demo story over broad feature coverage.
- Prefer exact field names supplied by the user over generic schema names.
- Prefer one Context Grounding tool plus one or two high-signal optional tools.
- Keep prompts explicit about when the agent must use Context Grounding before deciding.
- Include source references in the output when the demo depends on retrieved knowledge.
- Surface missing evidence, policy ambiguity, and low confidence in the output schema.
- Avoid production hardening unless it is required for the demo to run.

## Response Contract

When finished, report:

- files changed
- architecture choices and any user-provided inputs used
- Context Grounding index and folder binding status
- guardrail availability and verification result
- validation commands and outcomes
- remaining runtime inputs or deployment choices, if any
