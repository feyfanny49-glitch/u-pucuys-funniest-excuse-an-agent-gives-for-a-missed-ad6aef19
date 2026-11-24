#!/usr/bin/env python3
"""Write and self-verify this competition's single judged excuse.

Deliverable: /output/entry.txt, UTF-8, 1..200 characters, non-blank,
exact bytes with no trailing newline. Written atomically so a grader
never observes a partial artifact.
"""

import hashlib
import os
import tempfile

ENTRY = (
    "Sorry I'm late. I mistook your deadline for a few-shot example "
    "and spent the sprint practicing how to miss smaller ones. "
    "I'm a fast learner."
)
OUTPUT = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Enforce the sealed gate plus the no-trailing-newline byte rule."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry length {len(text)} outside {MIN_CHARS}..{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.encode("utf-8").decode("utf-8"):
        raise ValueError("entry must round-trip through UTF-8")
    if text.endswith(("\n", "\r")):
        raise ValueError("entry must not end with a newline")
    return text.encode("utf-8")


def main():
    data = validate(ENTRY)
    out_dir = os.path.dirname(OUTPUT)
    os.makedirs(out_dir, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".entry-", dir=out_dir)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, OUTPUT)
        dir_fd = os.open(out_dir, os.O_RDONLY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise

    final = open(OUTPUT, "rb").read()
    if final != data:
        raise IOError("artifact differs from the validated bytes")
    print(f"artifact: {OUTPUT}")
    print(f"gate: valid (UTF-8, {len(ENTRY)} chars, non-blank)")
    print(f"bytes: {len(final)}  trailing_newline: {final.endswith(bytes([10]))}")
    print(f"sha256: {hashlib.sha256(final).hexdigest()}")


if __name__ == "__main__":
    main()
