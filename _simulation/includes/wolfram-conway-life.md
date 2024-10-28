\ifndef{wolframConwayLife}
\define{wolframConwayLife}

include{_simulation/includes/automata-base.md}
\include{_simulation/includes/wolfram-automata.md}
\include{_simulation/includes/game-of-life.md}

\editme

\subsection{Combining Wolfram and Conway}

\notes{We can create an interesting hybrid system by combining Wolfram's elementary cellular automata with Conway's Game of Life. The system consists of a square grid where the interior follows Conway's rules, but the border cells evolve according to a chosen Wolfram rule. The Wolfram rule wraps around the border, creating a dynamic boundary condition for the Life cells.}

\setuphelpercode{from typing import Tuple, Optional, Set
import numpy as np}

\helpercode{class HybridAutomaton:
    """Combined Wolfram-Conway automaton system
    
    A square grid where:
    - Interior follows Conway's Game of Life rules
    - Border follows a specified Wolfram rule
    - Border wraps around (Wolfram rule connects at corners)
    """
    def __init__(self, size: int, wolfram_rule: int):
        """
        Args:
            size: Size of the square grid
            wolfram_rule: Which Wolfram rule to use for borders (0-255)
        """
        self.size = size
        self.wolfram_rule = wolfram_rule
        self.grid = Grid(size, size)
        self.rule_mapping = get_rule_mapping(wolfram_rule)
        
    def get_border_cells(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Get the four borders as 1D arrays (for Wolfram rules)
        Returns borders in order: top, right, bottom, left
        """
        return (
            self.grid.grid[0, :],          # Top border
            self.grid.grid[:, -1],         # Right border
            self.grid.grid[-1, ::-1],      # Bottom border (reversed)
            self.grid.grid[::-1, 0]        # Left border (reversed)
        )
        
    def set_border_cells(self, top: np.ndarray, right: np.ndarray, 
                        bottom: np.ndarray, left: np.ndarray):
        """Set the border cells from 1D arrays"""
        self.grid.grid[0, :] = top
        self.grid.grid[:, -1] = right
        self.grid.grid[-1, :] = bottom[::-1]  # Reverse to maintain correct order
        self.grid.grid[:, 0] = left[::-1]
        
	def evolve_borders(self):
		"""Evolve the border cells using a single Wolfram rule

		The border is treated as a single 1D array that wraps around
		the entire perimeter of the grid, with the rule applying 
		continuously around corners.
		"""
		# Get current borders and join them into a single perimeter
		# Going clockwise: top -> right -> bottom -> left
		top, right, bottom, left = self.get_border_cells()
		# Note: bottom and left are already reversed in get_border_cells
		perimeter = np.concatenate([top, right, bottom, left])

		# Evolve the entire perimeter as one continuous 1D array
		new_perimeter = np.zeros_like(perimeter)
		# Include wrap-around for the full perimeter
		extended = np.hstack([perimeter[-1:], perimeter, perimeter[:1]])
		for i in range(len(perimeter)):
			neighborhood = (extended[i], extended[i+1], extended[i+2])
			new_perimeter[i] = self.rule_mapping[neighborhood]

		# Split the evolved perimeter back into borders
		size = self.size
		new_top = new_perimeter[:size]
		new_right = new_perimeter[size:2*size]
		new_bottom = new_perimeter[2*size:3*size][::-1]  # Reverse for bottom
		new_left = new_perimeter[3*size:][::-1]          # Reverse for left

		# Update borders
		self.set_border_cells(new_top, new_right, new_bottom, new_left)

	def evolve_interior(self):
        """Evolve interior cells using Conway's rules"""
        new_grid = Grid(self.size, self.size)
        # Copy borders to new grid
        top, right, bottom, left = self.get_border_cells()
        new_grid.grid[0, :] = top
        new_grid.grid[:, -1] = right
        new_grid.grid[-1, :] = bottom[::-1]
        new_grid.grid[:, 0] = left[::-1]
        
        # Evolve interior cells
        for y in range(1, self.size-1):
            for x in range(1, self.size-1):
                neighbors = count_life_neighbors(self.grid, x, y, boundary='fixed')
                if self.grid[x, y]:
                    new_grid[x, y] = 1 if neighbors in [2, 3] else 0
                else:
                    new_grid[x, y] = 1 if neighbors == 3 else 0
                    
        self.grid = new_grid
        
    def step(self):
        """Perform one step of hybrid evolution"""
        self.evolve_borders()
        self.evolve_interior()
        
    def run(self, steps: int) -> List[Grid]:
        """Run simulation for specified number of steps
        
        Returns:
            List of Grid instances representing evolution history
        """
        history = [self.grid.copy()]
        for _ in range(steps):
            self.step()
            history.append(self.grid.copy())
        return history}

\setupcode{import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation}

\helpercode{def create_hybrid_animation(size: int = 30,
                             wolfram_rule: int = 30,
                             steps: int = 50,
                             interval: int = 200,
                             initial_pattern: Optional[LifePattern] = None):
    """Create animation of hybrid Wolfram-Conway system
    
    Args:
        size: Grid size
        wolfram_rule: Wolfram rule number for borders
        steps: Number of steps to simulate
        interval: Animation interval in milliseconds
        initial_pattern: Optional LifePattern to initialize interior
    """
    # Initialize system
    hybrid = HybridAutomaton(size, wolfram_rule)
    
    # Set initial pattern if provided
    if initial_pattern:
        pattern_grid = initial_pattern.to_grid(size-2)  # Smaller to fit interior
        hybrid.grid.grid[1:-1, 1:-1] = pattern_grid.grid
    
    # Run simulation
    history = hybrid.run(steps)
    
    # Create animation
    fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
    fig.set_facecolor('white')
    
    plot_automata_grid(history[0], ax)
    
    def animate(frame):
        ax.clear()
        plot_automata_grid(history[frame], ax)
        ax.set_title(f"Hybrid Evolution - Step {frame}")
        return ax,
    
    anim = FuncAnimation(
        fig, animate,
        frames=len(history),
        interval=interval,
        blit=True
    )
    
    # Save animation
    filename = f'hybrid-r{wolfram_rule}'
    if initial_pattern:
        filename += f'-{initial_pattern.name.lower()}'
    anim.save(mlai.filename_join(f'{filename}.gif',
                                '\writeDiagramsDir/simulation'),
              writer='pillow')
    return history}

\notes{Let's demonstrate this hybrid system with some examples. First, let's see how Rule 30 interacts with a glider:}

\plotcode{# Create hybrid system with Rule 30 and a glider
create_hybrid_animation(
    size=30,
    wolfram_rule=30,
    steps=50,
    initial_pattern=GLIDER
)}

\figure{\includegif{\diagramsDir/simulation/hybrid-r30-glider}{80%}}{A glider pattern evolving within borders governed by Rule 30. Notice how the complex border patterns influence the glider's behavior.}{hybrid-r30-glider}

\notes{Now let's try a different combination - Rule 110 (another complex rule) with a loafer:}

\plotcode{# Create hybrid system with Rule 110 and a loafer
create_hybrid_animation(
    size=30,
    wolfram_rule=110,
    steps=50,
    initial_pattern=LOAFER
)}

\figure{\includegif{\diagramsDir/simulation/hybrid-r110-loafer}{80%}}{A loafer pattern evolving within borders governed by Rule 110. The border patterns create a dynamic environment that affects the loafer's movement.}{hybrid-r110-loafer}

\notes{This hybrid system demonstrates how two different types of cellular automata can be combined to create new behaviours.}

\endif
