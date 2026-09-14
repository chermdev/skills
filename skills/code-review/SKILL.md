---
name: code-review
description: Review a proposed code or configuration change against requirements, correctness, maintainability and verification. Use for PR review or a configured completion review; do not turn review requests into unsolicited rewrites.
---

# Code Review

Review the actual candidate and its surrounding integration paths. A review is an evidence-based assessment, not a count of stylistic suggestions.

## Establish the review contract

1. Identify the base and candidate revisions or exact local diff, scope, requirements, acceptance criteria and configured severity policy.
2. Read changed files and relevant callers, tests, schemas and deployment constraints. Explain any missing context that prevents a conclusion.
3. Assess requirements first: does the result deliver the intended behavior without adding unauthorized scope?
4. Assess implementation: boundary failures, state transitions, concurrency, resource handling, authorization and compatibility where affected.
5. Assess verification: do tests exercise the failure conditions and real boundary, or merely duplicate the implementation's assumptions?
6. Evaluate maintainability through concrete future-change cost. Respect existing conventions; do not block on personal style absent a real correctness or maintenance consequence.

## Findings

For each supported finding include location, severity/impact, triggering condition, evidence, recommended correction and a way to verify it. Mark uncertain claims as questions with the evidence needed to decide them.

Do not manufacture findings to fill a quota. Keep non-blocking suggestions distinct from defects. Use an available specialist for a material domain/security/data uncertainty without launching every review discipline.

## Receiving and closing reviews

- Reproduce or trace a finding before editing. Accept it, resolve the uncertainty, or disagree with concrete evidence.
- Fix accepted findings within the request's scope; track deferred work with a reason.
- Recheck the actual fix and affected behavior, not just the author's response.
- Invalidate conclusions whose relevant code changed after review. Record the reviewed revision and remaining limitations.
- Honor configured independent review. Self-review and a second pass by the same writer do not satisfy independence; a subagent review is not human approval.
- When independent review is unavailable, report the unmet gate rather than relabeling self-review as independent.

## Output and authority

Return findings ordered by impact, scope examined, checks observed, and an overall verdict tied to the candidate. Distinguish planned checks from executed checks.

Review does not authorize posting comments, requesting reviewers, approving/merging a PR or changing code unless the user's request includes those actions. Reuse a canonical feature/PR record; do not create another project workflow.

Read [sources](references/sources.md) for adapted review and verification patterns.

