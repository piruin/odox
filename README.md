<p align="center">
  <img src="./banner.jpg" alt="ODOX" width="100%">
</p>

## What ODOX is

ODOX is a self-documenting `AGENTS.md` framework for Odoo repositories.

It keeps one strong agent contract at the repository root, then uses each Odoo module's `README.md` as the main local contract for both humans and AI agents.

That means:

- the root `AGENTS.md` owns repo-wide workflow, indexing, and documentation rules
- each module `README.md` explains the current module behavior and structure
- module `AGENTS.md` is optional and only exists for agent-specific hazards or workflows
- code wins when docs drift, and the docs must be updated back into sync

The goal is simple: less recursive AGENTS sprawl, better module documentation, and a documentation shape that fits how Odoo repositories are actually maintained.

## ODOX model

ODOX uses a hybrid structure:

1. Repository root

- `AGENTS.md` is mandatory
- `README.md` stays human-facing

2. Odoo module

- `README.md` is the default primary contract
- `AGENTS.md` is optional and supplemental

This keeps the repo-level workflow explicit while making module documentation readable and shared.

## Module README expectations

A module `README.md` should stay technical, concise, and aligned with current code. It should usually cover:

- purpose and business scope
- main models, wizards, views, security, and data areas
- dependencies and integration points
- extension seams and important workflows
- verification or test entrypoints when they exist
- important human-relevant hazards or invariants

ODOX treats 300 lines as a soft readability threshold, not a hard cap. If a module README grows beyond that, review whether to:

- split module responsibilities
- trim stale or redundant prose
- move agent-only detail into a small optional `AGENTS.md`

## When to add module AGENTS.md

Add a module `AGENTS.md` only when the module has agent-specific context that should not live in the README, such as:

- edit hazards or sequencing rules
- generated files or special maintenance workflows
- local constraints that would clutter the README
- multiple internal subareas that need explicit agent routing

If a module does not have those needs, keep it README-only.

## How to use

1. Copy [AGENTS.md](./AGENTS.md?plain=1) into the root of your Odoo repository.
2. Keep your root `README.md` as the human-facing project overview.
3. For each Odoo module, maintain a concise `README.md` that matches the current code.
4. Add a module `AGENTS.md` only when agent-only instructions are genuinely needed.

When working in a module, agents should read:

1. the root `AGENTS.md`
2. the module `README.md`
3. the module `AGENTS.md`, if one exists

## Why this differs from deep DOX trees

Classic recursive AGENTS trees optimize for local precision everywhere. ODOX keeps that precision where it matters most for Odoo work:

- repo-wide workflow at the root
- module-level truth in each addon README
- agent-only exceptions in small supplemental AGENTS files

This better matches Odoo's natural durable boundary: the module.

## Credits

<p align="center">
  Adapted from the DOX idea by <strong><a href="https://www.agent-zero.ai/">Agent Zero</a></strong><br>
  ODOX reframes the model for self-documenting Odoo repositories
</p>
