# UiPath SE Skills Library

Reusable Codex skills for Sales Engineers turning customer discovery into credible UiPath demos and customer-facing artifacts.

## Skills

- `uipath-se`: Route Sales Engineering requests to the narrowest skill in this library.
- `uipath-se-account-research`: Build account and process research briefs for demo planning.
- `uipath-se-discovery`: Convert customer calls, notes, diagrams, and rough use cases into structured discovery.
- `uipath-se-end-to-end-demo`: Build artifact-first, runnable UiPath presales demos and solution showcases.
- `uipath-se-demo-readiness`: Validate, rehearse, reset, and package demos before customer delivery.
- `uipath-se-executive-artifacts`: Create slides, one-pagers, demo scripts, capability maps, and executive summaries.
- `uipath-se-scale-maestro-demo`: Scale and operate an already deployed Maestro BPMN process, including controlled batch starts and instance lifecycle actions.
- `build-uipath-end-to-end-demo`: Legacy shared build skill retained for existing prompts.

## Example Prompt

```text
Use the UiPath SE skills library in shared-components/skills to turn this customer discovery into a reusable end-to-end demo plan, readiness checklist, and executive-facing artifacts.
```

To let the router choose the right specialist skill:

```text
Use the uipath-se skill in shared-components/skills to route this request.
```

To use an individual skill:

```text
Use the uipath-se-discovery skill in shared-components/skills to analyze this customer transcript.
```
