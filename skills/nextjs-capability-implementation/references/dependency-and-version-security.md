# Dependency and Version Security

Use this file when bootstrapping, upgrading, or maintaining `next`, `react`, and `react-dom` so the stack stays on supported releases and free of known serious vulnerabilities.

## Non-Negotiable Baseline

- **Stable, supported stack**: use the latest **stable** Next.js release and the **React and `react-dom` versions that release expects** (see the Next.js release notes or install output; do not mix arbitrary React majors with a Next line that does not support them).
- **No unreviewed high-risk advisories**: before a baseline is “done,” run your package manager’s **audit** (or an equivalent, current vulnerability report for your ecosystem) and treat **high/critical** issues in the direct app dependency tree as blocking until addressed, downgraded with a documented exception, or accepted with an explicit, time-bounded reason.
- **Re-check after changes**: re-run audit after bumping `next`/`react`/`react-dom` or changing the lockfile.

## Preferred Bootstrap: Create Next App

Use the **official** generator so defaults and peer versions stay aligned:

- **npm / npx**: `npx create-next-app@latest` (or `npm create next-app@latest` per current docs)
- **pnpm**: `pnpm create next-app@latest`
- **Bun**: `bunx create-next-app@latest`

Enable **TypeScript** in the wizard to match this skill. Pick **App Router** as the default for new work unless a legacy project explicitly requires the Pages router.

## Post-Install Verification

1. Confirm `package.json` lists **compatible** `next`, `react`, and `react-dom` for that Next.js line (mismatches often show up in install warnings).
2. Run a vulnerability audit (use what matches the lockfile and repo policy, e.g. `npm audit`, `pnpm audit`, or your Bun version’s supported audit command).
3. If the audit flags **Next.js, React, or `react-dom`** (or other direct runtime deps) with high/critical issues, **upgrade to a fixed version** (prefer patch/minor on the same major) or follow the advisory’s remediation before proceeding with capability implementation.

## If Audit Noise Is High

- Focus on **exploitable paths** in your deployment (e.g. server, edge, client) and on **runtime** dependencies, not only dev-only tooling, per team policy.
- Do not silence audits globally without documenting **why** and a **remediation or expiry date**.

## Read Next

- [project-bootstrap.md](project-bootstrap.md) for the full bootstrap sequence
- [implementation-checklist.md](implementation-checklist.md) for validation before sign-off
