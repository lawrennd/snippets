\ifndef{wolframAutomata}
\define{wolframAutomata}


\editme


\subsection{Wolfram Automata}

\notes{Cellular automata are systems with simple rules that lead to complex behaviours. A simple cellular automata can be defined over one dimension of cells binary cells, and a discrete time evolution. At each time step a cell's state is dependent on its state in a previous time step and that of its neighbours.}

\notes{Stephen Wolfram noticed that such systems could be represented by a binary number that described the nature of these rules. Each cell ($x$) has a state at time $t$, and the state of two neighbours ($x+1$ and $x-1$ at time $t$. The cellular automata dictates what the value of that cell will be at time $t+1$. The possible values of the cell are $1$ or $0$.}

\notes{This simple system has eight different input states (three bits associated with the cell and its two neighbours). And two possible output states (one bit associated with the cell's output state). so the rules of the cellular automata can be expressed by exhaustively running through the eight different input states giving the output state. To do this requires a string of eight bits (or a byte) long: one output per different input. That means there are 256 different possible cellular automata.}

\notes{Wolfram numbered the different cellular automata according to the output states in an 8 bit binary number, each bit indexed by the three bits of the input states (most significant bit first). So Rule 0 would give zero output regardless of the input state. Rule 1 will give an output of 1 for the input state of three zeros etc and Rule 255 will give an output of 1 regardless of the input state.}

\setuphelpercode{import numpy as np
from typing import Dict, Tuple, List}

\helpercode{def get_neighborhood_state(left: int, center: int, right: int) -> int:
    """Convert three cells into their neighborhood state index (0-7)
    
    Args:
        left: State of left cell (0 or 1)
        center: State of center cell (0 or 1)
        right: State of right cell (0 or 1)
        
    Returns:
        Integer from 0-7 representing the neighborhood state
    """
    return (left << 2) | (center << 1) | right}


\helpercode{def generate_rule_markdown_table(rule_number: int) -> str:
    """Generate a Markdown table explaining a cellular automaton rule
    
    Args:
        rule_number: Integer from 0-255 specifying the rule
        
    Returns:
        Markdown formatted table explaining the rule
    """
    rule_binary = format(rule_number, '08b')
    
    # Create table header
    table = "| Pattern | Result | Binary Position | Rule Bit |\n"
    table += "|---------|---------|----------------|----------|\n"
    
    # Create patterns
    neighborhoods = [
        (1,1,1), (1,1,0), (1,0,1), (1,0,0),
        (0,1,1), (0,1,0), (0,0,1), (0,0,0)
    ]
    
    # Add each row
    for i, pattern in enumerate(neighborhoods):
        pattern_str = ''.join(['■' if x == 1 else '□' for x in pattern])
        result = '■' if rule_binary[i] == '1' else '□'
        table += f"| {pattern_str} | {result} | {7-i} | {rule_binary[i]} |\n"
    
    return table}

\displaycode{markdown = generate_rule_markdown_table(1)
print(markdown)}


\subsection{Wolfram Automata Coding}

| Pattern | Result | Binary Position | Rule Bit |
|---------|---------|----------------|----------|
| ■■■ | □ | 7 | 0 |
| ■■□ | □ | 6 | 0 |
| ■□■ | □ | 5 | 0 |
| ■□□ | □ | 4 | 0 |
| □■■ | □ | 3 | 0 |
| □■□ | □ | 2 | 0 |
| □□■ | □ | 1 | 0 |
| □□□ | ■ | 0 | 1 |

The rule number 1 in binary is: 00000001

\newslide{Wolfram Automata Coding}

Each bit in the binary number determines the result for one of the eight possible patterns of three cells:

* A foreground square (■) represents a cell in state 1
* A background square (□) represents a cell in state 0
* The patterns are ordered from 111 (7) to 000 (0)
* The binary number determines the next state of the center cell for each pattern

\newslide{Wolfram Automata Coding}

For example:

* If you see pattern '111' (■■■), the next state will be {'■' if rule_binary[0] == '1' else '□'}
* If you see pattern '110' (■■□), the next state will be {'■' if rule_binary[1] == '1' else '□'}

And so on...

\newslide{Wolfram Automata Coding}

At each time step:

1. Look at each cell and its two neighbors
2. Find this pattern in the table above
3. The center cell becomes the value shown in the 'Result' column


\helpercode{def generate_rule_explanation_svg(rule_number, cell_size=30):
    """
	Generate an SVG visualization of how a specific Wolfram rule works
	"""
    
	rule_binary = format(rule_number, '08b')
    
    # Define dimensions
    pattern_width = 3 * cell_size
    pattern_height = cell_size
    total_width = 8 * (pattern_width + cell_size)  # Extra space between patterns
    total_height = 3 * pattern_height
    
    neighborhoods = [
        (1,1,1), (1,1,0), (1,0,1), (1,0,0),
        (0,1,1), (0,1,0), (0,0,1), (0,0,0)
    ]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_width} {total_height}">
    <style>
        .label {{ font: bold {cell_size//2}px sans-serif; }}
    </style>
    '''
    
    # Draw each neighborhood pattern and its result
    for i, (neighborhood) in enumerate(neighborhoods):
        x_offset = i * (pattern_width + cell_size)
        
        # Draw input pattern (top row)
        for j, cell in enumerate(neighborhood):
            x = x_offset + j * cell_size
            if cell == 1:
                svg += f'<rect x="{x}" y="0" width="{cell_size}" height="{cell_size}" fill="black" stroke="gray"/>'
            else:
                svg += f'<rect x="{x}" y="0" width="{cell_size}" height="{cell_size}" fill="white" stroke="gray"/>'
        
        # Draw arrow
        arrow_y = pattern_height + cell_size//2
        svg += f'<line x1="{x_offset + pattern_width//2}" y1="{pattern_height + 5}" x2="{x_offset + pattern_width//2}" y2="{2*pattern_height - 5}" stroke="black" marker-end="url(#arrowhead)"/>'
        
        # Draw result (bottom row)
        result = int(rule_binary[i])
        x = x_offset + cell_size
        y = 2 * pattern_height
        if result == 1:
            svg += f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" fill="black" stroke="gray"/>'
        else:
            svg += f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" fill="white" stroke="gray"/>'
    
        # Add binary value label
        svg += f'<text x="{x_offset + pattern_width//2}" y="{total_height + cell_size//2}" text-anchor="middle" class="label">{rule_binary[i]}</text>'
    
    # Add arrowhead definition
    svg += '''
    <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
            <polygon points="0 0, 10 3.5, 0 7" fill="black"/>
        </marker>
    </defs>
    '''
    
    svg += '</svg>'
    return svg}

\displaycode{svg = generate_rule_explanation_svg(1)
filename = mlai.filename_join("rule-001_explanation.svg", "\writeDiagramsDir/simulation/")
with open(filename, 'w') as f:
  f.write(svg)
}

\newslide{Rule 1}

\figure{\includediagram{\diagramsDir/simulation/rule-001_explanation}{95%}}{Rule 1 expressed in pixel form.}{rule-001_explanation}



\setuphelpercode{import numpy as np}

\helpercode{def get_rule_mapping(rule_number: int) -> Dict[Tuple[int, int, int], int]:
    """Convert a rule number (0-255) into a dictionary of state transitions
    
    Args:
        rule_number: Integer from 0-255 specifying the rule
        
    Returns:
        Dictionary mapping neighborhood tuples to next state
        
    Raises:
        ValueError: If rule_number is not between 0 and 255
    """
    if not 0 <= rule_number <= 255:
        raise ValueError("Rule number must be between 0 and 255")
    
    # Convert rule number to 8-bit binary
    rule_binary = format(rule_number, '08b')
    
    # Create mapping for all possible neighborhood combinations
    neighborhoods = [
        (1,1,1), (1,1,0), (1,0,1), (1,0,0),
        (0,1,1), (0,1,0), (0,0,1), (0,0,0)
    ]
    
    # Create rule dictionary
    return {neighborhood: int(rule_binary[i]) for i, neighborhood in enumerate(neighborhoods)}}

\helpercode{def generate_svg(cells: np.ndarray, filename: str, cell_size: int = 10) -> None:
    """Generate an SVG file for a single time slice of the automaton
    
    Args:
        cells: 1D numpy array representing cell states
        filename: Path to save SVG file
        cell_size: Size of each cell in pixels
    """
    width = len(cells) * cell_size
    height = cell_size
    
    # Start SVG file
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">\n'
    
    # Add cells
    for i, cell in enumerate(cells):
        x = i * cell_size
        if cell == 1:
            svg += f'  <rect x="{x}" y="0" width="{cell_size}" height="{cell_size}" fill="black" />\n'
    
    svg += '</svg>'
    
    # Write to file
    with open(filename, 'w') as f:
        f.write(svg)}

\helpercode{def cellular_automaton(rule_number: int, size: int, steps: int, 
                         initial_state: np.ndarray = None,
                         periodic: bool = True,
                         svg_interval: int = None) -> np.ndarray:
    """Implement elementary cellular automaton for any rule number
    
    Args:
        rule_number: Integer 0-255 specifying which rule to use
        size: Width of the automaton
        steps: Number of time steps to evolve
        initial_state: Optional initial state array. If None, single center cell is set to 1
        periodic: If True, use periodic boundary conditions
        svg_interval: If set, generate SVG files every this many steps
        
    Returns:
        2D numpy array of shape (size, steps) containing automaton history
        
    Notes:
        With periodic=True, the automaton wraps around the edges
        With periodic=False, cells outside the grid are treated as 0
    """
    # Initialize the cellular automaton
    ca = np.zeros((size, steps), dtype=int)
    
    # Set initial state
    if initial_state is not None:
        ca[:, 0] = initial_state
    else:
        ca[size // 2, 0] = 1  # Set the middle cell of the first column to 1
    
    # Get rule mapping
    rule = get_rule_mapping(rule_number)
    
    # Evolve the cellular automaton
    for t in range(1, steps):
        for i in range(size):
            # Get neighbor states with boundary handling
            if periodic:
                left = ca[(i-1) % size, t-1]
                right = ca[(i+1) % size, t-1]
            else:
                left = ca[i-1, t-1] if i > 0 else 0
                right = ca[i+1, t-1] if i < size-1 else 0
            
            center = ca[i, t-1]
            neighborhood = (left, center, right)
            ca[i, t] = rule[neighborhood]
        
        # Generate SVG if requested
        if svg_interval and t % svg_interval == 0:
			filename = mlai.filename_join(f"cellular-automata-rule-{rule_number:03d}-step-{:03d}.svg", "\writeDiagramsDir/simulation/")		
            generate_svg(ca[:, t], filename)
    
    return ca}

\setuphelpercode{import matplotlib.pyplot as plt}

\helpercode{def plot_automaton(rule_number: int = 30, 
                     size: int = 101, 
                     steps: int = 100, 
                     initial_state: np.ndarray = None,
                     periodic: bool = True,
                     svg_interval: int = None,
                     title: str = None) -> None:
    """Plot the evolution of a cellular automaton
    
    Args:
        rule_number: Rule to use (0-255)
        size: Width of the automaton
        steps: Number of time steps
        initial_state: Optional initial state array
        periodic: Whether to use periodic boundary conditions
        svg_interval: If set, save SVGs every this many steps
        title: Optional custom title for the plot
    """
    # Generate the cellular automaton
    ca = cellular_automaton(
        rule_number, 
        size, 
        steps, 
        initial_state=initial_state,
        periodic=periodic,
        svg_interval=svg_interval
    )
    
    # Plot the result
    fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
    ax.imshow(ca, cmap='binary', aspect='auto')
    
    if title is None:
        title = f"Elementary Cellular Automaton - Rule {rule_number}"
    ax.set_title(title)
    ax.set_xlabel("Time →")
    ax.set_ylabel("Space")
    
    mlai.write_figure(
        filename=f'rule-{rule_number:03d}-progression.svg',
        directory='\writeDiagramsDir/simulation'
    )}

\endif
