\ifndef{classicalTransitionExample}
\define{classicalTransitionExample}

\editme

\subsection{Classical Transition Example: From Wave-Like to Classical Behavior}

\notes{Building on the previous examples, we'll now explore how the system transitions from wave-like behavior to classical-like behavior as it becomes more complex. This example demonstrates the emergence of apparent decoherence and classical dynamics without external measurement.}

\notes{In this example, we'll simulate a system with multiple latent coordinates that become resolvable as observables. We'll show how the system transitions from wave-like behavior to classical-like behavior as more variables activate and interact.}

\helpercode{def compute_wavefunction(x, m, sigma):
    """
    Compute the wavefunction for a 1D Gaussian distribution.
    
    Parameters:
    -----------
    x : ndarray
        Position values
    m : float
        Mean value
    sigma : float
        Standard deviation
        
    Returns:
    --------
    psi : ndarray
        Wavefunction values
    """
    return np.exp(-(x - m)**2 / (2 * sigma**2)) / np.sqrt(sigma * np.sqrt(np.pi))

def compute_joint_wavefunction(x, y, m1, m2, sigma, coupling=0.0):
    """
    Compute the joint wavefunction for a 2D Gaussian distribution with coupling.
    
    Parameters:
    -----------
    x, y : ndarray
        Position values
    m1, m2 : float
        Mean values
    sigma : float
        Standard deviation
    coupling : float
        Coupling strength
        
    Returns:
    --------
    psi : ndarray
        Joint wavefunction values
    """
    # For a coupled Gaussian, the wavefunction is a product of Gaussians with correlation
    if coupling == 0:
        return compute_wavefunction(x, m1, sigma) * compute_wavefunction(y, m2, sigma)
    else:
        # Coupled case - more complex wavefunction
        det = 1 - coupling**2
        norm = 1 / np.sqrt(sigma**2 * np.pi * np.sqrt(det))
        return norm * np.exp(-(x - m1)**2 / (2 * sigma**2 * det) - 
                            (y - m2)**2 / (2 * sigma**2 * det) + 
                            coupling * (x - m1) * (y - m2) / (sigma**2 * det))

def compute_classical_trajectory(m1_initial, m2_initial, sigma, coupling, steps=100):
    """
    Compute a classical trajectory for a coupled system.
    
    Parameters:
    -----------
    m1_initial, m2_initial : float
        Initial mean values
    sigma : float
        Standard deviation
    coupling : float
        Coupling strength
    steps : int
        Number of time steps
        
    Returns:
    --------
    m1_history, m2_history : ndarray
        History of mean values
    """
    m1 = m1_initial
    m2 = m2_initial
    
    m1_history = np.zeros(steps)
    m2_history = np.zeros(steps)
    
    # Simple harmonic motion with coupling
    omega1 = 0.1
    omega2 = 0.15
    coupling_strength = 0.05 * coupling
    
    for i in range(steps):
        t = i * 0.1
        
        # Update positions based on coupled harmonic motion
        m1 += omega1 * np.sin(omega1 * t) + coupling_strength * np.sin(omega2 * t)
        m2 += omega2 * np.sin(omega2 * t) + coupling_strength * np.sin(omega1 * t)
        
        m1_history[i] = m1
        m2_history[i] = m2
    
    return m1_history, m2_history
}

\notes{Now let's run a simulation to demonstrate the transition from wave-like to classical behavior. We'll start with a system where the coordinates are governed by a wave-like equation and show how they transition to classical-like behavior as more variables activate and interact.}


\setupcode{import numpy as np
from scipy.optimize import minimize}

\code{# Create position grids
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Initial parameters
m1_initial = 0.0
m2_initial = 0.0
sigma_initial = 2.0  # Low resolution (high sigma)
sigma_final = 0.5   # High resolution (low sigma)
coupling_initial = 0.0  # No coupling initially
coupling_final = 0.7   # Strong coupling at the end

steps = 50

# Run simulation
m1 = m1_initial
m2 = m2_initial
sigma = sigma_initial
coupling = coupling_initial

m1_history = np.zeros(steps)
m2_history = np.zeros(steps)
sigma_history = np.zeros(steps)
coupling_history = np.zeros(steps)

# Compute classical trajectory
classical_m1_history, classical_m2_history = compute_classical_trajectory(
    m1_initial, m2_initial, sigma_final, coupling_final)

for i in range(steps):
    # Update sigma and coupling
    t = i / (steps - 1)
    sigma = sigma_initial + (sigma_final - sigma_initial) * t
    coupling = coupling_initial + (coupling_final - coupling_initial) * t
    
    # Update coordinates based on classical trajectory
    if i < len(classical_m1_history):
        m1 = classical_m1_history[i]
        m2 = classical_m2_history[i]
    else:
        # If we run out of classical trajectory, just use the last value
        m1 = classical_m1_history[-1]
        m2 = classical_m2_history[-1]
    
    # Store history
    m1_history[i] = m1
    m2_history[i] = m2
    sigma_history[i] = sigma
    coupling_history[i] = coupling
}


\helpercode{def plot_wavefunction(ax, x, y, psi, title=None):
    """
    Plot the wavefunction as a 2D heatmap.
    
    Parameters:
    -----------
    ax : matplotlib.axes.Axes
        Axes to plot on
    x, y : ndarray
        Position values
    psi : ndarray
        Wavefunction values
    title : str, optional
        Plot title
    """
    im = ax.imshow(psi, extent=[x.min(), x.max(), y.min(), y.max()], 
                  origin='lower', cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    if title:
        ax.set_title(title)
    
    plt.colorbar(im, ax=ax, label='|ψ|²')

def plot_classical_trajectory(ax, m1_history, m2_history, title=None):
    """
    Plot the classical trajectory.
    
    Parameters:
    -----------
    ax : matplotlib.axes.Axes
        Axes to plot on
    m1_history, m2_history : ndarray
        History of mean values
    title : str, optional
        Plot title
    """
    ax.plot(m1_history, m2_history, 'r-', linewidth=2)
    ax.scatter(m1_history[0], m2_history[0], color='green', s=100, label='Start')
    ax.scatter(m1_history[-1], m2_history[-1], color='red', s=100, label='End')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    ax.legend()
    
    if title:
        ax.set_title(title)
}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{
# Plot the results
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Transition from Wave-Like to Classical Behavior', fontsize=16)

# Plot 1: Initial wavefunction (low resolution, no coupling)
psi_initial = compute_joint_wavefunction(X, Y, m1_initial, m2_initial, sigma_initial, coupling_initial)
plot_wavefunction(axes[0, 0], x, y, psi_initial, 'Initial Wavefunction')

# Plot 2: Mid wavefunction (medium resolution, some coupling)
mid_step = 25
psi_mid = compute_joint_wavefunction(X, Y, m1_history[mid_step], m2_history[mid_step], 
                                    sigma_history[mid_step], coupling_history[mid_step])
plot_wavefunction(axes[0, 1], x, y, psi_mid, f'Mid Wavefunction (σ = {sigma_history[mid_step]:.2f})')

# Plot 3: Final wavefunction (high resolution, strong coupling)
psi_final = compute_joint_wavefunction(X, Y, m1_history[-1], m2_history[-1], 
                                      sigma_history[-1], coupling_history[-1])
plot_wavefunction(axes[1, 0], x, y, psi_final, 'Final Wavefunction')

# Plot 4: Classical trajectory
plot_classical_trajectory(axes[1, 1], classical_m1_history, classical_m2_history, 'Classical Trajectory')

plt.tight_layout()
mlai.write_figure(filename='classical-transition-example-1.svg', 
                  directory='\writeDiagramsDir/information-game')}

\figure{\includediagram{\diagramsDir/information-game/classical-transition-example-1}{80%}}{Transition from wave-like to classical behavior.}{classical-transition-example-1}

\notes{Let's also plot the evolution of the system over time to see how it transitions from wave-like to classical behavior.}

\plotcode{# Plot the evolution of the system
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Evolution of System Behavior', fontsize=16)

# Plot 1: Evolution of sigma (resolution)
axes[0, 0].plot(range(len(sigma_history)), sigma_history, 'b-', label='σ')
axes[0, 0].set_xlabel('Time Step')
axes[0, 0].set_ylabel('Standard Deviation ($\sigma$)')
axes[0, 0].set_title('Evolution of Resolution')
axes[0, 0].grid(True)
axes[0, 0].legend()

# Plot 2: Evolution of coupling
axes[0, 1].plot(range(len(coupling_history)), coupling_history, 'r-', label='Coupling')
axes[0, 1].set_xlabel('Time Step')
axes[0, 1].set_ylabel('Coupling Strength')
axes[0, 1].set_title('Evolution of Coupling')
axes[0, 1].grid(True)
axes[0, 1].legend()

# Plot 3: Evolution of m1
axes[1, 0].plot(range(len(m1_history)), m1_history, 'g-', label='$m_1$')
axes[1, 0].plot(range(len(classical_m1_history)), classical_m1_history, 'k--', label='Classical $m_1$')
axes[1, 0].set_xlabel('Time Step')
axes[1, 0].set_ylabel('$m_1$')
axes[1, 0].set_title('Evolution of $m_1$')
axes[1, 0].grid(True)
axes[1, 0].legend()

# Plot 4: Evolution of m2
axes[1, 1].plot(range(len(m2_history)), m2_history, 'g-', label='$m_2$')
axes[1, 1].plot(range(len(classical_m2_history)), classical_m2_history, 'k--', label='Classical $m_2$')
axes[1, 1].set_xlabel('Time Step')
axes[1, 1].set_ylabel('$m_2$')
axes[1, 1].set_title('Evolution of $m_2$')
axes[1, 1].grid(True)
axes[1, 1].legend()

plt.tight_layout()
mlai.write_figure(filename='classical-transition-example-2.svg', 
                  directory='\writeDiagramsDir/information-game')}

\figure{\includediagram{\diagramsDir/information-game/classical-transition-example-2}{80%}}{Evolution of system behavior from wave-like to classical.}{classical-transition-example-2}

\notes{This example demonstrates how the system transitions from wave-like behavior to classical-like behavior as it becomes more complex. In the initial state, the system is governed by a wave-like equation, with a broad, symmetric wavefunction. As resolution increases (sigma decreases) and coupling emerges, the wavefunction becomes more localized and structured.}

\notes{The classical trajectory shows how the system behaves in the classical regime, following a deterministic path through phase space. This is a key insight from the information game: as the system becomes more complex, it transitions from wave-dominated evolution to a dynamics of coarse constraints and informational inertia.}

\notes{The evolution plots show how the system's behavior changes over time. As resolution increases and coupling emerges, the system's dynamics become more classical-like, with the mean values following a deterministic trajectory. This is reminiscent of the emergence of classical behavior from quantum mechanics, but here it arises naturally from the information geometry of the system.}

\notes{This is a profound insight: classical behavior can emerge naturally from information geometry, without needing to postulate physical laws or external measurement. The system's own complexity creates the conditions for classical behavior, with the Fisher information matrix encoding both the current geometry and the system's history.}

\notes{In summary, we've traced a full arc from latent coordinates to classical behavior:

1. Latent regime: a symmetric, curvature-minimised wave equation governs the silent geometry of $M$-space.
2. Variable activation: entropy gradient breaks symmetry; directions become resolvable, and wave equations reappear — now active.
3. Interaction onset: new directions activate; wavefunctions couple; the Fisher matrix acquires off-diagonal structure; locality and joint dynamics emerge.
4. Layered interaction: subsystems form, interactions propagate, and a network of informational flow develops.
5. Classical regime: entropy dominates; interference fades; wave structure gives way to ensemble dynamics governed by effective constraints.}

\notes{Through this progression, the system evolves from an unstructured entropy minimum to a coarse but stable configuration governed by emergent geometry. What began as a game of curvature ends as a self-organised system with behaviour that mimics the laws of classical motion.}

\endif 
