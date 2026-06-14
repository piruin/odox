# ODOX framework

- ODOX is a self-documenting documentation contract for Odoo repositories.
- Agents must follow this file before editing code or durable documentation.

## Purpose

- Keep Odoo repositories understandable at the repo level and at the module level.
- Make module `README.md` files the primary local contract for both humans and AI agents.
- Keep `AGENTS.md` focused on agent-specific workflow, routing, and hazards that do not belong in a human-facing README.
- Encourage documentation that evolves alongside the codebase instead of becoming a separate maintenance burden.

## Core Contract

- The root `AGENTS.md` is mandatory and owns repo-wide workflow, indexing, and documentation maintenance rules.
- The default durable boundary is the Odoo module or addon, not every nested folder.
- Each module should have one primary `README.md` that reflects the current code in that module.
- Module `AGENTS.md` files are optional and additive. They may refine local agent behavior but must not duplicate or contradict
  the module README or this root contract.
- When code and documentation disagree, treat code as truth unless the discrepancy is clearly a regression or known bug

## Read Before Editing

1. Read the root `AGENTS.md`.
2. Identify whether the work is repo-wide or contained within one or more Odoo modules.
3. For repo-wide work, read the root `README.md` and any directly relevant local docs.
4. For module work, read that module's `README.md` first.
5. If the module also has an `AGENTS.md`, read it after the module README and before editing.
6. If multiple modules are affected, repeat the read path for each affected module.
7. Use the nearest applicable module README as the local shared contract and the nearest applicable `AGENTS.md` as the local
   agent supplement.

## ODOX Pass

Every meaningful change requires an ODOX pass before the task is complete.

A change is considered meaningful if it alters:

- observable behavior or user workflows
- business responsibilities or owned scope
- durable structure, models, fields, wizards, views, reports, menus, or scheduled actions
- security rules, access rights, groups, approval paths, record rules, or visibility constraints
- integrations, dependencies, extension seams, or configuration contracts
- required inputs, outputs, permissions, constraints, side effects, or generated artifacts
- verification commands, test entrypoints, operational checks, or deployment expectations
- migration behavior, upgrade considerations, or data lifecycle assumptions
- documentation structure, including README.md or AGENTS.md creation, deletion, move, rename, or index contents
- user preferences about behavior, communication, process, organization, or quality

The following changes do not automatically require README updates unless they affect documented behavior:

- code formatting
- comment updates
- translation corrections
- purely internal refactors with no observable impact
- test implementation changes that do not change verification expectations

## Update After Editing

Every meaningful change requires an ODOX pass before the task is done.

Update the closest owning documentation when a change affects:

- purpose, scope, ownership, or responsibilities
- durable structure, models, views, security, workflows, dependencies, or extension points
- required inputs, outputs, permissions, constraints, side effects, or artifacts
- verification commands, test entrypoints, or operational checks
- user preferences about behavior, communication, process, organization, or quality
- documentation structure, including `README.md` or `AGENTS.md` creation, deletion, move, rename, or index contents

Update the root docs when repo-wide structure or module inventory changes. Update a module README when local code behavior or
structure changes. Update a module `AGENTS.md` only when agent-specific local instructions change.

## Module Documentation Rules

- Default to README.md as the primary contract inside each Odoo module.
- Keep module READMEs operational, technical, and aligned with current code.
- Avoid marketing copy as the main content.
- Document only what the module owns or materially changes.

A module README should usually cover:

- purpose and business scope
- owned models and significant model extensions
- wizards, reports, scheduled actions, and menus introduced by the module
- views that introduce workflows, validation paths, extension seams, or notable user interactions
- security areas and permission boundaries
- integration points, dependencies, and extension seams
- verification or test entrypoints when they exist
- human-relevant hazards, invariants, and upgrade considerations

A module README should document only the models, menus, views, scheduled actions, security rules, reports, and integrations that
the module introduces or materially changes.

Do not document:

- generic Odoo conventions
- inherited fields that behave exactly as standard Odoo behavior
- cosmetic view inheritance such as label changes, sequence adjustments, or styling-only modifications
- repo-wide workflows already covered by root documentation

If a module has no standalone menu, state that explicitly rather than inventing a menu structure.

## Security Documentation Rules

Security-related changes are always considered meaningful.

Whenever a module changes:

- access rights (ir.model.access)
- record rules (ir.rule)
- security groups
- approval workflows
- sudo behavior
- cross-company visibility
- ownership constraints
- field or view visibility restrictions

review and update the owning module README.

Module READMEs should provide a concise security summary describing:

- who can access the module
- major permission boundaries
- exceptional access behavior
- important ownership assumptions

## Extension Seam Rules

When a module intentionally exposes extension points, document them.

Examples include:

- methods intended for inheritance
- hooks or callback patterns
- mixins
- automated action extension paths
- configuration parameters
- report customization points
- integration interfaces
- dependency injection mechanisms
- expected override patterns

Document extension seams only when they are intentional and useful for maintainers.

## Verification Rules

Before completing meaningful work in a module:

- verify that the module README still matches the current code
- run existing automated checks when available
- perform a manual consistency review when no automated checks exist

Examples of verification entrypoints include:

- tagged Odoo tests
- module installation checks
- module upgrade checks
- report rendering validation
- security smoke tests
- scheduled action verification
- integration validation procedures
- data migration validation steps

Do not duplicate generic verification procedures already owned by root documentation.

## Odoo Upgrade Awareness

When changing any of the following:

- **manifest**.py
- security XML files
- noupdate records
- XML identifiers
- migration scripts
- scheduled actions
- mail templates
- report actions
- demo data relied upon by tests
- configuration defaults with operational impact

consider whether installation, upgrade, or migration behavior changes.

If upgrade behavior changes:

- document operational impact
- document migration expectations when appropriate
- document new administrator responsibilities when applicable

## Optional Module AGENTS.md Rules

- Create a module `AGENTS.md` only when at least one of these is true. when in doubt, don't:
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
- Prefer updating existing sections instead of creating overlapping explanations.
- Put broad workflow rules in the root `AGENTS.md`.
- Put module behavior and code-facing context in the module `README.md`.
- Put agent-only constraints in optional module `AGENTS.md`.
- Delete stale or contradictory text immediately instead of explaining history.

## Verification Before Completion

Before completing meaningful work:

### For module-level work:

- confirm the affected module README still reflects the implemented behavior
- verify that documentation accurately describes owned responsibilities and constraints

### For repo-wide work:

- confirm that root guidance and module guidance remain consistent
- verify that module inventories and documentation indexes remain accurate

## User Preferences

- Prefer module-level `README.md` as the main shared contract for humans and agents.
- Keep the root model hybrid: root `AGENTS.md` for repo-wide agent workflow, root `README.md` for human-facing overview.
- Keep module `AGENTS.md` rare and justified by real agent-only needs.
- Prefer documentation that helps future maintainers understand why a module exists, how it behaves, where it can be extended,
  and how it should be verified.

## Child DOX Index

- Root scope currently owns the entire repository unless otherwise documented.
- Human-facing repository overview: README.md
- The root AGENTS.md maintains the inventory of any module-level AGENTS.md files that exist.
- Only actual module-level AGENTS.md files should be listed here.

Expected structure:

- repository root: AGENTS.md and README.md
- each Odoo module: README.md
- exceptional modules only: supplemental AGENTS.md
