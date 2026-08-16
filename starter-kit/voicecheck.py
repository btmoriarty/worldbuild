#!/usr/bin/env python3
"""Minimal voice checker for a story bible. No dependencies.

Reads a ban list and reports every match with file, line and column, so a voice law
is enforceable instead of aspirational.

    python3 voicecheck.py canon/**/*.md
    python3 voicecheck.py --bans canon/voice-bans.txt canon/vignettes/a-scene.md

Ban file format, one rule per line:

    error   \\bload-bearing\\b        figurative structural metaphor; name the function
    warn    \\b(really|very|quite)\\b  filler/intensifier
    # comments and blank lines are ignored

Column 1 is the severity, column 2 a Python regex, the rest the message. Fields are
separated by whitespace runs, so the regex may not contain a literal space: use \\s.

Exit code is 1 if any error fired, else 0. Warnings never fail the run.

Suppression, because a voice law has to be able to quote what it bans:

    ... the words to avoid are X and Y.   <!-- voicecheck:allow -->

puts one line out of scope, and `voicecheck:disable-file` anywhere in a file exempts
the whole file. Use them for rules files and glossaries, not for prose you like.

This is a FLOOR, not a ceiling. It catches strings. It cannot see cadence sameness,
explained jokes, unearned lyricism or invented precision, which are the failures that
make prose read as machine-made. A clean run is not a voice review.
"""

import argparse
import pathlib
import re
import sys

DEFAULT_BANS = "canon/voice-bans.txt"

# Used only when no ban file exists yet, so a new world is not unenforced on day one.
FALLBACK = [
    ("error", r"\b(the honest (answer|truth|version|read|case|part|thing))\b",
     "announcing candour instead of exercising it; the next sentence is the honest thing"),
    ("error", r"\b(load-bearing|linchpin|cornerstone)\b",
     "dead structural metaphor; name the function instead"),
    ("error", r"\bI want to be (honest|clear|direct|upfront)\b",
     "throat-clearing; just say it"),
    ("warn", r"\b(really|very|quite|simply|just|genuinely|honestly|truly|actually)\b",
     "filler/intensifier; test whether deleting it changes anything"),
    ("warn", r"\bfelt a (profound|deep|strange|sudden) sense of\b",
     "naming the feeling; put it in the furniture"),
    ("warn", r"\bnot only\b.{0,40}\bbut also\b",
     "antithesis; fine once, fatal at density"),
]


def load_bans(path):
    if not path or not pathlib.Path(path).exists():
        return [(s, re.compile(p, re.I), m) for s, p, m in FALLBACK], False
    rules = []
    for n, raw in enumerate(pathlib.Path(path).read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 2)
        if len(parts) < 3:
            print(f"{path}:{n}: skipping malformed rule", file=sys.stderr)
            continue
        sev, pat, msg = parts
        if sev not in ("error", "warn"):
            print(f"{path}:{n}: severity must be error or warn", file=sys.stderr)
            continue
        try:
            rules.append((sev, re.compile(pat, re.I), msg))
        except re.error as e:
            print(f"{path}:{n}: bad regex ({e})", file=sys.stderr)
    return rules, True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--bans", default=DEFAULT_BANS)
    ap.add_argument("--quiet", action="store_true", help="print only violations")
    args = ap.parse_args()

    rules, real = load_bans(args.bans)
    if not real and not args.quiet:
        print(f"note: no ban file at {args.bans}; using {len(FALLBACK)} built-in defaults.\n"
              f"      write your world's own list there as the author rules on things.\n")

    errors = warnings = 0
    in_code = False
    for f in args.files:
        p = pathlib.Path(f)
        if not p.is_file():
            continue
        text = p.read_text(encoding="utf-8")
        # A rules file has to be able to name what it forbids.
        if "voicecheck:disable-file" in text:
            continue
        for n, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_code = not in_code
                continue
            if in_code or "voicecheck:allow" in line:
                continue
            for sev, rx, msg in rules:
                for m in rx.finditer(line):
                    print(f"{f}:{n}:{m.start() + 1} [{sev}] {msg}  ->  '{m.group(0)}'")
                    if sev == "error":
                        errors += 1
                    else:
                        warnings += 1
        in_code = False

    print(f"\nvoicecheck: {errors} error(s), {warnings} warning(s) across {len(args.files)} file(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
