# Layering Model

## Summary

- Defines guidance for layering model.
- Preserves capability boundaries and long-term maintainability decisions.

The architecture separates concerns into four layers.

---

## Domain Layer

Defines the core business concepts.

Contains:

- domain entities
- business rules
- value objects
- policies
- domain validations

This layer should remain independent of frameworks.

---

## Application Layer

Coordinates workflows and use cases.

Contains:

- use case orchestration
- commands and queries
- service coordination
- transaction flows

This layer invokes domain logic and infrastructure.

---

## Infrastructure Layer

Implements external integrations.

Contains:

- database repositories
- API adapters
- messaging systems
- storage providers
- authentication providers

This layer is replaceable.

---

## Presentation Layer

Handles interaction with users or transport protocols.

Examples:

- web interfaces
- REST endpoints
- GraphQL resolvers
- CLI commands

This layer should remain thin.
