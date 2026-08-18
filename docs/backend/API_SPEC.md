# API Specification

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Principles
- version business contracts
- validate all inputs
- return stable error codes
- do not expose internal database schema unnecessarily
- use idempotency for retryable commands such as order creation

## Error envelope
```json
{
  "error": {
    "code": "inventory_conflict",
    "message": "Requested quantity is unavailable.",
    "request_id": "..."
  }
}
```

## Commands
- create/update cart
- validate cart
- create order intent
- confirm order
- retrieve order
- invoke agent action

All money values in APIs MUST use minor units or explicit decimal strings; never ambiguous floating point values.
