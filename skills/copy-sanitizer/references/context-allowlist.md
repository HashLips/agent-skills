# Context Allowlist

Sanitization is **context-aware**. Detect the document type and active repo conventions **before** scoring or editing. Required syntax is never "fixed" for statistical smoothness.

## Intake: classify context

| Context | Signals | Default stance |
| --- | --- | --- |
| **Skill package** | `SKILL.md`, `references/`, frontmatter `name:` | Preserve repo skill and MD layout rules |
| **Agent definition** | `*-agent.md`, role sections | Preserve template fields and kebab paths |
| **Technical spec** | schemas, APIs, field tables | Preserve identifiers and label lines |
| **Narrative** | chapters, dialogue, no frontmatter | Stricter on uniform rhythm; respect character voice |
| **Marketing / web** | CTAs, short sections | Stricter on buzz stacks; still no global word ban |
| **General prose** | none of the above | Default heuristics only |

If the user names a host skill (e.g. agent-skill-creator, md-design-system), load its layout rules and treat them as **allowlisted**.

## Always preserve (any context)

- **Paths and names:** kebab-case folders (`copy-sanitizer`), filenames, `references/` links
- **Frontmatter:** YAML keys and values
- **Code and literals:** fenced blocks, inline code, commands, URLs, regex
- **Markdown list markers:** leading `-` or `1.` (list syntax, not prose joins)
- **Tracking field keys:** snake_case (`hyphen_joins`, `metrics_first_pass`)
- **Domain-standard compounds** the audience expects (legal, medical, product names)

## Skill and MD design system (required dashes)

When the source follows **agent-skill-creator** or **md-design-system**, keep:

| Convention | Example | Notes |
| --- | --- | --- |
| Skill `name` | `copy-sanitizer` | kebab-case in frontmatter |
| Named list items | `- **status** — value` or `- **status:** value` | em dash or colon **between label and value** is layout, not a prose hyphen join |
| Unordered lists | `- item` | leading hyphen is syntax |
| Reference paths | `references/detection-patterns.md` | do not unpack path hyphens |
| Interface bullets | `- **Inputs** — amount, currency` | same label/value pattern |

**Do not** change `- **field** — value` lines into unpacked prose to "reduce hyphens." That breaks repository contracts.

Em dashes in **running explanatory paragraphs** inside skills are still subject to density checks. Em dashes in **canonical list label lines** are allowed.

## Prose vs syntax (decision rule)

```
Is it structural syntax (list marker, path, key, frontmatter, code)?
  → Preserve.

Is it label — value on a bullet per MD design system?
  → Preserve.

Is it running prose (sentences, blurbs, chapter text)?
  → Apply hyphen-break and punctuation heuristics.
```

When unsure, prefer **preserve** if removal breaks parseability, diff clarity, or a named host skill contract.

## Cross-skill workflow

1. User or path indicates host skill → read that skill's layout rules.
2. Record active conventions in tracking `notes` (large jobs).
3. Run detection on **prose regions**; skip or down-weight syntax regions.
4. Never "sanitize" another skill's required `SKILL.md` shape to plain paragraphs.
