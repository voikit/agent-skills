#!/usr/bin/env python3
"""Refresh shared/tool-map.json (and tool-map.md): the list of Voikit MCP tools.

The skills never copy tool schemas; they only name tools. This map is what the
lint checks those names against, so a renamed or removed tool is caught.

Two sources:

  # maintainers: from the tool definitions in the product source tree
  python3 scripts/export_tool_map.py --from-source /path/to/tool/definitions

  # anyone: from a live connection (a read-only token is enough)
  VOIKIT_MCP_TOKEN=... python3 scripts/export_tool_map.py --url https://voikit.ai/mcp
"""
import argparse
import datetime
import glob
import json
import os
import re
import sys
import urllib.request

from common import ROOT


def from_source(folder):
    tools = []
    for path in sorted(glob.glob(os.path.join(folder, "*.ts"))):
        src = open(path, encoding="utf-8").read()
        for block in re.split(r"\bdefineTool\(\{", src)[1:]:
            head = re.split(r"\n\s*(?:run|prepare):", block[:8000])[0]
            name = re.search(r'name:\s*"([a-z0-9_]+)"', head)
            surfaces = re.search(r"surfaces:\s*\[([^\]]*)\]", block[:12000])
            if not name or not surfaces or '"mcp"' not in surfaces.group(1):
                continue

            def field(key):
                m = re.search(key + r':\s*"([^"]+)"', head)
                return m.group(1) if m else None

            title = re.search(r'title:\s*\{[^}]*en:\s*"([^"]*)"', head)
            tools.append(
                {
                    "name": name.group(1),
                    "domain": field("domain"),
                    "kind": field("kind"),
                    "risk": field("risk"),
                    "sensitive": bool(re.search(r"sensitive:\s*true", head)),
                    "customer_facing": bool(re.search(r"customerFacing:\s*true", head)),
                    "risk_reducer": bool(re.search(r"riskReducer:\s*true", head)),
                    "title": title.group(1) if title else "",
                }
            )
    return tools


def rpc(url, token, session, method, params=None, notify=False):
    body = {"jsonrpc": "2.0", "method": method}
    if params is not None:
        body["params"] = params
    if not notify:
        body["id"] = 1
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "Authorization": "Bearer " + token,
    }
    if session:
        headers["Mcp-Session-Id"] = session
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=60) as res:
        session = res.headers.get("Mcp-Session-Id") or session
        raw = res.read().decode("utf-8")
    if notify or not raw.strip():
        return None, session
    if raw.lstrip().startswith("{"):
        return json.loads(raw), session
    for line in raw.splitlines():  # server-sent events
        if line.startswith("data:"):
            msg = json.loads(line[5:].strip())
            if msg.get("id") == 1:
                return msg, session
    raise SystemExit("no JSON-RPC answer from the server")


def from_live(url):
    token = os.environ.get("VOIKIT_MCP_TOKEN")
    if not token:
        sys.exit("set VOIKIT_MCP_TOKEN (never pass a token on the command line)")
    init = {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "voikit-agent-skills", "version": "0.1.0"}}
    _, session = rpc(url, token, None, "initialize", init)
    rpc(url, token, session, "notifications/initialized", notify=True)
    tools, cursor = [], None
    while True:
        msg, session = rpc(url, token, session, "tools/list", {"cursor": cursor} if cursor else {})
        result = msg.get("result") or {}
        for t in result.get("tools", []):
            meta, ann = t.get("_meta") or {}, t.get("annotations") or {}
            tools.append(
                {
                    "name": t["name"],
                    "domain": meta.get("ai.voikit/domain"),
                    "kind": meta.get("ai.voikit/kind"),
                    "risk": meta.get("ai.voikit/risk"),
                    "sensitive": bool(ann.get("destructiveHint")),
                    "customer_facing": None,
                    "risk_reducer": None,
                    "title": t.get("title") or "",
                }
            )
        cursor = result.get("nextCursor")
        if not cursor:
            return tools


def write(tools, source):
    tools.sort(key=lambda t: (t["domain"] or "", t["name"]))
    out = {"generated": datetime.date.today().isoformat(), "source": source, "count": len(tools), "tools": tools}
    with open(os.path.join(ROOT, "shared", "tool-map.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=True)
        f.write("\n")
    lines = ["# Voikit MCP tools", "", f"Generated {out['generated']} from {source}. {len(tools)} tools. Do not edit by hand.", ""]
    lines += ["A connection only sees the tools its role, sections, approval mode and plan allow;", "`capabilities` is the truth for one connection.", ""]
    domain = None
    for t in tools:
        if t["domain"] != domain:
            domain = t["domain"]
            lines += ["", f"## {domain}", "", "| Tool | Kind | Risk | Notes | What it is |", "|---|---|---|---|---|"]
        notes = [n for n, on in (("always owner-approved", t["sensitive"]), ("reaches customers", t["customer_facing"]), ("risk reducer", t["risk_reducer"])) if on]
        lines.append(f"| `{t['name']}` | {t['kind'] or ''} | {t['risk'] or ''} | {', '.join(notes)} | {t['title']} |")
    with open(os.path.join(ROOT, "shared", "tool-map.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"wrote shared/tool-map.json and shared/tool-map.md ({len(tools)} tools)")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--from-source", metavar="DIR", help="folder with the tool definition files")
    g.add_argument("--url", help="a Voikit MCP endpoint, e.g. https://voikit.ai/mcp")
    a = p.parse_args()
    if a.from_source:
        tools = from_source(a.from_source)
        if not tools:
            sys.exit("no tool definitions found in " + a.from_source)
        write(tools, "source definitions")
    else:
        write(from_live(a.url), "live tools/list")


if __name__ == "__main__":
    main()
