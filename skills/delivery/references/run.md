# Coordinate an approved sequence

Used by `$delivery-execute` / `$delivery run`. The invoking task coordinates the sequence. [Execution](execution.md) is the single source for feature eligibility, dispatch, model/effort, task topology, ownership, verification and event-driven coordination. Load it before dispatch.

## Entry and preparation

Read the contract and handoff. Apply [readiness](readiness.md) to the selected/next plan. Preserve existing owners and unfinished work. If no plan is specified, use the agreed repository order; ask only when competing priorities remain unresolved.

For gaps, use [planning](planning.md) within the authorized preparation scope. Readiness defines the decision and spike contract. Preparation may update canonical plans and conduct permitted bounded investigation; it does not approve new scope. Wait for required user decisions before dependent work.

## Continue after a result

Use execution's event-driven coordination and acceptance gates. A completion notification is a candidate for verification, not automatic acceptance. After accepting and integrating authorized changes, update compact rollups and evaluate the next eligible feature without requiring the user to repeat the command. Schedule serially unless execution's parallel gates are satisfied.

Continue until the authorized sequence finishes, the user stops it, or no eligible work remains. On a blocker, preserve the candidate and report the exact constraint and next action; continue independent authorized work if any. Do not invent background continuation when the host cannot provide it, activate unapproved scope, waive acceptance or authorize rollout merely to keep moving.
