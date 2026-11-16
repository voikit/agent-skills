# Contributing

Thank you for helping assistants run Voikit accounts well.

## What we welcome

- Fixes to a skill that led an assistant to do the wrong thing (include the prompt and what happened).
- Clearer wording, better decision rules, missing "when things go wrong" cases.
- New playbooks for kinds of business, written from real setups.
- New skills for jobs the Voikit tools already support.

## The six rules

1. Behaviour over API: say how to think and in what order; let the account supply the facts.
2. Every change has a reason, a preview and a way back.
3. Ask only what cannot be found.
4. The owner approves what customers hear.
5. Honest about limits: if the tools cannot do it, say where it is done.
6. English and ASCII only; never name vendors; no secrets or customer data.

Details: [AGENTS.md](AGENTS.md) and [docs/writing-a-skill.md](docs/writing-a-skill.md).

## Pull requests

1. Edit sources (`skills/*/SKILL.md`, `shared/`, `templates/`), then run:
   ```
   python3 scripts/sync_shared.py
   python3 scripts/lint_skills.py
   ```
2. Test the skill on a real Voikit test account, in at least one assistant, with the scenarios in [evals/README.md](evals/README.md). Say in the pull request which assistant you used and what happened.
3. Add a line to `CHANGELOG.md` and bump the skill's `metadata.version`.
4. Use Conventional Commits and sign off your commits (`git commit -s`).

## Checklist

- [ ] Lint passes.
- [ ] The description says what the skill does and when to use it, with the phrases people actually say.
- [ ] Nothing in the skill becomes false when the product changes a limit, a label or a plan.
- [ ] Customer-facing text is always shown to the owner first.
- [ ] Tested on a real account; no real customer data in the pull request.
