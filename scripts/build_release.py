#!/usr/bin/env python3
"""Build and check the files a release publishes.

    python3 scripts/build_release.py                # build and check
    python3 scripts/build_release.py --tag v0.1.1   # the same, and refuse a wrong version

A release offers people exactly ONE file to download:

  dist/voikit.zip          a single skill named "voikit" that carries every guide.
                           The same file is uploaded in Claude, in ChatGPT and in
                           any other app that takes an Agent Skills zip.

Written next to it:

  dist/SHA256SUMS.txt      checksum of voikit.zip
  dist/RELEASE_NOTES.md    install steps plus this version's changelog section
  dist/RELEASE_ASSETS.txt  the files the release workflow attaches (one per line)
  dist/single-skills/      one zip per skill, for people who want only some;
                           built and checked, not attached to the release

Upload pages accept a zip with exactly one top-level folder and exactly one
SKILL.md, a short lower-case name and a description without angle brackets.
Every zip is checked against those rules here, so a release cannot publish a
file that an upload page refuses for its shape.

The version comes from one place: "version" in .claude-plugin/plugin.json.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import zipfile

from common import ROOT, SKILLS_DIR, parse_frontmatter, read, skill_names

DIST = os.path.join(ROOT, "dist")
SINGLE = os.path.join(DIST, "single-skills")
FIXED_TIME = (2026, 1, 1, 0, 0, 0)  # stable archives: same input, same bytes
REPO = "voikit/agent-skills"
LATEST = f"https://github.com/{REPO}/releases/latest/download/voikit.zip"
ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
STANDARD_DIRS = {"references", "assets", "scripts", "agents"}
RESERVED = ("anthropic", "claude", "openai", "chatgpt")
MAX_ZIP_BYTES = 5 * 1024 * 1024


def fail(msg):
    sys.exit("release build failed: " + msg)


def plugin_version():
    return json.loads(read(os.path.join(ROOT, ".claude-plugin", "plugin.json")))["version"]


def add_text(zf, arc, text, mode=0o644):
    info = zipfile.ZipInfo(arc, FIXED_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = mode << 16
    zf.writestr(info, text)


def add_tree(zf, folder, arc_root):
    for base, dirs, files in os.walk(folder):
        dirs[:] = sorted(d for d in dirs if d != "__pycache__")
        for f in sorted(files):
            full = os.path.join(base, f)
            arc = os.path.join(arc_root, os.path.relpath(full, folder)).replace(os.sep, "/")
            add_text(zf, arc, read(full), 0o755 if f.endswith(".py") else 0o644)


def bundle_skill_md(version):
    """bundle/voikit.md with the version stamped in."""
    text = read(os.path.join(ROOT, "bundle", "voikit.md"))
    text, n = re.subn(r'(\n  version: )"[^"]*"', rf'\g<1>"{version}"', text, count=1)
    if n != 1:
        fail("bundle/voikit.md has no metadata.version line to stamp")
    return text.replace("{{VERSION}}", version).replace("{{LATEST}}", LATEST)


def build_bundle(names, version):
    """One skill, "voikit": SKILL.md routes to references/<skill>.md."""
    seen = {}
    path = os.path.join(DIST, "voikit.zip")
    with zipfile.ZipFile(path, "w") as zf:
        add_text(zf, "voikit/SKILL.md", bundle_skill_md(version))
        add_text(zf, "voikit/agents/openai.yaml", read(os.path.join(ROOT, "bundle", "openai.yaml")))
        for name in names:
            folder = os.path.join(SKILLS_DIR, name)
            _, body = parse_frontmatter(read(os.path.join(folder, "SKILL.md")))
            seen[f"references/{name}.md"] = body.lstrip("\n")
            for sub in ("references", "assets", "scripts"):
                subdir = os.path.join(folder, sub)
                if not os.path.isdir(subdir):
                    continue
                for f in sorted(os.listdir(subdir)):
                    full = os.path.join(subdir, f)
                    if not os.path.isfile(full):
                        continue
                    key, text = f"{sub}/{f}", read(full)
                    if seen.setdefault(key, text) != text:
                        fail(f"two skills carry a different {key}")
        for key in sorted(seen):
            add_text(zf, "voikit/" + key, seen[key], 0o755 if key.endswith(".py") else 0o644)
    return path


def check_zip(path, standard_dirs_only=False):
    """The shape and metadata rules of the upload pages."""
    name = os.path.basename(path)[:-4]
    rel = os.path.relpath(path, ROOT)
    if os.path.getsize(path) > MAX_ZIP_BYTES:
        fail(f"{rel} is larger than {MAX_ZIP_BYTES // (1024 * 1024)} MB")
    with zipfile.ZipFile(path) as zf:
        entries = zf.namelist()
        tops = {e.split("/")[0] for e in entries}
        skill_files = [e for e in entries if e.split("/")[-1].lower() == "skill.md"]
        if tops != {name}:
            fail(f"{rel}: needs exactly one top-level folder named {name!r}, has {sorted(tops)}")
        if skill_files != [f"{name}/SKILL.md"]:
            fail(f"{rel}: needs exactly one SKILL.md at {name}/SKILL.md, has {skill_files}")
        for e in entries:
            parts = e.split("/")
            if e.startswith("/") or ".." in parts or any(p.startswith(".") or p == "__MACOSX" for p in parts):
                fail(f"{rel}: unsafe or hidden path {e!r}")
            if standard_dirs_only and len(parts) > 2 and parts[1] not in STANDARD_DIRS:
                fail(f"{rel}: {e!r} is outside the standard folders {sorted(STANDARD_DIRS)}")
        text = zf.read(f"{name}/SKILL.md").decode("utf-8")
    meta, body = parse_frontmatter(text)
    if meta is None:
        fail(f"{rel}: SKILL.md has no frontmatter")
    if meta.get("name") != name or not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name) or len(name) > 64:
        fail(f"{rel}: frontmatter name must equal the folder name, lower case with hyphens, at most 64 characters")
    if any(word in name for word in RESERVED):
        fail(f"{rel}: the skill name contains a reserved word")
    desc = meta.get("description", "")
    if not 1 <= len(desc) <= 1024 or "<" in desc or ">" in desc:
        fail(f"{rel}: description must be 1-1024 characters without angle brackets")
    extra = set(meta) - ALLOWED_KEYS
    if extra:
        fail(f"{rel}: frontmatter keys some apps refuse: {sorted(extra)}")
    if "{{" in text:
        fail(f"{rel}: an unfilled placeholder is left in SKILL.md")
    if not body.strip():
        fail(f"{rel}: SKILL.md has no body")


def changelog_heading_and_section(version):
    text = read(os.path.join(ROOT, "CHANGELOG.md"))
    m = re.search(rf"^## {re.escape(version)}\b([^\n]*)\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return (m.group(1), m.group(2).strip()) if m else (None, None)


def release_notes(version, changes):
    return f"""# Voikit Agent Skills {version}

## Install or update

Download **voikit.zip** from the assets of this release. It is the only file you need. ("Source code" is the repository, not an installable skill.)

- **Claude:** skills settings, upload a skill, drag `voikit.zip` in.
- **ChatGPT:** Skills, Create, Upload from your computer, pick `voikit.zip`.
- **Claude Code:** `/plugin marketplace add {REPO}` then `/plugin install voikit@voikit-agent-skills`.
- **Codex, Cursor and other coding agents:** `npx skills add {REPO}`.

Then say to your assistant: **Connect my Voikit account.** It guides you step by step.

Updating from an older version: add the new `voikit.zip` the same way. If your app keeps the old `voikit` skill beside the new one, remove the old one.

Always the newest file: {LATEST}

## What changed

{changes}
"""


def clear_stale():
    """Zips of older builds at the top of dist/ must not be published by accident."""
    for f in sorted(os.listdir(DIST)):
        full = os.path.join(DIST, f)
        if not (os.path.isfile(full) and f.endswith(".zip")):
            continue
        try:
            os.remove(full)
        except OSError:  # a folder where deleting is not allowed: move it aside
            aside = os.path.join(DIST, "_old")
            os.makedirs(aside, exist_ok=True)
            os.replace(full, os.path.join(aside, f + ".old"))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--tag", help="the release tag, e.g. v0.1.1; must match the version in plugin.json")
    args = p.parse_args()

    if subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "lint_skills.py")]).returncode != 0:
        fail("the lint did not pass")
    version = plugin_version()
    if not re.match(r"^\d+\.\d+\.\d+$", version):
        fail(f"plugin.json version {version!r} is not MAJOR.MINOR.PATCH")
    if args.tag and args.tag != "v" + version:
        fail(f"tag {args.tag} does not match plugin.json version {version}; bump the version, then tag v{version}")
    heading, changes = changelog_heading_and_section(version)
    if not changes:
        fail(f"CHANGELOG.md has no '## {version}' section")
    if args.tag and "unreleased" in heading.lower():
        fail(f"CHANGELOG.md still marks {version} as unreleased; put the date")

    os.makedirs(SINGLE, exist_ok=True)
    clear_stale()
    names = skill_names()
    for name in names:
        path = os.path.join(SINGLE, name + ".zip")
        with zipfile.ZipFile(path, "w") as zf:
            add_tree(zf, os.path.join(SKILLS_DIR, name), name)
        check_zip(path)
    bundle = build_bundle(names, version)
    check_zip(bundle, standard_dirs_only=True)

    digest = hashlib.sha256(open(bundle, "rb").read()).hexdigest()
    with open(os.path.join(DIST, "SHA256SUMS.txt"), "w", encoding="utf-8") as f:
        f.write(f"{digest}  voikit.zip\n")
    with open(os.path.join(DIST, "RELEASE_NOTES.md"), "w", encoding="utf-8") as f:
        f.write(release_notes(version, changes))
    with open(os.path.join(DIST, "RELEASE_ASSETS.txt"), "w", encoding="utf-8") as f:
        f.write("dist/voikit.zip\ndist/SHA256SUMS.txt\n")
    print(f"voikit {version}: dist/voikit.zip ({os.path.getsize(bundle) // 1024} kB, {len(names)} guides) passes the upload rules")
    print(f"also built {len(names)} single-skill zips in dist/single-skills/ (not attached to releases)")


if __name__ == "__main__":
    main()
