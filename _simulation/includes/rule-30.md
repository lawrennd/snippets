\ifndef{rule30}
\define{rule30}

\editme


\subsection{Rule 30}



\notes{Wolfram explored exhaustively the different automata, and [discovered that Rule 30](But the surprising [discovery I made in the 1980s](https://content.wolfram.com/sw-publications/2020/07/origins-randomness-physical-systems.pdf)) exhibited particularly interesting behaviour.}

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

\figure{\includediagram{\diagramsDir/simulation/rule-030_explanation}{95%}}{Rule 30 expressed in pixel form.}{rule-030-explanation}

\setupcode{import numpy as np}


\helpercode{def rule_30(size, steps):
    # Initialize the cellular automaton
    ca = np.zeros((steps, size), dtype=int)
    ca[0, size // 2] = 1  # Set the middle cell of the first row to 1
    
    # Define Rule 30
    rule = {(1,1,1): 0, (1,1,0): 0, (1,0,1): 0, (1,0,0): 1,
            (0,1,1): 1, (0,1,0): 1, (0,0,1): 1, (0,0,0): 0}
    
    # Evolve the cellular automaton
    for i in range(1, steps):
        for j in range(size):
            left = ca[i-1, (j-1) % size]
            center = ca[i-1, j]
            right = ca[i-1, (j+1) % size]
            ca[i, j] = rule[(left, center, right)]
    
    return ca
}

\code{# Set parameters
size = 101
steps = 50

# Generate the cellular automaton
ca = rule_30(size, steps)}

\setupdisplaycode{import matplotlib.pyplot as plt}

\plotcode{
# Plot the result
fig, ax = plt.subplots(figsize=mlai.plot.big_wide_figsize)
ax.imshow(ca, cmap='binary')
ax.axis('off')
ax.tight_layout()

mlai.write_figure(filename='rule-030-progression.svg', directory='\writeDiagramsDir/simulation')}


\newslide{}

\figure{\includediagram{\diagramsDir/simulation/rule-030-progression}{70%}}{Progression of Rule 30 with a single cell on as the initial condition.}{rule-030-progression}

\subsection{Rule 30 in Cambridge}

\figure{\includejpg{\diagramsDir/simulation/rule-030-cambridge-north}{70%}}{Rule 30 has been used to decorate Cambridge North station with aluminium cladding.}{rule-030-cambridge-north}

\notes{
> But the surprising [discovery I made in the 1980s](https://content.wolfram.com/sw-publications/2020/07/origins-randomness-physical-systems.pdf) by looking at things like rule 30 is that actually no such “external source” is needed: instead, it’s perfectly possible for [randomness to be generated intrinsically](https://www.wolframscience.com/nks/chap-7--mechanisms-in-programs-and-nature#sect-7-5--the-intrinsic-generation-of-randomness) within a system just through the process of applying definite underlying rules.
}
\endif
