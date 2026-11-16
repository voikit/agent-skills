# Notes for AI coding agents working on this repository

This repository holds Agent Skills for Voikit. A skill is read by an assistant at run time, so every sentence is an instruction to a model. Edit with that reader in mind.

## Rules

1. **English and ASCII only** in `skills/`, `shared/`, `templates/`, `docs/` and the README. The assistant translates at run time. The lint rejects other characters.
2. **Single source.** Never edit a file under `skills/*/references/`, `skills/*/assets/` or a synced script: edit the source in `shared/` or `templates/` and run `python3 scripts/sync_shared.py`. The map is in `scripts/common.py`.
3. **Real tools only.** A tool name in backticks must exist in `shared/tool-map.json`. Name tools; never copy their arguments or schemas (the assistant reads the live description). If a field or status is not a tool, add it to `scripts/lint-allow.txt`.
4. **Behaviour over API.** Do not write anything that the next product release makes false: counts, limits, plan contents, field formats, button labels. Send the assistant to `capabilities`, `search_help` or `feature_availability` instead.
5. **Never name vendors.** No phone-number suppliers, speech or voice engines, infrastructure or internal system names, anywhere, including comments and examples. The banned list is not in this repository on purpose: it is read from `.banned-terms.local` (git-ignored) or the `VOIKIT_BANNED_TERMS` secret.
6. **No secrets, no customer data.** No tokens, account addresses, real phone numbers or real customer names in files, issues or commits. Examples use invented businesses.
7. **One skill, one job.** A SKILL.md stays under 500 lines and reads top to bottom: when to use, before you start, workflow, decision rules, what to show, never, when things go wrong, references.
8. **Each skill folder must work alone.** No links to files outside the skill's own folder.
9. **Do not weaken the guardrails** in `shared/operating-rules.md` (approval, owner sign-off on customer-facing text, no retries of pending changes, red lines) without a maintainer's explicit request.

## Before you finish

```
python3 scripts/sync_shared.py
python3 scripts/lint_skills.py
```

Both must pass. When tools were added or renamed in the product, refresh the map first with `python3 scripts/export_tool_map.py` (see its help).

## Commits

Conventional Commits with the skill as scope: `feat(voikit-call-center): ...`, `fix(voikit-mcp): ...`, `docs: ...`, `chore: ...`. Bump `metadata.version` in a skill's frontmatter when its behaviour changes, and add a line to `CHANGELOG.md`.
