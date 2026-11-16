#!/usr/bin/env python3
"""Lint the skills. Standard library only; no network.

Checks
  - frontmatter: name == folder, name pattern, description length and a "Use" trigger
  - SKILL.md is at most 500 lines
  - every file the SKILL.md points to (references/, assets/, scripts/) exists
  - every tool name written in backticks exists in shared/tool-map.json
  - text is plain ASCII (the skills are English; the assistant translates at run time)
  - no banned term (suppliers, engines, internal names) appears anywhere
  - copies of shared files are in sync

Banned terms are deliberately NOT stored in this public repo. They are read from
  .banned-terms.local   (one term per line, git-ignored), and / or
  VOIKIT_BANNED_TERMS   (comma-separated; used by CI from a secret)
"""
import json
import os
import re
import subprocess
import sys

from common import ROOT, SKILLS_DIR, parse_frontmatter, read, skill_names

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TOKEN_RE = re.compile(r"`([a-z][a-z0-9]*(?:_[a-z0-9]+)+)`")
POINTER_RE = re.compile(r"\b((?:references|assets|scripts)/[A-Za-z0-9._-]+)")
TEXT_EXT = (".md", ".py", ".json", ".yml", ".yaml", ".txt")
SKIP_DIRS = {".git", "dist", "node_modules", "__pycache__"}

errors = []


def err(path, msg):
    errors.append(f"{os.path.relpath(path, ROOT)}: {msg}")


def load_tools():
    path = os.path.join(ROOT, "shared", "tool-map.json")
    if not os.path.exists(path):
        print("warning: shared/tool-map.json is missing; tool names are not checked")
        return None
    return {t["name"] for t in json.loads(read(path))["tools"]}


def load_allow():
    path = os.path.join(ROOT, "scripts", "lint-allow.txt")
    return {l.strip() for l in read(path).splitlines() if l.strip() and not l.startswith("#")}


def load_banned():
    terms = []
    local = os.path.join(ROOT, ".banned-terms.local")
    if os.path.exists(local):
        terms += [l.strip() for l in read(local).splitlines()]
    terms += os.environ.get("VOIKIT_BANNED_TERMS", "").split(",")
    return [t.strip().lower() for t in terms if t.strip() and not t.strip().startswith("#")]


def text_files():
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(TEXT_EXT) and f != ".banned-terms.local":
                yield os.path.join(base, f)


def check_skill(name, tools, allow):
    path = os.path.join(SKILLS_DIR, name, "SKILL.md")
    text = read(path)
    meta, body = parse_frontmatter(text)
    if meta is None:
        return err(path, "no frontmatter")
    if meta.get("name") != name:
        err(path, f"frontmatter name {meta.get('name')!r} != folder {name!r}")
    if not NAME_RE.match(name) or len(name) > 64:
        err(path, "bad skill name")
    desc = meta.get("description", "")
    if not 40 <= len(desc) <= 1024:
        err(path, f"description length {len(desc)} (want 40-1024)")
    if "Use " not in desc:
        err(path, 'description must say when to use the skill ("Use when ...")')
    if "<" in desc or ">" in desc:
        err(path, "description must not contain angle brackets")
    if not isinstance(meta.get("metadata"), dict) or meta["metadata"].get("tier") not in ("core", "premium"):
        err(path, "metadata.tier must be core or premium")
    if text.count("\n") > 500:
        err(path, "SKILL.md is longer than 500 lines")
    for rel in sorted(set(POINTER_RE.findall(body))):
        if not os.path.exists(os.path.join(SKILLS_DIR, name, rel)):
            err(path, f"points to a missing file: {rel}")
    if "references/operating-rules.md" not in body:
        err(path, "must tell the assistant to read references/operating-rules.md")


def check_tool_names(path, tools, allow):
    if tools is None:
        return
    prefixes = {t.split("_")[0] for t in tools if "_" in t}
    for tok in sorted(set(TOKEN_RE.findall(read(path)))):
        if tok in tools or tok in allow:
            continue
        if tok.split("_")[0] in prefixes:
            err(path, f"`{tok}` looks like a tool name but is not in shared/tool-map.json")


def main():
    tools, allow, banned = load_tools(), load_allow(), load_banned()
    names = skill_names()
    if not names:
        err(SKILLS_DIR, "no skills found")
    for name in names:
        check_skill(name, tools, allow)
    for path in text_files():
        rel = os.path.relpath(path, ROOT)
        text = read(path)
        if not rel.startswith(os.path.join("shared", "tool-map")):  # generated from the product
            for i, line in enumerate(text.splitlines(), 1):
                bad = [c for c in line if ord(c) > 126 or (ord(c) < 32 and c != "\t")]
                if bad:
                    err(path, f"line {i}: non-ASCII character {bad[0]!r}")
                    break
        low = text.lower()
        for term in banned:
            if re.search(r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])", low):
                err(path, "contains a banned term (see .banned-terms.local)")
                break
        if path.endswith(".md") and not rel.startswith(os.path.join("shared", "tool-map")):
            check_tool_names(path, tools, allow)
    sync = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "sync_shared.py"), "--check"], capture_output=True, text=True)
    if sync.returncode != 0:
        errors.append(sync.stdout.strip())
    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s)")
        sys.exit(1)
    note = "" if banned else " (no banned-terms list loaded)"
    print(f"ok: {len(names)} skills, {0 if tools is None else len(tools)} known tools{note}")


if __name__ == "__main__":
    main()
