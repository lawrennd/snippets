\ifndef{dimensionalityReductionComparison}
\define{dimensionalityReductionComparison}

\editme

\subsection{Comparing Dimensionality Reduction Methods}

\notes{Different dimensionality reduction methods have different strengths and are suited to different tasks. Here's a comparison of the main approaches we've covered:}

\slides{
* PCA: Linear, fast, interpretable
* MDS: Distance-based, can be non-linear
* t-SNE: Excellent visualization, local structure
* UMAP: Fast, preserves global structure, versatile
}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
import mlai.plot as plot}

\code{def compare_dim_reduction_methods(X, labels, random_state=42):
    """Compare different dimensionality reduction methods"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, 
                                    figsize=plot.big_wide_figsize)
    
    # PCA
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    ax1.scatter(X_pca[:, 0], X_pca[:, 1], 
                c=labels, cmap=plt.cm.viridis)
    ax1.set_title('PCA')
    
    # MDS
    from sklearn.manifold import MDS
    mds = MDS(n_components=2, random_state=random_state)
    X_mds = mds.fit_transform(X)
    ax2.scatter(X_mds[:, 0], X_mds[:, 1], 
                c=labels, cmap=plt.cm.viridis)
    ax2.set_title('MDS')
    
    # t-SNE
    from sklearn.manifold import TSNE
    tsne = TSNE(n_components=2, random_state=random_state)
    X_tsne = tsne.fit_transform(X)
    ax3.scatter(X_tsne[:, 0], X_tsne[:, 1], 
                c=labels, cmap=plt.cm.viridis)
    ax3.set_title('t-SNE')
    
    # UMAP
    import umap
    reducer = umap.UMAP(random_state=random_state)
    X_umap = reducer.fit_transform(X)
    ax4.scatter(X_umap[:, 0], X_umap[:, 1], 
                c=labels, cmap=plt.cm.viridis)
    ax4.set_title('UMAP')
    
    plt.tight_layout()
    return fig}

\notes{Here's a summary of when to use each method:

1. **PCA**: 
   * When you need interpretable features
   * When computational speed is important
   * When the data has a linear structure

2. **MDS**: 
   * When you have only distance/similarity information
   * When you want to preserve all pairwise distances
   * When you need a non-linear embedding

3. **t-SNE**:
   * When creating visualizations is the primary goal
   * When local structure is more important than global structure
   * When you have up to a few thousand points

4. **UMAP**:
   * When you need faster computation than t-SNE
   * When both local and global structure are important
   * When you need a reusable transformation
   * When you want to incorporate label information}

\endif
