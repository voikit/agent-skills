# Install and connect

## The short way

1. Download `voikit.zip` from the latest release: https://github.com/voikit/agent-skills/releases/latest/download/voikit.zip
2. Add it to your assistant (Claude: skills settings; ChatGPT: Skills > Create > Upload from your computer).
3. Say "Connect my Voikit account". The skill guides you step by step. Then say what you need.

The rest of this page is the detail behind those three steps.

## Part 1 - the skills

A skill is a folder with a `SKILL.md` file. `voikit.zip` is one skill, named `voikit`, that carries every guide; it is what most people should install. Every folder under `skills/` is also a skill of its own, for people who want only some of them. Do not install both the one-file skill and the separate ones: the assistant would see everything twice.

### Claude (web, desktop, mobile)

- Upload `voikit.zip` in your skills settings.
- Or paste this repository's address into a chat and ask Claude to install the Voikit skill.

- Paste-in prompt: "Install the Voikit skill from https://github.com/voikit/agent-skills (the file bundle/voikit.md), then help me connect my Voikit account."

### ChatGPT

- Open Skills, choose Create, then Upload from your computer, and pick `voikit.zip`.
- Or ask in a chat: "Create a skill from this file, exactly as written, and install it: https://raw.githubusercontent.com/voikit/agent-skills/main/bundle/voikit.md".
- Skills must be enabled for your account or workspace.

### Claude Code

```
/plugin marketplace add voikit/agent-skills
/plugin install voikit@voikit-agent-skills
```

The plugin includes the Voikit connector: run `/mcp` and sign in when asked. Or copy the folders:

```
git clone https://github.com/voikit/agent-skills.git
cp -r agent-skills/skills/voikit-* ~/.claude/skills/
```

For one project only, copy them into that project's `.claude/skills/`.

### Other Agent Skills clients (Codex, Cursor and others)

Run `npx skills add voikit/agent-skills`, or copy the folders in `skills/` into the client's skills directory. If the client has no skills support, paste `bundle/voikit.md` at the top of a chat; it then works as a mode, without the guides and the optional scripts.

### Where the zips come from

From the Releases page of this repository, or build them:

```
python3 scripts/build_release.py
```

`dist/voikit.zip` is the one-file skill; `dist/<skill>.zip` holds one skill; `dist/voikit-agent-skills.zip` holds the folders as they are.

## Part 2 - the Voikit connector

The connector address is the address you sign in to Voikit with, plus `/mcp`: `https://voikit.ai/mcp` or `https://voikit.com/mcp`. The panel page **Tools > AI agents (MCP)** shows your exact address.

You do not have to follow the steps below by hand: with the skill installed, say "Connect my Voikit account" and the assistant guides you.

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
