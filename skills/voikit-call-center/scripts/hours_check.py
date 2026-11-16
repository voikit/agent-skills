#!/usr/bin/env python3
"""Check a weekly business-hours table before proposing it, and answer
"is the business open at this moment?".

    python3 hours_check.py hours.json
    python3 hours_check.py hours.json --at "thu 22:15"

hours.json: days sat..fri, each a list of ["HH:MM","HH:MM"] ranges.
    {"sat": [["09:00","13:00"],["16:00","20:00"]], "thu": [["09:00","14:00"]]}
A day that is missing or empty is closed. ["22:00","02:00"] runs past midnight.
["00:00","24:00"] is all day. Standard library only.
"""
import json
import re
import sys

DAYS = ["sat", "sun", "mon", "tue", "wed", "thu", "fri"]
HHMM = re.compile(r"^(\d{2}):(\d{2})$")


def minutes(value):
    m = HHMM.match(value)
    if not m:
        raise ValueError(f"not HH:MM: {value!r}")
    h, mi = int(m.group(1)), int(m.group(2))
    if not (0 <= h <= 24 and 0 <= mi < 60 and (h < 24 or mi == 0)):
        raise ValueError(f"not a time of day: {value!r}")
    return h * 60 + mi


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    table = json.load(open(sys.argv[1], encoding="utf-8"))
    problems, spans, total = [], {}, 0
    for day in table:
        if day not in DAYS:
            problems.append(f"unknown day {day!r} (use {', '.join(DAYS)})")
    for day in DAYS:
        spans[day] = []
        for rng in table.get(day) or []:
            try:
                start, end = minutes(rng[0]), minutes(rng[1])
            except (ValueError, IndexError, TypeError) as e:
                problems.append(f"{day}: {e}")
                continue
            if start == end:
                problems.append(f"{day}: empty range {rng}")
                continue
            if end < start:
                end += 24 * 60  # past midnight
            spans[day].append((start, end, rng))
            total += end - start
        spans[day].sort()
        for a, b in zip(spans[day], spans[day][1:]):
            if b[0] < a[1]:
                problems.append(f"{day}: ranges overlap: {a[2]} and {b[2]}")
        if len(spans[day]) > 4:
            problems.append(f"{day}: more than four ranges")

    print("day  hours")
    for day in DAYS:
        text = ", ".join(f"{r[0]}-{r[1]}" for _, _, r in spans[day]) or "closed"
        print(f"{day}  {text}")
    print(f"open {total / 60:.1f} hours a week; closed days: {', '.join(d for d in DAYS if not spans[d]) or 'none'}")

    if "--at" in sys.argv:
        day, clock = sys.argv[sys.argv.index("--at") + 1].lower().split()
        now = minutes(clock)
        prev = DAYS[DAYS.index(day) - 1]
        is_open = any(s <= now < e for s, e, _ in spans[day]) or any(e > 24 * 60 and now < e - 24 * 60 for _, e, _ in spans[prev])
        print(f"at {day} {clock}: {'OPEN (in-hours destination)' if is_open else 'CLOSED (after-hours destination)'}; holidays override this")

    for p in problems:
        print("PROBLEM:", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
