# Maintainer guide

- Treat every directory below `skills/` as an independent Agent Skill and its only canonical copy.
- Keep `SKILL.md`, `agents/`, `references/`, `scripts/`, and `assets/` together inside that skill.
- Do not add generated platform copies. Point plugin manifests at `./skills/`.
- Run `./scripts/validate.sh` before committing once the validation tooling exists.
- Do not add a license until the repository owner chooses one explicitly.
