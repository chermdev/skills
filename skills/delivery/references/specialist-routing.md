# Specialist routing

Use this reference when planning or executing a feature with material discipline-specific uncertainty. Delivery owns scope, state, ownership, dependencies, checkpoints and rollout. Specialists own decision criteria and evidence within that scope.

## Select by the affected boundary

| Trigger | Relevant capability | Expected contribution |
| --- | --- | --- |
| Module/domain responsibilities change | software-design | Boundaries, invariants, trade-offs and owned contracts |
| Tenant boundary or lifecycle changes | saas-architecture | Isolation/lifecycle matrix and tenant failure cases |
| Persistence semantics or migration changes | database-design | Data constraints, concurrency and safe transition |
| Consumer-facing contract changes | api-design | Inputs/results/errors, compatibility and retry semantics |
| Partial failure across processes | distributed-systems | Protocol guarantees, crash windows and reconciliation |
| Behavior needs a verification strategy | software-testing | Risk-to-check mapping and observed evidence |
| Trust boundary changes | security-review | Scoped findings and negative checks |
| Unexpected behavior needs diagnosis | debugging | Reproduction, supported cause and bounded experiments |
| Structure changes while behavior stays stable | refactoring | Preserved observables and safe transformations |
| Candidate reaches configured review | code-review | Candidate-specific findings and verified closure |
| Material live exposure is being assessed | production-readiness | Readiness verdict, recovery and rollout evidence |
| Agent instructions themselves change | skill-authoring | Discriminating triggers and behavioral evaluations |

These names are examples of locally supplied capabilities, not hard dependencies. Discover installed skills by their actual descriptions, allowing host namespaces. Do not assume sibling filesystem paths. Do not install a collection as a side effect of routing.

## Composition contract

1. Identify the unresolved decision or verification boundary. Load the smallest matching capability, not every row of the table.
2. Supply the approved scope, relevant raw artifacts, local conventions, affected contracts and requested output. A specialist does not receive authority to expand scope or exposure.
3. Record its contribution in the canonical feature: capability, purpose, decision/findings, evidence, candidate identity and remaining limitation. Link bulky evidence.
4. Reconcile conflicts against the project's constraints and user intent. Principles set requirements; technology capabilities implement them and may surface constraints that require revisiting a choice.
5. Revisit only contributions invalidated by a material change. Do not repeat the same review at every phase when its inputs remain unchanged.

A missing skill is not itself a blocker. Apply the relevant criteria directly and disclose the fallback. Missing expertise/evidence needed to satisfy a configured gate can be a blocker; name that specific gap. Never invent a successful specialist invocation.

## Proportionality and permissions

A text or spacing correction does not require SaaS architecture, database review, security audit or a new plan merely because the product is a SaaS. A tenant authorization change needs isolation evidence even if its diff is small.

Skills guide reasoning; they do not enforce access control, branch protection, migration restrictions or environment separation. Record requirements for those mechanisms where the project needs them. They also do not bypass human review when required.

Orchestration does not imply subagent dispatch. Honor user/host delegation policy and the repository's ownership, WIP and contract-freeze rules. Self-review, independent agent review and human approval remain distinct.

## Existing records

Keep approved and completed history intact. For an active feature missing newer planning sections, add only the relevant scope/contract/evidence details during normal continuation. Missing optional headings do not invalidate prior approval or force setup/migration.
