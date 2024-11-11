\ifndef{dimRedFailureModes}
\define{dimRedFailureModes}

\editme

\subsection{When Dimensionality Reduction Fails}

\slides{
* Dimensionality reduction can fail in several key scenarios:
    * Truly high dimensional data with no simpler structure
    * Highly nonlinear relationships between dimensions 
    * Varying intrinsic dimensionality across data
}

\notes{While dimensionality reduction is powerful, it's important to understand when it can fail:

1. When the data really is high dimensional with no simpler structure
2. When the relationship between dimensions is highly nonlinear
3. When different parts of the data have different intrinsic dimensionality}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\subsection{The Swiss Roll Example}

\slides{
* Classic example of nonlinear structure
* 2D manifold embedded in 3D
* Linear methods like PCA fail
* Requires nonlinear methods (t-SNE, UMAP)
}

\code{# Generate data that lies on a Swiss roll manifold
def generate_swiss_roll(n_points=1000):
    t = 1.5 * np.pi * (1 + 2 * np.random.rand(n_points))
    y = 21 * np.random.rand(n_points)
    x = t * np.cos(t)
    z = t * np.sin(t)
    return np.column_stack((x, y, z)), t

X, t = generate_swiss_roll()

fig = plt.figure(figsize=plot.big_wide_figsize)
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=t, cmap='viridis')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$') 
ax.set_zlabel('$z$')
plt.colorbar(scatter)

mlai.write_figure('swiss-roll.svg', directory='\writeDiagramsDir/dimred')}

\figure{\includediagram{\diagramsDir/dimred/swiss-roll}{80%}}{The Swiss roll dataset is a classic example of data with nonlinear structure. The color represents the position along the roll, showing how points that are far apart in the original space are actually close in the intrinsic manifold.}{swiss-roll-example}

\subsection{Common Failure Modes}

\slides{
* Key failure scenarios:
    * Linear methods on nonlinear manifolds
    * Assuming global structure when only local exists
    * Not accounting for noise
}

\notes{This example shows data lying on a Swiss roll manifold. Linear dimensionality reduction methods like PCA will fail to capture the structure of this data, while nonlinear methods like t-SNE or UMAP may perform better.

Common failure modes include:
1. Using linear methods on nonlinear manifolds
2. Assuming global structure when only local structure exists
3. Not accounting for noise in the data}

\endif
