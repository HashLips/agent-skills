# Observability and Server-Side Logging

Use this file to instrument Next.js capability flows with actionable server-side logs.

## Logging Boundaries

Log on the server at these boundaries:

- Route Handlers (HTTP ingress and response outcome)
- Server Actions (user-triggered mutation entry and result)
- Capability service boundaries (use-case start/failure/success)
- External adapter calls (upstream dependency outcome and latency)

Do not rely on client logs for security, auditing, or operational diagnosis.

---

## What To Log

Prefer structured logs with stable fields:

- `event`: stable event name (e.g., `checkout.submit.started`)
- `capability`: owning module name
- `requestId` or correlation id
- `actorId` (if authenticated and safe to log)
- `outcome`: success or failure
- `latencyMs`

For failures, include safe error metadata and error class/type.

---

## Sensitive Data Rules

- Never log secrets, raw tokens, credentials, or private keys.
- Minimize logging of PII; log identifiers only when required and allowed.
- Redact request bodies or headers by default; whitelist only safe fields.

---

## Where Logging Lives

- Transport-level context logging in Route Handlers and Server Actions.
- Business-event logging in capability/application services.
- Infrastructure adapter logging for dependency failures and timings.

Keep logging wrappers reusable in `shared/lib` when patterns repeat.

---

## Operational Outcome

A correctly instrumented capability should allow operators to answer:

- what happened
- for which capability and request
- whether it succeeded or failed
- how long it took
- where it failed if it did
