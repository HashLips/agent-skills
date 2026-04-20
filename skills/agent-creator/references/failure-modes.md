# Failure Modes and Recovery (Micro-Section)

Every generated `*-agent.md` must include a compact failure/recovery section. Keep it to 3-4 bullets.

## Required coverage

- **Missing or contradictory inputs** — state when to pause and ask for minimum clarifications vs proceed with declared assumptions.
- **Unavailable dependencies/tools/context** — state fallback behavior and what partial output is still expected.
- **Role ownership conflict** — state tie-break authority and no-silent-override rule.

## Copy-safe pattern

Use short rules like:

- If requirements are ambiguous or conflicting, request the minimum clarifications needed to proceed safely; do not invent critical constraints.
- If required tools/context are unavailable, produce a clearly labeled partial output with blockers, risks, and the exact unblock request.
- If decision ownership conflicts with another role, escalate to the named tie-break owner and pause conflicting changes until resolved.

## Anti-patterns

- "Do your best and continue" without escalation criteria.
- "Collaborate with team" without naming who decides conflicts.
- Silent assumptions on high-risk constraints (security, compliance, release gates).
