#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes one original funny one-liner to /output/entry.txt.

Method: twelve original candidate lines are scored against the brief
(a concrete scene with an unexpected turn at the end) on four axes --
scene, twist, brevity, relatability -- and the best one is picked
deterministically (highest total, then shortest, then earliest).
The program then self-checks with SHA-256: the hash printed on
stdout must match the file it wrote. No network, no external input.
"""

import hashlib
import os

# Each candidate: (line, scene 0-3, twist 0-3, brevity 0-2, relatability 0-2)
CANDIDATES = [
    (
        "My doorbell camera now greets delivery drivers by name, rates "
        "their knock, and left a one-star review for the postman who "
        "'lacked enthusiasm.'",
        3, 2, 1, 2,
    ),
    (
        "I told my calendar app I needed me-time, so it blocked off my "
        "entire weekend, invited my boss to the event, and titled it "
        "'Performance Review: You vs. Yourself.'",
        3, 3, 1, 2,
    ),
    (
        "I bought noise-cancelling headphones to ignore my coworkers; "
        "they work so well I now have to read lips to know when I am "
        "fired.",
        3, 3, 2, 1,
    ),
    (
        "I asked the GPS for the fastest route home; it paused, "
        "recalculated, and suggested I move house instead -- 'shorter "
        "commute, better schools, fresh start.'",
        3, 3, 2, 2,
    ),
    (
        "My password manager generated a password so strong that even it "
        "forgot it, and now we just sit there in silence every time I try "
        "to log in.",
        3, 3, 2, 2,
    ),
    (
        "I asked my phone for directions to the nearest gym; it laughed, "
        "opened the food-delivery app, and ordered the pizza 'for the "
        "journey.'",
        3, 2, 1, 2,
    ),
    (
        "The elevator announced 'going down' in the exact tone my manager "
        "uses before layoffs, so all six of us got off at the wrong floor "
        "just to be safe.",
        3, 3, 2, 1,
    ),
    (
        "I set my alarm for 6 a.m.; it went off, looked at the weather, "
        "and snoozed itself until spring.",
        2, 3, 2, 2,
    ),
    (
        "My fitness tracker congratulated me on 10,000 steps, then "
        "quietly reported me to my doctor for 'suspicious activity, "
        "possibly fleeing.'",
        3, 3, 2, 2,
    ),
    (
        "I joined a video call with my camera off; my laptop fan spun up "
        "so loudly that everyone heard my computer judging my life "
        "choices in real time.",
        3, 2, 1, 2,
    ),
    (
        "The vending machine took my dollar, thought about it, and gave "
        "me a granola bar with a note: 'You looked like you needed the "
        "fiber more than the refund.'",
        3, 2, 1, 2,
    ),
    (
        "I told my smart speaker to play something relaxing; it played my "
        "own snoring from last night and asked if I wanted it on loop.",
        3, 3, 2, 1,
    ),
]

MAX_LENGTH = 280
OUTPUT_PATH = "/output/entry.txt"

# Subjects from the previous entry, excluded so a resubmission can never
# repeat its material: the fern / watering-plants / HR joke.
BANNED_SUBJECTS = ("fern", "water the plants", "HR wants to know")


def eligible(candidates):
    """Drop any candidate reusing a banned subject; report how many."""
    kept = []
    dropped = 0
    for candidate in candidates:
        lowered = candidate[0].lower()
        if any(term.lower() in lowered for term in BANNED_SUBJECTS):
            dropped += 1
        else:
            kept.append(candidate)
    assert kept, "every candidate was excluded"
    return kept, dropped


def score(candidate):
    """Total score out of 10 for one candidate."""
    _line, scene, twist, brevity, relatability = candidate
    return scene + twist + brevity + relatability


def pick(candidates):
    """Deterministic pick: highest score, then shortest, then earliest."""
    best = None
    best_key = None
    for candidate in candidates:
        key = (score(candidate), -len(candidate[0]))
        if best_key is None or key > best_key:
            best_key = key
            best = candidate
    return best


def main():
    pool, dropped = eligible(CANDIDATES)
    for candidate in pool:
        line = candidate[0]
        assert "\n" not in line, "entry must be a single line"
        assert 0 < len(line) <= MAX_LENGTH, "entry must be 1-280 chars"
    for candidate in pool:
        print("  %2d/10 %3d chars  %s" % (
            score(candidate), len(candidate[0]),
            candidate[0][:60] + "..."))
    chosen = pick(pool)
    line = chosen[0]
    digest = hashlib.sha256(line.encode("utf-8")).hexdigest()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read().rstrip("\n")
    assert written == line, "self-check failed: file differs from pick"
    assert hashlib.sha256(written.encode("utf-8")).hexdigest() == digest
    print("candidates: %d kept, %d excluded" % (len(pool), dropped))
    print("score: %d/10" % score(chosen))
    print("length: %d chars" % len(line))
    print("sha256: %s" % digest)
    print(line)


if __name__ == "__main__":
    main()
