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
