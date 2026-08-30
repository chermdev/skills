#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
validation_python="${VALIDATION_PYTHON:-python3}"

"${validation_python}" "${repo_root}/scripts/validate.py"

if command -v claude >/dev/null 2>&1; then
  claude plugin validate "${repo_root}/.claude-plugin/plugin.json" --strict
  claude plugin validate "${repo_root}/.claude-plugin/marketplace.json" --strict
else
  echo "skip: Claude Code validator is not installed"
fi

if [[ -n "${CODEX_PLUGIN_VALIDATOR:-}" ]]; then
  "${validation_python}" "${CODEX_PLUGIN_VALIDATOR}" "${repo_root}"
else
  echo "skip: set CODEX_PLUGIN_VALIDATOR to plugin-creator/scripts/validate_plugin.py"
fi

if [[ -n "${SKILL_VALIDATOR:-}" ]]; then
  while IFS= read -r skill_dir; do
    "${validation_python}" "${SKILL_VALIDATOR}" "${skill_dir}"
  done < <(find "${repo_root}/skills" -name SKILL.md -print0 | xargs -0 -n1 dirname | sort)
else
  echo "skip: set SKILL_VALIDATOR to skill-creator/scripts/quick_validate.py"
fi

npx --yes skills@latest add "${repo_root}" --list
