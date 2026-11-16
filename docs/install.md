# Install and connect

Two parts: give your assistant the skills, and connect it to your Voikit account.

## Part 1 - the skills

A skill is a folder with a `SKILL.md` file. Every folder under `skills/` works on its own. Install `voikit-mcp` first; it teaches the assistant how to check the connection and change things safely.

### Claude (web, desktop, mobile)

- Easiest: paste this repository's address into a chat and ask Claude to install the Voikit skills.
- Or upload a skill zip in your skills settings. One zip per skill.

### ChatGPT

- Open Skills, choose Create, then Upload from your computer, and pick a skill zip. Repeat for each skill you want.
- Skills must be enabled for your account or workspace.

### Claude Code

```
/plugin marketplace add voikit/agent-skills
/plugin install voikit@voikit-agent-skills
```

Or copy the folders:

```
git clone https://github.com/voikit/agent-skills.git
cp -r agent-skills/skills/voikit-* ~/.claude/skills/
```

For one project only, copy them into that project's `.claude/skills/`.

### Other Agent Skills clients (Codex, Cursor and others)

Copy the folders in `skills/` into the client's skills directory. If the client has no skills support, paste one `SKILL.md` (and its `references/operating-rules.md`) at the top of a chat; it then works as a mode, without the optional scripts.

### Where the zips come from

From the Releases page of this repository, or build them:

```
python3 scripts/build_release.py
```

`dist/<skill>.zip` holds one skill; `dist/voikit-agent-skills.zip` holds all of them.

## Part 2 - the Voikit connector

The Voikit MCP server is at `https://voikit.ai/mcp`. If you sign in to Voikit on another Voikit domain, use that domain; the panel page **Tools > AI agents (MCP)** shows your exact address.

### Claude and ChatGPT (sign-in, no token)

1. In the assistant, add a custom connector (a remote MCP server) and enter the server address.
2. You are sent to Voikit to sign in.
3. On the page "an AI assistant wants to connect to your account", choose the role, the sections it may use and the approval mode, then allow it.

### Claude Code, Cursor and other clients with a config file (token)

1. In the Voikit panel open **Tools > AI agents (MCP)** and start a new connection.
2. Choose the client, a name you will recognise ("Sara's laptop"), the role, the sections, the approval mode, the limits and the expiry.
3. Copy the token and the ready command shown for your client. The token is shown only once.

### Choices that keep you safe

| Choice | Recommended start |
|---|---|
| Approval mode | "Propose, you approve": every change waits for your yes in the panel |
| Sections | Only what the job needs; you can add more later |
| Expiry | 90 days |
| Connections | One per person and per device |

You can pause or cut a connection at any time, and see and undo everything it changed, on the same panel page.

## Check that it works

Ask the assistant: "Check my Voikit connection and tell me what you can do." It should call `capabilities` and answer with the sections that are on and the approval mode. Then try: "Set up Voikit for my business."

## Using the skills in your language

Write to the assistant in your own language. The skills are written in English, and they tell the assistant to answer in the language you use and to write greetings, rules and messages in the language your customers use.
