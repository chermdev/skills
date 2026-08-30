# Dashboard, list, and help

## Dashboard

With no explicit mode, read the repository contract, index, active initiative and feature records, and current handoff. If no contract exists, report that delivery is unconfigured and offer setup without creating files.

Show a compact, read-only dashboard containing:

- initiative and feature counts by delivery status and planning maturity;
- active owner, branch/worktree, and current feature;
- blockers or user decisions;
- the next approved, unblocked feature—or the next initiative needing grooming;
- rollout decisions and pending external mirrors that affect the next action.

Use canonical records for details. Surface an obvious rollup mismatch as a warning; reserve repository-wide reconciliation and provider reads for `$delivery audit`.

End with a numbered menu. Accept a number or natural-language follow-up:

1. List plans and features
2. Configure or import tracking
3. Groom or plan an initiative
4. Execute the next feature
5. Audit delivery state
6. Show help

## List

`$delivery list` is read-only. List initiatives by default and accept filters such as `active`, `blocked`, `draft`, `needs-grooming`, `ready`, `completed`, or an initiative name. When listing features, show their initiative, planning state, delivery status, owner, dependencies, rollout state, and immediate next action.

Prefer a compact table. Read feature frontmatter when the requested detail is not trustworthy from the index or initiative rollup. Do not silently repair mismatches while listing.

## Help

Explain that natural language is the primary interface and show only the public modes: `$delivery`, `list`, `setup`, `plan`, `next`, `audit`, and `help`. Mention `$delivery handoff` only under advanced recovery for an explicit pause, transfer, or repair.
