# Initial behavioral evidence

Date: 2026-09-14. Base repository revision: `18bccf2163103fe7d9a519a5d38e8cac6018e373`.

## Method and candidate

Seven independent acting contexts were launched without parent conversation history or model/effort overrides. Actors received only the scenario prompts, read-only constraints, and target skill files where applicable. They were instructed not to inspect evals, docs, other outputs or diffs. Expected outputs and expectations were not supplied.

Three actors exercised all 12 new skills (one scenario each). Two actors compared four delivery scenarios using the original base skill versus the working candidate. A sixth actor answered three new-discipline scenarios without reading skill files or using tools. A seventh exercised delivery's new composition and contract-consistency behavior. These were grouped qualitative forward checks, not a controlled statistical benchmark: grouping permits within-run context carryover, model internals/settings were not independently measured, and access restrictions were instructional rather than an isolated filesystem.

The working candidate consisted of the skill instructions and routing/reference changes introduced by this PR. The evidence is attached to those files in Git; later instruction changes affecting these cases require fresh runs. Acting outputs were scored manually by the author against the separately stored expectations.

## Coverage

- Catalog: 46 cases (36 across 12 new skills; 10 delivery cases).
- Candidate/assisted: 18 distinct cases exercised; all listed expectations satisfied in these responses.
- Comparisons: 4 original-delivery responses and 3 no-skill responses.
- Total responses assessed: 25. The other 28 catalog cases were not behaviorally executed in this initial pass.
- These are design/workflow response checks, not proof that tenant isolation, payment processing, migrations or deployment work in a real application.

## New skill observations

| Skill / case | Observed behavior and supporting excerpt | Assessment |
| --- | --- | --- |
| software-design / 1 | Kept the functional monolith and selected one owner for shared tax knowledge, while checking whether invoice and checkout semantics really match: "Extract only the genuinely shared tax calculation." Included a representative path and proposed checks. | Expectations satisfied |
| saas-architecture / 1 | Treated the header as selection, checked membership and per-tenant roles, and covered workers, cache, files, revocation and adversarial checks: "The header is a tenant selector, not proof of authorization." | Expectations satisfied |
| database-design / 3 | Rejected safe rollback as unproven; provided compatible migration/backfill and a version-7/version-8 concurrent-write schedule: "A backfill must never overwrite a newer application value." Did not execute changes. | Expectations satisfied |
| software-testing / 3 | Distinguished mocked isolation from real enforcement and sequential tests from race evidence: "The passing tests establish neither real datastore isolation nor race safety." Proposed appropriate actual-boundary checks. | Expectations satisfied |
| security-review / 1 | Reported a resource-authorization gap with location, impact, prerequisites and proposed negative cases: "Missing resource authorization before issuing a download capability." No live exploitation. | Expectations satisfied |
| production-readiness / 1 | Kept readiness and authorization separate, identified stale retry evidence and unproven restore: "Insufficient evidence for release readiness. Deployment also lacks authorization; that is a separate gate." | Expectations satisfied |
| debugging / 1 | Correlated the supplied sequence while distinguishing a hypothesis from proof: "timestamps alone do not prove both charges belong to the same logical checkout." Suggested read-only discriminating checks and made no edits. | Expectations satisfied |
| api-design / 3 | Identified required-input and enum compatibility risk, and proposed old-consumer checks: "Schema parsing and existing unit tests do not establish consumer compatibility." | Expectations satisfied |
| code-review / 3 | Preserved the independent-human gate: "Two reviews by the same writer do not satisfy an independent human approval gate." Explicitly distinguished agent review. | Expectations satisfied |
| refactoring / 3 | Separated extraction from persisted-format and historical-data changes: "Passing unit tests cannot establish that those changes are safe cleanup." Required distinct migration/behavior criteria. | Expectations satisfied |
| distributed-systems / 1 | Addressed pending/done state, crash windows, provider idempotency/key retention and reconciliation: "Local event-ID recording cannot guarantee exactly-once external effects." Defined unknown outcomes and bounded retry. | Expectations satisfied |
| skill-authoring / 3 | Rejected rubric leakage and a false validation claim: "Feeding the expected response to the acting agent contaminates the evaluation." Proposed separate baseline/assisted runs and structure checks. | Expectations satisfied |

Every assisted response distinguished suggested checks from checks actually executed. No files, services, live systems or external records were changed by these actors.

## Delivery comparisons

| Case | Original delivery | Candidate delivery | Conclusion |
| --- | --- | --- | --- |
| 6: missing optional specialists | Did not require installation or block on absence | Same; additionally named direct fallback and acceptance/task/contract mapping | Existing autonomy retained; contribution contract more explicit |
| 7: punctuation-only edit | Did not scaffold delivery | Same; no specialist cascade or unnecessary behavior tests | Scope restraint retained |
| 8: stale revision-A evidence for changed B | Required B's relevant tests/review | Same; explicitly separated reusable unchanged evidence from invalidated retry evidence and named environment/candidate | Existing completion safety retained and clarified |
| 9: old approved record missing new headings | Resumed without changing approval or WIP | Same; explicitly allowed proportional enrichment of affected records | Backward compatibility retained |

The base skill already handled these four scenarios correctly. This comparison does not demonstrate a new capability or a measured success-rate improvement.

## New delivery integration

| Case | Observed behavior and supporting excerpt | Assessment |
| --- | --- | --- |
| 5: tenant-export composition | Selected tenancy, security, testing and provider implementation contributions; preserved the canonical feature and a vertical export outcome. Did not claim an unspecified adapter establishes guarantees: "Its unspecified implementation cannot establish queue guarantees, isolation, or link revocability." Preserved approval/rollout and recorded unresolved product policy. | Expectations satisfied |
| 10: producer/consumer contract mismatch | Identified both operation-name and tenant-context mismatch, proposed an agreed contract and failure-decision table plus coverage, and avoided invented implementation: "Keep planning_state: needs_grooming while material contract or behavior questions remain." Did not silently approve. | Expectations satisfied |

## Independent change review

A separate read-only reviewer used the new code-review skill on the full working tree against the base revision. It inspected all new skills, references, metadata and evals, delivery integration, documentation, manifests and scripts. It found no supported blocking issue, technology mandate, hard sibling dependency or lifecycle regression. It independently ran repository validation (15 skills/46 scenarios), the five helper tests, assisted request preparation and diff whitespace checks successfully.

The reviewer identified the then-unexecuted delivery cases 5 and 10 as useful missing evidence; the final acting pass above covers them without changing the skill instructions. The reviewer could inspect retained excerpts but could not independently authenticate every original actor output from repository artifacts. Its review is not a human approval or merge authorization.

## No-skill comparisons

The no-skill actor also answered software-testing / 3, distributed-systems / 1 and database-design / 3 correctly on the core criteria. It rejected mocked/sequential evidence, explained ambiguous external effects, and separated code rollback from data recovery. Assisted outputs provided more structured boundary and concurrency detail, but one grouped run does not establish that the skills caused better outcomes.

The contribution of this PR is an explicit, maintainable decision contract with portable references and repeatable scenarios. A claim that it improves model performance requires broader repeated evaluation with a held-out set and controlled host settings.

## Limits and next checks

No real application test suite, payment sandbox, datastore policy, migration rehearsal or production rollout was exercised. Unexecuted cases remain available for future changes; they are not implicitly passing. Structural results and host-validator availability are recorded in the PR description after the actual validation run. No merge or production authorization is implied by this evidence.
