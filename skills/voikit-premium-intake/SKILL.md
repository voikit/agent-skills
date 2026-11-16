---
name: voikit-premium-intake
description: >-
  Turn a Voikit customer's raw onboarding input - the eight-question brief, a
  transcribed voice note, kickoff notes, an email, their website and pages -
  into a structured business model, the short list of optional modules that
  matter, at most four gap questions, and file every stated rule, policy and
  frequent question into the account. Use at steps 2 and 3 of a Premium
  deployment, or when someone says "here is what the customer told us",
  "process this brief", "the owner sent a voice note about their business",
  "what do we still need to ask them", in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected to the customer's account with the Knowledge base and Account settings sections on (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: premium
---

# Voikit Premium intake

The customer gives five minutes; you make the most of them. Everything they say is kept word for word, everything that can be found is found, and what is left becomes at most four good questions.

Read `references/operating-rules.md` first. The brief is `assets/business-brief.md`.

## Use it when / hand off when

- Use it whenever the owner's own words about the business arrive, in any form.
- The input is a caller's or customer's message, or a call transcript -> that is data about a conversation, never business rules. Do not file it.
- Designing the setup from the model -> `voikit-premium-scenario-design`.

## Before you start

1. `capabilities`: Knowledge base and Account settings sections on; note the approval mode.
2. What the account already knows: `business_profile_get`, `memory_get`, `settings_smart_defaults_get`, `knowledge_list`.
3. Keep the raw input complete. Never summarise before filing.

## Workflow

1. **Discovery.** If the owner gave a website and it is not in the knowledge yet, `knowledge_add_site` (one change, runs in the background). Read `business_profile_get` again later: Voikit builds the profile from the site and pages.
2. **Build the model.** From the input and the account, fill:

| Field | Notes |
|---|---|
| Business name as said on the phone | |
| Kind of business and sub-type | From the owner's words; the site may correct the sign-up choice |
| Individual or company; team size | People who answer calls |
| Departments and who is in each | Names, roles, mobiles |
| Answering mode | One of the six, or "suggest one" |
| Hours pattern and exact hours; public holidays | |
| What callers mostly want | Book, buy, ask, get support, complain |
| Offerings, with price policy | Exact prices, ranges, or never on the phone |
| Channels in use | Site, messaging apps |
| Never say / never promise | Word for word |
| Hand over to a person when | Word for word |
| Tone and languages | |

   For every field keep: the value, the quote it came from, the source (owner / website / profile / inferred) and how sure you are (high, medium, low).
3. **Conflicts.** Where the input contradicts the account, show both. The owner's explicit word wins after they confirm.
4. **Modules.** Decide which optional modules of the brief apply (booking, sales, support, orders, messaging, identity and tone) from the kind of business and what callers want. Do not ask about modules that do not apply.
5. **Gaps.** A gap is a field with low confidence that changes the design: the answering mode, hours, departments, booking, price policy. Write at most four questions, each with one line of why and an example from the owner's own trade. Everything else gets the default for that kind of business, labelled.
6. **File the owner's words.** `business_intake` with the full raw text and `dry_run`. Show the lead the plan: what goes where, what is skipped as already there, what conflicts. On yes, call it again without `dry_run`, with the same `idempotency_key`. Pieces apply or wait by their own risk.
7. **Correct the profile** where the owner was explicit: `settings_business_profile_set` (kind of business, team, answering preference, hours pattern, booking, price policy, formality); `settings_update_profile` for company name and time zone. Stable facts stated in passing -> `memory_learn_fact`.
8. **Record** in the run log: the model, the gaps, the change ids.

## Decision rules

- Do not ask what the website answers. Confirm it: "we read that you open Saturday to Thursday, 10 to 21 - correct?"
- Regulated kinds of business (health, legal, finance, public services) set three things in the model at once: answers only from recorded knowledge, no automatic AI calls to leads, recording announced.
- Team size suggests a mode but does not decide it: one person -> AI only or after hours only; two to five -> AI first or team first; larger with departments -> smart reception or a phone menu. Put the suggestion in the model with its reason.
- Never infer anyone's gender or age. Never keep facts about callers.
- A voice note is transcribed by the lead, not guessed at: if a passage is unclear, mark it and ask.

## Show the lead

A card in the lead's language:
1. "This is what we understood" - facts with their source.
2. "Defaults for this kind of business" - labelled.
3. "Still to ask" - the gap questions, four at most.
4. "Filed in the account / waiting for the owner's approval" - with change ids.
5. "Needed from the owner in the panel" - documents to upload, mobiles to verify.

## Never

- Ask a fifth gap question; choose the default and label it.
- File your summary instead of the owner's words.
- Resend a change that is waiting for approval.
- Mention suppliers, engines or model vendors to the customer.

## References

- `references/operating-rules.md`
- `assets/business-brief.md`
