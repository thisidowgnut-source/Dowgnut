# Dowgnut Documentation

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

Dowgnut is an AI-native commerce platform with two first-class systems: the customer product experience and the autonomous development platform.

## Documentation objectives
This documentation set is an engineering contract for product, design, frontend, backend, agents, security, QA, operations, and release work. It is intended to be consumed by humans and coding agents.

## Normative language
The keywords MUST, MUST NOT, REQUIRED, SHOULD, SHOULD NOT, and MAY are used as normative requirements. They are interpreted in their ordinary engineering specification sense.

## Documentation hierarchy
1. Product truth: `docs/product/`
2. System truth: `docs/architecture/`
3. Agent truth: `docs/agents/`
4. Implementation truth: source code and tests
5. Operational truth: `docs/operations/`
6. Decision truth: `docs/adr/`

When two documents conflict, the higher-level source of truth wins unless an ADR explicitly supersedes it.

## Start here
- `docs/00_DOCUMENTATION_INDEX.md`
- `docs/product/PRD.md`
- `docs/architecture/SYSTEM_ARCHITECTURE.md`
- `docs/agents/MASTER_AGENT_PROMPT.md`
- `docs/engineering/DEFINITION_OF_DONE.md`
- `docs/product/ROADMAP.md`

## Repository map
- `app/` Expo / React Native client
- `agent/` development-agent runtime
- `docs/` project documentation
- future `backend/` Supabase assets
- future `packages/` shared contracts and UI primitives
