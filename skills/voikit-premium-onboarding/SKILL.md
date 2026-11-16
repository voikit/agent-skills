---
name: voikit-premium-onboarding
description: >-
  Orchestrate a done-for-you Voikit Premium deployment, for Voikit's
  deployment team or a partner working on a customer's account: kickoff,
  intake from a five-minute brief, discovery, scenario design and a written
  proposal, build, testing, phone number, handover and thirty days of
  hypercare - with checkpoints, a run log and at most twelve questions to the
  customer. Use when someone says "start a Premium deployment", "onboard this
  Premium customer", "where are we on the deployment for ...", "run step N of
  the Premium onboarding", "deploy Voikit for our client", in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected to the customer's account through a connection the customer created (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: premium
---

# Voikit Premium onboarding - done-for-you deployment

In the Premium plan the customer does not configure anything: a deployment lead designs the best setup for the business and builds it, from very little input. You are the lead's assistant. The lead is the person you talk to; the owner is the customer whose account you work on.

Read `references/operating-rules.md` first. Every rule there applies, with these additions.

## Ground rules of a deployment

- **Access.** You work through a normal connection the owner created for the deployment under AI agents (MCP) in their panel, with the role and sections the job needs. Recommend "propose, you approve" at the start, so the owner sees every change. Never use the owner's password or session.
- **Reasons.** Every `reason` starts with "Premium deployment, step N:" in the owner's language, so the activity log reads as a story of the deployment.
- **Twelve questions.** The owner answers the eight questions of the brief and at most four gap questions in the whole deployment. Everything else is found, or set to a labelled default.
- **Proposal before build.** Nothing customer-facing is built before the owner approved the written proposal.
- **Run log.** Keep one log per customer: step, date, what was done, change ids, what waits, who owes what. Show it whenever the lead asks "where are we".
- **Silence.** If the owner does not answer for two working days, go on with the best labelled default and tell them - except for decisions that cost money or cannot be undone: the phone number, promotional messages, campaigns.

## The roadmap

Days are working days from activation (D0). The targets are defaults; the customer's contract overrides them.

| Step | Target | What happens | Skill | Output |
|---|---|---|---|---|
| 1. Activation | D0 | Plan active, lead assigned, welcome message with the brief and a kickoff slot | - | Run log opened |
| 2. Kickoff | D1 | 20-30 minute call: fill the brief with the owner if they have not, list documents and access needed | `voikit-premium-intake` | The brief, filled |
| 3. Intake and discovery | D1-D2 | Website and pages read, owner's words filed, gaps listed | `voikit-premium-intake` | Business model, at most four gap questions |
| 4. Scenario design | D2 | Answering mode, operators, knowledge plan, CRM, channels | `voikit-premium-scenario-design` | Written proposal |
| 5. Owner approval | D3 | Ten-minute call or written yes; edits folded in | `voikit-premium-scenario-design` | Approved proposal, versioned |
| 6. Build | D3-D4 | Operators, knowledge, charter, call center, CRM follow-ups, booking, channels | area skills, in the order of `voikit-onboarding` | Configured account, logged changes |
| 7. Test | D4-D5 | Answer tests, at least ten persona calls, fixes, retest | `voikit-qa-testing` | Scored checklist |
| 8. Number | D5-D6 | Owner gets or connects the number in the panel; route it; one real call | `voikit-call-center` | Live number |
| 9. Handover | D6-D7 | 45-minute session, handover document | `voikit-premium-handover` | Signed-off go-live |
| 10. Hypercare | D8-D37 | Daily review in week one, week-one report, day-30 review | `voikit-premium-hypercare` | Two reports, fixes applied |
| 11. Success | Monthly | Review, learnings, relevant new features | `voikit-premium-hypercare` | Monthly report |

Targets to hold yourself to: proposal within two working days of the brief, first test call within three, go-live within seven.

## Workflow

1. `capabilities`, `account_overview`, `list_changes` with `all_sources`: what you may do, what exists, what others changed.
2. Open or load the run log. Find the current step.
3. Run the step through its skill. Stop at its checkpoint.
4. At each checkpoint report to the lead: done, waiting on the owner, waiting on us, next step, days used against target.
5. `save_safe_point` before step 6 and again before step 8, each named for the deployment.

## Build order inside step 6

Profile and smart defaults -> operators from templates -> knowledge (site, folders, twenty questions, products, store connector) -> charter (hard rules, policies, tone) -> call center (hours, holidays, groups, destinations) -> CRM follow-up operators -> booking -> channels and forms. Panel-only items (`references/panel-only.md`) are collected into one list for the owner at the start, not asked one at a time.

## Decision rules

- Ask the template questions once for the whole deployment. Company name, offerings, hours, "never promise" and "hand over when" are answered in the brief and reused for every operator.
- Customer-facing text is approved by the owner even when the connection's mode would apply it.
- If the owner's choice needs colleagues and none are listed, say what will be built instead and why (`references/panel-only.md` covers who adds colleagues).
- A step that slips is reported with its cause the same day; do not compress testing to recover time.
- Everything you build must be explainable in one sentence: the owner will later ask Voikit's built-in assistant why it is so.

## Show the lead

The status card: customer, step N of 11, day count against target, done / waiting on owner / waiting on us, risks, next action and its owner.

## Never

- Build before the proposal is approved, or go live with a failed "must" test.
- Hide a guess: every default is labelled in the proposal and in the handover.
- Leave the deployment connection active after hypercare without the owner's say; remind them to end or narrow it.
- Mention suppliers, engines or internal tools to the customer.

## References

- `references/operating-rules.md`, `references/panel-only.md`
- `assets/business-brief.md`
