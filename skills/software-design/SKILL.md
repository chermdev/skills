---
name: software-design
description: Design or assess module boundaries, domain models, abstractions, and dependency direction when a feature changes responsibilities or exposes coupling. Use for architecture decisions and complexity reduction; routine edits do not require an architecture exercise.
---

# Software Design

Ground the design in one concrete use case and the code that already implements its rules. Preserve the project's language and paradigm; classes, services, layers, and interfaces are options, not requirements.

## Decision procedure

1. Identify the behavior, business invariants, expected changes, and ownership. Separate measured constraints from estimates and unknown product decisions.
2. Trace where those rules live today. Name any rule duplicated across modules, hidden dependency, or interface that requires callers to understand its internals.
3. Compare the smallest viable alternatives. Prefer keeping a decision local over introducing a universal abstraction. Similar-looking code is not necessarily the same knowledge.
4. Place boundaries around actual differences in meaning, ownership, failure, or change rate. Keep terminology consistent inside a domain; allow the same term to differ across contexts.
5. Make dependency direction protect the important rules. Isolate external concerns when that improves substitution, testing, or ownership; do not require a wrapper for every dependency.
6. Demonstrate one representative path through the proposed boundaries. Include the failure path and how the invariant is enforced. Check whether the new interfaces reduce what callers need to know.
7. Record expensive-to-reverse choices with alternatives, trade-offs, and a revisit trigger. Keep cheap choices local to the task.

## Review criteria

- A module should hide a coherent decision, not merely forward every call.
- Splitting into smaller files is useful only when responsibilities become easier to understand.
- Shared domain vocabulary does not justify shared mutable ownership across independent contexts.
- Default to the simplest deployment topology compatible with known requirements. Split services for demonstrated ownership, scaling, or failure-isolation needs.
- Do not impose object-oriented domain entities on a functional design or rewrite the existing architecture for an unrelated feature.
- Technology constraints can invalidate an option. Revisit the affected decision explicitly rather than pretending the implementation is interchangeable.

## Output and boundaries

Return a concise decision record: affected responsibility, evidence, options, choice, owned contracts, and verification. Link the existing architecture record when there is one; do not create a second project tracker.

For changes to data consistency, service protocols, or tenancy, use an available specialist only for that uncertainty. Continue with explicit assumptions if it is absent; this skill has no mandatory sibling dependencies.

For consolidation and source context, read [sources](references/sources.md). For behavior-preserving implementation, use a refactoring capability when available.

