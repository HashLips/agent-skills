# Implementation Process

When designing a system:

1. Identify the core capabilities.
2. Define boundaries for each capability.
3. Establish contracts between modules.
4. Define security and trust boundaries (authorization, validation, sensitive data) for each capability.
5. Assign responsibilities to architectural layers.
6. Prevent cross-layer leakage.
7. Compose the application from capability modules.

This ensures systems remain modular, adaptable, and defensible at their boundaries.

For security detail, see [security.md](security.md).
