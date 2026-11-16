---
name: voikit-mcp
description: >-
  Foundation skill for working on a Voikit account through the Voikit MCP
  server: connecting an assistant (Claude, ChatGPT, Cursor and others),
  reading what the connection may do, approval modes, the life of a change
  (reason, preview, pending, revert, safe points), limits and errors, and
  which Voikit skill fits which job. Use when someone asks to "connect Voikit",
  "set up the Voikit connector / MCP", "why is my change pending", "undo what
  the assistant changed", "the connection is paused / forbidden", or before any
  other Voikit skill when the connection has not been checked yet.
license: Apache-2.0
compatibility: Needs a Voikit account. Works in Claude, ChatGPT and any Agent Skills client that can connect a remote MCP server.
metadata:
  version: "0.1.0"
  tier: core
---

# Voikit MCP - connect, check, change safely

Voikit is an AI call center and omnichannel platform: AI operators answer calls and chats from the business's own knowledge and rules, hand over to the team, and track work in a CRM. The Voikit MCP server lets an assistant read and configure one account. The skills supply the method; the server supplies the live facts.

Read `references/operating-rules.md` first. It holds the rules every Voikit skill follows.

## Use it when

- Voikit tools are missing and the person wants to connect.
- A change is waiting, was refused, or must be undone.
- You are about to start any Voikit work and have not called `capabilities` yet.

## Connecting

The server address is `https://voikit.ai/mcp`. An account that signs in on another Voikit domain uses that domain; the panel page **Tools > AI agents (MCP)** shows the exact address and a ready command for each client.

| Client | How |
|---|---|
| Claude (web, desktop, mobile) and ChatGPT | Add a custom connector (remote MCP server) with the server address. No token: the person signs in to Voikit, then picks the role, the sections and the approval mode on Voikit's consent page and allows it. |
| Claude Code, Cursor and other clients with a config file | In the panel create a connection (client, role and sections, approval mode, limits and expiry), copy the token and the ready command. The token is shown once; treat it like a password. |

Advise the owner to: start with "propose, you approve"; switch on only the sections the job needs (fewer sections, sharper assistant); make one connection per person and per device, so one can be cut without touching the others; never paste a token into a chat, a ticket or a shared file. If someone pastes a token to you, tell them to issue a new one.

## First calls of every session

1. `capabilities` - sections that are on, approval mode, ceilings and what is left today, language, time zone, how changes are confirmed.
2. `account_overview` - what the account already has.
3. If the person reports a problem: `diagnose` before anything else.

State what you found in two lines before proposing work: "I can read and propose changes to the call center, operators and knowledge; every change waits for your approval in the panel."

## The life of a change

1. Read the current state with the matching read tool.
2. Show the owner what you intend, in their words. For customer-facing text, show the exact text.
3. Call the write tool with a `reason` and an `idempotency_key`.
4. Act on the status as the operating rules say. A `pending_confirmation` answer includes `how_to_confirm`: relay it.
5. Later: `get_change` for one change, `list_changes` for all of yours (`all_sources` shows everyone's).
6. Undo with `revert_change`; withdraw a waiting proposal with `cancel_change`.

Before a batch: `save_safe_point`; `list_safe_points` shows the saved ones. Restoring a safe point is the owner's action in the panel.

## Which skill for which job

| The person wants | Skill |
|---|---|
| An account taken from empty to answering calls | `voikit-onboarding` |
| An AI operator created or changed (greeting, rules, transfer, voice) | `voikit-ai-agents` |
| Correct answers: FAQ, products, website, store connection | `voikit-knowledge-base` |
| Musts and nevers, policies, tone | `voikit-business-memory` |
| Hours, who answers, queues, ring groups, voicemail | `voikit-call-center` |
| Tasks, follow-ups, scheduled AI calls | `voikit-crm-followups` |
| The inbox, replies, who answers chats, SMS | `voikit-conversations` |
| Instagram comment rules, leads, showcases | `voikit-instagram-automation` |
| Conversation flows and forms | `voikit-flows-forms` |
| Appointments | `voikit-appointments` |
| Outbound campaigns | `voikit-campaigns` |
| Testing before go-live | `voikit-qa-testing` |
| "How did last week go", what to fix | `voikit-reviews` |
| A problem, or Voikit support | `voikit-support` |
| A ready layout for a kind of business | `voikit-industry-playbooks` |
| Voikit's team or a partner deploying for a Premium customer | `voikit-premium-onboarding` |

The server also offers ready prompts (`weekly_review`, `after_hours_setup`, `crm_cleanup`, `knowledge_from_site`) and resources (capabilities, account overview, call-center configuration, pending changes) for clients that show them.

## Never

- Resend a change that is `pending_confirmation`.
- Keep calling after `forbidden`: repeated refused calls pause the connection.
- Ask for, store or echo a token.
- Say something is impossible or possible without `feature_availability` or `search_help`.

## If something goes wrong

- No Voikit tools at all -> not connected, or the connector is switched off in this chat.
- A tool you expected is missing -> its section is off, the mode is read only, or the plan does not include it. The owner widens it under **Tools > AI agents (MCP)**.
- "Paused" -> the owner paused it, or too many refused calls did. The owner resumes it in the panel.
- "Expired" -> the owner issues a new token or extends the expiry.
- Still unclear -> `ask_ava` (Voikit's built-in assistant; counts against the account's assistant quota), then `voikit-support`.

## References

- `references/operating-rules.md` - rules for every Voikit skill
- `references/panel-only.md` - what is done only in the panel
