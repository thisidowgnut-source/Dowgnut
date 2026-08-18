# CI/CD

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Continuous checks
At minimum:
- dependency install
- lint
- typecheck
- unit tests
- agent tests
- build validation for affected app targets

## Delivery
Main branch should remain buildable.

Release pipelines MUST be repeatable and environment-specific.

Deployment credentials MUST be isolated from developer credentials.
