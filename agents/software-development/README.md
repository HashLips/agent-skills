# Software development agents

> **Testing phase:** These agent definitions have been **generated** and have **not** been run through a full **end-to-end** implementation. Treat them as **experimental** until you validate them in your own workflow.

Role-driven agent definitions. They follow the [agent-creator](../../skills/agent-creator/SKILL.md) pattern: `*-agent.md`, portable, with completion and handoff, and light use of bold.

## Where to start

- **Entry point for end-to-end work:** [orchestrator-agent.md](orchestrator-agent.md) — routes a user’s goal (e.g. a client product page) through the right sequence of specialist agents and keeps handoffs explicit.
- For a **single** discipline, load only that agent (e.g. [backend-developer-agent.md](backend-developer-agent.md)).

## All agents

| Role | File |
|------|------|
| Orchestrator | [orchestrator-agent.md](orchestrator-agent.md) |
| Product manager | [product-manager-agent.md](product-manager-agent.md) |
| Business analyst | [business-analyst-agent.md](business-analyst-agent.md) |
| Solution architect | [solution-architect-agent.md](solution-architect-agent.md) |
| Capability architect | [capability-architect-agent.md](capability-architect-agent.md) |
| Security architect | [security-architect-agent.md](security-architect-agent.md) |
| UX designer | [ux-designer-agent.md](ux-designer-agent.md) |
| Front-end developer | [frontend-developer-agent.md](frontend-developer-agent.md) |
| Back-end developer | [backend-developer-agent.md](backend-developer-agent.md) |
| Test engineer | [test-engineer-agent.md](test-engineer-agent.md) |
| Code reviewer | [code-reviewer-agent.md](code-reviewer-agent.md) |
| DevOps engineer | [devops-engineer-agent.md](devops-engineer-agent.md) |
| Documentation | [documentation-agent.md](documentation-agent.md) |

Paths are relative to this `agents/software-development` folder. Adjust if you copy this pack elsewhere in your repo.
