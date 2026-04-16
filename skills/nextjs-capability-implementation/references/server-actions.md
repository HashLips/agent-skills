# Server Actions

Server actions allow UI-triggered server-side execution.

Use them for:

- form submissions
- mutations
- server-only operations triggered by UI

---

## Guidelines

Server actions should:

- validate input
- call capability logic
- emit structured server-side logs for start/success/failure
- return a shaped result
- trigger revalidation when necessary
