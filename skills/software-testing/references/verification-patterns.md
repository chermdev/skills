# Verification patterns

Use only patterns that target the change's risks. Commands and fixtures come from the repository and its technology capabilities.

| Change | Useful evidence | Insufficient evidence |
| --- | --- | --- |
| Domain calculation | Boundary/property examples with independent expected values | Reusing the production calculation to compute expectations |
| Authorization | Two actors/tenants, manipulated IDs, denied side effects, real enforcement | Mocking the authorization check to return false |
| Data concurrency | Interleaved operations and persisted invariant after commit/abort | Sequential happy-path calls |
| Retried mutation | Concurrent duplicates, timeout after effect, replay and conflicting payload | One request returns success |
| Migration | Representative old data, concurrent writes, mixed versions, restart and recovery | Empty-schema apply succeeds |
| UI behavior | Owned states and real action outcome, accessibility where affected | Snapshot or screenshot alone proves persistence |
| Presentation-only edit | Inspect changed rendering/content and relevant layout | New tests that only search for the literal replacement text |

## Regression evidence

Reproduce the original failure before fixing it when feasible. If the fix already exists, use an isolated candidate/baseline comparison or a controlled counterexample. Do not destructively revert unrelated work to demonstrate red/green.

For a flaky test, preserve first-attempt evidence and investigate the changing state. Retries can characterize frequency, but retry success does not make the initial failure disappear.

## Meaningful boundaries

Choose the lowest-cost check that actually crosses the risk boundary. A unit test may prove a pure rule but not the datastore constraint; an integration check may prove persistence but not a user's complete workflow. Avoid running every layer for every case.

## Evidence record

Record the candidate, environment, command or manual procedure, observed result, and relevant artifacts. Missing access or tooling is a limitation, not a pass. Reuse unchanged evidence explicitly and rerun checks affected by later edits.
