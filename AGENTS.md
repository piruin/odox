# ODOX framework

- ODOX is a self-documenting documentation contract for Odoo repositories.
- Agents must follow this file before editing code or durable documentation.

## Purpose

- Keep Odoo repositories understandable at the repo level and at the module level.
- Make module `README.md` files the primary local contract for both humans and AI agents.
- Keep `AGENTS.md` focused on agent-specific workflow, routing, and hazards that do not belong in a human-facing README.

## Core Contract

- The root `AGENTS.md` is mandatory and owns repo-wide workflow, indexing, and documentation maintenance rules.
- The default durable boundary is the Odoo module or addon, not every nested folder.
- Each module should have one primary `README.md` that reflects the current code in that module.
- Module `AGENTS.md` files are optional and additive. They may refine local agent behavior but must not duplicate or contradict the module README or this root contract.
- When code and documentation disagree, treat the current code as the source of truth and bring the documentation back into sync.

## Read Before Editing

1. Read the root `AGENTS.md`.
2. Identify whether the work is repo-wide or contained within one or more Odoo modules.
3. For repo-wide work, read the root `README.md` and any directly relevant local docs.
4. For module work, read that module's `README.md` first.
5. If the module also has an `AGENTS.md`, read it after the module README and before editing.
6. If multiple modules are affected, repeat the read path for each affected module.
7. Use the nearest applicable module README as the local shared contract and the nearest applicable `AGENTS.md` as the local agent supplement.

Do not rely on memory. Re-read the applicable ODOX chain in the current session before editing.

## Update After Editing

Every meaningful change requires an ODOX pass before the task is done.

Update the closest owning documentation when a change affects:

- purpose, scope, ownership, or responsibilities
- durable structure, models, views, security, workflows, dependencies, or extension points
- required inputs, outputs, permissions, constraints, side effects, or artifacts
- verification commands, test entrypoints, or operational checks
- user preferences about behavior, communication, process, organization, or quality
- documentation structure, including `README.md` or `AGENTS.md` creation, deletion, move, rename, or index contents

Update the root docs when repo-wide structure or module inventory changes. Update a module README when local code behavior or structure changes. Update a module `AGENTS.md` only when agent-specific local instructions change.

## Module Documentation Rules

- Default to `README.md` as the primary contract inside each Odoo module.
- Keep module READMEs operational, technical, and aligned with current code. Avoid marketing copy as the main content.
- A good module README usually covers:
  - purpose and business scope
  - main models, wizards, views, security areas, and data files
  - integration points, dependencies, and extension seams
  - verification or test entrypoints when they exist
  - human-relevant hazards or invariants
- Use 300 lines as a soft readability threshold for module READMEs.
- If a module README grows much beyond 300 lines, review whether to split module responsibilities, trim stale prose, or move agent-only detail into an optional module `AGENTS.md`.
- If a module cannot stay understandable near that threshold, treat it as a signal that the module boundary or documentation structure needs reconsideration.

## Optional Module AGENTS.md Rules

- Create a module `AGENTS.md` only when at least one of these is true:
  - the module has agent-specific edit hazards that do not belong in the README
  - the module has a non-obvious maintenance workflow or generated-artifact rule
  - the module has local constraints that would clutter the human-facing README
  - the module has multiple subareas that need explicit agent routing
- Keep module `AGENTS.md` files short and supplemental.
- Do not restate the full README in `AGENTS.md`.
- No deeper child `AGENTS.md` files should be created inside a module unless the user explicitly wants an exception.

## Style

- Keep docs concise, current, and operational.
- Prefer durable facts over intentions or roadmap language.
- Put broad workflow rules in the root `AGENTS.md`.
- Put module behavior and code-facing context in the module `README.md`.
- Put agent-only constraints in optional module `AGENTS.md`.
- Delete stale or contradictory text immediately instead of explaining history.

## Verification

- Before finishing meaningful work in a module, verify that the module README still matches the current code.
- Before finishing repo-wide documentation changes, verify that root guidance, module rules, and indexes agree with each other.
- When an existing automated check exists, run it. When none exists, perform a manual consistency review of the touched docs and code.

## User Preferences

- Prefer module-level `README.md` as the main shared contract for humans and agents.
- Keep the root model hybrid: root `AGENTS.md` for repo-wide agent workflow, root `README.md` for human-facing overview.
- Treat 300 lines as a soft README review threshold, not a hard cap.
- Keep module `AGENTS.md` rare and justified by real agent-only needs.

## Child DOX Index

- Root scope: this file currently owns the entire repository.
- Human-facing root overview: [README.md](C:\Users\pirui\Workspace\piruin\odox\README.md)
- No child `AGENTS.md` files exist yet in this starter repository.
- Expected adopter structure:
  - repo root: root `AGENTS.md` plus root `README.md`
  - each Odoo module: module `README.md`
  - exceptional modules only: supplemental module `AGENTS.md`
