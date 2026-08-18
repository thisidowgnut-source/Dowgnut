# User Journeys

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Customer purchase journey
Landing → discover flavor → inspect detail → add to box/cart → review cart → authenticate if needed → checkout → order confirmation → order history.

## AI-assisted journey
Open AI → describe need → agent searches products → agent proposes box → user edits or approves → cart updates → normal checkout.

## Operator journey
Login → view products/inventory → review orders → adjust availability/content → inspect operational alerts.

## Developer journey
Read task → agent inspects repository → plan → implement → tests → fix → diff → update docs → commit/push → report.

## Failure journeys
For every journey, define what the user sees when:
- network is unavailable
- inventory changes mid-flow
- payment is declined
- AI provider is unavailable
- a tool call fails
- authorization is denied
