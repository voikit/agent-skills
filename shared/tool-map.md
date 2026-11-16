# Voikit MCP tools

Generated 2026-11-16 from source definitions. 180 tools. Do not edit by hand.

A connection only sees the tools its role, sections, approval mode and plan allow;
`capabilities` is the truth for one connection.


## account

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `account_overview` | read |  |  | Account overview |
| `ask_ava` | read |  |  | Ask Ava |
| `cancel_change` | control |  |  | Withdraw a pending change |
| `capabilities` | read |  |  | What this connection can do |
| `diagnose` | read |  |  | Diagnose calls |
| `feature_availability` | read |  |  | Is a feature available here? |
| `fetch` | read |  |  | Fetch a record |
| `get_change` | control |  |  | Status of a change |
| `list_changes` | control |  |  | List proposed changes |
| `list_safe_points` | control |  |  | Safe points |
| `revert_change` | control |  |  | Revert an applied change |
| `save_safe_point` | control |  |  | Save a safe point |
| `search` | read |  |  | Search the account |
| `search_help` | read |  |  | Search Voikit help |
| `support_create_ticket` | control |  |  | Open a support ticket |
| `support_departments` | read |  |  | Voikit support departments |
| `support_get_ticket` | read |  |  | One support ticket |
| `support_list_tickets` | read |  |  | Support tickets |
| `support_reply_ticket` | control |  |  | Reply on a support ticket |
| `support_solve_ticket` | control |  |  | Mark a support ticket solved |

## agents

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `agents_add_rule` | write | low |  | Add an operator rule |
| `agents_create` | write | medium |  | Create an operator |
| `agents_create_from_template` | write | medium |  | Create an operator from a template |
| `agents_edit_prompt` | write | medium |  | Edit the system prompt |
| `agents_get` | read |  |  | Operator details |
| `agents_list` | read |  |  | AI operators |
| `agents_list_knowledge` | read |  |  | Knowledge items |
| `agents_list_models` | read |  |  | Allowed AI models |
| `agents_list_templates` | read |  |  | Voikit agent templates |
| `agents_list_voices` | read |  |  | Available voices |
| `agents_retire` | write | high |  | Retire an operator |
| `agents_set_active` | write | medium |  | Switch an operator on / off |
| `agents_set_departments` | write | medium |  | Smart-reception departments |
| `agents_set_greeting` | write | low |  | Operator greeting |
| `agents_set_name` | write | low |  | Operator name |
| `agents_set_transfer` | write | medium |  | Transfer to a colleague |
| `agents_update` | write | medium |  | Update an operator |

## billing

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `billing_get_balance` | read |  |  | Credit & plan |
| `billing_list_transactions` | read |  |  | Credit transactions |

## callcenter

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `appointments_availability` | read |  |  | Free slots |
| `appointments_cancel` | write | medium |  | Cancel an appointment |
| `appointments_create` | write | low |  | Book an appointment |
| `appointments_list` | read |  |  | Appointments |
| `callcenter_add_holiday` | write | medium |  | Add a holiday |
| `callcenter_create_queue` | write | medium |  | Create a queue |
| `callcenter_create_ring_group` | write | medium |  | Create a ring group |
| `callcenter_get_config` | read |  |  | Call-center configuration |
| `callcenter_get_status` | read |  |  | Phone system status |
| `callcenter_remove_holiday` | write | medium |  | Remove a holiday |
| `callcenter_set_destination` | write | high |  | Destination in / after hours |
| `callcenter_set_hours` | write | medium |  | Change business hours |
| `callcenter_set_queue_members` | write | medium |  | Queue members |
| `callcenter_set_recording` | write | medium |  | Call recording |
| `callcenter_set_voicemail_notify` | write | low |  | Voicemail notices |
| `callcenter_update_queue` | write | medium |  | Update a queue |
| `callcenter_update_ring_group` | write | medium |  | Update a ring group |
| `calls_list` | read |  |  | Recent calls |
| `numbers_list` | read |  |  | Phone numbers |
| `numbers_set_route` | write | high |  | Where a number's calls go |

## campaigns

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `campaigns_get` | read |  |  | One campaign |
| `campaigns_how_to_start` | read |  |  | How a campaign is started |
| `campaigns_list` | read |  |  | Campaigns |
| `campaigns_pause` | write | low | risk reducer | Pause a campaign |
| `campaigns_stop` | write | medium | risk reducer | Stop a campaign |

## contacts

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `contacts_search` | read |  |  | Search contacts |
| `contacts_set_profile` | write | low |  | Contact name & notes |
| `contacts_timeline` | read |  |  | A contact's timeline |

## conversations

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `automations_activity` | read |  |  | Recent comments and what happened |
| `automations_create` | write | medium | always owner-approved | Create a comment rule |
| `automations_delete` | write | medium | always owner-approved | Delete a comment rule |
| `automations_entry_points` | write | medium | always owner-approved | Instagram ice breakers and chat menu |
| `automations_entry_points_get` | read |  |  | Read Instagram ice breakers and menu |
| `automations_list` | read |  |  | Instagram comment rules |
| `automations_media` | read |  |  | Instagram posts and reels |
| `automations_media_upload` | control |  |  | Upload a file for a rule |
| `automations_reorder` | write | medium | always owner-approved | Order the comment rules |
| `automations_review_decide` | write | medium | always owner-approved, reaches customers | Approve or reject a comment reply |
| `automations_reviews` | read |  |  | Replies waiting for approval |
| `automations_settings` | write | low |  | Pause all rules / hide spam |
| `automations_test` | read |  |  | Test the comment rules |
| `automations_toggle` | write | medium |  | Turn a comment rule on or off |
| `automations_update` | write | medium | always owner-approved | Change a comment rule |
| `conversations_add_note` | write | low |  | Internal note on a conversation |
| `conversations_assign` | write | low |  | Assign a conversation |
| `conversations_get` | read |  |  | One conversation with messages |
| `conversations_list` | read |  |  | Conversations |
| `conversations_reply` | write | medium | always owner-approved, reaches customers | Reply to the customer |
| `conversations_set_mode` | write | low |  | Hand over to a human / back to AI |
| `conversations_set_status` | write | low |  | Set conversation status |
| `leads_analyze` | control |  |  | Read a lead's conversation again |
| `leads_get` | read |  |  | One lead with its timeline |
| `leads_list` | read |  |  | Instagram leads |
| `leads_opt_out` | write | medium |  | Stop automatic messages to a lead |
| `leads_set_stage` | write | low |  | Move a lead to a stage |
| `leads_settings_get` | read |  |  | Lead and follow-up settings |
| `leads_settings_update` | write | medium | always owner-approved | Change lead and follow-up settings |
| `leads_suggestion` | write | low |  | Confirm the number the assistant saw |
| `showcases_create` | write | low |  | Create a product showcase |
| `showcases_delete` | write | medium | always owner-approved | Delete a product showcase |
| `showcases_list` | read |  |  | Product showcases |
| `showcases_send` | write | medium | always owner-approved, reaches customers | Send a showcase to a customer |
| `showcases_update` | write | low |  | Change a product showcase |

## crm

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `crm_add_comment` | write | low |  | Add a note to a task |
| `crm_cancel_ai_call` | write | low | risk reducer | Cancel a scheduled call |
| `crm_close_task` | write | low |  | Close a task |
| `crm_create_customer` | write | low |  | Create a customer |
| `crm_create_task` | write | low |  | Create a CRM task |
| `crm_get_customer` | read |  |  | Customer file |
| `crm_get_task` | read |  |  | Task detail |
| `crm_list_customers` | read |  |  | Customers |
| `crm_list_pipelines` | read |  |  | Pipelines & stages |
| `crm_list_tasks` | read |  |  | CRM tasks |
| `crm_move_task` | write | low |  | Move a task to a stage |
| `crm_reopen_task` | write | low |  | Reopen a task |
| `crm_schedule_ai_call` | write | medium | always owner-approved, reaches customers | Schedule an AI follow-up call |
| `crm_set_assignees` | write | medium |  | Set a task's assignees |
| `crm_set_followup_agent` | write | low |  | Follow-up agent per task type |
| `crm_task_by_code` | read |  |  | Task by tracking code |
| `crm_update_task` | write | low |  | Update a task |

## flows

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `flows_attach` | write | medium |  | Attach a flow to an operator |
| `flows_create` | write | medium |  | Create a flow |
| `flows_delete` | write | high |  | Delete a flow |
| `flows_edit` | write | medium |  | Edit flow nodes |
| `flows_forms` | read |  |  | Forms |
| `flows_get` | read |  |  | Flow details |
| `flows_list` | read |  |  | Flows |
| `flows_node_types` | read |  |  | Flow node types |
| `flows_set_active` | write | medium |  | Switch a flow on/off |
| `flows_templates` | read |  |  | Flow templates |
| `flows_update` | write | medium |  | Replace a flow |
| `flows_validate` | read |  |  | Validate a flow |
| `forms_create` | write | low |  | Create a form |
| `forms_delete` | write | high |  | Delete a form |
| `forms_get` | read |  |  | Form detail |
| `forms_list` | read |  |  | Forms |
| `forms_set_active` | write | medium |  | Switch a form on or off |
| `forms_submissions` | read |  |  | Form answers |
| `forms_update` | write | low |  | Edit a form |

## knowledge

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `business_intake` | write | low |  | Take in what the owner says about the business |
| `business_profile_get` | read |  |  | Business profile |
| `knowledge_add_qa` | write | low |  | Add a Q&A |
| `knowledge_add_site` | write | medium |  | Add a website to read |
| `knowledge_add_text` | write | low |  | Add a text to the knowledge |
| `knowledge_connector_sync` | write | low |  | Full sync of a connection |
| `knowledge_connector_test` | read |  |  | Test a site connection |
| `knowledge_connectors` | read |  |  | Site & store connections |
| `knowledge_create_folder` | write | low |  | Create a knowledge folder |
| `knowledge_create_product` | write | low |  | Add a product |
| `knowledge_delete_item` | write | high |  | Delete a knowledge item |
| `knowledge_delete_products` | write | high | always owner-approved | Delete products |
| `knowledge_delete_qa` | write | medium |  | Delete a Q&A |
| `knowledge_list` | read |  |  | Knowledge items and folders |
| `knowledge_list_products` | read |  |  | Products |
| `knowledge_list_qa` | read |  |  | Knowledge Q&A |
| `knowledge_move` | write | low |  | Move into a folder |
| `knowledge_test_answer` | read |  |  | Test a customer answer |
| `knowledge_update_product` | write | low |  | Update a product |
| `knowledge_update_qa` | write | low |  | Update a Q&A |
| `knowledge_update_text` | write | low |  | Update a knowledge text |
| `learning_decide` | write | medium |  | Decide a learning proposal |
| `learning_list_findings` | read |  |  | Learning proposals |
| `memory_feedback` | read |  |  | Feedback on the assistant's answers |
| `memory_get` | read |  |  | Business memory (charter) |
| `memory_learn_fact` | write | low |  | Remember a business fact |
| `memory_remove_rule` | write | medium |  | Remove a business rule |
| `memory_rollback` | write | medium |  | Restore a business memory version |
| `memory_set_policies` | write | medium |  | Several business policies at once |
| `memory_set_policy` | write | medium |  | A business policy |
| `memory_set_rule` | write | medium |  | Add or change a business rule |
| `memory_set_rules` | write | medium |  | Several business rules at once |
| `memory_versions` | read |  |  | Business memory history |

## reports

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `reports_summary` | read |  |  | Report summary |

## settings

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `settings_business_profile_set` | write | medium |  | Correct the business profile |
| `settings_get` | read |  |  | Account settings |
| `settings_smart_defaults_apply` | write | medium |  | Apply smart defaults |
| `settings_smart_defaults_get` | read |  |  | Smart defaults |
| `settings_update_profile` | write | medium |  | Update the account profile |

## sms

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `sms_list` | read |  |  | Sent SMS |
| `sms_send` | write | medium | always owner-approved, reaches customers | Send an SMS |

## team

| Tool | Kind | Risk | Notes | What it is |
|---|---|---|---|---|
| `team_list_members` | read |  |  | Team members |
