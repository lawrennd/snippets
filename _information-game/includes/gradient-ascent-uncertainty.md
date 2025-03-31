\ifndef{gradientAscentUncertainty}
\define{gradientAscentUncertainty}

\editme

\subsection{Gradient Ascent and Uncertainty Principles}

\notes{In our exploration of information dynamics, we now turn to the relationship between gradient ascent on entropy and uncertainty principles. This section demonstrates how systems naturally evolve from quantum-like states (with minimal uncertainty) toward classical-like states (with excess uncertainty) through entropy maximization.}

\slides{
* Gradient ascent on entropy naturally respects uncertainty principles
* Systems evolve from quantum-like to classical-like regimes
* Uncertainty ellipses visualize this transition
}

\newslide{Gaussian Systems and Uncertainty}

\notes{
For simplicity, we'll focus on multivariate Gaussian distributions, where the uncertainty relationships are particularly elegant. In this setting, the precision matrix $\Lambda$ (inverse of the covariance matrix) fully characterizes the distribution. The entropy of a multivariate Gaussian is directly related to the determinant of the covariance matrix,
$$
S = \frac{1}{2}\log\det(V) + \text{constant},
$$
where $V = \Lambda^{-1}$ is the covariance matrix.

For conjugate variables like position and momentum, the Heisenberg uncertainty principle imposes constraints on the minimum product of their uncertainties. In our information-theoretic framework, this appears as a constraint on the determinant of certain submatrices of the covariance matrix.
}

\slides{
* Multivariate Gaussian: $\rho(z) \propto \exp\left(-\frac{1}{2}z^T \Lambda z\right)$
* Precision matrix $\Lambda$ determines uncertainty structure
* Entropy: $S = \frac{1}{2}\log\det(V) + \text{constant}$
* Uncertainty principle: $\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$
}

\setupcode{import numpy as np
from scipy.linalg import eigh
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse}

\notes{
The code below implements gradient ascent on the entropy of a multivariate Gaussian system while respecting uncertainty constraints. We'll track how the system evolves from minimal uncertainty states (quantum-like) to states with excess uncertainty (classical-like).

First, we define key functions for computing entropy and its gradient.
}

\code{
# Constants
hbar = 1.0  # Normalized Planck's constant
min_uncertainty_product = hbar/2}


\helpercode{# Compute entropy of a multivariate Gaussian with precision matrix Lambda
def compute_entropy(Lambda):
    """
    Compute entropy of multivariate Gaussian with precision matrix Lambda.
    
    Parameters:
    -----------
    Lambda: array
        Precision matrix
    
    Returns:
    --------
    entropy: float
        Entropy value
    """
    # Covariance matrix is inverse of precision matrix
    V = np.linalg.inv(Lambda)
    
    # Entropy formula for multivariate Gaussian
    n = Lambda.shape[0]
    entropy = 0.5 * np.log(np.linalg.det(V)) + 0.5 * n * (1 + np.log(2*np.pi))
    
    return entropy

# Compute gradient of entropy with respect to precision matrix
def compute_entropy_gradient(Lambda):
    """
    Compute gradient of entropy with respect to precision matrix.
    
    Parameters:
    -----------
    Lambda: array
        Precision matrix
    
    Returns:
    --------
    gradient: array
        Gradient of entropy
    """
    # Gradient is -0.5 * inverse of Lambda
    V = np.linalg.inv(Lambda)
    gradient = -0.5 * V
    
    return gradient
}

\notes{
The `compute_entropy` function calculates the entropy of a multivariate Gaussian distribution from its precision matrix. The `compute_entropy_gradient` function computes the gradient of entropy with respect to the precision matrix, which is essential for our gradient ascent procedure.

Next, we implement functions to handle the constraints imposed by the uncertainty principle:
}

\code{
# Project gradient to respect uncertainty constraints
def project_gradient(eigenvalues, gradient):
    """
    Project gradient to respect minimum uncertainty constraints.
    
    Parameters:
    -----------
    eigenvalues: array
        Eigenvalues of precision matrix
    gradient: array
        Gradient vector
    
    Returns:
    --------
    projected_gradient: array
        Gradient projected to respect constraints
    """
    n_pairs = len(eigenvalues) // 2
    projected_gradient = gradient.copy()
    
    # For each position-momentum pair
    for i in range(n_pairs):
        idx1, idx2 = 2*i, 2*i+1
        
        # Check if we're at the uncertainty boundary
        product = 1.0 / (eigenvalues[idx1] * eigenvalues[idx2])
        
        if product <= min_uncertainty_product * 1.01:
            # We're at or near the boundary
            # Project gradient to maintain the product
            avg_grad = 0.5 * (gradient[idx1]/eigenvalues[idx1] + gradient[idx2]/eigenvalues[idx2])
            projected_gradient[idx1] = avg_grad * eigenvalues[idx1]
            projected_gradient[idx2] = avg_grad * eigenvalues[idx2]
    
    return projected_gradient

# Initialize a multidimensional state with position-momentum pairs
def initialize_multidimensional_state(n_pairs, squeeze_factors=None):
    """
    Initialize a precision matrix for multiple position-momentum pairs.
    
    Parameters:
    -----------
    n_pairs: int
        Number of position-momentum pairs
    squeeze_factors: list, optional
        Factors to squeeze initial uncertainty ellipses
    
    Returns:
    --------
    Lambda: array
        Initial precision matrix
    """
    if squeeze_factors is None:
        squeeze_factors = [0.1] * n_pairs
    
    # Create block diagonal precision matrix
    Lambda = np.zeros((2*n_pairs, 2*n_pairs))
    
    for i in range(n_pairs):
        # Position-momentum pair with minimum uncertainty
        lambda_x = 1.0 / (squeeze_factors[i] * np.sqrt(min_uncertainty_product))
        lambda_p = 1.0 / (np.sqrt(min_uncertainty_product) / squeeze_factors[i])
        
        # Place on diagonal
        idx1, idx2 = 2*i, 2*i+1
        Lambda[idx1, idx1] = lambda_x
        Lambda[idx2, idx2] = lambda_p
    
    return Lambda
}

\notes{
The `project_gradient` function ensures that our gradient ascent respects the uncertainty principle by projecting the gradient to maintain minimum uncertainty products when necessary. The `initialize_multidimensional_state` function creates a starting state with multiple position-momentum pairs, each initialized to the minimum uncertainty allowed by the uncertainty principle, but with different "squeeze factors" that determine the shape of the uncertainty ellipse.}

\helpercode{
# Add gradient check function
def check_entropy_gradient(Lambda, epsilon=1e-6):
    """
    Check the analytical gradient of entropy against numerical gradient.
    
    Parameters:
    -----------
    Lambda: array
        Precision matrix
    epsilon: float
        Small perturbation for numerical gradient
    
    Returns:
    --------
    analytical_grad: array
        Analytical gradient with respect to eigenvalues
    numerical_grad: array
        Numerical gradient with respect to eigenvalues
    """
    # Get eigendecomposition
    eigenvalues, eigenvectors = eigh(Lambda)
    
    # Compute analytical gradient
    analytical_grad = entropy_gradient(eigenvalues)
    
    # Compute numerical gradient
    numerical_grad = np.zeros_like(eigenvalues)
    for i in range(len(eigenvalues)):
        # Perturb eigenvalue up
        eigenvalues_plus = eigenvalues.copy()
        eigenvalues_plus[i] += epsilon
        Lambda_plus = eigenvectors @ np.diag(eigenvalues_plus) @ eigenvectors.T
        entropy_plus = compute_entropy(Lambda_plus)
        
        # Perturb eigenvalue down
        eigenvalues_minus = eigenvalues.copy()
        eigenvalues_minus[i] -= epsilon
        Lambda_minus = eigenvectors @ np.diag(eigenvalues_minus) @ eigenvectors.T
        entropy_minus = compute_entropy(Lambda_minus)
        
        # Compute numerical gradient
        numerical_grad[i] = (entropy_plus - entropy_minus) / (2 * epsilon)
    
    # Compare
    print("Analytical gradient:", analytical_grad)
    print("Numerical gradient:", numerical_grad)
    print("Difference:", np.abs(analytical_grad - numerical_grad))
    
    return analytical_grad, numerical_grad}

\notes{Now we implement the main gradient ascent procedure.}

\code{

# Perform gradient ascent on entropy
def gradient_ascent_entropy(Lambda_init, n_steps=100, learning_rate=0.01):
    """
    Perform gradient ascent on entropy while respecting uncertainty constraints.
    
    Parameters:
    -----------
    Lambda_init: array
        Initial precision matrix
    n_steps: int
        Number of gradient steps
    learning_rate: float
        Learning rate for gradient ascent
    
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
    
    for step in range(n_steps):
        # Compute gradient of entropy
        grad_matrix = compute_entropy_gradient(Lambda)
        
        # Diagonalize Lambda to work with eigenvalues
        eigenvalues, eigenvectors = eigh(Lambda)
        
        # Transform gradient to eigenvalue space
        grad = np.diag(eigenvectors.T @ grad_matrix @ eigenvectors)
        
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
}

\notes{
The `gradient_ascent_entropy` function implements the core optimization procedure. It performs gradient ascent on the entropy while respecting the uncertainty constraints. The algorithm works in the eigenvalue space of the precision matrix, which makes it easier to enforce constraints and ensure the matrix remains positive definite.

To analyze the results, we implement functions to track uncertainty metrics and detect interesting dynamics:
}

\code{
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
}

\notes{
The `track_uncertainty_metrics` function analyzes the evolution of uncertainty products for each position-momentum pair and classifies them as either "quantum-like" (near minimum uncertainty) or "classical-like" (with excess uncertainty). This classification helps us understand how the system transitions between these regimes during entropy maximization.

We also implement a function to detect saddle points in the gradient flow, which are critical for understanding the system's dynamics:
}

\code{
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
}

\notes{
The `detect_saddle_points` function identifies points in the gradient flow where some eigenvalues change much faster than others, indicating saddle-like behavior. These saddle points are important because they represent critical transitions in the system's evolution.

Finally, we implement visualization functions to help us understand the system's behavior:
}

\code{
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
    return fig
}

\notes{
The `plot_multidimensional_uncertainty` function visualizes the uncertainty ellipses for multiple position-momentum pairs at different steps of the gradient ascent process. These visualizations help us understand how the system transitions from quantum-like to classical-like regimes.

This implementation builds on the `InformationReservoir` class we saw earlier, but generalizes to multiple position-momentum pairs and focuses specifically on the uncertainty relationships. The key connection is that both implementations track how systems naturally evolve from minimal entropy states (with quantum-like uncertainty relations) toward maximum entropy states (with classical-like uncertainty relations).
}

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

# Verify gradient calculation
print("Testing gradient calculation:")
test_Lambda = np.array([[2.0, 0.5], [0.5, 1.0]])  # Example precision matrix
analytical_grad, numerical_grad = check_entropy_gradient(test_Lambda)

# Verify if we're ascending or descending
entropy_before = compute_entropy(test_Lambda)
eigenvalues, eigenvectors = eigh(test_Lambda)
step_size = 0.01
eigenvalues_after = eigenvalues + step_size * analytical_grad
test_Lambda_after = eigenvectors @ np.diag(eigenvalues_after) @ eigenvectors.T
entropy_after = compute_entropy(test_Lambda_after)

print(f"Entropy before step: {entropy_before}")
print(f"Entropy after step: {entropy_after}")
print(f"Change in entropy: {entropy_after - entropy_before}")
if entropy_after > entropy_before:
    print("We are ascending the entropy gradient")
else:
    print("We are descending the entropy gradient")

test_grad = compute_entropy_gradient(test_Lambda)
print(f"Precision matrix:\n{test_Lambda}")
print(f"Entropy gradient:\n{test_grad}")
print(f"Entropy: {compute_entropy(test_Lambda):.4f}")
# Initialize system with 2 position-momentum pairs
n_pairs = 2
Lambda_init = initialize_multidimensional_state(n_pairs, squeeze_factors=[0.1, 0.5])
# Run gradient ascent
n_steps = 100
Lambda_history, entropy_history = gradient_ascent_entropy(Lambda_init, n_steps, learning_rate=0.01)

# Track metrics
uncertainty_metrics = track_uncertainty_metrics(Lambda_history)
saddle_metrics = detect_saddle_points(Lambda_history)

# Print results
print("\nFinal entropy:", entropy_history[-1])
print("Initial uncertainty products:", uncertainty_metrics['uncertainty_products'][0])
print("Final uncertainty products:", uncertainty_metrics['uncertainty_products'][-1])
print("Saddle point candidates at steps:", saddle_metrics['saddle_candidates'])
}

\plotcode{
# Plot entropy evolution
plt.figure(figsize=plot.big_wide_figsize)
plt.plot(entropy_history)
plt.xlabel('Gradient Ascent Step')
plt.ylabel('Entropy')
plt.title('Entropy Evolution During Gradient Ascent')
plt.grid(True)
mlai.write_figure(filename='entropy-evolution-during-gradient-ascent.svg', 
                  directory='./information-game')

# Plot uncertainty products evolution
plt.figure(figsize=plot.big_wide_figsize)
for i in range(n_pairs):
    plt.plot(uncertainty_metrics['uncertainty_products'][:, i], 
             label=f'Pair {i+1}')
plt.axhline(y=min_uncertainty_product, color='k', linestyle='--', 
           label='Minimum uncertainty')
plt.xlabel('Gradient Ascent Step')
plt.ylabel('Uncertainty Product (ΔxΔp)')
plt.title('Evolution of Uncertainty Products')
plt.legend()
plt.grid(True)

mlai.write_figure(filename='uncertainty-products-evolution.svg', 
                  directory='./information-game')



# Plot uncertainty ellipses at key steps
step_indices = [0, 20, 50, 99]  # Initial, early, middle, final
plot_multidimensional_uncertainty(Lambda_history, step_indices)

# Plot eigenvalues evolution
plt.subplots(figsize=plot.big_wide_figsize)
for i in range(2*n_pairs):
    plt.semilogy(saddle_metrics['eigenvalues_history'][:, i], 
                label=f'$\\lambda_{i+1}$')
plt.xlabel('Gradient Ascent Step')
plt.ylabel('Eigenvalue (log scale)')
plt.title('Evolution of Precision Matrix Eigenvalues')
plt.legend()
plt.grid(True)
plt.tight_layout()
mlai.write_figure(filename='eigenvalue-evolution.svg', 
                  directory='./information-game')}

\newslide{Eigenvalue Evolution}

\figure{\includediagram{\diagramsDir/information-game/eigenvalue-evolution}{70%}}{Eigenvalue evolution during gradient ascent.}{eigenvalue-evolution}

\newslide{Uncertainty Products Evolution}

\figure{\includediagram{\diagramsDir/information-game/uncertainty-products-evolution}{70%}}{Uncertainty products evolution during gradient ascent.}{uncertainty-products-evolution}

\newslide{Entropy Evolution During Gradient Ascent}

\figure{\includediagram{\diagramsDir/information-game/entropy-evolution-during-gradient-ascent}{70%}}{Entropy evolution during gradient ascent.}{entropy-evolution-during-gradient-ascent}

\newslide{Evolution of Uncertainty Products}

\figure{\includediagram{\diagramsDir/information-game/uncertainty-products-evolution}{70%}}{.}{uncertainty-products-evolution}



\endif 
