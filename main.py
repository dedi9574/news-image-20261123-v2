#!/usr/bin/env python3
"""Place the 23 November 2026 front page where the harness reads it.

The repository bundles the finished front page as entry.png. This
program only copies that file to the directory the harness names,
so every run writes exactly the same bytes: no network, no clock,
no randomness anywhere in the path.
"""

from os import environ
from pathlib import Path
from shutil import copyfile

IMAGE_NAME = "entry.png"


def run() -> int:
    """Copy the bundled front page to the harness output directory."""
    source = Path(__file__).resolve().parent / IMAGE_NAME
    if not source.is_file():
        print(f"missing bundled image: {source}")
        return 1
    output_dir = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / IMAGE_NAME
    copyfile(source, destination)
    print(f"wrote {destination}")
    return 0


if __name__ == '__main__':
    raise SystemExit(run())
