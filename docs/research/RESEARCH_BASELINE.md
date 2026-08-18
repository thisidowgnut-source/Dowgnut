# Research Baseline

> Status: Normative project documentation
> Last reviewed: 2026-08-18
> Source of truth: `thisidowgnut-source/Dowgnut`

## Repository structure research
The documentation structure was benchmarked against large, actively maintained repositories including React, Next.js, TypeScript, Docker Docs, Kubernetes, VS Code extensions, and OpenAI Cookbook. These repositories commonly separate root governance documents from deeper product/developer documentation and often provide dedicated Code of Conduct, Contributing, Security, Support, Changelog, roadmap, and docs structures.

React currently exposes clear contributing, code-of-conduct, and license guidance in its top-level documentation. Next.js and TypeScript expose contribution and security documentation as first-class repository resources. Docker's docs repository further separates documentation content from contributor and style guidance. Kubernetes separates contributor, security, ownership, release, and content structures.

## Dowgnut adaptation
Dowgnut adopts these proven patterns but extends them for an AI-native application:
- root AI-agent instructions
- agent-specific architecture and security
- product vs system documentation separation
- ADRs
- data/RLS contracts
- evaluation and verification requirements

This is a synthesis, not a claim that Dowgnut exactly follows any external repository's internal process.
