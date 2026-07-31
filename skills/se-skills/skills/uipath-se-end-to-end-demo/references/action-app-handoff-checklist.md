# Action App Handoff Checklist

Use this checklist whenever the implemented demo includes a UiPath Coded Action App or Action Center human review step.

## Before Building

- Confirm the app is a Coded Action App, not a Coded Web App.
- Place the app source under the same solution folder tree, usually `action-app/`.
- Define the action input schema from the same data contracts used by orchestration.
- Define the action output schema as a durable `ReviewDecision`.
- Keep local fixtures shaped like real deployed task data, not only convenient UI state.

## Input Normalization

Normalize the inbound payload before rendering:

- Read from `task.data` when running in Action Center.
- Read from local fixture query parameters when running locally.
- Convert missing arrays to empty arrays.
- Convert missing objects to empty objects or safe defaults.
- Convert missing strings to empty strings or labeled placeholders.
- Keep raw payload available for debug display or test assertions when useful.

Common arrays that must be guarded:

- Evidence summaries.
- Document lists.
- Missing items.
- Guidelines.
- Citations.
- Agent findings.
- Recommended downstream actions.
- Audit events.

## Review Submission

The submit handler must:

- Capture the selected decision.
- Capture reviewer comments.
- Include missing information requests or override reasons.
- Include the current scenario id, case id, and recommendation id when available.
- Return a complete `ReviewDecision` payload to Action Center.
- Show pending, success, and error states.

Do not complete the task through CLI or API automation when the user wants to provide the review decision themselves.

## Orchestration Wiring

Verify:

- The human review step points to the deployed action app or correct task schema.
- The input payload matches the app's expected schema.
- The `completed` path resumes the flow.
- Downstream expressions read output fields by the correct output field ids.
- The review result updates the case/work item audit trail.

## Debugging Symptoms

If the app does not display:

- Check browser console for undefined `.map()` or missing nested object errors.
- Confirm deployed task payload shape matches local fixture shape or is normalized.
- Confirm Vite uses relative base paths for coded app assets.
- Confirm the app was published as type `Action`.
- Confirm the task references the deployed app version intended for the test.

If the submit button appears to do nothing:

- Check the submit handler is bound to the visible button.
- Check required fields are not silently failing validation.
- Check the Action Center completion call returns success.
- Check errors are surfaced in the UI.
- Check output field names match orchestration expectations.
