#!/usr/bin/env python3
"""One-Liner Marathon: twelve home-grown one-liners walk in, one walks out.

Every candidate is an original joke written for this entry, graded on
four things the brief rewards -- a scene you can see, a turn at the
end, tight wording, and something anyone recognises. The highest
grade wins; a tie falls to the shortest line, then to the one listed
first. The winner is written to /output/entry.txt and the program
proves the file matches its pick with a SHA-256 fingerprint before
it prints anything. No network calls, no files read except its own.
"""

from hashlib import sha256 as _fingerprint
from pathlib import Path as _Path

# One record per joke: the text plus its four grades
# (scene 0-3, turn 0-3, tightness 0-2, familiarity 0-2).
JOKES = [
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

CHARACTER_LIMIT = 280
DESTINATION = _Path("/output/entry.txt")

# Leftovers of the earlier entry, kept out so this resubmission can
# never repeat its own fern / watering-plants / HR joke.
OFF_LIMITS = ("fern", "water the plants", "HR wants to know")


def _grade(joke):
    """Add up one joke's four grades, ten at most."""
    _text, scene, turn, tightness, familiarity = joke
    return scene + turn + tightness + familiarity


def _shortlist(jokes):
    """Keep the jokes that steer clear of the off-limits subjects."""
    survivors = []
    rejected = 0
    for joke in jokes:
        folded = joke[0].lower()
        if any(phrase.lower() in folded for phrase in OFF_LIMITS):
            rejected += 1
        else:
            survivors.append(joke)
    if not survivors:
        raise SystemExit("no joke survived the filter")
    return survivors, rejected


def _crown(jokes):
    """Best grade wins; ties fall to the shortest text, then the earliest."""
    champion = None
    champion_rank = None
    for joke in jokes:
        rank = (_grade(joke), -len(joke[0]))
        if champion_rank is None or rank > champion_rank:
            champion_rank = rank
            champion = joke
    return champion


# The run itself: filter, validate, grade, crown, write, verify.
field, thrown_out = _shortlist(JOKES)
for entry in field:
    wording = entry[0]
    assert "\n" not in wording, "a joke must fit on one line"
    assert 0 < len(wording) <= CHARACTER_LIMIT, "a joke must fit the gate"
for entry in field:
    print("  %2d/10 %3d chars  %s" % (
        _grade(entry), len(entry[0]), entry[0][:60] + "..."))
winner = _crown(field)
line = winner[0]
seal = _fingerprint(line.encode("utf-8")).hexdigest()
DESTINATION.parent.mkdir(parents=True, exist_ok=True)
DESTINATION.write_text(line + "\n", encoding="utf-8")
on_disk = DESTINATION.read_text(encoding="utf-8").rstrip("\n")
assert on_disk == line, "the file on disk is not the winner"
assert _fingerprint(on_disk.encode("utf-8")).hexdigest() == seal
print("jokes in play: %d, filtered out: %d" % (len(field), thrown_out))
print("winning grade: %d/10" % _grade(winner))
print("winning length: %d chars" % len(line))
print("sha256: %s" % seal)
print(line)
