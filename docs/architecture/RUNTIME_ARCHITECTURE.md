# Runtime Architecture

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Client runtime
Expo / React Native with file-based navigation.

## Agent runtime
Google ADK orchestrates agent logic. AG-UI provides the event-based agent-to-frontend boundary. Model access is abstracted behind a provider adapter, defaulting to NVIDIA NIM.

## Backend runtime
Supabase supplies Postgres, Auth, storage, and server-side functions as required.

## Event flow
Run start → streamed text/tool events → state snapshot/delta → tool result → completion/error.

AG-UI tool and state events MUST be processed in order and correlated by event identifiers as required by the protocol.
