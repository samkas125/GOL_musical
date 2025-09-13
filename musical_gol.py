#!/usr/bin/env python3
"""
Musical Conway's Game of Life
Main application file for the musical cellular automaton.

This program combines Conway's Game of Life with real-time musical generation,
creating dynamic soundscapes that evolve with the cellular patterns.

Author: AI Assistant
Version: 1.0.0
"""

import sys
import os

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from visualizer import GameVisualizer


def main():
    """Main entry point for the Musical Conway's Game of Life application."""
    print("Musical Conway's Game of Life")
    print("=============================")
    print("Loading application...")
    
    try:
        # Create and run the visualizer
        visualizer = GameVisualizer(width=60, height=40, cell_size=18)
        print("Application loaded successfully!")
        print("\nControls:")
        print("- SPACE: Start/pause simulation")
        print("- Left click: Toggle cells")
        print("- M: Toggle music")
        print("- 1-4: Change musical scale")
        print("- Q/W/E/T: Change musical mode")
        print("- F1-F8: Switch rule sets")
        print("- TAB: Cycle through rule sets")
        print("- P: Cycle through patterns")
        print("- See full controls in the application window")
        print("\nEnjoy the musical evolution!")
        
        visualizer.run()
        
    except KeyboardInterrupt:
        print("\nApplication interrupted by user.")
    except Exception as e:
        print(f"Error running application: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
