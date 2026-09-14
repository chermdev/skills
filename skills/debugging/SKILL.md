---
name: debugging
description: Diagnose reproducible or intermittent software failures, regressions, flaky checks, and incorrect state by tracing evidence and testing hypotheses. A diagnosis request remains read-only except for authorized diagnostic experiments.
---

# Debugging

Locate the failing boundary before accumulating fixes. Preserve the user's distinction between diagnosis and implementation.

## Investigation loop

1. State expected versus observed behavior, affected version/environment, frequency and the smallest known reproduction. Read complete relevant errors and recent changes.
2. Trace the operation across the relevant boundaries. Compare one failing and one working execution when possible; identify the first divergence.
3. List a small set of evidence-backed hypotheses. For each, name a discriminating observation or experiment and the result that would refute it.
4. Run the smallest permitted experiment. Change one causal variable when feasible, and retain observations even when the hypothesis fails.
5. Update the explanation from the result. If uncertainty remains, state it and choose the next useful observation instead of asserting a root cause.
6. When a fix is requested, correct the established cause with a bounded change, then verify the original reproduction and relevant regressions.

## Difficult cases

- Intermittent behavior may require correlation IDs, event order, timing and concurrency traces. Avoid arbitrary sleeps as the final fix when a completion signal exists.
- A retry that hides a failure is not proof of a fix. Record initial failure, retry outcomes and the actual synchronization or state defect.
- Distinguish incorrect input, propagation failures, authorization failures, stale cache, environment mismatch and external-service uncertainty.
- Repeated failed hypotheses suggest missing evidence or a wrong model. Reassess before trying another speculative change; use a task-specific stopping condition rather than a universal attempt count.
- During an incident, an authorized reversible mitigation can precede a complete diagnosis. Record that it is mitigation, its risk, rollback and the remaining investigation.

## Evidence discipline

Inspect secret presence or redacted metadata without dumping environment variables, tokens or sensitive payloads. Keep diagnostic logging bounded and remove temporary instrumentation when its purpose ends, if modification is authorized.

If reproduction is unavailable, report the strongest supported inference plus what would confirm it. Do not blame a library, architecture or user without evidence. Consult current official sources when investigating version-specific behavior.

## Output and scope

Return observations, supported cause or remaining hypotheses, the smallest corrective action, and verification status. For diagnosis-only requests, explain the proposed correction without applying it. For an authorized fix, implement and verify within scope.

Read [sources](references/sources.md) for the adapted investigation method. Use existing issue/feature evidence records if present; a simple bug does not need a new multi-session plan.

