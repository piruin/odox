# ODOX operation protocol

## Repository layout after initialization

Initialize from the Git repository root. Use these exact repository-local
paths so an initialized repository is self-contained:

```text
AGENTS.md
.agents/odox/
  contract.md           # editable local ODOX contract
  .upstream-base.md     # exact upstream contract used as merge base
  metadata.json         # schema, base version, and source metadata
```

The root `AGENTS.md` contains this bounded section exactly once:

```markdown
<!-- odox:managed:start -->
## ODOX

This repository uses the editable local ODOX contract at
`.agents/odox/contract.md`. Read it with this repository's instructions before
editing durable code or documentation. Explicit repository instructions take
precedence over the generic ODOX contract.
<!-- odox:managed:end -->
```

The markers are intentionally hidden from normal document structure. Do not
find the section by heading or rewrite surrounding instructions.

## Status

Read only. Inspect the markers, local contract, base snapshot, and metadata;
compare local base version with the installed skill version without fetching.
Report initialization state, both versions, module counts or known README gaps,
and a useful `document` hint when gaps exist. Do not create files or invoke
network commands.

## Initialize

1. Read existing root instructions, if any.
2. If the managed markers are absent, append the bounded bootstrap without
   reorganizing or replacing existing content. If they are present, preserve
   the entire root file unchanged.
3. Copy the installed canonical `contract.md` into both the editable local
   contract and `.upstream-base.md`.
4. Write metadata with `schema_version`, `base_contract_version`, and the
   installed skill source/version. Do not infer a version from prose.
5. Report missing module README gaps only; never create or rewrite them during
   initialization.

Initialization is idempotent. Stop and ask before overwriting a pre-existing
local contract or base snapshot that is not a coherent initialized state.

## Update

`update upstream` is the only operation allowed to use the network. Refresh
only ODOX, for example:

```text
npx skills add piruin/odox@odox -g -a codex
```

Then use the newly installed canonical contract. `update local` uses the
already installed copy and must not contact a remote service.

Perform a semantic three-way comparison of old base, editable local, and new
upstream as policies. Classify each change by responsibility or rule, not line
position:

- Upstream-only change: apply it.
- Local-only change: preserve it.
- Same semantic result: retain one clear statement.
- Independent changes in the same file: combine them.
- Competing changes to the same rule, ownership, or policy: explain the
  conflict and pause for a maintainer decision.

After acceptance, write the merged local contract and replace the base snapshot
with the exact new upstream contract, then update metadata. Do not advance the
base snapshot after interruption, rejected change, or unresolved conflict.

## Check

`fast` validates managed markers, the local contract, base snapshot, metadata
schema/version, and their structural consistency. It is the default.

`full` runs fast validation plus a semantic audit of root instructions and all
Odoo modules. `changed` runs fast validation plus modules inferred from current
Git changes. `module <path...>` runs fast validation plus only explicitly named
modules. Reject `full` with module paths as redundant.

A semantic audit verifies documentation against inspected code: owned behavior,
models, views, security, dependencies, extension seams, tests, and invariants.
Report missing or stale facts with evidence; do not change files during check.

## Document

Use `all`, `changed`, or `module <path...>` scopes. Inspect module manifests,
models, views, security data, reports, scheduled actions, and tests before
writing. Create missing README files from verified behavior. Update existing
files in place, retaining useful organization and prose. Ask before resolving a
contradiction that would alter or invent business meaning.

`document` is deliberate and may write documentation; it is never an implicit
side effect of `init`, status, or check.
