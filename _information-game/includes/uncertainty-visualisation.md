\ifndef{uncertaintyVisualisation}
\define{uncertaintyVisualisation}

\editme

\subsection{Visualising the Parameter-Capacity Uncertainty Principle}

\notes{The uncertainty principle between parameters $\theta$ and capacity variables $c$ is a fundamental feature of information reservoirs. We can visualize this uncertainty relation using phase space plots.}

\slides{
* Uncertainty principle: $\Delta\theta \cdot \Delta c \geq k$
* Minimal uncertainty states form ellipses in phase space
* Quantum-like properties emerge from information constraints
* Different uncertainty states visualized as probability distributions
}

\notes{
We can demonstrate how the uncertainty principle manifests in different regimes:

1. **Quantum-like regime**: Near minimal entropy, the uncertainty product $\Delta\theta \cdot \Delta c$ approaches the lower bound $k$, creating wave-like interference patterns in probability space.

2. **Transitional regime**: As entropy increases, uncertainty relations begin to decouple, with $\Delta\theta \cdot \Delta c > k$.

3. **Classical regime**: At high entropy, parameter uncertainty dominates, creating diffusion-like dynamics with minimal influence from uncertainty relations.

The visualization shows probability distributions for these three regimes in both parameter space and capacity space.
}

\setupcode{import numpy as np}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai
from matplotlib.patches import Ellipse}

\plotcode{# Visualization of uncertainty ellipses
fig, ax = plt.subplots(figsize=plot.big_figsize)

# Parameters for uncertainty ellipses
k = 1  # Uncertainty constant
centers = [(0, 0), (2, 2), (4, 4)]
widths = [0.25, 0.5, 2]
heights = [4, 2.5, 2]
#heights = [k/w for w in widths]
colors = ['blue', 'green', 'red']
labels = ['Quantum-like', 'Transitional', 'Classical']

# Plot uncertainty ellipses
for center, width, height, color, label in zip(centers, widths, heights, colors, labels):
    ellipse = Ellipse(center, width, height, 
                     edgecolor=color, facecolor='none', 
                     linewidth=2, label=label)
    ax.add_patch(ellipse)
    
    # Add text label
    ax.text(center[0], center[1] + height/2 + 0.2, 
            label, ha='center', color=color)
    
    # Add area label (uncertainty product)
    area =  width * height
    ax.text(center[0], center[1] - height/2 - 0.3, 
            f'Area = {width:.2f} $\\times$ {height: .2f} $\\pi$', ha='center')

# Set axis labels and limits
ax.set_xlabel('Parameter $\\theta$')
ax.set_ylabel('Capacity $C$')
ax.set_xlim(-3, 7)
ax.set_ylim(-3, 7)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_title('Parameter-Capacity Uncertainty Relation')

# Add diagonal line representing constant uncertainty product
x = np.linspace(0.25, 6, 100)
y = k/x
ax.plot(x, y, 'k--', alpha=0.5, label='Minimum uncertainty: $\\Delta \\theta \\Delta C = k$')

ax.legend(loc='upper right')
mlai.write_figure(filename='uncertainty-ellipses.svg', 
                  directory = '\writeDiagramsDir/information-game')
}

\newslide{Visualisation of the Uncertainty Principle}
\figure{\includediagram{\diagramsDir/information-game/uncertainty-ellipses}{50%}}{Visualisaiton of the uncertainty trade-off between parameter precision and capacity.}{uncertainty-ellipses}

\notes{This visualization helps explain why information reservoirs with quantum-like properties naturally emerge at minimal entropy. The uncertainty principle is not imposed but arises naturally from the constraints of Shannon information theory applied to physical systems operating at minimal entropy.} 

\endif
