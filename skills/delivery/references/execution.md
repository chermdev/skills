# Execution

First check the handoff for work already owned by the current execution. Resume an `in_progress`
feature, or continue the configured review for an `in_review` feature, after confirming approval,
plan activation, dependencies, ownership, and any applicable parallel gates remain valid. Its
existing WIP slot counts once. Do not apply the new-work `not_started` predicate to a continuation,
reset its status, or claim another owner's work without an authorized ownership transfer. A
`blocked` feature resumes only after its blocker is resolved and its recorded prior state is restored.

For new work, use the following sequence; a validated continuation resumes at the relevant step
without reclaiming its WIP slot:

1. Read the horizon, plan, canonical feature, linked contracts, index, and current handoff. Apply the repository's configured `$delivery next` predicate. By default, the containing plan must be `active / approved` with priority reconciled; the feature must be `not_started / approved`, have all dependencies `completed`, an assigned owner and non-empty physical boundary, satisfy WIP, and meet every applicable parallel requirement. If any condition fails, report the first actionable gate instead of silently promoting state.
2. When parallel execution is proposed, require an `approved` contract-freeze record that covers every feature in the window, exact shared schemas/signatures/DDL, ownership by file and function, merge order, independent QA, and current approvals. Treat a missing or superseded freeze as serial execution.
3. Claim the feature before writes: move it to `in_progress` and record owner, base commit, branch/worktree, owned boundary, actual WIP slot, and rollout state. Replace the runtime handoff so it points to this active delivery.
4. Resolve the feature's model/effort recommendation against current user instructions and host capabilities using [model and effort selection](model-selection.md). Record the actual setting and any override or limitation. Selecting a model does not itself create a task or authorize delegation.
5. Inspect integration points and unresolved decisions. Stop for a decision only when a reasonable assumption would materially change behavior or scope.
6. Implement the smallest complete vertical outcome. Keep unrelated user changes untouched.
7. Verify in proportion to risk using the repository's commands and the feature's definition of done. User-facing changes require outside-in validation of owned states; data/security changes require real boundary and failure-path evidence.
8. Obtain every configured review stage. The writer fixes accepted findings; the independent final reviewer verifies blocking fixes. Do not complete with unresolved configured blocking severities.
9. Record a concise verdict, limitations, commands, and commit reference in the feature. Move bulky evidence to a linked record.
10. Move `in_review -> completed` only when the configured completion gate is true. Set rollout independently—normally remain `gated` until explicit authorization, then follow guarded `authorized -> released` transitions.
11. Update minimal rollups and replace the short handoff with the next eligible feature, blocker, or required decision. If the workflow records immutable SHAs after commit, use a small coordination-only follow-up rather than amending the reviewed implementation commit.

Maintain the handoff automatically at ownership changes, meaningful pauses, blockers, and completion. Progress detail belongs in the feature; the handoff is only the restart checkpoint.

Do not deploy, enable tenants, mutate production, or update external trackers unless the request and repository rules authorize those actions.
