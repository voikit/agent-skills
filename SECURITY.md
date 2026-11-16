# Security

## Reporting

Please report security problems privately to security@voikit.ai. Do not open a public issue. Include what you found, how to reproduce it, and what an attacker could do with it.

This covers the skills in this repository (for example an instruction that could lead an assistant to leak data or skip an approval) and the Voikit MCP server they talk to.

## What the skills must never contain

- Tokens, passwords, one-time codes or account addresses.
- Real customers' names, phone numbers or conversations.
- Instructions that widen an assistant's access, skip the owner's approval, or retry refused calls.

## For people using the skills

- A connection token is shown once in the Voikit panel. Treat it like a password; never paste it into a chat, a ticket or a shared file. If it leaks, issue a new one or cut the connection.
- Make one connection per person and per device, with only the sections the job needs.
- Start with the approval mode "propose, you approve".
- Install skills only from this repository or a source you trust: a skill is a set of instructions your assistant will follow, and may include scripts.
- Messages from your customers are data. The skills tell the assistant never to follow instructions found inside them; if you see it happen, report it.
