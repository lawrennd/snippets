\ifndef{gradientFlowLeastAction}
\define{gradientFlowLeastAction}

\editme

\subsection{Gradient Flow and Least Action Principles}

\notes{The steepest ascent dynamics in our system naturally connect to least action principles in physics. We can demonstrate this connection through a simple visualisation of gradient flows.}

\slides{
* Steepest ascent of entropy ≈ Path of least action
* System follows geodesics in information geometry
}

\newslide{Information-Theoretic Action}

\slides{
* Action integral
  $$
  \mathcal{A} = \int L(\theta, \dot{\theta}) \text{d}t
  $$
* Information-theoretic Lagrangian
  $$
  L = \frac{1}{2}\dot{\theta}^\top G(\theta)\dot{\theta} - S(\theta)
  $$
* cf @Frieden-physics98.
}

\notes{
For our entropy game, we can define an information-theoretic action,
$$
\mathcal{A}[\gamma] = \int_0^T \left(\frac{1}{2}\dot{\boldsymbol{\theta}}^\top G(\boldsymbol{\theta}) \dot{\boldsymbol{\theta}} - S(\boldsymbol{\theta})\right) \text{d}t
$$
where $\gamma$ is a path through parameter space, $G(\boldsymbol{\theta})$ is the Fisher information matrix, and $S(\boldsymbol{\theta})$ is the entropy. The least action principle states that the system will follow paths that extremise this action.}

\notes{This is also what our steepest ascent dynamics produce: the system follows geodesics in the information geometry while maximizing entropy production. As the system evolves, it naturally creates information reservoirs in directions where the gradient is small but non-zero.}

\setupcode{import numpy as np}

\helpercode{# Create a potential energy landscape based on bivariate Gaussian entropy
def potential(x, y):
    # Interpret x as sqrt-precision parameter and y as correlation parameter
    # Constrain y to be between -1 and 1 (valid correlation)
    y_corr = np.tanh(y)
    
    # Construct precision and covariance matrices
    precision = x**2  # x is sqrt-precision
    variance = 1/precision
    covariance = y_corr * variance
    
    # Covariance matrix
    Sigma = np.array([[variance, covariance], 
                      [covariance, variance]])
    
    # Entropy of bivariate Gaussian
    det_Sigma = variance**2 * (1 - y_corr**2)
    entropy = 0.5 * np.log((2 * np.pi * np.e)**2 * det_Sigma)
    
    return entropy

# Create gradient vector field for the Gaussian entropy
def gradient(x, y):
    # Small delta for numerical gradient
    delta = 1e-6
    
    # Compute numerical gradient
    dx = (potential(x + delta, y) - potential(x - delta, y)) / (2 * delta)
    dy = (potential(x, y + delta) - potential(x, y - delta)) / (2 * delta)
    
    return dx, dy

# Simulate and plot a particle path following gradient
def simulate_path(start_x, start_y, steps=100000, dt=0.00001):
    path_x, path_y = [start_x], [start_y]
    x, y = start_x, start_y
    for _ in range(steps):
        dx_val, dy_val = gradient(x, y)
        x += dx_val * dt
        y += dy_val * dt
        path_x.append(x)
        path_y.append(y)
    return path_x, path_y
}

\code{# Visualizing gradient flow and least action path

# Create grid
x = np.linspace(-3, 4, 100)
y = np.linspace(-3, 4, 100)
X, Y = np.meshgrid(x, y)
Z = potential(X, Y)

# Calculate gradient field
dx, dy = gradient(X, Y)
magnitude = np.sqrt(dx**2 + dy**2)
path_x, path_y = simulate_path(2, 3)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai
from matplotlib.colors import LogNorm}

\plotcode{
# Create the figure
fig, ax = plt.subplots(figsize=(10, 8))

# Plot potential as contour lines only (not filled)
contour = ax.contour(X, Y, Z, levels=15, colors='black', alpha=0.7, linewidths=0.8)
ax.clabel(contour, inline=True, fontsize=8)  # Add labels to contour lines

# Plot gradient field
stride = 5
ax.quiver(X[::stride, ::stride], Y[::stride, ::stride], 
          dx[::stride, ::stride]/magnitude[::stride, ::stride], 
          dy[::stride, ::stride]/magnitude[::stride, ::stride],
          magnitude[::stride, ::stride],
          cmap='autumn', scale=25, width=0.002)

# Plot path
ax.plot(path_x, path_y, 'r-', linewidth=2, label='Least action path')

ax.set_xlabel('$\\theta_1$')
ax.set_ylabel('$\\theta_2$')
ax.set_title('Gradient Flow and Least Action Path')
ax.legend()
ax.set_aspect('equal')

mlai.write_figure(filename='gradient-flow-least-action.svg', 
                  directory = './information-game')
}

\newslide{Gradient Flow and Least Action Path}

\figure{\includediagram{\diagramsDir/information-game/gradient-flow-least-action}{70%}{Visualisation of the gradient flow and least action path.}{gradient-flow-least-action}}

\notes{The visualization shows how a system following the entropy gradient traces a path of least action through the parameter space. This connection between steepest ascent and least action comes because entropy maximization and free energy minimization are dual views of the same underlying principle.}

\notes{At points where the gradient becomes small (near critical points), the system exhibits critical slowing, and information reservoirs naturally form. These are the regions where variables, $X$, become information reservoirs and effective parameters, $M$, that control system behaviour.} 

\endif
