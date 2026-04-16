# Coupling Rules

Maintaining loose coupling is essential for long-term system adaptability.

---

## Dependency Direction

Dependencies should move inward toward the domain.

Outer layers may depend on inner layers.

Inner layers should not depend on outer layers.

---

## Avoid

- cross-module internal imports
- leaking framework types into domain logic
- direct database usage inside presentation code
