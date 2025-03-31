\ifndef{epiEntropyEquivalence}
\define{epiEntropyEquivalence}

\editme

\subsection{Extreme Physical Information and Entropy Maximization}

\notes{The gradient flow dynamics we've been exploring have interesting connections to Roy Frieden's Extreme Physical Information (EPI) principle. This section explores the formal equivalence between entropy maximization in exponential families and EPI optimization.}

\slides{
* Frieden's EPI principle: Physics laws arise from information optimization
* Minimizing: $\Delta = I(X|\boldsymbol{\theta}) - J(M|\boldsymbol{\theta})$
* $I$ = Fisher information, $J$ = bound information
* Formally equivalent to entropy maximization for exponential families
}

\newslide{Exponential Family and Fisher Information}

\slides{
* Exponential family: $\rho(z;\boldsymbol{\theta}) = h(z)\exp\left(\boldsymbol{\theta}^\top T(z) - A(\boldsymbol{\theta})\right)$
* Fisher information matrix: $G(\boldsymbol{\theta}) = \nabla^2_{\boldsymbol{\theta}} A(\boldsymbol{\theta})$
* Entropy gradient: $\nabla_{\boldsymbol{\theta}}S(Z) = \mathbf{g} = \nabla^2_{\boldsymbol{\theta}} A(\boldsymbol{\theta})$
* Gradient ascent: $\Delta \boldsymbol{\theta} = \eta \mathbf{g}$
}

\notes{
In our entropy game, we've been maximizing entropy through gradient ascent on the natural parameters $\boldsymbol{\theta}$. For exponential family distributions, the entropy gradient is directly related to the Fisher information matrix:

$$\nabla_{\boldsymbol{\theta}}S(Z) = \mathbf{g} = \nabla^2_{\boldsymbol{\theta}} A(\boldsymbol{\theta})$$

where $A(\boldsymbol{\theta})$ is the log-partition function. The Fisher information matrix is precisely the Hessian of this function:

$$G(\boldsymbol{\theta}) = \nabla^2_{\boldsymbol{\theta}} A(\boldsymbol{\theta})$$

This establishes a direct connection between entropy maximization and the geometry of the parameter space as measured by Fisher information.
}

\newslide{Frieden's EPI Principle}

\notes{
Roy Frieden's Extreme Physical Information (EPI) principle proposes that physical laws arise from the optimization of an information-theoretic functional. The EPI functional is defined as:

$$\Delta = I(X|\boldsymbol{\theta}) - J(M|\boldsymbol{\theta})$$

where $I(X|\boldsymbol{\theta})$ is the Fisher information associated with observable variables $X$, and $J(M|\boldsymbol{\theta})$ is the "bound information" associated with memory variables $M$. The principle states that physical systems evolve to minimize this difference.

For exponential families, the Fisher information can be expressed in terms of the Fisher information matrix:

$$I(X|\boldsymbol{\theta}) = \text{Tr}[G_X(\boldsymbol{\theta})]$$

where $G_X(\boldsymbol{\theta})$ is the Fisher information matrix for the observable variables.
}

\slides{
* EPI principle: Minimize $\Delta = I(X|\boldsymbol{\theta}) - J(M|\boldsymbol{\theta})$
* For exponential families: $I(X|\boldsymbol{\theta}) = \text{Tr}[G_X(\boldsymbol{\theta})]$
* Gradient flow on EPI functional leads to same equilibrium as entropy maximization
* Both approaches identify information-theoretic optima
}

\newslide{Formal Equivalence}

\notes{
The formal equivalence between entropy maximization and EPI optimization can be established by examining their equilibrium conditions. For entropy maximization, equilibrium occurs when:

$$\nabla_{\boldsymbol{\theta}}S(Z) = 0$$

For EPI optimization, equilibrium occurs when:

$$\frac{\delta \Delta}{\delta \rho} = \text{constant}$$

For exponential families with a partitioned system $Z = (X,M)$, these conditions become equivalent when the system respects certain Markov properties. Specifically, when $X$ and $X'$ are conditionally independent given $M$, both approaches lead to the same equilibrium distribution.

This equivalence provides a profound connection between our entropy game dynamics and fundamental principles in physics. It suggests that the paths of steepest entropy increase that we've been studying are not just mathematical constructs but may reflect deeper physical principles about how information flows in natural systems.
}

\setupcode{import numpy as np
from scipy.linalg import eigh
import matplotlib.pyplot as plt}

\helpercode{
def compute_epi_functional(G, partition_indices):
    """
    Compute the EPI functional for a given Fisher information matrix
    and partition of variables into observables and memory.
    
    Parameters:
    -----------
    G: array
        Fisher information matrix
    partition_indices: list
        Indices of observable variables (complement is memory variables)
    
    Returns:
    --------
    Delta: float
        EPI functional value
    """
    n = G.shape[0]
    obs_indices = np.array(partition_indices)
    mem_indices = np.array([i for i in range(n) if i not in obs_indices])
    
    # Extract submatrices
    G_obs = G[np.ix_(obs_indices, obs_indices)]
    G_mem = G[np.ix_(mem_indices, mem_indices)]
    
    # Compute trace of each submatrix
    I_obs = np.trace(G_obs)
    J_mem = np.trace(G_mem)
    
    return I_obs - J_mem

def epi_gradient(G, partition_indices):
    """
    Compute gradient of EPI functional with respect to parameters.
    
    Parameters:
    -----------
    G: array
        Fisher information matrix
    partition_indices: list
        Indices of observable variables
    
    Returns:
    --------
    gradient: array
        Gradient of EPI functional
    """
    n = G.shape[0]
    gradient = np.zeros(n)
    
    obs_indices = np.array(partition_indices)
    mem_indices = np.array([i for i in range(n) if i not in obs_indices])
    
    # Set gradient components (simplified model)
    gradient[obs_indices] = -1.0  # Minimize Fisher information for observables
    gradient[mem_indices] = 1.0   # Maximize Fisher information for memory
    
    return gradient

def compare_entropy_and_epi_paths(G_init, partition_indices, steps=100, learning_rate=0.01):
    """
    Compare paths of entropy maximization and EPI optimization.
    
    Parameters:
    -----------
    G_init: array
        Initial Fisher information matrix
    partition_indices: list
        Indices of observable variables
    steps: int
        Number of gradient steps
    learning_rate: float
        Step size for gradient updates
    
    Returns:
    --------
    entropy_path: array
        Path through parameter space under entropy maximization
    epi_path: array
        Path through parameter space under EPI optimization
    """
    # Initialize
    G_entropy = G_init.copy()
    G_epi = G_init.copy()
    
    entropy_path = []
    epi_path = []
    
    for _ in range(steps):
        # Entropy maximization step
        eigenvalues_entropy, eigenvectors_entropy = eigh(G_entropy)
        entropy_grad = entropy_gradient(eigenvalues_entropy)
        eigenvalues_entropy += learning_rate * entropy_grad
        eigenvalues_entropy = np.maximum(eigenvalues_entropy, 1e-10)
        G_entropy = eigenvectors_entropy @ np.diag(eigenvalues_entropy) @ eigenvectors_entropy.T
        entropy_path.append(eigenvalues_entropy.copy())
        
        # EPI optimization step
        eigenvalues_epi, eigenvectors_epi = eigh(G_epi)
        epi_grad = epi_gradient(G_epi, partition_indices)
        projected_epi_grad = project_gradient(eigenvalues_epi, epi_grad)
        eigenvalues_epi += learning_rate * projected_epi_grad
        eigenvalues_epi = np.maximum(eigenvalues_epi, 1e-10)
        G_epi = eigenvectors_epi @ np.diag(eigenvalues_epi) @ eigenvectors_epi.T
        epi_path.append(eigenvalues_epi.copy())
    
    return np.array(entropy_path), np.array(epi_path)
}

\code{
# Initialize system with 2 position-momentum pairs
n_pairs = 2
G_init = initialize_multidimensional_state(n_pairs, squeeze_factors=[0.1, 0.2])

# Define partition: first pair is observable, second pair is memory
partition_indices = [0, 1]  # Indices of first position-momentum pair

# Compare paths
entropy_path, epi_path = compare_entropy_and_epi_paths(G_init, partition_indices)
}

\plotcode{
# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: Paths through eigenvalue space for first pair
ax1.plot(entropy_path[:, 0], entropy_path[:, 1], 'r-', label='Entropy Max')
ax1.plot(epi_path[:, 0], epi_path[:, 1], 'b--', label='EPI Min')
ax1.set_xlabel('Position eigenvalue')
ax1.set_ylabel('Momentum eigenvalue')
ax1.set_title('Observable Variables Path')
ax1.legend()
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.grid(True)

# Plot 2: Paths through eigenvalue space for second pair
ax2.plot(entropy_path[:, 2], entropy_path[:, 3], 'r-', label='Entropy Max')
ax2.plot(epi_path[:, 2], epi_path[:, 3], 'b--', label='EPI Min')
ax2.set_xlabel('Position eigenvalue')
ax2.set_ylabel('Momentum eigenvalue')
ax2.set_title('Memory Variables Path')
ax2.legend()
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.grid(True)

plt.tight_layout()

mlai.write_figure(filename='epi-entropy-comparison.svg', 
                  directory='./information-game')
}

\newslide{Comparison of Entropy Maximization and EPI Optimization}

\figure{\includediagram{\diagramsDir/information-game/epi-entropy-comparison}{80%}}{Comparison of parameter paths under entropy maximization (red solid line) and EPI optimization (blue dashed line) for observable variables (left) and memory variables (right).}{epi-entropy-comparison}

\notes{
The figure above compares the paths taken through parameter space under entropy maximization versus EPI optimization. For observable variables (left), both approaches lead to similar equilibrium states but may follow different trajectories. For memory variables (right), the paths can diverge more significantly depending on the specific constraints and initial conditions.

Despite these potential differences in trajectories, both approaches ultimately identify information-theoretic optima that balance uncertainty between different parts of the system. This suggests a deep connection between the principle of maximum entropy and Frieden's EPI principle, at least for systems described by exponential family distributions.

The equivalence between these approaches provides a unifying perspective on information dynamics in physical systems. It suggests that the paths of steepest entropy increase that we've been studying in our entropy game may have fundamental physical significance beyond their mathematical elegance.
}

\notes{
This connection to Frieden's work also relates to our earlier discussion of least action principles. The EPI principle can be viewed as a special case of a more general variational principle, where the "action" being minimized is an information-theoretic functional rather than a physical one. This reinforces the idea that information geometry provides a natural framework for understanding both physical and information-theoretic dynamics.
}

\endif 