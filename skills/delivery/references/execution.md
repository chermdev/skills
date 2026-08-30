# Execution

1. Read the initiative, canonical feature, linked contracts, and current handoff. Confirm the feature has `planning_state: ready`, is approved or already in progress, its dependencies are satisfied, and no other writer owns its scope.
2. Record the owner, base commit, branch/worktree, owned boundary, and rollout state before edits when the local contract requires it. Replace the runtime handoff so it points to this active delivery.
3. Inspect integration points and unresolved decisions. Stop for a decision only when a reasonable assumption would materially change behavior or scope.
4. Implement the smallest complete vertical outcome. Keep unrelated user changes untouched.
5. Verify in proportion to risk using the repository's commands and the feature's definition of done. User-facing changes require outside-in validation of owned states; data/security changes require real boundary and failure-path evidence.
6. Obtain independent review when required. The writer fixes accepted findings; the reviewer verifies blocking fixes. Do not complete with unresolved blocking findings.
7. Record a concise verdict, limitations, commands, and commit reference in the feature. Move bulky evidence to a linked record.
8. Mark implementation complete only when every completion criterion is satisfied. Set rollout independently—usually `ready_for_decision` when exposure still needs authorization.
9. Update minimal rollups and replace the short handoff with the next feature, blocker, or required decision. If the workflow records immutable SHAs after commit, use a small coordination-only follow-up rather than amending the reviewed implementation commit.

Maintain the handoff automatically at ownership changes, meaningful pauses, blockers, and completion. Progress detail belongs in the feature; the handoff is only the restart checkpoint.

Do not deploy, enable tenants, mutate production, or update external trackers unless the request and repository rules authorize those actions.
