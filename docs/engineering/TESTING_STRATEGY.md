# Testing Strategy

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Test pyramid
- unit: calculations, reducers, validators, domain logic
- integration: Supabase/API/agent tool boundaries
- contract: API and event payloads
- E2E: critical customer journeys
- visual regression: key screens against approved references
- agent evaluations: task success, tool correctness, safety

## Critical tests
Catalog availability → cart → checkout validation → order creation; AI proposal → human approval → cart mutation.

Tests MUST be deterministic where possible and test failure modes, not only happy paths.
