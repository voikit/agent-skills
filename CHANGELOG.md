# Changelog

All notable changes to the skills. Versions follow semantic versioning.

## 0.1.0 - unreleased

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
