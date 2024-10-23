\ifndef{rule30}
\define{rule30}

\editme


\subsection{Rule 30}

\notes{Wolfram explored exhaustively the different automata, and [discovered that Rule 30](But the surprising [discovery I made in the 1980s](https://content.wolfram.com/sw-publications/2020/07/origins-randomness-physical-systems.pdf)) exhibited particularly interesting behaviour.}


\setupcode{import numpy as np}


\code{def rule_30(size, steps):
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

# Set parameters
size = 401
steps = 200

# Generate the cellular automaton
ca = rule_30(size, steps)}

\setupdisplaycode{import matplotlib.pyplot as plt}

\displaycode{
# Plot the result
plt.figure(figsize=(10, 10))
plt.imshow(ca, cmap='binary')
plt.title("Rule 30 Cellular Automaton")
plt.axis('off')
plt.tight_layout()
plt.show()}


\notes{
> But the surprising [discovery I made in the 1980s](https://content.wolfram.com/sw-publications/2020/07/origins-randomness-physical-systems.pdf) by looking at things like rule 30 is that actually no such “external source” is needed: instead, it’s perfectly possible for [randomness to be generated intrinsically](https://www.wolframscience.com/nks/chap-7--mechanisms-in-programs-and-nature#sect-7-5--the-intrinsic-generation-of-randomness) within a system just through the process of applying definite underlying rules.
}
\endif
