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
