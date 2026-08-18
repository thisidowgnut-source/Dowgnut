# Secrets and Credentials

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Secrets
Examples: API keys, service-role keys, private OAuth secrets, signing secrets, database passwords.

## Rules
- local development uses ignored `.env` files
- CI uses secret stores
- production secrets are injected by the deployment platform
- secrets MUST NOT be logged
- rotation procedures MUST exist before production use

The mobile app may contain public/publishable identifiers, but never service-role or server secret keys.
