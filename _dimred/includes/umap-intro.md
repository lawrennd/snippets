\ifndef{umapIntro}
\define{umapIntro}

\editme

\subsection{UMAP}

\notes{Uniform Manifold Approximation and Projection (UMAP) is a dimensionality reduction technique that builds on ideas from manifold learning and topological data analysis. It provides similar visualization quality to t-SNE but with better preservation of global structure and faster computation times.}

\slides{
* Based on Riemannian geometry and algebraic topology
* Preserves both local and global structure
* Faster than t-SNE
* Can be used for general dimension reduction
* Supports supervised and semi-supervised learning
}

\notes{UMAP constructs a weighted graph using fuzzy simplicial sets. For points $\dataVector_i$ and $\dataVector_j$, the weight is:

$$w_{ij} = \exp\left(\frac{-d(\dataVector_i, \dataVector_j) - \rho_i}{\sigma_i}\right)$$

where $\rho_i$ is the distance to the nearest neighbor of $i$, and $\sigma_i$ is chosen to achieve a desired local connectivity. This forms a high-dimensional fuzzy topological representation which UMAP then tries to approximate in lower dimensions.}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
import mlai.plot as plot
from sklearn.datasets import make_moons}

\code{def compare_umap_tsne(n_samples=1000, noise=0.1, 
                         random_state=42):
    """Compare UMAP and t-SNE on the two moons dataset"""
    # Generate data
    X, labels = make_moons(n_samples=n_samples, 
                          noise=noise, 
                          random_state=random_state)
    
    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, 
                                  figsize=plot.two_figsize)
    
    # t-SNE embedding
    from sklearn.manifold import TSNE
    tsne = TSNE(n_components=2, random_state=random_state)
    X_tsne = tsne.fit_transform(X)
    ax1.scatter(X_tsne[:, 0], X_tsne[:, 1], 
                c=labels, cmap=plt.cm.viridis)
    ax1.set_title('t-SNE')
    
    # UMAP embedding
    import umap
    reducer = umap.UMAP(random_state=random_state)
    X_umap = reducer.fit_transform(X)
    ax2.scatter(X_umap[:, 0], X_umap[:, 1], 
                c=labels, cmap=plt.cm.viridis)
    ax2.set_title('UMAP')
    
    plt.tight_layout()
    return fig}

\notes{UMAP has several advantages over t-SNE:

1. **Speed**: UMAP is significantly faster than t-SNE, especially for large datasets
2. **Global Structure**: UMAP often preserves more of the global structure of the data
3. **Theoretical Foundation**: UMAP has strong mathematical foundations in topology
4. **Versatility**: Can be used for general dimensionality reduction, not just visualization}

\subsection{UMAP Parameters}

\notes{UMAP's behavior can be controlled through several key parameters:

* `n_neighbors`: Controls how local/global the embedding is (similar to perplexity in t-SNE)
* `min_dist`: Controls how tightly points are allowed to pack together
* `metric`: The distance metric used in the high-dimensional space}

\code{def plot_umap_params(X, labels, 
                        n_neighbors=[5, 15, 50], 
                        min_dist=[0.1, 0.5, 0.9],
                        random_state=42):
    """Plot UMAP embeddings with different parameter settings"""
    fig, axes = plt.subplots(len(n_neighbors), len(min_dist), 
                            figsize=(5*len(min_dist), 
                                   5*len(n_neighbors)))
    
    for i, nn in enumerate(n_neighbors):
        for j, md in enumerate(min_dist):
            reducer = umap.UMAP(n_neighbors=nn,
                              min_dist=md,
                              random_state=random_state)
            X_umap = reducer.fit_transform(X)
            axes[i,j].scatter(X_umap[:, 0], X_umap[:, 1],
                            c=labels, cmap=plt.cm.viridis)
            axes[i,j].set_title(f'n_neighbors={nn}, min_dist={md}')
    
    plt.tight_layout()
    return fig}

\notes{Unlike t-SNE, UMAP can also be used to learn a reusable transformation. This means it can:
1. Transform new data points without rerunning the entire algorithm
2. Be used as part of a larger machine learning pipeline
3. Support supervised and semi-supervised dimensionality reduction}

\code{# Example of supervised UMAP
def supervised_umap_example(X_train, y_train, X_test, y_test,
                          random_state=42):
    """Demonstrate supervised UMAP"""
    # Fit UMAP with labels
    reducer = umap.UMAP(n_neighbors=15,
                       min_dist=0.1,
                       random_state=random_state)
    reducer.fit(X_train, y=y_train)
    
    # Transform test data
    X_test_umap = reducer.transform(X_test)
    
    # Plot results
    fig, ax = plt.subplots(figsize=plot.big_figsize)
    scatter = ax.scatter(X_test_umap[:, 0], 
                        X_test_umap[:, 1],
                        c=y_test, 
                        cmap=plt.cm.viridis)
    plt.colorbar(scatter)
    ax.set_title('Supervised UMAP Embedding')
    return fig}

\endif
