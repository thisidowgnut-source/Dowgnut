# ADR-0002: Reuse Upstream Agent Protocols

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Status
Accepted.

## Context
AG-UI/ADK/A2UI upstream examples and middleware already solve protocol plumbing.

## Decision
Reuse and adapt upstream implementations instead of rewriting protocol schemas or transport.

## Consequences
We track upstream compatibility, pin versions when necessary, and isolate adapters.
