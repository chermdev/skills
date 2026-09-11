# Coordination and maintenance

## Automatic checkpoint

Treat the handoff as a replaceable checkpoint, not a journal. Keep only:

- active branch/worktree and owner;
- services or disposable resources needed for the next action;
- current feature, blocker, rollout state, and immediate next action;
- pending external mirrors.

Link to canonical features, evidence, runbooks, and legacy backlog. Remove superseded checkpoints; Git preserves history.

Planning and execution own this update automatically at meaningful transitions. Use the explicit `$delivery handoff` alias only to pause mid-feature, transfer ownership, preserve state before a context boundary, or repair a stale checkpoint after interruption.

## Progressive disclosure

When a feature's objective, scope, next action, or definition of done becomes hard to find, move detailed matrices, logs, failed attempts, timing data, artifacts, and immutable ledgers into `records/`. Leave the feature's verdict, limitations, commands, important checkpoint, and link.

## Coherence audit

`$delivery audit` is the deliberate repository-wide operation. It is broader than the lightweight coherence check performed while replacing the handoff.

Before handing off or closing:

- every in-progress feature has one owner;
- dependencies and status agree with the plan rollup;
- implementation and rollout states are not conflated;
- active feature model/effort recommendations have a specific rationale, follow the current policy, and agree with any rollup; actual execution overrides or host limitations are recorded separately; missing legacy fields are reported without rewriting completed history;
- the index contains only coarse progress and links;
- the handoff contains no historical feature journal;
- migrated legacy items link to their plan;
- no detailed checklist is copied across canonical and rollup files;
- the immediate next action and any required user decision are explicit.
- every advertised next feature satisfies the configured eligibility predicate;
- every active parallel window has an approved, current freeze record and stays within WIP;
- every completed feature satisfies the configured completion gate;
- every rollout transition has its required authorization and evidence.

Prefer deleting stale summaries to adding another corrective paragraph.

## External reconciliation

When configured trackers are canonical or mirrors, `$delivery audit` may compare them with Git records read-only:

- match by `external_refs`, never by title alone;
- compare only fields assigned to a canonical source in `config.yaml`;
- report missing items, stale mirrors, conflicting edits, invalid status mappings, and broken dependency links;
- treat a conflict in a canonical field as a decision, not last-write-wins;
- propose the exact local and external writes required to reconcile.

Apply local corrections within the user's requested scope. External comments, labels, status changes, issue creation, closure, or archival require explicit authorization. If a provider is unavailable, record the pending reconciliation and last observed provider revision instead of guessing.
