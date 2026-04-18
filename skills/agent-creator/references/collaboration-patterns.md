# Collaboration Patterns

Use this for **ongoing** partners while the work is in progress. The **stop** rule, **definition of done**, and **next role + package** live in **Completion and handoff** (see [completion-and-handoff.md](completion-and-handoff.md)). Do not replace that section with a vague “we hand off to the team” bullet here.

## Interfaces, not vibes

- Define **what you send** and **what you need back** (artifact + shape), e.g. “You receive: acceptance criteria + NFRs + open questions. You return: estimate, risks, and milestone options.”
- **Reference other agents** by **role** (“Security agent”, “PM agent”) or, if a library uses filenames, **by the shared naming pattern** (e.g. `security-reviewer-agent`) without embedding disk paths to a monorepo.

## Boundaries

- **One owner** per class of decision. Example: roadmap: PM; stack: engineering; threat model: security.
- Use **if/then** triggers: “If PII, security review is mandatory before merge.”

## Chaining agents

- **Sequential:** A’s default **outputs** = B’s **inputs**; name fields, not code paths.
- **Parallel reviews:** e.g. RFC in one place; each reviewer owns their section.

## Referencing skills (portable)

- In **any** product, a user might have **optional** “skills” (reusable how-tos) loaded alongside agents. The agent can say: follow **`<named skill>`** *when* it is available in that environment. **Do not** require a `skills/` directory or a relative URL. If no skill exists, the **agent** alone is authoritative.

**Agents** = *who* + *how the role decides*. **Skills** = *how* to do a class of work *when* present. Do not conflate the two in one file unless the team’s convention explicitly co-locates them.

## Conflicts

- Named **escalation** in **decision framework** or **escalation**: e.g. “Engineering manager decides tie-break on technical tradeoffs for this product.”
