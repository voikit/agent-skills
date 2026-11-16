<!-- Generated from shared/answering-modes.md by scripts/sync_shared.py. Edit the source, not this copy. -->

# The six answering modes

"Who answers the phone first" is the most important decision of a Voikit setup. Voikit's built-in setup offers these six modes; use the same names with the owner.

| Mode | During business hours | After hours and holidays | Nobody answered | Needs colleagues? |
|---|---|---|---|---|
| 1. AI operator only | AI operator | AI operator (takes a message) | Message and SMS to the owner | No |
| 2. AI operator first, transfer when needed | AI operator, a colleague when needed | AI operator | AI operator takes a message | No |
| 3. Team first, AI operator as backup | Colleagues ring together | AI operator | AI operator | Yes |
| 4. Phone menu (1 sales, 2 support ...) | Menu, then each department's ring group or queue | AI operator | AI operator | Yes |
| 5. Smart reception (no keys) | AI operator finds the right department and connects | AI operator | AI operator takes a message | Yes, at least two |
| 6. After hours only | The team | AI operator | AI operator | No |

## Choosing

- One person, or an information line -> mode 1. Only urgent matters, complaints or an explicit request reach the owner's mobile.
- Small team whose callers mostly ask the same things -> mode 2. This is the default for most businesses.
- Callers expect a person (a clinic front desk, a known local shop) and the team can usually pick up -> mode 3.
- Several separate departments and callers who already know which one they need -> mode 4. Keep the menu to five options at most and give key 0 to the AI operator.
- Several departments but callers do not know which one they need (typical for business customers) -> mode 5.
- A team that answers everything itself in hours and only wants nights, holidays and missed calls covered -> mode 6.
- If two modes fit, ask one question that states both consequences. Never pick silently.

## Rules the product applies

- A mode that needs colleagues but has none listed is built as mode 1. Mode 5 with fewer than two colleagues becomes mode 2. If an owner says "the mode I chose was not applied", check the colleague list first.
- The standard structure is: phone number -> a business-hours table -> in hours: ring group / menu / AI operator; after hours and holidays: AI operator; nobody answered: AI operator.
- Ring group or queue: team size alone does not decide. A ring group (colleagues ring together or in turn, first to answer gets the call) fits most businesses. A queue (callers wait in line) is for many simultaneous calls: a menu branch with three or more colleagues, or a very large team.
- Useful defaults: ring colleagues about 20 seconds (30 in mode 6) before the AI operator answers; queue wait about 90 seconds. Most callers hang up after half a minute of ringing.
- A colleague's mobile rings only after it is verified in the panel. Until then calls skip it.
- "If nobody answers" must never be empty: an empty fallback ends the call.
- Online shops, schools and restaurants usually want the AI operator to answer fully after hours, not only take a message: evenings and weekends are when their customers call.

## What an assistant can build and what it cannot

Through the tools: business hours and holidays of an existing hours table, destinations in hours / after hours / on holidays, ring groups, queues and their members, voicemail notices, recording, the operator's transfer number, and the departments of smart reception (mode 5).

Only in the panel (or with Voikit's built-in assistant): creating the first phone setup and its hours table, colleague phone users and verifying their mobiles, the phone menu of mode 4, and buying or connecting a phone number.
