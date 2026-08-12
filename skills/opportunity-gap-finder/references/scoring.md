# Screening and Ranking

## Summary

- Apply hard gates before comparative scoring.
- Rank opportunities on a 1–5 scale and report evidence confidence separately.

## Stage 1: Hard Gates

First classify the pursuit by selecting every applicable type:

- **Self-directed** — value is primarily learning, expression, enjoyment, or personal progress.
- **Knowledge-producing** — value is primarily discovery, evidence, or public knowledge.
- **Externally served** — value depends on improving outcomes for other actors.
- **Continuing operation** — value requires repeated delivery, maintenance, governance, or participation.
- **Commercial** — success requires capturing sufficient financial value.

Apply every universal gate and only the conditional gates relevant to the pursuit.

### Universal Gates

- **Purpose** — the intended value and success threshold are clear.
- **Mechanism** — the approach can plausibly create the intended value or learning.
- **Feasibility** — the next commitment fits obtainable resources, capability, time, and permissions.
- **Acceptable harm** — legal, ethical, safety, environmental, and social risks are acceptable or reducible.
- **User fit** — the pursuit is compatible with the user's goals, resources, timeframe, and commitment.

### Conditional Gates

- **Actor** — required for externally served work; a specific affected actor or beneficiary is identifiable.
- **Progress** — required for externally served work; the desired outcome and consequence matter enough to motivate action or support.
- **Gap** — required when claiming an unmet external need; alternatives leave a meaningful, evidenced shortfall.
- **Access** — required when value depends on participants, buyers, sponsors, partners, or decision-makers.
- **Knowledge contribution** — required for research; the question or evidence contribution is useful and not already adequately resolved.
- **Sustainability** — required for continuing operations; money, labour, trust, ownership, permission, or participation can plausibly continue.
- **Value capture** — required for commercial success; enough created value can plausibly return as revenue or another financial contribution.

Classify each gate as:

- pass,
- uncertain and testable,
- fail,
- not applicable, with an explanation.

A failed applicable gate usually means reframe or reject. An uncertain gate becomes a priority validation assumption. A justified `not applicable` result is neutral, not a pass or failure.

## Stage 2: Comparative Dimensions

Score every applicable dimension from 1 to 5. Explain every score with evidence or mark it provisional. Calculate each category as the arithmetic mean of its applicable dimensions; exclude justified `not applicable` dimensions from both numerator and denominator.

### Need Strength

- **Consequence** — importance of achieving or missing the outcome.
- **Frequency or recurrence** — how often the need arises or persists.
- **Motivation to act** — willingness to contribute money, time, trust, permission, effort, or behaviour change.
- **Reachable value pool** — enough accessible people, organisations, places, or social value to meet the user's success threshold.
- **Durability and timing** — the need is likely to remain relevant long enough to act.

### Gap Strength

- **Alternative weakness** — current options, workarounds, or non-consumption leave material unmet progress.
- **Root-cause fit** — the mechanism addresses an important cause rather than only a visible symptom.
- **Distinct value** — the improvement is meaningful and explainable to the actor.
- **Proof visibility** — value or impact can be observed and attributed.

### Delivery Quality

- **Feasibility** — the mechanism can be delivered with obtainable capability, resources, partners, and permissions.
- **Adoption ease** — required trust, learning, switching, integration, travel, habit, or coordination is manageable.
- **Access and distribution** — participants and decision-makers can be reached through credible channels.
- **Sustaining model** — money, labour, ownership, maintenance, incentives, or institutional support can continue.
- **Risk-adjusted learning speed** — key assumptions can be tested cheaply, quickly, safely, and reversibly.

### User Fit

- **Advantage** — relevant insight, credibility, access, relationships, assets, or capability.
- **Purpose fit** — alignment with the user's desired financial and non-financial outcomes.
- **Commitment fit** — alignment with preferred pace, scale, role, and maintenance burden.
- **Risk fit** — acceptable exposure to financial, legal, ethical, safety, and reputational risk.

## Ranking

Use the default category weights, or adjust category weights before scoring when the pursuit requires it:

- **Default** — Need Strength 30%, Gap Strength 25%, Delivery Quality 25%, User Fit 20%.
- **Personal or creative pursuit** — increase User Fit and reduce Gap Strength when external unmet need is not the purpose.
- **Knowledge-producing pursuit** — increase Need Strength and User Fit; use the knowledge-contribution gate to assess originality or usefulness.
- **Public-interest pursuit** — increase Need Strength and Delivery Quality.
- **Commercial pursuit** — increase Need Strength and Delivery Quality, with value capture as a gate.
- **High-stakes pursuit** — treat acceptable harm, evidence quality, and reversibility as gates rather than score compensation.

Adjust category weights only, not individual dimension weights. If a whole category is not applicable, redistribute its weight proportionately across the remaining categories. Weights across applicable categories must total 100%. Calculate:

```text
Category score = mean of applicable dimension scores
Comparative score = sum(category score × category weight)
```

Round the final comparative score to one decimal place at most. Use it only to expose trade-offs, not to create false certainty. Report:

```text
Comparative score: [1–5]
Evidence strength: absent | weak | moderate | strong
Evidence consistency: aligned | mixed | contradictory
Resulting confidence: low | medium | high
Applicable gates:
- [gate]: pass | uncertain | fail
Not-applicable gates and reasons:
Eligibility: pursue-ready | validate first | reframe or reject
Ranking reason:
```

Do not convert this into a precise success probability.

## Kill Factors

Flag these even when an average score appears strong:

- no clear purpose or intended value,
- no specific actor, desired progress, or meaningful consequence when external impact is claimed,
- no evidence beyond enthusiasm or trend attention,
- alternatives are already good enough for the target actor,
- required behaviour change, trust, coordination, or switching is unrealistic,
- beneficiary, decision-maker, and contributor have no aligned incentive,
- the accessible population or value cannot meet the user's success threshold,
- the need may disappear before a useful response can be delivered,
- access depends on an unstable platform, gatekeeper, law, or partner,
- economics, labour, maintenance, or governance cannot be sustained,
- the intervention creates greater harm or risk than the original problem,
- the user lacks essential fit with no credible path to acquire or partner for it,
- the opportunity conflicts with the user's ethical boundaries or desired life.

## Portfolio View

When several opportunities remain credible, label them:

- **Lead** — strongest next-step case.
- **Option** — attractive if a named uncertainty resolves.
- **Small bet** — bounded pursuit valuable for learning or intrinsic return.
- **Monitor** — timing or evidence is not ready.
- **Reject or reframe** — a hard gate fails.

Prefer the option with the best combination of evidence, downside control, learning speed, and fit, not automatically the largest theoretical market.
