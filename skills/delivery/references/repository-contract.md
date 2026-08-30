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
│   └── feature-template.md
└── <initiative>/
    ├── PLAN.md
    ├── features/
    │   └── NN-<feature>.md
    └── records/               # only when detailed evidence needs disclosure
        └── <feature>-acceptance.md
```

## Sources of truth

- `config.yaml`: contract version, paths, tracker routing, local verification profile, and rollout authority.
- `README.md`: short human-facing entrypoint generated from the configuration; it does not duplicate this skill.
- `INDEX.md`: initiative registry and coarse next feature.
- `<initiative>/PLAN.md`: outcome, decisions, dependency graph, feature order, and rollout strategy.
- `features/*.md`: canonical executable contract and completion record for one vertical delivery.
- `records/*.md`: detailed evidence that is not needed to choose or execute the next action.
- `handoff.md`: replaceable runtime checkpoint.
- `LEGACY-BACKLOG.md`: unmigrated work only; migrate an item when it is selected.
- External trackers: canonical or mirrors per artifact type, as declared in `config.yaml`.

The manifest may route different work to different systems. Roadmap initiatives, implementation features, public bugs, pull requests, handoffs, and evidence do not need the same canonical tracker.

Plans and features that originate outside Git carry stable provenance:

```yaml
external_refs:
  - provider: linear
    id: WAM-123
    url: https://linear.app/example/issue/WAM-123/example
    last_observed_revision: null
```

Provider IDs identify records. `config.yaml` assigns canonical ownership per artifact or field; the newest timestamp is not an authority rule.

## Implementation status

Use the repository's vocabulary when present. Suggested values:

- `draft`: still being shaped.
- `approved`: scope and dependency order are approved.
- `in_progress`: one write owner is executing it.
- `blocked`: a named decision or dependency prevents progress.
- `completed`: implementation, verification, review, documentation, and commit record are complete.
- `canceled`: intentionally stopped without a replacement; preserve the reason.
- `superseded`: replaced by a linked record.

Map an external `deprecated` state to `superseded` when a replacement exists, or `canceled` when the work was intentionally abandoned. Preserve the provider's original state and reference.

## Planning maturity

Use `planning_state` independently on initiatives and features:

- `intake`: provenance is captured, but classification and repository analysis are incomplete.
- `needs_grooming`: the intended outcome is known, but material decisions or implementation evidence are missing.
- `ready_for_approval`: outcome, scope, dependencies, and verification are reviewable; implementation is not approved.
- `ready`: planning is approved and the record may execute when its delivery status and dependencies permit it.

A tracker item does not become `ready` from priority, assignment, or provider status alone.

## Rollout state

- `not_applicable`: no independent exposure.
- `gated`: exposure stays disabled.
- `ready_for_decision`: implementation is complete and awaits explicit authorization.
- `approved`: exposure was authorized but has not started.
- `live`: approved exposure is active and verified.
- `rolled_back`: exposure was reverted and the safe state is recorded.

Rollout never proves implementation completeness. Local readiness never authorizes production.
