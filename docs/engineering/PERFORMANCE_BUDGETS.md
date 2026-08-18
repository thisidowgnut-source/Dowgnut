# Performance Budgets

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

Initial budgets are targets and MUST be measured before being enforced as hard gates.

App: fast initial interactive render, minimized bundle weight, image optimization, bounded animations.

Backend: predictable latency for catalog and cart commands.

Agent: stream first useful output quickly, bound tool latency, and time out stalled provider requests.

Exact numeric budgets should be established from real telemetry rather than invented without measurement.
