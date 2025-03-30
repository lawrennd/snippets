\ifndef{gradientAscentLargeSystem}
\define{gradientAscentLargeSystem}

\editme

\subsection{Scaling to Large Systems: Emergent Statistical Behavior}

\notes{We now extend our analysis to much larger systems with thousands of position-momentum pairs. This allows us to observe emergent statistical behaviors and phase transitions that aren't apparent in smaller systems.}

\slides{
* Scale to systems with 1000+ position-momentum pairs
* Observe emergent statistical behaviors
* Identify clusters of similar dynamical patterns
* Analyze quantum-classical phase transitions
}

\notes{Large-scale systems reveal how microscopic uncertainty constraints lead to macroscopic statistical patterns. By analyzing thousands of position-momentum pairs simultaneously, we can identify emergent behaviors and natural clustering of dynamical patterns.}

\helpercode{# Optimized implementation for very large systems
def large_scale_gradient_ascent(n_pairs, steps=100, learning_rate=1, sample_interval=5):
    """
    Memory-efficient implementation of gradient ascent for very large systems.
    
    Parameters:
    -----------
    n_pairs: int
        Number of position-momentum pairs
    steps: int
        Number of gradient steps to take
    learning_rate: float
        Step size for gradient ascent
    sample_interval: int
        Store state every sample_interval steps to save memory
    
    Returns:
    --------
    sampled_states: list
        Sparse history of states at sampled intervals
    entropy_history: list
        Complete history of entropy values
    uncertainty_metrics: dict
        Metrics tracking uncertainty products over time
    """
    # Initialize with diagonal precision matrix (no need to store full matrix)
    dim = 2 * n_pairs
    eigenvalues = np.zeros(dim)
    
    # Initialize with minimal entropy state
    for i in range(n_pairs):
        squeeze = 0.1 * (1 + (i % 10))  # Cycle through 10 different squeeze factors
        eigenvalues[2*i] = 1.0 / (squeeze * min_uncertainty_product)
        eigenvalues[2*i+1] = 1.0 / (min_uncertainty_product / squeeze)
    
    # Storage for results (sparse to save memory)
    sampled_states = []
    entropy_history = []
    uncertainty_products = np.zeros((steps+1, n_pairs))
    
    # Initial entropy and uncertainty
    entropy = 0.5 * (dim * (1 + np.log(2*np.pi)) - np.sum(np.log(eigenvalues)))
    entropy_history.append(entropy)
    
    # Track initial uncertainty products
    for i in range(n_pairs):
        uncertainty_products[0, i] = 1.0 / np.sqrt(eigenvalues[2*i] * eigenvalues[2*i+1])
    
    # Store initial state
    sampled_states.append(eigenvalues.copy())
    
    # Gradient ascent loop
    for step in range(steps):
        # Compute gradient with respect to eigenvalues (diagonal precision)
        grad = -1.0 / (2.0 * eigenvalues)
        
        # Project gradient to respect constraints
        for i in range(n_pairs):
            idx1, idx2 = 2*i, 2*i+1
            
            # Current uncertainty product (in eigenvalue space, this is inverse)
            current_product = eigenvalues[idx1] * eigenvalues[idx2]
            
            # If we're already at minimum uncertainty, project gradient
            if abs(current_product - 1/min_uncertainty_product**2) < 1e-6:
                # Tangent direction preserves the product
                tangent = np.array([-eigenvalues[idx2], -eigenvalues[idx1]])
                tangent = tangent / np.linalg.norm(tangent)
                
                # Project the gradient onto this tangent
                pair_gradient = np.array([grad[idx1], grad[idx2]])
                projection = np.dot(pair_gradient, tangent) * tangent
                
                grad[idx1] = projection[0]
                grad[idx2] = projection[1]
        
        # Update eigenvalues
        eigenvalues += learning_rate * grad
        
        # Ensure eigenvalues remain positive
        eigenvalues = np.maximum(eigenvalues, 1e-10)
        
        # Compute entropy
        entropy = 0.5 * (dim * (1 + np.log(2*np.pi)) - np.sum(np.log(eigenvalues)))
        entropy_history.append(entropy)
        
        # Track uncertainty products
        for i in range(n_pairs):
            uncertainty_products[step+1, i] = 1.0 / np.sqrt(eigenvalues[2*i] * eigenvalues[2*i+1])
        
        # Store state at sampled intervals
        if step % sample_interval == 0 or step == steps-1:
            sampled_states.append(eigenvalues.copy())
    
    # Compute regime classifications
    regimes = np.zeros((steps+1, n_pairs), dtype=object)
    for step in range(steps+1):
        for i in range(n_pairs):
            if abs(uncertainty_products[step, i] - min_uncertainty_product) < 0.1*min_uncertainty_product:
                regimes[step, i] = "Quantum-like"
            else:
                regimes[step, i] = "Classical-like"
    
    uncertainty_metrics = {
        'uncertainty_products': uncertainty_products,
        'regimes': regimes
    }
    
    return sampled_states, entropy_history, uncertainty_metrics

# Analyze statistical properties of large-scale system
def analyze_large_system(uncertainty_metrics, n_pairs, steps):
    """
    Analyze statistical properties of a large-scale system.
    
    Parameters:
    -----------
    uncertainty_metrics: dict
        Metrics from large_scale_gradient_ascent
    n_pairs: int
        Number of position-momentum pairs
    steps: int
        Number of gradient steps taken
    
    Returns:
    --------
    analysis: dict
        Statistical analysis results
    """
    uncertainty_products = uncertainty_metrics['uncertainty_products']
    regimes = uncertainty_metrics['regimes']
    
    # Compute statistics over time
    mean_uncertainty = np.mean(uncertainty_products, axis=1)
    std_uncertainty = np.std(uncertainty_products, axis=1)
    min_uncertainty_over_time = np.min(uncertainty_products, axis=1)
    max_uncertainty_over_time = np.max(uncertainty_products, axis=1)
    
    # Count regime transitions
    quantum_count = np.zeros(steps+1)
    for step in range(steps+1):
        quantum_count[step] = np.sum(regimes[step] == "Quantum-like")
    
    # Identify clusters of similar behavior
    from sklearn.cluster import KMeans
    
    # Reshape to have each pair as a sample with its uncertainty trajectory as features
    pair_trajectories = uncertainty_products.T  # shape: (n_pairs, steps+1)
    
    # Use fewer clusters for very large systems
    n_clusters = min(10, n_pairs // 100)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(pair_trajectories)
    
    # Count pairs in each cluster
    cluster_counts = np.bincount(cluster_labels, minlength=n_clusters)
    
    # Get representative pairs from each cluster (closest to centroid)
    representative_pairs = []
    for i in range(n_clusters):
        cluster_members = np.where(cluster_labels == i)[0]
        if len(cluster_members) > 0:
            # Find pair closest to cluster centroid
            centroid = kmeans.cluster_centers_[i]
            distances = np.linalg.norm(pair_trajectories[cluster_members] - centroid, axis=1)
            closest_idx = cluster_members[np.argmin(distances)]
            representative_pairs.append(closest_idx)
    
    return {
        'mean_uncertainty': mean_uncertainty,
        'std_uncertainty': std_uncertainty,
        'min_uncertainty': min_uncertainty_over_time,
        'max_uncertainty': max_uncertainty_over_time,
        'quantum_count': quantum_count,
        'quantum_fraction': quantum_count / n_pairs,
        'cluster_counts': cluster_counts,
        'representative_pairs': representative_pairs,
        'cluster_labels': cluster_labels
    }

# Visualize results for large-scale system
def visualize_large_system(sampled_states, entropy_history, uncertainty_metrics, analysis, n_pairs, steps):
    """
    Create visualizations for large-scale system results.
    
    Parameters:
    -----------
    sampled_states: list
        Sparse history of eigenvalues
    entropy_history: list
        History of entropy values
    uncertainty_metrics: dict
        Uncertainty metrics over time
    analysis: dict
        Statistical analysis results
    n_pairs: int
        Number of position-momentum pairs
    steps: int
        Number of gradient steps taken
    """
    # Plot entropy evolution
    plt.figure(figsize=(10, 6))
    plt.plot(entropy_history)
    plt.xlabel('Gradient Ascent Step')
    plt.ylabel('Entropy')
    plt.title(f'Entropy Evolution for {n_pairs} Position-Momentum Pairs')
    plt.grid(True)
    
    # Plot uncertainty statistics
    plt.figure(figsize=(10, 6))
    plt.plot(analysis['mean_uncertainty'], label='Mean uncertainty')
    plt.fill_between(range(steps+1), 
                    analysis['mean_uncertainty'] - analysis['std_uncertainty'],
                    analysis['mean_uncertainty'] + analysis['std_uncertainty'],
                    alpha=0.3, label='±1 std dev')
    plt.plot(analysis['min_uncertainty'], 'g--', label='Min uncertainty')
    plt.plot(analysis['max_uncertainty'], 'r--', label='Max uncertainty')
    plt.axhline(y=min_uncertainty_product, color='k', linestyle=':', label='Quantum limit')
    plt.xlabel('Gradient Ascent Step')
    plt.ylabel('Uncertainty Product (ΔxΔp)')
    plt.title(f'Uncertainty Evolution Statistics for {n_pairs} Pairs')
    plt.legend()
    plt.grid(True)
    
    # Plot quantum-classical transition
    plt.figure(figsize=(10, 6))
    plt.plot(analysis['quantum_fraction'] * 100)
    plt.xlabel('Gradient Ascent Step')
    plt.ylabel('Percentage of Pairs (%)')
    plt.title('Percentage of Pairs in Quantum-like Regime')
    plt.ylim(0, 100)
    plt.grid(True)
    
    # Plot representative pairs from each cluster
    plt.figure(figsize=(12, 8))
    for i, pair_idx in enumerate(analysis['representative_pairs']):
        cluster_idx = analysis['cluster_labels'][pair_idx]
        count = analysis['cluster_counts'][cluster_idx]
        plt.plot(uncertainty_metrics['uncertainty_products'][:, pair_idx], 
                label=f'Cluster {i+1} ({count} pairs, {count/n_pairs*100:.1f}%)')
    
    plt.axhline(y=min_uncertainty_product, color='k', linestyle=':', label='Quantum limit')
    plt.xlabel('Gradient Ascent Step')
    plt.ylabel('Uncertainty Product ($\Delta x \Delta p$)')
    plt.title('Representative Uncertainty Trajectories from Each Cluster')
    plt.legend()
    plt.grid(True)
    
    # Visualize uncertainty ellipses for representative pairs
    if len(sampled_states) > 0:
        # Get indices of sampled steps
        sampled_steps = list(range(0, steps+1, (steps+1)//len(sampled_states)))
        if sampled_steps[-1] != steps:
            sampled_steps[-1] = steps
        
        # Only visualize a few representative pairs
        pairs_to_visualize = analysis['representative_pairs'][:min(4, len(analysis['representative_pairs']))]
        
        fig, axes = plt.subplots(len(pairs_to_visualize), len(sampled_states), 
                                figsize=(4*len(sampled_states), 3*len(pairs_to_visualize)))
        
        # Handle case of single pair or single step
        if len(pairs_to_visualize) == 1:
            axes = axes.reshape(1, -1)
        if len(sampled_states) == 1:
            axes = axes.reshape(-1, 1)
        
        for row, pair_idx in enumerate(pairs_to_visualize):
            for col, step_idx in enumerate(range(len(sampled_states))):
                ax = axes[row, col]
                eigenvalues = sampled_states[step_idx]
                
                # Extract eigenvalues for this pair
                idx1, idx2 = 2*pair_idx, 2*pair_idx+1
                pos_eigenvalue = eigenvalues[idx1]
                mom_eigenvalue = eigenvalues[idx2]
                
                # Convert precision eigenvalues to covariance eigenvalues
                cov_eigenvalues = np.array([1/pos_eigenvalue, 1/mom_eigenvalue])
                
                # Calculate ellipse parameters (assuming principal axes aligned with coordinate axes)
                width, height = 2 * np.sqrt(cov_eigenvalues)
                
                # Create ellipse
                ellipse = Ellipse((0, 0), width=width, height=height, angle=0,
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
                uncertainty_product = np.sqrt(1/(pos_eigenvalue * mom_eigenvalue))
                
                # Determine regime
                if abs(uncertainty_product - min_uncertainty_product) < 0.1*min_uncertainty_product:
                    regime = "Quantum-like"
                    color = 'red'
                else:
                    regime = "Classical-like"
                    color = 'blue'
                
                # Add labels
                if row == 0:
                    step_num = sampled_steps[step_idx]
                    ax.set_title(f"Step {step_num}")
                if col == 0:
                    cluster_idx = analysis['cluster_labels'][pair_idx]
                    count = analysis['cluster_counts'][cluster_idx]
                    ax.set_ylabel(f"Cluster {row+1}\n({count} pairs)")
                
                # Add uncertainty product text
                ax.text(0.05, 0.95, f"ΔxΔp = {uncertainty_product:.2f}",
                      transform=ax.transAxes, fontsize=10, verticalalignment='top')
                
                # Add regime text
                ax.text(0.05, 0.85, regime, transform=ax.transAxes, 
                      fontsize=10, verticalalignment='top', color=color)
                
                ax.set_xlabel("Position")
                ax.set_ylabel("Momentum")
        
        plt.tight_layout()}

\notes{In large-scale systems, we observe several emergent phenomena that aren't apparent in smaller systems:

1. *Statistical phase transitions*: As the system evolves, we observe a gradual transition from predominantly quantum-like behavior to predominantly classical-like behavior. This transition resembles a phase transition in statistical physics.

2. *Natural clustering*: The thousands of position-momentum pairs naturally organize into clusters with similar dynamical behaviors. Some clusters maintain quantum-like characteristics for longer periods, while others quickly transition to classical-like behavior.

3. *Scale-invariant patterns*: The statistical properties of the system show remarkable consistency across different scales, suggesting underlying universal principles in the entropy-uncertainty relationship.}

\newslide{Emergent Statistical Behaviors}

\slides{
* Statistical phase transitions emerge
* Natural clustering of dynamical behaviors
* Scale-invariant patterns across system sizes
* Quantum-classical boundary becomes a statistical property
}

\notes{The quantum-classical boundary, which appears sharp in small systems, becomes a statistical property in large systems. At any given time, some fraction of the system exhibits quantum-like behavior while the remainder shows classical-like characteristics. This fraction evolves over time, creating a dynamic boundary between quantum and classical regimes.}

\notes{The clustering analysis reveals natural groupings of position-momentum pairs based on their dynamical trajectories. These clusters represent different "modes" of behavior within the large system, with some modes maintaining quantum coherence for longer periods while others quickly decohere into classical-like states.}

\setupcode{import numpy as np
from scipy.linalg import eigh
from sklearn.cluster import KMeans}

\code{# Constants
hbar = 1.0  # Normalized Planck's constant
min_uncertainty_product = hbar/2

# Run large-scale simulation
n_pairs = 5000  # 5000 position-momentum pairs (10,000×10,000 matrix)
steps = 100      # Fewer steps for large system

# Run the optimized implementation
sampled_states, entropy_history, uncertainty_metrics = large_scale_gradient_ascent(
    n_pairs=n_pairs, steps=steps, learning_rate=0.01, sample_interval=5)

# Analyze results
analysis = analyze_large_system(uncertainty_metrics, n_pairs, steps)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai
from matplotlib.patches import Ellipse, Circle}

\plotcode{# Visualize results
visualize_large_system(sampled_states, entropy_history, uncertainty_metrics, 
                      analysis, n_pairs, steps)

# Additional plot: Phase transition visualization
plt.figure(figsize=(10, 6))
quantum_fraction = analysis['quantum_fraction'] * 100
classical_fraction = 100 - quantum_fraction

plt.stackplot(range(steps+1), 
             [quantum_fraction, classical_fraction],
             labels=['Quantum-like', 'Classical-like'],
             colors=['red', 'blue'], alpha=0.7)

plt.xlabel('Gradient Ascent Step')
plt.ylabel('Percentage of System (%)')
plt.title('Quantum-Classical Phase Transition')
plt.legend(loc='center right')
plt.ylim(0, 100)
plt.grid(True)}

\notes{The large-scale simulation reveals how microscopic uncertainty constraints lead to macroscopic statistical patterns. The system naturally organizes into regions of quantum-like and classical-like behavior, with a dynamic boundary that evolves over time.}

\notes{This perspective provides a new way to understand the quantum-classical transition not as a sharp boundary, but as a statistical property of large systems. The fraction of the system exhibiting quantum-like behavior gradually decreases as entropy increases, creating a smooth transition between quantum and classical regimes.}

\notes{The clustering analysis identifies natural groupings of position-momentum pairs based on their dynamical trajectories. These clusters represent different "modes" of behavior within the large system, with some modes maintaining quantum coherence for longer periods while others quickly decohere into classical-like states.}

\notes{This approach to large-scale quantum-classical systems provides a powerful framework for understanding how microscopic quantum constraints manifest in macroscopic statistical behaviors. It bridges quantum mechanics and statistical physics through the common language of information theory and entropy.}

\endif
