# Implementation Checklist

## Project and dependency baseline (before or when touching dependencies)

- **Next / React / `react-dom`**: on current stable, compatible versions per [dependency-and-version-security.md](dependency-and-version-security.md)
- **Audit**: package-manager audit (or equivalent) run for the lockfile; high/critical runtime issues resolved or explicitly documented

When implementing a feature:

1. Identify the capability module.
2. Place business logic in the module.
3. Use route files for composition only.
4. Use server actions for UI-triggered mutations.
5. Use route handlers for APIs.
6. Handle cookies and session data on the server.
7. Validate input at transport boundaries before capability execution.
8. Map external data before rendering.
9. Compose UI from feature components.
10. Confirm no secrets or sensitive values are exposed to client code.
11. Add structured server-side logs for transport entry, capability outcome, and failures.
12. Ensure linting (ESLint) passes for changed files.
13. Ensure tests (Jest or equivalent) pass for affected modules.
14. Confirm hooks and Context are limited to Client Components and do not embed server-authoritative business rules.
