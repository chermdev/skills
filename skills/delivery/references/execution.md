# Execution

Read the current handoff first. Resume work already owned by this task; do not reset its status,
count its WIP slot twice, or take another writer's boundary. Resolve a recorded blocker before
restoring the prior execution state. Read current facts rather than reconstructing old conversations.

## Coordinator

- Check the manifest, plan rollup and selected feature for approval, plan activation, reconciled
  priority, complete dependencies, ownership and WIP. Open horizon/provider records only when those
  facts are missing or stale. Report the first actionable failed gate; selection does not grant approval.
- For parallel work, require the configured contract freeze, disjoint physical ownership, safe merge
  order and independent QA/runtime access. A missing freeze means serial execution, not a new blocker
  for otherwise eligible serial work. Honor an explicit shared-checkout/device override.
- Before dispatch or resumption, MUST satisfy the [execution settings gate](model-selection.md#apply-at-execution): resolve both model and effort, pass explicit supported controls, and record the applied settings or a concrete unresolved constraint. A note saying "inherited" does not satisfy this gate.
- Dispatch a compact assignment: outcome, owned boundary, feature path, necessary contracts,
  acceptance states, execution settings and runtime restrictions. Preserve one visible task per feature
  when requested; resume its existing task for fixes. Use native completion/blocker events.
- Verify the returned commit, acceptance evidence and limitations. Reopen only a disputed claim or
  missing requirement; do not repeat the owner's entire discovery and QA. Update minimal rollups.

## Feature owner

1. Read the canonical feature and relevant contract sections; use already loaded instructions.
   Confirm the coordinator's eligibility facts and current ownership. Do not reread the portfolio.
2. Before writes, record `in_progress`, one owner, base commit, branch/worktree, physical boundary,
   WIP and rollout. Confirm that actual model/effort satisfy the coordinator's
   [execution settings gate](model-selection.md#apply-at-execution). Do not start implementation
   under an unresolved mismatch; preserve prior work while the coordinator resolves it.
3. Inspect integration points and define a finite acceptance matrix. UI work identifies the affected
   journey and required visual/interaction states; persistence/security work identifies actual boundary
   and failure cases. Separate an unrelated discovered feature instead of silently expanding scope.
4. Implement the smallest complete outcome. Batch independent reads and checks; return targeted
   excerpts and failure summaries. Keep full logs and captures in artifacts. Preserve unrelated work.
5. Run the repository's required checks for the changed behavior. Reuse the existing runtime. Prepare
   short UI action sequences and inspect meaningful transitions, final states and failures; do not
   capture/dump the entire interface after every action. Respect an explicit tool preference.
6. Obtain the configured review for this risk. Reviewers get a fixed diff/commit, the invariant to
   inspect and existing evidence. They remain read-only unless assigned a fix and do not recursively
   delegate. Routine localized changes may use owner verification where the local policy permits;
   substantial features retain independent QA; critical changes retain domain/architecture and QA.
7. Fix accepted findings and recheck the affected invariant and changed diff. Broaden tests/review only
   if the fix changes broader behavior, invalidates evidence or exposes a new risk. Do not rerun an
   unchanged full suite merely because a new reviewer joined.
8. Record a concise verdict, commands/results with source revision, inspected evidence and limitations.
   Move `in_review -> completed` only when every applicable gate is satisfied and blocking findings
   are resolved. Keep rollout separate and normally `gated`; completion does not authorize deployment.
9. Report completion or a concrete blocker, release ownership/runtime and update the short handoff.
   Bulky logs and historical attempts stay in linked evidence, not in the executable feature contract.

If attempts repeat without a changed implementation, new evidence or a narrower hypothesis, reassess
the boundary and approach. A checkpoint is a reason to change strategy, not a blind token cap or an
automatic request for user input. Record a newly discovered dependency before continuing dependent work.

Do not deploy, enable tenants, mutate production or update external trackers without authorization.
Do not amend a reviewed implementation solely to record its SHA; use a small coordination follow-up
when the repository requires immutable commit references. Maintain handoffs at ownership changes,
meaningful pauses, blockers and completion, rather than rewriting them after every tool call.
