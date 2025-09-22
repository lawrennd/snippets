\ifndef{hierarchicalClusteringChimpanzees}
\define{hierarchicalClusteringChimpanzees}

\editme

\subsection{Hierarchical Clustering}

\notes{Hierarchical clustering is an alternative method, where all elements are at first considered their own clusters, and repetetively join the closest clusters together, until only one remains. This is very nicely visualised using [dendrograms](https://en.wikipedia.org/wiki/Dendrogram).}

\codeassignment{Using our earlier dataset, let's conduct hierarchical clustering, and produce a dendrogram.}{import numpy as np

def cluster_hierarchical_handwritten(X):
    n_samples = X.shape[0]
    clusters = {i: [i] for i in range(n_samples)}
    distances = np.full((2*n_samples-1, 2*n_samples-1), np.inf)

    # compute pairwise distances
    for i in range(n_samples):
        for j in range(i+1, n_samples):
            pass # TODO compute and set distances between samples

    Z = []
    next_cluster = n_samples

    while len(clusters) > 1:
        # find closest pair
        keys = list(clusters.keys())
        min_d, pair = np.inf, None
        for i in range(len(keys)):
            for j in range(i+1, len(keys)):
                pass # TODO calculate distance between clusters, if new best, update min_d and pair

        i, j = pair
        new_cluster = clusters[i] + clusters[j]
        Z.append([i, j, min_d, len(new_cluster)])
        clusters[next_cluster] = new_cluster
        del clusters[i], clusters[j]
        next_cluster += 1

    return np.array(Z)}{}

\setupcode{from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from scipy.cluster.hierarchy import dendrogram}

\helpercode{def show_dendrogram(Z, paths, zoom=0.15):
    fig, (ax_dendro, ax_imgs) = plt.subplots(2, 1, figsize=(13, 6), gridspec_kw={"height_ratios": [100, 1]})
    dendro = dendrogram(Z, no_labels=True, ax=ax_dendro)
    ax_dendro.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax_imgs.set_xlim(ax_dendro.get_xlim())
    ax_imgs.set_ylim(0, 1)
    ax_imgs.axis("off")
    leaves = dendro["leaves"]
    xmin, xmax = ax_dendro.get_xlim()
    margin = 0.02 * (xmax - xmin)
    x_positions = np.linspace(xmin + margin, xmax - margin, num=len(leaves))

    for x, leaf_idx in zip(x_positions, leaves):
        img = mpimg.imread(paths[leaf_idx])
        imagebox = OffsetImage(img, zoom=zoom)
        ab = AnnotationBbox(imagebox, (x, 0.5), frameon=False)
        ax_imgs.add_artist(ab)

    plt.tight_layout()
    plt.show()}

\code{linkage_output = cluster_hierarchical_handwritten(embeddings_2d)
show_dendrogram(linkage_output, paths)}

\endif
