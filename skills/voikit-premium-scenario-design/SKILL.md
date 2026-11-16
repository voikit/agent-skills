---
name: voikit-premium-scenario-design
description: >-
  Design the best Voikit setup for one business from its business model and
  write it as a one-page proposal the owner approves before anything is
  built: the answering mode, the AI operators and their greetings, the
  knowledge plan, red lines and hand-over cases, CRM follow-ups, channels and
  booking, with every default labelled. Use at steps 4 and 5 of a Premium
  deployment, or when someone says "design the setup for this customer",
  "write the proposal", "which scenario fits this business", "prepare the
  plan for the owner to approve", in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected to the customer's account; read access is enough to design (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: premium
---

# Voikit Premium scenario design

Design is where a done-for-you deployment earns its name: the owner reads one page, recognises their own business in it, and says yes.

Read `references/operating-rules.md` first. Modes are in `references/answering-modes.md`; the proposal format is `assets/proposal.md`.

## Use it when / hand off when

- Use it after intake, before any build.
- Missing facts -> back to `voikit-premium-intake`; do not design around a hole.
- After approval -> the build, led by `voikit-premium-onboarding`.

## Before you start

1. The business model and gap answers from intake.
2. `settings_smart_defaults_get`: what Voikit recommends for this kind of business and why.
3. `agents_list_templates`: the operator templates, their purposes, and which CRM task types each follows up.
4. `feature_availability` for anything the design depends on (a channel, booking, recording, the number of operators the plan allows).
5. `account_overview`: what already exists, so the design reuses it.

## Workflow

1. **Answering mode.** Choose with `references/answering-modes.md`. Write the reason in one sentence. If two modes fit, put the choice to the owner as one question with both consequences.
2. **Call paths.** In hours, after hours, on holidays, when nobody answers. Every path ends at a person or a recorded message.
3. **Operators.** One per job, each from a template: reception first; then only the ones the business needs (sales, support, order status, appointment confirmation, follow-up). For each: name, job in one sentence, the greeting word for word.
4. **Red lines and hand-over.** The owner's "never" and "connect to a person when" lists, as they said them, plus the essentials for their kind of business offered as suggestions.
5. **Knowledge plan.** Folders, sources (site, documents the owner will upload, store connector), the first twenty questions, the price policy.
6. **CRM.** Which kinds of work are tracked, which operator follows up each, and what the owner should set for attempts and spacing.
7. **Channels and booking.** What is switched on now; what waits for the owner in the panel (`references/panel-only.md`).
8. **Write the proposal** with `assets/proposal.md`, in the owner's language, plain words, one page. Label every default.
9. **Review with the lead**, then send to the owner. Collect "I approve" or "change this line".
10. **Version it.** Fold the edits in, mark the approved version and date in the run log. The approved proposal is the specification for the build and for the tests.

## Decision rules

- Start from what Voikit already recommends for this kind of business and change only what the owner's answers contradict. A design that fights the product's defaults needs a reason.
- Fewer operators is better. A second operator is justified by a different job, not by a different department name.
- Prefer a booking request that staff confirm over a firm booking when schedules differ per person or only staff know capacity.
- After hours: shops, schools and restaurants usually want full answers; offices and clinics usually want a message taken. Say which you chose.
- Do not design in panel-only pieces (a phone menu, new phone users) without listing who builds them and when.
- Do not design in anything `feature_availability` does not confirm for this account.
- Regulated kinds of business: answers only from recorded knowledge; recording announced; every complaint to a person; no automatic AI calls to leads.
- The greeting is short, names the business, offers help, and announces recording when recording is on.

## Show the lead and the owner

- The lead sees: the proposal, the list of assumptions with their confidence, and the open risks.
- The owner sees only the proposal page. No tool names, no internal terms.

## Never

- Start building on an unapproved proposal.
- Present a default as the owner's choice.
- Promise dates, prices or features that are not confirmed.
- Name suppliers, engines or model vendors.

## References

- `references/operating-rules.md`, `references/answering-modes.md`, `references/panel-only.md`
- `assets/proposal.md`
