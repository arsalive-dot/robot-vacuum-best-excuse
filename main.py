#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes the one-line excuse a robot vacuum gives for missing a spot,
in the voice of a small machine keeping a straight face.

The excuse is rooted in the vacuum's own world — a cliff sensor that
read rug fringe as a staircase — and the joke lands in the last clause:
six months of respectful avoidance, delivered deadpan, as if it were
entirely reasonable.
"""

import os

ENTRY = (
    "My cliff sensor mistook the rug fringe for a staircase, so I have "
    "been respectfully avoiding that spot for six months."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
