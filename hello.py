"""Module providing hello_world function."""

from __future__ import annotations

import sys


def hello_world(name: str) -> None:
    """Print greeting from Codex for the given ``name``."""

    print(f"Hello, {name} dari Codex!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hello.py <nama>")
        sys.exit(1)

    hello_world(sys.argv[1])
