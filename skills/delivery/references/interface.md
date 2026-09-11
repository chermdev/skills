# Dashboard, list, and help

## Dashboard

With no explicit mode, read the repository contract, index, active plan and feature records, and current handoff. If no contract exists, report that delivery is unconfigured and offer setup without creating files.

Show a compact, read-only dashboard containing:

- horizon, plan, and feature counts by delivery status and planning maturity;
- active owner, branch/worktree, and current feature;
- blockers or user decisions;
- the next eligible feature—or the next plan needing grooming, activation, or priority reconciliation;
- rollout decisions and pending external mirrors that affect the next action.

Use canonical records for details. Surface an obvious rollup mismatch as a warning; reserve repository-wide reconciliation and provider reads for `$delivery audit`.

End with a numbered menu. Accept a number or natural-language follow-up:

1. List horizons, plans, and features
2. Configure or import tracking
3. Groom or shape a plan
4. Execute the next feature
5. Audit delivery state
6. Show help

## List

`$delivery list` is read-only. List plans by default and accept a horizon, plan, feature, planning-state, delivery-status, owner, or rollout filter. When listing features, show their plan/horizon, planning state, delivery status, owner, dependencies, rollout state, eligibility result, and immediate next action.

Include recommended model/effort when discussing assignment, complexity or execution settings; distinguish them from actual settings on in-progress work.

Prefer a compact table. Read feature frontmatter when the requested detail is not trustworthy from the index or plan rollup. Do not silently repair mismatches while listing.

## Help

Explain that natural language is the primary interface and show only the public modes: `$delivery`, `list`, `setup`, `plan`, `next`, `audit`, and `help`. Mention `$delivery handoff` only under advanced recovery for an explicit pause, transfer, or repair.
