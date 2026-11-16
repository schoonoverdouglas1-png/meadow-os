#!/usr/bin/env python3
"""Meadow OS kernel — MEADOW-0.1 'First Field'. Sibling to Rad OS.
Boot reads system/MEADOW-CORE.md FIRST, always."""
import sys, os
ROOT = os.path.dirname(os.path.abspath(__file__))

def boot():
    core = open(os.path.join(ROOT, "system", "MEADOW-CORE.md")).read()
    print("MEADOW-CORE read first:", len(core), "bytes")
    print("Meadow OS MEADOW-0.1 'First Field' — the field is open.")

def acquired():
    print("Acquired code growing in the meadow (provenance on each):")
    for line in open(os.path.join(ROOT, "acquired", "INDEX.md")):
        if line.startswith("- "):
            print(" ", line.rstrip())

def test():
    ok = 0
    core = os.path.join(ROOT, "system", "MEADOW-CORE.md")
    if os.path.exists(core) and "M-E-A-D-O-W" in open(core).read(): ok += 1
    if os.path.exists(os.path.join(ROOT, "acquired", "INDEX.md")): ok += 1
    if os.path.exists(os.path.join(ROOT, "programs", "first_growth.md")): ok += 1
    print(f"MEADOW test: {ok}/3 PASS")
    return ok == 3

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "boot"
    if cmd == "boot": boot()
    elif cmd == "acquired": acquired()
    elif cmd == "test": sys.exit(0 if test() else 1)
    else: print("commands: boot | acquired | test")
