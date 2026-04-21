# Failure Modes and Recovery

## Summary

- Every agent must include a compact failure/recovery section.
- Keep this section to 3-4 operational bullets.

## Required coverage

- Missing or contradictory inputs.
- Unavailable dependencies, tools, or context.
- Role ownership conflict and tie-break path.

## Copy-safe pattern

- Request minimum clarifications for ambiguity.
- Produce labeled partial output when dependencies are blocked.
- Escalate ownership conflicts to named decision authority.

## Anti-patterns

- Continue without escalation criteria.
- Vague “collaborate with team” with no decider.
- Silent high-risk assumptions.
