#!/usr/bin/env python3
"""
Demo script for Musical Conway's Game of Life.
Shows how to use the system programmatically without the GUI.
"""

import sys
import os
import time

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from game_of_life import GameOfLife
from music_generator import MusicGenerator


def demo_patterns():
    """Demonstrate various Game of Life patterns and their musical output."""
    print("Musical Conway's Game of Life - Demo")
    print("====================================")
    
    # Create a small grid for the demo
    game = GameOfLife(width=20, height=15)
    music_gen = MusicGenerator(game)
    
    # Set musical parameters
    music_gen.set_scale('major')
    music_gen.set_mode('position')
    music_gen.set_volume(0.2)
    
    patterns = game.get_patterns()
    
    print("\nAvailable patterns:")
    for name in patterns.keys():
        print(f"  - {name}")
    
    print("\nDemonstrating patterns with musical output...")
    print("(Each pattern will run for 10 generations)")
    
    for pattern_name, pattern in patterns.items():
        print(f"\n--- {pattern_name.upper()} ---")
        
        # Clear grid and add pattern
        game.clear_grid()
        game.add_pattern(pattern, 5, 5)  # Place pattern in center
        
        print(f"Initial population: {len(game.get_living_cells())}")
        
        # Run for 10 generations
        for gen in range(10):
            print(f"Generation {game.generation}: Population = {len(game.get_living_cells())}")
            
            # Generate music for this generation
            music_gen.generate_music()
            
            # Advance to next generation
            game.next_generation()
            
            # Small delay to hear the music
            time.sleep(0.5)
        
        print(f"Final population: {len(game.get_living_cells())}")
        print("Press Enter to continue to next pattern...")
        input()
    
    print("\nDemo completed!")
    
    # Cleanup
    music_gen.cleanup()


def demo_musical_modes():
    """Demonstrate different musical generation modes."""
    print("\nMusical Modes Demo")
    print("==================")
    
    game = GameOfLife(width=15, height=10)
    music_gen = MusicGenerator(game)
    
    # Create a simple pattern
    game.add_pattern(game.get_patterns()['glider'], 3, 3)
    game.add_pattern(game.get_patterns()['blinker'], 8, 5)
    
    modes = ['position', 'density', 'pattern', 'harmonic']
    
    for mode in modes:
        print(f"\n--- {mode.upper()} MODE ---")
        music_gen.set_mode(mode)
        
        # Run for 5 generations
        for gen in range(5):
            print(f"Gen {game.generation}: {len(game.get_living_cells())} cells")
            music_gen.generate_music()
            game.next_generation()
            time.sleep(0.3)
        
        print("Press Enter for next mode...")
        input()
        game.clear_grid()
        game.add_pattern(game.get_patterns()['glider'], 3, 3)
        game.add_pattern(game.get_patterns()['blinker'], 8, 5)


if __name__ == "__main__":
    try:
        print("Choose demo mode:")
        print("1. Pattern demonstration")
        print("2. Musical modes demonstration")
        print("3. Both")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            demo_patterns()
        elif choice == "2":
            demo_musical_modes()
        elif choice == "3":
            demo_patterns()
            demo_musical_modes()
        else:
            print("Invalid choice. Running pattern demo...")
            demo_patterns()
            
    except KeyboardInterrupt:
        print("\nDemo interrupted by user.")
    except Exception as e:
        print(f"Error running demo: {e}")
        sys.exit(1)
