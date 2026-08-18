# Observability

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Logs
Structured logs with timestamp, level, service, request/run ID, event name, and safe metadata.

## Metrics
Track:
- app crashes
- API latency
- checkout failures
- inventory conflicts
- agent success/failure
- tool call latency
- model/provider errors

## Traces
Agent runs SHOULD correlate frontend events, backend requests, tool calls, and external provider calls through a shared request/run identifier.
