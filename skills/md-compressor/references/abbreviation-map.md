# Abbreviation Map

## Policy

- **light:** avoid map abbreviations except `e.g.`, `i.e.`, `etc.`, `vs`.
- **medium / heavy / extreme:** use canonical abbreviations for repeated terms.
- Do not abbreviate inside code, commands, URLs, file names, or env vars.
- Expand on first use in **medium** when ambiguity risk exists; **heavy / extreme** may skip expansion if legend line covers dense tokens (legend optional at **extreme** if net token cost).

## Canonical Abbreviations

- **Markdown** → `MD`
- **reference** → `ref`
- **references** → `refs`
- **configuration** → `config`
- **application** → `app`
- **environment** → `env`
- **requirements** → `reqs`
- **requirement** → `req`
- **information** → `info`
- **example** → `ex`
- **examples** → `exs`
- **approximately** → `approx`
- **minimum** → `min`
- **maximum** → `max`
- **temporary** → `temp`
- **identifier** → `id`
- **identifiers** → `ids`
- **number** → `num`
- **numbers** → `nums`
- **parameter** → `param`
- **parameters** → `params`
- **function** → `fn`
- **functions** → `fns`
- **message** → `msg`
- **messages** → `msgs`
- **compression** → `compress` (heavy/extreme, body text)
- **documentation** → `docs`
- **implementation** → `impl`
- **workflow** → `wf` (heavy/extreme)

## Phrase Shortforms

- **for example** → `e.g.`
- **that is** → `i.e.`
- **versus** → `vs`
- **with respect to** → `re`
- **and so on** → `etc.`

## Heavy / Extreme Dense Tokens (Use With Legend)

When **heavy** or **extreme** and a one-line legend is present at file top (legend optional at extreme):

- **must not** → `mustn't` only if negation scope stays obvious; prefer keeping `must not`
- **should not** → keep spelled out if safety-related
- **before** → `b4` — avoid; use only in non-critical labels
- **without** → `w/o` — avoid in requirements

Prefer map entries over invented heavy tokens.

## Avoid

- Inventing abbreviations not in this map (medium) or not listed + legend (heavy/extreme).
- Stacking many abbreviations in one sentence at **medium**.
- Abbreviating headings into unreadable fragments at **light** or **medium**.
- Replacing words with symbols outside [symbol-and-punctuation-policy.md](symbol-and-punctuation-policy.md).
