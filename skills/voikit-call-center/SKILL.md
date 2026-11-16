---
name: voikit-call-center
description: >-
  Configure how calls reach a Voikit account: business hours and holidays, who
  answers first (the AI operator, the team, a phone menu or smart reception),
  ring groups and queues, what happens after hours and when nobody answers,
  voicemail notices, recording, and where each phone number goes. Use when
  someone says "set business hours", "after-hours", "who answers the phone",
  "add a holiday", "ring my team first", "create a queue / ring group",
  "voicemail", "record calls", "route my number", "calls are not reaching us",
  in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected with the Call center section on (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: core
---

# Voikit call center

The call center decides where every incoming call goes: to whom during business hours, to whom after hours and on holidays, and where next when nobody picks up.

Read `references/operating-rules.md` first. The six answering modes are in `references/answering-modes.md`.

## Use it when / hand off when

- Use it for hours, routing, ring groups, queues, voicemail, recording.
- What the AI operator says or when it transfers -> `voikit-ai-agents`.
- Calls not answered and you do not know why -> start with `diagnose` here, then `voikit-support`.

## Before you start

1. `capabilities`, then `callcenter_get_config`: hours tables with their destinations, numbers and where each goes, queues, ring groups, voicemail boxes, holidays, extensions, operators, recording. It carries the ids the write tools take.
2. `callcenter_get_status` and `numbers_list` ("where would a call go right now, and why").
3. `account_overview`: colleagues' phone users and unverified mobiles.
4. `business_profile_get` for hours, team size and the owner's answering preference.
5. More than three changes ahead -> `save_safe_point`.

## Workflow

1. **Agree the mode.** State it in one sentence the owner can confirm: "In hours the AI operator answers first and connects to the team when needed; after hours it takes messages."
2. **Hours.** Show the weekly table. Check it if you can run code: `python3 scripts/hours_check.py hours.json`. Then `callcenter_set_hours`, passing only the days that change.
3. **Holidays.** Public holidays are kept up to date by Voikit. Add only the company's own closing days with `callcenter_add_holiday`; never invent one. Read the tool description for the date format the account uses.
4. **People.** Colleagues who take calls must exist as phone users with verified mobiles (panel-only; see `references/panel-only.md`). Prepare the list for the owner: name, mobile, department. An unverified mobile does not ring.
5. **Ring group or queue.** `callcenter_create_ring_group` for most teams; `callcenter_create_queue` plus `callcenter_set_queue_members` when callers must wait in line. Member lists are complete final lists, not additions. Set "if nobody answers" to the AI operator.
6. **Destinations.** `callcenter_set_destination` for in hours, after hours and holidays of the hours table. High risk: always approved by the owner.
7. **Number.** `numbers_set_route` to point the phone number at the hours table. High risk, always approved by the owner, and the last step of a first setup.
8. **Voicemail and recording.** `callcenter_set_voicemail_notify` for where notices of new messages go. `callcenter_set_recording` only after the owner confirms and the greeting announces it.
9. **Verify.** Read `callcenter_get_config` and `numbers_list` again and walk three calls with the owner: one now, one at 22:00, one on a holiday. Real test calls -> `voikit-qa-testing`.

## Decision rules

- Mode choice and its fallbacks: `references/answering-modes.md`.
- Build new pieces before pointing anything at them, and repoint before switching anything off. The safe order is: group or queue -> destinations -> number.
- While rebuilding, keep the AI operator as the temporary destination so no call is lost.
- One hours table for the business is enough unless departments truly keep different hours.
- Split shifts and a short day are separate ranges of the same day.
- Recording without notice can be unlawful where the caller is. For company accounts in regulated fields Voikit may switch recording on by default; otherwise it is the owner's choice.
- Changing queue members during business hours affects live calls: say so, and prefer a quiet moment.

## Show the owner

One card: hours table / the answering mode in one sentence / who rings, in what order, for how long / after-hours path / nobody-answered path / defaults chosen for their kind of business / change ids or "waiting for your approval".

## Never

- Leave a path that ends in silence: every route ends at a person or a recorded message.
- Point a number at an operator that is switched off, or at a group whose members are all unverified.
- Promise a phone menu, a new phone user or a new number through the tools: those are panel-only.
- Switch on recording without the owner's explicit yes.

## If something goes wrong

- A colleague's phone never rings -> the mobile is not verified, or the colleague must press a key to accept the call and did not.
- "It worked yesterday" -> `list_changes` with `all_sources` to see what changed, then `revert_change` if the owner wants.
- `callcenter_get_status` says settings are not live yet -> wait and read again before testing.

## References

- `references/operating-rules.md`, `references/answering-modes.md`, `references/panel-only.md`
- `scripts/hours_check.py` - optional check of a weekly hours table
