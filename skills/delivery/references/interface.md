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

1. Review readiness — `$delivery-review`
2. Groom or shape a plan — `$delivery-plan`
3. Execute an approved sequence — `$delivery-execute`
4. List horizons, plans and features — `$delivery list`
5. Configure or import tracking — `$delivery setup`
6. Audit delivery state — `$delivery audit`
7. Show help — `$delivery help`

## List

`$delivery list` is read-only. List plans by default and accept a horizon, plan, feature, planning-state, delivery-status, owner, or rollout filter. When listing features, show their plan/horizon, planning state, delivery status, owner, dependencies, rollout state, eligibility result, and immediate next action.

Include recommended model/effort when discussing assignment, complexity or execution settings; distinguish them from actual settings on in-progress work.

Prefer a compact table. Read feature frontmatter when the requested detail is not trustworthy from the index or plan rollup. Do not silently repair mismatches while listing.

## Help

Present the three autocomplete entry points as the primary workflow:

- `$delivery-review`: optional read-only readiness assessment.
- `$delivery-plan`: prepare or revise the plan and resolve discoverable gaps.
- `$delivery-execute`: preflight and coordinate approved features; prepare authorized gaps or surface required decisions before proceeding.

They load shared Delivery automatically; users need not invoke it first or invoke all three in order. Natural-language requests may select a relevant skill when implicit invocation is enabled; explicit autocomplete selection makes the intended mode unambiguous. Skills do not run independently in the background.

Use `$delivery` directly for the dashboard, `list`, `setup`, `audit` and `help`. Preserve `review`, `plan` and `run` as compatible mode aliases and `next` for one eligible feature. Mention `handoff` only for advanced recovery after a pause, ownership transfer or stale checkpoint.
