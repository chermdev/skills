---
name: delivery
description: Inspect, set up, groom, plan, execute, or audit multi-session software delivery using durable initiative and vertical-feature records, explicit ownership, QA/review gates, automatic checkpoints, and rollout tracked separately. Use for structured initiatives and tracker intake; deployment-only and ordinary single-session changes use other workflows.
---

# Delivery

Use repository files as shared memory while keeping each execution path small enough to scan.

## Interface and modes

The user only needs to remember `$delivery`. Infer a mode from natural language or route an explicit mode:

- `$delivery`: show the read-only delivery dashboard and a numbered action menu. `$delivery list` lists initiatives or features with optional filters, and `$delivery help` explains the interface. Read [interface](references/interface.md).
- `$delivery setup`: discover the repository, decide where work is tracked, initialize the local contract, or migrate existing tracker state. Read [setup](references/setup.md).
- `$delivery plan`: groom an intake initiative or shape an explored outcome into vertical features. Read [planning](references/planning.md).
- `$delivery next`: execute the next approved, unblocked feature. Read [execution](references/execution.md).
- `$delivery audit`: find local drift or reconcile configured external mirrors without blind bidirectional sync. Read [maintenance](references/maintenance.md).

`$delivery handoff` remains an advanced recovery alias for an explicit pause, ownership transfer, or stale-checkpoint repair. Normal planning and execution maintain the handoff automatically. Read only the reference for the selected mode.

## Enter the repository contract

Read the nearest `AGENTS.md`, then the configured delivery manifest or planning document it points to. Preserve existing paths, trackers, statuses, and local verification rules; the repository contract overrides this skill's defaults.

If no contract exists, run setup only when the user asks to configure delivery or requests structured multi-session planning. Do not scaffold planning files for an ordinary change.

## Invariants

- One canonical feature record owns scope, dependencies, implementation progress, checks, review, and completion.
- Rollups summarize and link. They do not copy feature checklists or evidence.
- `planning_state` describes planning maturity. `status` describes delivery progress. `rollout_state` describes exposure; delivery can be complete while rollout is still gated.
- One task or worktree owns writes for a feature. Parallel work is limited to independent features or bounded read-only evidence.
- Features are vertical deliveries with a visible or operable outcome, not horizontal implementation phases.
- Detailed logs, failed attempts, screenshots, timings, and commit ledgers move to disclosed evidence records when they bury the executable contract.
- Imported work preserves provider IDs and URLs. Canonical field ownership decides conflicts; timestamps never silently decide them.
- Production deployment, tenant enablement, external messages, tracker mutations, and other consequential actions still require the authorization implied by the user's request and local rules.

Finish with the repository's canonical state coherent and the immediate next action discoverable without reconstructing the conversation.
