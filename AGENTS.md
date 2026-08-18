# Repository Instructions for AI Agents

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Mission
Build Dowgnut as an AI-native commerce platform while preserving product intent, security, and maintainability.

## Required preflight
Before editing:
1. inspect git status
2. read `docs/00_DOCUMENTATION_INDEX.md`
3. read the relevant product and architecture docs
4. inspect existing implementation before adding new abstractions
5. identify reusable upstream patterns

## Required postflight
After editing:
1. run targeted tests
2. run typecheck/lint or equivalent
3. inspect diff
4. update docs/tasks if needed
5. report exact verification evidence

## Hard rules
Never expose secrets. Never claim checks passed without running them. Do not weaken security controls to unblock delivery. Prefer composition of existing AG-UI/ADK capabilities over protocol rewrites.
