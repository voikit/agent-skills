---
name: voikit-premium-handover
description: >-
  Hand a finished Voikit deployment over to the customer: the handover
  document (what was built, why, how to change it, test results, the next
  thirty days), the agenda of the handover session, a short walkthrough
  script, and the go-live sign-off. Use at step 9 of a Premium deployment, or
  when someone says "prepare the handover", "write the handover document",
  "we are going live with this customer", "what do I show the owner in the
  handover meeting", in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected to the customer's account; read access is enough (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: premium
---

# Voikit Premium handover

A good handover leaves the owner able to answer three questions without calling anyone: what do I have, how do I change it, who do I ask.

Read `references/operating-rules.md` first. The document format is `assets/handover.md`; the checklist is `assets/golive-checklist.md`.

## Use it when / hand off when

- Use it when the checklist is scored and every "must" line passes.
- Tests not done or failing -> `voikit-qa-testing` first. Do not write a handover around a failure.
- After sign-off -> `voikit-premium-hypercare`.

## Before you start

Read the account as it is now, not as it was planned:
`account_overview`, `callcenter_get_config`, `numbers_list`, `agents_list`, `memory_get`, `knowledge_list`, `crm_list_pipelines`, and `list_changes` with `all_sources` for the deployment period.

## Workflow

1. **Compare with the approved proposal.** List every difference between what was approved and what exists, with the reason. Unexplained differences are fixed or explained before handover.
2. **Open items.** Pending changes (`list_changes`), panel-only items the owner still owes, failed non-must tests. Each with an owner and a date.
3. **Write the document** with `assets/handover.md`, in the owner's language. Section 2, "why it is built this way", is the one owners keep: three decisions, each with its reason in their terms.
4. **Session agenda (45 minutes).**

| Minutes | Part |
|---|---|
| 5 | What you have: the call path in one picture, the operators by name |
| 10 | A live test call together: greeting, a frequent question, a transfer |
| 10 | Where things are in the panel: calls and their summaries, the CRM board, the inbox, the knowledge |
| 10 | Changing things: by hand in the panel, by telling the built-in assistant, by a connected assistant; where to see and undo changes |
| 5 | The next thirty days and what we need from you |
| 5 | Questions; sign-off |

5. **Walkthrough script (about five minutes)** for a recording of the customer's own panel: the same order as the agenda, one sentence per screen, no jargon.
6. **Sign-off.** The owner confirms the checklist result and the open items. Record the date in the run log as go-live.
7. **Access.** Agree with the owner what happens to the deployment connection during hypercare: keep it as it is, narrow it to read and propose, or set an expiry. It is their decision and their click in the panel.

## Decision rules

- Write for the person who will actually run it day to day, often not the owner: the receptionist, the office manager.
- "How to change" examples use the five jobs owners really do: hours and holidays, the greeting, a new question and answer, a colleague who receives calls, undoing a change.
- Every default chosen for their kind of business is listed once more, so nothing is a surprise later.
- The red lines are repeated word for word as approved.
- If two-step verification is still off on the owner's account, it is the first open item.

## Show the lead

The document, the agenda, the open-item list, and one line: ready to hand over / ready after these items.

## Never

- Describe something as built that waits for approval.
- Hand over credentials, tokens or codes in the document.
- Leave an open item without an owner and a date.
- Include other customers' data, or callers' personal details, in examples.

## References

- `references/operating-rules.md`
- `assets/handover.md`, `assets/golive-checklist.md`
