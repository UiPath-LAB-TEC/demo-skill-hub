# Example Flow Pattern

This pattern distills the reusable parts of the invoice contract validation demo flow. Do not copy tenant-specific IDs, connector payloads, or resource names. Recreate the shape with the current tenant's available resources. For a node-and-edge-level version, read [sanitized-example-flow.md](sanitized-example-flow.md).

## Narrative

An invoice enters the process, gets downloaded and extracted, is checked for duplicates, enriched with PO data, validated by several agents, reviewed by a human, then routed to payment creation or vendor notification.

## Reusable Sequence

1. Start with `New Invoice`.
2. Ingest or retrieve the document.
3. Extract invoice details. Prefer an IXP document extraction node in new demos.
4. Run an early duplicate or quality check.
5. Branch for exceptions or vendor notification.
6. Pull related business data through an API workflow.
7. Run a multi-agent validation block:
   - Inline agent with tool and context grounding.
   - Published or coded agent for a specialized check.
   - External agent or connector-backed agent on a branch when useful.
8. Merge agent outcomes.
9. Decide whether the item is validated.
10. Send the decision to HITL.
11. Route approved items to normalization and final system action.
12. Route rejected or exception items to notification and close.

## Example Actor Inventory

- Manual trigger for a simple demo entry point.
- RPA for invoice retrieval and extraction in the source example.
- API workflow for PO data lookup.
- Inline GL coding agent with web search and a GL coding index.
- Published agents for invoice-PO validation and contract discrepancy checking.
- Coded agent for duplicate invoice checking.
- External Google Vertex agent for vendor-email reasoning.
- Outlook connector for notifications.
- Quick Form or coded action app for human review.
- Script and HTTP actions for final payment preparation and creation.
- Decisions, merge, and multiple end nodes for visible routing.

## Layout Pattern

- Use a main horizontal path from trigger to close.
- Put ingestion at the far left under a green sticky note.
- Put the agent validation block in the center under a large blue sticky note.
- Put HITL to the right under a yellow sticky note.
- Put final actions and close paths at the far right under a neutral sticky note.
- Keep tool and context nodes attached close to the inline agent so the customer can see grounded agentic reasoning.
