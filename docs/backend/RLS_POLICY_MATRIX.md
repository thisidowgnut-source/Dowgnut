# RLS Policy Matrix

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

| Resource | anon | authenticated | service/backend |
|---|---|---|---|
| catalog | read published | read published | full |
| inventory | no direct write | no direct write | controlled |
| own cart | session rules | own only | controlled |
| own orders | no | own only | controlled |
| profiles | public/minimal | own | controlled |
| audit_events | no | no | write/read as authorized |

RLS is the authorization boundary for client-visible database access. Service credentials MUST never be exposed to the client.
