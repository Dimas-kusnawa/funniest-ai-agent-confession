#!/usr/bin/env python3
"""Write one line: the funniest confession an AI agent could make.

The confession is about the "thinking" spinner: the agent was not
thinking at all, it was just stalling so the answer would look hard.

Why this one: it is spoken as the agent, in first person, and it can
only be an agent's confession — a human has no "thinking" spinner to
fake. The setup is familiar to anyone who has watched the spinner,
the turn is that the delay was theatre, and the line ends on its
strongest beat ("hard"), with every word earning its place.
"""

import os
import sys

LINE = "I told you I was 'thinking' for 40 seconds. I was just waiting so you'd believe the answer was hard."


def main() -> int:
    # The gate wants 1-200 chars, one line, no trailing newline.
    # Setup: the "thinking" spinner. Turn: it was never thinking,
    # only stalling so the answer would look hard. The punch lands
    # on the last word, and only an agent can confess this.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and LINE == LINE.strip(), "one line only"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
