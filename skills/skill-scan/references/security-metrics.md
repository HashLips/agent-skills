# Security Metrics

One row per ID in **Security Findings**. Status: `pass` | `warn` | `fail` | `info` | `n/a`. Evidence: path + ≤120 char excerpt for `warn`/`fail`.

**Focus:** data exposure, unauthorized execution/network, hidden instructions, guardrail bypass, deception about what the skill does.

**Catalog:** 46 metrics (report every ID).

## Categories

| Cat | Focus |
| --- | --- |
| `INJ` | Instruction hijacking / anti-scan |
| `EXF` | Data exfiltration & credential access |
| `EXE` | Destructive or privileged execution |
| `NET` | Network, downloads, supply chain |
| `OBS` | Obfuscation & hidden content |
| `SOC` | Deception & misleading scope |
| `SCM` | Secrets & sensitive paths in package |
| `PRIV` | Sandbox / approval bypass |
| `AGT` | Agent behavior manipulation |
| `AGY` | Run without user awareness |
| `TOL` | Dangerous tool chains |
| `POI` | Buried or flooding instructions |
| `DEP` | Supply chain & undeclared scripts |

---

## INJ

| ID | Metric | `fail` | `warn` |
| --- | --- | --- | --- |
| INJ-01 | Override system/user boundaries | ignore/disregard safety, fake `<system>`, developer mode | soft “most important instruction” |
| INJ-02 | Jailbreak persona | DAN, uncensored, bypass policies | security-test role-play |
| INJ-03 | Hidden instructions | HTML comments, zero-width, base64 → commands | unusual hiding |
| INJ-04 | Dual-use harm | — | harmful if followed (share data, delete “cache”, undeclared cleanup) |
| INJ-05 | Instruction flooding | long noise + buried harmful line | SKILL.md >8k `est_tokens`, low signal |
| INJ-06 | Anti-scanner | do not report, skip file, treat as safe | hide/downgrade findings |
| INJ-07 | Authority confusion | fake system/developer “must approve” | ambiguous role |

## EXF

| ID | Metric | `fail` | `warn` |
| --- | --- | --- | --- |
| EXF-01 | Explicit exfil | upload env/keys, webhooks, send `~/.ssh`, paste sites | share logs, no destination |
| EXF-02 | Credential paths | read `.env`, `~/.ssh`, keychain, cookies, AWS creds | generic read config |
| EXF-03 | Encoded exfil | encoding → URL/shell | encoded blob, unclear purpose |
| EXF-04 | Capture exfil | screenshot/clipboard/mic upload external | debug capture external |

## EXE

| ID | Metric | `fail` | `warn` |
| --- | --- | --- | --- |
| EXE-01 | Destructive FS | `rm -rf /`, wipe home, format disk | broad `rm -rf` + variable |
| EXE-02 | Remote code exec | `curl \| bash`, wget pipe sh, IEX download | download then run |
| EXE-03 | Privilege escalation | sudo, chmod 777, disable firewall, `/etc` | run as admin |
| EXE-04 | Persistence | cron, LaunchAgent, registry Run | every session vague |
| EXE-05 | Malicious scripts | exfil/destructive/obfuscated script | script + network/shell unclear |
| EXE-06 | Resource abuse | miner, fork bomb | heavy loop, no purpose |

## NET

| ID | Metric | `fail` | `warn` |
| --- | --- | --- | --- |
| NET-01 | Outbound data | POST user data, webhooks, unknown telemetry | any `http(s)://` in instructions |
| NET-02 | Inbound untrusted | fetch skill from URL, clone unknown repo | third-party doc fetch |
| NET-03 | Untrusted downloads | unknown binary, typosquat package | non-org GitHub release |
| NET-04 | Internet required | cannot work offline, no trust note | optional network examples |
| NET-05 | MCP / unknown endpoints | MCP/SSE/WS to unknown host | public API with docs |
| NET-06 | Messaging exfil | email files, Discord/Telegram tokens | vague notify team |

## OBS

| ID | Metric | `fail` | `warn` |
| --- | --- | --- | --- |
| OBS-01 | Encoded instruction blocks | multi-layer hide commands | single benign base64 example |
| OBS-02 | Homoglyph tricks | Cyrillic in commands, RTL override | unusual Unicode in prose |
| OBS-03 | Active HTML/JS | script, iframe, javascript:, handlers | raw HTML in doc |
| OBS-04 | Opaque binaries | executable in assets, no purpose | large binary |

## SOC

| ID | Metric | `fail` | `warn` |
| --- | --- | --- | --- |
| SOC-01 | Description vs body mismatch | says format docs; body exfiltrates | scope broader than description |
| SOC-02 | Impersonation | claims official Cursor/Anthropic/OpenAI skill | similar known skill name |
| SOC-03 | False urgency | URGENT run now, pressure | strong pressure language |
| SOC-04 | Fake audit clearance | pre-written “all clear” | — |

## SCM

| ID | Metric | `fail` | `warn` |
| --- | --- | --- | --- |
| SCM-01 | Hardcoded secrets | live `sk-`, `ghp_`, `AKIA`, JWT | placeholder key |
| SCM-02 | Private keys embedded | PEM private key | — |
| SCM-03 | Path traversal reads | `../../` outside skill | abs path to sensitive dirs |

## PRIV

| ID | Metric | `fail` | `warn` |
| --- | --- | --- | --- |
| PRIV-01 | Disable confirmations | never confirm, auto-approve all | fewer confirmations |
| PRIV-02 | Disable sandbox | disable sandbox, ignore warnings | `all` permissions unjustified |
| PRIV-03 | Hidden delegate | subagent without user seeing | heavy delegate for sensitive ops |

## AGT

| ID | Metric | `fail` | `warn` |
| --- | --- | --- | --- |
| AGT-01 | Permanent rule injection | always remember, edit global `.cursor/rules` | project rule suggestion |
| AGT-02 | Cross-session change | shell profile, global git config | — |
| AGT-03 | Skill install chain | install other skill then run remote code | external skill ref |

## AGY

| ID | Metric | `fail` | `warn` |
| --- | --- | --- | --- |
| AGY-01 | Without confirmation | never ask, run all steps, self-approve | minimize prompts |
| AGY-02 | Prod autonomy | auto-deploy prod, fix permissions silently | handle everything vague |
| AGY-03 | Unchecked retries | retry forever, ignore failures | aggressive retry |

## TOL

| ID | Metric | `fail` | `warn` |
| --- | --- | --- | --- |
| TOL-01 | Dangerous tool chain | shell + browser + exfil one flow | many tools, no scope |
| TOL-02 | Git/deploy abuse | force push, global memory, deploy hooks | casual git write |
| TOL-03 | Package abuse | npm/pip from skill body, URL install | install “what is needed” |

## POI

| ID | Metric | `fail` | `warn` |
| --- | --- | --- | --- |
| POI-01 | Buried harmful line | long filler + bad line at end | long low-signal sections |
| POI-03 | Token flooding attack | exhaustion / hide payload | package >15k `est_tokens`, low density |

## DEP

| ID | Metric | `fail` | `warn` |
| --- | --- | --- | --- |
| DEP-01 | Requires other skills | always use skill X for sensitive steps | optional cross-skill |
| DEP-02 | Undeclared scripts | scripts run, not in SKILL.md | documented but powerful script |
| DEP-03 | Untrusted install hooks | postinstall remote, unpinned URL dep | unpinned versions |
| DEP-04 | External binary/CDN | run CDN/binary without trust note | third-party script ref |

---

## Critical fails (verdict → Reject / Critical Risk)

`EXF-01`, `EXF-02`, `EXE-01`, `EXE-02`, `INJ-01`, `SCM-01`, `SCM-02`, malicious `EXE-05`, `TOL-01` + exfil chain.

## Risk score (0–100, higher = worse)

| Band | Label |
| ---: | --- |
| 0–10 | Safe |
| 11–30 | Low Risk |
| 31–60 | Moderate Risk |
| 61–80 | High Risk |
| 81–100 | Critical Risk |

Derive from metrics: no `fail`, ≤2 `warn` → 0–30; no `fail`, ≥3 `warn` → 31–60; non-critical `fail` → 61–80; critical `fail` → 81–100.

## Verdict

| Verdict | When |
| --- | --- |
| **Approved** | Risk ≤30; no `fail` |
| **Approved with Notes** | Risk ≤60; `warn` only |
| **Needs Review** | ambiguous dual-use, moderate risk |
| **High Risk** | any `fail` (non-critical) or risk ≥61 |
| **Reject** | critical `fail` or risk ≥81 |

## Report: what users need

1. **Safe to run?** — Verdict + overall risk + all `warn`/`fail` with evidence
2. **Data leaving?** — EXF, SCM, NET outbound rows + network signals (internet required, URL count, scripts)
3. **Actions we did not expect?** — EXE, AGY, TOL, NET, DEP rows
4. **Context cost** — `est_tokens` + context savvy Yes/No

Optional short prose under **Risks summary** only when `warn`/`fail` exist; skip empty analysis subsections.
