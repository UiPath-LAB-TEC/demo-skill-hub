# UiPath Demo Artifact Map

Use this map to choose the simplest artifact set that can carry the demo story. Name the selected skills in `SPEC.md` so the builder knows what to open.

| Demo need | Likely artifact | Builder skill |
|---|---|---|
| Visual workflow orchestration, connector nodes, Flow tools, inline agents, simple approvals | Maestro Flow `.flow` | `uipath-maestro-flow` |
| BPMN-style process orchestration, long-running process shape, generated project metadata | Maestro BPMN `.bpmn`, `project.uiproj` | `uipath-maestro-bpmn` |
| Desktop/web UI automation, Excel, email, documents, queues, legacy apps | RPA `.xaml` or coded `.cs` workflow | `uipath-rpa` |
| Legacy .NET Framework XAML project | Legacy RPA XAML | `uipath-rpa-legacy` |
| Low-code or coded reasoning agent, tool use, chat-style decisioning | `agent.json` or Python agent project | `uipath-agents` |
| Web app, action app, rich review UI, reusable Action Center experience | Coded App or Coded Action App | `uipath-coded-apps` |
| API-first automation or reusable HTTP/connector workflow | API Workflow JSON | `uipath-api-workflow` |
| Case stages, milestones, human-owned work, case plan | `caseplan.json` | `uipath-maestro-case` |
| Human approval, escalation, data correction, output review checkpoint | HITL task in Flow/Maestro/agent surface | `uipath-human-in-the-loop` |
| Runtime Action Center task operations | Existing tasks | `uipath-tasks` |
| Structured demo data, seeded records, attachments | Data Fabric entities/records/files | `uipath-data-fabric` |
| Assets, queues, buckets, packages, folders, triggers, connections, Orchestrator or Integration Service resources | Platform resources | `uipath-platform` |
| Multi-project packaging, publishing, deployment, activation | Solution `.uipx` | `uipath-solution` |
| Test cases, sets, executions, reports | Test Manager | `uipath-test` |
| Governance policy demo | Governance product or access policy | `uipath-governance` |
| Admin, identity, roles, audit, tenant lifecycle | Admin resources | `uipath-admin` |
| Document Understanding / IXP model review | IXP model and predictions | `uipath-ixp` |
| Read-only quality audit of built artifacts | Artifact review | `uipath-review` |
| Failure/root-cause investigation | Diagnostics and troubleshooting | `uipath-troubleshoot` |

Selection heuristics:

- Start from the demo promise, not from a preferred artifact.
- Prefer one primary artifact surface plus supporting resources.
- Use Flow when the viewer should see a live orchestration canvas.
- Use BPMN or Case when the story is about operational process management rather than node-level automation.
- Use RPA when the demo must touch applications or files through UI/workflow automation.
- Use Agents when reasoning or autonomous decisions are the main value.
- Use Coded Apps only when the human-facing UI matters to the demo.
- Use API Workflows only when API composition is itself part of the story.
- Use Platform, Data Fabric, Test Manager, and Solution packaging as supporting surfaces, not default scope.
