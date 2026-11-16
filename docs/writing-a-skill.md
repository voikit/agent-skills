# Writing a Voikit skill

## The contract

```
skills/voikit-<job>/
  SKILL.md            required
  references/         generated copies from shared/ (never edit here)
  assets/             generated copies from templates/ (never edit here)
  scripts/            optional, Python standard library only
```

### Frontmatter

```yaml
---
name: voikit-call-center            # equals the folder name; lowercase, hyphens
description: >-                     # what it does + when to use it, up to 1024 characters
  Configure how calls reach a Voikit account: ... Use when someone says "set
  business hours", "after-hours", "who answers the phone" ..., in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected with the Call center section on (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: core                        # core or premium
---
```

The description is what makes an assistant pick the skill. Write the phrases people actually say. Keep to these keys; assistants reject frontmatter they do not know.

### Body, in this order

1. One paragraph: what this part of Voikit is.
2. "Read `references/operating-rules.md` first."
3. Use it when / hand off when (name sibling skills).
4. Before you start (which reads, in which order).
5. Workflow (numbered; each step: the goal, the tool, what the owner sees).
6. Decision rules (the judgement a good deployment specialist would apply).
7. Show the owner (the card or table).
8. Never.
9. If something goes wrong.
10. References.

## Writing rules

- Address the assistant: "Read", "Show", "Never". Call the Voikit customer "the owner" and their customers "the customer" or "the caller".
- Name tools in backticks, name only. Arguments and formats come from the live tool description.
- The freeze test: would this sentence still be true after the next product release? If not, replace it with a pointer to `capabilities`, `search_help` or `feature_availability`, or delete it.
- Decision rules beat procedures. "Knowledge before routing, because an operator without knowledge fails every test call" survives; a click path does not.
- Say what cannot be done and where it is done instead.
- Examples use invented businesses from different countries.
- ASCII only. No vendor names. No customer data.

## Scripts

A script earns its place when it replaces guessing with a check: text length and risky content, an hours table, a score. Keep it small, standard library only, with a docstring that shows the command. A skill must still work where code cannot run: describe the same check in a sentence.

## Shared material

Put text several skills need in `shared/` or `templates/`, add it to the map in `scripts/common.py`, and run `python3 scripts/sync_shared.py`. Skills cannot link outside their own folder, because a skill is installed and uploaded as one folder.

## Before you open a pull request

```
python3 scripts/sync_shared.py
python3 scripts/lint_skills.py
```

Then run the skill's scenarios from `evals/README.md` on a test account.
