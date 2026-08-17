"""Static package checks for the behavior fixtures used by the ODOX skill."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "odox"


class SkillPackageTests(unittest.TestCase):
    def test_ci_workflow_runs_package_tests(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "package-tests.yml").read_text(encoding="utf-8")
        for expected in (
            "push:",
            "pull_request:",
            "actions/checkout@v6",
            "python3 tests/test_skill_package.py",
        ):
            self.assertIn(expected, workflow)

    def test_skill_metadata_and_resources_are_discoverable(self) -> None:
        skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertRegex(skill, r"(?m)^name: odox$")
        self.assertNotIn("TODO", skill)
        for resource in ("contract.md", "contract-version.txt", "operations.md"):
            self.assertTrue((SKILL / "references" / resource).is_file(), resource)

    def test_contract_versions_match(self) -> None:
        contract = (SKILL / "references" / "contract.md").read_text(encoding="utf-8")
        declared = re.search(r"ODOX Contract Version:\*\* `([^`]+)`", contract)
        self.assertIsNotNone(declared)
        version = (SKILL / "references" / "contract-version.txt").read_text(encoding="utf-8").strip()
        self.assertEqual(declared.group(1), version)
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")

    def test_operations_define_idempotent_bootstrap_and_safety(self) -> None:
        operations = (SKILL / "references" / "operations.md").read_text(encoding="utf-8")
        for expected in (
            "<!-- odox:managed:start -->",
            "<!-- odox:managed:end -->",
            "Initialization is idempotent.",
            "only operation allowed to use the network",
            "semantic three-way",
            "base snapshot after interruption",
        ):
            self.assertIn(expected, operations)

    def test_fixture_expectations_cover_required_behavior_seams(self) -> None:
        expectations = json.loads((ROOT / "tests" / "fixtures" / "expectations.json").read_text(encoding="utf-8"))
        names = {fixture["name"] for fixture in expectations["fixtures"]}
        required = {
            "init-without-root-instructions",
            "init-with-existing-instructions",
            "init-already-managed",
            "update-independent-edits",
            "update-policy-conflict",
            "update-local-offline",
            "check-missing-contract",
            "check-module-selection",
            "document-curated-readme",
            "status-read-only",
        }
        self.assertTrue(required <= names)

    def test_manual_acceptance_runner_has_concrete_repositories(self) -> None:
        runner = ROOT / "tests" / "run_skill_fixture.py"
        self.assertTrue(runner.is_file())
        for name in (
            "init-existing-instructions",
            "init-idempotent",
            "update-independent-edits",
            "update-policy-conflict",
            "update-local-offline",
            "update-interrupted",
            "check-selected-module",
            "document-curated-readme",
            "status-read-only",
        ):
            fixture = ROOT / "tests" / "fixtures" / "acceptance" / name
            self.assertTrue((fixture / "before").is_dir())
            self.assertTrue((fixture / "assertions.json").is_file())

    def test_fixture_preparation_creates_a_temporary_git_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "repository"
            subprocess.run(
                [sys.executable, "tests/run_skill_fixture.py", "prepare", "status-read-only", str(destination)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            result = subprocess.run(
                ["git", "rev-parse", "--is-inside-work-tree"],
                cwd=destination,
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.stdout.strip(), "true")

    def test_document_fixture_contains_representative_addon_seams(self) -> None:
        addon = ROOT / "tests" / "fixtures" / "document-addon" / "care_note"
        for relative_path in (
            "__manifest__.py",
            "models/care_note.py",
            "views/care_note_views.xml",
            "security/ir.model.access.csv",
            "data/ir_cron.xml",
            "report/care_note_report.xml",
            "tests/test_care_note.py",
            "README.md",
        ):
            self.assertTrue((addon / relative_path).is_file(), relative_path)


if __name__ == "__main__":
    unittest.main()
