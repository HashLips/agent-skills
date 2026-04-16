# Server vs Client Components

Next.js separates server and client execution environments.

---

## Server Components

Use for:

- data fetching
- accessing server resources
- preparing data for rendering

---

## Client Components

Use for:

- UI interactivity
- browser APIs
- event handlers
- local state
- React hooks and Context (see [react-hooks-and-context.md](react-hooks-and-context.md))

---

## Security Rule

Sensitive operations should remain on the server.
