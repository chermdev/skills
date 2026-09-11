# Delivery state

This repository uses the global `$delivery` skill and the local configuration in [`config.yaml`](config.yaml).

## Start

- View the delivery dashboard: `$delivery`
- List horizons, plans, or features: `$delivery list`
- Configure or revise the contract: `$delivery setup`
- Groom or shape an outcome plan: `$delivery plan`
- Execute the next approved feature: `$delivery next`
- Check state coherence: `$delivery audit`
- Show the interface: `$delivery help`

## Local state

- [`INDEX.md`](INDEX.md): horizon/plan registry, next decision, and eligible feature.
- `plans/<plan>/PLAN.md`: outcome, decisions, dependency graph, and rollout strategy.
- `plans/<plan>/features/*.md`: canonical executable feature records.
- `plans/<plan>/records/*.md`: detailed evidence and approved contract freezes when needed.
- [`handoff.md`](handoff.md): replaceable runtime checkpoint.

Planning and execution update `handoff.md` automatically. Use `$delivery handoff` only for an explicit pause, ownership transfer, or checkpoint repair.

Tracker routing, paths, verification overrides, and rollout authority live only in `config.yaml`. Generic workflow and status semantics live in `$delivery`.

The default hierarchy is `Horizon -> Outcome plan -> Vertical feature -> Task`. Planning maturity,
delivery progress, and rollout exposure are independent. `$delivery next` never changes those states
implicitly; it reports the first failed eligibility gate.
