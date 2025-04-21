\ifndef{interactionGeometryExample}
\define{interactionGeometryExample}

\editme

\subsection{Interaction Geometry Example: Coupling Between Observables}

\notes{Building on the minimal resolution example, we'll now explore how observables interact with each other once they become resolvable. This example demonstrates the emergence of interaction geometry, where observables become information-bearing not just individually, but in combination.}


\notes{In this example, we'll simulate a system with three latent coordinates that become resolvable as observables. We'll show how these observables interact with each other, leading to the emergence of a network of dependencies.}

\helpercode{def compute_fisher_information(m1, m2, m3, sigma=1.0, coupling=0.0):
    """
    Compute the Fisher information matrix for a 3D Gaussian distribution with coupling.
    
    Parameters:
    -----------
    m1, m2, m3 : float
        Mean values of the distribution
    sigma : float
        Standard deviation (resolution parameter)
    coupling : float
        Coupling strength between coordinates
        
    Returns:
    --------
    G : ndarray
        3x3 Fisher information matrix
    """
    # Base Fisher information matrix (diagonal)
    G = np.eye(3) / sigma**2
    
    # Add off-diagonal terms for coupling
    if coupling > 0:
        G[0, 1] = G[1, 0] = coupling / sigma**2
        G[0, 2] = G[2, 0] = coupling / sigma**2
        G[1, 2] = G[2, 1] = coupling / sigma**2
    
    return G

def compute_entropy_gradient(m1, m2, m3, sigma=1.0, coupling=0.0):
    """
    Compute the entropy gradient for a 3D Gaussian distribution with coupling.
    
    Parameters:
    -----------
    m1, m2, m3 : float
        Mean values of the distribution
    sigma : float
        Standard deviation (resolution parameter)
    coupling : float
        Coupling strength between coordinates
        
    Returns:
    --------
    gradient : ndarray
        3D gradient vector [dS/dm1, dS/dm2, dS/dm3]
    """
    G = compute_fisher_information(m1, m2, m3, sigma, coupling)
    theta = np.array([m1, m2, m3])  # Natural parameters
    return G @ theta

def compute_entropy(m1, m2, m3, sigma=1.0, coupling=0.0):
    """
    Compute the entropy of a 3D Gaussian distribution with coupling.
    
    Parameters:
    -----------
    m1, m2, m3 : float
        Mean values of the distribution
    sigma : float
        Standard deviation (resolution parameter)
    coupling : float
        Coupling strength between coordinates
        
    Returns:
    --------
    entropy : float
        Entropy value
    """
    # For a 3D Gaussian with coupling, the entropy depends on the determinant of the covariance matrix
    # This is a simplified model
    det = (1 - coupling**2)**3 * sigma**6
    return 0.5 * np.log((2 * np.pi * np.e)**3 * det)

def is_resolvable(m1, m2, m3, sigma, threshold=0.1):
    """
    Determine if coordinates are resolvable based on the entropy gradient.
    
    Parameters:
    -----------
    m1, m2, m3 : float
        Mean values of the distribution
    sigma : float
        Standard deviation (resolution parameter)
    threshold : float
        Activation threshold
        
    Returns:
    --------
    resolvable : ndarray
        Boolean array indicating which coordinates are resolvable
    """
    gradient = compute_entropy_gradient(m1, m2, m3, sigma)
    return np.abs(gradient) > threshold
}


\notes{Now let's run a simulation to demonstrate how observables interact with each other once they become resolvable. We'll start with a system where all coordinates are unresolved and show how they become resolvable and interact with each other.}
\setupcode{import numpy as np
from scipy.optimize import minimize}

\code{# Initial parameters
m1_initial = 0.0
m2_initial = 0.0
m3_initial = 0.0
sigma_initial = 2.0  # Low resolution (high sigma)
sigma_final = 0.1   # High resolution (low sigma)
coupling_initial = 0.0  # No coupling initially
coupling_final = 0.5   # Strong coupling at the end

steps = 50

# Run simulation
m1 = m1_initial
m2 = m2_initial
m3 = m3_initial
sigma = sigma_initial
coupling = coupling_initial

m1_history = np.zeros(steps)
m2_history = np.zeros(steps)
m3_history = np.zeros(steps)
sigma_history = np.zeros(steps)
coupling_history = np.zeros(steps)
resolvable_history = np.zeros((steps, 3), dtype=bool)
fisher_history = np.zeros((steps, 3, 3))

for i in range(steps):
    # Update sigma and coupling
    t = i / (steps - 1)
    sigma = sigma_initial + (sigma_final - sigma_initial) * t
    coupling = coupling_initial + (coupling_final - coupling_initial) * t
    
    # Check resolvability
    resolvable = is_resolvable(m1, m2, m3, sigma)
    
    # Update coordinates based on entropy gradient
    gradient = compute_entropy_gradient(m1, m2, m3, sigma, coupling)
    m1 += 0.1 * gradient[0]
    m2 += 0.1 * gradient[1]
    m3 += 0.1 * gradient[2]
    
    # Compute Fisher information matrix
    fisher = compute_fisher_information(m1, m2, m3, sigma, coupling)
    
    # Store history
    m1_history[i] = m1
    m2_history[i] = m2
    m3_history[i] = m3
    sigma_history[i] = sigma
    coupling_history[i] = coupling
    resolvable_history[i] = resolvable
    fisher_history[i] = fisher
}

\helpercode{def plot_fisher_matrix(ax, fisher, title=None):
    """
    Plot the Fisher information matrix as a heatmap.
    
    Parameters:
    -----------
    ax : matplotlib.axes.Axes
        Axes to plot on
    fisher : ndarray
        3x3 Fisher information matrix
    title : str, optional
        Plot title
    """
    im = ax.imshow(fisher, cmap='viridis')
    ax.set_xticks(np.arange(3))
    ax.set_yticks(np.arange(3))
    ax.set_xticklabels(['$M_1$', '$M_2$', '$M_3$'])
    ax.set_yticklabels(['$M_1$', '$M_2$', '$M_3$'])
    
    # Add text annotations
    for i in range(3):
        for j in range(3):
            text = ax.text(j, i, f'{fisher[i, j]:.2f}',
                          ha='center', va='center', color='w')
    
    if title:
        ax.set_title(title)
    
    plt.colorbar(im, ax=ax, label='Fisher Information')

def plot_interaction_network(ax, fisher, resolvable, title=None):
    """
    Plot the interaction network between observables.
    
    Parameters:
    -----------
    ax : matplotlib.axes.Axes
        Axes to plot on
    fisher : ndarray
        3x3 Fisher information matrix
    resolvable : ndarray
        Boolean array indicating which coordinates are resolvable
    title : str, optional
        Plot title
    """
    # Create a graph with nodes for each observable
    nodes = ['$M_1$', '$M_2$', '$M_3$']
    pos = {0: (0, 0), 1: (1, 0), 2: (0.5, 1)}  # Triangle layout
    
    # Draw nodes
    for i, node in enumerate(nodes):
        if resolvable[i]:
            ax.scatter(pos[i][0], pos[i][1], s=300, color='red', alpha=0.7)
        else:
            ax.scatter(pos[i][0], pos[i][1], s=300, color='gray', alpha=0.3)
        ax.text(pos[i][0], pos[i][1], node, ha='center', va='center', fontsize=12)
    
    # Draw edges with weights based on Fisher information
    for i in range(3):
        for j in range(i+1, 3):
            if fisher[i, j] > 0.01:  # Only draw significant connections
                weight = fisher[i, j] / fisher[i, i]  # Normalize by diagonal
                ax.plot([pos[i][0], pos[j][0]], [pos[i][1], pos[j][1]], 
                       'k-', linewidth=weight*3, alpha=0.7)
                # Add weight label
                mid_x = (pos[i][0] + pos[j][0]) / 2
                mid_y = (pos[i][1] + pos[j][1]) / 2
                ax.text(mid_x, mid_y, f'{weight:.2f}', ha='center', va='center', 
                       fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
    
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    ax.axis('off')
    
    if title:
        ax.set_title(title)
}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{# Plot the results
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Emergence of Interaction Geometry', fontsize=16)

# Plot 1: Initial state (low resolution, no coupling)
plot_fisher_matrix(axes[0, 0], fisher_history[0], 'Initial Fisher Matrix')
plot_interaction_network(axes[0, 1], fisher_history[0], resolvable_history[0], 'Initial Interaction Network')

# Plot 2: Mid state (medium resolution, some coupling)
mid_step = 25
plot_fisher_matrix(axes[1, 0], fisher_history[mid_step], f'Mid Fisher Matrix ($\sigma = {sigma_history[mid_step]:.2f}$)')
plot_interaction_network(axes[1, 1], fisher_history[mid_step], resolvable_history[mid_step], 'Mid Interaction Network')

plt.tight_layout()
mlai.write_figure(filename='interaction-geometry-example-1.svg', 
                  directory='\writeDiagramsDir/information-game')}

\figure{\includediagram{\diagramsDir/information-game/interaction-geometry-example-1}{80%}}{Emergence of interaction geometry between observables.}{interaction-geometry-example-1}

\notes{Let's also plot the final state to see how the interaction geometry has evolved.}

\plotcode{# Plot the final state
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Final Interaction Geometry', fontsize=16)

# Plot 1: Final Fisher matrix
plot_fisher_matrix(axes[0, 0], fisher_history[-1], 'Final Fisher Matrix')
plot_interaction_network(axes[0, 1], fisher_history[-1], resolvable_history[-1], 'Final Interaction Network')

# Plot 2: Evolution of coupling and resolvability
axes[1, 0].plot(sigma_history, coupling_history, 'b-', label='Coupling Strength')
axes[1, 0].set_xlabel('Standard Deviation ($\sigma$)')
axes[1, 0].set_ylabel('Coupling Strength')
axes[1, 0].set_title('Evolution of Coupling')
axes[1, 0].grid(True)
axes[1, 0].legend()

# Plot resolvability history
axes[1, 1].plot(sigma_history, resolvable_history[:, 0], 'r-', label='$M_1$ Resolvable')
axes[1, 1].plot(sigma_history, resolvable_history[:, 1], 'g-', label='$M_2$ Resolvable')
axes[1, 1].plot(sigma_history, resolvable_history[:, 2], 'b-', label='$M_3$ Resolvable')
axes[1, 1].set_xlabel('Standard Deviation (σ)')
axes[1, 1].set_ylabel('Resolvable')
axes[1, 1].set_title('Activation History')
axes[1, 1].grid(True)
axes[1, 1].legend()

plt.tight_layout()
mlai.write_figure(filename='interaction-geometry-example-2.svg', 
                  directory='\writeDiagramsDir/information-game')}

\figure{\includediagram{\diagramsDir/information-game/interaction-geometry-example-2}{80%}}{Final interaction geometry and evolution of coupling and resolvability.}{interaction-geometry-example-2}

\notes{This example demonstrates how observables interact with each other once they become resolvable. In the initial state, all coordinates are unresolved and there is no coupling between them. As resolution increases (sigma decreases), the coordinates become resolvable one by one, and coupling between them emerges.}

\notes{The Fisher information matrix evolves from a diagonal matrix (no coupling) to a matrix with significant off-diagonal terms (strong coupling). This represents the emergence of interaction geometry, where observables become information-bearing not just individually, but in combination.}

\notes{The interaction network visualization shows how the observables are connected to each other, with the thickness of the connections representing the strength of the coupling. As the system evolves, the network becomes more connected, reflecting the emergence of a rich interaction structure.}

\notes{This is a key insight from the information game: as more variables activate, the system develops a network of dependencies between observables, leading to the emergence of more complex dynamics. The Fisher information matrix acts as both memory and mediator, encoding the system's informational shape at every stage.}

\notes{In the next example, we'll explore how this interaction geometry leads to the emergence of classical behavior as the system becomes more complex.}

\endif 
