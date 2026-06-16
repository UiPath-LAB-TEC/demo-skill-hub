# Sanitized Example Flow

This is a sanitized excerpt of the invoice contract validation demo. Use it as a pattern for structure and storytelling. Do not copy IDs, `SolutionId`, `projectId`, connection IDs, resource IDs, tenant URLs, generated connector `detail` payloads, hard-coded users, or hard-coded email addresses.

## Canvas Summary

- 27 nodes, 25 edges, 4 sticky-note section bands.
- Main movement is left to right: invoice intake -> extraction -> duplicate check -> PO lookup -> multi-agent validation -> HITL -> payment or notification.
- The visual center is a multi-agent validation block with an inline agent, published agents, a tool, and a context source.
- A non-critical external-agent branch remains visible for customer storytelling even when it does not need to execute in every demo run.

## Sticky-Note Bands

| Band | Color | Purpose |
| --- | --- | --- |
| Ingestion | Green | Trigger, document retrieval, extraction, and duplicate check. |
| Multi-Agent Validation Pipeline | Blue | Agent reasoning, agent resources, PO lookup, and merge. |
| Human in the Loop | Yellow | Human review and approval routing. |
| Close | White or neutral | Final system action, vendor notification, and end states. |

## Sanitized Node Inventory

| Label | Generic type | Demo purpose |
| --- | --- | --- |
| New Invoice | Manual trigger | Simple, reliable demo entry point. |
| Download Invoice | RPA workflow | Shows UiPath execution for document intake. |
| Extract Invoice Data | IXP extraction preferred; RPA extraction fallback | Shows document understanding. |
| Duplicate Invoice Checker | Coded or published agent | Early risk check before expensive downstream work. |
| Duplicate? | Decision | Splits exception handling from normal processing. |
| Vendor Email Agent | External agent or connector-backed agent | Shows non-UiPath/third-party agent participation. |
| Notify Vendor | Connector activity | Shows business communication and exception closure. |
| Get PO Data | API workflow | Shows structured system integration. |
| GL Coding Agent | Inline agent | Shows agentic reasoning inside the Flow. |
| Web Search | Agent tool | Shows the inline agent can use tools. |
| GL Coding Index | Agent context source | Shows grounding against enterprise knowledge. |
| Invoice PO Validation Agent | Published or low-code agent | Specialized validation actor. |
| Contract Discrepancy Agent | Published or low-code agent | Second specialized validation actor. |
| Merge | Merge logic | Rejoins multiple validation outputs. |
| Validated? | Decision | Routes clean, exception, and review paths. |
| Human Review | Quick Form or coded action app | Proves HITL control over agentic work. |
| Approved? | Decision | Separates approved and rejected human outcomes. |
| Normalize Payment Data | Script action | Shows developer-friendly transformation. |
| Create Payment | HTTP action or connector | Shows final system execution. |
| Inform Vendor | Connector activity | Shows rejection or discrepancy notification. |
| End | End nodes | Keep each terminal path explicit. |

## Logical Edge Pattern

```text
New Invoice
  -> Download Invoice
  -> Extract Invoice Data
  -> Duplicate Invoice Checker
  -> Duplicate?

Duplicate? -> Vendor Email Agent -> Notify Vendor -> End

Duplicate? -> Get PO Data
Get PO Data -> GL Coding Agent
Get PO Data -> Invoice PO Validation Agent
Get PO Data -> Contract Discrepancy Agent

GL Coding Agent -> Web Search
GL Coding Agent -> GL Coding Index

GL Coding Agent -> Merge
Invoice PO Validation Agent -> Merge
Contract Discrepancy Agent -> Merge

Merge -> Validated?
Validated? -> Normalize Payment Data -> Create Payment -> End
Validated? -> Human Review -> Approved?
Approved? -> Normalize Payment Data -> Create Payment -> End
Approved? -> Inform Vendor -> End
```

## Reuse Rules

- Copy the story shape, not the implementation IDs.
- Keep an inline agent with at least one visible tool and one visible grounding source.
- Keep at least one specialized agent besides the inline agent.
- Keep HITL after agent reasoning and before final action.
- Prefer an IXP extraction node for new document demos; use RPA extraction only when IXP is unavailable or the demo already depends on RPA.
- Replace connector, agent, RPA, API workflow, and context-resource nodes with resources discovered in the current tenant.
