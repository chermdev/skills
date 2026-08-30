# Maintainer guide

- Treat every directory below `skills/` as an independent Agent Skill and its only canonical copy.
- Keep `SKILL.md`, `agents/`, `references/`, `scripts/`, and `assets/` together inside that skill.
- Do not add generated platform copies. Point plugin manifests at `./skills/`.
- Run `./scripts/validate.sh` before committing once the validation tooling exists.
- Keep repository and plugin license metadata aligned with `LICENSE`.
