---
name: software-testing
description: Define or improve verification for behavior changes, bug fixes, integrations, and risky data or authorization paths. Use for test strategy and test adequacy; choose tooling separately and avoid test mandates for trivial non-behavioral edits.
---

# Software Testing

Choose the smallest set of checks that can detect the relevant failures. The number of tests and coverage percentage do not establish correctness.

## Select checks from risk

1. Read the required behavior and existing checks. Map each material invariant and failure mode to an observable assertion at an appropriate boundary.
2. For an ordinary reproducible bug, prefer a regression test that fails for the observed defect before fixing it. Verify the failure is the intended one, not broken setup.
3. For new domain logic, prefer test-first where useful. For integration, UI, infrastructure and migrations, choose verification that exercises the actual surface. Do not force one framework or test style onto all changes.
4. Use unit checks for isolated rules, integration checks for component/data boundaries, contract checks for independently changing consumers, and a few outside-in checks for critical user outcomes.
5. Control time, randomness, test data and external state. Model realistic responses at external boundaries; do not mock away the enforcement being tested.
6. Run the relevant checks on the candidate state, inspect exit codes and failures, and state what they establish and what remains unverified.

## Adequacy questions

- Would this check fail if the behavior regressed? For a new regression check, demonstrate the defect or a representative counterexample when safely possible.
- Does a success assertion also verify persistence or externally visible effects, rather than only a success message?
- Are rejection, retry, empty, permission and cancellation states covered where owned by this change?
- Does concurrency matter? A single-threaded happy path cannot establish uniqueness, inventory limits, or correct retry handling.
- Is an integration being tested through its real security/transaction boundary? Mocking the repository is insufficient to prove datastore isolation.
- Are tests independent and repeatable? Retries can collect evidence but must not hide a flaky failure.

## Proportionality

A wording or spacing change may need only inspection or a rendered check. A prototype can use reduced verification with explicit limitations. A migration may require compatibility, backfill and restore rehearsal rather than UI tests. Security and financial invariants require stronger negative and failure-path evidence.

Do not write assertions that mirror implementation details solely to increase coverage. Broaden testing to resolve a concrete risk or satisfy an existing gate; stop once that risk is sufficiently addressed.

## Output

Record behavior/risk -> check -> observed result -> limitation in the existing feature or test record. Distinguish planned, executed, passed, failed, and unavailable checks. Never infer a passing run from a test file, previous session, or another agent's summary.

For detailed examples read [verification patterns](references/verification-patterns.md); for adapted methodology read [sources](references/sources.md). A technology-specific capability may select commands and fixtures, but does not own the overall strategy.

