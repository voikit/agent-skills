#!/usr/bin/env python3
"""Build the upload packages.

    python3 scripts/build_release.py

Writes
  dist/voikit.zip                THE ONE FILE most people need: a single skill
                                 named "voikit" that holds every guide
  dist/<skill>.zip               one zip per skill, for people who want only some
  dist/voikit-agent-skills.zip   the skills/ and templates/ folders as they are

Upload voikit.zip in Claude (skills settings) or in ChatGPT
(Skills > Create > Upload from your computer).
"""
import os
import subprocess
import sys
import zipfile

from common import ROOT, SKILLS_DIR, parse_frontmatter, read, skill_names

DIST = os.path.join(ROOT, "dist")
FIXED_TIME = (2026, 1, 1, 0, 0, 0)  # stable archives: same input, same bytes


def add_tree(zf, folder, arc_root):
    for base, dirs, files in os.walk(folder):
        dirs[:] = sorted(d for d in dirs if d != "__pycache__")
        for f in sorted(files):
            full = os.path.join(base, f)
            arc = os.path.join(arc_root, os.path.relpath(full, folder)).replace(os.sep, "/")
            info = zipfile.ZipInfo(arc, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o755 if f.endswith(".py") else 0o644) << 16
            with open(full, "rb") as fh:
                zf.writestr(info, fh.read())


def add_text(zf, arc, text, mode=0o644):
    info = zipfile.ZipInfo(arc, FIXED_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = mode << 16
    zf.writestr(info, text)


def build_bundle(names):
    """One skill, "voikit": bundle/voikit.md routes to guides/<skill>.md."""
    seen = {}
    with zipfile.ZipFile(os.path.join(DIST, "voikit.zip"), "w") as zf:
        add_text(zf, "voikit/SKILL.md", read(os.path.join(ROOT, "bundle", "voikit.md")))
        for name in names:
            folder = os.path.join(SKILLS_DIR, name)
            _, body = parse_frontmatter(read(os.path.join(folder, "SKILL.md")))
            add_text(zf, f"voikit/guides/{name}.md", body.lstrip("\n"))
            for sub in ("references", "assets", "scripts"):
                subdir = os.path.join(folder, sub)
                if not os.path.isdir(subdir):
                    continue
                for f in sorted(os.listdir(subdir)):
                    full = os.path.join(subdir, f)
                    if not os.path.isfile(full):
                        continue
                    text = read(full)
                    key = f"{sub}/{f}"
                    if key in seen:
                        if seen[key] != text:
                            sys.exit(f"bundle: two skills carry a different {key}")
                        continue
                    seen[key] = text
                    add_text(zf, "voikit/" + key, text, 0o755 if f.endswith(".py") else 0o644)
    return len(seen)


def main():
    lint = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "lint_skills.py")])
    if lint.returncode != 0:
        sys.exit("lint failed; nothing was built")
    os.makedirs(DIST, exist_ok=True)
    names = skill_names()
    for name in names:
        with zipfile.ZipFile(os.path.join(DIST, name + ".zip"), "w") as zf:
            add_tree(zf, os.path.join(SKILLS_DIR, name), name)
    with zipfile.ZipFile(os.path.join(DIST, "voikit-agent-skills.zip"), "w") as zf:
        for name in names:
            add_tree(zf, os.path.join(SKILLS_DIR, name), "skills/" + name)
        add_tree(zf, os.path.join(ROOT, "templates"), "templates")
    extra = build_bundle(names)
    print(f"built voikit.zip ({len(names)} guides, {extra} shared files), {len(names)} skill zips and voikit-agent-skills.zip in dist/")


if __name__ == "__main__":
    main()
