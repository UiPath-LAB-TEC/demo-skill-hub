# Build the agent

## UiPath LangChain Document Validator Agent

Build a demo-grade UiPath Coded Agent using `uipath-langchain`, LangChain `create_agent()`, and a thin LangGraph wrapper.

Use the `uipath-agents` skill. The agent should be ready to push to Studio Web as a solution, but do not push it yet.

## Architecture

Implement the agent as a LangChain ReAct agent wrapped by a minimal LangGraph workflow.

- Use Pydantic models for structured UiPath input and output schemas.
- Use one LangGraph node only, for example `run_validator_agent`.
- The LangGraph shape should be `START -> run_validator_agent -> END`.
- Do not create separate LangGraph nodes for Context Grounding, web search, and final assessment.
- Inside the single node, create a LangChain agent with `langchain.agents.create_agent()`.
- Attach both tools to the LangChain agent so the ReAct loop decides when to call them.
- Use `response_format=ValidationOutput` and return the structured response as the final UiPath output.

## Inputs

The agent receives structured data extracted upstream:

- `utility_bill_business_name`
- `utility_bill_business_address`
- `business_license_type`
- `certificate_good_standing_business_name`

Create an `input.json` file at the project root with one representative payload matching this schema so the agent can be tested with file input, for example:

```powershell
uip codedagent run agent --input-file input.json
```

## Tools

Attach these as LangChain tools to `create_agent()`:

- Context Grounding tool:
  - Uses UiPath Context Grounding index `KYC_DocVal_AgentCG`
  - Folder path: `AMER Presales/FINS`
  - Implement as a LangChain tool that queries the index for operating procedure guidance.

- Web Search MCP tools:
  - MCP server name: `web-search`
  - URL: `https://staging.uipath.com/uipathlabs/Playground/agenthub_/mcp/dc28419a-6c8c-45d5-9e6b-7de1ab2336b9/web-search`
  - Load the MCP tools through a small async context manager, for example `get_kyc_validator_tools()`.
  - In that context manager, validate the UiPath MCP environment, resolve the KYC validator folder path, set `UIPATH_FOLDER_PATH` when missing, then call `open_mcp_tools([get_kyc_validator_mcp_config()])`.
  - Use `async with get_kyc_validator_tools() as mcp_tools:` inside the LangGraph node before calling `create_agent()`.
  - Do not load MCP tools at module import time.

## Agent Behavior

The LangChain agent should:

- Compare the utility bill business name against the Certificate of Good Standing business name.
- Use Context Grounding to determine the operating procedure rules for name matching and license appropriateness.
- Use web search to validate business intent and whether the business appears to operate at the supplied address.
- Be conservative when evidence is missing or contradictory.

## Outputs

Return this structured output:

- `business_name_match`: boolean
- `business_license_type_match`: boolean
- `business_exists_at_address`: boolean
- `risk_summary`: string
- `rationale`: string

## Implementation Notes

Use `UiPathAzureChatOpenAI` or the tenant-supported UiPath LangChain chat model inside the graph node, not at module import time.

The core pattern should be:

```python
agent = create_agent(
    model=model,
    tools=[context_grounding_tool, *mcp_tools],
    system_prompt=system_prompt,
    response_format=ValidationOutput,
)

result = await agent.ainvoke({"messages": messages})
return ValidationOutput.model_validate(result["structured_response"]).model_dump()
```


Keep it as simple as possible. This is demo-grade only.
