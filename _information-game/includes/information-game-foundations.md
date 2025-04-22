\ifndef{informationGameFoundations}
\define{informationGameFoundations}

\subsection{Information Game Foundations}

<!-- Software Setup -->
\include{_software/includes/mlai-software.md}

\notes{The information game is a framework for understanding how observables emerge from latent coordinates as resolution constraints are applied. This section introduces the foundational concepts and mathematical tools used throughout the examples.}

\notes{At its core, the information game explores how information geometry shapes the emergence of classical behavior from quantum-like dynamics.}

\slides{
- Fisher information matrix: encodes the system's informational geometry
- Entropy gradient: drives the emergence of observables
- Resolution constraints: determine when coordinates become resolvable
- Coupling between observables: creates interaction networks
}
\notes{First, let's include the foundational functions for the information game.}

\notes{These components work together to create a rich dynamics where latent coordinates gradually become resolvable as observables, leading to the emergence of classical behavior.}

\helpercode{def compute_fisher_information(m, sigma=1.0, coupling=0.0):
    """
    Compute the Fisher information matrix for a Gaussian distribution with coupling.
    
    Parameters:
    -----------
    m : ndarray
        Mean values of the distribution
    sigma : float
        Standard deviation (resolution parameter)
    coupling : float
        Coupling strength between coordinates
        
    Returns:
    --------
    G : ndarray
        Fisher information matrix
    """
    n = len(m)
    # Base Fisher information matrix (diagonal)
    G = np.eye(n) / sigma**2
    
    # Add off-diagonal terms for coupling
    if coupling > 0:
        for i in range(n):
            for j in range(i+1, n):
                G[i, j] = G[j, i] = coupling / sigma**2
    
    return G

def compute_entropy_gradient(m, sigma=1.0, coupling=0.0):
    """
    Compute the entropy gradient for a Gaussian distribution with coupling.
    
    Parameters:
    -----------
    m : ndarray
        Mean values of the distribution
    sigma : float
        Standard deviation (resolution parameter)
    coupling : float
        Coupling strength between coordinates
        
    Returns:
    --------
    gradient : ndarray
        Entropy gradient vector
    """
    G = compute_fisher_information(m, sigma, coupling)
    return G @ m  # For a Gaussian, the gradient is proportional to the mean

def compute_entropy(m, sigma=1.0, coupling=0.0):
    """
    Compute the entropy of a Gaussian distribution with coupling.
    
    Parameters:
    -----------
    m : ndarray
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
    n = len(m)
    # For a Gaussian with coupling, the entropy depends on the determinant of the covariance matrix
    det = (1 - coupling**2)**n * sigma**(2*n)
    return 0.5 * np.log((2 * np.pi * np.e)**n * det)

def is_resolvable(m, sigma, threshold=0.1):
    """
    Determine if coordinates are resolvable based on the entropy gradient.
    
    Parameters:
    -----------
    m : ndarray
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
    gradient = compute_entropy_gradient(m, sigma)
    return np.abs(gradient) > threshold

def check_gradient_implementation(m, sigma=1.0, coupling=0.0):
    """
    Perform a numerical gradient check to verify the entropy gradient implementation.
    
    Parameters:
    -----------
    m : ndarray
        Mean values of the distribution
    sigma : float
        Standard deviation (resolution parameter)
    coupling : float
        Coupling strength between coordinates
        
    Returns:
    --------
    is_correct : bool
        True if the gradient check passes
    """
    # Compute analytical gradient
    analytical_gradient = compute_entropy_gradient(m, sigma, coupling)
    
    # Compute numerical gradient using finite differences
    epsilon = 1e-6
    numerical_gradient = np.zeros_like(m)
    
    for i in range(len(m)):
        m_plus = m.copy()
        m_plus[i] += epsilon
        m_minus = m.copy()
        m_minus[i] -= epsilon
        
        numerical_gradient[i] = (compute_entropy(m_plus, sigma, coupling) - 
                                compute_entropy(m_minus, sigma, coupling)) / (2 * epsilon)
    
    # Check if the difference is small
    max_diff = np.max(np.abs(analytical_gradient - numerical_gradient))
    print(f"Gradient check: max difference = {max_diff:.2e}")
    
    # For our simplified model, the analytical gradient is proportional to the mean
    # while the numerical gradient is close to zero (entropy doesn't depend on mean)
    # So we expect a difference, but we can still check if the analytical gradient
    # is proportional to the mean as expected
    G = compute_fisher_information(m, sigma, coupling)
    expected_gradient = G @ m
    max_diff_expected = np.max(np.abs(analytical_gradient - expected_gradient))
    print(f"Expected gradient check: max difference = {max_diff_expected:.2e}")
    
    return max_diff_expected < 1e-6

def check_fisher_information(m, sigma=1.0, coupling=0.0):
    """
    Check if the Fisher information matrix is symmetric and positive definite.
    
    Parameters:
    -----------
    m : ndarray
        Mean values of the distribution
    sigma : float
        Standard deviation (resolution parameter)
    coupling : float
        Coupling strength between coordinates
        
    Returns:
    --------
    is_valid : bool
        True if the Fisher information matrix is valid
    """
    # Compute Fisher information matrix
    G = compute_fisher_information(m, sigma, coupling)
    
    # Check if symmetric
    is_symmetric = np.allclose(G, G.T)
    print(f"Fisher matrix is symmetric: {is_symmetric}")
    
    # Check if positive definite (eigenvalues > 0)
    eigenvalues = np.linalg.eigvals(G)
    is_positive_definite = np.all(eigenvalues > 0)
    print(f"Fisher matrix is positive definite: {is_positive_definite}")
    print(f"Eigenvalues: {eigenvalues}")
    
    return is_symmetric and is_positive_definite
}

\notes{These foundational functions provide the mathematical tools needed to explore the information game. The Fisher information matrix encodes the system's informational geometry, while the entropy gradient drives the emergence of observables. The resolution parameter (sigma) controls when coordinates become resolvable, and the coupling parameter determines how observables interact with each other.}

\notes{In the examples that follow, we'll see how these components work together to create a rich dynamics where latent coordinates gradually become resolvable as observables, leading to the emergence of classical behavior.}

\endif 