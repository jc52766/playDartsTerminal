#!/usr/bin/env python3
"""
Terminal Darts Game - 501
A realistic darts simulation with accuracy-based gameplay
"""

import random
import re
from typing import Dict, List, Tuple, Optional

class DartsGame:
    def __init__(self):
        # Dartboard segments in clockwise order starting from top
        self.segments = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]
        
        # Create adjacency mapping for realistic misses
        self.adjacency = self._create_adjacency_map()
        
        # Get accuracy rates from user
        self.accuracy = self._get_accuracy_settings()
        
        # Game state
        self.score = 501
        self.darts_thrown = 0
        self.turn_darts = 0
        self.game_over = False
        
    def _create_adjacency_map(self) -> Dict[int, List[int]]:
        """Create mapping of each segment to its adjacent segments"""
        adjacency = {}
        for i, segment in enumerate(self.segments):
            left_neighbor = self.segments[(i - 1) % len(self.segments)]
            right_neighbor = self.segments[(i + 1) % len(self.segments)]
            adjacency[segment] = [left_neighbor, right_neighbor]
        return adjacency
    
    def _get_accuracy_settings(self) -> Dict[str, float]:
        """Get accuracy settings from user input"""
        print("🎯 Accuracy Settings")
        print("Enter your accuracy percentages (1-100) or press Enter for defaults:")
        
        # Get singles accuracy
        while True:
            singles_input = input("Singles accuracy % [default: 80]: ").strip()
            if not singles_input:
                singles_accuracy = 80
                break
            try:
                singles_accuracy = float(singles_input)
                if 1 <= singles_accuracy <= 100:
                    break
                else:
                    print("Please enter a value between 1 and 100")
            except ValueError:
                print("Please enter a valid number")
        
        # Get doubles accuracy
        while True:
            doubles_input = input("Doubles accuracy % [default: 15]: ").strip()
            if not doubles_input:
                doubles_accuracy = 15
                break
            try:
                doubles_accuracy = float(doubles_input)
                if 1 <= doubles_accuracy <= 100:
                    break
                else:
                    print("Please enter a value between 1 and 100")
            except ValueError:
                print("Please enter a valid number")
        
        # Get triples accuracy
        while True:
            triples_input = input("Triples accuracy % [default: 10]: ").strip()
            if not triples_input:
                triples_accuracy = 10
                break
            try:
                triples_accuracy = float(triples_input)
                if 1 <= triples_accuracy <= 100:
                    break
                else:
                    print("Please enter a value between 1 and 100")
            except ValueError:
                print("Please enter a valid number")
        
        # Convert to decimal and display confirmation
        accuracy_dict = {
            'single': singles_accuracy / 100,
            'double': doubles_accuracy / 100,
            'triple': triples_accuracy / 100
        }
        
        print(f"\nAccuracy settings confirmed:")
        print(f"Singles: {singles_accuracy}% | Doubles: {doubles_accuracy}% | Triples: {triples_accuracy}%")
        print("=" * 50)
        
        return accuracy_dict
    
    def parse_input(self, user_input: str) -> Optional[Tuple[str, int]]:
        """Parse user input like 't20', 'd19', 's16', 'ob', 'db'"""
        user_input = user_input.lower().strip()
        
        # Handle bull cases
        if user_input == 'ob':
            return ('single', 25)
        elif user_input == 'db':
            return ('double', 25)
        
        # Handle regular segments
        match = re.match(r'^([std])(\d+)$', user_input)
        if not match:
            return None
            
        multiplier_char, number_str = match.groups()
        number = int(number_str)
        
        # Validate segment number
        if number < 1 or number > 20:
            return None
            
        multiplier_map = {'s': 'single', 't': 'triple', 'd': 'double'}
        return (multiplier_map[multiplier_char], number)
    
    def simulate_throw(self, target_type: str, target_number: int) -> Tuple[str, int, int]:
        """Simulate a dart throw with accuracy and realistic misses"""
        # Special handling for bulls
        if target_number == 25:
            if target_type == 'single':  # Outer bull
                if random.random() < self.accuracy['single']:
                    return ('single', 25, 25)
                else:
                    # Miss outer bull - could hit double bull, single segments, or miss board
                    miss_options = [
                        ('double', 25, 50),  # Hit inner bull instead
                        ('single', 6, 6), ('single', 13, 13), ('single', 4, 4), ('single', 18, 18),  # Adjacent segments
                        ('miss', 0, 0)  # Complete miss
                    ]
                    return random.choice(miss_options)
            else:  # Double bull
                if random.random() < self.accuracy['double']:
                    return ('double', 25, 50)
                else:
                    # Miss double bull - likely hit outer bull or adjacent segments
                    miss_options = [
                        ('single', 25, 25),  # Hit outer bull instead
                        ('single', 6, 6), ('single', 13, 13), ('single', 4, 4), ('single', 18, 18),
                        ('miss', 0, 0)
                    ]
                    return random.choice(miss_options)
        
        # Regular segments
        accuracy_rate = self.accuracy[target_type]
        
        if random.random() < accuracy_rate:
            # Hit the target
            multiplier = {'single': 1, 'double': 2, 'triple': 3}[target_type]
            return (target_type, target_number, target_number * multiplier)
        else:
            # Miss - hit adjacent area or different multiplier
            return self._generate_miss(target_type, target_number)
    
    def _generate_miss(self, target_type: str, target_number: int) -> Tuple[str, int, int]:
        """Generate a realistic miss based on target"""
        miss_options = []
        
        # Add adjacent segments (most common miss)
        for adj_segment in self.adjacency[target_number]:
            miss_options.extend([
                ('single', adj_segment, adj_segment),
                ('single', adj_segment, adj_segment),  # Weight singles more
            ])
        
        # Add same segment different multiplier
        if target_type == 'triple':
            miss_options.extend([
                ('single', target_number, target_number),
                ('single', target_number, target_number),  # More likely to hit single
            ])
        elif target_type == 'double':
            miss_options.extend([
                ('single', target_number, target_number),
                ('single', target_number, target_number),
            ])
        elif target_type == 'single':
            # Less likely to accidentally hit double/triple when aiming for single
            miss_options.append(('single', target_number, target_number))
        
        # Add complete miss only for doubles (narrow outer ring, easier to miss entirely)
        if target_type == 'double':
            miss_options.append(('miss', 0, 0))
        
        return random.choice(miss_options)
    
    def is_valid_finish(self, remaining_score: int) -> bool:
        """Check if remaining score can be finished with a double"""
        if remaining_score <= 0 or remaining_score == 1:
            return False
        if remaining_score > 170:  # Maximum possible finish (T20, T20, DB)
            return True
        
        # Check if it's an even number (can finish with double)
        return remaining_score % 2 == 0 and remaining_score <= 40
    
    def apply_score(self, hit_type: str, hit_number: int, points: int) -> bool:
        """Apply score and check for bust. Returns True if valid, False if bust"""
        new_score = self.score - points
        
        # Check for bust
        if new_score < 0 or new_score == 1:
            return False
        
        # Check for valid finish (must finish on double)
        if new_score == 0:
            if hit_type != 'double':
                return False
        
        self.score = new_score
        return True
    
    def play_turn(self):
        """Play a complete turn (up to 3 darts)"""
        turn_start_score = self.score
        turn_results = []
        
        print(f"\n--- Turn {(self.darts_thrown // 3) + 1} ---")
        print(f"Current score: {self.score}")
        
        dart = 0
        while dart < 3:
            if self.game_over:
                break
                
            print(f"\nDart {dart + 1}/3")
            user_input = input("What are you aiming for? (e.g., t20, d19, s16, ob, db) [default: t20]: ").strip()
            
            # Default to t20 if empty input
            if not user_input:
                user_input = "t20"
                print("Aiming for t20 (default)")
            
            # Parse input
            parsed = self.parse_input(user_input)
            if not parsed:
                print("Invalid input! Use format like: t20, d19, s16, ob, db")
                continue  # Don't increment dart counter, just ask again
            
            target_type, target_number = parsed
            
            # Simulate throw
            hit_type, hit_number, points = self.simulate_throw(target_type, target_number)
            
            # Display result
            if hit_type == 'miss':
                print(f"Miss! You aimed for {user_input} but missed the board entirely.")
                turn_results.append("Miss (0)")
            else:
                hit_description = self._format_hit(hit_type, hit_number)
                if (hit_type, hit_number) == (target_type, target_number):
                    print(f"Great shot! You hit {hit_description} for {points} points!")
                else:
                    target_description = self._format_hit(target_type, target_number)
                    print(f"You aimed for {target_description} but hit {hit_description} for {points} points.")
                
                turn_results.append(f"{hit_description} ({points})")
            
            # Apply score
            if points > 0:
                if not self.apply_score(hit_type, hit_number, points):
                    print(f"BUST! Score would go to {self.score - points}. Turn over.")
                    self.score = turn_start_score  # Reset to start of turn
                    break
            
            self.darts_thrown += 1
            dart += 1  # Only increment dart counter after successful throw
            
            # Check for win
            if self.score == 0:
                self.game_over = True
                print(f"\n🎯 GAME OVER! You finished with {hit_description}!")
                print(f"Total darts thrown: {self.darts_thrown}")
                break
            
            print(f"Score remaining: {self.score}")
        
        # Turn summary
        print(f"\nTurn summary: {' | '.join(turn_results)}")
        
        if not self.game_over and self.score <= 170:
            if self.is_valid_finish(self.score):
                print(f"You can finish! Score: {self.score}")
            else:
                print(f"Difficult finish - Score: {self.score}")
    
    def _format_hit(self, hit_type: str, hit_number: int) -> str:
        """Format hit for display"""
        if hit_number == 25:
            return "Double Bull" if hit_type == 'double' else "Outer Bull"
        
        type_map = {'single': 'Single', 'double': 'Double', 'triple': 'Triple'}
        return f"{type_map[hit_type]} {hit_number}"
    
    def play_game(self):
        """Main game loop"""
        print("🎯 Welcome to Terminal Darts - 501!")
        print("Rules: Start with 501 points, finish on a double, 3 darts per turn")
        print("Input format: t20 (triple 20), d19 (double 19), s16 (single 16)")
        print("Special: ob (outer bull = 25), db (double bull = 50)")
        print("=" * 50)
        
        while not self.game_over:
            self.play_turn()
            
            if not self.game_over:
                input("\nPress Enter to continue to next turn...")
        
        print("\nThanks for playing!")

def main():
    game = DartsGame()
    game.play_game()

if __name__ == "__main__":
    main()
