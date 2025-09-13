
"""
Pygame visualization for Conway's Game of Life with musical integration and note display.
Now with white highlighting for cells that are currently playing notes.
"""

import pygame
import sys
from typing import Tuple, Optional
from game_of_life import GameOfLife, RuleSet
from music_generator import MusicGenerator


class GameVisualizer:
    """Handles the visual display and user interaction for the Game of Life with note display and visual feedback."""

    def __init__(self, width: int = 50, height: int = 50, cell_size: int = 20):
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
        self.screen_height = height * cell_size + 120  # Extra space for UI

        # Colors
        self.colors = {
            'background': (20, 20, 20),
            'grid_lines': (40, 40, 40),
            'dead_cell': (30, 30, 30),
            'living_cell': (255, 255, 100),  # Yellow for musical cells
            'playing_note': (255, 255, 255),  # WHITE for cells currently playing notes
            'new_cell': (255, 255, 150),
            'dying_cell': (255, 100, 100),
            'text': (255, 255, 255),
            'note_text': (0, 0, 0),  # Black text for notes on colored cells
            'playing_note_text': (0, 0, 0),  # Black text for notes on white cells
            'ui_bg': (40, 40, 40),
            'ui_border': (80, 80, 80)
        }

        # Color palettes by scale (warm vs cool)
        self.scale_colors = {
            # Happy/Bright scales → warmer colors
            'major': (255, 215, 0),            # gold
            'ionian': (255, 200, 50),
            'lydian': (255, 165, 0),           # orange
            'mixolydian': (255, 140, 0),

            # Sad/Dark scales → cooler colors
            'minor': (100, 149, 237),          # cornflower blue
            'natural_minor': (70, 130, 180),   # steel blue
            'harmonic_minor': (65, 105, 225),  # royal blue
            'melodic_minor': (72, 61, 139),    # dark slate blue
            'aeolian': (95, 158, 160),         # cadet blue
            'dorian': (123, 104, 238),         # medium slate blue
            'phrygian': (106, 90, 205),        # slate blue
            'locrian': (25, 25, 112),          # midnight blue

            # Exotic/neutral → mix of vibrant colors
            'pentatonic': (60, 179, 113),      # medium sea green
            'major_pentatonic': (50, 205, 50), # lime green
            'minor_pentatonic': (46, 139, 87), # sea green
            'blues': (30, 144, 255),           # dodger blue

            'chromatic': (220, 20, 60),        # crimson
            'whole_tone': (255, 99, 71),       # tomato
            'half_whole_diminished': (186, 85, 211),  # orchid
            'whole_half_diminished': (138, 43, 226),  # blue violet
            'bebop_dominant': (199, 21, 133),  # medium violet red
            'bebop_major': (255, 105, 180),    # hot pink
            'harmonic_major': (255, 69, 0),    # red-orange
            'hungarian_minor': (148, 0, 211)   # dark violet
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
        
        # Scale cycling
        self.available_scales = [
            'major', 'minor', 'pentatonic', 'chromatic',
            'natural_minor', 'harmonic_minor', 'melodic_minor',
            'major_pentatonic', 'minor_pentatonic', 'blues',
            'ionian', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'aeolian', 'locrian',
            'whole_tone', 'half_whole_diminished', 'whole_half_diminished',
            'bebop_dominant', 'bebop_major', 'harmonic_major', 'hungarian_minor'
        ]
        self.current_scale_index = 0

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

        elif event.key == pygame.K_g:
            self.show_grid = not self.show_grid

        elif event.key == pygame.K_n:  # Toggle note display
            self.show_notes = not self.show_notes

        # Scale cycling with S key
        elif event.key == pygame.K_s:
            self._cycle_scale()

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

        # Pattern cycling with P key (changed from P to X to avoid conflict)
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
                    # Check if this cell is currently playing a note
                    is_playing = self.music_gen.is_cell_playing_note(x, y) if self.music_enabled else False

                    if is_playing:
                        # WHITE for cells currently playing notes
                        color = self.colors['playing_note']
                        text_color = self.colors['playing_note_text']
                    else:
                        # Scale-based color for other living cells
                        current_scale = self.music_gen.current_scale
                        color = self.scale_colors.get(current_scale, self.colors['living_cell'])
                        text_color = self.colors['note_text']

                    pygame.draw.rect(self.screen, color, rect)

                    # Draw inner rectangle for better visibility
                    inner_rect = pygame.Rect(x * self.cell_size + 1, y * self.cell_size + 1,
                                           self.cell_size - 2, self.cell_size - 2)
                    pygame.draw.rect(self.screen, color, inner_rect)

                    # Draw note name on top of the cell if enabled and available
                    if self.show_notes and self.music_enabled:
                        note_name = self.music_gen.get_cell_note(x, y)
                        if note_name:
                            self._draw_note_on_cell(x, y, note_name, text_color)

                else:
                    # Dead cell
                    pygame.draw.rect(self.screen, self.colors['dead_cell'], rect)

        # Draw UI
        self._draw_ui()

        pygame.display.flip()

    def _draw_note_on_cell(self, x: int, y: int, note_name: str, text_color: Tuple[int, int, int]) -> None:
        """Draw a note name on top of a cell with specified text color."""
        # Create text surface
        text_surface = self.note_font.render(note_name, True, text_color)
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

    def _cycle_scale(self) -> None:
        """Cycle through available musical scales."""
        self.current_scale_index = (self.current_scale_index + 1) % len(self.available_scales)
        scale = self.available_scales[self.current_scale_index]
        self.music_gen.set_scale(scale)
        print(f"Switched to scale: {scale}")

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
            "SPACE: Pause/Play | R: Reset | M: Music On/Off | N: Notes On/Off",
            "S: Cycle Scales | Q/W/E/T: Mode (Position/Density/Pattern/Harmonic)",
            "F1-F8: Rule Sets | TAB: Cycle Rules | P: Cycle Patterns",
            "G: Grid | +/-: Speed | Up/Down: Volume | WHITE CELLS = Playing Notes",
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
