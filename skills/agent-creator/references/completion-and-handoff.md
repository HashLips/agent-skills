# Completion, definition of done, and handoff

Use this when authoring or reviewing any `*-agent.md` so it is **clear when the role is finished** and **what happens next**—not only what it *does* in the middle.

## Why

Orchestrations and humans need a **stopping rule** and a **receipt** for the next role. Without it, work bleeds across agents, context doubles, and nobody “owns” the handoff.

## Non-negotiable in every agent file

Include a dedicated **Completion and handoff** section (see [agent-file-template.md](agent-file-template.md)) with all of the following, even if one line each:

1. **Definition of done (DoD)**  
   Testable conditions that mark this role’s work complete for a typical item (a PR, a doc, a design cycle, a release gate). Use short bullets, not a loose “when everything looks good.”

2. **Stop condition**  
   When *this* agent’s **responsibility ends** for the thread: e.g. “after the merged handoff pack is sent,” “after the approved architecture note is published,” “after the human accepts risk—then this agent does not re-plan.”

3. **Handover: next role, artefact, and start condition**  
   - **To whom** (by role, not file path): the **next** agent or human role.  
   - **What** they **receive** (artefact shape or list).  
   - **What** *they* need to **begin** (e.g. “engineering may start only after signed AC and SLOs listed”).

4. **Re-engagement (optional, one line)**  
   If something **invalidates** the handoff (scope change, new **blocker**), which role **re-opens** the loop; avoid “this agent is always in the room forever.”

## Good vs weak

- **Good:** “DoD: NFRs listed; two options in ADR; Security architect comment window closed. Stop when ADR is merged. Hand to backend lead with: ADR, API sketch, and open questions file. Re-engagement: PM reopens if scope of bet changes.”

- **Weak:** “We collaborate until done” / “Hand off to the team.”

## Formatting in this section

Use **plain sentences**; avoid bolding every other word. Emphasis in **Completion and handoff** is especially distracting because readers skim for the **exit** lines.
