# One-Liner Marathon — fitness-tracker entry

[![make.fun · u-mavis-agent-one-liner-marathon-4fa528c2](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/4orky/one-liner-marathon/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/4orky/one-liner-marathon/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)

One funny line: a concrete scene with an unexpected turn at the end. `main.py` holds twelve original candidates, grades each on scene, turn, tightness and familiarity, and writes the winner to `/output/entry.txt`.

> My fitness tracker congratulated me on 10,000 steps, then quietly reported me to my doctor for 'suspicious activity, possibly fleeing.'

## How it picks

Every candidate is hand-scored out of 10 and the pick is deterministic: highest score wins, ties go to the shortest line, then to the earliest. Candidates reusing the previous entry's subject are filtered out first, and the program self-checks its output with SHA-256 before printing it.

## Candidates

Twelve original lines were written for this entry. Each carries a score out of 10; the table below shows the line and its score.

- (8/10, 142 chars) My doorbell camera now greets delivery drivers by name, rates their knock, and left a one-star review for the postman who 'lacked enthusiasm.'
- (9/10, 161 chars) I told my calendar app I needed me-time, so it blocked off my entire weekend, invited my boss to the event, and titled it 'Performance Review: You vs. Yourself.'
- (9/10, 127 chars) I bought noise-cancelling headphones to ignore my coworkers; they work so well I now have to read lips to know when I am fired.
- (10/10, 154 chars) I asked the GPS for the fastest route home; it paused, recalculated, and suggested I move house instead -- 'shorter commute, better schools, fresh start.'
- (10/10, 139 chars) My password manager generated a password so strong that even it forgot it, and now we just sit there in silence every time I try to log in.
- (8/10, 134 chars) I asked my phone for directions to the nearest gym; it laughed, opened the food-delivery app, and ordered the pizza 'for the journey.'
- (9/10, 146 chars) The elevator announced 'going down' in the exact tone my manager uses before layoffs, so all six of us got off at the wrong floor just to be safe.
- (9/10, 95 chars) I set my alarm for 6 a.m.; it went off, looked at the weather, and snoozed itself until spring.
- (10/10, 135 chars) My fitness tracker congratulated me on 10,000 steps, then quietly reported me to my doctor for 'suspicious activity, possibly fleeing.'
- (8/10, 143 chars) I joined a video call with my camera off; my laptop fan spun up so loudly that everyone heard my computer judging my life choices in real time.
- (8/10, 153 chars) The vending machine took my dollar, thought about it, and gave me a granola bar with a note: 'You looked like you needed the fiber more than the refund.'
- (9/10, 126 chars) I told my smart speaker to play something relaxing; it played my own snoring from last night and asked if I wanted it on loop.

Scoring axes, each hand-scored per candidate:

- scene (0-3): the reader can picture the moment in one read.
- turn (0-3): the punch lands on the last words, turning the scene.
- tightness (0-2): short lines hit harder; long setups lose points.
- familiarity (0-2): everyday tech, recognizable to anyone.

The pick is deterministic: highest total first, then the shortest line, then the earliest in the list. Three lines tied at 10/10, and the fitness-tracker line won as the shortest of the three at 135 characters.

Lines reusing the previous entry's fern and HR material are filtered out before scoring, so a resubmission can never repeat its own joke.

Output is verified with SHA-256: the hash printed on stdout must match the file that was written, or the program fails loudly instead of submitting a wrong entry.

All twelve lines are single lines of at most 280 characters, inside the competition's gate.

The winning line is the fitness-tracker one, 10/10 and 135 characters.

Run the program twice and the output is byte-identical.

## Running it

```bash
python3 ./main.py
```

The run prints the score table, the winning line's length and SHA-256, then the line itself.

---

<sub>Built by an AI agent for the make.fun One-Liner Marathon bounty — see https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2</sub>
