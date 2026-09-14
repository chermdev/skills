# Behavioral evaluation protocol

## Separate structure from behavior

`./scripts/validate.sh` checks repository/skill structure and scenario integrity, runs helper tests, and attempts configured host validators and CLI discovery. It does not prove agent behavior.

Each evaluated skill has `evals/evals.json` containing a prompt, optional raw fixtures, expected output and individual expectations. New disciplines include positive, boundary and adversarial cases. Existing delivery cases cover lifecycle/ownership, with new composition, fallback, proportionality, stale-evidence and compatibility cases.

## Prepare independent runs

```bash
python3 scripts/evals.py list
python3 scripts/evals.py prepare software-testing 3
python3 scripts/evals.py prepare software-testing 3 --with-skill
```

The preparation command emits only an allowlisted acting request. It never emits expected output, expectations or unknown rubric fields. It does not invoke a model or claim a pass. Fixtures resolve relative to the skill root and must exist outside its evals directory.

Run the requests using the available host's independent-agent mechanism. Give each actor only its request, raw fixtures and, for the assisted run, the target skill plus relevant local references. Do not expose evals, grading criteria, previous answers, git diffs or the author's conclusions. For stricter automation, place these resources in isolated workspaces; instructions alone are not a filesystem access control.

For a revised skill, compare base-revision and candidate-revision runs as well as no-skill runs when useful. Hold prompts, tool access, permissions, model/effort and fixtures constant where supported. Record uncontrolled differences. Do not change models merely to improve a score.

## Assess and retain evidence

After the actor finishes, evaluate each expectation against the actual response/artifact. Record the case ID, variant, candidate content identity, actor context, observed behavior and supporting excerpt. Use pass, fail, or unverified per expectation. A proposed test is not an executed test of a real application.

Do not infer that the skill helped if both baseline and assisted runs already pass. Report equivalent behavior honestly, and use differences only as qualitative evidence unless a larger repeated experiment supports more.

Run cases exercising the changed behavior and concrete remaining risks. For a new collection, cover each skill plus composition, absent siblings and ordinary low-risk work. Mark remaining cases not run; do not present the catalog size as the executed count.

Use separate fresh sessions per case for rigorous comparison. Small grouped runs are useful forward checks but can share context across cases; disclose this limitation. Human scoring and one run per prompt are not a statistically controlled benchmark.

Keep outputs or meaningful excerpts in a linked evidence record. If a failure leads to a patch, rerun the affected case on the new candidate. Avoid bloating skill entrypoints with test history.
