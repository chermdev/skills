---
name: delivery
description: Plan, execute, resume, or audit structured multi-session delivery with feature ownership and durable handoffs. Use for delivery plans and tracker reconciliation; handle ordinary fixes and standalone reviews directly.
---

# Delivery

Use repository files as shared memory while keeping each execution path small enough to scan.

## Interface and modes

Use `$delivery` for the dashboard. Autocomplete entry points `delivery-review`, `delivery-plan` and `delivery-execute` select the shared modes below; they depend on this skill and do not copy its rules. Infer a mode from natural language or route an explicit mode:

- `$delivery`: show the read-only delivery dashboard and a numbered action menu. `$delivery list` lists horizons, plans, or features with optional filters, and `$delivery help` explains the interface. Read [interface](references/interface.md).
- `$delivery setup`: discover the repository, decide where work is tracked, initialize the local contract, or migrate existing tracker state. Read [setup](references/setup.md).
- `$delivery review` / `$delivery-review`: assess readiness read-only; identify decisions and bounded spikes. Read [readiness](references/readiness.md).
- `$delivery run` / `$delivery-execute`: check readiness, prepare authorized gaps and coordinate the approved sequence through completion events. Read [run](references/run.md).
- `$delivery plan` / `$delivery-plan`: groom an intake plan or shape an explored outcome into vertical features. Read [planning](references/planning.md).
- `$delivery next`: execute the next approved, unblocked feature. Read [execution](references/execution.md).
- `$delivery audit`: find local drift or reconcile configured external mirrors without blind bidirectional sync. Read [maintenance](references/maintenance.md).

`$delivery handoff` remains an advanced recovery alias for an explicit pause, ownership transfer, or stale-checkpoint repair. Normal planning and execution maintain the handoff automatically. Read only the reference for the selected mode.

## Enter the repository contract

Use the applicable `AGENTS.md` already in context, then read the delivery manifest or planning entrypoint it identifies. Read the selected mode reference once; reopen only changed or newly relevant sections. Preserve existing paths, trackers, statuses, and local verification rules; the repository contract overrides this skill's defaults.

If no contract exists, run setup only when the user asks to configure delivery or requests structured multi-session planning. Do not scaffold planning files for an ordinary change.

## Shared contract

- Keep one canonical feature record for scope, dependencies, progress and evidence. Rollups summarize and link; they do not copy checklists or detailed logs.
- Use `Horizon -> Outcome plan -> Vertical feature -> Task` as the default hierarchy. Map imported entities by meaning and preserve provider IDs/URLs and canonical field ownership.
- Keep planning maturity, delivery progress and rollout exposure separate. Readiness and ordering do not grant scope approval or execution authorization.
- Repository-specific paths, providers, models, effort, task topology and eligibility live in the repository contract. Do not replace them with global constants or infer authorization from configuration alone.
- Read only what the selected mode needs. Planning owns feature shaping; readiness owns assessment criteria; execution owns dispatch, model/effort enforcement, verification, bug handling and agent coordination. Sequence orchestration uses execution rather than redefining it.
- Consequential actions remain bounded by the user's authorization and host/repository rules. Completion does not authorize deployment or exposure.

## Companion entry points

`delivery-review`, `delivery-plan` and `delivery-execute` load this shared skill and their selected reference. Resolve `delivery` (including a plugin-prefixed name) from the available skill catalog; in a source checkout, use the sibling `../delivery/SKILL.md`. Resolve reference paths from the Delivery root. If the companion is missing, report the required selected installation; do not fetch it silently or invent a replacement workflow.

These entry points select a mode; they do not change the calling agent's model. Execution settings are applied through host controls by the execution workflow. Users can select an entry point explicitly through autocomplete, or the agent can select a relevant skill from a natural-language request when the host permits implicit invocation. Selection is not a background trigger or a scheduler.

Finish with the canonical state coherent for the selected mode; read-only modes report findings without repairing records.
