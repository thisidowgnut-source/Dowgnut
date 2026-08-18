# A2UI Specification

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

A2UI is reserved for agent-generated UI that benefits from structured, dynamic rendering.

## Rules
- generated UI MUST have a bounded component vocabulary
- dangerous actions MUST require explicit approval
- visual design tokens MUST come from Dowgnut design system
- generated content MUST degrade gracefully when unsupported
- analytics and accessibility semantics MUST remain available

A2UI MUST NOT become a backdoor for arbitrary executable frontend code.
