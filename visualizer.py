"""
Pygame visualization for Conway's Game of Life with musical integration and note display.
"""

import pygame
import sys
from typing import Tuple, Optional
from game_of_life import GameOfLife
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

    def _draw_ui(self) -> None:
        """Draw the user interface."""
        ui_y = self.height * self.cell_size + 10  # Increased margin

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
