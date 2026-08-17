# ODOX source repository

This repository packages the ODOX management skill. Its canonical reusable
contract is [`.agents/skills/odox/references/contract.md`](.agents/skills/odox/references/contract.md).
Do not copy that contract into this file: this source-repository exception
keeps one authoritative contract in the distributable skill.

## Source maintenance

- Keep the package discoverable at `.agents/skills/odox` for the open Skills CLI.
- Treat `references/contract.md` as the versioned upstream contract. Its
  `ODOX Contract Version` and `references/contract-version.txt` must match.
- Keep `SKILL.md`, the contract, lifecycle reference, fixture expectations,
  and root README aligned whenever an operation or storage layout changes.
- Do not add a runtime CLI, merge script, hook, or agent-specific plugin.
  ODOX operations are performed by an agent following the skill.
- Keep fixture tests behavior-oriented. They may validate package structure,
  but must not couple correctness to a particular model prompt or merge wording.

## Verification

Run `py -3 tests/test_skill_package.py` and the skill validator after changing
the package. For an observable agent-behavior check, prepare and assert a
temporary repository with `py -3 tests/run_skill_fixture.py prepare <fixture>
<destination>`. Capture the agent's response in `<destination>/operation-output.md`
before running `... assert <fixture> <destination>`.

## Child DOX Index

- Root scope: this file owns the ODOX source repository.
- Human-facing root overview: [README.md](README.md)
- Canonical distributable skill: [.agents/skills/odox/SKILL.md](.agents/skills/odox/SKILL.md)
- Canonical reusable contract: [.agents/skills/odox/references/contract.md](.agents/skills/odox/references/contract.md)
