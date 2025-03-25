\ifndef{hierarchicalMemoryExample}
\define{hierarchicalMemoryExample}

\editme

\subsection{Hierarchical Memory Organization Example}

\notes{As our system evolves from quantum-like to classical regimes, a hierarchical memory structure emerges. We can illustrate this with a simple dynamical system example.}

\slides{
* Classical information reservoirs organize hierarchically
* Variables separate into distinct timescale bands
* Fast variables: rapidly changing, high processing capacity
* Slow variables: gradually changing, high memory capacity
* Connections across scales create efficient information processing
}

\notes{
Consider a system with 8 variables that undergo steepest ascent entropy maximization. As the system evolves, the eigenvalue spectrum of the Fisher information matrix reveals a natural separation into timescales:

1. **Very slow variables** (eigenvalues ≈ 0.01) - Deep memory, context variables
2. **Slow variables** (eigenvalues ≈ 0.1) - Long-term memory
3. **Medium variables** (eigenvalues ≈ 1.0) - Intermediate processing/memory
4. **Fast variables** (eigenvalues ≈ 10.0) - Rapid processing, minimal memory

This creates a natural hierarchy where slow variables provide context for faster variables, and faster variables provide detailed implementation of processes guided by slower variables.
}

\code{
# Visualizing hierarchical memory structure
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

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
fig, ax = plt.subplots(figsize=(10, 8))

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
            f'λ = {eigenvalue}', 
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
}

\notes{
This hierarchical structure emerges naturally during entropy maximization, without requiring explicit design. The timescale separation creates a computational architecture where information flows between levels, with each level operating at its characteristic timescale.

This example illustrates how classical hierarchical information reservoirs can achieve high capacity without requiring quantum-like interference effects. Different variables specialize in different aspects of information processing based purely on their eigenvalue in the Fisher information matrix.
} 

\endif
