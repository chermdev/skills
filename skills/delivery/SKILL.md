---
name: delivery
description: Plan, execute, resume, or audit structured multi-session delivery with feature ownership and durable handoffs. Use for delivery plans and tracker reconciliation; handle ordinary fixes and standalone reviews directly.
---

# Delivery

Use repository files as shared memory while keeping each execution path small enough to scan.

## Interface and modes

The user only needs to remember `$delivery`. Infer a mode from natural language or route an explicit mode:

- `$delivery`: show the read-only delivery dashboard and a numbered action menu. `$delivery list` lists horizons, plans, or features with optional filters, and `$delivery help` explains the interface. Read [interface](references/interface.md).
- `$delivery setup`: discover the repository, decide where work is tracked, initialize the local contract, or migrate existing tracker state. Read [setup](references/setup.md).
- `$delivery plan`: groom an intake plan or shape an explored outcome into vertical features. Read [planning](references/planning.md).
- `$delivery next`: execute the next approved, unblocked feature. Read [execution](references/execution.md).
- `$delivery audit`: find local drift or reconcile configured external mirrors without blind bidirectional sync. Read [maintenance](references/maintenance.md).

`$delivery handoff` remains an advanced recovery alias for an explicit pause, ownership transfer, or stale-checkpoint repair. Normal planning and execution maintain the handoff automatically. Read only the reference for the selected mode.

## Enter the repository contract

Use the applicable `AGENTS.md` already in context, then read the delivery manifest or planning entrypoint it identifies. Read the selected mode reference once; reopen only changed or newly relevant sections. Preserve existing paths, trackers, statuses, and local verification rules; the repository contract overrides this skill's defaults.

If no contract exists, run setup only when the user asks to configure delivery or requests structured multi-session planning. Do not scaffold planning files for an ordinary change.

## Proportionate execution

- Keep one coordinator and one writer per feature; honor the user-selected task topology. Delegation must answer a bounded independent question, not reproduce the owner’s full workflow. Reviewers do not delegate further by default.
- The coordinator checks eligibility and rollups; a feature owner needs its canonical feature, relevant contracts and scoped instructions, not the entire portfolio.
- Select verification and review by changed behavior and failure impact. Preserve stronger repository gates, but do not infer a security review merely from working in an app that handles money.
- Use existing evidence for unchanged code and environment; after fixes, verify the affected invariant and expand only for a stated regression risk.
- When repeated attempts produce no new evidence or implementation progress, narrow the hypothesis, change tools, or separate newly discovered scope. Do not add more agents or effort without a specific reason.

## Invariants

- Use `Horizon -> Outcome plan -> Vertical feature -> Task` as the default hierarchy. A provider entity named “initiative” maps by meaning: strategic direction becomes a horizon; a bounded outcome becomes a plan.
- One canonical feature record owns scope, dependencies, implementation progress, checks, review, and completion. Tasks remain implementation detail inside that feature, a pull request, or an explicitly linked sub-ticket.
- Rollups summarize and link. They do not copy feature checklists or evidence.
- Feature frontmatter records a recommended model, reasoning effort, and complexity rationale. Apply the repository/user policy and available host capabilities; recommendations do not authorize execution or delegation.
- `planning_state` describes planning maturity. `status` describes delivery progress. `rollout_state` describes exposure; delivery can be complete while rollout is still gated.
- `$delivery next` selects work only through the repository's explicit eligibility predicate; priority, approval, assignment, or a tracker status alone is insufficient.
- One task or worktree owns writes for a feature. `parallelizable_with` is candidate compatibility, not permission. Parallel execution also requires dependency completion, an approved shared-contract freeze, disjoint physical ownership, safe merge order, independent QA, and available WIP.
- Features are vertical deliveries with a visible or operable outcome, not horizontal implementation phases.
- Completion requires deterministic verification and review gates. Exposure follows its own guarded rollout transitions and explicit authorization.
- Detailed logs, failed attempts, screenshots, timings, and commit ledgers move to disclosed evidence records when they bury the executable contract.
- Imported work preserves provider IDs and URLs. Canonical field ownership decides conflicts; timestamps never silently decide them.
- Production deployment, tenant enablement, external messages, tracker mutations, and other consequential actions still require the authorization implied by the user's request and local rules.

Finish with the repository's canonical state coherent and the immediate next action discoverable without reconstructing the conversation.
