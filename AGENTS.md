# AGENTS.md — portfolio-manual

This is a generated public catalog. Keep its scope intentionally narrow:
only public project names, links, and broad categories belong here.

- Do not add local paths, deployment details, private project names, or source
  repository operational guidance.
- Generated catalog files are updated from their reviewed source; use an issue
  for corrections instead of editing them in place.
- Keep `CHATHISTORY.md` and `REFS-LOCAL.md` local-only and untracked.
- Run `pre-commit run --all-files` and `python3 scripts/check_catalog.py`
  before publishing changes.

## Sudo Boundary

Agents cannot run `sudo` in this environment. Finish non-elevated work and
give the user the exact elevated command to run if one is required. Do not
claim an elevated change was applied until the user shares the result.

## Local CI Verification

Before every push, run:

```bash
pre-commit run --all-files
python3 scripts/check_catalog.py
```

## Agent Memory

- `CHATHISTORY.md` is the local-only handoff log and must stay gitignored.
- `LESSONSLEARNED.md` holds tracked durable lessons for this catalog.
- `REFS-LOCAL.md` holds local-only references; `REFS-PUBLIC.md` holds public
  references.

## Portfolio Standards Reference

Portfolio-wide governance and repository baseline rules live in
`./util-repos/traction-control`. Keep this repository's generated catalog
limited to its reviewed public allowlist.
