# chermdev skills

A canonical collection of independent Agent Skills.

- [`apple-hig`](skills/apple-hig/SKILL.md): Find and apply live Apple Human Interface Guidelines using a linked topic directory, navigation guidance, and checks for relevant changes.
- [`delivery`](skills/delivery/SKILL.md): A structured workflow for multi-session software delivery.
- [`delivery-review`](skills/delivery-review/SKILL.md): Read-only plan readiness, decisions and spikes.
- [`delivery-plan`](skills/delivery-plan/SKILL.md): Groom plans and perform bounded preparation.
- [`delivery-execute`](skills/delivery-execute/SKILL.md): Coordinate approved features and continue after verified completion.

The three autocomplete entry points require `delivery`, which owns their shared rules. Models, effort, task topology and authorization remain repository-specific.
- [`opengraph-design`](skills/opengraph-design/SKILL.md): Design branded social preview images using existing site assets, deliberate composition, and verified metadata.

## Choose one installation mode

Do not combine these modes. Installing the same skill directly and through the plugin makes hosts discover duplicate skills with the same name.

### Editable or selective installation

Use the open Agent Skills CLI when you want individual skills that you can inspect, symlink, copy, or update independently:

```bash
npx skills@latest add chermdev/skills --list
npx skills@latest add chermdev/skills --skill delivery
# Optional autocomplete entry points; keep delivery installed alongside them.
npx skills@latest add chermdev/skills --skill delivery-review delivery-plan delivery-execute
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

Released under the [MIT License](LICENSE).
