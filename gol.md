Project Tree:
```
├── .gitignore
├── GOL_musical.md
├── README.md
├── demo.py
├── game_of_life.py
├── music_generator.py
├── musical_gol.py
├── requirements.txt
└── visualizer.py
```

# File: .gitignore
```text
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[codz]
*$py.class
.vscode

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#   Usually these files are written by a python script from a template
#   before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py.cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
# Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
# uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
# poetry.lock
# poetry.toml

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#   pdm recommends including project-wide configuration in pdm.toml, but excluding .pdm-python.
#   https://pdm-project.org/en/latest/usage/project/#working-with-version-control
# pdm.lock
# pdm.toml
.pdm-python
.pdm-build/

# pixi
#   Similar to Pipfile.lock, it is generally recommended to include pixi.lock in version control.
# pixi.lock
#   Pixi creates a virtual environment in the .pixi directory, just like venv module creates one
#   in the .venv directory. It is recommended not to include this directory in version control.
.pixi

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# Redis
*.rdb
*.aof
*.pid

# RabbitMQ
mnesia/
rabbitmq/
rabbitmq-data/

# ActiveMQ
activemq-data/

# SageMath parsed files
*.sage.py

# Environments
.env
.envrc
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#   JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#   be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#   and can be added to the global gitignore or merged into this file.  For a more nuclear
#   option (not recommended) you can uncomment the following to ignore the entire idea folder.
# .idea/

# Abstra
#   Abstra is an AI-powered process automation framework.
#   Ignore directories containing user credentials, local state, and settings.
#   Learn more at https://abstra.io/docs
.abstra/

# Visual Studio Code
#   Visual Studio Code specific template is maintained in a separate VisualStudioCode.gitignore 
#   that can be found at https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore
#   and can be added to the global gitignore or merged into this file. However, if you prefer, 
#   you could uncomment the following to ignore the entire vscode folder
# .vscode/

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc

# Marimo
marimo/_static/
marimo/_lsp/
__marimo__/

# Streamlit
.streamlit/secrets.toml

# gol.md
gol.md
```
# End of file: .gitignore

# File: GOL_musical.md
```markdown
# GOL Musical - Conway's Game of Life with Musical Elements

## Project Overview
A Python implementation of Conway's Game of Life that generates music based on the evolving patterns of cellular automata. Each living cell contributes to a musical composition, creating dynamic soundscapes that evolve with the game.

## Features
- Interactive Conway's Game of Life simulation with multiple rule sets
- Real-time musical generation based on cell patterns
- Visual grid display with pygame
- User interaction for setting initial patterns
- Multiple musical modes and scales
- 8 different cellular automaton rule sets for diverse patterns
- Extensive pattern library with rule-specific patterns

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
- 1-8: Switch between different rule sets
- P: Cycle through predefined patterns

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

## Rule Sets
The application now supports 8 different cellular automaton rule sets, each creating unique patterns:

### 1. Conway (B3/S23) - Classic
- The original Conway's Game of Life
- Creates stable patterns, oscillators, and gliders
- Perfect for traditional Game of Life patterns

### 2. HighLife (B36/S23) - Replicator
- Similar to Conway but with additional birth condition
- Features replicator patterns that can create infinite growth
- More chaotic and unpredictable than Conway

### 3. Day & Night (B3678/S34678) - Symmetric
- Creates symmetric patterns with interesting oscillatory behavior
- Good for creating balanced, aesthetic patterns
- Exhibits both growth and decay phases

### 4. Maze (B3/S12345) - Structural
- Generates maze-like structures and corridors
- Creates branching, organic-looking patterns
- Good for creating complex, interconnected structures

### 5. Coral (B3/S45678) - Growth
- Creates coral-like branching patterns that grow outward
- Tends to create dense, spreading patterns
- Good for creating natural-looking growth patterns

### 6. Seeds (B2/S) - Sparse
- Simple rule that creates sparse, seed-like patterns
- Creates very sparse, scattered patterns
- Good for creating minimalist, ambient patterns

### 7. Diamoeba (B35678/S5678) - Organic
- Creates amoeba-like patterns that can grow and contract
- Creates flowing, organic-looking patterns
- Good for creating fluid, dynamic patterns

### 8. Life without Death (B3/S012345678) - Persistent
- Cells never die, only grow and spread
- Creates ever-growing, persistent patterns
- Good for creating continuous, evolving patterns

## Pattern Library
The application includes an extensive pattern library with patterns optimized for different rule sets:
- Classic Conway patterns (glider, blinker, block, beehive, toad, beacon)
- HighLife patterns (replicator)
- Day & Night patterns (oscillators)
- Maze patterns (maze seeds)
- Coral patterns (coral seeds)
- Seeds patterns (sparse lines)
- Diamoeba patterns (organic shapes)
- Life without Death patterns (persistent gliders)
- Complex patterns (pulsar, Gosper glider gun)

## Version History
- v1.1.0: Enhanced with multiple rule sets and expanded pattern library
  - Added 8 different cellular automaton rule sets
  - Implemented flexible rule system architecture
  - Added rule-specific patterns and seeds
  - Enhanced pattern library with 20+ patterns
  - Added rule switching functionality
  - Updated documentation with rule set information
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
Supports multiple rule sets for creating different types of patterns.
"""

import numpy as np
from typing import Tuple, List, Optional, Dict, Set
from enum import Enum


class RuleSet(Enum):
    """Available rule sets for cellular automata."""
    CONWAY = "conway"           # B3/S23 - Classic Conway's Game of Life
    HIGHLIFE = "highlife"       # B36/S23 - HighLife variant
    DAY_NIGHT = "day_night"     # B3678/S34678 - Day & Night
    MAZE = "maze"               # B3/S12345 - Maze generation
    CORAL = "coral"             # B3/S45678 - Coral growth
    SEEDS = "seeds"             # B2/S - Seeds pattern
    DIAMOEBA = "diamoeba"       # B35678/S5678 - Diamoeba
    LIFE_WITHOUT_DEATH = "life_without_death"  # B3/S012345678 - Life without Death


class GameOfLife:
    """Cellular automaton with multiple rule sets for creating different patterns."""
    
    def __init__(self, width: int = 50, height: int = 50, rule_set: RuleSet = RuleSet.CONWAY):
        """
        Initialize the Game of Life grid.
        
        Args:
            width: Grid width in cells
            height: Grid height in cells
            rule_set: Rule set to use for cellular automaton
        """
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=bool)
        self.generation = 0
        self.population_history = []
        self.rule_set = rule_set
        self.birth_rules, self.survival_rules = self._parse_rules(rule_set)
    
    def _parse_rules(self, rule_set: RuleSet) -> Tuple[Set[int], Set[int]]:
        """
        Parse rule set into birth and survival conditions.
        
        Args:
            rule_set: The rule set to parse
            
        Returns:
            Tuple of (birth_conditions, survival_conditions)
        """
        rule_definitions = {
            RuleSet.CONWAY: ("B3/S23", {3}, {2, 3}),
            RuleSet.HIGHLIFE: ("B36/S23", {3, 6}, {2, 3}),
            RuleSet.DAY_NIGHT: ("B3678/S34678", {3, 6, 7, 8}, {3, 4, 6, 7, 8}),
            RuleSet.MAZE: ("B3/S12345", {3}, {1, 2, 3, 4, 5}),
            RuleSet.CORAL: ("B3/S45678", {3}, {4, 5, 6, 7, 8}),
            RuleSet.SEEDS: ("B2/S", {2}, set()),
            RuleSet.DIAMOEBA: ("B35678/S5678", {3, 5, 6, 7, 8}, {5, 6, 7, 8}),
            RuleSet.LIFE_WITHOUT_DEATH: ("B3/S012345678", {3}, {0, 1, 2, 3, 4, 5, 6, 7, 8})
        }
        
        _, birth, survival = rule_definitions[rule_set]
        return birth, survival
    
    def set_rule_set(self, rule_set: RuleSet) -> None:
        """Change the rule set for the cellular automaton."""
        self.rule_set = rule_set
        self.birth_rules, self.survival_rules = self._parse_rules(rule_set)
        
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
        """Count living neighbors around cell at (x, y) with wrapping edges."""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                # Use modulo to wrap around edges
                nx = (x + dx) % self.width
                ny = (y + dy) % self.height
                if self.grid[ny, nx]:
                    count += 1
        return count
    
    def next_generation(self) -> None:
        """Advance the game by one generation using the current rule set."""
        new_grid = np.zeros((self.height, self.width), dtype=bool)
        
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                current_state = self.grid[y, x]
                
                # Apply current rule set
                if current_state:
                    # Living cell - check survival rules
                    if neighbors in self.survival_rules:
                        new_grid[y, x] = True
                else:
                    # Dead cell - check birth rules
                    if neighbors in self.birth_rules:
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
            # Classic Conway patterns
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
            ],
            # HighLife patterns
            'replicator': [
                [1, 1, 0, 1, 1],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [1, 1, 0, 1, 1]
            ],
            # Day & Night patterns
            'day_night_oscillator': [
                [1, 1, 1, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [1, 1, 1, 1]
            ],
            # Maze patterns
            'maze_seed': [
                [1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0],
                [1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0],
                [1, 0, 1, 0, 1]
            ],
            # Coral patterns
            'coral_seed': [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]
            ],
            # Seeds patterns
            'seeds_line': [
                [1, 0, 1, 0, 1, 0, 1, 0, 1]
            ],
            # Diamoeba patterns
            'diamoeba_seed': [
                [0, 1, 1, 1, 0],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [0, 1, 1, 1, 0]
            ],
            # Life without Death patterns
            'lwd_glider': [
                [1, 1, 1],
                [1, 0, 0],
                [0, 1, 0]
            ],
            # Complex patterns
            'pulsar': [
                [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
            ],
            'gosper_glider_gun': [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        }
    
    def get_rule_set_info(self) -> Dict[str, str]:
        """Get information about the current rule set."""
        rule_info = {
            RuleSet.CONWAY: "Classic Conway's Game of Life - Creates stable patterns, oscillators, and gliders",
            RuleSet.HIGHLIFE: "HighLife - Similar to Conway but with replicator patterns that can create infinite growth",
            RuleSet.DAY_NIGHT: "Day & Night - Creates symmetric patterns with interesting oscillatory behavior",
            RuleSet.MAZE: "Maze - Generates maze-like structures and corridors",
            RuleSet.CORAL: "Coral - Creates coral-like branching patterns that grow outward",
            RuleSet.SEEDS: "Seeds - Simple rule that creates sparse, seed-like patterns",
            RuleSet.DIAMOEBA: "Diamoeba - Creates amoeba-like patterns that can grow and contract",
            RuleSet.LIFE_WITHOUT_DEATH: "Life without Death - Cells never die, only grow and spread"
        }
        return rule_info.get(self.rule_set, "Unknown rule set")
    
    def get_available_rule_sets(self) -> List[RuleSet]:
        """Get list of all available rule sets."""
        return list(RuleSet)
```
# End of file: game_of_life.py

# File: music_generator.py
```python
"""
Musical generation system for Conway's Game of Life.
Maps cellular patterns to musical elements with note name display support.
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

    # Note names corresponding to each scale
    MAJOR_NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    MINOR_NOTES = ['C', 'D♭', 'E♭', 'F', 'G', 'A♭', 'B♭']
    PENTATONIC_NOTES = ['C', 'D', 'E', 'G', 'A']
    CHROMATIC_NOTES = ['C', 'D♭', 'D', 'E♭', 'E', 'F', 'F#', 'G', 'A♭', 'A', 'B♭', 'B']

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
        self.note_names = {
            'major': self.MAJOR_NOTES,
            'minor': self.MINOR_NOTES,
            'pentatonic': self.PENTATONIC_NOTES,
            'chromatic': self.CHROMATIC_NOTES
        }
        self.current_scale = 'major'
        self.octave_range = 3  # Number of octaves to use
        self.base_octave = 3

        # Initialize pygame mixer
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

        # Musical parameters
        self.note_duration = .3  # Duration of each note in seconds
        self.max_volume = 0.25
        self.volume_decay = 0.95

        # Active sounds tracking
        self.active_sounds = []

        # Cell note mapping for display
        self.cell_notes = {}  # Maps (x, y) to note name

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

    def _get_note_name(self, x: int, y: int, scale: str = None) -> str:
        """
        Get the note name for a cell at position (x, y).

        Args:
            x: X coordinate of the cell
            y: Y coordinate of the cell
            scale: Scale to use (defaults to current scale)

        Returns:
            Note name as string (e.g., 'C', 'D♭', 'F#')
        """
        if scale is None:
            scale = self.current_scale

        # Map position to scale index
        position = (x + y) % len(self.scales[scale])
        base_note = self.note_names[scale][position]

        # Add octave number based on position
        octave_offset = ((x * 7 + y * 11) % (self.octave_range * 2)) - self.octave_range
        octave_number = self.base_octave + octave_offset

        return f"{base_note}{octave_number}"

    def _update_cell_notes(self) -> None:
        """Update the mapping of cells to their note names."""
        self.cell_notes.clear()
        living_cells = self.game.get_living_cells()

        for x, y in living_cells:
            note_name = self._get_note_name(x, y)
            self.cell_notes[(x, y)] = note_name

    def _generate_position_based_music(self) -> None:
        """Generate music based on cell positions."""
        living_cells = self.game.get_living_cells()

        for x, y in living_cells:
            frequency = self._get_note_frequency(x, y)
            volume = self.max_volume

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
                if note_index < len(self.scales[self.current_scale]):
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

        # Update cell notes for display
        self._update_cell_notes()

        # Generate new music
        if self.current_mode in self.modes:
            self.modes[self.current_mode]()

    def get_cell_note(self, x: int, y: int) -> Optional[str]:
        """
        Get the note name for a specific cell position.

        Args:
            x: X coordinate of the cell
            y: Y coordinate of the cell

        Returns:
            Note name if cell is alive and has a note, None otherwise
        """
        return self.cell_notes.get((x, y))

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
Pygame visualization for Conway's Game of Life with musical integration and note display.
"""

import pygame
import sys
from typing import Tuple, Optional
from game_of_life import GameOfLife, RuleSet
from music_generator import MusicGenerator


class GameVisualizer:
    """Handles the visual display and user interaction for the Game of Life with note display."""

    def __init__(self, width: int = 50, height: int = 50, cell_size: int = 20):  # INCREASED cell_size from 12 to 20
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
        self.screen_height = height * cell_size + 120  # Extra space for UI (increased slightly)

        # Colors
        self.colors = {
            'background': (20, 20, 20),
            'grid_lines': (40, 40, 40),
            'dead_cell': (30, 30, 30),
            'living_cell': (255, 255, 100),  # Yellow for musical cells
            'new_cell': (255, 255, 150),
            'dying_cell': (255, 100, 100),
            'text': (255, 255, 255),
            'note_text': (0, 0, 0),  # Black text for notes on yellow cells
            'ui_bg': (40, 40, 40),
            'ui_border': (80, 80, 80)
        }

        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Musical Conway's Game of Life")
        self.clock = pygame.time.Clock()

        # Font sizing based on cell size - scale appropriately
        ui_font_size = max(20, min(32, self.cell_size + 4))  # UI font scales with cell size
        small_ui_font_size = max(16, min(24, self.cell_size))  # Smaller UI font
        note_font_size = max(10, min(self.cell_size - 4, 16))  # Note font fits in cells

        self.font = pygame.font.Font(None, ui_font_size)
        self.small_font = pygame.font.Font(None, small_ui_font_size)
        self.note_font = pygame.font.Font(None, note_font_size)

        # Game state
        self.game = GameOfLife(width, height)
        self.music_gen = MusicGenerator(self.game)
        self.running = True
        self.paused = True
        self.show_grid = True
        self.show_notes = True  # Option to toggle note display
        self.music_enabled = True
        self.generation_speed = 20  # Frames per generation

        # Rule set management
        self.available_rule_sets = self.game.get_available_rule_sets()
        self.current_rule_index = 0  # Start with Conway (index 0)

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

        elif event.key == pygame.K_n:  # Toggle note display
            self.show_notes = not self.show_notes

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

        # Rule set switching (F1-F8 keys)
        elif event.key == pygame.K_F1:
            self._switch_rule_set(0)  # Conway
        elif event.key == pygame.K_F2:
            self._switch_rule_set(1)  # HighLife
        elif event.key == pygame.K_F3:
            self._switch_rule_set(2)  # Day & Night
        elif event.key == pygame.K_F4:
            self._switch_rule_set(3)  # Maze
        elif event.key == pygame.K_F5:
            self._switch_rule_set(4)  # Coral
        elif event.key == pygame.K_F6:
            self._switch_rule_set(5)  # Seeds
        elif event.key == pygame.K_F7:
            self._switch_rule_set(6)  # Diamoeba
        elif event.key == pygame.K_F8:
            self._switch_rule_set(7)  # Life without Death

        # Cycle through rule sets with Tab
        elif event.key == pygame.K_TAB:
            self._cycle_rule_set()

        # Pattern cycling with P key
        elif event.key == pygame.K_p:
            self._cycle_pattern()

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
                    # Living cell - always yellow for musical cells
                    color = self.colors['living_cell']

                    pygame.draw.rect(self.screen, color, rect)

                    # Draw inner rectangle for better visibility
                    inner_rect = pygame.Rect(x * self.cell_size + 1, y * self.cell_size + 1,
                                           self.cell_size - 2, self.cell_size - 2)
                    pygame.draw.rect(self.screen, color, inner_rect)

                    # Draw note name on top of the cell if enabled and available
                    if self.show_notes and self.music_enabled:
                        note_name = self.music_gen.get_cell_note(x, y)
                        if note_name:
                            self._draw_note_on_cell(x, y, note_name)

                else:
                    # Dead cell
                    pygame.draw.rect(self.screen, self.colors['dead_cell'], rect)

        # Draw UI
        self._draw_ui()

        pygame.display.flip()

    def _draw_note_on_cell(self, x: int, y: int, note_name: str) -> None:
        """Draw a note name on top of a cell."""
        # Create text surface
        text_surface = self.note_font.render(note_name, True, self.colors['note_text'])
        text_rect = text_surface.get_rect()

        # Center the text in the cell
        cell_center_x = x * self.cell_size + self.cell_size // 2
        cell_center_y = y * self.cell_size + self.cell_size // 2
        text_rect.center = (cell_center_x, cell_center_y)

        # Draw the text
        self.screen.blit(text_surface, text_rect)

    def _switch_rule_set(self, rule_index: int) -> None:
        """Switch to a specific rule set by index."""
        if 0 <= rule_index < len(self.available_rule_sets):
            self.current_rule_index = rule_index
            rule_set = self.available_rule_sets[rule_index]
            self.game.set_rule_set(rule_set)
            print(f"Switched to rule set: {rule_set.value}")

    def _cycle_rule_set(self) -> None:
        """Cycle to the next rule set."""
        self.current_rule_index = (self.current_rule_index + 1) % len(self.available_rule_sets)
        rule_set = self.available_rule_sets[self.current_rule_index]
        self.game.set_rule_set(rule_set)
        print(f"Switched to rule set: {rule_set.value}")

    def _cycle_pattern(self) -> None:
        """Cycle through available patterns."""
        pattern_names = list(self.patterns.keys())
        if not pattern_names:
            return
        
        if self.selected_pattern is None:
            self.selected_pattern = pattern_names[0]
        else:
            current_index = pattern_names.index(self.selected_pattern)
            self.selected_pattern = pattern_names[(current_index + 1) % len(pattern_names)]
        
        print(f"Selected pattern: {self.selected_pattern}")

    def _draw_ui(self) -> None:
        """Draw the user interface."""
        ui_y = self.height * self.cell_size + 10  # Increased margin

        # Background for UI
        ui_rect = pygame.Rect(0, ui_y, self.screen_width, self.screen_height - ui_y)
        pygame.draw.rect(self.screen, self.colors['ui_bg'], ui_rect)
        pygame.draw.line(self.screen, self.colors['ui_border'], 
                        (0, ui_y), (self.screen_width, ui_y))

        # Status information
        current_rule = self.available_rule_sets[self.current_rule_index]
        status_text = [
            f"Generation: {self.game.generation}",
            f"Population: {len(self.game.get_living_cells())}",
            f"Density: {self.game.get_cell_density():.3f}",
            f"Rule Set: {current_rule.value}",
            f"Speed: {self.generation_speed}",
            f"Volume: {self.music_gen.max_volume:.1f}"
        ]

        x_offset = 15  # Increased margin
        line_height = max(18, self.cell_size)  # Scale line height with cell size
        for i, text in enumerate(status_text):
            surface = self.small_font.render(text, True, self.colors['text'])
            self.screen.blit(surface, (x_offset, ui_y + 10 + i * line_height))

        # Controls - adjusted spacing for larger fonts
        controls_y = ui_y + 10 + len(status_text) * line_height + 15
        controls_text = [
            "SPACE: Pause/Play | R: Reset | M: Music On/Off | C: Clear | N: Notes On/Off",
            "1-4: Scale (Major/Minor/Pentatonic/Chromatic)",
            "Q/W/E/T: Mode (Position/Density/Pattern/Harmonic)",
            "F1-F8: Rule Sets | TAB: Cycle Rules | P: Cycle Patterns",
            "G: Grid | +/-: Speed | Up/Down: Volume",
            "Left Click: Toggle Cell | Right Click: Place Pattern"
        ]

        control_line_height = max(16, self.cell_size - 2)  # Slightly smaller for controls
        for i, text in enumerate(controls_text):
            surface = self.small_font.render(text, True, self.colors['text'])
            self.screen.blit(surface, (15, controls_y + i * control_line_height))

        # Current settings - positioned on the right
        settings_text = [
            f"Scale: {self.music_gen.current_scale}",
            f"Mode: {self.music_gen.current_mode}",
            f"Music: {'ON' if self.music_enabled else 'OFF'}",
            f"Notes: {'ON' if self.show_notes else 'OFF'}",
            f"Pattern: {self.selected_pattern if self.selected_pattern else 'None'}",
            f"Status: {'PAUSED' if self.paused else 'RUNNING'}"
        ]

        settings_x = max(self.screen_width - 250, self.screen_width * 0.7)  # Adaptive positioning
        for i, text in enumerate(settings_text):
            surface = self.small_font.render(text, True, self.colors['text'])
            self.screen.blit(surface, (int(settings_x), ui_y + 10 + i * line_height))

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
    # UPDATED: Larger cell size for better note visibility
    visualizer = GameVisualizer(width=60, height=40, cell_size=20)  # Increased from 10 to 20
    visualizer.run()


if __name__ == "__main__":
    main()
```
# End of file: visualizer.py

