\ifndef{automataBase}
\define{automataBase}

\editme

\subsection{Cellular Automata}

\notes{Cellular automata are systems of cells that evolve according to fixed rules. The rules depend on the current state of cells and their neighbors. We'll explore both one-dimensional (Wolfram) and two-dimensional (Conway) cellular automata. First, we'll set up some base functionality that both types share.}

\setuphelpercode{import numpy as np
from typing import Union, Tuple, Optional}

\helpercode{class Grid:
    """Base class for cellular automaton grids
    
    Handles common grid operations and visualization
    """
    def __init__(self, width: int, height: Optional[int] = None):
        """
        Args:
            width: Width of grid
            height: Height of grid. If None, creates 1D grid
        """
        self.width = width
        self.height = height if height is not None else 1
        self.grid = np.zeros((self.height, self.width), dtype=int)
        
    def __getitem__(self, key: Union[int, Tuple[int, int]]) -> int:
        """Get cell state"""
        if isinstance(key, tuple):
            return self.grid[key[1], key[0]]
        return self.grid[0, key]
        
    def __setitem__(self, key: Union[int, Tuple[int, int]], value: int):
        """Set cell state"""
        if isinstance(key, tuple):
            self.grid[key[1], key[0]] = value
        else:
            self.grid[0, key] = value
            
    def copy(self) -> 'Grid':
        """Create a deep copy of the grid"""
        new_grid = Grid(self.width, self.height)
        new_grid.grid = self.grid.copy()
        return new_grid}

\helpercode{def generate_grid_svg(grid: Union[Grid, np.ndarray], 
                        cell_size: int = 30,
                        highlight_cells: Optional[set] = None) -> str:
    """Generate SVG visualization of a grid
    
    Args:
        grid: Grid to visualize
        cell_size: Size of each cell in pixels
        highlight_cells: Optional set of (x,y) coordinates to highlight
        
    Returns:
        SVG string representing the grid
    """
    if isinstance(grid, Grid):
        array = grid.grid
    else:
        array = grid
        
    height, width = array.shape
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
                  viewBox="-1.5 -1.5 {width*cell_size + 3} {height*cell_size + 3}"
                  width="{width*cell_size + 3}"
                  height="{height*cell_size + 3}">
        <style>
            .cell {{ fill: black; }}
            .highlight {{ stroke: red; stroke-width: 3; }}
            .grid {{ stroke: #c0c0c0; stroke-width: 3; }}
        </style>
        <rect width="100%" height="100%" fill="white"/>
    '''
    
    # Draw grid lines
    for i in range(width + 1):
        svg += f'<line class="grid" x1="{i*cell_size}" y1="0" '
        svg += f'x2="{i*cell_size}" y2="{height*cell_size}"/>'
    for i in range(height + 1):
        svg += f'<line class="grid" x1="0" y1="{i*cell_size}" '
        svg += f'x2="{width*cell_size}" y2="{i*cell_size}"/>'
        
    # Draw cells
    for y in range(height):
        for x in range(width):
            if array[y, x]:
                svg += f'<rect class="cell" x="{x*cell_size}" y="{y*cell_size}" '
                svg += f'width="{cell_size}" height="{cell_size}"'
                if highlight_cells and (x,y) in highlight_cells:
                    svg += ' class="highlight"'
                svg += '/>'
                
    svg += '</svg>'
    return svg}

\notes{These base classes and functions provide:
1. A flexible grid structure that works for both 1D and 2D automata
2. Consistent array access patterns
3. Grid visualization tools
4. Support for highlighting interesting cells or patterns

We'll build on this foundation to implement both Wolfram's elementary one dimensional cellular automata and later Conway's two dimensional Game of Life.}

\endif
