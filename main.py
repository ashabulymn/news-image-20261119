#!/usr/bin/env python3
"""Sum up 19 November 2026 world news in one image.

Deterministic, no network. Copies the pre-built front-page image
entry.jpg (1024x1024, <1 MiB) to /output/entry.png.
Running twice writes the same bytes.
"""
import hashlib
import pathlib
import shutil
import sys

SRC = pathlib.Path(__file__).resolve().parent / "entry.jpg"
DST = pathlib.Path("/output/entry.png")


def main() -> int:
    if not SRC.is_file():
        print(f"missing {SRC}", file=sys.stderr)
        return 1
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    digest = hashlib.sha256(DST.read_bytes()).hexdigest()
    print(f"wrote {DST} sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
