# React Hooks and Context (Next.js + Capabilities)

Use this file when choosing where hooks and Context belong in a capability-based Next.js app.

## Placement Rule

Hooks (`useState`, `useEffect`, `useReducer`, custom hooks) and React Context **run only in Client Components** (files with `"use client"`).

Keep **business rules and mutations** on the server:

- Server Components for data preparation
- Server Actions or Route Handlers as thin adapters into capability logic

Do not move domain decisions into Context providers or effect chains just because it is convenient.

---

## Hooks

Use hooks for:

- local UI state (open/closed, form field UI state that does not encode business invariants)
- browser-only concerns (resize, focus, subscriptions)
- wiring event handlers to call Server Actions

Avoid hooks for:

- authoritative authorization or pricing rules
- persistence or secret access
- anything that must stay correct if the client is tampered with

---

## Context

Use Context for **UI-wide presentation state** that is safe to expose:

- theme (light/dark)
- layout chrome (sidebar open)
- purely client UI preferences

Avoid Context for:

- secrets, tokens, or session payloads
- canonical application state that should live in the capability layer
- large objects fetched on the server that should be passed as props instead

Prefer **props and composition** from Server Components down into Client Components when data is prepared on the server.

---

## Capability Alignment

- **Capability module** owns use-cases and domain/application logic.
- **Client subtree** owns interactivity; it calls Server Actions with validated inputs.
- **Context** should not become a hidden service locator for capability logic.

---

## Summary

Hooks and Context are **client presentation tools**. Capabilities stay **server-truth** unless the behavior is intentionally and safely client-only.
