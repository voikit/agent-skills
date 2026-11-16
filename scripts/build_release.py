#!/usr/bin/env python3
"""Build the upload packages.

    python3 scripts/build_release.py

Writes
  dist/<skill>.zip               one zip per skill (the skill folder at the top level)
  dist/voikit-agent-skills.zip   every skill plus templates/ in one archive

Upload a single-skill zip in Claude (skills settings) or in ChatGPT
(Skills > Create > Upload from your computer).
"""
import os
import subprocess
import sys
import zipfile

from common import ROOT, SKILLS_DIR, skill_names

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
    print(f"built {len(names)} skill zips and voikit-agent-skills.zip in dist/")


if __name__ == "__main__":
    main()
