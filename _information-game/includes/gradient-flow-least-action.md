\ifndef{gradientFlowLeastAction}
\define{gradientFlowLeastAction}

\editme

\subsection{Gradient Flow and Least Action Principles}

\notes{The steepest ascent dynamics in our system naturally connect to least action principles in physics. We can demonstrate this connection through visualizing how our uncertainty ellipses evolve along paths of steepest entropy increase.}

\slides{
* Steepest ascent of entropy ≈ Path of least action
* System follows geodesics in information geometry
}

\newslide{Information-Theoretic Action}

\slides{
* Action integral
  $$
  \mathcal{A}[\gamma] = \int_0^T \left(\dot{\boldsymbol{\theta}} \cdot \nabla_{\boldsymbol{\theta}} S - \frac{1}{2}\|\dot{\boldsymbol{\theta}}\|^2\right) \text{d}t
  $$
* First term represents entropy production rate along path
* Second term constrains speed of parameter changes
}

\notes{
For our entropy game, we can define an information-theoretic action,
$$
\mathcal{A}[\gamma] = \int_0^T \left(\dot{\boldsymbol{\theta}} \cdot \nabla_{\boldsymbol{\theta}} S - \frac{1}{2}\|\dot{\boldsymbol{\theta}}\|^2\right) \text{d}t
$$
where $\gamma$ is a path through parameter space. The first term represents the rate of entropy production along the path ($\frac{\text{d}S}{\text{d}\theta} \cdot \frac{\text{d}\theta}{\text{d}t}$), while the second term 
constrains how quickly parameters can change. Maximizing this action leads naturally to gradient flow dynamics, where changes in parameters follow the entropy gradient:
$$
\dot{\boldsymbol{\theta}} = \nabla_{\boldsymbol{\theta}} S
$$
}

\notes{This is exactly what our steepest ascent dynamics implement: the system follows the entropy gradient, with the learning rate controlling the size of parameter updates. As the system evolves, it naturally creates 
information reservoirs in directions where the gradient is small but non-zero.}

\setupcode{import numpy as np}


\helpercode{
def simulate_action_path(G_init, steps=100, learning_rate=0.01):
    """
    Simulate path through parameter space following entropy gradient.
    Returns both the path and the entropy production rate.
    """
    G = G_init.copy()
    path_history = []
    entropy_production = []
    
    for _ in range(steps):
        # Get current state
        eigenvalues, eigenvectors = eigh(G)
        
        # Compute gradient
        grad = entropy_gradient(eigenvalues)
        proj_grad = project_gradient(eigenvalues, grad)
        
        # Store current point and entropy production rate
        path_history.append(eigenvalues.copy())
        entropy_production.append(np.dot(proj_grad, grad))
        
        # Update eigenvalues
        eigenvalues += learning_rate * proj_grad
        eigenvalues = np.maximum(eigenvalues, 1e-10)
        
        # Reconstruct G
        G = eigenvectors @ np.diag(eigenvalues) @ eigenvectors.T
        
    return np.array(path_history), np.array(entropy_production)
}

\code{
# Initialize system with 2 position-momentum pairs
n_pairs = 2
G_init = initialize_multidimensional_state(n_pairs, squeeze_factors=[0.1, 0.2])

# Simulate path
path_history, entropy_production = simulate_action_path(G_init)
}

\plotcode{
# Create figure with two subplots
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

# Plot 1: Path through eigenvalue space
ax.plot(path_history[:, 0], path_history[:, 1], 'r-', label='Pair 1')
ax.plot(path_history[:, 2], path_history[:, 3], 'b-', label='Pair 2')
ax.set_xlabel('Position eigenvalue')
ax.set_ylabel('Momentum eigenvalue')
ax.set_title('Path Through Parameter Space')
ax.legend()

# Add minimum uncertainty hyperbolas
x = np.linspace(0.1, 5, 100)
ax.plot(x, min_uncertainty_product/x, 'k--', alpha=0.5, label='Min uncertainty')
ax.set_xscale('log')
ax.set_yscale('log')
ax.grid(True)

mlai.write_figure(filename='gradient-flow-least-action.svg', 
                  directory='./information-game')
}

\plotcode{# Plot 2: Uncertainty ellipses at selected points
steps_to_show = [0, 25, 50, -1]
plot_multidimensional_uncertainty(Lambda_history, step_indices=steps_to_show, pairs_to_plot=[0, 1])
ax2.set_title('Evolution of Uncertainty Ellipses')

plt.tight_layout()

mlai.write_figure(filename='gradient-flow-least-action-uncertainty-ellipses.svg', 
                  directory='./information-game')
}

\newslide{Gradient Flow and Least Action Path}

\figure{\includediagram{\diagramsDir/information-game/gradient-flow-least-action}{80%}}{Visualization of the gradient flow through parameter space.}{gradient-flow-least-action}

\newslide{Gradient Flow and Least Action Path}

\figure{\includediagram{\diagramsDir/information-game/gradient-flow-least-action-uncertainty-ellipses}{80%}}{Visualization of the corresponding evolution of uncertainty ellipses (right). The dashed lines show minimum uncertainty bounds.}{gradient-flow-least-action-uncertainty-ellipses}

\notes{
The action integral governing this evolution can be written:
$$
\mathcal{A}[\gamma] = \int_0^T \left(\dot{\boldsymbol{\theta}} \cdot \nabla_{\boldsymbol{\theta}} S - \frac{1}{2}\dot{\boldsymbol{\theta}}^\top G \dot{\boldsymbol{\theta}}\right) \text{d}t
$$
where $G$ is the Fisher information metric. The path follows steepest entropy increase while respecting quantum uncertainty constraints, naturally transitioning from quantum-like to classical-like behavior.
}

\endif
