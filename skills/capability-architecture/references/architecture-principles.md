# Core Architectural Principles

## Summary

- Defines guidance for core architectural principles.
- Preserves capability boundaries and long-term maintainability decisions.

The foundation of this architecture is the rule:

**Separate what the system does from how it is displayed, how it is stored, and how it is called.**

This prevents business logic from becoming tightly coupled to delivery frameworks or infrastructure choices.

---

## What the System Does

This is the **business capability**.

Examples:

- verifying identity
- processing an order
- calculating a price
- orchestrating a workflow

This logic should exist in the **domain or application layer**.

It should not depend on:

- UI frameworks
- HTTP transport
- databases
- external APIs

---

## How It Is Displayed

This refers to presentation mechanisms:

- UI components
- pages
- mobile screens
- CLI output
- dashboards

Presentation layers gather input and display results but should not contain core business rules.

---

## How It Is Stored

This includes persistence mechanisms:

- databases
- document stores
- caches
- object storage
- external services

Storage access should occur through infrastructure adapters such as repositories.

---

## How It Is Called

Delivery mechanisms include:

- HTTP APIs
- server actions
- message queues
- scheduled jobs
- CLI commands

These should act as transport adapters that invoke application capabilities.

---

## Architectural Outcome

When properly separated:

- UI changes do not break business logic
- databases can be replaced without rewriting features
- APIs can evolve without affecting domain models
- capabilities can be reused across delivery mechanisms
