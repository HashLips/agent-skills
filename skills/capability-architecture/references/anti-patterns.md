# Architecture Anti-Patterns

## Summary

- Defines guidance for architecture anti-patterns.
- Preserves capability boundaries and long-term maintainability decisions.

These patterns increase coupling, reduce adaptability, and make systems harder to evolve.

---

## Layer Leakage

Business logic depends on UI frameworks, HTTP objects, ORM entities, or transport-specific types.

Avoid by:

- keeping domain models framework-agnostic
- mapping external/request models at the boundary
- converting persistence models in infrastructure adapters

---

## Capability Bypass

One module reaches into another module's internals rather than using its contract.

Avoid by:

- exposing explicit interfaces/commands/queries/events
- preventing internal cross-imports between capabilities
- treating module internals as private implementation details

---

## Presentation-Heavy Business Rules

Controllers, resolvers, pages, or UI components contain business decisions and orchestration.

Avoid by:

- moving use-case orchestration to application layer
- keeping entry points thin (input mapping, auth, invocation, output mapping)

---

## Infrastructure-Coupled Domain

Domain logic directly calls databases, queues, or external APIs.

Avoid by:

- defining ports/contracts in domain or application layers
- implementing adapters in infrastructure layer only

---

## Premature Shared Abstractions

Generic shared utilities are extracted before real reuse patterns exist.

Avoid by:

- allowing capability-local duplication initially
- extracting only after repeated and stable reuse
- promoting reuse incrementally: local -> application -> platform

---

## Ambiguous Capability Ownership

Multiple modules partially own the same business workflow with no clear source of truth.

Avoid by:

- defining one owning capability per business function
- documenting ownership boundaries and interaction contracts

---

## Wrong Dependency Direction

Inner layers depend on outer layers, making core logic fragile and hard to test.

Avoid by:

- enforcing inward dependency direction
- reviewing imports for domain/application independence
- treating framework details as replaceable outer concerns

---

## Missing Security at Capability Boundaries

Use cases are reachable without consistent authentication or authorization, or untrusted input reaches domain logic unchanged.

Avoid by:

- enforcing the same policy at every entry point into a capability
- validating and mapping external input at the boundary

See [security.md](security.md) for full guidance.
