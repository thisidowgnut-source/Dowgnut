# Product Requirements Document

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## 1. Product summary
Dowgnut is a mobile-first doughnut commerce product with an AI-native customer experience and an independent development agent.

## 2. Goals
- Deliver a visually distinctive doughnut storefront.
- Enable browsing, product detail, cart, checkout, order history, and profile.
- Enable AI-assisted box composition.
- Enable autonomous development workflows with verification and approval gates.

## 3. Non-goals for MVP
- full ERP
- autonomous financial settlement
- unrestricted production deployment
- custom payment processor

## 4. Primary personas
- customer
- store operator
- developer/maintainer
- marketing operator

## 5. MVP capabilities
### Storefront
Flavor catalog, availability, price, detail, add-to-cart.

### Cart
Quantity changes, remove, subtotal, validation, checkout handoff.

### Account
Authentication, profile, order history.

### AI
Build My Box, recommendation, cart mutation, clarifying questions, approval.

### Development Agent
Repository inspection, coding tools, tests, quality gates, task management, GitHub integration.

## 6. Functional requirements
FR-001: User can browse available products.
FR-002: User can view product details.
FR-003: User can add products to a persistent cart.
FR-004: Cart totals MUST be derived from authoritative product pricing.
FR-005: Checkout MUST validate inventory and pricing before order creation.
FR-006: AI recommendations MUST NOT create orders without explicit user approval.
FR-007: Development Agent MUST run verification before claiming completion.
FR-008: Agent high-risk operations MUST be blocked or require approval.

## 7. Non-functional requirements
- secure authorization
- deterministic financial calculations
- accessible interactive controls
- observable agent runs
- graceful failure and retry
- mobile-responsive layout
- maintainable component boundaries

## 8. Acceptance
A feature is complete only when it satisfies `docs/engineering/DEFINITION_OF_DONE.md`.
