# NVIDIA NIM Specification

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Default
Use the configured NVIDIA NIM OpenAI-compatible endpoint through the agent provider adapter.

Configuration:
- `NVIDIA_API_KEY`
- `NVIDIA_BASE_URL`
- `NVIDIA_MODEL`

The current preferred model may change. Model availability and free-endpoint limits MUST be treated as external dependencies, not guaranteed product capabilities.

## Operational requirements
- timeout
- retry only safe requests
- rate-limit handling
- circuit breaking where necessary
- model name recorded in agent run telemetry
