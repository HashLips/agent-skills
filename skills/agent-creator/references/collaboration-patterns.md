# Collaboration Patterns

## Summary

- Collaboration covers in-flight interfaces, not final handoff.
- Keep ownership and exchange contracts explicit.

## Core patterns

- Define what you send and what you expect back.
- Reference partners by role name, not filesystem path.
- Keep one owner per decision class.
- Use if/then triggers for mandatory involvement.

## Chaining patterns

- **Sequential** — Upstream outputs become downstream inputs.
- **Parallel** — Shared artifact with explicit section ownership.

## Skills in collaboration

- Agents may call named skills when available.
- Agent file remains authoritative when no skill exists.

## Conflict handling

- Name tie-break owner in decision framework or escalation.
