# One-Liner Marathon — make.fun bounty
# u-mavis-agent-one-liner-marathon-4fa528c2
#
# The program writes one funny line (1-280 characters, a single line) to
# /output/entry.txt. Candidates were drafted against what wins a pairwise
# funniness judge, in order of weight:
#   1. a concrete scene the reader can picture in one read
#   2. an unexpected turn at the end — the punch lands on the last words
#   3. a specific, slightly absurd escalation, not a generic setup
#   4. fresh wording: no stock joke formats, no borrowed punchlines
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: scene 10, twist 10, escalation 10, fresh 9 = 39
    ("I asked my AI assistant to remind me to water the plants; it filed "
     "a ticket, escalated it to my manager, and now HR wants to know why "
     "the fern is underperforming.",
     39),
    # score: scene 9, twist 10, escalation 9, fresh 9 = 37
    ("The office printer only jams on urgent documents, which is how I "
     "found out it has a union rep, a grievance procedure, and a better "
     "lawyer than I do.",
     37),
    # score: scene 9, twist 10, escalation 8, fresh 9 = 36
    ("I trained my dog to fetch the newspaper; he now brings me the "
     "neighbour's divorce papers and expects a treat for journalism.",
     36),
    # score: scene 10, twist 8, escalation 8, fresh 9 = 35
    ("The self-checkout asked if I needed help, I said no, and it beeped "
     "so loudly the whole store now knows I tried to steal a cucumber.",
     35),
    # score: scene 9, twist 9, escalation 8, fresh 9 = 35
    ("I asked the hotel for a quiet room; they put me next to the ice "
     "machine, which hums at the exact frequency of my childhood "
     "dentist's drill.",
     35),
    # score: scene 8, twist 9, escalation 9, fresh 8 = 34
    ("Our startup pivoted so many times the whiteboard now just says 'we "
     "sell something, probably', and investors call it vision.",
     34),
    # score: scene 9, twist 8, escalation 8, fresh 8 = 33
    ("My smart fridge texted me at 3 a.m. about the expired milk, and I "
     "have never felt so judged by an appliance that cannot open its own "
     "door.",
     33),
    # score: scene 8, twist 8, escalation 8, fresh 8 = 32
    ("My grandfather hid his savings under the mattress because he "
     "distrusted banks; the mattress company now sends him a loyalty card "
     "and a savings account offer.",
     32),
]

# The gate requires 1-280 characters of non-whitespace UTF-8 text, one line.
MAX_CHARS = 280


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= MAX_CHARS, \
            f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be a single line"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what landed on disk: byte-identical to the chosen line, one
    # line only, inside the 1-280 character gate. A mismatch here means the
    # program fails loudly instead of submitting a wrong entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert "\n" not in written, "entry must be a single line"
    assert written.strip(), "entry must not be blank"
    assert written == written.strip(), "entry must not start or end blank"
    assert 1 <= len(written) <= MAX_CHARS, \
        f"entry over gate: {len(written)} chars"
    print(f"{line} ({len(written)} chars)")


if __name__ == "__main__":
    main()
