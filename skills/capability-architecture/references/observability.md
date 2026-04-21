# Observability by Capability

## Summary

- Defines guidance for observability by capability.
- Preserves capability boundaries and long-term maintainability decisions.

Observability is part of architecture, not an afterthought. Define it where capabilities cross boundaries.

---

## Principle

Each capability should define how operators can answer:

- what happened
- for which capability and request
- whether it succeeded or failed
- how long it took
- where it failed

---

## Boundary Signals

At minimum, define signals for:

- capability entry
- capability success
- capability failure
- external dependency call outcomes

These can be implemented as structured logs, metrics, traces, or a combination.

---

## Logging Rules

- Use structured logs with stable fields (event name, capability, correlation id, outcome, latency).
- Include enough context for diagnosis without exposing secrets or unnecessary sensitive data.
- Keep transport-level context in adapters and business-event context in capability/application logic.

---

## Metrics and Traces

- Track latency and error rate per capability and key use case.
- Add trace points around external adapters and high-risk workflows.
- Propagate correlation/trace identifiers across boundaries.

---

## Architectural Outcome

When observability is capability-aligned:

- incident diagnosis is faster
- ownership of failures is clearer
- refactors preserve operational visibility instead of breaking it
