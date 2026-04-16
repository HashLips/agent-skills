---
name: capability-architecture
description: Design software systems around capabilities, clear boundaries, and layered responsibilities to reduce coupling and improve long-term maintainability, security, and observability at trust boundaries. Use when designing new architecture, refactoring for modularity, defining module contracts, evaluating system structure, or hardening authorization, data handling, and operational visibility across frontend, backend, or service-based applications.
---

# Capability Architecture

Design systems that remain adaptable, modular, and maintainable by organizing software around capabilities, boundaries, contracts, and layered responsibilities.

## Core Rule

Always separate:

- what the system does
- how it is displayed
- how it is stored
- how it is called

This keeps business logic portable and prevents tight coupling to frameworks, transport, and infrastructure.

## Execution Workflow

When designing or refactoring architecture:

1. Identify business capabilities
2. Define module boundaries per capability
3. Establish explicit contracts between modules
4. Define security and trust boundaries per capability (identity, authorization, sensitive data, validation)
5. Define observability boundaries per capability (logs, metrics, traces, correlation)
6. Assign responsibilities by layer
7. Isolate external systems behind adapters
8. Prevent cross-layer and cross-module leakage
9. Compose the system from capability modules

## Non-Negotiable Rules

- Organize by capabilities, not by technical artifact type
- Keep dependency direction inward toward domain logic
- Keep presentation and transport layers thin
- Keep infrastructure replaceable through adapters
- Communicate between modules through contracts only
- Introduce shared abstractions only after reuse is proven
- Enforce authorization consistently at capability entry points, not only at one outer transport layer
- Validate untrusted input at trust boundaries; keep domain and application logic working on safe, explicit inputs
- Classify sensitive data and secrets; keep secret handling in infrastructure, not in domain rules
- Define capability-level observability signals at entry, success, and failure boundaries
- Keep logs structured and safe: include correlation context, exclude secrets and unnecessary sensitive data

## Output Contract

Architectures produced with this skill should:

- define clear capability ownership
- define boundaries and contracts for interactions
- show explicit layer responsibility split
- avoid framework/database leakage into domain logic
- document known anti-pattern risks and mitigations
- state trust boundaries, authorization expectations, and sensitive data handling per capability where relevant
- define observability expectations (events, metrics, trace points, correlation ids) per capability where relevant

## Reference Index

- Core separation principle; read first to ground all decisions: [references/architecture-principles.md](references/architecture-principles.md)
- Layer responsibilities and boundaries; read when assigning logic to domain/application/infrastructure/presentation: [references/layering-model.md](references/layering-model.md)
- Capability ownership model; read when defining module structure and ownership: [references/capability-modules.md](references/capability-modules.md)
- Contract-first interaction rules; read when defining interfaces, commands, queries, or events: [references/boundary-contracts.md](references/boundary-contracts.md)
- Dependency direction and coupling constraints; read when validating imports and layer isolation: [references/coupling-rules.md](references/coupling-rules.md)
- Reuse progression strategy; read before extracting shared abstractions: [references/reuse-guidelines.md](references/reuse-guidelines.md)
- Common failure patterns and mitigations; read during reviews and refactors: [references/anti-patterns.md](references/anti-patterns.md)
- Security at boundaries (authz, validation, secrets, sensitive data); read when defining contracts, entry points, or threat-sensitive capabilities: [references/security.md](references/security.md)
- Observability at boundaries (logging, metrics, traces); read when defining operational visibility and debugging paths for capabilities: [references/observability.md](references/observability.md)
- Step-by-step architecture workflow; read when executing a new design from scratch: [references/implementation-process.md](references/implementation-process.md)

## When To Use This Skill

Use this skill when:

- designing new system architecture
- refactoring an existing codebase for modularity
- structuring frontend, backend, or service-based systems
- defining contracts and boundaries across modules
- enforcing long-term maintainability practices
- aligning security controls with capability boundaries and contracts
- designing reliable operational visibility for capability behavior in production

This skill is framework-agnostic and pairs well with framework-specific implementation skills.
