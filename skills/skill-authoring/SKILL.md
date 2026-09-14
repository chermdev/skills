---
name: skill-authoring
description: Create, consolidate or revise Agent Skills from recurring workflows, documented failures, and reviewed technical sources. Use for skill instructions and behavioral evaluations; copying a book summary or installing a third-party package is a separate task.
---

# Skill Authoring

Encode decisions that improve an agent's work. Assume general engineering knowledge; spend instructions on discriminating triggers, meaningful trade-offs, workflow constraints and evidence.

## Authoring procedure

1. Identify representative requests, a near-miss that should not trigger the skill, the expected work product, and observed failure modes. Inspect existing skills for overlap before adding one.
2. Define one responsibility. Keep delivery orchestration, engineering disciplines and technology implementations separate. A domain skill can inform several delivery phases without becoming another tracker.
3. Evaluate sources before adapting them. Record exact repo revision/path or publication/section, what was read, what was retained, and intentional departures.
4. Translate principles into conditional decisions, failure checks and stopping conditions. Remove background exposition that does not change behavior.
5. Write a concise SKILL.md with name/description frontmatter. Put substantial conditional detail in locally linked references. Scripts and assets need a concrete repeated use.
6. Make the skill independently usable. Discover optional specialists by capability; do not assume sibling paths, an installation mode, a provider, model, tool or hidden shared file.
7. Validate structure and behavior separately; iterate on demonstrated failures, not a longer list of generic rules.

## Source and adaptation rules

- A skill inspired by a book is not proof that its author accurately represents that book. Attribute only material actually inspected.
- Do not import a complete book or chapter set as skill instructions. Synthesize actionable decisions and keep provenance.
- Check upstream licenses at the pinned revision and retain required notices with the portable skill when adapting content.
- Do not automatically pull upstream changes. Review updates for changed behavior, dependencies, permissions and licensing.
- Distinguish technology facts from agnostic criteria. Verify version-sensitive implementation guidance with current official documentation.
- Preserve user intent and repository constraints. Do not import mandatory pauses, extra approvals, trackers, architecture choices or deployment authority from a source.

## Evaluation procedure

Create realistic prompts and raw fixtures that expose a decision. Keep expected results and grading criteria out of the acting agent's input.

Compare no-skill baseline and skill-assisted runs on equivalent isolated fixtures with the same available tools, model/effort where controllable, and permissions. Record uncontrolled variables. Separate prompts from the rubric; require evidence for each result.

Include a positive case, a boundary/non-trigger case and an adversarial or partial-failure case. Add integration tests for optional composition and absent siblings. Mark not-run cases honestly; valid JSON is not a behavioral pass.

Use independent agents for forward-testing when available and authorized. Pass only the task, target skill and required raw artifacts, not the intended answer, suspected defect or implementation history. Keep generated work isolated from the repository.

## Acceptance and output

Ship the focused instructions, necessary resources, provenance and eval cases. Run added scripts, metadata/link checks and applicable host validation. Report the actual behavior exercised, remaining gaps and current installation/save state.

Follow the destination's existing save/versioning workflow. A request to create repository source does not authorize installing it globally. Do not claim a saved or installed skill based solely on a local directory.

Read [sources](references/sources.md) for adapted skill-testing methodology.

