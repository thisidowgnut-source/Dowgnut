# Development Agent Tool Contract

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Read tools
- `repo_list`
- `repo_read`
- `repo_search`

## Edit tools
- `repo_create`
- `repo_patch`

## Verification tools
- `run_command`
- `run_tests`
- `run_typecheck`
- `run_lint`
- `run_build`

## Git tools
- `git_status`
- `git_diff`
- `git_commit`
- `git_push`

## GitHub tools
Issues and PRs MAY be exposed through a dedicated adapter. Every write operation MUST include a safe operation mode and audit record.

## Tool contract
Every tool must declare:
- input schema
- authorization requirement
- side effects
- timeout
- retry semantics
- audit event
- failure behavior
