# OAuth and Webhooks

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

OAuth integrations MUST request minimum scopes. State and nonce protections are required where applicable.

Webhook handlers MUST:
- authenticate requests or verify signatures
- reject replay when the provider supports timestamps/nonces
- validate payloads
- be idempotent
- record provider event IDs
- avoid leaking secrets in logs
