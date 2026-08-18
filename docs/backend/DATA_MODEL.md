# Data Model

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Core entities
### products
id, slug, name, description, price_minor, currency, status, metadata.

### product_variants
id, product_id, name, price_delta_minor, availability.

### inventory
product/variant reference, quantity_available, reserved_quantity, updated_at.

### carts
id, user_id or session_id, currency, status, created_at, updated_at.

### cart_items
cart_id, product_id/variant_id, quantity, unit_price_snapshot_minor.

### orders
id, user_id, currency, subtotal_minor, total_minor, status, payment_status, fulfillment_status.

### order_items
order_id, product_id, quantity, unit_price_minor, product_name_snapshot.

### agent_threads
id, user_id, provider, metadata, created_at.

### agent_runs
thread_id, status, model, started_at, finished_at, error_code.

### audit_events
actor, action, resource_type, resource_id, metadata, created_at.

Money MUST be stored in integer minor units. Never use floating point for authoritative monetary totals.
