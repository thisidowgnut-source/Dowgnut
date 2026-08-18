# Order State Machine

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Example lifecycle
DRAFT → PENDING_PAYMENT → PAID → PREPARING → READY → COMPLETED

Terminal states:
CANCELLED, PAYMENT_FAILED, REFUNDED.

Transitions MUST be explicit and validated server-side. Client UI may display state but MUST NOT authoritatively change order state.
