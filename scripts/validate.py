#!/usr/bin/env python3
"""Validate the repository's canonical skills and platform manifests."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = ROOT / "skills"
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class ValidationError(Exception):
    pass


def load_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValidationError(f"{path.relative_to(ROOT)}: invalid JSON: {error}") from error
    if not isinstance(value, dict):
        raise ValidationError(f"{path.relative_to(ROOT)}: root must be an object")
    return value


def scalar(value: str) -> str:
    value = value.strip()
    if value.startswith(("'", '"')):
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError) as error:
            raise ValidationError(f"invalid quoted YAML scalar: {value}") from error
        if not isinstance(parsed, str):
            raise ValidationError(f"expected a string scalar, got: {value}")
        return parsed
    return value


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValidationError(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValidationError(f"{path.relative_to(ROOT)}: unclosed YAML frontmatter") from error

    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line or line[0].isspace():
            continue
        match = re.fullmatch(r"([A-Za-z0-9_-]+):\s*(.*)", line)
        if match:
            values[match.group(1)] = scalar(match.group(2))
    return values


def validate_skills() -> list[Path]:
    skill_files = sorted(SKILLS_ROOT.rglob("SKILL.md"))
    if not skill_files:
        raise ValidationError("skills/: no skills found")

    stray = [path for path in ROOT.rglob("SKILL.md") if not path.is_relative_to(SKILLS_ROOT)]
    if stray:
        paths = ", ".join(str(path.relative_to(ROOT)) for path in stray)
        raise ValidationError(f"canonical skill copies must live only under skills/: {paths}")

    names: set[str] = set()
    for path in skill_files:
        metadata = frontmatter(path)
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if not SKILL_NAME_RE.fullmatch(name) or len(name) > 64:
            raise ValidationError(f"{path.relative_to(ROOT)}: invalid skill name {name!r}")
        if path.parent.name != name:
            raise ValidationError(
                f"{path.relative_to(ROOT)}: folder {path.parent.name!r} must match name {name!r}"
            )
        if not description:
            raise ValidationError(f"{path.relative_to(ROOT)}: description is required")
        if name in names:
            raise ValidationError(f"duplicate skill name: {name}")
        names.add(name)
    return skill_files


def validate_links() -> None:
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip().strip("<>").split(maxsplit=1)[0]
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#"):
                continue
            relative = unquote(parsed.path)
            if not relative:
                continue
            resolved = (path.parent / relative).resolve()
            template_source = path.parent / (
                f"{Path(relative).stem.lower()}-template{Path(relative).suffix.lower()}"
            )
            if "assets" in path.parts and template_source.exists():
                continue
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                raise ValidationError(
                    f"{path.relative_to(ROOT)}: broken internal link {raw_target!r}"
                )


def require_string(payload: dict[str, object], key: str, source: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{source}: {key} must be a non-empty string")
    return value


def validate_manifests() -> None:
    codex = load_json(ROOT / ".codex-plugin/plugin.json")
    claude = load_json(ROOT / ".claude-plugin/plugin.json")
    codex_market = load_json(ROOT / ".agents/plugins/marketplace.json")
    claude_market = load_json(ROOT / ".claude-plugin/marketplace.json")

    plugin_name = require_string(codex, "name", ".codex-plugin/plugin.json")
    if require_string(claude, "name", ".claude-plugin/plugin.json") != plugin_name:
        raise ValidationError("Claude and Codex plugin names differ")
    if codex.get("version") != claude.get("version"):
        raise ValidationError("Claude and Codex plugin versions differ")
    if codex.get("skills") != "./skills/" or claude.get("skills") != "./skills/":
        raise ValidationError("plugin manifests must point skills at ./skills/")

    codex_plugins = codex_market.get("plugins")
    if not isinstance(codex_plugins, list) or len(codex_plugins) != 1:
        raise ValidationError("Codex marketplace must contain exactly one bundle entry")
    codex_entry = codex_plugins[0]
    if not isinstance(codex_entry, dict) or codex_entry.get("name") != plugin_name:
        raise ValidationError("Codex marketplace plugin name does not match manifest")
    source = codex_entry.get("source")
    if source != {"source": "local", "path": "./"}:
        raise ValidationError("Codex marketplace must point to the repository root")
    policy = codex_entry.get("policy")
    if policy != {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}:
        raise ValidationError("Codex marketplace policy is incomplete or unsupported")
    require_string(codex_entry, "category", ".agents/plugins/marketplace.json")

    claude_plugins = claude_market.get("plugins")
    if not isinstance(claude_plugins, list) or len(claude_plugins) != 1:
        raise ValidationError("Claude marketplace must contain exactly one bundle entry")
    claude_entry = claude_plugins[0]
    if not isinstance(claude_entry, dict) or claude_entry.get("name") != plugin_name:
        raise ValidationError("Claude marketplace plugin name does not match manifest")
    if claude_entry.get("source") != "./":
        raise ValidationError("Claude marketplace must point to the repository root")


def main() -> int:
    try:
        skill_files = validate_skills()
        validate_links()
        validate_manifests()
    except ValidationError as error:
        print(f"validation failed: {error}", file=sys.stderr)
        return 1
    print(f"repository validation passed ({len(skill_files)} skill)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
