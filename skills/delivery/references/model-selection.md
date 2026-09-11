# Model and effort selection

Plan execution settings with the feature so another session can dispatch it without
reconstructing the reasoning. Keep this recommendation independent of approval, ownership,
parallelism and rollout. Markdown fields do not configure an agent automatically.

## Feature frontmatter

- `recommended_model`: an exact host model identifier allowed by the user/repository policy,
  or `null` when no supported selection is known. Do not turn a display name into a guessed ID.
- `recommended_reasoning_effort`: a supported effort value for that model, or `null` when
  unresolved or the host/model does not expose an effort control. Null does not mean low effort.
- `reasoning_rationale`: a short, feature-specific explanation of the complexity and failure
  impact behind the choice. Explain unresolved capabilities or absent controls here as well.

Keep all three fields in new feature records. Replace template placeholders during planning;
use YAML null rather than strings such as `"null"`, `default`, or `TBD` as dispatch values.
Follow the repository's language convention for prose. Rollups link or summarize these fields;
the feature remains canonical. Actual settings belong in the execution checkpoint.

## Select proportionately

1. Read explicit user preferences and the local contract first. An explicit user override takes
   precedence over a recorded recommendation. Preserve configured model families, effort ranges,
   budgets and fallback rules; do not import another project's policy.
2. Verify the available model identifiers and supported effort controls from current tool schemas,
   host configuration or official documentation when needed. Treat repository model policy as
   intent, not proof that a particular host supports it. Do not invent price or capability claims.
3. Choose the least intensive permitted configuration that fits the feature's reasoning demands.
   Where the allowed range is medium–high, use the following criteria:

   | Effort | Typical fit | Evidence to put in the rationale |
   | --- | --- | --- |
   | medium | Bounded changes using established contracts and concrete reproduction/acceptance checks | Existing adapter/component reuse, localized behavior, deterministic validation |
   | high | Security boundaries, concurrent or out-of-order state, distributed integrations, difficult recovery, or domain calculations needing independent verification | Specific failure modes, interacting systems, ambiguity and consequences of an incorrect result |

   File count and UI/backend labels alone do not determine effort. A small authorization fix may
   need high effort; a larger form-driven screen using established components may fit medium.
   For a different allowed range, apply these criteria to supported choices without inventing
   a mapping between providers' effort controls.
4. Reassess after grooming, a material scope change, or a newly discovered failure mode.
   Higher effort does not resolve missing product decisions: preserve `needs_grooming` when
   intent is unresolved. More effort does not replace acceptance evidence or independent review.

For example, **only when a project's policy and host allow Sol 5.6 Medium–High**, a feature
that repairs membership revocation and billing authorization boundaries could contain:

```yaml
recommended_model: gpt-5.6-sol
recommended_reasoning_effort: high
reasoning_rationale: "Membership revocation and billing gates cross security-critical authorization boundaries."
```

This is an example policy, not a global default or a claim that every host provides this model.
If model capabilities are unknown, keep affected fields null with a concrete explanation and
continue independent planning. Missing execution metadata alone does not change scope approval.

## Apply at execution

Read the canonical recommendation again before dispatch. Revalidate availability on the target
host and respect the user's requested task topology. Create separate tasks or delegate only when
authorized by the user and governing instructions; this skill's metadata grants neither action.

Use the callable tool's current schema. For example, Codex separate-task tools may accept
`model` and `thinking`, while a subagent tool may accept `model` and `reasoning_effort`.
These are tool-specific mappings; verify them before calling. Never send null placeholders as
literal model IDs, guess flags, or claim that editing frontmatter changed the current agent.

If a recommendation is unavailable, use an already authorized fallback and record the actual
setting and reason. Otherwise surface the mismatch before dependent execution; continue any
independent planning. If the host cannot expose or change the current model/effort, record the
limitation rather than claim the recommendation was applied. Do not silently change an explicit
user selection. Keep the recommendation and actual execution record distinct.
