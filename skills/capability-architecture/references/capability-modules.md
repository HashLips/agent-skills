# Capability Modules

## Summary

- Defines guidance for capability modules.
- Preserves capability boundaries and long-term maintainability decisions.

Systems should be organized around **capabilities**.

A capability represents a business function of the system.

Examples:

- authentication
- checkout
- profile management
- reporting
- verification

Each capability should encapsulate its own logic and boundaries.

---

## Capability Ownership

A capability should own:

- its domain logic
- its application orchestration
- its infrastructure adapters
- its presentation entry points

---

## Benefits

Capability-centered design provides:

- clear ownership
- modular boundaries
- easier refactoring
- safer scaling of teams
- better reuse across systems
