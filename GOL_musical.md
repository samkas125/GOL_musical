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

### Basic Controls
- **Left Click**: Toggle cell state
- **Space**: Start/pause simulation
- **R**: Reset grid
- **M**: Toggle music mode
- **N**: Toggle note display
- **G**: Toggle grid lines
- **+/-**: Adjust generation speed
- **Up/Down**: Adjust volume
- **Right Click**: Place selected pattern

### Musical Controls
- **S**: Cycle through all musical scales (24 scales total)
- **Q/W/E/T**: Switch musical modes (Position/Density/Pattern/Harmonic)

### Pattern & Rule Controls
- **P**: Cycle through predefined patterns
- **F1-F8**: Switch between different rule sets
- **TAB**: Cycle through rule sets
- **WHITE CELLS**: Currently playing notes (visual feedback)

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

## Musical Features

### Visual Feedback
- **Playing Notes**: Cells currently playing notes are highlighted in white
- **Scale Colors**: Different scales use different color palettes
- **Real-time Settings**: Live display of current musical parameters
- **Consolidated Controls**: Simple scale cycling with S key

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
- v1.2.0: Major musical enhancement with rich sound generation
  - Enhanced tone generation with multiple waveforms and harmonic synthesis
  - Added ADSR envelope shaping and reverb effects
  - Implemented chord generation with density-based selection
  - Added melodic phrasing and interval-based note transitions
  - Enhanced rhythm patterns with syncopation and tempo control
  - Improved visual feedback with playing note highlighting
  - Added comprehensive musical controls and settings display
  - Enhanced UI with real-time parameter display
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
