# ODOX contract

**ODOX Contract Version:** `1.1.0`

## Purpose

ODOX keeps Odoo repositories understandable at the repository and module
levels. The root `AGENTS.md` owns agent workflow and repository-wide hazards;
each Odoo module's `README.md` is the primary shared technical contract.

## Core contract

- Treat an Odoo addon or module as the default durable documentation boundary.
- Keep one primary `README.md` per module. Make it concise, operational, and
  consistent with current code.
- Create a module `AGENTS.md` only for genuine agent-only hazards, generated
  artifact rules, non-obvious maintenance workflows, or local routing. Keep it
  supplemental; do not duplicate the README.
- Treat code as the source of truth when it disagrees with documentation,
  unless the discrepancy is a known bug or a regression; then make the
  exception explicit before changing documentation.
- Keep root instructions focused on agent workflow and hazards. Keep the root
  README human-facing.

## Read before editing

1. Read root `AGENTS.md`.
2. Identify the owning repository or module boundary.
3. For repository-wide work, read root `README.md` and relevant local docs.
4. For module work, read that module's `README.md`, then its optional
   `AGENTS.md`, before editing.
5. Repeat for every affected module; use the nearest README as the shared
   contract and the nearest AGENTS file as the agent supplement.

## Keep documentation current

Update the closest owning documentation after a meaningful change to purpose,
scope, responsibilities, structure, models, views, security, workflows,
dependencies, extension points, inputs, outputs, permissions, constraints,
side effects, artifacts, verification, or operational checks. Update root docs
when repository structure or module inventory changes.

Module READMEs normally cover purpose and business scope; key models, wizards,
views, security, and data; integrations and dependencies; extension seams;
verification; and important invariants. Review readability when a README grows
past roughly 300 lines; this is a soft threshold, not a cap.

## ODOX pass and documentation scope

Run an ODOX pass for changes to observable workflows, responsibilities,
structure, models, fields, wizards, views, reports, menus, scheduled actions,
security, integrations, dependencies, extension seams, inputs, outputs,
constraints, generated artifacts, verification, deployment expectations,
upgrade behavior, data lifecycle, documentation structure, or user
preferences. Formatting, comments, translations, internal refactors, and test
implementation alone do not require README changes unless documented behavior
changes.

Document only behavior a module owns or materially changes. Do not restate
generic Odoo conventions, unchanged inherited fields, cosmetic-only view
inheritance, or repository-wide workflow. State explicitly when a module has
no standalone menu rather than inventing one.

## Security, extensions, and upgrades

Security changes are meaningful. When changing ACLs, record rules, groups,
approval paths, sudo behavior, company visibility, ownership constraints, or
field/view visibility, update the owning README with the audience, major
permission boundaries, exceptional access, and ownership assumptions.

Document intentional extension seams such as inheritable methods, hooks,
mixins, action extension paths, configuration parameters, report customization,
integration interfaces, and expected overrides. Do not document incidental
implementation details as extension points.

When changing manifests, security XML, noupdate records, XML identifiers,
migrations, scheduled actions, templates, report actions, test demo data, or
operational defaults, assess installation, upgrade, and migration impact.
Document operational impact, migration expectations, and new administrator
responsibilities where applicable.

## Verification

Before finishing, verify that touched module READMEs match code. For repository
changes, verify root guidance, indexes, and local rules agree. Run existing
automated checks or make an explicit manual consistency review when none exist.
Use relevant entrypoints such as tagged tests, installation or upgrade checks,
report rendering, security smoke tests, scheduled-action checks, integration
validation, and migration validation. Do not duplicate generic root procedures
in module documentation.

## Precedence

This is a generic contract. Explicit instructions already present in the
repository take precedence. Preserve them during ODOX initialization and
updates; use this contract to fill only the reusable ODOX responsibility.
