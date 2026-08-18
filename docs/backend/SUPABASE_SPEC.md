# Supabase Specification

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

Supabase provides Postgres, Auth, storage, and server-side capabilities.

## Rules
- exposed tables MUST have RLS enabled
- service-role/secret keys MUST remain server-side
- authorization policies MUST be least privilege
- migrations MUST be version-controlled
- production schema changes MUST be backwards-aware

Auth uses JWT-based identity. Application tables SHOULD reference the authenticated user identity through stable foreign keys rather than duplicating identity data.
