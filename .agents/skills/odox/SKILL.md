---
name: odox
description: Maintain the ODOX documentation contract in an Odoo repository. Use for ODOX status, initialization, contract updates, structural or semantic documentation checks, and creating or maintaining module README.md files. Trigger for `/odox`, `odox init`, `odox update`, `odox check`, `odox document`, or equivalent natural-language requests.
---

# ODOX

Use this skill as an installer and maintenance workflow, never as a runtime
dependency. An initialized repository must remain understandable when this
skill is unavailable.

Read [the canonical contract](references/contract.md) before `init`, `update`,
`check`, or `document`. Read [the operation protocol](references/operations.md)
for exact storage, safety, and scope rules.

## Invocation

Use slash syntax where the host supports it; otherwise accept the equivalent
natural-language request.

| Invocation | Effect |
| --- | --- |
| `/odox` | Read-only status and next-action hint. |
| `/odox init` | Add the managed root bootstrap and local editable contract. |
| `/odox update [upstream|local]` | Semantically reconcile a local contract with a new upstream contract. Default: `upstream`. |
| `/odox check [fast|full|changed|module ...]` | Validate structure, then optionally audit documentation scope. Default: `fast`. |
| `/odox document [all|changed|module ...]` | Deliberately create or maintain module READMEs. |

Reject `full` combined with named modules. Always include fast root validation
in module-scoped checks. Do not fetch, install, write, or reorganize files for
a bare status request.

## Agent rules

1. Find the Git repository root and read its root instructions before acting.
2. Preserve explicit repository instructions. They override this reusable
   contract when the two disagree.
3. Make network access only for an explicit `update upstream`; refresh only the
   globally installed `odox` skill. `update local`, status, check, and document
   work without network access.
4. Perform updates as a semantic three-way comparison of old upstream base,
   editable local contract, and new upstream contract. Apply only independent
   changes automatically. Explain a same-policy conflict and ask the maintainer
   to decide; never hide it with a line merge.
5. Advance the base snapshot only after the complete merged local contract is
   accepted. Leave it unchanged after a conflict, interruption, or rejection.
6. Derive documentation from inspected code. Preserve useful curated README
   structure and prose, correct evidence-backed drift, and ask before changing
   ambiguous business meaning.

## Package release

When changing this skill, update the contract version in
`references/contract.md` and `references/contract-version.txt` together. Run
the package tests and validator named in the source repository instructions.
