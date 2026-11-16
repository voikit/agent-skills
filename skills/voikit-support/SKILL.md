---
name: voikit-support
description: >-
  Troubleshoot a Voikit account and, when it is needed, work with Voikit's
  support team: run the diagnosis, find the cause of unanswered calls, missing
  rings, wrong routing or a stuck change, answer "how do I / where is" from
  Voikit's own help, and open, follow or close a support ticket in the
  person's own words. Use when someone says "calls are not being answered",
  "my phone does not ring", "something is broken", "how do I ... in Voikit",
  "where is ... in the panel", "contact Voikit support", "open a ticket",
  "what happened to my ticket", in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected; the Account and help tools are always on (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: core
---

# Voikit troubleshooting and support

Most problems have a cause the account itself can show. Find it first; open a ticket when the cause is on Voikit's side, when the fix needs Voikit's team, or when the person asks for support.

Read `references/operating-rules.md` first.

## Use it when / hand off when

- Use it for faults, "how do I" questions and tickets.
- Once the cause is known and it is configuration, fix it in that area's skill.
- "How is the account doing" with no fault -> `voikit-reviews`.

## Workflow

### A problem

1. Ask one question if needed: what did you expect, what happened, when, on which number or channel.
2. `diagnose`: the checklist of what usually stops calls from being answered - phone-system problems, numbers with no destination or switched off, queues nobody can answer, colleagues' unverified mobiles, many unanswered calls. Findings come most serious first, each with where to fix it.
3. Narrow it down with the matching read:

| Symptom | Read | Usual causes |
|---|---|---|
| Calls not answered at all | `numbers_list`, `callcenter_get_status` | Number without a destination, settings not live yet, plan period ended, no credit (`billing_get_balance`) |
| A colleague's phone does not ring | `account_overview` | Mobile not verified; colleague did not press the accept key; not a member of the group |
| Calls go to the wrong place | `callcenter_get_config` | Hours table, holiday, in-hours / after-hours destination |
| The operator says something wrong | `knowledge_test_answer`, `memory_get`, `agents_get` | Missing fact, wording does not match, rule missing, wrong knowledge selection |
| The operator hangs up instead of transferring | `agents_get`, `account_overview` | No transfer number, unverified mobile, test call placed from the transfer number itself |
| "It changed by itself" | `list_changes` with `all_sources` | A change by a colleague, the built-in assistant or another connection; `revert_change` if the owner wants |
| A change does nothing | `get_change` | Still waiting for approval, expired, or failed |
| The assistant is refused everywhere | `capabilities` | Connection paused, expired, read only, section off |

4. Say the cause in one sentence, the fix, and who does it. If it is yours to prepare, hand over to the area's skill.

### A "how do I / where is / can it" question

`search_help` first, `feature_availability` for "can it" and "is it in my plan". Answer only from what they return, with the page name as returned. If they do not settle it: `ask_ava`, Voikit's built-in assistant, which reads the same account and changes nothing (it counts against the account's assistant quota).

### A ticket

Open one only when the person asked for support or agreed to it.

1. `support_list_tickets`: is there already an open ticket about this? Then add to it with `support_reply_ticket` instead of opening another.
2. `support_departments`: pick the department. A locked department is not in the plan; say which plan opens it, do not pick another department to get around it.
3. Write the subject and body in the person's language from what they said, plus the facts you gathered: what was tried, exact error text, numbers, dates and times, what `diagnose` reported. Show it to them.
4. `support_create_ticket`. Give them the tracking code.
5. Follow up with `support_get_ticket`; pass on the person's answers with `support_reply_ticket`; when they say it is solved, `support_solve_ticket`.

When to go to a ticket without long digging: billing and invoices, plan changes or cancellation, a number that will not activate, anything `diagnose` reports as a platform-side problem, a suspected security issue.

## Decision rules

- Diagnose before guessing, and read before diagnosing a second time.
- Fix the cause, not the symptom: re-routing around an unverified mobile hides the problem.
- One problem, one ticket. No duplicates, no "any update?" replies within the response time of the plan.
- Never put passwords, tokens or one-time codes in a ticket. Mask customers' phone numbers unless the ticket is about that exact call.
- Voikit's internals (suppliers, engines, servers) are not yours to speculate about, even when a fault seems to be there. Describe the symptom and let support name the cause.

## Show the owner

Cause -> fix -> who -> when it will be confirmed. For a ticket: the tracking code, the department, and what happens next.

## Never

- Open a ticket the person did not ask for.
- Promise a response time; read it from the ticket or the help.
- Mark a ticket solved before the person says so.

## References

- `references/operating-rules.md`, `references/panel-only.md`
