# Edge Functions Specification

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

Use server-side functions for privileged operations, external API secrets, payment orchestration, signed webhooks, and operations that must not run in the mobile client.

Functions MUST:
- validate input
- authenticate/authorize
- apply rate limits where exposed
- log request IDs
- redact sensitive values
- return stable errors
