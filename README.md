<p align="center">
  <img src="./banner.jpg" alt="ODOX" width="100%">
</p>

## What ODOX is

ODOX is a self-documenting documentation contract for Odoo repositories. It is
distributed as one agent-independent skill: install it once, then initialize
each repository with a durable local contract that agents can follow without
ODOX being installed.

The root `AGENTS.md` remains the repository-wide agent workflow. Each Odoo
module's `README.md` is the main technical contract for people and agents.
Optional module `AGENTS.md` files are reserved for real agent-only hazards.

## Install

Install ODOX globally with the open Skills CLI:

```bash
npx skills add piruin/odox@odox -g -a codex
```

Slash commands work on hosts that provide them. Every operation also accepts
plain language, for example: “Initialize ODOX in this repository.” Advanced
project-local installation remains available through the Skills CLI, but global
installation is the normal onboarding path. Keep local skill payloads out of a
repository with clone-local Git excludes if that advanced mode is used.

## Lifecycle

| Request | Result |
| --- | --- |
| `/odox` | Read-only status, installed/base versions, and a useful next step. |
| `/odox init` | Preserves root instructions, adds one hidden managed bootstrap, and stores an editable local contract plus its upstream base. |
| `/odox update` | Refreshes only the global ODOX skill, then performs an agent-led semantic three-way update. |
| `/odox update local` | Updates against the installed copy without network access. |
| `/odox check` | Runs inexpensive structural validation. Use `full`, `changed`, or module paths for semantic audits. |
| `/odox document` | Deliberately creates or maintains module READMEs; it is never an initialization side effect. |

Initialized repositories store their editable contract, exact upstream base,
and version metadata under `.agents/odox/`. Existing repository instructions
always take precedence. ODOX surfaces same-policy update conflicts for the
maintainer instead of silently applying a text merge.

## Contract model

ODOX uses a hybrid structure:

1. Repository root
   - `AGENTS.md` is mandatory and owns workflow, indexing, and hazards.
   - `README.md` is human-facing.
2. Odoo module
   - `README.md` is the default primary technical contract.
   - `AGENTS.md` is optional and supplemental.

Module READMEs should describe current purpose, behavior, models, views,
security, dependencies, extension seams, verification, and important
invariants. Around 300 lines is a review threshold, not a hard limit.

## Source repository

This repository is the documented source-repository exception: the single
canonical reusable contract lives in
[`.agents/skills/odox/references/contract.md`](.agents/skills/odox/references/contract.md),
not as a duplicate root contract. The package contains the lifecycle protocol
and fixture-based validation scenarios used to keep that contract release-ready.

## Development

GitHub Actions runs `python3 tests/test_skill_package.py` for every push and
pull request. Run the same command locally before publishing a package change.

## Credits

<p align="center">
  Adapted from the DOX idea by <strong><a href="https://www.agent-zero.ai/">Agent Zero</a></strong><br>
  ODOX reframes the model for self-documenting Odoo repositories
</p>
