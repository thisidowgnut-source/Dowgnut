# Navigation Specification

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

Use Expo Router for file-based navigation.

Required route groups:
- storefront
- product detail
- cart
- checkout
- account
- agent

Navigation MUST preserve cart state, support deep links where product marketing requires them, and prevent accidental loss of unsaved checkout input.
