# Definition of Done

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

A task is Done only when all applicable criteria are satisfied:

1. Requirement mapped to code/tests.
2. Existing behavior preserved unless intentionally changed.
3. Automated tests added/updated.
4. Typecheck/lint/build checks pass where applicable.
5. Security impact reviewed.
6. Documentation updated.
7. Error/loading/empty states implemented.
8. Accessibility considered.
9. Telemetry/analytics considered.
10. Diff inspected for unrelated changes.
11. No secrets or debug artifacts committed.
12. Exact verification evidence recorded.

An agent MUST NOT claim completion if any required gate is unknown or failing.
