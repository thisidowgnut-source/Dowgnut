# Agent Approval Gates

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

### Automatic
Read/search/test/typecheck/diff.

### Approval
External writes, package installation, branch/commit/push, issue/PR creation, schema migration.

### Blocked
Force push, secret exfiltration, destructive database deletion, production payment changes without approved workflow, arbitrary code execution outside the sandbox.

Every approval should state the exact action and expected side effect.
