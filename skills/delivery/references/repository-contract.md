# Repository contract

Use this layout only when the repository has no established alternative:

```text
.github/plans/
├── config.yaml
├── README.md
├── INDEX.md
├── handoff.md
├── LEGACY-BACKLOG.md          # optional during migration
├── templates/
│   ├── plan-template.md
│   ├── feature-template.md
│   └── contract-freeze-template.md
└── plans/
    └── <plan>/
        ├── PLAN.md
        ├── features/
        │   └── NN-<feature>.md
        └── records/           # evidence and approved shared-contract freezes
            └── <feature>-acceptance.md
```

The default hierarchy is:

```text
Portfolio horizon
└── Outcome plan
    └── Vertical feature
        └── Task, checklist item, sub-ticket, or pull request
```

`PLAN.md` is the plan record, not another hierarchy layer. A horizon expresses strategic direction
and may live only in the portfolio tracker. A plan ends when one observable outcome and its release
boundary are complete. A feature is independently reviewable. Tasks do not own delivery scope.

## Sources of truth

- `config.yaml`: contract version, paths, tracker routing, local verification profile, and rollout authority.
- `README.md`: short human-facing entrypoint generated from the configuration; it does not duplicate this skill.
- `INDEX.md`: horizon/plan registry, coarse state, and next decision or eligible feature.
- `plans/<plan>/PLAN.md`: outcome, decisions, dependency graph, feature order, and rollout strategy.
- `features/*.md`: canonical executable contract and completion record for one vertical delivery.
- `records/*.md`: detailed evidence that is not needed to choose or execute the next action.
- `handoff.md`: replaceable runtime checkpoint.
- `LEGACY-BACKLOG.md`: unmigrated work only; migrate an item when it is selected.
- External trackers: canonical or mirrors per artifact type, as declared in `config.yaml`.

The manifest may route different work to different systems. Portfolio horizons, plans, features,
tasks, public bugs, pull requests, handoffs, and evidence do not need the same canonical tracker.
Declare field-level authority when one artifact is split across systems. Reconciliation is advisory;
never let timestamps decide a conflict or assume one provider ticket equals one vertical feature.

Plans and features that originate outside Git carry stable provenance:

```yaml
external_refs:
  - provider: linear
    entity_type: issue
    id: WAM-123
    url: https://linear.app/example/issue/WAM-123/example
    provider_revision: null
    observed_at: 2026-09-10T05:00:05-06:00
```

Provider IDs identify records. `config.yaml` assigns canonical ownership per artifact or field; the newest timestamp is not an authority rule.

## Feature execution recommendations

Each new canonical feature includes `recommended_model`, `recommended_reasoning_effort`,
and `reasoning_rationale` in its YAML frontmatter. These fields describe a recommendation,
not approval, assignment or automatic host configuration. Null means unresolved or unavailable;
explain which in the rationale. Preserve existing records and fill missing fields when planning
or selecting active work rather than rewriting completed history.

Use [model and effort selection](model-selection.md) for field semantics, complexity criteria,
user overrides and dispatch. Record actual execution settings separately in the feature checkpoint.

## State dimensions and transitions

Use the repository's vocabulary when present. For a new contract, keep the dimensions independent.

### Plan status

- `proposed -> active -> completed`
- `blocked` is a temporary execution condition; `canceled` and `superseded` are terminal alternatives.
- `proposed -> active` requires plan planning `approved`, portfolio priority reconciled, and a plan owner.

### Feature delivery status

- `not_started`: no implementation has begun.
- `in_progress`: one write owner is executing it.
- `in_review`: implementation awaits configured review/completion gates.
- `blocked`: a named decision or dependency prevents progress.
- `completed`: implementation, verification, review, documentation, and commit record are complete.
- `canceled`: intentionally stopped without a replacement; preserve the reason.
- `superseded`: replaced by a linked record.

The normal flow is `not_started -> in_progress -> in_review -> completed`. Blocking and recovery
must record the prior state. Delivery status never encodes approval maturity.

Map an external `deprecated` state to `superseded` when a replacement exists, or `canceled` when the work was intentionally abandoned. Preserve the provider's original state and reference.

## Planning maturity

Use `planning_state` independently on plans and features:

- `intake`: provenance is captured, but classification and repository analysis are incomplete.
- `needs_grooming`: the intended outcome is known, but material decisions or implementation evidence are missing.
- `ready_for_approval`: outcome, scope, dependencies, and verification are reviewable; implementation is not approved.
- `approved`: planning is approved; execution still depends on plan activation, dependency status,
  ownership, WIP, and parallel-safety gates.

A tracker item does not become eligible for execution from priority, assignment, or provider status alone.

### `$delivery next` eligibility

Unless the local contract overrides it, a feature is eligible to start only when all are true:

- containing plan is `active / approved` and portfolio priority is reconciled;
- feature is `not_started / approved`;
- every dependency is `completed`;
- owner and non-empty physical boundary are assigned;
- selecting it stays within plan WIP;
- every applicable parallel requirement is true.

Report the first actionable failed predicate. Do not silently activate plans, approve planning, or
assign owners as a side effect of selection.

This predicate selects new work. Resume owned `in_progress` work or continue `in_review` gates
through the handoff after rechecking approval, plan activation, dependencies, ownership, WIP,
and applicable parallel safety. Count its existing WIP slot once; do not reset delivery status
to satisfy new-work eligibility. Resolve a blocker before restoring its recorded prior state.

### Contract freeze

Freeze records use `draft -> approved -> superseded`. `shared_contracts_frozen` is true only while
an approved record covers every feature in the parallel window, exact shared schemas/signatures/DDL,
file/function ownership, merge order, independent QA, and current owner/reviewer approvals. Any
material contract change supersedes the record and closes the parallel window. The scheduler then
falls back to serial dependency/priority order until a new freeze is approved.

### Review and completion

Define review severities and blocking levels in `config.yaml`. A default low-risk feature may use
owner self-review plus independent QA. Finance, auth, security, or similarly consequential work
should require architecture/domain review followed by independent QA. `in_review -> completed`
requires the definition of done, verification, every required review stage, and zero blocking findings.

### Rollout state

- `not_applicable`: no independent exposure.
- `gated`: exposure stays disabled.
- `authorized`: exposure was explicitly authorized but is not yet verified live.
- `released`: authorized exposure is active and verified.
- `pending_reconciliation`: historical exposure exists but evidence is incomplete.
- `rolled_back`: exposure was reverted and the safe state is recorded.

Normal rollout is `gated -> authorized -> released -> rolled_back`; a repaired release may move
`rolled_back -> authorized`. Authorization requires a green release gate plus a documented exposure
and recovery mechanism. Release requires verification evidence. Reconciliation may move historical
work to `gated` or `released` only with evidence. Rollout never proves implementation completeness,
and local readiness never authorizes production.

## Compatibility with existing contracts

The repository contract overrides these defaults. Preserve existing vocabulary and manifest versions
until the user approves migration. During an explicit migration, map meaning rather than strings:

- a broad legacy `initiative` usually becomes a horizon; a bounded one becomes a plan;
- delivery `draft` becomes `not_started` while planning maturity remains separate;
- delivery `approved` becomes planning `approved`, not execution started;
- planning `ready` becomes `approved`;
- rollout `ready_for_decision / approved / live` maps to `gated / authorized / released` only after
  verifying its original semantics and evidence.

Report ambiguous mappings and preserve historical records instead of bulk-rewriting them.
