---
name: voikit-knowledge-base
description: >-
  Give a Voikit account's AI operators correct answers: organise the knowledge
  base in folders, add the website, write approved question-and-answer pairs,
  enter products and prices, connect and test a store or site connector, and
  prove the result with answer tests. Use when someone says "add my FAQ",
  "import my website", "add my products / price list", "the agent answers
  wrong", "it does not know our address", "connect my WooCommerce / store",
  "organise the knowledge base", in any language.
license: Apache-2.0
compatibility: Needs the Voikit MCP server connected with the Knowledge base section on (see voikit-mcp).
metadata:
  version: "0.1.0"
  tier: core
---

# Voikit knowledge base

Knowledge is what the operators answer from: texts, website pages, files, question-and-answer pairs, products and live data from a connected store. Rules about behaviour (never promise, tone) are not knowledge; they belong to `voikit-business-memory`.

Read `references/operating-rules.md` first.

## Use it when / hand off when

- Use it to add, fix, organise or test what the AI knows.
- "Never say / always say / our return policy is" -> `voikit-business-memory`. When the owner pours out everything at once (facts, rules, tone together), pass the whole text to `business_intake`: it files each piece where it belongs.
- Which knowledge one operator uses -> `voikit-ai-agents`.

## Before you start

1. `capabilities`, then `knowledge_list` (items and the folder tree), `knowledge_list_qa`, `knowledge_list_products`.
2. `business_profile_get`: what Voikit already learned from the site and pages - offerings, prices, frequent questions, hours.
3. `knowledge_connectors` if the business has an online store.

## Workflow

1. **Folders.** One folder per area of the business the owner thinks in (services, prices, branches, shipping, a product line). `knowledge_create_folder`, then `knowledge_move`. Three to seven folders is typical; do not build a deep tree.
2. **Website.** `knowledge_add_site` for the public site. It is read in the background and counts against the plan's monthly crawl quota: add the site once, not page by page, and check `knowledge_list` later.
3. **Frequent questions.** Collect the twenty questions customers really ask (the profile's frequent questions, the owner's list, the inbox). Draft answers only from the profile, the site and the owner's words. Show them; on approval `knowledge_add_qa`.
4. **Products and services.** `knowledge_create_product` with title, description, price and category for what is sold or booked. For a store with many products prefer the connector.
5. **Texts.** How a service works, the company's story, a process: `knowledge_add_text`; change with `knowledge_update_text`.
6. **Store connector.** The owner installs the connector on their site (panel-only). Then `knowledge_connector_test` checks both directions and `knowledge_connector_sync` asks for a fresh send.
7. **Prove it.** `knowledge_test_answer` on the twenty questions: the exact answer, how sure it was, which items it used. Each test counts as one AI chat message, so test the list once, fix, and retest only the failures.
8. **Attach.** For phone operators make sure the right items or folders are selected (`agents_list_knowledge`, then `agents_update`). Selecting a folder means everything in it.

## Decision rules

- Question-and-answer matching leans on wording. For every question add the alternatives customers actually use (colloquial, short, misspelt) with `knowledge_update_qa`.
- One fact, one place. If the price is in a product, do not repeat it in a text and a Q&A; duplicates drift apart.
- Prices: follow the owner's price policy from the profile (exact, ranges, or never on the phone). If it is "never", no prices go into knowledge at all.
- A wrong answer has three possible causes; test in this order: the fact is missing, the wording does not match, the operator is not using that item.
- An answer the owner must give (a policy, a guarantee) is never drafted by you: ask.
- Files (PDF, Word, Excel, images) are uploaded by the owner in the panel; offer to prepare the list of what to upload and into which folder.

## Show the owner

- Before adding: the drafts, grouped by folder, with the source of each ("from your site", "your words").
- After testing: a table - question, answer given, pass or fail, what you changed.
- The storage and crawl quotas are the plan's; say when one is close instead of failing silently.

## Never

- Invent a price, an opening hour, an address or a policy.
- Delete in bulk without the owner asking. `knowledge_delete_products` cannot be undone and always waits for the owner. With `knowledge_delete_item` a text can be restored, a file or a site cannot. `knowledge_delete_qa` can be restored.
- Put customers' personal details into knowledge.
- Add the same site twice.

## If something goes wrong

- The site shows no pages yet -> reading is still running; check `knowledge_list` again later.
- The connector test fails -> report which direction failed and the hint; the fix is on the owner's site.
- The answer test is right but the phone operator is wrong -> that operator's knowledge selection.

## References

- `references/operating-rules.md`
