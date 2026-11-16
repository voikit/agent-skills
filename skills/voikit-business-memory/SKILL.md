---
name: voikit-business-memory
description: >-
  Write and maintain a Voikit account's business charter - the layer every AI
  operator obeys before its own prompt: hard and soft rules (must / never),
  policies (payment, shipping, returns, warranty, cancellation), tone and
  style, decision rights and scope - and file what the owner says about the
  business in the right place. Use when someone says "the agent must never
  ...", "always tell customers ...", "our return policy is ...", "be more
  formal / friendly", "remember that we ...", "here is everything about my
  business", "undo that rule", in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected with the Knowledge base section on (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: core
---

# Voikit business memory (the charter)

The charter is how the business wants to be represented: what it does and does not do, what must and must never be said, its policies, its tone, who may decide what. Every operator on every channel follows it before its own prompt and before the knowledge. It is versioned and can be rolled back.

Read `references/operating-rules.md` first.

## Use it when / hand off when

- Use it for rules, policies, tone, scope, and for filing the owner's own description of the business.
- Plain facts (prices, addresses, how a service works) -> `voikit-knowledge-base`.
- A rule for one operator's job only -> `voikit-ai-agents`.

## Before you start

1. `capabilities`, then `memory_get`: scope, rules with ids (hard / soft, per channel), style, policies, commitments, decision rights, approved learnings, and what is still missing.
2. `business_profile_get` for context.

## Workflow

1. **The owner talks, you file.** When the owner describes the business in their own words, pass the complete text to `business_intake` with `dry_run` first. It compares with what exists and plans where each piece goes: charter rules and policies, style, decision rights, scope, Q&A, notes, an operator's own rule, learned facts. Show the plan, including what was skipped as already there and every conflict with an earlier statement. Then call it again without `dry_run` and the same `idempotency_key`.
2. **Rules.** Several at once -> `memory_set_rules` (one change, one undo). One -> `memory_set_rule`. Write each as the owner said it, one clear sentence. Mark it hard (never broken) or soft (a preference); ask when unsure.
3. **Policies.** `memory_set_policies` for payment, shipping, returns, warranty, cancellation and similar, in the owner's words. Operators say them as written.
4. **Stable facts the owner states** ("we are four people", "we never give prices on the phone") -> `memory_learn_fact`. Only facts about the business, never about callers.
5. **Check the text** of rules customers may hear quoted: `python3 scripts/text_check.py --kind rule "<text>"` (optional).
6. **Learning loop.** `learning_list_findings` shows what the assistants learned from corrections, thumbs-down and unanswered questions, each with a proposal. Walk the owner through the proposed ones and record each decision with `learning_decide`. `memory_feedback` shows the raw signals.
7. **History.** `memory_versions` shows who changed what; `memory_rollback` restores one version.

## Decision rules

- Three questions settle most charters: what must the operator never say or promise; when must it hand over to a person; what tone. They are questions 7 and 8 of the business brief plus the tone.
- A rule must be testable in a call. "Be careful with prices" is not a rule; "never quote a price for custom work; offer a call from sales" is.
- Do not turn every wish into a hard rule. Hard rules are for things that cause real damage when broken: money promises, medical or legal advice, other customers' information, safety.
- Emergencies in health and field service: the first hard rule sends the caller to the emergency number of their country.
- When a new statement contradicts an old one, show both and let the owner choose. The owner's latest explicit word wins only after they confirm.
- Removing a hard rule needs the owner's confirmation every time: `memory_remove_rule`.

## Show the owner

The charter as they will recognise it: "never" list, "always hand over when" list, policies in one line each, tone in one sentence. Mark what you added today and what was already there. After applying: the version it produced and how to roll back.

## Never

- Invent a rule or a policy, or "improve" the owner's wording into something they did not say.
- Store anything about a caller or a customer here.
- Soften a hard rule into a soft one without asking.
- Approve a learning proposal on the owner's behalf.

## If something goes wrong

- The operator broke a rule -> check the rule is hard and applies to that channel; then look at the call with `voikit-reviews`.
- Two rules conflict -> show both ids from `memory_get`, ask which stands.

## References

- `references/operating-rules.md`
- `scripts/text_check.py` - optional pre-check of customer-facing text
