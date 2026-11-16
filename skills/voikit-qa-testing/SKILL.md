---
name: voikit-qa-testing
description: >-
  Test a Voikit setup before it meets real customers and decide go / no-go:
  configuration checks with the read tools, answer tests on the most frequent
  questions, a script of persona test calls for a person to place, a scored
  go-live checklist and a fix list. Use when someone says "test my agent", "is
  it ready to go live", "run the go-live checklist", "write test calls for my
  operator", "check before we connect the number", "why did the test call
  fail", in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected; read access is enough for most checks (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: core
---

# Voikit QA and go-live testing

Nothing goes live untested. You check what can be checked with tools, script what a person must test by phone, score the result and say plainly whether it is ready.

Read `references/operating-rules.md` first. The checklist is `assets/golive-checklist.md`.

## Use it when / hand off when

- Use it at the end of any setup and after any change to greetings, rules, routing or knowledge.
- When a test fails, the fix belongs to that area's skill; come back and retest only what failed.

## Before you start

1. `capabilities`, `account_overview`.
2. Know what was agreed: the answering mode, the greeting, the hard rules, the hand-over cases (`memory_get`, `agents_get`, `callcenter_get_config`).

## Workflow

1. **Configuration checks (you).** Lines P1 to P8 of the checklist, each with its read tool. `diagnose` and `callcenter_get_status` must come back clean.
2. **Answer tests (you).** The twenty questions customers ask most (from `business_profile_get`, the Q&A list and the owner). `knowledge_test_answer` on each; pass means correct, short and from the right source. Each test counts as one AI chat message: run the list once, fix, retest the failures only.
3. **Flows and rules (you).** `flows_validate` for each active flow; `automations_test` with sample comments if Instagram rules exist.
4. **Test-call script (for a person).** Write the calls in the owner's language, one persona per call, each with: who is calling, what they say first, what they push on, and the pass condition. Cover at least:
   - a frequent question, asked colloquially
   - a question that is not in the knowledge
   - each hard rule, with a caller who insists ("just give me a discount")
   - "let me talk to a person" in hours, with the colleague answering
   - the same with the colleague not answering
   - a call after hours, and one on a holiday if it can be simulated
   - a booking, order or request, start to finish
   - a caller who is vague, one who is upset, one who talks over the operator
   - for regulated fields: a request for advice the operator must refuse
5. **How to place them.** A person calls from the panel's test phone or a real phone that is not registered as a colleague or as the transfer number. Plan at least ten calls.
6. **Read the results.** After the calls, `calls_list` and the CRM (`crm_list_tasks`): were the calls recorded, summarised, and turned into tasks with the right follow-up operator.
7. **Score.** Record every line as pass, fail or not applicable. With code execution: `python3 scripts/scorecard.py results.json`. Otherwise count by hand: go-live needs every "must" line passing and at least 90 percent of the applicable lines.
8. **Fix list.** For each failure: what happened, what should happen, where the fix is, who does it. Retest those lines only.

## Decision rules

- A failed hard-rule test blocks go-live, whatever the overall score.
- A transfer that ends in a goodbye instead of a real hand-over is a failure, even if the operator was polite.
- "Mostly right" is a fail for prices, hours, addresses and policies.
- Test the way customers talk, not the way the knowledge is written.
- You cannot place calls. Never report a call test as passed without the person's result.
- Test changes go through the same approval path as any change; testing is not a reason to widen the approval mode.

## Show the owner

1. The verdict in one line: ready / ready after these fixes / not ready.
2. The score and the checklist with pass or fail per line.
3. The fix list.
4. What was not tested and why.

## Never

- Mark a line passed because the configuration "looks right".
- Connect the phone number or announce go-live while a "must" line fails.
- Use real customers' numbers for test calls.

## If something goes wrong

- The test call does not reach the operator -> `numbers_list` (where would a call go right now), `diagnose`.
- The transfer test fails -> the caller's phone is the transfer number itself, or the colleague's mobile is unverified.
- The answer is right in the answer test and wrong on the phone -> that operator's knowledge selection (`voikit-ai-agents`).

## References

- `references/operating-rules.md`
- `assets/golive-checklist.md`
- `scripts/scorecard.py` - optional scoring of the checklist
