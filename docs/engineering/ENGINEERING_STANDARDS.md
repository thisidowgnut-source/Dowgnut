# Engineering Standards

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Code
Prefer small modules, explicit types, deterministic business logic, and dependency inversion around external services.

## Testing
Every business rule MUST have automated coverage at the most appropriate level.

## Error handling
Errors MUST preserve context, support correlation IDs, and avoid leaking secrets.

## Dependencies
Pin or constrain important production dependencies. Review new dependencies for maintenance, license, security, and bundle impact.

## Documentation
Any change to architecture, APIs, security, or operational behavior MUST update the corresponding document or ADR.
