# Provider Policy

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

The application MUST separate business logic from model/provider APIs.

Current default AI provider: NVIDIA NIM.

Provider configuration is environment-driven. Switching providers SHOULD require configuration changes plus compatibility tests, not business-logic rewrites.

Never commit API keys, model secrets, OAuth client secrets, or private webhook signing secrets.
