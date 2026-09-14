# chermdev skills

A canonical collection of independent Agent Skills.

- [`apple-hig`](skills/apple-hig/SKILL.md): Find and apply live Apple Human Interface Guidelines using a linked topic directory, navigation guidance, and checks for relevant changes.
- [`delivery`](skills/delivery/SKILL.md): A structured workflow for multi-session software delivery.
- [`opengraph-design`](skills/opengraph-design/SKILL.md): Design branded social preview images using existing site assets, deliberate composition, and verified metadata.

## Agnostic engineering disciplines

| Skill | Purpose |
| --- | --- |
| [software-design](skills/software-design/SKILL.md) | Domain boundaries, dependencies and complexity |
| [saas-architecture](skills/saas-architecture/SKILL.md) | Tenant isolation, lifecycle and fairness |
| [database-design](skills/database-design/SKILL.md) | Invariants, concurrency and safe migrations |
| [api-design](skills/api-design/SKILL.md) | Contracts, compatibility and retry semantics |
| [distributed-systems](skills/distributed-systems/SKILL.md) | Partial failure, ordering and reconciliation |
| [software-testing](skills/software-testing/SKILL.md) | Risk-based verification and test adequacy |
| [security-review](skills/security-review/SKILL.md) | Trust boundaries and concrete security findings |
| [code-review](skills/code-review/SKILL.md) | Candidate review and verified finding closure |
| [production-readiness](skills/production-readiness/SKILL.md) | Operational evidence, recovery and rollout assessment |
| [debugging](skills/debugging/SKILL.md) | Evidence-based diagnosis and bounded experiments |
| [refactoring](skills/refactoring/SKILL.md) | Behavior-preserving structural change |
| [skill-authoring](skills/skill-authoring/SKILL.md) | Actionable instructions and independent evaluation |

Delivery selects relevant capabilities; each skill also works independently. Technology-specific skills are future work. See the [system design and source strategy](docs/engineering-skills.md), including the composition diagram.

## Choose one installation mode

Do not combine these modes. Installing the same skill directly and through the plugin makes hosts discover duplicate skills with the same name.

### Editable or selective installation

Use the open Agent Skills CLI when you want individual skills that you can inspect, symlink, copy, or update independently:

```bash
npx skills@latest add chermdev/skills --list
npx skills@latest add chermdev/skills --skill delivery
```

`skills` 1.5.23 has an upstream parsing bug in the equals-sign form: `--skill=delivery` is accepted but can select every skill. Use the documented space-separated form above to select an individual skill.

### Managed plugin installation

Use this mode when Claude Code or Codex should manage the collection as one versioned plugin.

Claude Code:

```bash
claude plugin marketplace add chermdev/skills
claude plugin install chermdev-skills@chermdev-skills
```

Codex:

```bash
codex plugin marketplace add chermdev/skills
codex plugin add chermdev-skills@chermdev-skills
```

The repository root is the plugin root for both hosts, so every installation mode consumes the same files under `skills/`.

## Maintenance

Run `./scripts/validate.sh` before committing. It checks skill metadata, internal links, manifests, marketplace entries, and `npx skills add ./ --list`; when the host validators are installed, it also runs Claude Code validation. The Codex plugin validator can be supplied through `CODEX_PLUGIN_VALIDATOR`, and the official skill validator through `SKILL_VALIDATOR`.

Validation also checks eval scenario structure, portable resources and rubric-free request preparation. Behavioral execution is separate: see the [evaluation protocol](docs/evaluation-protocol.md) and [initial evidence](docs/evaluations/agnostic-skills.md).

Released under the [MIT License](LICENSE).
