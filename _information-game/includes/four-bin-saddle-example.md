\ifndef{fourBinSaddleExample}
\define{fourBinSaddleExample}

\editme

\subsection{Four-Bin Saddle Point Example}

\notes{To illustrate saddle points and information reservoirs, we need at least a 4-bin system. This creates a 3-dimensional parameter space where we can observe genuine saddle points.}

\slides{* Four-bin system creates 3D parameter space
* Saddle points appear where:
  * Gradient is zero
  * Some directions increase entropy
  * Other directions decrease entropy
* Information reservoirs form in critically slowed directions
}

\notes{Consider a 4-bin system parameterized by natural parameters $\theta_1$, $\theta_2$, and $\theta_3$ (with one constraint). A saddle point occurs where the gradient $\nabla_\theta S = 0$, but the Hessian has mixed eigenvalues - some positive, some negative.}

\notes{At these points, the Fisher information matrix $G(\theta)$ eigendecomposition reveals.

* Fast modes: large positive eigenvalues → rapid evolution
* Slow modes: small positive eigenvalues → gradual evolution 
* Critical modes: near-zero eigenvalues → information reservoirs

The eigenvectors of $G(\theta)$ at the saddle point determine which parameter combinations form information reservoirs.
}

\setupcode{import numpy as np}

\code{# Simplified saddle point example
# Define a function with a saddle point (simplified for visualization)
def f(x, y, order=4, yorder=None):
    if yorder is None:
         yorder = order
    return x**order - y**yorder

def g(x, y, order=4, yorder=None):
    if yorder is None:
         yorder = order
    return order*x**(order-1), -yorder*y**(yorder-1)

# Create a grid of points
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

xorder = 2
yorder = 4

Z = f(X, Y, xorder, yorder)
dX, dY = g(X, Y, xorder, yorder)

# A few gradient vectors
stride = 20
u = dX[::stride, ::stride]
v = dY[::stride, ::stride]}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai

from mpl_toolkits.mplot3d import Axes3D}

\plotcode{fig = plt.figure(figsize=plot.big_wide_figsize)
# Create a 3D plot
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.set_zlim([-2.5, 2.5])
ax.set_xlabel('$\\theta_1$')
ax.set_ylabel('$\\theta_2$')
ax.set_zlabel('Entropy $S(\\boldsymbol{\\theta})')
ax.set_title('Saddle Point in Parameter Space')

w = np.zeros_like(u)
ax.quiver(X[::stride, ::stride], Y[::stride, ::stride], Z[::stride, ::stride], 
          u, v, w, color='r', length=0.5, normalize=True)

mlai.write_figure(filename='simplified-saddle-point-example.svg', 
                  directory = './information-game')
}

\notes{The animation of system evolution would show initial rapid movement along high-eigenvalue directions, progressive slowing in directions with low eigenvalues and formation of information reservoirs in the critically slowed directions. Parameter-capacity uncertainty emerges naturally at the saddle point.
} 

\endif
