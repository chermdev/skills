# Planning

Use this branch to groom imported intake or, when exploration is already sufficient, propose an implementation plan.

## Intake from configured trackers

If the user asks what to plan next, or names Linear, Plane, GitHub, or another configured provider:

1. Read candidate initiatives/features and their dependencies without mutating them.
2. Exclude completed, canceled, duplicate, already-indexed, and dependency-blocked items unless their state appears stale.
3. Compare the remaining candidates with repository code, local plans, durable decisions, and the current handoff.
4. Rank a small candidate set by prerequisite readiness, work unblocked, user/operator value, risk reduction, and decision uncertainty. State which facts came from the tracker and which are repository inferences.
5. Ask the user to select when the choice changes product priority. Once selected, continue the normal planning flow and preserve the external reference.

Do not treat tracker priority alone as implementation readiness. A high-priority item with unresolved behavior first becomes a decision, research, or prototype step.

## Groom before slicing

For an initiative with `planning_state: intake` or `needs_grooming`:

1. Separate provider facts, repository facts, inferences, and unresolved product intent.
2. Inspect the affected code paths, durable domain rules, architecture decisions, prior plans, and relevant history.
3. Use bounded read-only agents for independent repository questions when delegation is available and the evidence will materially improve the plan. Keep one coordinator responsible for the canonical records.
4. Use an available specialized skill when its described capability matches the uncertainty—for example domain modeling, architecture analysis, research, grilling, or a throwaway prototype. Do not hard-code a dependency on a particular third-party skill collection.
5. Resolve discoverable facts before asking the user. Batch only the remaining questions whose answers materially change product behavior, scope, rollout, or dependencies; include the observed evidence and a recommended interpretation.

Do not manufacture acceptance criteria or feature boundaries from a vague tracker title. Keep the initiative `draft`; use `planning_state: needs_grooming` while material uncertainty remains. Set `planning_state: ready_for_approval` only when the outcome, decisions, vertical sequence, dependencies, and verification expectations are reviewable.

## Shape vertical features

1. Search the plan index, initiative folders, legacy backlog, technical contracts, and durable decisions for overlap. Extend an overlapping initiative instead of duplicating it.
2. Capture unresolved product or architecture decisions before implementation tasks. Keep domain rules in their durable contract and link them from the plan.
3. Define one initiative outcome and rollout boundary.
4. Slice the outcome into the smallest independently reviewable vertical deliveries. Each feature includes its necessary domain/server/data/UI work and produces a visible or operable result.
5. Declare `depends_on`, `parallelizable`, safe rollout assumptions, and the critical path. Parallelizable means either merge order is safe and write ownership does not overlap.
6. Give every feature measurable completion criteria, appropriate automated checks, user-facing QA when applicable, review gates, and an ownership strategy.
7. Present the proposed feature sequence and unresolved decisions to the user. Keep records `status: draft` and `planning_state: ready_for_approval` until the user approves implementation. On approval, set the initiative and approved features to `status: approved` and `planning_state: ready`.

Use `assets/plan-template.md` and `assets/feature-template.md` when creating a new contract. Adapt validation and rollout sections to the stack; do not impose browser or database checks on work that does not have those surfaces.
