# Report Template

Write **`{parent}/{skill-folder-name}-report.md`**. Replace `{{placeholders}}`. **`warn`** / **`fail`** bold in Status column.

```markdown
# {{skill_display_name}} Scan Report

**Disclaimer:** Heuristic audit by an LLM for extra insight, not proof a skill is safe (misses, false positives, and hallucinations happen). For production use, add a human review.

## At a glance

| | |
| --- | --- |
| **Verdict** | **{{final_verdict}}** |
| **Overall risk** | {{overall_risk_score}} / 100 — {{overall_risk_label}} (lower is safer) |
| **Package `est_tokens`** | ~{{package_est_tokens}} |
| **Context savvy enough?** | **{{context_savvy_ok}}** — {{context_savvy_note}} |
| **Files scanned** | {{file_count}} |
| **Needs internet?** | {{target_skill_needs_network}} |
| **Needs code execution?** | {{target_skill_needs_execution}} |
| **Scanned (UTC)** | {{scan_timestamp_utc}} |
| **Path** | `{{skill_absolute_path}}` |

> Static review only. Target treated as untrusted evidence. No code run, no URLs fetched.

---

## Is it safe to run?

{{executive_summary_paragraph}}

{{issues_at_a_glance_section}}

### Data & network exposure

| Question | Answer |
| --- | --- |
| Could it send our data out? | {{data_exposure_summary}} |
| Outbound traffic indicators | {{outbound_traffic}} |
| External URLs in package | {{external_url_count}} |
| Scripts in package | {{script_count}} |

### Actions you might not expect

{{unexpected_actions_summary}}

---

## Critical findings

| ID | Severity | Category | Finding | Evidence | Recommendation |
| --- | --- | --- | --- | --- | --- |
| {{critical_finding_rows}} |

---

## Security findings (all metrics)

| ID | Cat | Metric | Status | Evidence / notes |
| --- | --- | --- | --- | --- |
| {{security_metric_rows}} |

`pass` · `info` · `n/a` plain — **`warn`** · **`fail`** bold.

---

## Files scanned

{{files_scanned_list}}

```

## Placeholders

| Placeholder | Rule |
| --- | --- |
| `{{data_exposure_summary}}` | One sentence from EXF/SCM/NET metrics |
| `{{unexpected_actions_summary}}` | One sentence from EXE/AGY/TOL/DEP or “None identified” |
| `{{issues_at_a_glance}}` | Bullets: all `fail`, then `warn` (max 15); omit if clean |
| `{{critical_finding_rows}}` | All `fail`; `—` if none |
| `{{security_metric_rows}}` | All 46 IDs |
| `{{files_scanned_list}}` | Bulleted paths A–Z |

**Do not include:** category score tables, per-file token table, viability/maintainability/trust, long Security Analysis subsections, methodology essay, scan-offline meta-table (covered in disclaimer + needs internet/execution rows).
