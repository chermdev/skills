#!/usr/bin/env python3
"""Prepare rubric-free requests for a host's independent acting agent."""

from __future__ import annotations

import argparse
import json

from validate import ROOT, SKILLS_ROOT, ValidationError, load_json, validate_evals, validate_skills


def prepare(skill: str, case_id: int, with_skill: bool = False) -> dict[str, object]:
    skill_files = validate_skills()
    validate_evals(skill_files)
    selected = next((path for path in skill_files if path.parent.name == skill), None)
    if selected is None:
        raise ValidationError(f"unknown skill: {skill}")
    payload = load_json(selected.parent / "evals/evals.json")
    case = next((item for item in payload["evals"] if item["id"] == case_id), None)
    if case is None:
        raise ValidationError(f"unknown eval ID for {skill}: {case_id}")
    # Explicit allowlist: never include expected_output, expectations, or future rubric fields.
    request: dict[str, object] = {
        "case": f"{skill}:{case_id}",
        "prompt": case["prompt"],
        "files": [str((selected.parent / name).resolve()) for name in case["files"]],
        "mode": "with-skill" if with_skill else "baseline",
        "isolation": "Do not read evals directories, grading rubrics, prior outputs or repository history. Use an isolated workspace and only the supplied task resources. Do not perform external mutations.",
    }
    if with_skill:
        request["skill_file"] = str(selected.resolve())
    else:
        request["isolation"] += " Do not load the candidate skill or other collection instructions."
    return request


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="List scenario identifiers; does not execute them")
    command = commands.add_parser("prepare", help="Emit a rubric-free acting request as JSON")
    command.add_argument("skill")
    command.add_argument("case_id", type=int)
    command.add_argument("--with-skill", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "list":
            skills = validate_skills()
            validate_evals(skills)
            result = []
            for path in skills:
                eval_path = path.parent / "evals/evals.json"
                if eval_path.exists():
                    payload = load_json(eval_path)
                    result.extend({"skill": payload["skill_name"], "id": c["id"]} for c in payload["evals"])
        else:
            result = prepare(args.skill, args.case_id, args.with_skill)
        print(json.dumps(result, indent=2))
    except ValidationError as error:
        parser.exit(1, f"eval preparation failed: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
