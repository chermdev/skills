# Planning

Use this branch to groom imported intake or, when exploration is already sufficient, shape an outcome plan and its feature DAG.

## Intake from configured trackers

If the user asks what to plan next, or names Linear, Plane, GitHub, or another configured provider:

1. Read candidate horizons, plans, features, and dependencies without mutating them.
2. Exclude completed, canceled, duplicate, already-indexed, and dependency-blocked items unless their state appears stale.
3. Compare the remaining candidates with repository code, local plans, durable decisions, and the current handoff.
4. Rank a small candidate set by prerequisite readiness, work unblocked, user/operator value, risk reduction, and decision uncertainty. State which facts came from the tracker and which are repository inferences.
5. Ask the user to select when the choice changes product priority. Once selected, continue the normal planning flow and preserve typed external references. Provider priority remains separate from implementation readiness.

Do not treat tracker priority alone as implementation readiness. A high-priority item with unresolved behavior first becomes a decision, research, or prototype step.

## Groom before slicing

For a plan with `planning_state: intake` or `needs_grooming`:

1. Separate provider facts, repository facts, inferences, and unresolved product intent.
2. Inspect the affected code paths, durable domain rules, architecture decisions, prior plans, and relevant history.
3. Answer bounded discovery locally by default. Delegate only an independent question whose evidence materially improves the plan and when authorized; do not launch a fixed panel of specialists. Keep one coordinator responsible for canonical records.
4. Use an available specialized skill when its described capability matches the uncertainty—for example domain modeling, architecture analysis, research, grilling, or a throwaway prototype. Do not hard-code a dependency on a particular third-party skill collection.
5. Resolve discoverable facts before asking the user. Batch only the remaining questions whose answers materially change product behavior, scope, rollout, or dependencies; include the observed evidence and a recommended interpretation.

Do not manufacture acceptance criteria or feature boundaries from a vague tracker title. Keep the plan `proposed`; use `planning_state: needs_grooming` while material uncertainty remains. Set `planning_state: ready_for_approval` only when the outcome, decisions, vertical sequence, dependencies, ownership strategy, and verification expectations are reviewable.

## Shape vertical features

1. Search the plan index, plan folders, legacy backlog, technical contracts, and durable decisions for overlap. Extend an overlapping plan instead of duplicating it.
2. Capture unresolved product or architecture decisions before implementation tasks. Keep domain rules in their durable contract and link them from the plan.
3. Define one bounded plan outcome and rollout boundary. Keep broad strategic themes as horizons; do not turn them into permanently open delivery containers.
4. Slice the outcome into the smallest independently reviewable vertical deliveries. Each feature includes its necessary domain/server/data/UI work and produces a visible or operable result.
5. Declare `depends_on`, `parallelizable_with`, safe rollout assumptions, and the critical path. The relation is only a candidate. Before parallel execution, require an approved freeze record containing exact shared contracts, non-overlapping file/function ownership, merge order, reviewers, and independently verifiable QA. WIP limits still apply. If the repository has no WIP policy, default to two active features per plan: one critical-path feature plus one genuinely independent feature, with review still counting as WIP. Do not maximize branch count from the graph alone. When a required freeze is missing or superseded, close the parallel window and schedule the affected candidates serially in dependency and priority order; do not leave otherwise executable work paused indefinitely.
6. Give every feature finite, measurable acceptance states, appropriate automated checks, user-facing QA when applicable, risk-based review gates, and one write owner. State the evidence needed to finish before dispatch; distinguish in-scope defects from independent product work.
7. Select `recommended_model`, `recommended_reasoning_effort`, and `reasoning_rationale` for each feature using [model and effort selection](model-selection.md). Base the recommendation on the actual boundary, uncertainty and failure impact, not the feature title or size alone.
8. Present the proposed feature sequence and unresolved decisions to the user. Keep the plan `status: proposed` and features `status: not_started`; planning remains `ready_for_approval` until the user approves scope. Approval changes `planning_state` to `approved` without pretending execution started.
9. Activate a plan only after portfolio priority is reconciled, its planning is approved, and a plan owner is assigned. Then make only the first dependency-ready feature eligible by approving its planning and assigning its write owner/boundary. Do not bulk-promote every downstream feature.

## Short tasks and coherent batches

Keep the feature as a vertical outcome; divide its implementation into short, independently
checkable task batches, not separate horizontal features or a new agent for each step. Each batch
states its result, owned component/function boundary, dependencies and finishing check. Prefer a
batch that fits one focused session with only its feature and relevant contracts in context; do
not promise a fixed duration or token budget without evidence.

Before dispatch, compare adjacent batches for shared files, components, consumers and test setup.
Combine closely related changes when one owner can implement and verify them together. For example,
update a shared selector and its already-approved consumers in one coherent pass instead of sending
successive agents to restyle the same primitive. Keep separate domain outcomes and risky changes
separate; do not pull future unapproved work into a batch. Honor the repository's task topology and
one-writer rule; an implementation checklist does not authorize additional visible tasks.

Order quick wins by user value and dependency readiness, not just ease. If a batch requires open-ended
investigation, separate that investigation from the known implementation and state the question and
exit condition. Reuse the same owner for related fixes. Prepare one coherent reviewable candidate per
batch and reuse its checks; avoid coordination commits, handoffs and full reviews for every small edit.

Review recommendations after grooming or material scope changes without changing approval or rollout state. Keep frontmatter canonical; plan tables may summarize it. Follow the repository's documentation language, including frontmatter prose and rationales.

Use `assets/plan-template.md` and `assets/feature-template.md` when creating a new contract. Adapt validation and rollout sections to the stack; do not impose browser or database checks on work that does not have those surfaces.
