"""The World in One Day — Sunday 22 November 2026 (v4).

Writes the newspaper image to the output directory. The image is a
single 1024x1024 PNG held in this repository as entry.png; this program
copies it unchanged, so every run produces byte-identical output.

Usage:
    python3 main.py

The output directory comes from MAKEFUN_OUTPUT_DIR. When that variable
is unset the program uses /output if it exists (the competition's
output path), otherwise a local "out" directory. No network access,
no third-party packages — Python 3.13 standard library only.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

ENTRY = Path(__file__).with_name("entry.png")


def _output_dir() -> Path:
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return Path(env)
    if Path("/output").is_dir():
        return Path("/output")
    return Path("out")


def main() -> int:
    if not ENTRY.is_file():
        print(f"error: bundled image missing: {ENTRY}", file=sys.stderr)
        return 1
    source = ENTRY.read_bytes()
    source_digest = hashlib.sha256(source).hexdigest()

    out_dir = _output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(ENTRY, dest)

    written = dest.read_bytes()
    written_digest = hashlib.sha256(written).hexdigest()
    if written_digest != source_digest:
        print("error: output differs from bundled image", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(written)} bytes, sha256 {written_digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
