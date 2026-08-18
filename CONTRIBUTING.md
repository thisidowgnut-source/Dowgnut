# Contributing to Dowgnut

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Scope
Contributions may affect application code, agent code, documentation, database migrations, integrations, or infrastructure.

## Workflow
1. Read the relevant product and architecture docs.
2. Search existing issues/tasks before creating new work.
3. Keep changes narrowly scoped.
4. Add or update tests for behavior changes.
5. Run the repository quality gates.
6. Update documentation when behavior or architecture changes.
7. Use clear commit messages.
8. Provide an honest PR summary including test evidence.

## AI-assisted development
AI coding tools and autonomous agents are permitted. Any agent-authored change MUST still satisfy the same tests, review, security checks, and documentation requirements as human-authored code.

## Change categories
- `feat`: user-visible functionality
- `fix`: defect correction
- `refactor`: behavior-preserving code change
- `docs`: documentation only
- `test`: tests only
- `chore`: tooling/infrastructure
- `security`: security hardening

## Do not
- commit secrets
- bypass failing checks
- weaken RLS to unblock a feature
- add hidden network calls
- modify production data manually
- rewrite working upstream protocol plumbing without a documented reason
