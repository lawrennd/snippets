\ifndef{iterativeDimensionalityReduction}
\define{iterativeDimensionalityReduction}

\editme

\subsection{Iterative Dimensionality Reduction}

\notes{While spectral methods like PCA and classical MDS provide analytical solutions through eigendecomposition, many dimensionality reduction problems require iterative optimization approaches. These methods can often capture more complex relationships in the data but come at the cost of potentially getting stuck in local optima.}

\slides{
* Spectral methods (PCA, MDS) give analytical solutions
* Iterative methods optimize objective functions
  * Can capture more complex relationships
  * May find local optima
  * More computationally intensive
}

\subsection{Stress Functions}

\notes{A key concept in iterative dimensionality reduction is the stress function, which measures how well the low-dimensional representation preserves relationships in the original data. The classic Kruskal stress function is:
$$
\text{stress} = \sqrt{\frac{\sum_{i<j} (\distanceScalar_{ij} - \latentDistanceScalar_{ij})^2}{\sum_{i<j} \distanceScalar_{ij}^2}},
$$
where $\distanceScalar_{ij}$ are the original distances and $\latentDistanceScalar_{ij}$ are the distances in the reduced space.}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
import mlai.plot as plot}

\loadcode{kruskal_stress}{mlai}
\loadcode{generate_swiss_roll}{mlai}

\notes{Different stress functions place different emphasis on preserving local versus global structure. For example, Sammon mapping modifies the stress function to give more weight to preserving small distances:

$$\text{stress}_{\text{Sammon}} = \frac{1}{\sum_{i<j} \distanceScalar_{ij}} \sum_{i<j} \frac{(\distanceScalar_{ij} - \latentDistanceScalar_{ij})^2}{\distanceScalar_{ij}}$$}

\subsection{Gradient Descent for Stress Minimisation}

\notes{To optimize the stress function using gradient descent, we need to compute the gradient of the stress with respect to the latent coordinates. This can be done in two stages: first computing the gradient of stress with respect to distances, then the gradient of distances with respect to the latent coordinates.}

\setupcode{def stress_gradient_wrt_distances(D_original, D_reduced):
    """Compute gradient of Kruskal stress with respect to reduced distances"""
    numerator = np.sum((D_original - D_reduced)**2)
    denominator = np.sum(D_original**2)
    
    # Gradient of stress with respect to D_reduced
    d_stress_d_D_reduced = -2 * (D_original - D_reduced) / (denominator * np.sqrt(numerator/denominator))
    
    return d_stress_d_D_reduced}

\setupcode{def distance_gradient_wrt_coordinates(X):
    """Compute gradient of pairwise distances with respect to coordinates"""
    n, d = X.shape
    d_dist_d_X = np.zeros((n, d))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                # Distance between points i and j
                diff = X[i] - X[j]
                dist = np.linalg.norm(diff)
                
                if dist > 1e-10:  # Avoid division by zero
                    # Gradient of distance with respect to X[i]
                    d_dist_d_X[i] += (diff / dist)
                    # Gradient of distance with respect to X[j] 
                    d_dist_d_X[j] -= (diff / dist)
    
    return d_dist_d_X}

\setupcode{def stress_gradient_wrt_coordinates(X, D_original):
    """Compute gradient of Kruskal stress with respect to latent coordinates"""
    # Compute current distances
    D_reduced = np.zeros((X.shape[0], X.shape[0]))
    for i in range(X.shape[0]):
        for j in range(X.shape[0]):
            D_reduced[i, j] = np.linalg.norm(X[i] - X[j])
    
    # Gradient of stress with respect to distances
    d_stress_d_D = stress_gradient_wrt_distances(D_original, D_reduced)
    
    # Gradient of distances with respect to coordinates
    d_dist_d_X = distance_gradient_wrt_coordinates(X)
    
    # Chain rule: gradient of stress with respect to coordinates
    d_stress_d_X = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[0]):
            if i != j:
                diff = X[i] - X[j]
                dist = np.linalg.norm(diff)
                if dist > 1e-10:
                    d_stress_d_X[i] += d_stress_d_D[i, j] * (diff / dist)
                    d_stress_d_X[j] -= d_stress_d_D[i, j] * (diff / dist)
    
    return d_stress_d_X}

\setupcode{def gradient_descent_stress(X_init, D_original, learning_rate=0.01, momentum=0.9, max_iterations=100, tolerance=1e-6):
    """Perform gradient descent with momentum to minimize Kruskal stress"""
    X = X_init.copy()
    velocity = np.zeros_like(X)  # Initialize velocity for momentum
    stress_history = []
    
    for iteration in range(max_iterations):
        # Compute current stress
        D_reduced = np.zeros((X.shape[0], X.shape[0]))
        for i in range(X.shape[0]):
            for j in range(X.shape[0]):
                D_reduced[i, j] = np.linalg.norm(X[i] - X[j])
        
        stress = kruskal_stress(D_original, D_reduced)
        stress_history.append(stress)
        
        # Compute gradient
        gradient = stress_gradient_wrt_coordinates(X, D_original)
        
        # Update velocity with momentum
        velocity = momentum * velocity - learning_rate * gradient
        
        # Update coordinates using velocity
        X_new = X + velocity
        
        # Check for convergence
        if np.linalg.norm(X_new - X) < tolerance:
            print(f"Converged after {iteration + 1} iterations")
            break
            
        X = X_new
        
        if iteration % 10 == 0:
            print(f"Iteration {iteration}: stress = {stress:.6f}")
    
    return X, stress_history}

\subsection{Example: Gradient Descent in Action}

\notes{Let's demonstrate the gradient descent algorithm on a simple example. We'll start with a 2D dataset and reduce it to 1D using iterative optimization.}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform}

\code{# Generate Swiss roll dataset
np.random.seed(42)
X_original, t_original = generate_swiss_roll(n_points=100, noise=0.1)

# Compute original distances
D_original = squareform(pdist(X_original))

# Initialize 2D embedding randomly
X_init = np.random.randn(100, 2) * 0.01

print("Original data shape:", X_original.shape)
print("Initial embedding shape:", X_init.shape)
print("Initial stress:", kruskal_stress(D_original, squareform(pdist(X_init))))}

\code{# Run gradient descent with momentum
X_final, stress_history = gradient_descent_stress(
    X_init, D_original, 
    learning_rate=0.01, 
    momentum=0.9,
    max_iterations=200,
    tolerance=1e-8
)

print(f"Final stress: {stress_history[-1]:.6f}")
print(f"Stress reduction: {stress_history[0] - stress_history[-1]:.6f}")
print(f"Converged in {len(stress_history)} iterations")}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
from mlai import plot}

\plotcode{fig = plt.figure(figsize=(15, 5))

# Plot 1: Original 3D Swiss roll
ax1 = fig.add_subplot(131, projection='3d')
ax1.scatter(X_original[:, 0], X_original[:, 1], X_original[:, 2], 
           c=t_original, cmap='viridis', s=20, alpha=0.7)
ax1.set_title('Original 3D Swiss Roll')
ax1.set_xlabel('$x_1$')
ax1.set_ylabel('$x_2$')
ax1.set_zlabel('$x_3$')

# Plot 2: Final 2D embedding
ax2 = fig.add_subplot(132)
scatter = ax2.scatter(X_final[:, 0], X_final[:, 1], c=t_original, 
                     cmap='viridis', s=20, alpha=0.7)
ax2.set_title('Final 2D Embedding')
ax2.set_xlabel('$z_1$')
ax2.set_ylabel('$z_2$')
ax2.grid(True, alpha=0.3)

# Plot 3: Stress convergence
ax3 = fig.add_subplot(133)
ax3.plot(stress_history, 'g-', linewidth=2)
ax3.set_title('Stress Convergence')
ax3.set_xlabel('Iteration')
ax3.set_ylabel('Kruskal Stress')
ax3.grid(True, alpha=0.3)

plt.tight_layout()
mlai.write_figure("gradient_descent_stress_example.svg", directory="\writeDiagramsDir/dimred/")}

\notes{The gradient descent algorithm successfully reduces the Kruskal stress, finding a 2D embedding that preserves the pairwise distances from the original 3D Swiss roll data as well as possible. The convergence plot shows how the stress decreases over iterations, demonstrating the optimization process in action. The color coding shows how the algorithm preserves the underlying manifold structure.}

\subsection{Effect of Momentum}

\notes{Let's compare the performance of gradient descent with and without momentum to demonstrate the speedup:}

\code{# Compare gradient descent with and without momentum
import time

# Without momentum
print("Running gradient descent without momentum...")
start_time = time.time()
X_no_momentum, stress_history_no_momentum = gradient_descent_stress(
    X_init, D_original, 
    learning_rate=0.01, 
    momentum=0.0,  # No momentum
    max_iterations=200,
    tolerance=1e-8
)
time_no_momentum = time.time() - start_time

# With momentum
print("\nRunning gradient descent with momentum...")
start_time = time.time()
X_momentum, stress_history_momentum = gradient_descent_stress(
    X_init, D_original, 
    learning_rate=0.01, 
    momentum=0.9,  # With momentum
    max_iterations=200,
    tolerance=1e-8
)
time_momentum = time.time() - start_time

print(f"\nNo momentum: {len(stress_history_no_momentum)} iterations, {time_no_momentum:.2f}s")
print(f"With momentum: {len(stress_history_momentum)} iterations, {time_momentum:.2f}s")
print(f"Speedup: {time_no_momentum/time_momentum:.1f}x")}

\plotcode{fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Convergence comparison
axes[0].plot(stress_history_no_momentum, 'b-', linewidth=2, label='No Momentum')
axes[0].plot(stress_history_momentum, 'r-', linewidth=2, label='With Momentum')
axes[0].set_title('Convergence Comparison')
axes[0].set_xlabel('Iteration')
axes[0].set_ylabel('Kruskal Stress')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Final embeddings comparison
axes[1].scatter(X_no_momentum[:, 0], X_no_momentum[:, 1], c=t_original, 
               cmap='viridis', s=20, alpha=0.7, label='No Momentum')
axes[1].set_title('Final Embeddings')
axes[1].set_xlabel('$z_1$')
axes[1].set_ylabel('$z_2$')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
mlai.write_figure("momentum_comparison.svg", directory="\writeDiagramsDir/dimred/")}

\subsection{Comparison with Classical MDS}

\notes{Let's compare our iterative approach with the classical MDS solution to see how they perform:}

\code{# Classical MDS solution
from sklearn.manifold import MDS

mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
X_mds = mds.fit_transform(D_original)

# Compare stress values
stress_gd = kruskal_stress(D_original, squareform(pdist(X_momentum)))
stress_mds = kruskal_stress(D_original, squareform(pdist(X_mds)))

print(f"Gradient Descent (with momentum) Stress: {stress_gd:.6f}")
print(f"Classical MDS Stress: {stress_mds:.6f}")}

\plotcode{fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Gradient descent result
scatter1 = axes[0].scatter(X_momentum[:, 0], X_momentum[:, 1], c=t_original, 
                          cmap='viridis', s=20, alpha=0.7)
axes[0].set_title(f'Gradient Descent + Momentum (Stress: {stress_gd:.4f})')
axes[0].set_xlabel('$z_1$')
axes[0].set_ylabel('$z_2$')
axes[0].grid(True, alpha=0.3)

# Classical MDS result
scatter2 = axes[1].scatter(X_mds[:, 0], X_mds[:, 1], c=t_original, 
                          cmap='viridis', s=20, alpha=0.7)
axes[1].set_title(f'Classical MDS (Stress: {stress_mds:.4f})')
axes[1].set_xlabel('$z_1$')
axes[1].set_ylabel('$z_2$')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
mlai.write_figure("gradient_descent_vs_mds.svg", directory="\writeDiagramsDir/dimred/")}

\notes{Both methods achieve similar results, with classical MDS typically providing the global optimum for this type of problem. However, the iterative gradient descent approach is more flexible and can be extended to handle constraints, non-Euclidean distances, and other modifications that would be difficult with classical methods.}

\endif
