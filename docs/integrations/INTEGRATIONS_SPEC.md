# Integration Specification

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

Every integration MUST have an adapter with explicit boundaries.

Adapter requirements:
- auth strategy
- configuration
- timeout
- retry policy
- rate-limit handling
- error mapping
- telemetry
- test strategy
- data retention implications

External provider outages MUST degrade gracefully and MUST NOT corrupt authoritative order/inventory state.
