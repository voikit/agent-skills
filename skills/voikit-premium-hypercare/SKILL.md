---
name: voikit-premium-hypercare
description: >-
  Look after a Voikit Premium customer after go-live: a daily review in the
  first week, a week-one report, a day-thirty review, then a monthly success
  review - finding wrong answers, lost calls and stuck work early, proposing
  fixes, tracking how often the owner had to correct the setup, and reporting
  in plain words. Use at steps 10 and 11 of a Premium deployment, or when
  someone says "run today's hypercare check", "write the week-one report",
  "prepare the 30-day review", "monthly review for this customer", "how is our
  Premium customer doing", in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected to the customer's account with the Reports, Call center and Knowledge base sections on (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: premium
---

# Voikit Premium hypercare

The first thirty days decide whether the customer trusts the setup. You look every day so that they do not have to, and you fix small things before they become complaints.

Read `references/operating-rules.md` first. The method of a review is the skill `voikit-reviews`; this skill adds the cadence, the targets and the reports of a Premium deployment.

## Use it when / hand off when

- Use it from the day after go-live.
- A fault -> `voikit-support`. A fix -> the area skill, with a `reason` that starts "Premium hypercare, day N:".

## Cadence

| When | What | Output |
|---|---|---|
| Days 1-7, daily | Yesterday's calls and chats; unanswered calls; questions the AI could not answer; hand-overs that failed; new learning proposals | A five-line note to the lead; fixes proposed the same day |
| Day 7 | The week as a whole | Week-one report for the owner |
| Days 8-30, twice a week | The same reads, lighter | Fixes; a note only when something changed |
| Day 30 | The month, against the targets | Day-30 report and a review call |
| Monthly after that | 30 days against the month before; learnings; features that now fit the business | Monthly report; renewal conversation before the term ends |

## The daily check

1. `reports_summary` for one day, `diagnose`.
2. `calls_list`: every unanswered call has a cause; find the pattern.
3. `learning_list_findings` and `memory_feedback`: what the AI could not answer, what the owner corrected, any breach of a hard rule.
4. `crm_list_tasks` overdue and unassigned; `conversations_list` unread.
5. `list_changes` with `all_sources`: what the owner or their team changed since yesterday. A setting the owner changed is their choice: do not change it back; ask if it looks like a mistake.
6. Propose fixes. Knowledge gaps and board hygiene first; routing and operator changes only with the lead's yes and the owner's approval.

A breach of a hard rule is handled the same day: find the call, the cause, the fix, and tell the lead before the owner hears it from a customer.

## Targets to report against

| Measure | Target |
|---|---|
| Hard-rule breaches | Zero |
| Questions the AI could not answer, week four against week one | Down by half |
| Settings the owner had to correct in thirty days | Fewer than 15 in 100 of the ones we set |
| Calls lost with no message taken | Trending to zero |
| Owner's rating at handover and at day 30 | 4.5 of 5 or better |

Measure what the tools show; where a target cannot be measured from the account, say so instead of estimating.

## The reports

Write in the owner's language, one page, numbers with their meaning.

- **Week one:** what happened (calls, chats, bookings or orders taken, hand-overs), what we fixed and why, what the operator learned, what we need from you, what we watch next.
- **Day 30:** the month against the targets above, the three most useful fixes, what the setup still does not handle, recommendations for the next quarter, and the decision on the deployment connection (end it, narrow it, or keep it for monthly reviews).
- **Monthly:** this month against last, measured results of approved learnings, one or two suggestions that fit the business, anything in the account that needs the owner (expiring connection, credit, a pending approval).

## Decision rules

- Fix the cause once, not the symptom daily: three similar missed questions mean one good Q&A with alternatives, not three patches.
- Learning proposals are the owner's to approve; bring them a recommendation for each (`learning_decide` records it).
- Do not widen your own access or the approval mode to move faster.
- Good news is reported with the same care as problems: a number, and what caused it.
- Suggest a new feature only when the review shows the need and `feature_availability` shows the account can use it.

## Show the lead

Daily: date, calls and how many were lost, top issue and its cause, fixes proposed (change ids), anything waiting on the owner.

## Never

- Skip a day in week one.
- Revert the owner's own change without asking.
- Include callers' names or full numbers in a report.
- Report a target as met without the number behind it.

## References

- `references/operating-rules.md`
