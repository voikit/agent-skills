#!/usr/bin/env python3
"""Pre-check a text that customers will hear or read (a greeting, a rule, an SMS,
a direct message, a public reply) before proposing it to the owner.

    python3 text_check.py --kind greeting "Thanks for calling Aria Dental ..."
    python3 text_check.py --kind public-reply --file reply.txt
    python3 text_check.py --kind dm --never never.txt "..."

It reports, it does not decide: the Voikit server applies its own rules. The
point is to tell the owner in advance what will wait for their approval and to
catch slips (a link in a public reply, a greeting that takes 25 seconds to say).

--never FILE   one phrase per line that must not appear (the owner's red lines)
Standard library only. Works on any language; counts characters and UTF-8 bytes.
"""
import argparse
import re
import sys

LIMITS = {
    # kind: (min chars, max chars, max UTF-8 bytes, spoken)
    "greeting": (3, 400, None, True),
    "rule": (3, 400, None, False),
    "sms": (1, 600, None, False),
    "dm": (1, None, 850, False),
    "public-reply": (1, None, 850, False),
    "text": (1, None, None, False),
}
LINK = re.compile(r"(https?://|www\.)\S+|\b[a-z0-9][a-z0-9-]{0,62}\.[a-z]{2,24}\b(/\S*)?", re.I)
PHONE = re.compile(r"(\+|00)?\d[\d\s\-().]{6,}\d")
VARS = re.compile(r"\{\{[^}]*\}\}")
DIGIT = re.compile(r"\d")


def to_ascii_digits(s):
    out = []
    for ch in s:
        o = ord(ch)
        if 0x06F0 <= o <= 0x06F9:
            out.append(chr(o - 0x06F0 + 48))
        elif 0x0660 <= o <= 0x0669:
            out.append(chr(o - 0x0660 + 48))
        else:
            out.append(ch)
    return "".join(out)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("text", nargs="?")
    p.add_argument("--file")
    p.add_argument("--kind", choices=sorted(LIMITS), default="text")
    p.add_argument("--never")
    a = p.parse_args()
    text = open(a.file, encoding="utf-8").read() if a.file else (a.text or sys.stdin.read())
    text = text.strip()
    lo, hi, max_bytes, spoken = LIMITS[a.kind]
    plain = VARS.sub(" ", to_ascii_digits(text))
    problems, notes = [], []

    chars, size = len(text), len(text.encode("utf-8"))
    if chars < lo:
        problems.append(f"too short: {chars} characters (minimum {lo})")
    if hi and chars > hi:
        problems.append(f"too long: {chars} characters (maximum {hi})")
    if max_bytes and size > max_bytes:
        problems.append(f"too long: {size} bytes (maximum {max_bytes} per message)")

    has_link, has_phone = bool(LINK.search(plain)), bool(PHONE.search(plain))
    if a.kind == "public-reply" and (has_link or has_phone):
        problems.append("a public reply must not contain a link or a number")
    elif has_link or has_phone:
        what = " and ".join(w for w, on in (("a link", has_link), ("a phone or card-like number", has_phone)) if on)
        notes.append(f"contains {what}: this change always waits for the owner's approval, in every approval mode")

    if spoken:
        seconds = round(len(text.split()) / 2.5)
        notes.append(f"about {seconds} seconds when spoken")
        if seconds > 12:
            problems.append("a greeting longer than about 12 seconds loses callers; shorten it")
        if DIGIT.search(plain):
            notes.append("has digits: for speech, write numbers the way they should be said")
    if a.never:
        low = text.lower()
        for phrase in open(a.never, encoding="utf-8").read().splitlines():
            phrase = phrase.strip()
            if phrase and phrase.lower() in low:
                problems.append(f"contains a phrase the owner ruled out: {phrase!r}")

    print(f"kind: {a.kind} | {chars} characters, {size} bytes")
    for n in notes:
        print("note:", n)
    for pr in problems:
        print("PROBLEM:", pr)
    print("result:", "fix before proposing" if problems else "ok to show the owner")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
