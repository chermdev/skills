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

This is a mandatory gate before creating or resuming a feature task, including follow-up fixes
and authorized reviewer assignments. The coordinator MUST:

1. Read the canonical feature's model and effort. Resolve the effective pair from explicit user
   instructions first, then repository policy and the feature recommendation. Recommendations
   do not themselves authorize a tool override, task creation or delegation; honor the callable
   tool's authorization requirements. Resolve an authorization conflict before dependent execution.
2. Verify the exact model identifier and supported effort on the target host. Do not silently
   substitute a more capable model, raise effort, or accept a host default. When medium fits an
   established contract, do not select high merely because the feature spans several files.
3. Apply BOTH values through the host's supported controls. For example, separate-task tools may
   require `model` and `thinking`; subagent tools may require `model` and `reasoning_effort`.
   When those fields are supported and authorized, MUST send them explicitly on creation and
   follow-up dispatch. Never assume the parent task, existing task or Markdown sets them.
   If a full-history fork disallows overrides, use an authorized context mode that accepts the
   pair and include the necessary bounded context; do not drop the settings to keep the fork.
4. Check the dispatch result and record the task identifier, requested pair, applied pair when
   confirmed, and any explicit override in the feature checkpoint. A successful explicit setter
   without readback is evidence of an accepted setting request; record that limit without claiming
   an independently observed runtime setting. Reconcile a reported mismatch before implementation.

If the host lacks a control or the selected pair is unavailable, use only a fallback already
explicitly authorized by the user/repository and record its exact pair and reason. Otherwise
surface the concrete mismatch and request only the missing choice/authorization; keep progressing
on independent preparation. Writing "inherited", "unknown", or "host limitation" does not by
itself permit feature execution under unresolved settings. An unavailable effort control can be
recorded as not applicable only when that model/configuration is explicitly permitted.

Keep recommendations and actual execution history distinct. A later correction applies to future
work in the existing task; preserve completed work and do not rewrite its historical settings.
Editing frontmatter never changes the current agent. Never send null placeholders as literal
model IDs or invent unsupported flags.
