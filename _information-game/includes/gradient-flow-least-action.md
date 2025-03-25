\ifndef{gradientFlowLeastAction}
\define{gradientFlowLeastAction}

\editme

\subsection{Gradient Flow and Least Action Principles}

\notes{The steepest ascent dynamics in our system naturally connect to least action principles in physics. We can demonstrate this connection through a simple visualization of gradient flows.}

\slides{
* Steepest ascent of entropy ≈ Path of least action
* System follows geodesics in information geometry
* Action integral: $\mathcal{A} = \int L(\theta, \dot{\theta})dt$
* Information-theoretic Lagrangian: $L = \frac{1}{2}\dot{\theta}^TG(\theta)\dot{\theta} - S(\theta)$
}

\notes{
For our entropy game, we can define an information-theoretic action:

$$\mathcal{A}[\gamma] = \int_0^T \left(\frac{1}{2}\dot{\theta}^T G(\theta) \dot{\theta} - S(\theta)\right) dt$$

where $\gamma$ is a path through parameter space, $G(\theta)$ is the Fisher information matrix, and $S(\theta)$ is the entropy. The least action principle states that the system will follow paths that minimize this action.

This is exactly what our steepest ascent dynamics produce: the system follows geodesics in the information geometry while maximizing entropy production. As the system evolves, it naturally creates information reservoirs in directions where the gradient is small but non-zero.
}

\code{
# Visualizing gradient flow and least action path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# Create a potential energy landscape
def potential(x, y):
    return np.exp(-(x**2 + y**2)/4) - np.exp(-((x-2)**2 + (y-2)**2)/1)

# Create gradient vector field
def gradient(x, y):
    dx = -x/2 * np.exp(-(x**2 + y**2)/4) + (x-2) * np.exp(-((x-2)**2 + (y-2)**2)/1)
    dy = -y/2 * np.exp(-(x**2 + y**2)/4) + (y-2) * np.exp(-((x-2)**2 + (y-2)**2)/1)
    return dx, dy

# Create grid
x = np.linspace(-3, 4, 100)
y = np.linspace(-3, 4, 100)
X, Y = np.meshgrid(x, y)
Z = potential(X, Y)

# Calculate gradient field
dx, dy = gradient(X, Y)
magnitude = np.sqrt(dx**2 + dy**2)

# Create the figure
fig, ax = plt.subplots(figsize=(10, 8))

# Plot potential as contour
contour = ax.contourf(X, Y, Z, levels=50, cmap='viridis', alpha=0.7)
cbar = plt.colorbar(contour, ax=ax)
cbar.set_label('Entropy S(θ)')

# Plot gradient field
stride = 5
ax.quiver(X[::stride, ::stride], Y[::stride, ::stride], 
          dx[::stride, ::stride], dy[::stride, ::stride],
          magnitude[::stride, ::stride],
          cmap='autumn', scale=50, width=0.002)

# Simulate and plot a particle path following gradient
def simulate_path(start_x, start_y, steps=100, dt=0.1):
    path_x, path_y = [start_x], [start_y]
    x, y = start_x, start_y
    for _ in range(steps):
        dx_val, dy_val = gradient(x, y)
        x += dx_val * dt
        y += dy_val * dt
        path_x.append(x)
        path_y.append(y)
    return path_x, path_y

# Plot a path
path_x, path_y = simulate_path(-2, -2)
ax.plot(path_x, path_y, 'r-', linewidth=2, label='Least action path')

ax.set_xlabel('θ₁')
ax.set_ylabel('θ₂')
ax.set_title('Gradient Flow and Least Action Path')
ax.legend()
ax.set_aspect('equal')
}

\notes{
The visualization shows how a system following the entropy gradient naturally traces a path of least action through the parameter space. This connection between steepest ascent and least action is profound: it suggests that entropy maximization and energy minimization are dual aspects of the same fundamental principle.

At points where the gradient becomes small (near critical points), the system exhibits critical slowing, and information reservoirs naturally form. These are precisely the regions where parameters become effective variables for controlling system behavior with minimal energy expenditure.
} 

\endif
