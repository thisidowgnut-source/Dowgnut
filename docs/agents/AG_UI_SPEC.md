# AG-UI Specification

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

AG-UI is the agent-to-frontend event boundary.

## Required behaviors
- stream text incrementally
- stream tool-call lifecycle events
- correlate events using protocol IDs
- support state snapshots and deltas
- surface run errors cleanly
- maintain cancellation behavior
- avoid coupling UI components to model-specific payloads

The implementation SHOULD reuse the upstream protocol and middleware rather than reimplement event schemas.
