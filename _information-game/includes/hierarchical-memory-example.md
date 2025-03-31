\ifndef{hierarchicalMemoryExample}
\define{hierarchicalMemoryExample}

\editme

\subsection{Hierarchical Memory Organization Example}

\notes{As the game evolves to classical regimes, a hierarchical memory structure can emerge. We illustrate the idea with a simple dynamical system example.}

\slides{
* Classical information reservoirs organize hierarchically
* Variables separate into distinct timescale bands
* Fast variables: rapidly changing, high processing capacity
* Slow variables: gradually changing, high memory capacity
* Connect across scales for efficient information processing
}

\notes{Consider a system with 8 variables that undergo steepest ascent entropy maximization. As the system evolves, assume the eigenvalue spectrum of the Fisher information matrix has a separation into timescales as follows.

1. *Very slow variables* (eigenvalues ≈ 0.01) - Deep memory, context variables
2. *Slow variables* (eigenvalues ≈ 0.1) - Long-term memory
3. *Medium variables* (eigenvalues ≈ 1.0) - Intermediate processing/memory
4. *Fast variables* (eigenvalues ≈ 10.0) - Rapid processing, minimal memory

This implies a natural hierarchy where slow variables can provide context for faster variables, and faster variables can be guidedl  guided by slower variables.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai
import networkx as nx}

\plotcode{# Visualizing hierarchical memory structure

# Create a hierarchical structure
G = nx.DiGraph()

# Add nodes for different timescales
timescales = {
    'context': {'color': 'blue', 'size': 800, 'eigenvalue': 0.01},
    'long-term': {'color': 'green', 'size': 500, 'eigenvalue': 0.1},
    'intermediate': {'color': 'orange', 'size': 300, 'eigenvalue': 1.0},
    'processing': {'color': 'red', 'size': 100, 'eigenvalue': 10.0}
}

# Add nodes and connections
for level in timescales:
    G.add_node(level, **timescales[level])

# Add edges (hierarchical connections)
G.add_edge('context', 'long-term')
G.add_edge('context', 'intermediate')
G.add_edge('context', 'processing')
G.add_edge('long-term', 'intermediate')
G.add_edge('long-term', 'processing') 
G.add_edge('intermediate', 'processing')

# Create figure
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

# Get node attributes
node_colors = [G.nodes[n]['color'] for n in G.nodes]
node_sizes = [G.nodes[n]['size'] for n in G.nodes]
eigenvalues = [G.nodes[n]['eigenvalue'] for n in G.nodes]

# Create a hierarchical layout
pos = {
    'context': (0, 3),
    'long-term': (0, 2), 
    'intermediate': (0, 1),
    'processing': (0, 0)
}

# Draw the network
nx.draw_networkx(G, pos, with_labels=True, node_color=node_colors, 
                node_size=node_sizes, font_color='white', 
                font_weight='bold', ax=ax, arrowsize=20)

# Add eigenvalue labels
for node, position in pos.items():
    eigenvalue = G.nodes[node]['eigenvalue']
    ax.text(position[0] + 0.2, position[1], 
            f'$\\lambda = {eigenvalue}$', 
            fontsize=12)

ax.set_title('Hierarchical Memory Organization')
ax.set_axis_off()

# Add a second plot showing update dynamics
ax2 = fig.add_axes([0.6, 0.2, 0.35, 0.6])
t = np.linspace(0, 100, 1000)
for node, info in timescales.items():
    eigenvalue = info['eigenvalue']
    color = info['color']
    ax2.plot(t, np.sin(eigenvalue * t) * np.exp(-0.01 * t), 
             color=color, label=f"{node} (λ={eigenvalue})")

ax2.set_xlabel('Time')
ax2.set_ylabel('Parameter value')
ax2.set_title('Update Dynamics at Different Timescales')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.7)

mlai.write_figure(filename='hierarchical-memory-organisation-example.svg', 
                  directory = '\writeDiagramDir/information-game')
}

\figure{\includeDiagram{\diagramsDir/information-game/hierarchical-memory-organisation-example}{80%}}{}{hierarchical-memory-organisation-example}

\notes{A hierarchical memory structure emerges naturally during entropy maximization. The timescale separation creates a computational architecture where different levels operate at different characteristic timescales.}

\notes{The hierarchy is important in understanding how it is possible for information information reservoirs to achieve high capacity (entropy) without underlying quantum-like interference effects. Different variables are characterised based on their eigenvalue in the Fisher information matrix.} 

\endif
