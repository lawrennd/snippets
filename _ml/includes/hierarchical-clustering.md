\ifndef{hierarchicalClustering}
\define{hierarchicalClustering}

\editme

\subsection{Hierarchical Clustering}

\newslide{Mathematical Formulation}
\slides{
* Start with each data point as its own cluster
* Define distance between clusters (linkage criterion)
* At each step, merge the two closest clusters
* Continue until all points are in one cluster
* Result: A tree structure (dendrogram) showing merge history}

\notes{Hierarchical clustering builds a tree structure by iteratively merging the closest clusters. Unlike k-means, we don't need to specify the number of clusters in advance. Instead, we start with each point as its own cluster and merge the closest pairs until we have one cluster containing all points. The result is a dendrogram - a tree that shows the complete merge history and allows us to extract any number of clusters by cutting the tree at different heights.}

\subsection{Linkage Criteria}

\slides{
* **Single linkage**: Distance between closest points in clusters
* **Complete linkage**: Distance between farthest points in clusters  
* **Average linkage**: Average distance between all point pairs
* **Ward linkage**: Minimizes within-cluster variance increase}

\notes{The choice of linkage criterion determines how we measure distance between clusters. Single linkage uses the minimum distance between any two points in different clusters, making it sensitive to outliers. Complete linkage uses the maximum distance, creating more compact clusters. Average linkage provides a balance, while Ward linkage minimizes the increase in within-cluster variance, often producing more balanced cluster sizes.}

\newslide{Algorithm}

\slides{
* **Step 1**: Start with n clusters (one per point)
* **Step 2**: Compute distance matrix between all clusters
* **Step 3**: Find and merge the two closest clusters
* **Step 4**: Update distance matrix
* **Step 5**: Repeat until one cluster remains}

\notes{The agglomerative hierarchical clustering algorithm follows a simple iterative process. We start with each data point as its own cluster, then repeatedly find the two closest clusters and merge them. After each merge, we update our distance matrix to reflect the new cluster structure. This process continues until all points belong to a single cluster, creating a complete merge history that we can visualize as a dendrogram.}

\setupcode{import mlai
import numpy as np
import matplotlib.pyplot as plt
from mlai import plot}

\helpercode{def generate_cluster_data_hierarchical(n_points_per_cluster=20):
    """Generate synthetic data with clear cluster structure for hierarchical clustering"""
    # Define cluster centres in 2D space
    cluster_centres = np.array([[2, 2], [-2, 2], [0, -2]])
    
    # Generate data points around each centre
    data_points = []
    for centre in cluster_centres:
        cluster_points = np.random.normal(loc=centre, scale=0.6, size=(n_points_per_cluster, 2))
        data_points.append(cluster_points)
    
    return np.vstack(data_points)

}
\loadcode{generate_cluster_data}{mlai}

\loadcode{ClusterModel}{mlai}
\loadcode{WardsMethod}{mlai}

\code{# Generate synthetic data with cluster structure
np.random.seed(24)
Y = generate_cluster_data(n_points_per_cluster=30)

# Apply Ward's method using scipy (more reliable)
from scipy.cluster.hierarchy import linkage, ward
from scipy.spatial.distance import pdist

# Compute pairwise distances
distances = pdist(Y, metric='euclidean')

# Apply Ward linkage
linkage_matrix = ward(distances)

print(f"\nFinal clustering completed in {len(linkage_matrix)} steps")
print(f"Ward distances at each step: {[f'{d:.3f}' for d in linkage_matrix[:, 2]]}")}


\setupplotcode{import mlai
from mlai import plot
import matplotlib.pyplot as plt}

\plotcode{fig, ax = plt.subplots(figsize=plot.one_figsize)

# Plot data
ax.plot(Y[:, 0], Y[:, 1], '.', color='black', markersize=10, alpha=0.6)
ax.set_xlabel('$y_1$')
ax.set_ylabel('$y_2$')
ax.grid(True, alpha=0.3)

mlai.write_figure_caption(0, 'Initial data points - each point is its own cluster', 
                         filestub="hierarchical_clustering", ext="svg", directory="\writeDiagramsDir/ml")}

\setupplotcode{from scipy.cluster.hierarchy import dendrogram}

\plotcode{# Plot dendrogram
fig, ax = plt.subplots(figsize=plot.one_figsize)
dendrogram(linkage_matrix, ax=ax)
ax.set_xlabel('Sample Index')
ax.set_ylabel('Distance')

plt.tight_layout()

mlai.write_figure_caption(1, 'Dendogram of the clustering', 
                         filestub="hierarchical_clustering", ext="svg", directory="\writeDiagramsDir/ml")
}


\figure{\columns{\includediagram{\diagramsDir/ml/hierarchical_clustering}{100%}}{\includediagram{\diagramsDir/ml/hierarchical_clustering_dendogram}{100%}}{40%}{40%}}{Hierarchical clustering of some artificial data.}{hierarchical-clustering}


\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots("hierarchical_clustering_{counter:0>3}.svg", directory="\writeDiagramsDir/ml", 
                            text_top='hierarchical_clustering_{counter:0>3}.tex', counter=(0, 1))}


\notes{Other approaches to clustering involve forming taxonomies of the cluster 
centers, like humans apply to animals, to form trees. Hierarchical clustering builds a 
tree structure showing the relationships between data points. We'll demonstrate 
agglomerative clustering on the oil flow data set, which contains measurements from a 
multiphase flow facility.}

\include{_datasets/includes/oil-flow-data.md}
\include{_ml/includes/oil-flow-hierarchical-clustering.md}

\subsection{Phylogenetic Trees}
\slides{
* Hierarchical clustering of genetic sequence data
* Creates evolutionary trees showing species relationships
* Estimates common ancestors and mutation timelines
* Critical for tracking viral evolution and outbreaks
}
\notes{A powerful application of hierarchical clustering is in constructing phylogenetic trees from genetic sequence data. By comparing DNA/RNA sequences across species, we can reconstruct their evolutionary relationships and estimate when species diverged from common ancestors. The resulting tree structure, called a phylogeny, maps out the evolutionary history and relationships between organisms.

Modern phylogenetic methods go beyond simple clustering - they incorporate sophisticated models of genetic mutation and molecular evolution. These models can estimate not just the structure of relationships, but also the timing of evolutionary divergence events based on mutation rates. This has important applications in tracking the origins and spread of rapidly evolving pathogens like HIV and influenza viruses. Understanding viral phylogenies helps epidemiologists trace outbreak sources, track transmission patterns, and develop targeted containment strategies.

[^commonancestor]: Phylogenetic models incorporate molecular clock models that estimate mutation rates over time. By calibrating these with known divergence events from the fossil record, the timing of common ancestors can be estimated.}

\subsection{Product Clustering}
\slides{
* Hierarchical clustering for e-commerce products
* Creates product taxonomy trees
* Splits into nested categories (e.g. Electronics → Phones → Smartphones)
}
\notes{An e-commerce company could apply hierarchical clustering to organize their product catalog into a taxonomy tree. Products would be grouped into increasingly specific categories - for example, Electronics might split into Phones, Computers, etc., with Phones further dividing into Smartphones, Feature Phones, and so on. This creates an intuitive hierarchical organization. However, many products naturally belong in multiple categories - for instance, running shoes could reasonably be classified as both sporting equipment and footwear. The strict tree structure of hierarchical clustering doesn't allow for this kind of multiple categorization, which is a key limitation for product organization.}

\subsection{Hierarchical Clustering Challenge}
\slides{
* Many products belong in multiple clusters (e.g. running shoes are both 'sporting goods' and 'clothing')
* Tree structures are too rigid for natural categorization
* Human concept learning is more flexible:
    * Forms overlapping categories
    * Learns abstract rules
    * Builds causal theories}
\notes{Our psychological ability to form categories is far more sophisticated than hierarchical trees. Research in cognitive science has revealed that humans naturally form overlapping categories and learn abstract principles that guide classification. Josh Tenenbaum's influential work demonstrates how human concept learning combines multiple forms of inference through hierarchical Bayesian models that integrate similarity-based clustering with theory-based reasoning. This computational approach aligns with foundational work by Eleanor Rosch on prototype theory and Susan Carey's research on conceptual change, showing how categorization adapts to context and goals. While these cognitively-inspired models better capture human-like categorization, their computational complexity currently limits practical applications to smaller datasets. Nevertheless, they provide important insights into more flexible clustering approaches that could eventually enhance machine learning systems.}

\endif
