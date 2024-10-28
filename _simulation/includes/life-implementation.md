\ifndef{lifeImplementation}
\define{lifeImplementation}

\include{_simulation/includes/automata-base.md}

\editme

\subsection{Game of Life Implementation}

\notes{Now that we understand the rules of Life, let's implement them. Each cell's fate is determined by counting its eight neighbors and applying Conway's rules.}

\setuphelpercode{from typing import Optional, Set}

\helpercode{def count_life_neighbors(grid: Grid, x: int, y: int, boundary: str = 'periodic') -> int:
    """Count live neighbors for a cell in Game of Life
    
    Args:
        grid: Grid instance representing current state
        x, y: Cell coordinates
        boundary: Type of boundary conditions ('periodic' or 'fixed')
        
    Returns:
        Number of live neighbors (0-8)
    """
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
                
            if boundary == 'periodic':
                nx = (x + dx) % grid.width
                ny = (y + dy) % grid.height
                count += grid[nx, ny]
            else:  # fixed
                nx = x + dx
                ny = y + dy
                if 0 <= nx < grid.width and 0 <= ny < grid.height:
                    count += grid[nx, ny]
    return count}

\helpercode{def evolve_life(grid: Grid, boundary: str = 'periodic') -> Grid:
    """Evolve one step of Conway's Game of Life
    
    Args:
        grid: Grid instance representing current state
        boundary: Type of boundary conditions ('periodic' or 'fixed')
        
    Returns:
        New Grid instance representing next state
    """
    new_grid = Grid(grid.width, grid.height)
    
    for y in range(grid.height):
        for x in range(grid.width):
            neighbors = count_life_neighbors(grid, x, y, boundary)
            # Apply Conway's rules
            if grid[x, y]:  # Live cell
                new_grid[x, y] = 1 if neighbors in [2, 3] else 0
            else:  # Dead cell
                new_grid[x, y] = 1 if neighbors == 3 else 0
                
    return new_grid}

\helpercode{def run_life(width: int, 
                height: int, 
                steps: int, 
                initial_state: Optional[np.ndarray] = None,
                boundary: str = 'periodic') -> List[Grid]:
    """Run Game of Life for multiple steps
    
    Args:
        width: Grid width
        height: Grid height
        steps: Number of steps to evolve
        initial_state: Optional initial configuration
        boundary: Type of boundary conditions
        
    Returns:
        List of Grid instances representing evolution history
    """
    # Initialize first grid
    history = [Grid(width, height)]
    if initial_state is not None:
        history[0].grid = initial_state.copy()
    else:
        # Default to random initial state
        history[0].grid = np.random.randint(2, size=(height, width))
    
    # Evolve system
    for _ in range(steps - 1):
        history.append(evolve_life(history[-1], boundary))
        
    return history}

\notes{The implementation above provides:
1. Neighbor counting with different boundary conditions
2. Rule application following Conway's specifications
3. Support for both periodic and fixed boundaries
4. History tracking for visualization
5. Flexible initial state configuration

This base implementation will be essential when we combine it with Wolfram automata, as we'll need to modify the boundary conditions to interact with the Wolfram rules.}

\setupplotcode{import matplotlib.pyplot as plt}

\plotcode{# Demonstrate simple Life evolution with enhanced visualization
# Create a simple oscillator (blinker)
initial_state = np.zeros((5, 5))
initial_state[2, 1:4] = 1  # Three cells in a row

history = run_life(5, 5, steps=4, initial_state=initial_state)

# Visualize evolution
fig, axes = plt.subplots(1, 4, figsize=(15, 4))
fig.set_facecolor('white')  # White background for entire figure

for i, grid in enumerate(history):
    plot_automata_grid(grid, axes[i])
    axes[i].set_title(f'Step {i}')

plt.tight_layout()

mlai.write_figure(filename='life-blinker.svg', 
                 directory='\writeDiagramsDir/simulation')}


\figure{\includediagram{\diagramsDir/simulation/life-blinker}{80%}}{Evolution of a simple oscillator (blinker) in the Game of Life.}{life-blinker}

\notes{This implementation will serve as the foundation for our exploration of Life patterns and ultimately for our hybrid system combining Life with Wolfram automata. The key is the flexibility in boundary conditions, which will allow us to interface with Wolfram rules at the edges.}

\endif
