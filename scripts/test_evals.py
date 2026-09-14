#!/usr/bin/env python3
"""Check malformed scenarios, fixture containment and rubric isolation."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import evals
import validate


class EvalIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "skills/example"
        (self.skill / "evals").mkdir(parents=True)
        self.skill_file = self.skill / "SKILL.md"
        self.skill_file.write_text("---\nname: example\ndescription: An example\n---\n", encoding="utf-8")
        self.case = {"id": 1, "prompt": "Review this boundary", "files": [], "expected_output": "SECRET ANSWER", "expectations": ["SECRET RUBRIC"]}
        self.payload = {"skill_name": "example", "evals": [self.case]}
        self.write()
        for module in (validate, evals):
            for key, value in (("ROOT", self.root), ("SKILLS_ROOT", self.root / "skills")):
                active = patch.object(module, key, value)
                active.start()
                self.addCleanup(active.stop)

    def write(self):
        (self.skill / "evals/evals.json").write_text(json.dumps(self.payload), encoding="utf-8")

    def test_prepare_does_not_leak_rubric_or_unrecognized_fields(self):
        self.case["future_answer_field"] = "ALSO SECRET"
        self.write()
        for with_skill in (False, True):
            result = evals.prepare("example", 1, with_skill)
            self.assertEqual(result["prompt"], self.case["prompt"])
            self.assertNotIn("SECRET", json.dumps(result))
            self.assertEqual("skill_file" in result, with_skill)

    def test_duplicate_ids_and_boolean_ids_rejected(self):
        for cases in ([self.case, dict(self.case)], [dict(self.case, id=True)]):
            self.payload["evals"] = cases
            self.write()
            with self.assertRaises(validate.ValidationError):
                validate.validate_evals([self.skill_file])

    def test_missing_escaping_and_rubric_fixtures_rejected(self):
        (self.root / "secret.txt").write_text("private", encoding="utf-8")
        for fixture in ("missing.txt", "../../secret.txt", "evals/evals.json"):
            self.case["files"] = [fixture]
            self.write()
            with self.assertRaises(validate.ValidationError):
                validate.validate_evals([self.skill_file])

    def test_real_fixture_and_unknown_case(self):
        (self.skill / "fixture.txt").write_text("raw input", encoding="utf-8")
        self.case["files"] = ["fixture.txt"]
        self.write()
        self.assertEqual(validate.validate_evals([self.skill_file]), 1)
        self.assertEqual(evals.prepare("example", 1)["files"], [str(self.skill / "fixture.txt")])
        with self.assertRaises(validate.ValidationError):
            evals.prepare("example", 2)

    def test_skill_link_cannot_depend_on_sibling(self):
        sibling = self.root / "skills/sibling"
        sibling.mkdir()
        (sibling / "guide.md").write_text("shared", encoding="utf-8")
        with self.skill_file.open("a", encoding="utf-8") as stream:
            stream.write("[dependency](../sibling/guide.md)\n")
        with self.assertRaises(validate.ValidationError):
            validate.validate_links()


if __name__ == "__main__":
    unittest.main()
