# Process-Agnostic Fixture Patterns

The bundle intentionally does not include executable fixture JSON. Maestro start-event schemas differ by process, so a supposedly reusable sample could be rejected or, worse, map plausible values to the wrong inputs.

## Derive the Contract First

Inspect the deployed start event and record:

- Required and optional input names.
- Exact JSON types.
- Allowed values and formats.
- Cross-field constraints.
- Which values select branches, waits, faults, or human tasks.
- Which values can cause external side effects.

Create fixtures only after comparing this contract with the deployed process version.

## Single-Object Shape

Use one JSON object when every planned start should receive the same payload:

```json
{
  "<requiredStringInput>": "synthetic-value",
  "<requiredNumberInput>": 100,
  "<optionalBooleanInput>": false
}
```

Replace every placeholder key and value. Do not execute the example verbatim.

## Array Shape

Use an array when fixtures belong in one file:

```json
[
  {
    "<inputName>": "synthetic-path-a"
  },
  {
    "<inputName>": "synthetic-path-b"
  }
]
```

With the `cycle` strategy, the planner rotates through array items in their existing order.

## Directory Shape

Use one object per file when reviewers should see and approve scenarios separately. Name files so lexical order expresses the intended cycle:

```text
fixtures/
|-- 01-happy-path.json
|-- 02-alternate-branch.json
|-- 03-validation-path.json
|-- 04-long-running-path.json
`-- 05-controlled-fault.json
```

The planner sorts `.json` filenames before applying `cycle` or `first`.

## Useful Scenario Categories

Choose only categories supported by the target BPMN:

- Happy path reaching a normal terminal state.
- Alternate business branch.
- Validation or missing-information path.
- Human approval or task wait.
- Timer, message, queue, or other long-running wait.
- Controlled transient failure with known side effects.
- Boundary values for numeric or enumerated inputs.

Do not invent branches merely to fill a generic fixture set.

## Distribution

`cycle` repeats fixtures evenly only when the requested count is divisible by the fixture count. Otherwise, earlier fixtures receive one additional ordinal. Review the materialized plan rather than assuming an even distribution.

`first` always uses the first sorted fixture or first array item.

## Synthetic Data

- Use clearly synthetic identifiers and values.
- Avoid credentials, tokens, personal data, customer exports, and production URLs.
- Make intentional duplicates explicit when testing idempotency.
- Do not add correlation fields unless the deployed schema accepts them.
- Account for every connector, notification, queue, task, robot, and external write multiplied by the run count.

