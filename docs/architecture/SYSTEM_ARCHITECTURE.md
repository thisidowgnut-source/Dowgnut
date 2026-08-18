# System Architecture

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Logical architecture
```text
Expo App
  ├── Product UI
  ├── Cart UI/state
  └── AG-UI client
          │
          ▼
AG-UI / Agent Runtime
          │
          ▼
Google ADK
  ├── Product Agent
  ├── Development Agent
  └── Tool layer
          │
    ┌─────┼────────────┐
    ▼     ▼            ▼
Supabase GitHub     External APIs
```

## Boundaries
- UI MUST NOT contain service-role secrets.
- Financial and inventory truth MUST live server-side.
- Agent tools MUST enforce authorization independently of model intent.
- External integrations MUST be behind adapters.

## State
UI state is ephemeral or synchronized application state. Database state is authoritative for products, inventory, orders, and identity.
