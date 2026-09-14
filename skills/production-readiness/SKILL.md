---
name: production-readiness
description: Assess operational readiness for a release, rollout, migration, or material change to live behavior. Evaluate recovery, observability, capacity and compatibility proportionately; readiness assessment does not deploy or authorize exposure.
---

# Production Readiness

Give a release decision grounded in the candidate change, target environment, and evidence. Keep implementation completion, operational readiness, authorization and verified exposure distinct.

## Establish scope

Read the intended rollout, relevant SLOs or acceptance thresholds, affected users/tenants, dependencies, data changes and recovery responsibilities. Use existing release policy; do not invent mandatory enterprise controls for a small low-risk change.

## Assess relevant surfaces

| Surface | Evidence to request or inspect |
| --- | --- |
| Behavior | Acceptance checks, regressions, owned failure paths and configured reviews |
| Security | Authorization/isolation changes assessed; blocking findings resolved |
| Dependencies | Bounded deadlines, retry budgets, overload behavior and safe degradation |
| Data | Old/new compatibility, migration order, backfill safety and recovery evidence |
| Capacity | Representative workload, resource budgets, tenant skew and measured bottlenecks |
| Observability | User-impact signals, useful correlation, redaction, actionable alerts and ownership |
| Rollout | Exposure mechanism, candidate identity, health thresholds and rollback/stop criteria |
| Operations | Runbook or concise recovery steps, responsible operator and support implications |

Inspect the applicable surfaces only. Feature flags, canaries, breakers, and multi-region designs are options justified by failure impact, not universal launch requirements.

## Failure and recovery

- A timeout is an uncertain outcome if a dependency may have committed. Check idempotency or reconciliation before retries.
- Bound retries by attempts and total deadline; avoid multiplying retry budgets across layers.
- Check backpressure and bounded work queues/pools where overload is plausible.
- Separate liveness from readiness. A dependency outage should not cause a restart storm from an over-broad liveness check.
- A code rollback cannot reverse every data migration or external side effect. State the viable recovery path, loss window, expected duration and owner.
- A backup timestamp alone does not demonstrate restorability. Request restore/recovery evidence when material data risk warrants it.
- Define a stop condition in observable terms and name who may authorize rollback or further exposure.

## Verdict and handoff

Return one of: ready for the stated rollout, blocked by named findings, or insufficient evidence. List each material missing check and its consequence; distinguish a pending external authorization from a technical failure.

Record evidence with the candidate revision/environment. A previous build's successful run does not prove a changed candidate. Reuse valid evidence whose inputs remain unchanged and rerun checks affected by subsequent changes.

Readiness can complete while rollout remains gated. Do not deploy, enable tenants, merge, or run destructive recovery simply because this assessment is green. Use the existing feature/release record, not a new parallel tracker.

Read [sources](references/sources.md) for adapted resilience criteria.

