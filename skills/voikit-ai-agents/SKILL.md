---
name: voikit-ai-agents
description: >-
  Design, create and tune Voikit AI operators (the AI agents that answer calls
  and chats): pick a template, fill it from the business's own words, write
  and check the greeting, add rules, set transfer to people or departments,
  choose voice and model, attach knowledge, switch on or retire. Use when
  someone asks to "create an AI receptionist / operator / agent", "change the
  greeting", "the operator says X, fix it", "add a rule", "transfer to my
  mobile", "change the voice", "make a sales / support / follow-up agent", in
  any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected with the AI operators section on (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: core
---

# Voikit AI operators

An AI operator is what callers and chat visitors talk to. It follows, in this order: the business charter (skill `voikit-business-memory`), its own prompt and rules, and the knowledge attached to it.

Read `references/operating-rules.md` first.

## Use it when / hand off when

- Use it to create, change, switch off or review an operator.
- A rule that every operator should follow (never promise a discount) -> `voikit-business-memory`.
- A wrong answer about facts (price, address) -> `voikit-knowledge-base`.
- Where calls go before and after the operator -> `voikit-call-center`.

## Before you start

1. `capabilities`, then `agents_list`. For one operator: `agents_get` (with `include_prompt` when you will edit the prompt). It also tells you which fields that kind of operator supports.
2. `business_profile_get` and `memory_get`: the facts and rules the prompt must agree with.
3. For a new operator: `agents_list_templates` - purpose, direction, the setup questions, and which CRM task types it can follow up.

## Workflow

### A new operator

1. Choose the template by the job (reception, sales, support, order status, appointment confirmation, follow-up ...). One operator per job; do not build two receptionists.
2. Answer the template's questions from what is already known. `company_name` and the offerings are required; "never promise" and "hand over when" come from the brief or the charter. Ask the owner only for what is missing.
3. Draft the greeting. Check it: `python3 scripts/text_check.py --kind greeting "<text>"` (optional; without code execution apply the same checks by eye: 3-400 characters, about ten seconds spoken, numbers written as they are said, no link or phone number).
4. Show the owner: name, job in one sentence, greeting word for word, rules, when it transfers and to whom. Get a yes.
5. `agents_create_from_template` with the answers. Use `agents_create` only when no template fits; it writes the prompt from the business itself, so do not ask the owner for a prompt.
6. Transfer: `agents_set_transfer` for one number, or `agents_set_departments` for smart reception (several departments, each with a label, the members' mobiles and when to use it).
7. If it should answer a number or a time of day, continue in `voikit-call-center`. A new operator does not receive calls until a route points at it.

### Changing an operator

- Greeting -> `agents_set_greeting`. Name -> `agents_set_name`.
- One more instruction -> `agents_add_rule` (one clear sentence, in the owner's words).
- Part of the prompt -> `agents_edit_prompt` (append, replace an exact passage, set or remove a section). Read the prompt first; never retype the whole prompt for a small change.
- Voice, model, knowledge selection, call behaviour, booking, after-call messages, flow -> `agents_update`, with ids from `agents_list_voices`, `agents_list_models`, `agents_list_knowledge`. Only the fields you pass change.
- On / off -> `agents_set_active`. Switching off is refused while a route, menu, queue or number still points at the operator: move the routes first.
- Retire -> `agents_retire`: switched off for good and its extension freed (high risk; the owner's decision). It can be brought back from the panel or by reverting the change. For a pause use `agents_set_active`.

## Decision rules

- Greeting: who you reached, then an offer to help. One or two sentences. If recording is on, the greeting announces it.
- A rule belongs to the operator only if it is about that operator's job. Business-wide rules go to the charter, so every operator and channel follows them.
- On calls an operator answers only from the knowledge selected for it; in chat, when nothing is selected, all knowledge is used. After adding knowledge, check the operator's selection.
- Voice: pick by language and gender the owner wants from `agents_list_voices` and offer the preview link. Describe voices by label, never by vendor.
- Transfer during business hours only is a common wish; say plainly what happens outside those hours (the operator takes a message).
- Removing the transfer number means callers cannot reach a person: high risk, state the consequence before proposing.
- Outbound follow-up operators are tied to CRM task types -> `voikit-crm-followups`.

## Show the owner

Before: the card in step 4. After: what changed, the change id or "waiting for your approval", and one sentence on how to test it (call the operator's extension from the panel's test phone).

## Never

- Invent offerings, prices or promises in a prompt or a rule.
- Put a link, phone number or card number in a greeting without telling the owner it will wait for their approval.
- Create an operator when the plan's operator limit is reached; say so and offer to reuse or retire one.
- Rewrite a prompt the prompt team or the owner tuned by hand; edit the part that needs it.

## If something goes wrong

- "The operator still says the old thing" -> check which operator the route points at (`callcenter_get_config`) and whether the change is still pending.
- "It does not know X" -> `knowledge_test_answer`, then the knowledge selection of that operator.
- "It hangs up instead of transferring" -> check the transfer number and that the colleague's mobile is verified; then `diagnose`.

## References

- `references/operating-rules.md`
- `scripts/text_check.py` - optional pre-check of customer-facing text
