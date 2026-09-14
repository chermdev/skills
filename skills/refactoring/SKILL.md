---
name: refactoring
description: Plan or perform behavior-preserving restructuring of existing code when duplication, coupling or complexity obstructs a concrete change. Use for refactoring requests; separate new behavior and migrations from structural cleanup.
---

# Refactoring

State the behavior that must remain stable before choosing a transformation. Refactoring has a specific maintenance goal, not a target file count or design score.

## Procedure

1. Read the touched code, callers, existing tests and compatibility surface. Name the actual obstacle: duplicated rule, leaked representation, mixed responsibility, hidden state, or awkward dependency.
2. Define preserved observables: return values, errors, ordering, side effects, persistence, public names/formats, timing/resource bounds where contractual.
3. Establish a baseline with existing checks. Where behavior is undocumented, add targeted characterization around the important observable; do not enshrine an unsafe defect as desired policy.
4. Choose the smallest transformation that addresses the obstacle. Extract, inline, move, rename, split or consolidate only where it improves the identified responsibility.
5. Transform in independently understandable steps. Preserve user changes, public contracts and unrelated behavior.
6. Run affected checks and inspect the diff for unintended semantic changes. Stop when the original maintenance obstacle is resolved.

## Decision rules

- Consolidate shared business knowledge, not merely similar syntax.
- Avoid combining behavior fixes with structural changes unless necessary; distinguish and verify them separately when both are authorized.
- A new abstraction needs a real caller or variation that justifies its interface.
- Preserve external consumers through a compatibility bridge when renaming public APIs.
- Data movement and serialized-format changes need migration planning; a passing unit suite does not make them a pure refactor.
- Do not replace a familiar local pattern solely to match a book or framework preference.
- Test doubles that assert every internal call may need adjustment, but retain assertions on externally meaningful effects.

## Output and verification

Return the maintenance problem, transformation, preserved contract and observed checks. If an unexpected behavior change appears, explain it and restore the intended behavior through a scoped edit; never overwrite unrelated work.

Use a design capability only if choosing the boundary remains uncertain. Read [sources](references/sources.md) for the transformation and complexity criteria.

