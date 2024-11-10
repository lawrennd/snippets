\ifndef{dimRedFailureModes}
\define{dimRedFailureModes}

\editme

\subsection{When Dimensionality Reduction Fails}

\notes{While dimensionality reduction is powerful, it's important to understand when it can fail:

1. When the data really is high dimensional with no simpler structure
2. When the relationship between dimensions is highly nonlinear
3. When different parts of the data have different intrinsic dimensionality}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
import mlai.plot as plot}

\code{# Generate data that lies on a Swiss roll manifold
def generate_swiss_roll(n_points=1000):
    t = 1.5 * np.pi * (1 + 2 * np.random.rand(n_points))
    y = 21 * np.random.rand(n_points)
    x = t * np.cos(t)
    z = t * np.sin(t)
    return np.column_stack((x, y, z))

X = generate_swiss_roll()

fig = plt.figure(figsize=plot.big_wide_figsize)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=t)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$') 
ax.set_zlabel('$z$')}

\notes{This example shows data lying on a Swiss roll manifold. Linear dimensionality reduction methods like PCA will fail to capture the structure of this data, while nonlinear methods like t-SNE or UMAP may perform better.

Common failure modes include:
1. Using linear methods on nonlinear manifolds
2. Assuming global structure when only local structure exists
3. Not accounting for noise in the data}

\endif
