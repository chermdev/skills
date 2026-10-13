---
name: delivery-review
description: Review delivery readiness without changing plans or starting implementation. Identify unresolved decisions, missing evidence and bounded spikes.
---

# Delivery Review

Autocomplete entry point for the shared Delivery workflow, mode `review`.

Load the companion `delivery` skill from the available catalog (including plugin-prefixed names), or `../delivery/SKILL.md` in a source checkout. If unavailable, report the missing dependency and stop this workflow. Follow its shared contract and read `references/readiness.md` from its root; load other references only as needed.

Read-only: do not edit plans, run spikes, dispatch implementation or change trackers.
