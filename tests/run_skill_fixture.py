"""Materialize and assert manual, behavior-level ODOX skill fixtures.

This is test tooling, not an ODOX runtime command. It gives a tester an
isolated repository, lets an agent perform the named skill operation, then
checks observable file-system results.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


FIXTURES = Path(__file__).resolve().parent / "fixtures" / "acceptance"


def scenario_path(name: str) -> Path:
    path = FIXTURES / name
    if not (path / "assertions.json").is_file():
        raise ValueError(f"Unknown fixture: {name}")
    return path


def load_assertions(name: str) -> dict:
    return json.loads((scenario_path(name) / "assertions.json").read_text(encoding="utf-8"))


def prepare(name: str, destination: Path) -> None:
    fixture = scenario_path(name) / "before"
    if destination.exists():
        raise ValueError(f"Destination already exists: {destination}")
    shutil.copytree(fixture, destination)
    subprocess.run(["git", "init", "-q"], cwd=destination, check=True)
    subprocess.run(["git", "config", "user.email", "fixture@example.invalid"], cwd=destination, check=True)
    subprocess.run(["git", "config", "user.name", "ODOX fixture"], cwd=destination, check=True)
    subprocess.run(["git", "add", "--all"], cwd=destination, check=True)
    subprocess.run(["git", "commit", "-qm", "fixture baseline"], cwd=destination, check=True)
    details = load_assertions(name)
    print(f"Prepared {destination}")
    print(f"Perform this operation there: {details['operation']}")
    print("Then run this script with `assert` and the same fixture name.")


def assert_fixture(name: str, repository: Path) -> int:
    details = load_assertions(name)
    failures: list[str] = []
    for assertion in details["assertions"]:
        path = repository / assertion["path"]
        kind = assertion["kind"]
        if kind == "exists":
            if not path.is_file():
                failures.append(f"missing file: {assertion['path']}")
        elif kind in ("contains", "output_contains"):
            if not path.is_file() or assertion["text"] not in path.read_text(encoding="utf-8"):
                failures.append(f"missing required {kind} text in: {assertion['path']}")
        elif kind == "unchanged":
            original = scenario_path(name) / "before" / assertion["path"]
            if not path.is_file() or path.read_bytes() != original.read_bytes():
                failures.append(f"changed unexpectedly: {assertion['path']}")
        elif kind == "count":
            if not path.is_file() or path.read_text(encoding="utf-8").count(assertion["text"]) != assertion["value"]:
                failures.append(f"unexpected count in: {assertion['path']}")
        else:
            failures.append(f"unknown assertion kind: {kind}")
    if failures:
        print("FAILED")
        print("\n".join(failures))
        return 1
    print("PASSED")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)
    for command in ("prepare", "assert"):
        child = subcommands.add_parser(command)
        child.add_argument("fixture")
        child.add_argument("repository", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            prepare(args.fixture, args.repository)
            return 0
        return assert_fixture(args.fixture, args.repository)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
