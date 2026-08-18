# Domain Architecture

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Domains
- Catalog: products, flavors, pricing, availability.
- Cart: cart, cart items, pricing snapshot.
- Order: order, order items, payment state, fulfillment state.
- Identity: user, profile, addresses, roles.
- Agent: thread, run, tool call, approval.
- Marketing: campaigns, content, attribution.
- Operations: alerts, audit records, feature flags.

Domain modules SHOULD expose stable interfaces and avoid reaching across domain internals.
