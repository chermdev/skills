# Maintainer guide

- Write all repository content in English, including documentation, skill instructions, examples, templates, and code comments.
- Use Conventional Commits for commit messages: `<type>[optional scope][!]: <description>`, for example `feat(apple-hig): add live HIG navigation guidance`.
- Treat every directory below `skills/` as an independent Agent Skill and its only canonical copy.
- Keep `SKILL.md`, `agents/`, `references/`, `scripts/`, and `assets/` together inside that skill.
- Do not add generated platform copies. Point plugin manifests at `./skills/`.
- Run `./scripts/validate.sh` before committing once the validation tooling exists.
- Keep repository and plugin license metadata aligned with `LICENSE`.
- Keep methodology and domain skills technology-agnostic. Technology-specific instructions belong in dedicated skills; clearly marked examples do not establish global defaults.
- Keep each skill usable independently. Discover optional specialist capabilities instead of linking to sibling files or requiring the entire bundle.
- Adapt reviewed sources selectively, pin provenance, retain applicable notices inside portable skills, and distinguish source inspiration from directly analyzed books.
- Validate behavioral changes with realistic cases whose expected answers stay outside the acting agent's context. Report structural validation and behavioral evidence separately.
