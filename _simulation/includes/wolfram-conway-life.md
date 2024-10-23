\ifndef{wolframConwayLife}
\define{wolframConwayLife}

\editme

\setuphelpercode{import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple}

\helpercode{class FlowingAutomata:
    def __init__(self, width: int, height: int, wolfram_portion: float = 0.5):
        """
        Initialize flowing display where Wolfram patterns flow into Conway's Game of Life

        Inspired by Elliot Waite <https://www.youtube.com/watch?v=IK7nBOLYzdE>
        Args:
            width: Total width of the display in pixels
            height: Height of the display in pixels
            wolfram_portion: Portion of width for Wolfram's automaton (0-1)
        """
        self.width = width
        self.height = height
        self.wolfram_portion = wolfram_portion
        
        # Calculate section widths
        self.wolfram_width = int(width * wolfram_portion)
        self.conway_width = width - self.wolfram_width
        
        # Initialize the full grid
        self.grid = np.zeros((height, width), dtype=int)
        
        # Initialize generation counter
        self.generation = 0
        
        # Store current Wolfram column for the next generation
        self.current_wolfram_column = np.zeros(height, dtype=int)
        self.current_wolfram_column[height // 2] = 1  # Start with middle cell active
        
    def _get_rule_mapping(self, rule_number: int) -> dict:
        """
        Convert Wolfram rule number to rule dictionary
        """
        if not 0 <= rule_number <= 255:
            raise ValueError("Rule number must be between 0 and 255")
        
        rule_binary = format(rule_number, '08b')
        neighborhoods = [
            (1,1,1), (1,1,0), (1,0,1), (1,0,0),
            (0,1,1), (0,1,0), (0,0,1), (0,0,0)
        ]
        return {n: int(rule_binary[i]) for i, n in enumerate(neighborhoods)}
    
    def _calculate_next_wolfram_column(self, rule_number: int) -> np.ndarray:
        """Calculate the next Wolfram column based on current column"""
        rule = self._get_rule_mapping(rule_number)
        next_column = np.zeros_like(self.current_wolfram_column)
        
        for i in range(self.height):
            left = self.current_wolfram_column[(i-1) % self.height]
            center = self.current_wolfram_column[i]
            right = self.current_wolfram_column[(i+1) % self.height]
            next_column[i] = rule[(left, center, right)]
            
        return next_column
    
    def _count_conway_neighbors(self, x: int, y: int) -> int:
        """
        Count live neighbors for Conway's Game of Life
        """
        total = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                ny = (y + dy) % self.height
                nx = x + dx
                
                # For any position, including looking back into Wolfram section
                actual_x = self.wolfram_width + nx
                if nx < 0:
                    actual_x = self.wolfram_width + nx  # Will look into Wolfram section
                elif nx >= self.conway_width:
                    actual_x = self.wolfram_width + (nx % self.conway_width)
                
                total += self.grid[ny, actual_x]
        return total
    
    def _update_conway(self):
        """Update Conway's Game of Life portion"""
        new_conway = np.zeros((self.height, self.conway_width), dtype=int)
        
        # Update all Conway cells based on rules, allowing them to read the Wolfram section
        for y in range(self.height):
            for x in range(self.conway_width):
                neighbors = self._count_conway_neighbors(x, y)
                current_state = self.grid[y, self.wolfram_width + x]
                
                if current_state == 1:
                    if neighbors in [2, 3]:
                        new_conway[y, x] = 1
                else:
                    if neighbors == 3:
                        new_conway[y, x] = 1
        
        # Update Conway portion of the grid
        self.grid[:, self.wolfram_width:] = new_conway
    
    def step(self, rule_number: int):
        """Advance the system one generation"""
        # Shift Wolfram portion one step right
        self.grid[:, 1:self.wolfram_width] = self.grid[:, :self.wolfram_width-1]
        
        # Calculate and set new Wolfram column
        self.current_wolfram_column = self._calculate_next_wolfram_column(rule_number)
        self.grid[:, 0] = self.current_wolfram_column
        
        # Update Conway's Game of Life portion
        self._update_conway()
        
        self.generation += 1
    
    def plot(self, figsize: Tuple[int, int] = (12, 8)):
        """Display current state"""
        plt.figure(figsize=figsize)
        plt.imshow(self.grid, cmap='binary')
        
        # Add dividing line
        plt.axvline(x=self.wolfram_width-0.5, color='red', linestyle='--', alpha=0.5)
        
        # Add titles
        plt.text(self.wolfram_width/2, -5, "Wolfram Automaton",
                horizontalalignment='center')
        plt.text(self.wolfram_width + self.conway_width/2, -5, "Game of Life",
                horizontalalignment='center')
        
        plt.title(f'Generation {self.generation}')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def save_svg(self, filename: str, cell_size: int = 10):
        """Save current state as SVG"""
        width = self.width * cell_size
        height = self.height * cell_size
        
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
        <style>
            .cell {{ fill: black; }}
            .divider {{ stroke: red; stroke-dasharray: 5,5; }}
            .title {{ font: bold 14px sans-serif; }}
        </style>
        '''
        
        # Draw cells
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y, x]:
                    svg += f'<rect class="cell" x="{x * cell_size}" y="{y * cell_size}" width="{cell_size}" height="{cell_size}"/>'
        
        # Draw dividing line
        divider_x = self.wolfram_width * cell_size
        svg += f'<line class="divider" x1="{divider_x}" y1="0" x2="{divider_x}" y2="{height}"/>'
        
        svg += '</svg>'
        
        with open(filename, 'w') as f:
            f.write(svg)}
\helpercode{def run_flowing_demonstration(width: int = 100, height: int = 50,
                           wolfram_portion: float = 0.3,
                           wolfram_rule: int = 30,
                           generations: int = 100,
                           save_interval: int = 10):
    """
	Run a demonstration of the flowing automata
	"""
    
    # Initialize system
    automata = FlowingAutomata(width, height, wolfram_portion)
    
    # Run simulation
    automata.plot()  # Show initial state
    
    for gen in range(generations):
        automata.step(wolfram_rule)
        if gen % save_interval == 0:
            automata.plot()
            automata.save_svg(f"flowing-automata-gen-{gen:0>{3}}.svg")
}

\code{run_flowing_demonstration(
    width=100,
    height=50,
    wolfram_portion=0.1,
    wolfram_rule=30,
    generations=100,
    save_interval=1
)}



\endif
