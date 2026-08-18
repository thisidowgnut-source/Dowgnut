# Development Agent Workflow

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Discovery
Read task → identify affected domains → inspect tests and existing patterns.

## Planning
Produce a dependency-aware plan. Avoid parallel edits to the same files.

## Implementation
Prefer small, composable changes. Keep feature flags for risky user-facing changes when appropriate.

## Verification
Run unit tests → integration tests → typecheck/lint → build or platform check → inspect diff.

## Recovery
If verification fails:
1. capture failure
2. determine root cause
3. make smallest fix
4. rerun the failing check
5. rerun affected broader checks

## Delivery
Update task status, docs, changelog when required, then commit/push according to repository delivery policy.
