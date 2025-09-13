
"""
Musical generation system for Conway's Game of Life.
Maps cellular patterns to musical elements with note name display support.
Includes automatic note thinning - only plays lowest newborn note per row.
Notes that are playing are visually indicated with white cells.
"""

import pygame
import numpy as np
import math
from typing import List, Tuple, Dict, Optional, Set
from game_of_life import GameOfLife


class MusicGenerator:
    """Generates music based on Game of Life patterns with intelligent note thinning and visual feedback."""

    # Musical scales and frequencies
    MAJOR_SCALE = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]  # C major
    MINOR_SCALE = [261.63, 277.18, 311.13, 349.23, 392.00, 415.30, 466.16]  # C minor
    PENTATONIC = [261.63, 293.66, 329.63, 392.00, 440.00]  # C pentatonic
    CHROMATIC = [261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 
                 392.00, 415.30, 440.00, 466.16, 493.88]  # C chromatic

    # Additional scales from your project
    NATURAL_MINOR = [261.63, 293.66, 311.13, 349.23, 392.00, 415.30, 466.16]
    HARMONIC_MINOR = [261.63, 293.66, 311.13, 349.23, 392.00, 415.30, 493.88]
    MELODIC_MINOR = [261.63, 293.66, 311.13, 349.23, 392.00, 440.00, 493.88]
    MAJOR_PENTATONIC = [261.63, 293.66, 329.63, 392.00, 440.00]
    MINOR_PENTATONIC = [261.63, 311.13, 349.23, 392.00, 466.16]
    BLUES_SCALE = [261.63, 311.13, 349.23, 369.99, 392.00, 466.16]

    # Modes
    IONIAN = MAJOR_SCALE
    DORIAN = [261.63, 293.66, 311.13, 349.23, 392.00, 440.00, 466.16]
    PHRYGIAN = [261.63, 277.18, 311.13, 349.23, 392.00, 415.30, 466.16]
    LYDIAN = [261.63, 293.66, 329.63, 370.00, 392.00, 440.00, 493.88]
    MIXOLYDIAN = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 466.16]
    AEOLIAN = NATURAL_MINOR
    LOCRIAN = [261.63, 277.18, 311.13, 349.23, 369.99, 415.30, 466.16]

    # Exotic scales
    WHOLE_TONE = [261.63, 293.66, 329.63, 370.00, 415.30, 466.16]
    HALF_WHOLE_DIM = [261.63, 277.18, 311.13, 329.63, 349.23, 370.00, 392.00, 415.30]
    WHOLE_HALF_DIM = [261.63, 293.66, 311.13, 349.23, 370.00, 392.00, 415.30, 466.16]
    BEBOP_DOMINANT = [261.63, 293.66, 329.63, 349.23, 392.00, 415.30, 440.00, 466.16]
    BEBOP_MAJOR = [261.63, 293.66, 329.63, 349.23, 369.99, 392.00, 440.00, 493.88]
    HARMONIC_MAJOR = [261.63, 293.66, 329.63, 349.23, 392.00, 415.30, 493.88]
    HUNGARIAN_MINOR = [261.63, 293.66, 311.13, 370.00, 392.00, 415.30, 493.88]

    # Note names corresponding to each scale
    MAJOR_NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    MINOR_NOTES = ['C', 'D♭', 'E♭', 'F', 'G', 'A♭', 'B♭']
    PENTATONIC_NOTES = ['C', 'D', 'E', 'G', 'A']
    CHROMATIC_NOTES = ['C', 'D♭', 'D', 'E♭', 'E', 'F', 'F#', 'G', 'A♭', 'A', 'B♭', 'B']

    # Additional note names
    NATURAL_MINOR_NOTES = ['C', 'D', 'E♭', 'F', 'G', 'A♭', 'B♭']
    HARMONIC_MINOR_NOTES = ['C', 'D', 'E♭', 'F', 'G', 'A♭', 'B']
    MELODIC_MINOR_NOTES = ['C', 'D', 'E♭', 'F', 'G', 'A', 'B']
    MAJOR_PENTATONIC_NOTES = ['C', 'D', 'E', 'G', 'A']
    MINOR_PENTATONIC_NOTES = ['C', 'E♭', 'F', 'G', 'B♭']
    BLUES_NOTES = ['C', 'E♭', 'F', 'F#', 'G', 'B♭']

    IONIAN_NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    DORIAN_NOTES = ['C', 'D', 'E♭', 'F', 'G', 'A', 'B♭']
    PHRYGIAN_NOTES = ['C', 'D♭', 'E♭', 'F', 'G', 'A♭', 'B♭']
    LYDIAN_NOTES = ['C', 'D', 'E', 'F#', 'G', 'A', 'B']
    MIXOLYDIAN_NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B♭']
    AEOLIAN_NOTES = ['C', 'D', 'E♭', 'F', 'G', 'A♭', 'B♭']
    LOCRIAN_NOTES = ['C', 'D♭', 'E♭', 'F', 'G♭', 'A♭', 'B♭']

    WHOLE_TONE_NOTES = ['C', 'D', 'E', 'F#', 'G#', 'A#']
    HALF_WHOLE_DIMINISHED_NOTES = ['C', 'D♭', 'E♭', 'E', 'F#', 'G', 'A', 'B♭']
    WHOLE_HALF_DIMINISHED_NOTES = ['C', 'D', 'E♭', 'F', 'F#', 'G#', 'A', 'B']
    BEBOP_DOMINANT_NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B♭', 'B']
    BEBOP_MAJOR_NOTES = ['C', 'D', 'E', 'F', 'G', 'G#', 'A', 'B']
    HARMONIC_MAJOR_NOTES = ['C', 'D', 'E', 'F', 'G', 'A♭', 'B']
    HUNGARIAN_MINOR_NOTES = ['C', 'D', 'E♭', 'F#', 'G', 'A♭', 'B']

    def __init__(self, game: GameOfLife):
        """
        Initialize the music generator.

        Args:
            game: GameOfLife instance to generate music from
        """
        self.game = game

        # Build scales and note names dictionaries
        self.scales = {
            'major': self.MAJOR_SCALE,
            'minor': self.MINOR_SCALE,
            'pentatonic': self.PENTATONIC,
            'chromatic': self.CHROMATIC,
            'natural_minor': self.NATURAL_MINOR,
            'harmonic_minor': self.HARMONIC_MINOR,
            'melodic_minor': self.MELODIC_MINOR,
            'major_pentatonic': self.MAJOR_PENTATONIC,
            'minor_pentatonic': self.MINOR_PENTATONIC,
            'blues': self.BLUES_SCALE,
            'ionian': self.IONIAN,
            'dorian': self.DORIAN,
            'phrygian': self.PHRYGIAN,
            'lydian': self.LYDIAN,
            'mixolydian': self.MIXOLYDIAN,
            'aeolian': self.AEOLIAN,
            'locrian': self.LOCRIAN,
            'whole_tone': self.WHOLE_TONE,
            'half_whole_diminished': self.HALF_WHOLE_DIM,
            'whole_half_diminished': self.WHOLE_HALF_DIM,
            'bebop_dominant': self.BEBOP_DOMINANT,
            'bebop_major': self.BEBOP_MAJOR,
            'harmonic_major': self.HARMONIC_MAJOR,
            'hungarian_minor': self.HUNGARIAN_MINOR
        }

        self.note_names = {
            'major': self.MAJOR_NOTES,
            'minor': self.MINOR_NOTES,
            'pentatonic': self.PENTATONIC_NOTES,
            'chromatic': self.CHROMATIC_NOTES,
            'natural_minor': self.NATURAL_MINOR_NOTES,
            'harmonic_minor': self.HARMONIC_MINOR_NOTES,
            'melodic_minor': self.MELODIC_MINOR_NOTES,
            'major_pentatonic': self.MAJOR_PENTATONIC_NOTES,
            'minor_pentatonic': self.MINOR_PENTATONIC_NOTES,
            'blues': self.BLUES_NOTES,
            'ionian': self.IONIAN_NOTES,
            'dorian': self.DORIAN_NOTES,
            'phrygian': self.PHRYGIAN_NOTES,
            'lydian': self.LYDIAN_NOTES,
            'mixolydian': self.MIXOLYDIAN_NOTES,
            'aeolian': self.AEOLIAN_NOTES,
            'locrian': self.LOCRIAN_NOTES,
            'whole_tone': self.WHOLE_TONE_NOTES,
            'half_whole_diminished': self.HALF_WHOLE_DIMINISHED_NOTES,
            'whole_half_diminished': self.WHOLE_HALF_DIMINISHED_NOTES,
            'bebop_dominant': self.BEBOP_DOMINANT_NOTES,
            'bebop_major': self.BEBOP_MAJOR_NOTES,
            'harmonic_major': self.HARMONIC_MAJOR_NOTES,
            'hungarian_minor': self.HUNGARIAN_MINOR_NOTES
        }

        self.current_scale = 'major'
        self.octave_range = 3
        self.base_octave = 3

        # Initialize pygame mixer
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

        # Musical parameters
        self.note_duration = 0.3
        self.max_volume = 0.25
        self.volume_decay = 0.95

        # Active sounds tracking
        self.active_sounds = []

        # Cell note mapping for display
        self.cell_notes = {}

        # Track cell ages for newborn detection
        self.previous_living_cells = set()

        # Track which cells are currently playing notes (for white coloring)
        self.playing_notes = set()  # Set of (x, y) coordinates

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
        """Map cell position to musical frequency."""
        if scale is None:
            scale = self.current_scale

        position = (x + y) % len(self.scales[scale])
        base_frequency = self.scales[scale][position]

        octave_offset = ((x * 7 + y * 11) % (self.octave_range * 2)) - self.octave_range
        frequency = base_frequency * (2 ** octave_offset)

        return frequency

    def _get_note_name(self, x: int, y: int, scale: str = None) -> str:
        """Get the note name for a cell at position (x, y)."""
        if scale is None:
            scale = self.current_scale

        position = (x + y) % len(self.scales[scale])
        base_note = self.note_names[scale][position]

        octave_offset = ((x * 7 + y * 11) % (self.octave_range * 2)) - self.octave_range
        octave_number = self.base_octave + octave_offset

        return f"{base_note}{octave_number}"

    def _find_newborn_cells(self) -> List[Tuple[int, int]]:
        """Find cells that were just born this generation."""
        current_living_cells = set(self.game.get_living_cells())
        newborn_cells = current_living_cells - self.previous_living_cells
        self.previous_living_cells = current_living_cells
        return list(newborn_cells)

    def _thin_notes_by_row(self, cells: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """
        Return only the lowest frequency (highest X coordinate) newborn cell per row.
        This reduces audio clutter while maintaining musical interest.
        """
        if not cells:
            return []

        # Group cells by row (Y coordinate)
        rows = {}
        for x, y in cells:
            if y not in rows:
                rows[y] = []
            rows[y].append((x, y))

        # For each row, find the cell that would produce the lowest frequency
        # Lower frequency = higher Y + higher X (based on the frequency calculation)
        thinned_cells = []
        for y, row_cells in rows.items():
            if row_cells:
                # Sort by X coordinate (descending) to get lowest frequency first
                # The frequency calculation uses (x + y), so higher x = lower relative freq
                lowest_freq_cell = max(row_cells, key=lambda cell: cell[0])
                thinned_cells.append(lowest_freq_cell)

        return thinned_cells

    def _update_cell_notes(self) -> None:
        """Update the mapping of cells to their note names."""
        self.cell_notes.clear()
        living_cells = self.game.get_living_cells()

        for x, y in living_cells:
            note_name = self._get_note_name(x, y)
            self.cell_notes[(x, y)] = note_name

    def _generate_position_based_music(self) -> None:
        """Generate music based on cell positions with automatic note thinning."""
        # Clear previous playing notes
        self.playing_notes.clear()

        # Find newborn cells
        newborn_cells = self._find_newborn_cells()

        # Apply automatic thinning - only lowest note per row for newborns
        thinned_cells = self._thin_notes_by_row(newborn_cells)

        # Play thinned newborn notes and mark them as playing
        for x, y in thinned_cells:
            frequency = self._get_note_frequency(x, y)
            volume = self.max_volume

            sound = self._generate_tone(frequency, self.note_duration, volume)
            channel = sound.play()

            if channel:
                self.active_sounds.append(channel)
                # Mark this cell as currently playing a note (for white coloring)
                self.playing_notes.add((x, y))

    def _generate_density_based_music(self) -> None:
        """Generate music based on cell density patterns (keeps density-based scale changes)."""
        # Clear previous playing notes
        self.playing_notes.clear()

        density = self.game.get_cell_density()

        if density > 0:
            # Map density ranges to scale families (PRESERVED FROM ORIGINAL)
            if density < 0.005:
                chosen_scale = 'major_pentatonic'
            elif density < 0.01:
                chosen_scale = 'major'
            elif density < 0.05:
                chosen_scale = 'mixolydian'
            elif density < 0.1:
                chosen_scale = 'dorian'
            elif density < 0.15:
                chosen_scale = 'minor'
            elif density < 0.25:
                chosen_scale = 'blues'
            else:
                chosen_scale = 'chromatic'

            # Update current scale automatically
            self.current_scale = chosen_scale

            # Apply thinning to density-based notes too
            newborn_cells = self._find_newborn_cells()
            thinned_cells = self._thin_notes_by_row(newborn_cells)

            for x, y in thinned_cells:
                frequency = self._get_note_frequency(x, y, chosen_scale)
                volume = self.max_volume * (0.5 + density * 0.5)

                sound = self._generate_tone(frequency, self.note_duration, volume)
                channel = sound.play()

                if channel:
                    self.active_sounds.append(channel)
                    # Mark this cell as currently playing a note (for white coloring)
                    self.playing_notes.add((x, y))

    def _generate_pattern_based_music(self) -> None:
        """Generate music based on specific cell patterns."""
        # Clear previous playing notes
        self.playing_notes.clear()

        patterns = self._analyze_patterns()

        for pattern_type, positions in patterns.items():
            if positions:
                base_freq = {
                    'clusters': 300,
                    'lines': 400,
                    'isolated': 500,
                    'edges': 600
                }.get(pattern_type, 350)

                # Apply thinning to pattern-based notes as well
                newborn_positions = [pos for pos in positions if pos in self._find_newborn_cells()]
                thinned_positions = self._thin_notes_by_row(newborn_positions)

                for x, y in thinned_positions:
                    frequency = base_freq + (x + y) * 10
                    volume = self.max_volume * 0.6

                    sound = self._generate_tone(frequency, self.note_duration, volume)
                    channel = sound.play()

                    if channel:
                        self.active_sounds.append(channel)
                        # Mark this cell as currently playing a note (for white coloring)
                        self.playing_notes.add((x, y))

    def _generate_harmonic_music(self) -> None:
        """Generate harmonic music based on population dynamics."""
        # Clear previous playing notes (harmonic mode doesn't use visual feedback)
        self.playing_notes.clear()

        population_change = self.game.get_population_change()

        if abs(population_change) > 0:
            if population_change > 0:
                progression = [0, 2, 4, 6]
            else:
                progression = [6, 4, 2, 0]

            for note_index in progression:
                if note_index < len(self.scales[self.current_scale]):
                    frequency = self.scales[self.current_scale][note_index] * (2 ** self.base_octave)
                    volume = self.max_volume * 0.4

                    sound = self._generate_tone(frequency, self.note_duration * 1.5, volume)
                    channel = sound.play()

                    if channel:
                        self.active_sounds.append(channel)
                        # Note: Harmonic mode doesn't highlight specific cells since it's not position-based

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

            if neighbors >= 4:
                patterns['clusters'].append((x, y))
            elif neighbors <= 1:
                patterns['isolated'].append((x, y))
            elif neighbors == 2:
                if self._is_part_of_line(x, y):
                    patterns['lines'].append((x, y))

            if x == 0 or x == self.game.width - 1 or y == 0 or y == self.game.height - 1:
                patterns['edges'].append((x, y))

        return patterns

    def _is_part_of_line(self, x: int, y: int) -> bool:
        """Check if a cell is part of a linear pattern."""
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
            dx1, dy1 = neighbors[0]
            dx2, dy2 = neighbors[1]
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

    def is_cell_playing_note(self, x: int, y: int) -> bool:
        """
        Check if a specific cell is currently playing a note.
        Used by the visualizer to color playing cells white.

        Args:
            x: X coordinate of the cell
            y: Y coordinate of the cell

        Returns:
            True if the cell is currently playing a note, False otherwise
        """
        return (x, y) in self.playing_notes

    def get_cell_note(self, x: int, y: int) -> Optional[str]:
        """Get the note name for a specific cell position."""
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
