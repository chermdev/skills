# Bug records

Use this structure for bugs discovered during delivery. The coordinator resolves the location once
in the repository contract; feature owners MUST reuse it rather than invent per-task bug logs.

## Location and identity

Paths are relative to the configured planning root (default `.github/plans`):

```text
.github/plans/
  config.yaml                 # paths.bugs: bugs; paths.bug_template: templates/bug.md
  templates/bug.md             # installed from Delivery assets/bug-template.md
  bugs/
    BUG-20260919-search-focus.md
```

Use `BUG-YYYYMMDD-short-kebab-slug` as both filename stem and `bug_id`, dated at discovery.
Do not rename a record when its status changes or move resolved records. Before creating one,
search the bug directory and configured tracker for the same symptom/boundary. Update an existing
match and link all affected features. If two unrelated findings collide, qualify the slug by
component; no global counter or shared index is required. List records with `rg --files` and inspect
frontmatter for status; the feature links the bug rather than copying its details.

On an existing repository, preserve an explicitly configured bug path/schema or tracker authority.
If none is defined, the coordinator installs these defaults once when bug tracking is requested or
a delivery finding needs recording. Do not relocate existing reports automatically. If a tracker
owns bugs and writes are unavailable/unauthorized, use this local structure as a pending report with
`external_refs`; do not claim tracker synchronization or create a second canonical status.

## Required record

Copy [the bug template](../assets/bug-template.md). Keep these fields:

- Identity, concise title, created/updated dates and status.
- `origin_feature`: relative link to the discovering feature, or null when not tied to one.
- `owner`: responsible task/person, or `unassigned`; discovery does not claim another boundary.
- `blocks`: relative paths to features whose named acceptance criteria cannot pass; empty for a
  nonblocking finding. In the body, name each failed criterion and the evidence. Severity alone
  does not determine whether this delivery is blocked.
- `introduced_by_current_change`: true, false or null when unknown; do not infer a cause from timing.
- `external_refs`: existing provider IDs/URLs when relevant; no implicit external mutation.
- Observed/expected behavior, smallest known reproduction, environment and source revision,
  evidence links, affected file/function, known facts versus hypotheses, next action and exit check.

Keep logs/captures in existing evidence storage and link them. Never copy sensitive data into a bug
record when a redacted reproduction suffices. A small fixed bug can have a short record; do not
require a separate investigation document or commit for each finding.

## States and closure

- `open`: recorded and awaiting triage/assignment.
- `investigating`: one named owner is actively diagnosing or fixing it.
- `deferred`: no active work; MUST include why it is deferred and a concrete next action or trigger.
- `resolved`: MUST include fix revision (or other resolution) and the verification result/revision.
- `dismissed`: MUST include evidence for duplicate, expected behavior or invalid report; duplicates
  link the surviving bug. Failure to reproduce once is not proof that a bug is invalid.

A deferred bug can still block a feature. Keep `blocks` and that feature's workflow state accurate;
never mark acceptance complete because its bug was moved to future work. On resolution, retain the
historical blocking relation and closure evidence; reassess the feature before resuming it. Reopen
resolved/dismissed bugs as `open` when new evidence invalidates closure, retaining earlier evidence.
Use the [execution triage](execution.md#discovered-bugs-and-bounded-investigation) to decide whether
to fix inline or defer investigation. The current feature's follow-up field and handoff link the
record; they do not become competing bug registries.
