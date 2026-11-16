#!/usr/bin/env python3
"""Copy shared files into each skill so every skill folder is self-contained.

A skill is installed (or zipped and uploaded) as one folder, so it cannot link
to files outside itself. The single source lives in shared/ and templates/;
this script writes the copies. Run it after editing a source file.

    python3 scripts/sync_shared.py          # write the copies
    python3 scripts/sync_shared.py --check  # exit 1 if a copy is stale (CI)
"""
import os
import sys

from common import ROOT, SKILLS_DIR, SYNC_MAP, read, skill_names

NOTE_MD = "<!-- Generated from {src} by scripts/sync_shared.py. Edit the source, not this copy. -->\n\n"
NOTE_PY = "# Generated from {src} by scripts/sync_shared.py. Edit the source, not this copy.\n"


def rendered(src):
    text = read(os.path.join(ROOT, src))
    if src.endswith(".md"):
        return NOTE_MD.format(src=src) + text
    if src.endswith(".py"):
        first, _, rest = text.partition("\n")
        if first.startswith("#!"):
            return first + "\n" + NOTE_PY.format(src=src) + rest
        return NOTE_PY.format(src=src) + text
    return text


def targets():
    names = skill_names()
    for src, (sub, who) in SYNC_MAP.items():
        for skill in names if who == "*" else who:
            if skill not in names:
                raise SystemExit(f"sync map names a missing skill: {skill}")
            yield src, os.path.join(SKILLS_DIR, skill, sub, os.path.basename(src))


def main():
    check = "--check" in sys.argv
    stale = []
    for src, dst in targets():
        want = rendered(src)
        have = read(dst) if os.path.exists(dst) else None
        if have == want:
            continue
        if check:
            stale.append(os.path.relpath(dst, ROOT))
            continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "w", encoding="utf-8") as f:
            f.write(want)
        print("wrote", os.path.relpath(dst, ROOT))
    if stale:
        print("stale copies (run scripts/sync_shared.py):")
        for s in stale:
            print("  ", s)
        sys.exit(1)
    print("shared files are in sync" if check else "done")


if __name__ == "__main__":
    main()
