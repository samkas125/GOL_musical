Project Tree:
```
├── GOL_musical.md
├── README.md
├── demo.py
├── game_of_life.py
├── gol.md
├── music_generator.py
├── musical_gol.py
├── requirements.txt
└── visualizer.py
```

# File: GOL_musical.md
```markdown
# GOL Musical - Conway's Game of Life with Musical Elements

## Project Overview
A Python implementation of Conway's Game of Life that generates music based on the evolving patterns of cellular automata. Each living cell contributes to a musical composition, creating dynamic soundscapes that evolve with the game.

## Features
- Interactive Conway's Game of Life simulation
- Real-time musical generation based on cell patterns
- Visual grid display with pygame
- User interaction for setting initial patterns
- Multiple musical modes and scales

## Dependencies
- pygame 2.5.2 - For graphics and sound
- numpy 1.24.3 - For efficient array operations

## Installation
```bash
pip install -r requirements.txt
```

## Usage
Run the main application:
```bash
python musical_gol.py
```

## Controls
- Left click: Toggle cell state
- Space: Start/pause simulation
- R: Reset grid
- M: Toggle music mode
- C: Clear grid
- Arrow keys: Change musical scale/pattern

## Database Schema
This project does not use a database - all state is maintained in memory.

## Project Structure
```
GOL_musical/
├── musical_gol.py          # Main application file
├── game_of_life.py         # Core Game of Life logic
├── music_generator.py      # Musical generation system
├── visualizer.py           # Pygame visualization
├── requirements.txt        # Python dependencies
└── GOL_musical.md         # This documentation
```

## Musical Implementation
The musical aspect maps cellular patterns to musical elements:
- Each living cell contributes a note based on its position
- Different musical scales and patterns can be selected
- Rhythm is determined by generation speed
- Harmonic complexity emerges from cell density patterns

## Musical Implementation Details
The musical system maps cellular patterns to musical elements through several modes:

### Position-Based Music
- Each cell's position (x, y) determines its note frequency
- Uses mathematical mapping to musical scales
- Creates spatial melodies that evolve with pattern movement

### Density-Based Music  
- Cell density determines harmonic complexity
- Dense areas generate rich chords
- Sparse areas create simple melodies
- Volume scales with density

### Pattern-Based Music
- Different cell patterns generate different sounds:
  - Clusters: Low-frequency drone sounds
  - Lines: Mid-frequency melodies  
  - Isolated cells: High-frequency individual notes
  - Edge cells: Special boundary effects

### Harmonic Music
- Population dynamics drive harmonic progressions
- Growing populations: ascending progressions (major feel)
- Shrinking populations: descending progressions (minor feel)
- Creates emotional musical narratives

## Audio System
- Real-time sine wave generation using NumPy
- Stereo output with configurable sample rates
- Volume control and decay systems
- Multiple simultaneous sound channels

## Version History
- v1.0.0: Initial implementation with basic musical generation
  - Core Game of Life logic with numpy optimization
  - Four musical generation modes
  - Four musical scales (major, minor, pentatonic, chromatic)
  - Interactive pygame visualization
  - Pattern library with common Game of Life patterns
  - Real-time audio generation and playback
```
# End of file: GOL_musical.md

# File: README.md
```markdown
# Musical Conway's Game of Life

A Python implementation of Conway's Game of Life that generates music based on the evolving patterns of cellular automata. Each living cell contributes to a musical composition, creating dynamic soundscapes that evolve with the game.

![Musical Game of Life](https://via.placeholder.com/600x400/2c3e50/ecf0f1?text=Musical+Game+of+Life)

## Features

- **Interactive Conway's Game of Life**: Click to create patterns, watch them evolve
- **Real-time Musical Generation**: Each cell contributes to the musical composition
- **Multiple Musical Modes**: Different ways to map cellular patterns to sound
- **Various Musical Scales**: Major, minor, pentatonic, and chromatic scales
- **Visual Feedback**: Color-coded cells showing age and activity
- **Pattern Library**: Predefined patterns like gliders, oscillators, and still lifes

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main application:
```bash
python musical_gol.py
```

## Controls

### Basic Controls
- **SPACE**: Start/pause the simulation
- **Left Click**: Toggle cell state (alive/dead)
- **Right Click**: Place selected pattern at cursor
- **R**: Reset the entire grid
- **C**: Clear all cells
- **G**: Toggle grid lines visibility

### Musical Controls
- **M**: Toggle music on/off
- **1-4**: Change musical scale:
  - **1**: Major scale (bright, happy)
  - **2**: Minor scale (darker, melancholic)
  - **3**: Pentatonic scale (Asian-inspired)
  - **4**: Chromatic scale (full range)

- **Q/W/E/T**: Change musical generation mode:
  - **Q**: Position-based (each cell plays a note based on its position)
  - **W**: Density-based (chords based on cell density)
  - **E**: Pattern-based (different sounds for different cell patterns)
  - **T**: Harmonic (population dynamics create harmonic progressions)

### Speed and Volume
- **+/-**: Increase/decrease simulation speed
- **Up/Down Arrow**: Increase/decrease music volume

## Musical Modes Explained

### Position-Based Mode
Each living cell plays a note determined by its X and Y coordinates. This creates spatial melodies that change as patterns move and evolve.

### Density-Based Mode
The density of living cells determines the complexity of the music. Dense areas create rich chords, while sparse areas play simpler melodies.

### Pattern-Based Mode
Different types of cellular patterns (clusters, lines, isolated cells) generate different musical elements, creating complex polyphonic compositions.

### Harmonic Mode
Population changes drive harmonic progressions. Growing populations create ascending progressions, while shrinking populations create descending ones.

## Patterns

The application includes several predefined patterns:

- **Glider**: A moving pattern that travels diagonally
- **Blinker**: A simple oscillator
- **Block**: A stable 2x2 pattern
- **Beehive**: A stable hexagonal pattern
- **Toad**: A period-2 oscillator
- **Beacon**: A period-2 oscillator with two blocks

## Technical Details

- **Framework**: Python with Pygame for graphics and sound
- **Audio**: Real-time sine wave generation using NumPy
- **Visualization**: 60x40 cell grid with customizable cell size
- **Performance**: Optimized for smooth real-time audio and video

## Requirements

- Python 3.7+
- pygame 2.5.2
- numpy 1.24.3

## Tips for Best Experience

1. **Start Small**: Begin with simple patterns to hear the basic musical elements
2. **Experiment**: Try different scales and modes to find your preferred sound
3. **Watch Patterns**: Some patterns like gliders create moving melodies
4. **Density Matters**: Dense patterns create richer, more complex music
5. **Evolution**: Let patterns evolve naturally - the music changes as they do

## Troubleshooting

### No Sound
- Make sure your system volume is up
- Check that pygame's audio system is working
- Try adjusting the volume with Up/Down arrows

### Performance Issues
- Reduce the grid size in the code
- Increase the generation speed (use + key)
- Close other audio applications

### Import Errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check that you're running Python 3.7 or later

## Contributing

Feel free to fork this project and add your own musical modes, scales, or visual enhancements!

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Inspired by Conway's Game of Life and generative music
- Built with Python, Pygame, and NumPy
- Musical scales and theory inspired by traditional music theory
```
# End of file: README.md

# File: demo.py
```python
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
```
# End of file: demo.py

# File: game_of_life.py
```python
"""
Conway's Game of Life implementation with musical integration support.
"""

import numpy as np
from typing import Tuple, List, Optional


class GameOfLife:
    """Conway's Game of Life cellular automaton."""
    
    def __init__(self, width: int = 50, height: int = 50):
        """
        Initialize the Game of Life grid.
        
        Args:
            width: Grid width in cells
            height: Grid height in cells
        """
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=bool)
        self.generation = 0
        self.population_history = []
        
    def set_cell(self, x: int, y: int, alive: bool) -> None:
        """Set the state of a cell at position (x, y)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y, x] = alive
    
    def get_cell(self, x: int, y: int) -> bool:
        """Get the state of a cell at position (x, y)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y, x]
        return False
    
    def toggle_cell(self, x: int, y: int) -> None:
        """Toggle the state of a cell at position (x, y)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y, x] = not self.grid[y, x]
    
    def count_neighbors(self, x: int, y: int) -> int:
        """Count living neighbors around cell at (x, y)."""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.grid[ny, nx]:
                        count += 1
        return count
    
    def next_generation(self) -> None:
        """Advance the game by one generation."""
        new_grid = np.zeros((self.height, self.width), dtype=bool)
        
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                current_state = self.grid[y, x]
                
                # Apply Conway's rules
                if current_state:
                    # Living cell
                    if neighbors == 2 or neighbors == 3:
                        new_grid[y, x] = True
                else:
                    # Dead cell
                    if neighbors == 3:
                        new_grid[y, x] = True
        
        self.grid = new_grid
        self.generation += 1
        
        # Track population for musical analysis
        population = np.sum(self.grid)
        self.population_history.append(population)
        
        # Keep only last 100 generations for memory efficiency
        if len(self.population_history) > 100:
            self.population_history = self.population_history[-100:]
    
    def clear_grid(self) -> None:
        """Clear all cells from the grid."""
        self.grid.fill(False)
        self.generation = 0
        self.population_history = []
    
    def get_living_cells(self) -> List[Tuple[int, int]]:
        """Get list of coordinates of all living cells."""
        return [(x, y) for y in range(self.height) for x in range(self.width) if self.grid[y, x]]
    
    def get_cell_density(self) -> float:
        """Get the density of living cells (0.0 to 1.0)."""
        return np.sum(self.grid) / (self.width * self.height)
    
    def get_population_change(self) -> int:
        """Get the change in population from last generation."""
        if len(self.population_history) < 2:
            return 0
        return self.population_history[-1] - self.population_history[-2]
    
    def add_pattern(self, pattern: List[List[int]], x: int, y: int) -> None:
        """
        Add a predefined pattern to the grid at position (x, y).
        
        Args:
            pattern: 2D list where 1 represents living cell, 0 represents dead cell
            x: X coordinate of top-left corner
            y: Y coordinate of top-left corner
        """
        for py, row in enumerate(pattern):
            for px, cell in enumerate(row):
                if cell == 1:
                    self.set_cell(x + px, y + py, True)
    
    def get_patterns(self) -> dict:
        """Get dictionary of predefined patterns."""
        return {
            'glider': [
                [0, 1, 0],
                [0, 0, 1],
                [1, 1, 1]
            ],
            'blinker': [
                [1, 1, 1]
            ],
            'block': [
                [1, 1],
                [1, 1]
            ],
            'beehive': [
                [0, 1, 1, 0],
                [1, 0, 0, 1],
                [0, 1, 1, 0]
            ],
            'toad': [
                [0, 1, 1, 1],
                [1, 1, 1, 0]
            ],
            'beacon': [
                [1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, 1]
            ]
        }
```
# End of file: game_of_life.py

# File: gol.md
```markdown
Project Tree:
```
├── GOL_musical.md
├── README.md
├── demo.py
├── game_of_life.py
├── gol.md
├── music_generator.py
├── musical_gol.py
├── requirements.txt
└── visualizer.py
```

# File: GOL_musical.md
```markdown
# GOL Musical - Conway's Game of Life with Musical Elements

## Project Overview
A Python implementation of Conway's Game of Life that generates music based on the evolving patterns of cellular automata. Each living cell contributes to a musical composition, creating dynamic soundscapes that evolve with the game.

## Features
- Interactive Conway's Game of Life simulation
- Real-time musical generation based on cell patterns
- Visual grid display with pygame
- User interaction for setting initial patterns
- Multiple musical modes and scales

## Dependencies
- pygame 2.5.2 - For graphics and sound
- numpy 1.24.3 - For efficient array operations

## Installation
```bash
pip install -r requirements.txt
```

## Usage
Run the main application:
```bash
python musical_gol.py
```

## Controls
- Left click: Toggle cell state
- Space: Start/pause simulation
- R: Reset grid
- M: Toggle music mode
- C: Clear grid
- Arrow keys: Change musical scale/pattern

## Database Schema
This project does not use a database - all state is maintained in memory.

## Project Structure
```
GOL_musical/
├── musical_gol.py          # Main application file
├── game_of_life.py         # Core Game of Life logic
├── music_generator.py      # Musical generation system
├── visualizer.py           # Pygame visualization
├── requirements.txt        # Python dependencies
└── GOL_musical.md         # This documentation
```

## Musical Implementation
The musical aspect maps cellular patterns to musical elements:
- Each living cell contributes a note based on its position
- Different musical scales and patterns can be selected
- Rhythm is determined by generation speed
- Harmonic complexity emerges from cell density patterns

## Musical Implementation Details
The musical system maps cellular patterns to musical elements through several modes:

### Position-Based Music
- Each cell's position (x, y) determines its note frequency
- Uses mathematical mapping to musical scales
- Creates spatial melodies that evolve with pattern movement

### Density-Based Music  
- Cell density determines harmonic complexity
- Dense areas generate rich chords
- Sparse areas create simple melodies
- Volume scales with density

### Pattern-Based Music
- Different cell patterns generate different sounds:
  - Clusters: Low-frequency drone sounds
  - Lines: Mid-frequency melodies  
  - Isolated cells: High-frequency individual notes
  - Edge cells: Special boundary effects

### Harmonic Music
- Population dynamics drive harmonic progressions
- Growing populations: ascending progressions (major feel)
- Shrinking populations: descending progressions (minor feel)
- Creates emotional musical narratives

## Audio System
- Real-time sine wave generation using NumPy
- Stereo output with configurable sample rates
- Volume control and decay systems
- Multiple simultaneous sound channels

## Version History
- v1.0.0: Initial implementation with basic musical generation
  - Core Game of Life logic with numpy optimization
  - Four musical generation modes
  - Four musical scales (major, minor, pentatonic, chromatic)
  - Interactive pygame visualization
  - Pattern library with common Game of Life patterns
  - Real-time audio generation and playback
```
# End of file: GOL_musical.md

# File: README.md
```markdown
# Musical Conway's Game of Life

A Python implementation of Conway's Game of Life that generates music based on the evolving patterns of cellular automata. Each living cell contributes to a musical composition, creating dynamic soundscapes that evolve with the game.

![Musical Game of Life](https://via.placeholder.com/600x400/2c3e50/ecf0f1?text=Musical+Game+of+Life)

## Features

- **Interactive Conway's Game of Life**: Click to create patterns, watch them evolve
- **Real-time Musical Generation**: Each cell contributes to the musical composition
- **Multiple Musical Modes**: Different ways to map cellular patterns to sound
- **Various Musical Scales**: Major, minor, pentatonic, and chromatic scales
- **Visual Feedback**: Color-coded cells showing age and activity
- **Pattern Library**: Predefined patterns like gliders, oscillators, and still lifes

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main application:
```bash
python musical_gol.py
```

## Controls

### Basic Controls
- **SPACE**: Start/pause the simulation
- **Left Click**: Toggle cell state (alive/dead)
- **Right Click**: Place selected pattern at cursor
- **R**: Reset the entire grid
- **C**: Clear all cells
- **G**: Toggle grid lines visibility

### Musical Controls
- **M**: Toggle music on/off
- **1-4**: Change musical scale:
  - **1**: Major scale (bright, happy)
  - **2**: Minor scale (darker, melancholic)
  - **3**: Pentatonic scale (Asian-inspired)
  - **4**: Chromatic scale (full range)

- **Q/W/E/T**: Change musical generation mode:
  - **Q**: Position-based (each cell plays a note based on its position)
  - **W**: Density-based (chords based on cell density)
  - **E**: Pattern-based (different sounds for different cell patterns)
  - **T**: Harmonic (population dynamics create harmonic progressions)

### Speed and Volume
- **+/-**: Increase/decrease simulation speed
- **Up/Down Arrow**: Increase/decrease music volume

## Musical Modes Explained

### Position-Based Mode
Each living cell plays a note determined by its X and Y coordinates. This creates spatial melodies that change as patterns move and evolve.

### Density-Based Mode
The density of living cells determines the complexity of the music. Dense areas create rich chords, while sparse areas play simpler melodies.

### Pattern-Based Mode
Different types of cellular patterns (clusters, lines, isolated cells) generate different musical elements, creating complex polyphonic compositions.

### Harmonic Mode
Population changes drive harmonic progressions. Growing populations create ascending progressions, while shrinking populations create descending ones.

## Patterns

The application includes several predefined patterns:

- **Glider**: A moving pattern that travels diagonally
- **Blinker**: A simple oscillator
- **Block**: A stable 2x2 pattern
- **Beehive**: A stable hexagonal pattern
- **Toad**: A period-2 oscillator
- **Beacon**: A period-2 oscillator with two blocks

## Technical Details

- **Framework**: Python with Pygame for graphics and sound
- **Audio**: Real-time sine wave generation using NumPy
- **Visualization**: 60x40 cell grid with customizable cell size
- **Performance**: Optimized for smooth real-time audio and video

## Requirements

- Python 3.7+
- pygame 2.5.2
- numpy 1.24.3

## Tips for Best Experience

1. **Start Small**: Begin with simple patterns to hear the basic musical elements
2. **Experiment**: Try different scales and modes to find your preferred sound
3. **Watch Patterns**: Some patterns like gliders create moving melodies
4. **Density Matters**: Dense patterns create richer, more complex music
5. **Evolution**: Let patterns evolve naturally - the music changes as they do

## Troubleshooting

### No Sound
- Make sure your system volume is up
- Check that pygame's audio system is working
- Try adjusting the volume with Up/Down arrows

### Performance Issues
- Reduce the grid size in the code
- Increase the generation speed (use + key)
- Close other audio applications

### Import Errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check that you're running Python 3.7 or later

## Contributing

Feel free to fork this project and add your own musical modes, scales, or visual enhancements!

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Inspired by Conway's Game of Life and generative music
- Built with Python, Pygame, and NumPy
- Musical scales and theory inspired by traditional music theory
```
# End of file: README.md

# File: demo.py
```python
```
# End of file: gol.md

# File: music_generator.py
```python
"""
Musical generation system for Conway's Game of Life.
Maps cellular patterns to musical elements.
"""

import pygame
import numpy as np
import math
from typing import List, Tuple, Dict, Optional
from game_of_life import GameOfLife


class MusicGenerator:
    """Generates music based on Game of Life patterns."""
    
    # Musical scales and frequencies
    MAJOR_SCALE = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]  # C major
    MINOR_SCALE = [261.63, 277.18, 311.13, 349.23, 392.00, 415.30, 466.16]  # C minor
    PENTATONIC = [261.63, 293.66, 329.63, 392.00, 440.00]  # C pentatonic
    CHROMATIC = [261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 
                 392.00, 415.30, 440.00, 466.16, 493.88]  # C chromatic
    
    def __init__(self, game: GameOfLife):
        """
        Initialize the music generator.
        
        Args:
            game: GameOfLife instance to generate music from
        """
        self.game = game
        self.scales = {
            'major': self.MAJOR_SCALE,
            'minor': self.MINOR_SCALE,
            'pentatonic': self.PENTATONIC,
            'chromatic': self.CHROMATIC
        }
        self.current_scale = 'major'
        self.octave_range = 3  # Number of octaves to use
        self.base_octave = 3
        
        # Initialize pygame mixer
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        
        # Musical parameters
        self.note_duration = 0.1  # Duration of each note in seconds
        self.max_volume = 0.3
        self.volume_decay = 0.95
        
        # Active sounds tracking
        self.active_sounds = []
        
        # Musical modes
        self.modes = {
            'position': self._generate_position_based_music,
            'density': self._generate_density_based_music,
            'pattern': self._generate_pattern_based_music,
            'harmonic': self._generate_harmonic_music
        }
        self.current_mode = 'position'
        
    def _generate_tone(self, frequency: float, duration: float, volume: float = 0.3) -> pygame.mixer.Sound:
        """Generate a pure tone at the specified frequency."""
        sample_rate = pygame.mixer.get_init()[0]
        frames = int(duration * sample_rate)
        
        # Generate sine wave
        wave = np.zeros(frames)
        for i in range(frames):
            wave[i] = volume * math.sin(2 * math.pi * frequency * i / sample_rate)
        
        # Convert to 16-bit signed integers
        wave = (wave * 32767).astype(np.int16)
        
        # Create stereo sound
        stereo_wave = np.zeros((frames, 2), dtype=np.int16)
        stereo_wave[:, 0] = wave
        stereo_wave[:, 1] = wave
        
        return pygame.mixer.Sound(stereo_wave)
    
    def _get_note_frequency(self, x: int, y: int, scale: str = None) -> float:
        """
        Map cell position to musical frequency.
        
        Args:
            x: X coordinate of the cell
            y: Y coordinate of the cell
            scale: Scale to use (defaults to current scale)
            
        Returns:
            Frequency in Hz
        """
        if scale is None:
            scale = self.current_scale
        
        # Map position to scale index
        position = (x + y) % len(self.scales[scale])
        base_frequency = self.scales[scale][position]
        
        # Add octave variation based on position
        octave_offset = ((x * 7 + y * 11) % (self.octave_range * 2)) - self.octave_range
        frequency = base_frequency * (2 ** octave_offset)
        
        return frequency
    
    def _generate_position_based_music(self) -> None:
        """Generate music based on cell positions."""
        living_cells = self.game.get_living_cells()
        
        for x, y in living_cells:
            frequency = self._get_note_frequency(x, y)
            volume = self.max_volume * (0.5 + 0.5 * math.sin(self.game.generation * 0.1))
            
            # Create and play note
            sound = self._generate_tone(frequency, self.note_duration, volume)
            channel = sound.play()
            
            if channel:
                self.active_sounds.append(channel)
    
    def _generate_density_based_music(self) -> None:
        """Generate music based on cell density patterns."""
        density = self.game.get_cell_density()
        
        if density > 0.1:  # Only generate sound if there are enough cells
            # Use density to determine frequency range
            base_freq = 200 + density * 800
            
            # Generate chord based on density
            chord_notes = 3 + int(density * 4)
            for i in range(chord_notes):
                frequency = base_freq * (1 + i * 0.5)
                volume = self.max_volume * density * 0.8
                
                sound = self._generate_tone(frequency, self.note_duration * 2, volume)
                channel = sound.play()
                
                if channel:
                    self.active_sounds.append(channel)
    
    def _generate_pattern_based_music(self) -> None:
        """Generate music based on specific cell patterns."""
        # Analyze patterns in the grid
        patterns = self._analyze_patterns()
        
        for pattern_type, positions in patterns.items():
            if positions:
                # Generate different sounds for different patterns
                base_freq = {
                    'clusters': 300,
                    'lines': 400,
                    'isolated': 500,
                    'edges': 600
                }.get(pattern_type, 350)
                
                for x, y in positions[:5]:  # Limit to 5 positions per pattern
                    frequency = base_freq + (x + y) * 10
                    volume = self.max_volume * 0.6
                    
                    sound = self._generate_tone(frequency, self.note_duration, volume)
                    channel = sound.play()
                    
                    if channel:
                        self.active_sounds.append(channel)
    
    def _generate_harmonic_music(self) -> None:
        """Generate harmonic music based on population dynamics."""
        population_change = self.game.get_population_change()
        
        if abs(population_change) > 0:
            # Use population change to determine harmonic progression
            base_note = 0
            if population_change > 0:
                # Growing population - ascending progression
                progression = [0, 2, 4, 6]  # Major progression
            else:
                # Shrinking population - descending progression
                progression = [6, 4, 2, 0]  # Minor progression
            
            for note_index in progression:
                frequency = self.scales[self.current_scale][note_index] * (2 ** self.base_octave)
                volume = self.max_volume * 0.4
                
                sound = self._generate_tone(frequency, self.note_duration * 1.5, volume)
                channel = sound.play()
                
                if channel:
                    self.active_sounds.append(channel)
    
    def _analyze_patterns(self) -> Dict[str, List[Tuple[int, int]]]:
        """Analyze the grid for different types of patterns."""
        patterns = {
            'clusters': [],
            'lines': [],
            'isolated': [],
            'edges': []
        }
        
        living_cells = self.game.get_living_cells()
        
        for x, y in living_cells:
            neighbors = self.game.count_neighbors(x, y)
            
            # Categorize based on neighbor count and position
            if neighbors >= 4:
                patterns['clusters'].append((x, y))
            elif neighbors <= 1:
                patterns['isolated'].append((x, y))
            elif neighbors == 2:
                # Check if it's part of a line
                if self._is_part_of_line(x, y):
                    patterns['lines'].append((x, y))
            
            # Check if on edge
            if x == 0 or x == self.game.width - 1 or y == 0 or y == self.game.height - 1:
                patterns['edges'].append((x, y))
        
        return patterns
    
    def _is_part_of_line(self, x: int, y: int) -> bool:
        """Check if a cell is part of a linear pattern."""
        # Simple line detection - check if neighbors are aligned
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.game.width and 0 <= ny < self.game.height and 
                    self.game.get_cell(nx, ny)):
                    neighbors.append((dx, dy))
        
        if len(neighbors) == 2:
            # Check if neighbors are aligned
            dx1, dy1 = neighbors[0]
            dx2, dy2 = neighbors[1]
            
            # Horizontal, vertical, or diagonal alignment
            return (dx1 == dx2 == 0) or (dy1 == dy2 == 0) or (dx1 == dx2 and dy1 == dy2)
        
        return False
    
    def generate_music(self) -> None:
        """Generate music based on current game state and mode."""
        # Clean up finished sounds
        self.active_sounds = [s for s in self.active_sounds if s.get_busy()]
        
        # Generate new music
        if self.current_mode in self.modes:
            self.modes[self.current_mode]()
    
    def set_scale(self, scale: str) -> None:
        """Set the musical scale to use."""
        if scale in self.scales:
            self.current_scale = scale
    
    def set_mode(self, mode: str) -> None:
        """Set the musical generation mode."""
        if mode in self.modes:
            self.current_mode = mode
    
    def set_volume(self, volume: float) -> None:
        """Set the maximum volume for generated sounds."""
        self.max_volume = max(0.0, min(1.0, volume))
    
    def stop_all_sounds(self) -> None:
        """Stop all currently playing sounds."""
        pygame.mixer.stop()
        self.active_sounds = []
    
    def cleanup(self) -> None:
        """Clean up resources."""
        self.stop_all_sounds()
        pygame.mixer.quit()
```
# End of file: music_generator.py

# File: musical_gol.py
```python
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
        visualizer = GameVisualizer(width=60, height=40, cell_size=10)
        print("Application loaded successfully!")
        print("\nControls:")
        print("- SPACE: Start/pause simulation")
        print("- Left click: Toggle cells")
        print("- M: Toggle music")
        print("- 1-4: Change musical scale")
        print("- Q/W/E/T: Change musical mode")
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
```
# End of file: musical_gol.py

# File: requirements.txt
```text
pygame==2.5.2
numpy==1.24.3
```
# End of file: requirements.txt

# File: visualizer.py
```python
"""
Pygame visualization for Conway's Game of Life with musical integration.
"""

import pygame
import sys
from typing import Tuple, Optional
from game_of_life import GameOfLife
from music_generator import MusicGenerator


class GameVisualizer:
    """Handles the visual display and user interaction for the Game of Life."""
    
    def __init__(self, width: int = 50, height: int = 50, cell_size: int = 12):
        """
        Initialize the visualizer.
        
        Args:
            width: Grid width in cells
            height: Grid height in cells
            cell_size: Size of each cell in pixels
        """
        self.cell_size = cell_size
        self.width = width
        self.height = height
        
        # Calculate screen dimensions
        self.screen_width = width * cell_size
        self.screen_height = height * cell_size + 100  # Extra space for UI
        
        # Colors
        self.colors = {
            'background': (20, 20, 20),
            'grid_lines': (40, 40, 40),
            'dead_cell': (30, 30, 30),
            'living_cell': (100, 200, 255),
            'new_cell': (255, 255, 100),
            'dying_cell': (255, 100, 100),
            'text': (255, 255, 255),
            'ui_bg': (40, 40, 40),
            'ui_border': (80, 80, 80)
        }
        
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Musical Conway's Game of Life")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 18)
        
        # Game state
        self.game = GameOfLife(width, height)
        self.music_gen = MusicGenerator(self.game)
        self.running = True
        self.paused = True
        self.show_grid = True
        self.music_enabled = True
        self.generation_speed = 5  # Frames per generation
        
        # UI state
        self.selected_pattern = None
        self.patterns = self.game.get_patterns()
        
        # Animation
        self.frame_counter = 0
        self.cell_ages = {}  # Track how long cells have been alive
        
    def handle_events(self) -> None:
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse_click(event)
            
            elif event.type == pygame.MOUSEMOTION:
                self._handle_mouse_motion(event)
    
    def _handle_keydown(self, event: pygame.event.Event) -> None:
        """Handle keyboard input."""
        if event.key == pygame.K_SPACE:
            self.paused = not self.paused
        
        elif event.key == pygame.K_r:
            self.game.clear_grid()
            self.cell_ages = {}
            self.paused = True
        
        elif event.key == pygame.K_m:
            self.music_enabled = not self.music_enabled
        
        elif event.key == pygame.K_c:
            self.game.clear_grid()
            self.cell_ages = {}
        
        elif event.key == pygame.K_g:
            self.show_grid = not self.show_grid
        
        elif event.key == pygame.K_1:
            self.music_gen.set_scale('major')
        elif event.key == pygame.K_2:
            self.music_gen.set_scale('minor')
        elif event.key == pygame.K_3:
            self.music_gen.set_scale('pentatonic')
        elif event.key == pygame.K_4:
            self.music_gen.set_scale('chromatic')
        
        elif event.key == pygame.K_q:
            self.music_gen.set_mode('position')
        elif event.key == pygame.K_w:
            self.music_gen.set_mode('density')
        elif event.key == pygame.K_e:
            self.music_gen.set_mode('pattern')
        elif event.key == pygame.K_t:
            self.music_gen.set_mode('harmonic')
        
        elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
            self.generation_speed = max(1, self.generation_speed - 1)
        elif event.key == pygame.K_MINUS:
            self.generation_speed = min(20, self.generation_speed + 1)
        
        elif event.key == pygame.K_UP:
            self.music_gen.max_volume = min(1.0, self.music_gen.max_volume + 0.1)
        elif event.key == pygame.K_DOWN:
            self.music_gen.max_volume = max(0.0, self.music_gen.max_volume - 0.1)
    
    def _handle_mouse_click(self, event: pygame.event.Event) -> None:
        """Handle mouse clicks."""
        if event.button == 1:  # Left click
            x, y = event.pos
            if y < self.height * self.cell_size:  # Click within grid
                grid_x = x // self.cell_size
                grid_y = y // self.cell_size
                self.game.toggle_cell(grid_x, grid_y)
                
                # Track cell age for new cells
                if self.game.get_cell(grid_x, grid_y):
                    self.cell_ages[(grid_x, grid_y)] = 0
        
        elif event.button == 3:  # Right click - place pattern
            if self.selected_pattern:
                x, y = event.pos
                grid_x = x // self.cell_size
                grid_y = y // self.cell_size
                self.game.add_pattern(self.patterns[self.selected_pattern], grid_x, grid_y)
    
    def _handle_mouse_motion(self, event: pygame.event.Event) -> None:
        """Handle mouse motion for drawing."""
        if pygame.mouse.get_pressed()[0]:  # Left mouse button held
            x, y = event.pos
            if y < self.height * self.cell_size:  # Within grid
                grid_x = x // self.cell_size
                grid_y = y // self.cell_size
                if not self.game.get_cell(grid_x, grid_y):  # Only toggle if cell is dead
                    self.game.set_cell(grid_x, grid_y, True)
                    self.cell_ages[(grid_x, grid_y)] = 0
    
    def update(self) -> None:
        """Update the game state."""
        self.frame_counter += 1
        
        # Update cell ages
        for pos in list(self.cell_ages.keys()):
            if self.game.get_cell(pos[0], pos[1]):
                self.cell_ages[pos] += 1
            else:
                del self.cell_ages[pos]
        
        # Advance generation
        if not self.paused and self.frame_counter >= self.generation_speed:
            self.game.next_generation()
            self.frame_counter = 0
            
            # Generate music
            if self.music_enabled:
                self.music_gen.generate_music()
    
    def draw(self) -> None:
        """Draw the current state."""
        self.screen.fill(self.colors['background'])
        
        # Draw grid
        if self.show_grid:
            for x in range(0, self.screen_width, self.cell_size):
                pygame.draw.line(self.screen, self.colors['grid_lines'], 
                               (x, 0), (x, self.height * self.cell_size))
            for y in range(0, self.height * self.cell_size, self.cell_size):
                pygame.draw.line(self.screen, self.colors['grid_lines'], 
                               (0, y), (self.screen_width, y))
        
        # Draw cells
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, 
                                 self.cell_size, self.cell_size)
                
                if self.game.get_cell(x, y):
                    # Living cell - color based on age
                    age = self.cell_ages.get((x, y), 0)
                    if age < 3:
                        color = self.colors['new_cell']
                    else:
                        # Gradual color change based on age
                        intensity = min(255, 100 + age * 5)
                        color = (100, intensity, 255)
                    
                    pygame.draw.rect(self.screen, color, rect)
                    
                    # Draw inner rectangle for better visibility
                    inner_rect = pygame.Rect(x * self.cell_size + 1, y * self.cell_size + 1,
                                           self.cell_size - 2, self.cell_size - 2)
                    pygame.draw.rect(self.screen, color, inner_rect)
                else:
                    # Dead cell
                    pygame.draw.rect(self.screen, self.colors['dead_cell'], rect)
        
        # Draw UI
        self._draw_ui()
        
        pygame.display.flip()
    
    def _draw_ui(self) -> None:
        """Draw the user interface."""
        ui_y = self.height * self.cell_size + 5
        
        # Background for UI
        ui_rect = pygame.Rect(0, ui_y, self.screen_width, self.screen_height - ui_y)
        pygame.draw.rect(self.screen, self.colors['ui_bg'], ui_rect)
        pygame.draw.line(self.screen, self.colors['ui_border'], 
                        (0, ui_y), (self.screen_width, ui_y))
        
        # Status information
        status_text = [
            f"Generation: {self.game.generation}",
            f"Population: {len(self.game.get_living_cells())}",
            f"Density: {self.game.get_cell_density():.3f}",
            f"Speed: {self.generation_speed}",
            f"Volume: {self.music_gen.max_volume:.1f}"
        ]
        
        x_offset = 10
        for i, text in enumerate(status_text):
            surface = self.small_font.render(text, True, self.colors['text'])
            self.screen.blit(surface, (x_offset, ui_y + 5 + i * 20))
        
        # Controls
        controls_text = [
            "SPACE: Pause/Play | R: Reset | M: Music On/Off | C: Clear",
            "1-4: Scale (Major/Minor/Pentatonic/Chromatic)",
            "Q/W/E/T: Mode (Position/Density/Pattern/Harmonic)",
            "G: Grid | +/-: Speed | Up/Down: Volume",
            "Left Click: Toggle Cell | Right Click: Place Pattern"
        ]
        
        for i, text in enumerate(controls_text):
            surface = self.small_font.render(text, True, self.colors['text'])
            self.screen.blit(surface, (10, ui_y + 120 + i * 15))
        
        # Current settings
        settings_text = [
            f"Scale: {self.music_gen.current_scale}",
            f"Mode: {self.music_gen.current_mode}",
            f"Music: {'ON' if self.music_enabled else 'OFF'}",
            f"Status: {'PAUSED' if self.paused else 'RUNNING'}"
        ]
        
        x_offset = self.screen_width - 200
        for i, text in enumerate(settings_text):
            surface = self.small_font.render(text, True, self.colors['text'])
            self.screen.blit(surface, (x_offset, ui_y + 5 + i * 20))
    
    def run(self) -> None:
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        self.cleanup()
    
    def cleanup(self) -> None:
        """Clean up resources."""
        self.music_gen.cleanup()
        pygame.quit()
        sys.exit()


def main():
    """Main entry point."""
    visualizer = GameVisualizer(width=60, height=40, cell_size=10)
    visualizer.run()


if __name__ == "__main__":
    main()
```
# End of file: visualizer.py

