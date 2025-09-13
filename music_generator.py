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
        self.note_duration = 0.1  # Duration of each note in seconds
        self.max_volume = 0.3
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
