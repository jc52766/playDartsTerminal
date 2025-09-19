# 🎯 Terminal Darts Game - 501

A realistic terminal-based darts simulation game that follows proper 501 darts rules with accuracy-based gameplay.

## Features

- **Authentic 501 Darts Rules**: Start with 501 points, must finish on a double
- **Customizable Accuracy**: Set your own accuracy percentages for singles, doubles, and triples
- **Smart Miss Patterns**: When you miss, you hit nearby segments on the dartboard (not random areas)
- **Realistic Miss Logic**: Singles and triples never miss the board entirely (only doubles can)
- **Proper Turn Management**: 3 darts per turn with bust detection
- **Input Validation**: Invalid inputs don't consume darts - you can re-enter your aim
- **Complete Game Flow**: Score tracking, turn summaries, and win conditions
- **Streamlined Output**: Clean, concise display that's easy to follow

## Demo

[![asciicast](https://asciinema.org/a/dgUz4EPjfRp7zdTGJ76Qzk7Y1.svg)](https://asciinema.org/a/dgUz4EPjfRp7zdTGJ76Qzk7Y1)


## Installation & Running

1. Ensure you have Python 3.6+ installed
2. Download `darts_game.py`
3. Run the game:

```bash
python3 darts_game.py
```

## How to Play

### Input Format
- **Singles**: `s20` (single 20 = 20 points)
- **Doubles**: `d19` (double 19 = 38 points)  
- **Triples**: `t20` (triple 20 = 60 points)
- **Outer Bull**: `ob` (25 points)
- **Double Bull**: `db` (50 points)
- **Default**: Just press Enter to aim for `t20` (most common target)

### Game Rules
- Start with 501 points
- Each turn consists of up to 3 darts
- Subtract your score from 501
- Must finish exactly on 0 with a double (regular doubles d1-d20 or Double Bull db)
- **Bust conditions**: Score goes below 0 or lands on exactly 1
- When you bust, your score resets to what it was at the start of the turn

## Game Mechanics

### Customizable Accuracy Settings
At game start, you can set your own accuracy percentages (1-100%) for each target type:
- **Singles accuracy**: How often you hit singles when aiming for them [default: 80%]
- **Doubles accuracy**: How often you hit doubles when aiming for them [default: 15%]
- **Triples accuracy**: How often you hit triples when aiming for them [default: 10%]

Simply press Enter to use the defaults, or enter your own percentages to customize the difficulty.

### Realistic Miss Patterns
When you miss your target, the game simulates realistic dart throws:
- **Adjacent Segments**: Most likely to hit segments next to your target (e.g., aiming for 20 might hit 1 or 5)
- **Same Segment Different Multiplier**: Might hit single 20 when aiming for triple 20
- **Bulls Miss Logic**: When missing bulls, you either hit the other bull (close miss) or any random single 1-20 (complete miss of bull region)
- **Complete Miss**: Only possible when aiming for regular doubles (narrow outer ring)

### Dartboard Layout
The dartboard segments in clockwise order: 20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5

## Example Gameplay

```
🎯 Accuracy Settings
Enter your accuracy percentages (1-100) or press Enter for defaults:
Singles accuracy % [default: 80]: 
Doubles accuracy % [default: 15]: 
Triples accuracy % [default: 10]: 

Accuracy settings confirmed:
Singles: 80% | Doubles: 15% | Triples: 10%
==================================================
🎯 Welcome to Terminal Darts - 501!
Rules: Start with 501 points, finish on a double, 3 darts per turn
Input format: t20 (triple 20), d19 (double 19), s16 (single 16)
Special: ob (outer bull = 25), db (double bull = 50)
==================================================

Turn 1 | Score: 501
Dart 1: t20 → S20 (20) | 481
Dart 2: t60
Invalid! Use: t20, d19, s16, ob, db
Dart 2: t20 → T20 (60) | 421
Dart 3: t20 → S1 (1) | 420
Turn: S20 (20) | T20 (60) | S1 (1)

Turn 2 | Score: 420
Dart 1: d20 → S5 (5) | 415
Dart 2: d20 → MISS (0) | 415
Dart 3: t20 → S5 (5) | 410
Turn: S5 (5) | MISS (0) | S5 (5)

Turn 3 | Score: 410
Dart 1: db → S14 (14) | 396
Dart 2: db → OB (25) | 371
Dart 3: ob → DB (50) | 321
Turn: S14 (14) | OB (25) | DB (50)

...continuing until you reach a finishable score...

Turn 12 | Score: 50
Dart 1: db → DB (50) | 0

🎯 GAME OVER! Finished with DB! (36 darts)

Thanks for playing!
```

## Output Format Guide

The game uses a clean, streamlined output format:

### Hit Display Format
- `t20 → S20 (20) | 481` = Aimed for triple 20, hit single 20 for 20 points, score now 481
- `d20 → MISS (0) | 415` = Aimed for double 20, missed entirely, score remains 415
- `db → S14 (14) | 396` = Aimed for double bull, hit single 14, score now 396

### Short Codes
- **S** = Single (S20 = Single 20)
- **D** = Double (D16 = Double 16)  
- **T** = Triple (T20 = Triple 20)
- **OB** = Outer Bull (25 points)
- **DB** = Double Bull (50 points)
- **MISS** = Complete miss (0 points)

## License

This project is open source and available under the MIT License.
