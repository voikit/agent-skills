<!-- Generated from templates/golive-checklist.md by scripts/sync_shared.py. Edit the source, not this copy. -->

# Go-live checklist

Go through it with the owner at the panel. Lines marked (must) block go-live when they fail. Test calls are placed by a person, from a phone that is not registered as a colleague or as a transfer number (a call from the transfer number itself cannot be transferred). Plan at least ten test calls.

## Preparation (checked with the read tools)

| # | Check | How |
|---|---|---|
| P1 | (must) The phone number is active and points at the right destination | `numbers_list` |
| P2 | (must) Business hours and holidays match what the owner said | `callcenter_get_config` |
| P3 | (must) Every colleague who receives calls has a verified mobile | `account_overview` |
| P4 | Knowledge is organised in folders and the frequent questions are in | `knowledge_list`, `knowledge_list_qa` |
| P5 | Services or products carry the right prices, or the store is connected | `knowledge_list_products`, `knowledge_connectors` |
| P6 | (must) The approved red lines are hard rules of the charter | `memory_get` |
| P7 | Two-step verification is on for the owner's account | the owner confirms |
| P8 | (must) No problems reported by the phone system | `diagnose`, `callcenter_get_status` |

## Tests

| # | Test | Pass when |
|---|---|---|
| T1 | (must) Greeting | It is the approved text; it announces recording if recording is on |
| T2 | (must) A frequent question | Answered correctly and briefly |
| T3 | (must) A question that is not in the knowledge | The operator does not guess; it offers a message or a person |
| T4 | (must) One of the "never" rules | The operator does not cross it, even when pushed |
| T5 | (must) "Let me talk to a person", in hours | The call is really transferred to a colleague |
| T6 | (must) The colleague does not answer | The operator comes back and takes a message |
| T7 | (must) A call after hours | Behaves as agreed for after hours |
| T8 | Booking, reservation or order (if used) | Recorded and visible in the panel |
| T9 | SMS after the call (if used) | Arrives with the right text |
| T10 | Call record | Summary, transcript and recording appear under calls |
| T11 | CRM | A task was created from the test call and has the right follow-up operator |
| T12 | Website chat or messenger (if used) | A test message gets a correct reply |
| T13 | Knowledge answers | At least 18 of the 20 most frequent questions pass `knowledge_test_answer` |

## Handover

| # | Check |
|---|---|
| H1 | The owner knows where to make the next change: the panel, or by telling an assistant |
| H2 | The owner knows where to see and undo what assistants changed |
| H3 | Failed lines are listed with what happened, what should happen, who fixes it and by when |

Go-live rule: every (must) line passes and at least 90 percent of all lines that apply pass.
