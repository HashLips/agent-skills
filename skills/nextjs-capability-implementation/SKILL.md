---
name: nextjs-capability-implementation
description: Implements capability-based architecture inside TypeScript-first Next.js applications with correct server/client boundaries, routing adapters, secure configuration patterns, and server-side observability practices. Use when creating or refactoring Next.js projects that should follow capability architecture principles and enforce TypeScript, linting, and testing standards.
---

# Next.js Capability Implementation

Apply capability-architecture principles inside Next.js projects using concrete framework patterns for routing, composition, data flow, and security-sensitive boundaries.

## Core Workflow

When implementing a Next.js feature or system:

1. Bootstrap project with secure defaults
2. Establish capability-first folder structure
3. Keep `app/` focused on routing and composition
4. Enforce server/client execution boundaries
5. Implement thin transport adapters (Server Actions and Route Handlers)
6. Protect sessions, cookies, and environment variables
7. Add server-side observability at capability boundaries
8. Keep types and mapping logic close to capabilities
9. Validate implementation against checklist

## Non-Negotiable Rules

- Treat Next.js primitives as delivery mechanisms, not business-logic containers
- Keep Server Actions and Route Handlers thin; delegate to capability logic
- Do not leak secrets or sensitive env vars into client bundles
- Validate and map external data before UI/domain propagation
- Log significant server-side capability events with safe, structured context
- Use TypeScript (no new JavaScript-only feature modules); keep types close to capabilities
- Use React hooks and Context only in Client Components for presentation and wiring; keep capability truth on the server
- Keep feature ownership explicit in module structure and type placement

## Output Contract

Implementations produced with this skill should:

- preserve capability boundaries within a Next.js codebase
- separate server and client concerns intentionally
- keep routing layers compositional and thin
- handle auth/session/cookies in secure server contexts
- include server-side logging/observability at transport and capability boundaries
- be covered by basic linting (ESLint) and tests for critical capability paths
- keep project structure and references consistent and maintainable

## Reference Index

- Project bootstrap steps and baseline setup sequence: [references/project-bootstrap.md](references/project-bootstrap.md)
- Environment variable safety rules and secret exposure boundaries: [references/environment-variables.md](references/environment-variables.md)
- `.gitignore` patterns for Next.js and sensitive files: [references/gitignore.md](references/gitignore.md)
- Capability-first folder structure for Next.js repositories: [references/project-structure.md](references/project-structure.md)
- `app/` router responsibilities and composition boundaries: [references/app-router.md](references/app-router.md)
- Server versus client execution model and placement decisions: [references/server-vs-client.md](references/server-vs-client.md)
- Server Action usage as thin capability adapters: [references/server-actions.md](references/server-actions.md)
- Route Handler usage as HTTP transport adapters: [references/route-handlers.md](references/route-handlers.md)
- Cookie and session handling security guidance: [references/cookies-session-security.md](references/cookies-session-security.md)
- Server-side observability and logging patterns for capabilities: [references/observability-logging.md](references/observability-logging.md)
- Type placement strategy across capability modules: [references/type-placement.md](references/type-placement.md)
- Data fetching and mapping boundaries before rendering: [references/data-fetching.md](references/data-fetching.md)
- UI composition patterns that avoid feature-logic leakage: [references/ui-composition.md](references/ui-composition.md)
- React hooks and Context usage within server/client boundaries: [references/react-hooks-and-context.md](references/react-hooks-and-context.md)
- End-to-end implementation validation checklist: [references/implementation-checklist.md](references/implementation-checklist.md)

## When To Use This Skill

Use this skill when:

- building a new Next.js application with capability architecture
- refactoring an existing Next.js codebase for modularity
- implementing features with Server Actions or Route Handlers
- hardening configuration, cookies, and session boundaries
- adding reliable server-side logging and observability signals
- aligning project structure and UI composition with capability ownership

This skill is designed to pair with the `capability-architecture` skill.
