# Readiness Checklist

Use this checklist before marking a demo ready.

## Repo And Artifact State

- Current branch and uncommitted changes understood.
- Target solution folder identified.
- App, agent, RPA, orchestration, and data artifacts located.
- Generated caches and old packages not confused with current source.

## Local Checks

- JavaScript tests pass after JavaScript changes.
- App build passes when app code changed.
- Flow, Case, BPMN, RPA, and agent validation pass where applicable.
- Fixtures load and match documented contracts.

## Cloud Checks

- `uip login status --output json` confirms the intended tenant.
- Target folder and package versions are correct.
- Resources are refreshed before packaging.
- Deployment output uses current package versions.
- Connector bindings are healthy or documented as mocked.
- Action Center task renders deployed payload.

## Safety Checks

- Outbound recipients are demo-approved.
- Sample data is safe.
- Credentials and secrets are not committed.
- Mocked surfaces are labeled in internal notes.

## Readiness Decision

Mark ready only when the presenter can run the advertised scenario paths or has an explicit fallback for each missing live path.
