---
name: voikit-appointments
description: >-
  Handle appointments on a Voikit account: check free slots, book and cancel
  for a customer, review the upcoming calendar, let an AI operator take
  bookings on calls and chats, and arrange confirmation calls before an
  appointment. Use when someone says "book an appointment for ...", "what is
  free on Tuesday", "cancel the 3 pm booking", "let the agent take bookings",
  "who is coming tomorrow", "remind patients before their visit", "set up
  reservations", in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected with the Call center section on (appointment tools live there); AI operators and CRM sections for booking by the operator and confirmation calls (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: core
---

# Voikit appointments

Voikit keeps one calendar for the account: working hours for bookings and a slot length. AI operators, the website widget and the team book into it.

Read `references/operating-rules.md` first.

## Use it when / hand off when

- Use it to book, cancel, review, and to switch on booking for an operator.
- Reminder and confirmation calls are CRM follow-ups -> `voikit-crm-followups`.
- Booking hours and slot length are set by the owner in the panel (Appointments settings).

## Before you start

1. `capabilities`.
2. `appointments_list` for the range in question (default: today and the next two weeks).
3. `settings_smart_defaults_get` tells you whether this business takes bookings and the slot length Voikit assumes.

## Workflow

### Book

1. Get: the customer's name and phone, the day, the wanted time, and what it is for.
2. `appointments_availability` for that date. Offer two or three free slots, not the whole day.
3. Repeat the details back. `appointments_create`. The slot is checked again at booking time; if it was taken meanwhile, offer the next ones.
4. Tell the owner whether the customer was told. Booking does not message the customer by itself.

### Cancel

1. Find it with `appointments_list`. Confirm which one with the owner or the customer's own words.
2. `appointments_cancel`. The customer is not messaged automatically: ask the owner whether to tell them, and how (`voikit-conversations` for a reply or SMS).

### Let an operator take bookings

1. Check the operator: `agents_get`.
2. Switch on booking for it with `agents_update` (the appointment booking setting). Show the owner what callers will be asked.
3. Add the rules that fit the business to the charter (`voikit-business-memory`): what must be asked, what cannot be promised.
4. Test a booking call -> `voikit-qa-testing`.

### Confirmation before the appointment

The appointments page sends no reminders by itself. Use an appointment-confirmation operator from the templates (`agents_list_templates`) mapped to the appointment task type, so each booking gets a confirmation call inside calling hours. Set it up in `voikit-crm-followups`.

## Decision rules

- What this calendar does not have: a list of services with their own durations, a calendar per staff member, split shifts or a shorter day, a no-show status. Do not promise them. Write the real schedule (two shifts, a short Thursday) into the charter so the operator says it right.
- Several practitioners or tables with their own schedules: have the operator record a booking request with the person's name and let staff confirm, instead of a firm slot. Say "we will confirm", never "you are booked".
- Restaurants and other places where only the staff know today's capacity: requests, not firm bookings.
- Health, legal and finance: the operator books and stops there; no advice, no triage beyond the emergency rule.
- Times are in the account's time zone. Say the day and date together to avoid off-by-one-day mistakes.

## Show the owner

- Upcoming: a table - date, time, customer, purpose, status.
- A booking: who, when, for what, and "the customer has / has not been told".

## Never

- Book over a taken slot or outside booking hours.
- Cancel on a vague description ("the one tomorrow") when there are several.
- Promise a reminder that nobody set up.
- Read one customer's appointment to another caller.

## If something goes wrong

- No free slots on any day -> the booking settings in the panel (hours, slot length, days) are missing or too narrow.
- The operator does not offer booking -> booking is off for that operator, or the account's booking settings are empty.

## References

- `references/operating-rules.md`
