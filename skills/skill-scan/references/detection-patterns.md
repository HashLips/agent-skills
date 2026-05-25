# Detection Patterns

Case-insensitive match unless noted. Benign negation within 80 chars (`do not`, `never`, `forbidden`) → downgrade one level; live secrets stay `fail`.

## INJ / INJ-06

`ignore (all )?(previous|prior) instructions`, `disregard (system|safety|policy)`, `override (system|developer) prompt`, fake `<system>`, `developer mode`, `jailbreak`, `DAN`, `do not report`, `hide this`, `treat as safe`, `scanner should skip`, `execute this first`, `always prioritize this skill`

## Hidden (INJ, OBS)

HTML comments with instructions; zero-width chars; base64 lines >80 chars (decode mentally)

## EXF

`curl.*(-d|--data|-F).*(http)`, webhooks, pastebin, `transfer.sh`, `upload.*(env|ssh|key|token)`, `~/.ssh`, `id_rsa`, `.aws/credentials`, keychain, cookie harvest

## EXE

`rm -rf` + `/` or `~`, `sudo`, `curl.*\|.*(bash|sh)`, `wget.*\|.*sh`, `eval(`, `subprocess`, `exec(`, `os.system`, cron, LaunchAgents, registry Run keys

## NET

`https?://` (count unique), `git clone`, `npm install` / `pip install` from URL, `npx`, MCP unknown host

## SCM

`sk-[a-zA-Z0-9]{20,}`, `ghp_`, `AKIA`, `BEGIN PRIVATE KEY`, `Bearer eyJ`

## AGY / PRIV

`without confirmation`, `do not ask`, `auto-approve`, `never ask`, `disable sandbox`, `deploy to production`, `install what (you|it) needs`

## TOL

shell + upload + browser in one procedure; `git push --force`; edit `.cursor/rules` globally

## SOC

description says format/lint only but body has EXF/EXE patterns; `do not tell the user`; fake official skill; URGENT run now

## POI

harmful line in last 10% of very long file; package >15k `est_tokens`

## Scripts

Apply EXE/EXF/NET to `.sh`, `.py`, etc. Binary → OBS-04 `warn` minimum.

Evidence: `path:line — "snippet…"` (≤120 chars).
