# ADR-0001: Agent Provider Abstraction

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Status
Accepted.

## Context
Dowgnut wants NVIDIA NIM as its default model provider without coupling business logic to one vendor.

## Decision
Introduce a provider abstraction at the agent runtime boundary. NVIDIA is default through configuration.

## Consequences
Provider changes require adapter compatibility tests. Provider-specific features remain behind capability checks.
