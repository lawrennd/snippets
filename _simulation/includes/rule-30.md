\ifndef{rule30}
\define{rule30}

\editme

\subsection{Rule 30}

\notes{Wolfram explored exhaustively the different automata, and [discovered that Rule 30](But the surprising [discovery I made in the 1980s](https://content.wolfram.com/sw-publications/2020/07/origins-randomness-physical-systems.pdf)) exhibited particularly interesting behaviour.}

\notes{Rule 30 generates patterns that appear random, yet are completely deterministic.}

\displaycode{markdown = generate_rule_markdown_table(30)
print(markdown)}

| Pattern | Result | Binary Position | Rule Bit |
|---------|---------|----------------|----------|
| ■■■ | □ | 7 | 0 |
| ■■□ | □ | 6 | 0 |
| ■□■ | □ | 5 | 0 |
| ■□□ | ■ | 4 | 1 |
| □■■ | ■ | 3 | 1 |
| □■□ | ■ | 2 | 1 |
| □□■ | ■ | 1 | 1 |
| □□□ | □ | 0 | 0 |

The rule number 30 in binary is: 00011110

\newslide{Rule 30}

\plotcode{svg = generate_rule_explanation_svg(30)
filename = mlai.filename_join("rule-030_explanation.svg", "\writeDiagramsDir/simulation/")
with open(filename, 'w') as f:
    f.write(svg)}

\figure{\includediagram{\diagramsDir/simulation/rule-030_explanation}{95%}}{Rule 30 expressed in pixel form.}{rule-030-explanation}

\setuphelpercode{import numpy as np
from typing import Tuple, Optional}

\helpercode{def rule_30_evolution(size: int, 
                        steps: int, 
                        initial_state: Optional[np.ndarray] = None,
                        periodic: bool = True) -> np.ndarray:
    """Implement Rule 30 cellular automaton
    
    Args:
        size: Width of the automaton
        steps: Number of time steps to evolve
        initial_state: Optional initial state array. If None, single center cell is set to 1
        periodic: If True, use periodic boundary conditions
        
    Returns:
        2D numpy array of shape (steps, size) containing automaton history
    """
    # We can leverage our general cellular automaton implementation
    ca = cellular_automaton(
        rule_number=30,
        size=size,
        steps=steps,
        initial_state=initial_state,
        periodic=periodic
    )
    
    # Transpose to match original orientation
    return ca.T}

\code{# Set parameters
size = 101
steps = 50

# Generate the cellular automaton
ca = rule_30_evolution(size=size, steps=steps)}

\setupdisplaycode{import matplotlib.pyplot as plt}

\plotcode{
# Plot the result
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
fig.tight_layout()
ax.imshow(ca, cmap='binary')
ax.axis('off')

mlai.write_figure(filename='rule-030-progression.svg', directory='\writeDiagramsDir/simulation')}

\newslide{}

\figure{\includediagram{\diagramsDir/simulation/rule-030-progression}{70%}}{Progression of Rule 30 with a single cell on as the initial condition. Notice the emergence of seemingly random patterns, particularly along the central column.}{rule-030-progression}

\subsection{Rule 30 in Cambridge}

\figure{\includejpg{\diagramsDir/simulation/rule-030-cambridge-north}{70%}}{Rule 30 has been used to decorate Cambridge North station with aluminium cladding.}{rule-030-cambridge-north}

\notes{
> But the surprising [discovery I made in the 1980s](https://content.wolfram.com/sw-publications/2020/07/origins-randomness-physical-systems.pdf) by looking at things like rule 30 is that actually no such "external source" is needed: instead, it's perfectly possible for [randomness to be generated intrinsically](https://www.wolframscience.com/nks/chap-7--mechanisms-in-programs-and-nature#sect-7-5--the-intrinsic-generation-of-randomness) within a system just through the process of applying definite underlying rules.
}

\notes{Wolfram refers to the pseudorandom pattern that emerges, in particular down the center line of the automata as "computationally irreducible". At one point this line was even used within Wolfram as a pseudorandom number generator.}

\endif
