---
name: delivery-execute
description: Coordinate an approved delivery sequence with configured feature owners, model and effort. Check readiness, handle blockers and continue after verified completion.
---

# Delivery Execute

Autocomplete entry point for the shared Delivery workflow, mode `run`.

Load the companion `delivery` skill from the available catalog (including plugin-prefixed names), or `../delivery/SKILL.md` in a source checkout. If unavailable, report the missing dependency and stop this workflow. Follow its shared contract and read `references/run.md` from its root; load other references only as needed.

Execute only approved, eligible scope, honoring the repository task topology and explicitly applied model/effort. Never silently substitute a model.
