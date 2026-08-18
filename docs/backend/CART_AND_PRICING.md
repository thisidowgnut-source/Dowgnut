# Cart and Pricing Rules

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

Cart calculations MUST use authoritative server-side prices.

Use integer minor units and explicit currency.

At checkout:
1. re-read pricing
2. re-check inventory
3. validate discounts
4. calculate totals
5. create idempotent order intent
6. proceed to payment flow

Client totals are presentation only.
