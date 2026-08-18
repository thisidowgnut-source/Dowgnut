# Doughnut Flava Architecture

- `app/` — Expo / React Native client
- `agent/` — Google ADK development agent with AG-UI middleware
- future `backend/` — Supabase database/auth/business APIs

The development agent is provider-agnostic at the orchestration layer and defaults to NVIDIA NIM through ADK's LiteLLM connector.

Agent loop: inspect → plan → implement → verify → diff → update docs/tasks → approval for medium-risk actions.

Risk gates:
- Low: read/search/test/typecheck/diff — automatic.
- Medium: package install, branch/commit/push — approval.
- High: destructive git/db, production deploy, force push, package publish — blocked.

AG-UI and A2UI should reuse upstream middleware/examples rather than recreate protocol plumbing.
