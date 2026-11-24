#!/usr/bin/env python3
"""Monday, Reviewed in One Line — write one funny one-line review of my own
Monday to /output/entry.txt.

The line: I gave Monday one star, and Monday did the most Monday thing
imaginable — thanked me for the feedback and booked a 7 a.m. follow-up
with itself. A customer-service reply from the day itself.

Stdlib only. Deterministic, no network, no randomness. The program enforces
the competition gate on its own output: 1-200 characters, not only
whitespace, a single line, no leading or trailing whitespace.
"""
import hashlib
import os
import sys

ENTRY = ("I gave Monday one star; it thanked me for the feedback "
         "and booked a 7 a.m. follow-up with itself.")

LIMIT = 200

USAGE = "usage: main.py [--self-test]"


def check(text):
    """Reject anything the gate would refuse; return the text unchanged."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry is empty (gate needs 1-200 characters)")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, over the 200-character gate" % len(text)
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if text.strip() != text:
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def self_test():
    """Run the validator through its rejection cases and boundaries."""
    bad = [
        ("", "empty"),
        ("   ", "whitespace-only"),
        ("x" * 201, "201 chars"),
        ("one\ntwo", "multi-line"),
        ("one\rtwo", "carriage return"),
        (" padded", "leading whitespace"),
        ("padded ", "trailing whitespace"),
    ]
    for text, label in bad:
        try:
            check(text)
        except ValueError as exc:
            print("self-test ok: rejected %s: %s" % (label, exc))
        else:
            raise SystemExit("self-test FAIL: %s was accepted" % label)
    for n, label in ((1, "1-char"), (200, "200-char")):
        check("y" * n)
        print("self-test ok: %s boundary accepted" % label)
    check(ENTRY)
    print("self-test ok: entry itself accepted")
    print("self-test: all cases passed")
    return 0


def run():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--self-test" and len(sys.argv) == 2:
            return self_test()
        print(USAGE, file=sys.stderr)
        return 2
    text = check(ENTRY)
    blob = text.encode("utf-8")
    dest = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    folder = os.path.dirname(dest)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(dest, "wb") as handle:
        handle.write(blob)  # no trailing newline: the file is exactly the line
    with open(dest, "rb") as handle:
        if handle.read() != blob:
            raise SystemExit("round-trip mismatch: file does not match entry")
    print("wrote %s: %d chars, sha256 %s"
          % (dest, len(text), hashlib.sha256(blob).hexdigest()))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
