# Delivery state

This repository uses the global `$delivery` skill and the local configuration in [`config.yaml`](config.yaml).

## Start

- View the delivery dashboard: `$delivery`
- List initiatives or features: `$delivery list`
- Configure or revise the contract: `$delivery setup`
- Groom or plan an initiative: `$delivery plan`
- Execute the next approved feature: `$delivery next`
- Check state coherence: `$delivery audit`
- Show the interface: `$delivery help`

## Local state

- [`INDEX.md`](INDEX.md): initiative registry and next feature.
- `<initiative>/PLAN.md`: outcome, decisions, dependency graph, and rollout strategy.
- `<initiative>/features/*.md`: canonical executable feature records.
- `<initiative>/records/*.md`: detailed acceptance evidence when needed.
- [`handoff.md`](handoff.md): replaceable runtime checkpoint.

Planning and execution update `handoff.md` automatically. Use `$delivery handoff` only for an explicit pause, ownership transfer, or checkpoint repair.

Tracker routing, paths, verification overrides, and rollout authority live only in `config.yaml`. Generic workflow and status semantics live in `$delivery`.
