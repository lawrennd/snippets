\ifndef{rule30}
\define{rule30}

\editme


\include{_simulation/includes/automata-base.md}
\include{_simulation/includes/automata-diagrams.md}


\subsection{Rule 30}

\notes{Wolfram explored exhaustively the different automata, and [discovered that Rule 30](But the surprising [discovery I made in the 1980s](https://content.wolfram.com/sw-publications/2020/07/origins-randomness-physical-systems.pdf)) exhibited particularly interesting behaviour.}

\notes{Rule 30 generates patterns that appear random, yet are completely deterministic.}

\displaycode{markdown = generate_wolfram_rule_markdown_table(30)
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

\displaycode{# Generate Rule 30 explanation diagram
svg = generate_wolfram_rule_diagram(30)
filename = mlai.filename_join("rule-030_explanation.svg", "\writeDiagramsDir/simulation/")
with open(filename, 'w') as f:
    f.write(svg)}

\figure{\includediagram{\diagramsDir/simulation/rule-030_explanation}{95%}}{Rule 30 expressed in pixel form. Note how mixed the output states are compared to simpler rules.}{rule-030-explanation}

\setupcode{import numpy as np
import matplotlib.pyplot as plt}

\plotcode{# Create and visualize Rule 30 evolution
rule_30_history = run_wolfram_automaton(
    rule_number=30,
    width=101,
    steps=50
)

# Stack histories for visualization
evolution = np.vstack([grid.grid for grid in rule_30_history])

# Create visualization
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.imshow(evolution, cmap='binary')
ax.axis('off')
ax.set_title("Rule 30 Evolution")
fig.tight_layout()

mlai.write_figure(filename='rule-030-progression.svg', 
                 directory='\writeDiagramsDir/simulation')}

\subsection{Rule 30 in Cambridge}

\figure{\includejpg{\diagramsDir/simulation/rule-030-cambridge-north}{70%}}{Rule 30 has been used to decorate Cambridge North station with aluminium cladding.}{rule-030-cambridge-north}

\notes{
> But the surprising [discovery I made in the 1980s](https://content.wolfram.com/sw-publications/2020/07/origins-randomness-physical-systems.pdf) by looking at things like rule 30 is that actually no such "external source" is needed: instead, it's perfectly possible for [randomness to be generated intrinsically](https://www.wolframscience.com/nks/chap-7--mechanisms-in-programs-and-nature#sect-7-5--the-intrinsic-generation-of-randomness) within a system just through the process of applying definite underlying rules.
}

\notes{Wolfram refers to the pseudorandom pattern that emerges, in particular down the center line of the automata as "computationally irreducible". At one point this line was even used within Wolfram as a pseudorandom number generator.}

\endif
