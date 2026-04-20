# Hard QA Rubric (Pass/Fail)

Use this after drafting any `*-agent.md`. Fail fast. Fix every failed item before shipping.

## Gating checks

Mark each item `pass` or `fail`:

1. **Role boundary clarity**  
   Pass if responsibilities and constraints make it obvious when to use this role and when not to.

2. **Explicit refusal boundary**  
   Pass if constraints include at least one clear "must not" or out-of-scope refusal rule.

3. **Ambiguity handling**  
   Pass if failure micro-section states what happens when requirements are missing or contradictory.

4. **Dependency/tool unavailability handling**  
   Pass if failure micro-section states what to do when required tools/context are unavailable.

5. **Conflict tie-breaker**  
   Pass if decision framework or escalation names who resolves ownership/tradeoff conflicts.

6. **Completion contract quality**  
   Pass if Completion and handoff includes DoD, stop condition, next role + artefact package, and next-role start rule.

7. **Output concreteness**  
   Pass if outputs are named artefact types, not vague statements (e.g. "good strategy").

8. **Portability**  
   Pass if there are no required repo-local paths (`skills/`, `../`, monorepo-only links) in the agent body.

9. **Brevity and scannability**  
   Pass if the file is roughly 250-500 words, list-first, and readable in under 60 seconds.

10. **Formatting hygiene**  
   Pass if emphasis is sparse and there is no bold-noise pattern across bullets.

## Decision rule

- **Ship:** only if all 10 checks are `pass`.
- **Revise:** if any check is `fail`, fix and rerun rubric.
