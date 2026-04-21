# Security at Capability Boundaries

## Summary

- Defines guidance for security at capability boundaries.
- Preserves capability boundaries and long-term maintainability decisions.

Security is not separate from architecture: it is enforced where capabilities meet—entry points, contracts, and data that crosses trust zones.

---

## Principle

Every capability should declare:

- who may invoke it (authentication and identity context)
- what they may do (authorization and policy)
- what data may enter or leave (sensitivity, minimization, validation)

---

## Authentication and Authorization

- Treat the **application layer** (or an explicit security policy layer) as the place that decides whether a use case may run, given the caller’s identity and permissions.
- Do not assume a single outer gate is enough: if a capability is reachable from multiple transports (HTTP, jobs, CLI, internal calls), **each path must arrive at the same authorization checks** for that use case.
- Prefer **capability-scoped** rules (what this business function allows) over ad hoc checks scattered in UI or repositories.

---

## Trust Boundaries and Validation

- Define **trust boundaries** where data leaves a controlled zone (user input, external APIs, webhooks, files).
- Validate and normalize **untrusted input at the boundary**; pass only validated shapes inward via contracts.
- Do not leak raw transport objects into domain logic; map to safe domain or application inputs first.

---

## Data and Secrets

- Classify data handled by each capability (e.g., PII, credentials, financial). Document **what may be logged, cached, or returned** through APIs.
- Keep **secrets and crypto material** in infrastructure configuration; never embed them in domain or application code.
- Apply **least privilege** for service accounts, database roles, and third-party tokens per capability or integration.

---

## Cross-Cutting Security

- **Dependencies**: pin and audit libraries used by infrastructure adapters; keep domain free of risky parsing where possible.
- **Errors**: return safe messages at the presentation boundary; log detail only where appropriate and compliant.
- **Multi-tenant or high-risk domains**: make tenant isolation and separation requirements explicit in capability contracts.

---

## Architectural Outcome

When security is integrated with capabilities:

- authorization stays consistent across entry points
- sensitive operations have a clear owner and policy home
- refactors are less likely to accidentally expose a use case without checks
