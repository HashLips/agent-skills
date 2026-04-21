# Boundaries and Contracts

## Summary

- Defines guidance for boundaries and contracts.
- Preserves capability boundaries and long-term maintainability decisions.

Modules should communicate through **contracts**.

Contracts define the inputs and outputs between modules.

---

## Contract Examples

- service interfaces
- command objects
- query responses
- domain events

---

## External Boundaries

External systems must be isolated using adapters.

Examples:

- database repositories
- HTTP clients
- third-party integrations

This prevents external data shapes from leaking into internal logic.
