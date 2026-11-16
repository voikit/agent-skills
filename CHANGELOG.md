# Changelog

All notable changes to the skills. Versions follow semantic versioning.

## 0.1.1 - 2026-11-16

Releases that install without surprises.

- A release now offers one download for every app: `voikit.zip`, with its checksum. The archive of all folders is gone; upload pages refused it.
- The build checks every zip against the rules of the upload pages (one folder, one `SKILL.md`, name, description, frontmatter keys, standard folders) and stops the release when one fails.
- Inside `voikit.zip` the guides moved into `references/`, so the skill uses only the standard folders of the Agent Skills format.
- `voikit.zip` carries optional metadata for ChatGPT and Codex (`agents/openai.yaml`): a display name, a starter prompt and the Voikit connector it works with.
- The skill knows its version and where the newest file is.
- Release notes are written from this changelog, with install and update steps at the top.
- `docs/releasing.md`: the steps and the checks of a release.

## 0.1.0 - 2026-11-16

First set of skills.

- Core: `voikit-mcp`, `voikit-onboarding`, `voikit-ai-agents`, `voikit-knowledge-base`, `voikit-business-memory`, `voikit-call-center`, `voikit-crm-followups`, `voikit-conversations`, `voikit-instagram-automation`, `voikit-flows-forms`, `voikit-appointments`, `voikit-campaigns`, `voikit-qa-testing`, `voikit-reviews`, `voikit-support`, `voikit-industry-playbooks`.
- Premium deployment: `voikit-premium-onboarding`, `voikit-premium-intake`, `voikit-premium-scenario-design`, `voikit-premium-handover`, `voikit-premium-hypercare`.
- Shared operating rules, the six answering modes and the panel-only list, copied into each skill.
- Templates: business brief, proposal, handover document, go-live checklist.
- Optional tools: `text_check.py`, `hours_check.py`, `scorecard.py`.
- Repository scripts: lint, sync, release build, tool-map export.
- One-file install: `voikit.zip`, a single skill named `voikit` that carries every guide and walks the person through connecting, step by step.
- Install straight from GitHub: paste-in prompts for Claude and ChatGPT; the one-file skill reads its guides from the repository when they are not installed with it.
- The Claude Code plugin now brings the Voikit connector with it.
- Release workflow template (`docs/ci/release.yml`): a version tag publishes the zips.
