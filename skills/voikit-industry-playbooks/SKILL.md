---
name: voikit-industry-playbooks
description: >-
  Ready Voikit setup layouts for common kinds of business - clinic, online
  shop, B2B and software company, school or training centre, real-estate
  agency, restaurant and cafe, field service, and a company with several
  departments: the answering mode that fits, which AI operators to build, the
  knowledge folders and first questions, CRM follow-ups, sample red lines and
  the gap questions to ask. Use when someone says "set up Voikit for a dental
  clinic / shop / restaurant / agency ...", "what is the best setup for my
  kind of business", "give me a template for ...", or when another Voikit
  skill needs sensible defaults for a business type, in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected to apply a layout; can be used without it to plan (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: core
---

# Voikit industry playbooks

A playbook is a starting layout, not a script. Voikit itself fits the panel to the kind of business (smart defaults); the playbook tells you what to expect, what to check and what to ask.

Read `references/operating-rules.md` first. Answering modes are in `references/answering-modes.md`.

## How to use a playbook

1. `settings_smart_defaults_get`: the kind of business Voikit recorded, team, hours, booking, price policy, and every setting with its recommended value and why. If the kind of business is wrong, fix it first with `settings_business_profile_set`; everything else follows from it.
2. Pick the nearest playbook below. Compare its "typical business" with the real one and note every difference (bigger team, open at night, no booking).
3. Present the layout to the owner as a proposal with every default labelled. Ask only the gap questions.
4. Build with the area skills, in the order of `voikit-onboarding`.
5. Sample red lines are suggestions for the owner to accept, edit or drop. They become rules only in the owner's words.

## The playbooks

Mode numbers refer to the six answering modes.

### Clinic and health practice
- Mode 2. The operator answers frequent questions and records a booking request with the practitioner's name; staff confirm. One shared calendar cannot hold each practitioner's schedule.
- Operators: reception; appointment confirmation calls before the visit.
- Knowledge: services, price ranges, accepted insurers, practitioners and days, address and parking, preparation before a visit.
- Sample red lines: no diagnosis, no reading of test results, no medication advice; emergencies go to the emergency number at once; no other patient's information; price ranges only before examination; no promise of treatment results.
- Check: prices "approximate only"; recording announced; two-step verification on. Regulated field.
- Ask: which practitioners on which days; which insurers; what counts as urgent.

### Online shop
- Mode 2, and after hours the operator answers fully: evenings and weekends are shopping time.
- Operators: order support and status; unfinished-order or sales follow-up if wanted.
- Knowledge: store connector for orders, products and prices; shipping, returns, payment.
- Sample red lines: no firm stock or delivery promise without live data; no discount outside the recorded ones; order details only to the buyer; refunds are recorded, not promised.
- Check: connector test passes with a real order; exact prices; a second board for after-sales; booking off.
- Ask: store platform; return window; who handles refunds and wholesale.

### B2B and software company
- Mode 5 (smart reception): business callers often do not know whether their issue is technical or financial.
- Operators: reception that identifies existing customer, new customer, finance or supplier, takes company, person, subject and urgency, and states the response time.
- Knowledge: products and plans, the response-time commitment, a technical guide for the five most common problems.
- Sample red lines: no project price or contract promise; no fix or delivery time without the technical team; response time only as committed; calls for the chief executive end in a message.
- Check: every department has numbers and a "connect when" sentence; two boards (sales, support); recording on and announced.
- Ask: departments and who is in each; the response time you commit to; what is an outage.

### School and training centre
- Mode 2, full answers after hours. Calls come at lunch and in the evening.
- Operators: course information and consultation booking; follow-up of unfinished registrations.
- Knowledge: courses, schedules, exact fees as products, registration steps, placement.
- Sample red lines: no promise of exam results or grades; no fee or discount outside the recorded ones; no level placement on the phone; refunds go to finance; from a parent ask only the child's age and level.
- Check: two shifts and the short day written in the charter (booking settings hold one range).
- Ask: current courses and fees; how registration is completed; who handles withdrawals.

### Real-estate agency
- Mode 2. Before any transfer the operator asks: buy, rent or lease; area; budget; size and rooms; then repeats them back.
- Operators: lead qualification; viewing confirmation the day before.
- Knowledge: the areas the office covers, the process, fees. No listings with prices.
- Sample red lines: no firm price or availability of a specific property; no loan or bank advice; no owner's or other clients' details; negotiation goes to the agent.
- Check: price policy set to "never on the phone"; the caller's details land on the CRM task; a returning client reaches the same agent.
- Ask: areas covered; which agent handles which kind of deal; viewing hours.

### Restaurant and cafe
- Mode 2. Menu and prices are exact; a reservation is a request the floor manager confirms.
- Operators: reservations and information.
- Knowledge: menu with prices, hours, delivery area and fee, allergens as recorded.
- Sample red lines: no firm table or dish availability; no exact courier time; allergy questions only from recorded facts, otherwise "we will check with the kitchen"; events and group bookings go to a person.
- Check: weekend days are working days; the break between shifts is in the charter; recording set as the owner wants.
- Ask: capacity rules; delivery area; who confirms reservations.

### Field service (repairs, installation, maintenance)
- Mode 2. The operator checks the service area first, then takes: problem, exact address, suitable time, name, number.
- Operators: service-request intake; confirmation call before the technician arrives.
- Knowledge: service area by district, visit fee, price ranges, usual dispatch time.
- Sample red lines: danger to life or a gas leak goes to the emergency number at once; no firm repair price before the visit; no exact arrival time unless recorded; no repair instructions by phone; out-of-area requests are declined honestly.
- Check: prices "approximate only"; a board for service requests the dispatcher sees.
- Ask: areas served; visit fee; how fast you usually send someone.

### Company with several departments
- Mode 4 (phone menu) when callers know their department, mode 5 when they do not. Decide on purpose.
- Operators: reception; one per department only if the departments' jobs really differ.
- Knowledge: one folder per department.
- Sample red lines: no price or delivery promise without sales; no managers' direct numbers; when the department is unclear, ask one short question, never guess.
- Check: menu of five options at most with key 0 to the AI operator; busy departments have a queue whose wait ends at the AI operator; two boards; formal tone.
- Ask: departments, members and hours; which department takes unclear calls.

## Other kinds of business

- Legal, financial and insurance services: follow the clinic pattern for consultations; regulated; no advice, no rates, no promised outcomes.
- Car repair -> clinic pattern; car sales -> real estate; roadside help -> field service, around the clock.
- Hotels -> restaurant pattern, around the clock and more formal. Pharmacies -> online shop.
- Anything else: choose by team size and by whether callers book, buy or ask.

## Never

- Apply a playbook without showing it, or keep a default the owner contradicted.
- Copy sample red lines into the charter unconfirmed.
- Promise a feature because a playbook mentions it; check `feature_availability`.

## References

- `references/operating-rules.md`, `references/answering-modes.md`
