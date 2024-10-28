\ifndef{lifeRules}
\define{lifeRules}

\editme

\notes{\subsection{Life Rules}}

\notes{John Conway's game of life is a cellular automaton where the cells obey three very simple rules. The cells live on a rectangular grid, so that each cell has 8 possible neighbors.}

\setuphelpercode{from typing import Tuple, Optional, Set
import numpy as np}

\helpercode{def count_neighbors(grid: np.ndarray, 
                     x: int, 
                     y: int, 
                     boundary: str = 'periodic',
                     wolfram_borders: Optional[Set[int]] = None) -> int:
    """Count live neighbors for a cell in Game of Life
    
    Args:
        grid: 2D numpy array representing the current state
        x: X coordinate of cell
        y: Y coordinate of cell
        boundary: Type of boundary conditions ('periodic', 'fixed', or 'wolfram')
        wolfram_borders: If using 'wolfram' boundary, set of active border indices
        
    Returns:
        Number of live neighbors (0-8)
        
    Notes:
        boundary options:
        - 'periodic': Grid wraps around
        - 'fixed': Outside cells treated as dead
        - 'wolfram': Uses Wolfram rule for border cells
    """
    count = 0
    height, width = grid.shape
    
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
                
            nx, ny = x + dx, y + dy
            
            if boundary == 'periodic':
                nx = nx % width
                ny = ny % height
                count += grid[ny, nx]
            elif boundary == 'fixed':
                if 0 <= nx < width and 0 <= ny < height:
                    count += grid[ny, nx]
            elif boundary == 'wolfram':
                if 0 <= ny < height:
                    if 0 <= nx < width:
                        count += grid[ny, nx]
                    else:
                        # Check if this border position is active in Wolfram rule
                        border_idx = ny
                        if wolfram_borders and border_idx in wolfram_borders:
                            count += 1
                
    return count}

\helpercode{def apply_life_rules(current_state: int, neighbor_count: int) -> int:
    """Apply Conway's Game of Life rules to determine next cell state
    
    Args:
        current_state: Current state of cell (0 or 1)
        neighbor_count: Number of live neighbors (0-8)
        
    Returns:
        Next state of cell (0 or 1)
        
    Rules:
        1. Any live cell with fewer than two live neighbours dies (underpopulation)
        2. Any live cell with two or three live neighbours lives on
        3. Any live cell with more than three live neighbours dies (overpopulation)
        4. Any dead cell with exactly three live neighbours becomes alive (reproduction)
    """
    if current_state == 1:
        return 1 if 2 <= neighbor_count <= 3 else 0
    else:
        return 1 if neighbor_count == 3 else 0}

\helpercode{def generate_life_rule_diagram(rule_type: str) -> str:
    """Generate SVG visualization of Game of Life rules matching original diagrams
    
    Args:
        rule_type: One of 'loneliness-before', 'loneliness-after',
                  'overcrowding-before', 'overcrowding-after',
                  'birth-before', 'birth-after'
    Returns:
        SVG string visualizing the rule
    """
    # Rule configurations - (x,y) coordinates of filled cells
    configs = {
        'loneliness-before': [(0,0), (2,0), (1,1)],  # 2 neighbors
        'loneliness-after': [(0,0), (2,0)],  # Cell dies
        'overcrowding-before': [(0,0), (2,0), (2,1), (2,2), (1,1)],  # 4 neighbors
        'overcrowding-after': [(0,0), (2,0), (2,1), (2,2)],  # Cell dies
        'birth-before': [(0,0), (2,0), (2,2)],  # 3 neighbors
        'birth-after': [(0,0), (2,0), (2,2), (1,1)]  # New cell born
    }
    
    if rule_type not in configs:
        raise ValueError(f"Unknown rule type: {rule_type}")
    
    cell_size = 30
    
    # SVG setup with original viewBox and background
    svg = f'''<svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="-20 -20 130 130"
    width="130"
    height="130">
<rect width="130" height="130" x="-20" y="-20" fill="#fff"/>
'''
    
    # Draw filled cells
    for x, y in configs[rule_type]:
        svg += f'<rect width="{cell_size}" height="{cell_size}" '
        svg += f'x="{x*cell_size}" y="{y*cell_size}" fill="#000"/>\n'
    
    # Draw vertical grid lines
    for i in range(4):
        x = i * cell_size
        svg += f'<line x1="{x}" y1="-20" x2="{x}" y2="110" '
        svg += f'stroke="#c0c0c0" stroke-width="3"/>\n'
    
    # Draw horizontal grid lines
    for i in range(4):
        y = i * cell_size
        svg += f'<line x1="-20" y1="{y}" x2="110" y2="{y}" '
        svg += f'stroke="#c0c0c0" stroke-width="3"/>\n'
    
    # Draw red highlight box around center cell
    fill = "none" if "after" in rule_type else "#000"
    svg += f'<rect width="{cell_size}" height="{cell_size}" '
    svg += f'x="{cell_size}" y="{cell_size}" stroke="red" '
    svg += f'stroke-width="3" fill="{fill}"/>\n'
    
    svg += '</svg>'
    return svg}

\displaycode{# Generate the rule diagrams
for rule in ['loneliness', 'overcrowding', 'birth']:
    for state in ['before', 'after']:
        svg = generate_life_rule_diagram(f"{rule}-{state}")
        filename = mlai.filename_join(f"life-rules-{1 if rule == 'loneliness' else 2 if rule == 'overcrowding' else 3}-{0 if state == 'before' else 1}.svg", 
                                    "\writeDiagramsDir/simulation/")
        with open(filename, 'w') as f:
            f.write(svg)}


\newslide{Loneliness}

\figure{\columns{\threeColumns{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-1-0}{100%}}}{\aligncenter{*loneliness*}\aligncenter{\includediagram{\diagramsDir/util/right-arrow}{60%}}}{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-1-1}{100%}}}{30%}{39%}{30%}}{\aligncenter{\includejpg{\diagramsDir/maths/John-Conway}{100%}{}{right}}}{70%}{30%}}{'Death' through loneliness in Conway's game of life. If a cell is surrounded by less than three cells, it 'dies' through loneliness.}{life-rules-loneliness}

\notes{The game proceeds in turns, and at each location in the grid is either alive or dead. Each turn, a cell counts its neighbors. If there are two or fewer neighbors, the cell 'dies' of 'loneliness'.}

\newslide{Crowding}

\figure{\columns{\threeColumns{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-2-0}{100%}}}{\aligncenter{*overcrowding*}\aligncenter{\includediagram{\diagramsDir/util/right-arrow}{60%}}}{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-2-1}{100%}}}{30%}{39%}{30%}}{\aligncenter{\includejpg{\diagramsDir/maths/John-Conway}{100%}{}{right}}}{70%}{30%}}{'Death' through overpopulation in Conway's game of life. If a cell is surrounded by more than three cells, it 'dies' through loneliness.}{life-rules-crowding}

\notes{If there are four or more neighbors, the cell 'dies' from 'overcrowding'. If there are three neighbors, the cell persists, or if it is currently dead, a new cell is born.}

\newslide{Birth}

\figure{\columns{\threeColumns{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-3-0}{100%}}}{\aligncenter{*birth*}\aligncenter{\includediagram{\diagramsDir/util/right-arrow}{60%}}}{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-3-1}{100%}}}{30%}{39%}{30%}}{\aligncenter{\includejpg{\diagramsDir/maths/John-Conway}{100%}{}{right}}}{70%}{30%}}{Birth in Conway's life. Any position surrounded by precisely three live cells will give birth to a new cell at the next turn.}{life-rules-crowding}

\notes{And that's it. Those are the simple 'physical laws' for Conway's game.}

\endif

