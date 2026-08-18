# Dowgnut Security Policy

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Reporting vulnerabilities
Do not disclose exploitable vulnerabilities in public issues.

Provide:
- affected component
- reproduction steps
- impact assessment
- relevant logs or traces with secrets removed
- proposed mitigation when known

## Security requirements
- Secrets MUST remain outside source control.
- Client applications MUST never contain service-role or server secret credentials.
- Database authorization MUST use least privilege and RLS where applicable.
- High-risk destructive operations MUST require explicit approval.
- Agent tool inputs MUST be validated at trust boundaries.
- External webhook signatures MUST be verified before processing.

See `docs/security/SECURITY_THREAT_MODEL.md` and `docs/security/SECRETS_AND_CREDENTIALS.md`.
