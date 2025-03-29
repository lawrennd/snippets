\ifndef{gradientAscentUncertainty}
\define{gradientAscentUncertainty}

\editme

\subsection{Gradient Ascent on Entropy with Uncertainty Constraints}

\notes{As an example we perform gradient ascent starting with a minimal entropy state. This allows us to explore the saddle-point seeking behaviour of steepest ascent empirically.}

\slides{
* Entropy increases while respecting uncertainty constraints
* Reveals transition from quantum-like to classical-like behavior
* Implemented through gradient ascent on covariance eigenvalues
}

\notes{The minimal entropy states represent the origin point. By implementing gradient ascent on the entropy function while respecting the uncertainty constraints, we can observe how the entropy game evolves.}


\helpercode{# Compute entropy of a Gaussian with precision matrix Lambda
def compute_entropy(Lambda):
    """
    Compute entropy of a Gaussian with precision matrix Lambda.
    
    Parameters:
    -----------
    Lambda: array
        Precision matrix (inverse covariance)
    
    Returns:
    --------
    entropy: float
        Differential entropy value
    """
    n = Lambda.shape[0]  # Dimensionality
    covariance = np.linalg.inv(Lambda)
    return 0.5 * (n * (1 + np.log(2*np.pi)) + np.log(np.linalg.det(covariance)))

# Compute gradient of entropy with respect to eigenvalues
def entropy_gradient(eigenvalues):
    """
    Compute gradient of entropy with respect to eigenvalues of precision matrix.
    
    Parameters:
    -----------
    eigenvalues: array
        Eigenvalues of precision matrix Lambda
    
    Returns:
    --------
    gradient: array
        Gradient of entropy with respect to each eigenvalue
    """
    # For a Gaussian, gradient of entropy with respect to precision eigenvalue is -1/(2*eigenvalue)
    return -1.0 / (2.0 * eigenvalues)

# Project gradient to respect uncertainty constraints
def project_gradient(eigenvalues, gradient):
    """
    Project gradient to ensure uncertainty constraints are respected.
    
    Parameters:
    -----------
    eigenvalues: array
        Current eigenvalues of precision matrix
    gradient: array
        Raw gradient of entropy with respect to eigenvalues
    
    Returns:
    --------
    projected_gradient: array
        Gradient projected to respect constraints
    """
    n = len(eigenvalues) // 2
    projected_gradient = gradient.copy()
    
    # For each conjugate pair of variables
    for i in range(n):
        idx1, idx2 = 2*i, 2*i+1
        
        # Current uncertainty product (in eigenvalue space, this is inverse)
        current_product = eigenvalues[idx1] * eigenvalues[idx2]
        
        # If we're already at minimum uncertainty, project gradient to maintain this
        if abs(current_product - 1/min_uncertainty_product**2) < 1e-6:
            # Tangent direction preserves the product
            tangent = np.array([-eigenvalues[idx2], -eigenvalues[idx1]])
            tangent = tangent / np.linalg.norm(tangent)
            
            # Project the gradient onto this tangent
            pair_gradient = np.array([gradient[idx1], gradient[idx2]])
            projection = np.dot(pair_gradient, tangent) * tangent
            
            projected_gradient[idx1] = projection[0]
            projected_gradient[idx2] = projection[1]
    
    return projected_gradient

# Initialize a multidimensional minimal entropy state
def initialize_multidimensional_state(n_pairs, squeeze_factors=None):
    """
    Create a minimal entropy state for multiple position-momentum pairs.
    
    Parameters:
    -----------
    n_pairs: int
        Number of position-momentum pairs
    squeeze_factors: list, optional
        Squeeze factors for each pair (how asymmetric the uncertainty is)
        
    Returns:
    --------
    Lambda: 2n×2n array
        Initial precision matrix
    """
    if squeeze_factors is None:
        # Default: different squeeze factors for each pair
        squeeze_factors = [0.1 * (i+1) for i in range(n_pairs)]
    
    # Initialize precision matrix
    dim = 2 * n_pairs
    Lambda = np.zeros((dim, dim))
    
    # For each position-momentum pair
    for i in range(n_pairs):
        idx1, idx2 = 2*i, 2*i+1
        
        # Set precision for position (high precision = low uncertainty)
        Lambda[idx1, idx1] = 1.0 / (squeeze_factors[i] * min_uncertainty_product)
        
        # Set precision for momentum (low precision = high uncertainty)
        Lambda[idx2, idx2] = 1.0 / (min_uncertainty_product / squeeze_factors[i])
    
    return Lambda

# Perform gradient ascent on entropy
def gradient_ascent(Lambda_init, steps=100, learning_rate=0.01):
    """
    Perform gradient ascent on entropy while respecting uncertainty constraints.
    
    Parameters:
    -----------
    Lambda_init: array
        Initial precision matrix
    steps: int
        Number of gradient steps to take
    learning_rate: float
        Step size for gradient ascent
    
    Returns:
    --------
    Lambda_history: list
        History of precision matrices
    entropy_history: list
        History of entropy values
    """
    Lambda = Lambda_init.copy()
    Lambda_history = [Lambda.copy()]
    entropy_history = [compute_entropy(Lambda)]
    
    for _ in range(steps):
        # Eigendecomposition of Lambda
        eigenvalues, eigenvectors = eigh(Lambda)
        
        # Compute gradient with respect to eigenvalues
        grad = entropy_gradient(eigenvalues)
        
        # Project gradient to respect constraints
        proj_grad = project_gradient(eigenvalues, grad)
        
        # Update eigenvalues
        eigenvalues += learning_rate * proj_grad
        
        # Ensure eigenvalues remain positive
        eigenvalues = np.maximum(eigenvalues, 1e-10)
        
        # Reconstruct Lambda from updated eigenvalues
        Lambda = eigenvectors @ np.diag(eigenvalues) @ eigenvectors.T
        
        # Store history
        Lambda_history.append(Lambda.copy())
        entropy_history.append(compute_entropy(Lambda))
    
    return Lambda_history, entropy_history

# Track uncertainty products and regime classification
def track_uncertainty_metrics(Lambda_history):
    """
    Track uncertainty products and classify regimes for each conjugate pair.
    
    Parameters:
    -----------
    Lambda_history: list
        History of precision matrices
    
    Returns:
    --------
    metrics: dict
        Dictionary containing uncertainty metrics over time
    """
    n_steps = len(Lambda_history)
    n_pairs = Lambda_history[0].shape[0] // 2
    
    # Initialize tracking arrays
    uncertainty_products = np.zeros((n_steps, n_pairs))
    regimes = np.zeros((n_steps, n_pairs), dtype=object)
    
    for step, Lambda in enumerate(Lambda_history):
        # Get covariance matrix
        V = np.linalg.inv(Lambda)
        
        # Calculate Fisher information matrix
        G = Lambda / 2
        
        # For each conjugate pair
        for i in range(n_pairs):
            # Extract 2x2 submatrix for this pair
            idx1, idx2 = 2*i, 2*i+1
            V_sub = V[np.ix_([idx1, idx2], [idx1, idx2])]
            
            # Compute uncertainty product (determinant of submatrix)
            uncertainty_product = np.sqrt(np.linalg.det(V_sub))
            uncertainty_products[step, i] = uncertainty_product
            
            # Classify regime
            if abs(uncertainty_product - min_uncertainty_product) < 0.1*min_uncertainty_product:
                regimes[step, i] = "Quantum-like"
            else:
                regimes[step, i] = "Classical-like"
    
    return {
        'uncertainty_products': uncertainty_products,
        'regimes': regimes
    }

# Detect saddle points in the gradient flow
def detect_saddle_points(Lambda_history):
    """
    Detect saddle-like behavior in the gradient flow.
    
    Parameters:
    -----------
    Lambda_history: list
        History of precision matrices
    
    Returns:
    --------
    saddle_metrics: dict
        Metrics related to saddle point behavior
    """
    n_steps = len(Lambda_history)
    n_pairs = Lambda_history[0].shape[0] // 2
    
    # Track eigenvalues and their gradients
    eigenvalues_history = np.zeros((n_steps, 2*n_pairs))
    gradient_ratios = np.zeros((n_steps, n_pairs))
    
    for step, Lambda in enumerate(Lambda_history):
        # Get eigenvalues
        eigenvalues, _ = eigh(Lambda)
        eigenvalues_history[step] = eigenvalues
        
        # For each pair, compute ratio of gradients
        if step > 0:
            for i in range(n_pairs):
                idx1, idx2 = 2*i, 2*i+1
                
                # Change in eigenvalues
                delta1 = abs(eigenvalues_history[step, idx1] - eigenvalues_history[step-1, idx1])
                delta2 = abs(eigenvalues_history[step, idx2] - eigenvalues_history[step-1, idx2])
                
                # Ratio of max to min (high ratio indicates saddle-like behavior)
                max_delta = max(delta1, delta2)
                min_delta = max(1e-10, min(delta1, delta2))  # Avoid division by zero
                gradient_ratios[step, i] = max_delta / min_delta
    
    # Identify candidate saddle points (where some gradients are much larger than others)
    saddle_candidates = []
    for step in range(1, n_steps):
        if np.any(gradient_ratios[step] > 10):  # Threshold for saddle-like behavior
            saddle_candidates.append(step)
    
    return {
        'eigenvalues_history': eigenvalues_history,
        'gradient_ratios': gradient_ratios,
        'saddle_candidates': saddle_candidates
    }

# Visualize uncertainty ellipses for multiple pairs
def plot_multidimensional_uncertainty(Lambda_history, step_indices, pairs_to_plot=None):
    """
    Plot the evolution of uncertainty ellipses for multiple position-momentum pairs.
    
    Parameters:
    -----------
    Lambda_history: list
        History of precision matrices
    step_indices: list
        Indices of steps to visualize
    pairs_to_plot: list, optional
        Indices of position-momentum pairs to plot
    """
    n_pairs = Lambda_history[0].shape[0] // 2
    
    if pairs_to_plot is None:
        pairs_to_plot = range(min(3, n_pairs))  # Plot up to 3 pairs by default
    
    fig, axes = plt.subplots(len(pairs_to_plot), len(step_indices), 
                            figsize=(4*len(step_indices), 3*len(pairs_to_plot)))
    
    # Handle case of single pair or single step
    if len(pairs_to_plot) == 1:
        axes = axes.reshape(1, -1)
    if len(step_indices) == 1:
        axes = axes.reshape(-1, 1)
    
    for row, pair_idx in enumerate(pairs_to_plot):
        for col, step in enumerate(step_indices):
            ax = axes[row, col]
            Lambda = Lambda_history[step]
            covariance = np.linalg.inv(Lambda)
            
            # Extract 2x2 submatrix for this pair
            idx1, idx2 = 2*pair_idx, 2*pair_idx+1
            cov_sub = covariance[np.ix_([idx1, idx2], [idx1, idx2])]
            
            # Get eigenvalues and eigenvectors of submatrix
            values, vectors = eigh(cov_sub)
            
            # Calculate ellipse parameters
            angle = np.degrees(np.arctan2(vectors[1, 0], vectors[0, 0]))
            width, height = 2 * np.sqrt(values)
            
            # Create ellipse
            ellipse = Ellipse((0, 0), width=width, height=height, angle=angle,
                             edgecolor='blue', facecolor='lightblue', alpha=0.5)
            
            # Add to plot
            ax.add_patch(ellipse)
            ax.set_xlim(-3, 3)
            ax.set_ylim(-3, 3)
            ax.set_aspect('equal')
            ax.grid(True)
            
            # Add minimum uncertainty circle
            min_circle = plt.Circle((0, 0), min_uncertainty_product, 
                                   fill=False, color='red', linestyle='--')
            ax.add_patch(min_circle)
            
            # Compute uncertainty product
            uncertainty_product = np.sqrt(np.linalg.det(cov_sub))
            
            # Determine regime
            if abs(uncertainty_product - min_uncertainty_product) < 0.1*min_uncertainty_product:
                regime = "Quantum-like"
                color = 'red'
            else:
                regime = "Classical-like"
                color = 'blue'
            
            # Add labels
            if row == 0:
                ax.set_title(f"Step {step}")
            if col == 0:
                ax.set_ylabel(f"Pair {pair_idx+1}")
            
            # Add uncertainty product text
            ax.text(0.05, 0.95, f"ΔxΔp = {uncertainty_product:.2f}",
                   transform=ax.transAxes, fontsize=10, verticalalignment='top')
            
            # Add regime text
            ax.text(0.05, 0.85, regime, transform=ax.transAxes, 
                   fontsize=10, verticalalignment='top', color=color)
            
            ax.set_xlabel("Position")
            ax.set_ylabel("Momentum")
    
    plt.tight_layout()
    return fig}

\notes{As the system evolves through gradient ascent, we observe transitions.

1. *Uncertainty desaturation*: The system begins with a minimal entropy state that exactly saturates the uncertainty bound ($\Delta x \cdot \Delta p = \hbar/2$). As entropy increases, this bound becomes less tightly saturated.

2. *Shape transformation*: The initial highly squeezed uncertainty ellipse (with small position uncertainty and large momentum uncertainty) gradually becomes more circular, representing a more balanced distribution of uncertainty.

3. *Quantum-to-classical transition*: The system transitions from a quantum-like regime (where uncertainty is at the minimum allowed by quantum mechanics) to a more classical-like regime (where statistical uncertainty dominates over quantum uncertainty).}

\notes{This evolution reveals how information naturally flows from highly ordered configurations toward maximum entropy states, while still respecting the fundamental constraints imposed by the uncertainty principle.}

\newslide{Multivariate Systems and Saddle Points}

\slides{
* Multiple position-momentum pairs create rich dynamics
* System naturally slows near saddle points
* Some variables remain quantum-like while others become classical-like
}

\notes{In systems with multiple position-momentum pairs, the gradient ascent process encounters saddle points which trigger a natural slowdown. The system naturally slows down near saddle points, with some eigenvalue pairs evolving quickly while others hardly change. These saddle points represent partially equilibrated states where some degrees of freedom have reached maximum entropy while others remain ordered. At these critical points, some variables maintain quantum-like characteristics (uncertainty saturation) while others exhibit classical-like behavior (excess uncertainty).}

\notes{This natural separation creates a hybrid system where quantum-like memory interfaces with classical-like processing - emerging naturally from the geometry of the entropy landscape under uncertainty constraints.}

\setupcode{import numpy as np
from scipy.linalg import eigh}

\code{# Constants
hbar = 1.0  # Normalized Planck's constant
min_uncertainty_product = hbar/2

# Example usage for multidimensional system
# Initialize a system with 3 position-momentum pairs
n_pairs = 3
Lambda_init = initialize_multidimensional_state(n_pairs, squeeze_factors=[0.1, 0.2, 0.3])

# Perform gradient ascent
Lambda_history, entropy_history = gradient_ascent(Lambda_init, steps=100, learning_rate=0.01)

# Track uncertainty metrics
metrics = track_uncertainty_metrics(Lambda_history)

# Detect saddle points
saddle_metrics = detect_saddle_points(Lambda_history)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai
from matplotlib.patches import Ellipse}

\plotcode{# Plot uncertainty ellipses at different steps
plot_multidimensional_uncertainty(Lambda_history, step_indices=[0, 25, 50, 99], pairs_to_plot=[0, 1, 2])

# Plot entropy evolution
plt.figure(figsize=plot.big_wide_figsize)
plt.plot(entropy_history)
plt.xlabel('Gradient Ascent Step')
plt.ylabel('Entropy')
plt.title('Entropy Evolution During Gradient Ascent')
plt.grid(True)
mlai.write_figure(filename='entropy-evolution-during-gradient-ascent.svg', 
                  directory='./information-game')}

# Plot uncertainty products evolution
plt.figure(figsize=plot.big_wide_figsize)
for i in range(n_pairs):
    plt.plot(metrics['uncertainty_products'][:, i], label=f'Pair {i+1}')
plt.axhline(y=min_uncertainty_product, color='k', linestyle='--', label='Minimum uncertainty')
plt.xlabel('Gradient Ascent Step')
plt.ylabel('Uncertainty Product (ΔxΔp)')
plt.title('Evolution of Uncertainty Products')
plt.legend()
plt.grid(True)

mlai.write_figure(filename='uncertainty-products-evolution.svg', 
                  directory='./information-game')}

\newslide{Entropy Evolution During Gradient Ascent}

\figure{\includediagram{\diagramsDir/information-game/entropy-evolution-during-gradient-ascent}{70%}}{.}{entropy-evolution-during-gradient-ascent}

\newslide{Evolution of Uncertainty Products}

\figure{\includediagram{\diagramsDir/information-game/uncertainty-products-evolution}{70%}}{.}{uncertainty-products-evolution}

\notes{The gradient ascent approach provides a powerful framework for understanding how systems naturally evolve from minimal entropy states toward maximum entropy while respecting fundamental constraints. This perspective unifies quantum uncertainty with classical information theory through the common language of information geometry.}

\notes{In multidimensional systems, we observe the emergence of natural hierarchies and timescales. Some degrees of freedom quickly reach equilibrium (maximum entropy configurations) while others remain ordered for much longer periods. This separation of timescales creates a rich landscape of partially equilibrated states that may play important roles in information processing systems.}

\notes{The saddle points in this landscape represent configurations where the system naturally pauses during its evolution. These quasi-stable states exhibit hybrid behavior, with some variables maintaining quantum-like characteristics while others behave more classically.}

\endif 
