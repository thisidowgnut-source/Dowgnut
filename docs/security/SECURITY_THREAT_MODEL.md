# Security Threat Model

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Assets
Identity tokens, customer data, order data, inventory truth, payment information, provider credentials, GitHub credentials, agent execution capability.

## Threat actors
Unauthenticated internet user, malicious authenticated user, compromised dependency, prompt-injection attacker, malicious repository content, compromised external provider.

## Controls
Authentication, RLS, least privilege, secret isolation, input validation, sandboxing, approval gates, dependency scanning, audit logs, rate limits, and safe retries.

## Highest-risk paths
- agent shell execution
- GitHub write operations
- payment/checkout
- service-role database access
- webhook handling
