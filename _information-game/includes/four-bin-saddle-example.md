\ifndef{fourBinSaddleExample}
\define{fourBinSaddleExample}

\editme

\subsection{Four-Bin Saddle Point Example}

\notes{To illustrate saddle points and information reservoirs, we need at least a 4-bin system. This creates a 3-dimensional parameter space where we can observe genuine saddle points.}

\slides{
* Four-bin system creates 3D parameter space
* Saddle points appear where:
  * Gradient is zero
  * Some directions increase entropy
  * Other directions decrease entropy
* Information reservoirs form in critically slowed directions
}

\notes{
Consider a 4-bin system parameterized by natural parameters $\theta_1$, $\theta_2$, and $\theta_3$ (with one constraint). A saddle point occurs where the gradient $\nabla_\theta S = 0$, but the Hessian has mixed eigenvalues - some positive, some negative.

At these points, the Fisher information matrix $G(\theta)$ eigendecomposition reveals:
* Fast modes: large positive eigenvalues → rapid evolution
* Slow modes: small positive eigenvalues → gradual evolution 
* Critical modes: near-zero eigenvalues → information reservoirs

The eigenvectors of $G(\theta)$ at the saddle point determine which parameter combinations form information reservoirs.
}

\setupcode{import numpy as np}

\code{# Define a function with a saddle point (simplified for visualization)
def f(x, y):
    return x**2 - y**2

# Create a grid of points
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# A few gradient vectors
stride = 20
u = 2 * X[::stride, ::stride]
v = -2 * Y[::stride, ::stride]
}

\setupplotcode{
# Simplified saddle point example
import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai

from mpl_toolkits.mplot3d import Axes3D
}

\plotcode{fig = plt.figure(figsize=(10, 8))
# Create a 3D plot
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.set_xlabel('θ₁')
ax.set_ylabel('θ₂')
ax.set_zlabel('Entropy S(θ)')
ax.set_title('Saddle Point in Parameter Space')

w = np.zeros_like(u)
ax.quiver(X[::stride, ::stride], Y[::stride, ::stride], Z[::stride, ::stride], 
          u, v, w, color='r', length=0.3, normalize=True)

mlai.write_figure(filename='simplified-saddle-point-example.svg', 
                  directory = './information-game')
}

\notes{The animation of system evolution would show:
1. Initial rapid movement along high-eigenvalue directions
2. Progressive slowing in certain directions
3. Formation of information reservoirs in the critically slowed directions
4. Parameter-capacity uncertainty emerging naturally at the saddle point
} 

\endif
