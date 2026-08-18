# Privacy and Data Classification

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Classes
- Public: catalog marketing content
- Internal: operational metrics and non-public product plans
- Sensitive: user identity, addresses, order history
- Restricted: payment tokens, service credentials, security findings

Sensitive and restricted data MUST have explicit access rules, retention expectations, and logging restrictions.

Do not put personal data into agent prompts unless required for the task and authorized.
