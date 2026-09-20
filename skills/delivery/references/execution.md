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

## Manager and implementation agents

The coordinator acts as manager; the assigned feature owner is the implementation agent. Use this
split when the user/repository authorizes delegation, retaining its selected task topology. It does
not require extra agents for a bounded edit or authorize a new visible task for every batch.

| Role | Responsibility |
| --- | --- |
| Manager | Select ready work, group related batches, resolve model/effort, assign one writer and runtime ownership, clarify acceptance, track dependencies/blockers, review delivered evidence, integrate accepted changes and update canonical rollups. |
| Implementation agent | Read its bounded assignment, implement within ownership, run required scoped checks, record bugs, fix bounded in-scope findings and deliver a coherent candidate with evidence and remaining limitations. |
| Reviewer, only when required | Read the fixed candidate and existing evidence, verify the assigned risk independently and report actionable findings. No code writes or recursive delegation by default. |

The manager MUST avoid duplicating the owner's implementation, exploration or passing tests. Review
what changed against acceptance, inspect relevant evidence and request only missing evidence or
specific corrections. Keep fixes with the same owner. The manager may run an integration check when
combining changes introduces a concrete risk; do not repeat the full verification merely on handoff.

### Evidence before direction and acceptance

Before claiming a cause or assigning a specific correction, inspect evidence that supports it.
A user's symptom is sufficient to investigate, not proof of a root cause. Separate observed facts
from hypotheses; when evidence is missing, assign a bounded diagnosis rather than a speculative
fix. Recheck the affected target when the user corrects which screen or component they meant.
For a visual defect, inspect component parameters, inherited styles and wrappers before
expanding the fix into a dependency upgrade or architectural replacement. Preserve the
requested integration; a similar appearance does not establish equivalent behavior.

For visual delivery, the manager MUST inspect the actual rendered candidate against the approved
reference and relevant sibling screens before accepting it. Passing tests and an owner's summary
do not establish visual consistency. Reuse existing captures when their source and configuration
still apply; otherwise request only the missing affected view. Compare the shared treatment as well
as the presence of elements (for example, gradient falloff/intensity as well as hue). This is a
focused acceptance check, not permission for a new all-screen or accessibility audit.

### Coherent candidate handoffs

The owner finishes the available local review and groups related known corrections before requesting
staging or integration. Do not hand off every one-line edit separately. Distinguish staging for a
required shared-runtime check from accepting/integrating a completed candidate. When the owner
cannot run that check locally, a staging request is justified; group the findings from that bounded
journey into the next candidate and recheck only the affected claims. Do not require a second server,
full test rerun or fresh reviewer merely to reduce handoffs, and do not delay a real blocker report
while polishing unrelated details.

### Event-driven coordination

- Dispatch one self-contained assignment, then let the agent work. Use native completion,
  needs-input and blocker notifications to resume coordination. When the host requires waiting,
  use its bounded event-wait API and latest cursor; do not poll transcript/status on a timer.
- While waiting, perform useful independent manager work. If none remains, wait or yield using
  the host's supported continuation mechanism. Do not create heartbeat automations, extra workers
  or recurring status messages merely to monitor an already running assignment.
- A notification is a reason to inspect the new result, not to replay the task history. Read the
  compact completion summary, candidate revision, checks and blockers; open detail only to resolve
  a specific gap. Do not repeatedly acknowledge unchanged progress or narrate unchanged waits.
- Send a message when it changes the assignment: new user constraints, a dependency becoming ready,
  a concrete blocker, a review finding or an ownership/runtime handoff. Do not send routine
  "are you done?", status requests or reminders of instructions already received.
- Owners report completion or an actionable blocker through the native event mechanism. If the host
  lacks one, agree on one compact completion/blocker handoff; only inspect status for a user request,
  suspected delivery failure or recovery after interruption. Do not combine event waits with a
  second manual polling loop.
- User-facing updates remain concise and meaningful: an accepted result, material risk, scope
  decision or required input. Follow host communication requirements without turning internal
  coordination into a running transcript.

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

## Discovered bugs and bounded investigation

Record a discovered bug before leaving it behind using the mandatory [bug record structure](bugs.md)
and the repository's configured bug directory/template, with a stable reference. Include observed versus expected behavior, reproduction
or evidence/revision, affected boundary, whether it blocks a named acceptance criterion, and the
next action/owner (or explicitly unassigned). Distinguish observations from an unverified cause;
link existing reports instead of duplicating them. External tracker writes still need authorization.

- **Blocking, with an established local cause and bounded remedy:** fix within the existing owner
  boundary when authorized, then recheck the failed criterion and affected consumers. "Quick" means
  a concrete fix with a clear check, not a guess that an investigation will be short.
- **Blocking, requiring investigation or wider scope:** preserve the candidate and create a linked
  future investigation record with the open question, evidence already gathered and a stop/exit
  condition. Mark the affected task blocked under the repository's workflow. Continue independent
  accepted batches, but do not claim the blocked feature complete or silently weaken acceptance.
- **Nonblocking or pre-existing outside scope:** record a follow-up and continue the agreed outcome.
  Do not turn a visual change into a general accessibility, theme or financial-system audit. A defect
  introduced by the current change must be resolved or the offending change removed; do not relabel
  it as unrelated debt merely to finish.

A functional fallback is not automatically acceptance of the requested behavior. If direct buttons
work but the approved single menu does not, record the working delivery separately from that unmet
criterion. Preserve the remaining requirement and its linked bug; keep the affected feature blocked
or partially accepted under the repository's existing states. Only an explicit authorized scope
change can remove the criterion. A deferred nonblocking bug need not prevent completion of the
agreed outcome, but an unmet agreed criterion still does. Do not invent a new status or silently
mark the whole plan complete because the fallback was integrated.

After an attempt that adds no evidence, narrow the question or change the method before retrying.
When the next step is open-ended research rather than a bounded correction, stop expanding the batch
and use the triage above. Reuse passing evidence for unchanged code/environment; escalate checks or
review only for a concrete affected invariant. Keep the handoff to completed batches, the current
next action and links to deferred findings, not a transcript of the investigation.

If attempts repeat without a changed implementation, new evidence or a narrower hypothesis, reassess
the boundary and approach. A checkpoint is a reason to change strategy, not a blind token cap or an
automatic request for user input. Record a newly discovered dependency before continuing dependent work.

Do not deploy, enable tenants, mutate production or update external trackers without authorization.
Do not amend a reviewed implementation solely to record its SHA; use a small coordination follow-up
when the repository requires immutable commit references. Maintain handoffs at ownership changes,
meaningful pauses, blockers and completion, rather than rewriting them after every tool call.
