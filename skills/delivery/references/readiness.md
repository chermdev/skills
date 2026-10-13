# Readiness review

Used by `$delivery-review` / `$delivery review`, and as the entry check for sequence execution.
Review is read-only; it does not approve, activate, assign, repair trackers, run spikes or start implementation.

Read the repository contract, current handoff, selected plan and relevant feature metadata. Inspect only the code/evidence needed to distinguish existing delivery from proposed work. Preserve canonical field ownership and do not infer completion from routes or migrations alone.

Assess:

- Visible outcome, explicit exclusions and finite acceptance; identify overly broad or horizontal features.
- Existing implementation/evidence and whether proposed work would duplicate it.
- Product decisions, provider/platform feasibility, real dependencies, cycles and stale references.
- Exact ownership readiness, small coherent batches and shared-contract or runtime conflicts.
- Failure/retry, data integrity and exposure/rollback requirements proportional to the changed behavior.
- Test/review scope, recommended settings and actual execution eligibility under the repository contract.

Return a compact verdict per selected feature: **ready**, **needs decisions**, or **needs a spike**. These are review verdicts, not new stored delivery statuses. “Ready” means sufficiently specified; separately state whether approval, assignment, activation or other execution gates still fail. Several kinds of gap may coexist; list the actionable ones without forcing them into one label.

For a decision, state the choice, tradeoff and who must resolve it. Resolve facts through bounded read-only inspection when possible; do not invent pricing, permissions or product behavior. For a spike, specify one question, permitted boundary, expected evidence and a finite stopping condition. Propose it here, execute it only in an authorized preparation/execution scope. Identify uncertainty rather than promising a duration.

Finish with the smallest next action. No full-portfolio audit, fixed reviewer panel or independent agents unless a specific unresolved question and authorization justify them.
