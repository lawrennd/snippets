\ifndef{wolframAutomata}
\define{wolframAutomata}



\include{_simulation/includes/automata-base.md}
\include{_simulation/includes/automata-diagrams.md}

\editme

\subsection{Wolfram Automata}

\notes{Cellular automata are systems with simple rules that lead to complex behaviours. A simple cellular automata can be defined over one dimension of cells binary cells, and a discrete time evolution. At each time step a cell's state is dependent on its state in a previous time step and that of its neighbours.}

\notes{Stephen Wolfram noticed that such systems could be represented by a binary number that described the nature of these rules. Each cell ($x$) has a state at time $t$, and the state of two neighbours ($x+1$ and $x-1$ at time $t$. The cellular automata dictates what the value of that cell will be at time $t+1$. The possible values of the cell are $1$ or $0$.}

\notes{This simple system has eight different input states (three bits associated with the cell and its two neighbours). And two possible output states (one bit associated with the cell's output state). so the rules of the cellular automata can be expressed by exhaustively running through the eight different input states giving the output state. To do this requires a string of eight bits (or a byte) long: one output per different input. That means there are 256 different possible cellular automata.}

\notes{Wolfram numbered the different cellular automata according to the output states in an 8 bit binary number, each bit indexed by the three bits of the input states (most significant bit first). So Rule 0 would give zero output regardless of the input state. Rule 1 will give an output of 1 for the input state of three zeros etc and Rule 255 will give an output of 1 regardless of the input state.}

\setuphelpercode{import numpy as np
from typing import Dict, Tuple, List}


\displaycode{markdown = generate_wolfram_rule_markdown_table(1)
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
    
    return {neighborhood: int(rule_binary[i]) 
            for i, neighborhood in enumerate(neighborhoods)}}

\helpercode{def evolve_wolfram(grid: Grid, rule_number: int) -> Grid:
    """Evolve one step of a Wolfram cellular automaton
    
    Args:
        grid: 1D Grid instance representing current state
        rule_number: Which Wolfram rule to apply (0-255)
        
    Returns:
        New Grid instance representing next state
    """
    rule = get_rule_mapping(rule_number)
    new_grid = Grid(grid.width)
    
    for i in range(grid.width):
        left = grid[(i-1) % grid.width]
        center = grid[i]
        right = grid[(i+1) % grid.width]
        new_grid[i] = rule[(left, center, right)]
        
    return new_grid}

\helpercode{def run_wolfram_automaton(rule_number: int, 
                            width: int, 
                            steps: int, 
                            initial_state: np.ndarray = None) -> List[Grid]:
    """Run a Wolfram automaton for multiple steps
    
    Args:
        rule_number: Which rule to apply (0-255)
        width: Width of the automaton
        steps: Number of steps to evolve
        initial_state: Optional initial state. If None, single center cell is set to 1
        
    Returns:
        List of Grid instances representing evolution history
    """
    # Initialize first grid
    history = [Grid(width)]
    if initial_state is not None:
        history[0].grid[0,:] = initial_state
    else:
        history[0][width // 2] = 1
    
    # Evolve system
    for _ in range(steps - 1):
        history.append(evolve_wolfram(history[-1], rule_number))
        
    return history}

\displaycode{# Demonstrate Rule 1
rule_1_history = run_wolfram_automaton(1, width=8, steps=4)
svg = generate_wolfram_rule_diagram(1)
filename = mlai.filename_join("rule-001_explanation.svg", "\writeDiagramsDir/simulation/")
with open(filename, 'w') as f:
    f.write(svg)}

\subsection{Rule 1}

\figure{\includediagram{\diagramsDir/simulation/rule-001_explanation}{95%}}{Rule 1 expressed in pixel form.}{rule-001_explanation}


\endif
