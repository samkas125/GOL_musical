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
