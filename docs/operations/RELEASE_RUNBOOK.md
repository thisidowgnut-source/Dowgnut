# Release Runbook

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

1. Confirm scope and changelog.
2. Confirm migration safety.
3. Run full required checks.
4. Validate environment configuration.
5. Verify monitoring.
6. Deploy.
7. Run smoke tests.
8. Monitor error rates and critical journeys.
9. Announce release.
10. Keep rollback path available.

A release touching auth, RLS, payments, or order state requires explicit verification of those boundaries.
