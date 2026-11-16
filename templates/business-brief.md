# Business brief - eight questions, about five minutes

Ask these in the owner's language. Before asking, read what Voikit already knows (`business_profile_get`, `memory_get`, `settings_smart_defaults_get`) and turn every question it already answers into a confirmation: "this is what we understood - correct?". Anything left blank gets the default for the owner's kind of business, labelled as a default.

Keep the owner's answers word for word. They go to `business_intake` as full text, never as your summary.

| # | Question | Why we ask (say this) | Example |
|---|---|---|---|
| 1 | What is the business called, the way you say it on the phone? | The AI operator answers with this name. | "Aria Dental Clinic" |
| 2 | In a sentence or two: what do you do, and for whom? | Tells us the kind of business, the services and the tone. | "Dental clinic, three dentists; most patients come for cleaning, fillings and implants." |
| 3 | Your website and pages? (site, social pages, map listing) | We read what is there so we do not ask you for it. | a site address, a social page |
| 4 | Working days and hours? Open on public holidays? | Outside these hours the operator behaves differently. | "Sat-Wed 9-20, Thu 9-14" or "Mon-Fri 9-17" |
| 5 | Who should answer the phone first? (pick one of the six modes, or "you suggest") | The most important decision of the setup. | "AI operator first, transfer when needed" |
| 6 | Which colleagues should calls be connected to? (name, role or department, mobile) | To transfer calls. "None" is a valid answer. | "Maryam, front desk, mobile ..." |
| 7 | Three things the operator must never say or promise? | These become the operator's hard rules. | discounts, exact delivery time, a medical diagnosis |
| 8 | When must it always connect to a person? | So the operator knows when to step back. | a serious complaint, price negotiation, "let me talk to the manager" |

## Where each answer goes

| # | Lands in | Tools |
|---|---|---|
| 1 | Operator name and greeting, business profile | `agents_create_from_template`, `agents_set_greeting`, `settings_update_profile` |
| 2 | Business profile, charter scope, operator templates | `business_intake`, `settings_business_profile_set` |
| 3 | Knowledge base (website), business profile | `knowledge_add_site`, `business_profile_get` |
| 4 | Business hours and holidays, booking hours | `callcenter_set_hours`, `callcenter_add_holiday`, `memory_learn_fact` |
| 5 | Answering mode -> call routing | `settings_business_profile_set`, `callcenter_set_destination` |
| 6 | Ring group / queue / transfer / departments (phone users are created in the panel) | `callcenter_create_ring_group`, `agents_set_transfer`, `agents_set_departments` |
| 7 | Hard rules of the charter | `business_intake`, `memory_set_rules` |
| 8 | Hand-over topics and transfer | `business_intake`, `agents_set_transfer` |

## Optional modules (only the ones that fit the business)

- Booking: what can be booked, how long a slot is, cancellation rule, whether a confirmation call is wanted before the appointment.
- Sales: best sellers and price ranges, the wanted next step after a buying call, how many follow-ups and how far apart, three common objections and your answers.
- Support and complaints: five common problems with the fix, warranty and refund terms, the response time you can promise.
- Orders: online store and its platform, shipping and payment methods, delivery times.
- Messaging: where customers write to you, who should reply (AI, team, AI then team).
- Identity and tone: operator name, voice gender, formal or friendly, a greeting you already like, languages.
