---
name: voikit-flows-forms
description: >-
  Build Voikit conversation flows and dynamic forms: a step-by-step call or
  chat script with conditions, questions, form collection, CRM actions and
  webhooks, attached to an AI operator; and forms with conditional questions
  whose answers are stored. Use when someone says "build a flow / call
  script", "qualify leads step by step", "ask these questions in order",
  "create a survey / intake form", "if the rating is low ask why", "register a
  complaint and text the tracking code", "attach the flow to my agent", in any
  language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected with the Flow designer section on (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: core
---

# Voikit flows and forms

A flow makes an operator follow fixed steps instead of only its prompt: ask, branch, collect a form, create a CRM item, call a webhook, transfer. A form is a set of questions asked in order, by voice or chat, with the answers stored.

Read `references/operating-rules.md` first.

## Use it when / hand off when

- Use a flow when the order of steps matters and must be the same every time (qualification, complaint registration, order check, surveys).
- For free conversation with a few rules, the prompt is enough -> `voikit-ai-agents`.
- Instagram comment rules are not flows -> `voikit-instagram-automation`.

## Before you start

1. `capabilities`, then `flows_list` and `forms_list`.
2. `flows_node_types`: the exact contract of every node type and its fields. Read it every time before building; never build a node from memory.
3. `flows_templates`: ready flows (lead qualification, appointment booking, support and others). Start from one when it is close.

## Workflow

### A form

1. Agree the questions in the order they are asked. Write each the way the operator should say it.
2. Give each question a meaningful key (for example a rating, a delivered yes / no, a reason). Later questions can depend on earlier keys ("ask the reason only when the rating is low"), and a question can accept only a valid answer and ask again otherwise. Read the tool description for the exact syntax.
3. Show the owner the questions and the conditions in plain words. `forms_create`.
4. Later: `forms_get` before `forms_update`; `forms_submissions` for the answers.

### A flow

1. Draw it in words first: start -> what is asked -> each branch -> how every branch ends. Every branch must end in an answer, a transfer or a recorded request.
2. Build: `flows_create` from a template or from nodes and edges. Positions are laid out automatically.
3. `flows_validate` before saving when you build by hand: errors block saving, warnings deserve a look.
4. Small changes: `flows_edit` with precise operations (add a node after another, update one, connect, remove). Use `flows_update` only to replace the whole graph or rename.
5. Show the owner the flow as a numbered script, not as a graph dump.
6. `flows_attach` to the operator that should run it. One flow per operator: attaching replaces that operator's previous flow, so say which flow is being replaced.
7. `flows_set_active`. A disabled flow is not run even when attached; the operator falls back to its prompt.
8. Test with a real call or chat -> `voikit-qa-testing`.

## Decision rules

- Short flows work. If a caller answers more than five or six questions before getting anything, split the flow or drop questions.
- Ask for what the next step needs, nothing more. A complaint needs who, what, when; it does not need an address.
- A step that creates a CRM item should say the tracking code to the customer or text it, so they can follow up.
- Webhook steps send data outside the account: the owner names the address and approves it. Never invent an endpoint.
- Text inside a flow is customer-facing: it follows the charter, and a text with a link or number always waits for the owner.
- Switch off instead of deleting. `forms_set_active` archives a form with its answers; `forms_delete` works only for a form no flow uses and that has no answers. `flows_delete` removes the run history too and is always the owner's decision.

## Show the owner

The script view: numbered steps, each with what the operator says, what it stores, and where each answer leads. Then: which operator runs it, whether it is active, and how to switch it off.

## Never

- Save a flow with a dead end.
- Attach a flow to the main reception operator without telling the owner it replaces how that operator behaves on every call.
- Collect personal data the business has no use for.
- Read form answers aloud to anyone but the account's own team.

## If something goes wrong

- "The operator ignores the flow" -> is it attached to that operator, is it active, does the route point at that operator.
- Validation errors -> fix the first one; later ones are often consequences.
- A form cannot be deleted -> it has answers or a flow uses it; switch it off.

## References

- `references/operating-rules.md`
