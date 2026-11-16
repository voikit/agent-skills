---
name: voikit-campaigns
description: >-
  Prepare, monitor and safely stop outbound call campaigns on a Voikit
  account: explain how a campaign is started and reviewed, check a campaign's
  state and results, pause or stop one at once, and help the owner prepare a
  compliant audience, script and schedule. Use when someone says "start an
  outbound campaign", "call my customer list", "pause the campaign", "stop
  calling", "how is the campaign doing", "why was my campaign rejected", "what
  hours can I call", in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected with the Campaigns section on (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: core
---

# Voikit outbound campaigns

A campaign has an AI operator call a list of people for one purpose. Because unwanted calls harm people and can get a business's lines blocked, every campaign is reviewed for compliance before it may run, and the owner confirms the run personally.

Read `references/operating-rules.md` first.

## What an assistant can and cannot do

- Can: read campaigns, explain the process, help prepare, pause, stop.
- Cannot: start a campaign, in any approval mode. `campaigns_how_to_start` returns the exact steps and the campaign's current compliance state to relay to the owner.

## Use it when / hand off when

- Use it for anything about calling a list.
- One call to one customer about their own task -> `voikit-crm-followups`.
- The operator that will make the calls -> `voikit-ai-agents`.

## Before you start

1. `capabilities`.
2. `campaigns_list`; for one campaign `campaigns_get` (script or goal, counts, status).

## Workflow

### Help prepare

1. Purpose in one sentence, and the kind: a service call the people expect (an appointment, a delivery, a renewal they asked about) or promotion. Promotion carries more risk and more conditions.
2. Audience: where the numbers came from and what those people agreed to. If the owner cannot say, stop here and explain why.
3. Script: who is calling, why, and how to opt out, in the first sentences. Honest about being an AI operator when asked.
4. Schedule: inside the calling hours of the destination country. Voikit refuses to save a schedule outside them; do not help work around that.
5. The owner creates the campaign in the panel and sends it for review. Sending for review and running a promotional campaign need the owner's one-time code. There is no "run now" before review.
6. Relay `campaigns_how_to_start` so the owner sees exactly what is left.

### Monitor

`campaigns_get`: reached, not reached, outcomes. Compare with the purpose and report in three lines: what happened, what it means, what to change. Results that create CRM tasks are worked in `voikit-crm-followups`.

### Pause or stop

- `campaigns_pause` applies at once in every mode. Use it the moment something looks wrong: complaints, a wrong script, wrong numbers, calls at a bad hour.
- `campaigns_stop` ends the campaign for good and cannot be undone. Confirm with the owner unless harm is ongoing; when in doubt, pause.

## Decision rules

- Pause first, ask second, when people are being called wrongly. Pausing is always safe.
- A list bought or scraped is not consent. Say so plainly.
- People who asked not to be called stay off every list.
- Imports are done by the owner in the panel (paste or a spreadsheet file).
- If a campaign was rejected in review, read the reason back in plain words and help fix that reason only.

## Show the owner

- Before: a readiness card - purpose, audience and its consent basis, the opening lines of the script, the schedule, what review still needs.
- During: counts and outcomes, and one recommendation.
- After a pause or stop: what was halted, the change id, how many calls were left.

## Never

- Suggest a way to run a campaign without review or outside calling hours.
- Describe a promotional campaign as a service call.
- Promise results (answer rates, sales).
- Stop a campaign for good on a guess.

## If something goes wrong

- "It will not start" -> `campaigns_how_to_start` shows the missing step: review pending, rejected, code not entered, schedule outside hours, or no credit.
- Complaints from people called -> pause, then review the audience and script with the owner; consider `leads_opt_out` or a do-not-call mark for those people.

## References

- `references/operating-rules.md`
