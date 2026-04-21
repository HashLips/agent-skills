# Compression Workflow

## Goal

Produce the smallest readable Markdown that preserves all facts and instructions.

## Step Order

1. **Extract facts**
   - Mark requirements, constraints, numeric values, names, and explicit decisions.
   - Mark must/should rules and irreversible commitments.
2. **Delete low-value prose**
   - Remove motivational language, framing, and duplicate explanation.
   - Remove repeated restatements of the same rule.
3. **Refactor sentence shape**
   - Convert long sentences into short clauses.
   - Prefer one idea per bullet.
   - Replace passive voice when a shorter active form exists.
4. **Normalize structure**
   - Replace paragraph blocks with compact bullets or numbered steps.
   - Merge adjacent sections when they contain the same intent.
5. **Apply abbreviations**
   - Use the canonical map only when expansion is clear from context.
   - Keep first-use expansion if ambiguity risk exists.
6. **Compress punctuation/symbols**
   - Apply `standard` or `ultra` profile rules.
   - Keep punctuation required for correctness or readability.
7. **Run quality gate**
   - Verify no factual loss, no contradictory edits, and no broken links/code.

## Profile Behavior

- **standard**
  - Keep sentence punctuation mostly intact.
  - Use symbols only for common relations (`->`, `<=`, `>=`, `vs`).
  - Keep conjunction words when they improve flow.
- **ultra**
  - Drop optional terminal periods in bullets.
  - Remove commas that do not change parse meaning.
  - Replace safe phrase patterns with symbols from policy.
  - Collapse helper words if meaning remains clear.

## High-Value Compression Targets

- Filler openings: "In order to", "It is important to note that", "Basically".
- Hedging: "might", "somewhat", "quite", "very" (unless intensity is required).
- Redundant pairs: "each and every", "final outcome", "future plans".
- Empty qualifiers: "really", "just", "actually", "clearly".

## Never Compress These Blindly

- Exact requirement language (`must`, `must not`, `required`).
- Numeric thresholds, dates, versions, and limits.
- CLI commands, code snippets, paths, and identifiers.
- Legal, security, or safety statements.
