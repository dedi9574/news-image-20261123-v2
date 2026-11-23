#!/usr/bin/env python3
"""News Front Page — 23 November 2026.

Reproduces the front-page image for Monday 23 November 2026 by copying
the bundled entry.png (1024x1024 PNG) to the output directory.

The program performs no network access, reads no clock and uses no
randomness, so repeated runs always write identical bytes.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    print("wrote", target)


if __name__ == "__main__":
    sys.exit(main())
