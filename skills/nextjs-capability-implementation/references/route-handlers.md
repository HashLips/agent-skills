# Route Handlers

Route handlers expose HTTP endpoints.

Use them when:

- creating APIs
- handling webhooks
- integrating external services

---

## Responsibilities

Route handlers should:

- parse request input
- authenticate requests
- call capability logic
- emit structured server-side logs with request/outcome context
- return HTTP responses
