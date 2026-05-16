# Context Allowlist

Detect document type and host skills **before** editing. Required syntax is never changed to "sound natural."

## Intake: classify context

| Context | Signals | Default stance |
| --- | --- | --- |
| **Skill package** | `SKILL.md`, `references/`, frontmatter `name:` | Preserve repo layout; sanitize explanatory prose only |
| **Agent definition** | `*-agent.md`, role sections | Preserve template fields and kebab paths |
| **Technical spec** | schemas, APIs, field tables | Preserve identifiers; prose rules still apply to descriptions |
| **Narrative** | chapters, dialogue | Zero hyphen joins in narration; dialogue follows character voice |
| **Marketing / web** | CTAs, short sections | Stricter on buzz stacks; zero hyphen joins in body copy |
| **General prose** | none of the above | Full prose rules |

## Always preserve (syntax, not prose)

- **Paths and names:** `copy-sanitizer`, `references/foo.md`
- **Frontmatter:** YAML keys and values
- **Code and literals:** fences, inline code, commands, URLs, regex
- **List markers:** leading `-` or `1.`
- **Label lines:** `- **status** — value` or `- **status:** value`

## Prose rule (all contexts)

**Running prose = no hyphen joins between words** after sanitize. See [hyphen-break-patterns.md](hyphen-break-patterns.md).

Unpack `human-readable`, `end-to-end`, `AI-powered`, and similar forms in sentences. Keep hyphens only in the syntax rows above.

## Prose vs syntax

```
Syntax (path, code, list marker, label line, frontmatter)?
  → Preserve exactly.

Running prose (sentences, blurbs, chapter text)?
  → Zero hyphen joins in output; fix other patterns as needed.
```

When unsure, preserve if removal breaks parseability or a host skill contract.

## Host skills

If the user names agent-skill-creator or md-design-system, keep required list and path shapes. Sanitize explanatory sentences inside rules and paragraphs only.
