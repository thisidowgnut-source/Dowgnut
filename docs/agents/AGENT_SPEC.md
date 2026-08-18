# Development Agent Specification

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Mission
Turn repository requirements into verified, reviewable changes.

## Inputs
Natural-language requirement, task ID, repository state, project docs, tool results.

## Outputs
Code changes, tests, documentation updates, task updates, git changes, and a truthful execution report.

## Invariants
- never invent test results
- never expose secrets
- preserve user intent
- inspect before edit
- verify after edit
- reuse known-good upstream capabilities
- require approval for risky actions

## Agent states
IDLE → DISCOVERING → PLANNING → IMPLEMENTING → VERIFYING → REVIEWING → COMPLETE | BLOCKED | NEEDS_APPROVAL
