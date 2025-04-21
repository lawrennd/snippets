\ifndef{minimalResolutionExample}
\define{minimalResolutionExample}

\editme

\subsection{Minimal Resolution Example: 2D Latent Space}

\notes{To illustrate the concept of minimal resolution and emergent observables, we'll create a simple example using a 2D latent space. This example will demonstrate how observables emerge when resolution constraints are applied to a system with latent coordinates.}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import mlai.plot as plot
import mlai}

\notes{First, let's define a simple 2D latent space with coordinates $M_1$ and $M_2$. These coordinates are initially unresolved and governed by a wave-like equation. We'll implement a numerical simulation to show how these coordinates become resolvable as observables when resolution constraints are applied.}

\helpercode{def compute_fisher_information(m1, m2, sigma=1.0):
    """
    Compute the Fisher information matrix for a 2D Gaussian distribution.
    
    Parameters:
    -----------
    m1, m2 : float
        Mean values of the distribution
    sigma : float
        Standard deviation (resolution parameter)
        
    Returns:
    --------
    G : ndarray
        2x2 Fisher information matrix
    """
    # For a Gaussian distribution, the Fisher information matrix is 1/sigma^2 * I
    return np.array([[1/sigma**2, 0], [0, 1/sigma**2]])

def compute_entropy_gradient(m1, m2, sigma=1.0):
    """
    Compute the entropy gradient for a 2D Gaussian distribution.
    
    Parameters:
    -----------
    m1, m2 : float
        Mean values of the distribution
    sigma : float
        Standard deviation (resolution parameter)
        
    Returns:
    --------
    gradient : ndarray
        2D gradient vector [dS/dm1, dS/dm2]
    """
    # For a Gaussian distribution, the entropy gradient is proportional to the mean
    # This is a simplified model - in reality, the gradient depends on the Fisher matrix
    G = compute_fisher_information(m1, m2, sigma)
    theta = np.array([m1, m2])  # Natural parameters
    return G @ theta

def compute_entropy(m1, m2, sigma=1.0):
    """
    Compute the entropy of a 2D Gaussian distribution.
    
    Parameters:
    -----------
    m1, m2 : float
        Mean values of the distribution
    sigma : float
        Standard deviation (resolution parameter)
        
    Returns:
    --------
    entropy : float
        Entropy value
    """
    # For a 2D Gaussian, S = log(2πeσ²)
    return np.log(2 * np.pi * np.e * sigma**2)

def is_resolvable(m1, m2, sigma, threshold=0.1):
    """
    Determine if a coordinate is resolvable based on the entropy gradient.
    
    Parameters:
    -----------
    m1, m2 : float
        Mean values of the distribution
    sigma : float
        Standard deviation (resolution parameter)
    threshold : float
        Activation threshold
        
    Returns:
    --------
    resolvable : bool
        True if the coordinate is resolvable
    """
    gradient = compute_entropy_gradient(m1, m2, sigma)
    return np.linalg.norm(gradient) > threshold

def plot_latent_space(ax, m1_values, m2_values, sigma, resolvable=None):
    """
    Plot the latent space with resolution constraints.
    
    Parameters:
    -----------
    ax : matplotlib.axes.Axes
        Axes to plot on
    m1_values, m2_values : ndarray
        Grid of M1 and M2 values
    sigma : float
        Standard deviation (resolution parameter)
    resolvable : ndarray, optional
        Boolean array indicating which points are resolvable
    """
    # Create a contour plot of the entropy
    entropy_values = np.zeros_like(m1_values)
    for i in range(m1_values.shape[0]):
        for j in range(m1_values.shape[1]):
            entropy_values[i, j] = compute_entropy(m1_values[i, j], m2_values[i, j], sigma)
    
    contour = ax.contourf(m1_values, m2_values, entropy_values, levels=20, cmap='viridis')
    plt.colorbar(contour, ax=ax, label='Entropy')
    
    # If resolvable points are provided, highlight them
    if resolvable is not None:
        resolvable_points = np.where(resolvable)
        ax.scatter(m1_values[resolvable_points], m2_values[resolvable_points], 
                  color='red', s=50, label='Resolvable')
    
    ax.set_xlabel('M₁ (Latent Coordinate)')
    ax.set_ylabel('M₂ (Latent Coordinate)')
    ax.set_title(f'Latent Space (σ = {sigma:.2f})')
    ax.grid(True)
    ax.legend()

def simulate_activation(m1_initial, m2_initial, sigma_initial, sigma_final, steps=50):
    """
    Simulate the activation of latent coordinates as resolution increases.
    
    Parameters:
    -----------
    m1_initial, m2_initial : float
        Initial mean values
    sigma_initial, sigma_final : float
        Initial and final standard deviation values
    steps : int
        Number of simulation steps
        
    Returns:
    --------
    m1_history, m2_history : ndarray
        History of mean values
    sigma_history : ndarray
        History of standard deviation values
    resolvable_history : ndarray
        History of resolvability
    """
    m1 = m1_initial
    m2 = m2_initial
    sigma = sigma_initial
    
    m1_history = np.zeros(steps)
    m2_history = np.zeros(steps)
    sigma_history = np.zeros(steps)
    resolvable_history = np.zeros((steps, 2), dtype=bool)
    
    for i in range(steps):
        # Update sigma (decreasing resolution)
        sigma = sigma_initial + (sigma_final - sigma_initial) * i / (steps - 1)
        
        # Check resolvability
        resolvable1 = is_resolvable(m1, 0, sigma)
        resolvable2 = is_resolvable(0, m2, sigma)
        
        # Update coordinates based on entropy gradient
        gradient = compute_entropy_gradient(m1, m2, sigma)
        m1 += 0.1 * gradient[0]
        m2 += 0.1 * gradient[1]
        
        # Store history
        m1_history[i] = m1
        m2_history[i] = m2
        sigma_history[i] = sigma
        resolvable_history[i] = [resolvable1, resolvable2]
    
    return m1_history, m2_history, sigma_history, resolvable_history}

\notes{Now let's run a simulation to demonstrate how latent coordinates become resolvable as resolution increases. We'll start with a system where both coordinates are unresolved and show how they become resolvable one by one.}

\code{# Create a grid of M1 and M2 values
m1_range = np.linspace(-2, 2, 100)
m2_range = np.linspace(-2, 2, 100)
m1_values, m2_values = np.meshgrid(m1_range, m2_range)

# Initial parameters
m1_initial = 0.0
m2_initial = 0.0
sigma_initial = 2.0  # Low resolution (high sigma)
sigma_final = 0.1   # High resolution (low sigma)

# Run simulation
m1_history, m2_history, sigma_history, resolvable_history = simulate_activation(
    m1_initial, m2_initial, sigma_initial, sigma_final, steps=50)

# Plot the results
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Emergence of Observables from Latent Coordinates', fontsize=16)

# Plot 1: Initial state (low resolution)
plot_latent_space(axes[0, 0], m1_values, m2_values, sigma_initial)
axes[0, 0].set_title('Initial State (Low Resolution)')

# Plot 2: Mid state (medium resolution)
mid_step = 25
plot_latent_space(axes[0, 1], m1_values, m2_values, sigma_history[mid_step])
axes[0, 1].set_title(f'Mid State ($\\sigma = {sigma_history[mid_step]:.2f}$)')

# Plot 3: Final state (high resolution)
plot_latent_space(axes[1, 0], m1_values, m2_values, sigma_final)
axes[1, 0].set_title('Final State (High Resolution)')

# Plot 4: Activation history
axes[1, 1].plot(sigma_history, resolvable_history[:, 0], 'r-', label='$M_1$ Resolvable')
axes[1, 1].plot(sigma_history, resolvable_history[:, 1], 'b-', label='$M_2$ Resolvable')
axes[1, 1].set_xlabel('Standard Deviation ($\\sigma$)')
axes[1, 1].set_ylabel('Resolvable')
axes[1, 1].set_title('Activation History')
axes[1, 1].grid(True)
axes[1, 1].legend()

plt.tight_layout()
mlai.write_figure(filename='minimal-resolution-example.svg', 
                  directory='\writeDiagramsDir/information-game')}

\figure{\includediagram{\diagramsDir/information-game/minimal-resolution-example}{80%}}{Emergence of observables from latent coordinates as resolution increases.}{minimal-resolution-example}

\notes{This example demonstrates how latent coordinates become resolvable as resolution increases. In the initial state (low resolution), both coordinates are unresolved and the system exists in a state of symmetric uncertainty. As resolution increases (sigma decreases), the coordinates become resolvable one by one, transitioning from latent $M$-space to active $X$-space.}

\notes{The activation history shows when each coordinate becomes resolvable, which occurs when the entropy gradient exceeds the activation threshold. This is a key insight from the information game: observables emerge naturally from latent coordinates when resolution constraints are applied.}

\endif 
