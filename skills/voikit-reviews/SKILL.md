---
name: voikit-reviews
description: >-
  Review how a Voikit account is performing and turn the findings into fixes:
  a daily or weekly read of calls, the inbox, the CRM and appointments,
  unanswered calls and their causes, questions the AI could not answer, what
  the assistants learned from corrections, and a short list of concrete
  improvements. Use when someone says "how did yesterday / last week go",
  "weekly review", "what should I fix", "why are calls unanswered", "what are
  customers asking that we do not answer", "show me what the AI learned", "give
  me a report", in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected with the Reports, Call center and Knowledge base sections on; read access is enough to review (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: core
---

# Voikit reviews

A review answers three questions: what happened, what is going wrong, and what should change. It ends with at most five fixes, most serious first.

Read `references/operating-rules.md` first.

## Use it when / hand off when

- Use it for a daily check, a weekly review, a monthly look, or after a go-live.
- Applying a fix belongs to that area's skill.
- A fault (calls not connecting at all) -> `voikit-support`.

## Before you start

1. `capabilities`. Reports weigh more than ordinary calls against the daily ceiling: read once, then work from what you have.
2. Agree the period: yesterday, the last 7 days, the last 30.

## Workflow

1. **Numbers.** `reports_summary` for the period: calls by outcome and the reasons calls went unanswered, the inbox (active, unassigned, unread), the CRM (open, overdue, created, closed), appointments, and what assistants did.
2. **Health.** `diagnose`: anything that stops calls from being answered, most serious first.
3. **Unanswered calls.** `calls_list`: why they were not answered and the latest ones. Look for a pattern: a time of day, a day of the week, one number, one colleague.
4. **What the AI could not answer.** `learning_list_findings` for proposals waiting for the owner: a Q&A to add, a charter rule, a policy, a tone change, a hand-over topic. `memory_feedback` shows the raw signals: the owner's corrections, thumbs-down, unanswered questions, charter breaches.
5. **Work that is stuck.** `crm_list_tasks` overdue and unassigned; `conversations_list` open and unread.
6. **Write the review** (format below).
7. **Decide.** Walk the owner through the learning proposals one by one and record each with `learning_decide`. For other fixes, ask which to prepare, then hand each to its skill. Never bundle fixes into one big change.

## Cadence

| When | Read | Aim |
|---|---|---|
| Daily, in the first week after go-live | steps 1 to 4 for yesterday | Catch wrong answers and lost calls early |
| Weekly | all steps for 7 days | Three to five fixes |
| Monthly | all steps for 30 days, compared with the month before | Trends, and whether last month's fixes worked |

Approved learnings are measured by Voikit after two weeks (better, same or worse; a worse one is taken back on its own). Report those results in the next review instead of guessing whether a fix helped.

## Decision rules

- Lead with lost customers: unanswered calls and unanswered messages come before everything else.
- A number without a cause is not a finding. "32 unanswered calls" becomes "32 unanswered calls, 26 of them between 13:00 and 14:30 when nobody is at the desk and the after-hours path does not apply".
- One example beats a statistic: quote one anonymised case per finding. Never include callers' names or full numbers in a report.
- A question asked three times in a week deserves a Q&A.
- Do not recommend a paid upgrade as a fix unless `feature_availability` shows the plan is the actual blocker.
- Compare with the previous period when the tools give you both; otherwise say there is no baseline yet.

## Show the owner

1. **In one line:** how the period went.
2. **What went well:** two or three points with numbers.
3. **What is wrong:** most serious first, each as symptom -> cause -> fix -> who does it (you can prepare it / the owner in the panel).
4. **Waiting for your decision:** learning proposals and pending changes (`list_changes`).
5. **Next review:** when, and what you will check then.

## Never

- Apply a learning proposal or a fix as part of "the review" without the owner choosing it.
- Present a guess about cause as a fact; say "likely" and what would confirm it.
- Quote customers' personal details.

## If something goes wrong

- The daily ceiling is reached mid-review -> report what you have, say what is missing, finish tomorrow.
- Numbers look impossibly low -> the period, the time zone, or a section that is off for this connection.

## References

- `references/operating-rules.md`
