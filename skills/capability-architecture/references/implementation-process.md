# Implementation Process

## Summary

- Defines guidance for implementation process.
- Preserves capability boundaries and long-term maintainability decisions.

When designing a system:

1. Identify the core capabilities.
2. Define boundaries for each capability.
3. Establish contracts between modules.
4. Define security and trust boundaries (authorization, validation, sensitive data) for each capability.
5. Define observability boundaries (logs, metrics, traces, correlation) for each capability.
6. Assign responsibilities to architectural layers.
7. Prevent cross-layer leakage.
8. Compose the application from capability modules.

This ensures systems remain modular, adaptable, and defensible at their boundaries.

For security detail, see [security.md](security.md).
For observability detail, see [observability.md](observability.md).
