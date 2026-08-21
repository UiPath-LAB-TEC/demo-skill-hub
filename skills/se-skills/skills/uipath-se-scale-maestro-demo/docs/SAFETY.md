# Safety and Governance

## Read-Only by Default

Discovery, fixture inspection, plan generation, dry-run validation, and instance inspection are read-only or local. Starting, retrying, migrating, goto, canceling, or otherwise changing an instance requires bounded approval.

## Bounded Approval

Before mutation, present:

- Organization and tenant.
- Folder and folder key.
- Process name, key, and version.
- Operation and exact instance count or IDs.
- Concurrency, delay, and fixture distribution.
- Connector, queue, task, robot, message, and external-system side effects.
- Canary rule and stop conditions.
- Migration version or goto transitions when applicable.

Approval for one batch does not authorize another count, target, version, fixture set, or lifecycle action.

## Tenant and Folder Isolation

Never choose a cloud target from a copied sample, an “approved” label, or the active login alone. Discover the live process in the intended folder and verify its identifiers immediately before mutation.

The runner fingerprints process key, folder key, release key, and feed ID. Resume matching uses that fingerprint, but the operator must still verify organization and tenant because they are controlled by the authenticated CLI context.

## Side-Effect Multiplication

A count of 100 may produce 100 or more emails, tasks, queue items, robot jobs, connector requests, or external writes. Inventory these effects before choosing fixtures and concurrency.

Prefer synthetic fixtures, mock integrations, isolated queues, and non-production folders. Do not assume a demo label makes external connections harmless.

## Concurrency

Start conservatively. Increase concurrency only in a newly approved, unexecuted plan after considering:

- Tenant and service throttling.
- Connector API limits.
- Robot and license capacity.
- Queue and Action Center load.
- Downstream system limits.
- Evidence volume and operator response time.

The safest useful concurrency is usually more important than the maximum possible concurrency.

## Secrets and Sensitive Data

Never store access tokens, cookies, credentials, private tenant URLs, or unredacted sensitive payloads in plans, fixtures, logs, or screenshots.

The runner inherits authentication from UiPath CLI and does not accept tokens as arguments. Review fixture contents and raw stderr/stdout before sharing evidence externally.

## Canary Requirement

Use one canary when side effects, bindings, a new version, or target capacity have not already been validated for the exact batch. Verify:

- Correct folder and package version.
- Stable instance ID.
- Expected variables.
- Expected initial state or terminal route.
- Expected side effects only.

Stop if the canary differs. Do not “fix forward” by launching the rest first.

## No Automatic Retry

A failed start may be safe to submit again, but the runner does not assume that. An instance failure may have partially completed external effects. Diagnose and obtain approval before retrying.

## Browser Boundary

Playwright is permitted only for a UI-only capability after CLI and documented API options are exhausted. Reuse an authorized session; never automate passwords or MFA, bypass permissions, or turn an API validation failure into blind UI clicking.

## Evidence Retention

Retain the plan, generated inputs, target fingerprint, normalized ledger, raw CLI results, summary, and final state verification for the period appropriate to the demo or test. Sanitize evidence before sharing it beyond the authorized audience.
