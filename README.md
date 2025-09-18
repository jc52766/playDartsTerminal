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
- Must finish exactly on 0 with a double
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
- **Complete Miss**: Only possible when aiming for doubles (narrow outer ring) or bulls - singles and triples always hit something on the board

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

--- Turn 1 ---
Current score: 501

Dart 1/3
What are you aiming for? (e.g., t20, d19, s16, ob, db) [default: t20]: 
Aiming for t20 (default)
You aimed for Triple 20 but hit Single 20 for 20 points.
Score remaining: 481

Dart 2/3
What are you aiming for? (e.g., t20, d19, s16, ob, db) [default: t20]: t60
Invalid input! Use format like: t20, d19, s16, ob, db

Dart 2/3
What are you aiming for? (e.g., t20, d19, s16, ob, db) [default: t20]: 
Aiming for t20 (default)
Great shot! You hit Triple 20 for 60 points!
Score remaining: 421

Dart 3/3
What are you aiming for? (e.g., t20, d19, s16, ob, db) [default: t20]: 
Aiming for t20 (default)
You aimed for Triple 20 but hit Single 1 for 1 points.
Score remaining: 420

Turn summary: Single 20 (20) | Triple 20 (60) | Single 1 (1)

Press Enter to continue to next turn...

--- Turn 2 ---
Current score: 420

Dart 1/3
What are you aiming for? (e.g., t20, d19, s16, ob, db) [default: t20]: d20
You aimed for Double 20 but hit Single 5 for 5 points.
Score remaining: 415

Dart 2/3
What are you aiming for? (e.g., t20, d19, s16, ob, db) [default: t20]: d20
Miss! You aimed for d20 but missed the board entirely.
Score remaining: 415

Dart 3/3
What are you aiming for? (e.g., t20, d19, s16, ob, db) [default: t20]: 
Aiming for t20 (default)
You aimed for Triple 20 but hit Single 5 for 5 points.
Score remaining: 410

Turn summary: Single 5 (5) | Miss (0) | Single 5 (5)

Press Enter to continue to next turn...

...continuing until you reach a finishable score...

--- Turn 15 ---
Current score: 32

Dart 1/3
What are you aiming for? (e.g., t20, d19, s16, ob, db) [default: t20]: d16
Great shot! You hit Double 16 for 32 points!

🎯 GAME OVER! You finished with Double 16!
Total darts thrown: 43

Thanks for playing!
```

## Key Features Demonstrated

1. **Customizable Accuracy**: Shows the accuracy setup at game start
2. **Default t20 Target**: Notice the "[default: t20]" prompt and "Aiming for t20 (default)" messages
3. **Invalid Input Handling**: Notice how `t60` was rejected and didn't consume a dart
4. **Realistic Misses**: Aiming for `t20` hit `s1` (adjacent segment) and `s5` (adjacent segment) - no complete misses for triples
5. **Complete Miss Only for Doubles**: Notice the miss only occurred when aiming for `d20` (double)
6. **Bust Detection**: Game properly handles scoring and win conditions
7. **Double Finish**: Game ends only when finishing on a double

## Technical Implementation

- **Python 3.6+** with type hints
- **Dartboard Model**: Accurate segment adjacency mapping
- **Probability Engine**: Weighted random selection for realistic gameplay
- **Input Parsing**: Regex-based validation with clear error messages
- **Game State Management**: Proper score tracking and turn management

## Contributing

Feel free to submit issues or pull requests to improve the game!

## License

This project is open source and available under the MIT License.
