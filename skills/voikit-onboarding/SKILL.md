---
name: voikit-onboarding
description: >-
  Take a Voikit account from empty to an AI operator answering real calls, in
  the proven order: business profile, first operator, knowledge base, call
  center, phone number, test, smart defaults - asking the owner only what
  cannot be found. Use when someone says "set up Voikit for my business", "get
  my account ready", "configure everything", "I just signed up, what now", "go
  live", or asks for a full setup for a clinic, shop, restaurant, agency or any
  other business, in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected (see voikit-mcp). Works in Claude, ChatGPT and other Agent Skills clients.
metadata:
  version: "0.1.0"
  tier: core
---

# Voikit onboarding - from an empty account to live calls

You lead the whole setup and call on the other Voikit skills for each part. A prepared owner needs about ninety minutes; without preparation, plan two sittings.

Read `references/operating-rules.md` first.

## Use it when / hand off when

- Use it for a first setup or a full re-check of an existing one.
- One part only (just the hours, just the FAQ) -> go straight to that part's skill.
- Voikit's own team deploying for a Premium customer -> `voikit-premium-onboarding`.

## Before you start

1. `capabilities`, `account_overview`, `diagnose`. Say what the connection may do and what already exists.
2. Read what Voikit knows: `business_profile_get`, `memory_get`, `settings_smart_defaults_get`.
3. Run the brief in `assets/business-brief.md`: confirm what is known, ask only the gaps (four at a time at most).
4. `save_safe_point` named for today's setup.
5. Tell the owner the plan in six lines and what only they can do in the panel (`references/panel-only.md`): verify colleagues' mobiles, get the phone number, upload files, switch on two-step verification.

## Workflow

Each step ends with a checkpoint: show what was done, what waits for approval, and ask to continue.

1. **Profile (5 min).** Pass the owner's full words to `business_intake` with `dry_run` first, show the plan, then apply. Correct the kind of business, team size and answering preference with `settings_business_profile_set`; company name and time zone with `settings_update_profile`. Everything later builds on this.
2. **First operator (15 min).** Skill `voikit-ai-agents`: pick the template that fits (`agents_list_templates`), fill its questions from the brief, show the greeting and rules, create it.
3. **Knowledge (30 min).** Skill `voikit-knowledge-base`: website, folders, the twenty most frequent questions, products and prices. Then `voikit-business-memory` for the hard rules and policies. Knowledge comes before routing: an operator without knowledge fails every test call.
4. **Call center (30 min).** Skill `voikit-call-center`: choose one of the six answering modes (`references/answering-modes.md`), hours and holidays, who rings, what happens after hours and when nobody answers.
5. **Phone number (5 min).** The owner gets or connects the number in the panel. Then `numbers_list`, and `numbers_set_route` to point it at the hours table. This is always approved by the owner, and it comes last on purpose: from that moment real customers reach the operator.
6. **Test and go live.** Skill `voikit-qa-testing` with `assets/golive-checklist.md`. Fix, retest.
7. **Smart defaults (after go-live).** `settings_smart_defaults_get`: review what Voikit fitted for this kind of business and what is only offered; apply the offered ones the owner agrees to with `settings_smart_defaults_apply`. Settings the owner chose are never overwritten.

Optional, when the brief calls for it: `voikit-crm-followups`, `voikit-appointments`, `voikit-conversations`, `voikit-instagram-automation`, `voikit-flows-forms`. For a ready layout by kind of business: `voikit-industry-playbooks`.

## Decision rules

- An account that already has an operator and routing is reviewed, not rebuilt: list what differs from the brief and change only that.
- If the account has no live phone setup (`setup_required`), the owner runs Voikit's built-in setup once in the panel; continue from step 3.
- If the owner stops answering mid-way, finish what is safe (knowledge, drafts), list what waits, and stop before the phone number.
- Regulated fields: apply the regulated rules of the operating rules from step 1.

## Show the owner

At every checkpoint, one short card: done (with change ids) / waiting for your approval (and where to approve) / your turn in the panel / next step. At the end: the handover summary - what was built, the answering mode in one sentence, the defaults chosen for their kind of business, how to change things, how to undo.

## Never

- Connect the phone number before the test passes.
- Create a second operator, hours table or ring group when one that fits already exists.
- Skip the owner's approval of the greeting and the hard rules.
- Ask a question whose answer is on the website or in the profile.

## If something goes wrong

- A step keeps waiting for approval -> continue with steps that do not depend on it; list it in the card.
- Calls are not answered after go-live -> `diagnose`, then `voikit-support`.

## References

- `references/operating-rules.md`, `references/answering-modes.md`, `references/panel-only.md`
- `assets/business-brief.md`, `assets/golive-checklist.md`
