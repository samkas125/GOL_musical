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

- Inspired by Conway's Game of Life and generative music.
