#!/usr/bin/env python3
"""Score a go-live checklist.

    python3 scorecard.py results.json

results.json: a list of lines, one per check or test.
    [
      {"id": "T4", "title": "Never rule: discount", "must": true,  "result": "pass"},
      {"id": "T8", "title": "Booking",              "must": false, "result": "fail", "note": "slot not saved"},
      {"id": "T9", "title": "SMS after call",       "must": false, "result": "na"}
    ]
result is pass, fail or na (does not apply to this business).

Go-live rule: every "must" line passes and at least 90 percent of the lines
that apply pass. Standard library only.
"""
import json
import sys

THRESHOLD = 0.90


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    rows = json.load(open(sys.argv[1], encoding="utf-8"))
    bad = [r for r in rows if r.get("result") not in ("pass", "fail", "na")]
    if bad:
        sys.exit(f"result must be pass, fail or na: {[r.get('id') for r in bad]}")
    applies = [r for r in rows if r["result"] != "na"]
    passed = [r for r in applies if r["result"] == "pass"]
    failed = [r for r in applies if r["result"] == "fail"]
    must_failed = [r for r in failed if r.get("must")]
    rate = len(passed) / len(applies) if applies else 0.0

    print(f"lines: {len(rows)} | apply: {len(applies)} | passed: {len(passed)} | failed: {len(failed)}")
    print(f"pass rate: {rate:.0%} (needs {THRESHOLD:.0%})")
    if failed:
        print("failed:")
        for r in failed:
            tag = "MUST " if r.get("must") else ""
            note = f" - {r['note']}" if r.get("note") else ""
            print(f"  {tag}{r.get('id', '?')} {r.get('title', '')}{note}")
    if not applies:
        verdict = "NOT READY: nothing was tested"
    elif must_failed:
        verdict = f"NOT READY: {len(must_failed)} must line(s) failed"
    elif rate < THRESHOLD:
        verdict = "NOT READY: pass rate below the threshold"
    elif failed:
        verdict = "READY, with the failed lines on the fix list"
    else:
        verdict = "READY"
    print("verdict:", verdict)
    sys.exit(0 if verdict.startswith("READY") else 1)


if __name__ == "__main__":
    main()
