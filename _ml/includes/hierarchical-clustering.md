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
* *Single linkage*: Distance between closest points in clusters
* *Complete linkage*: Distance between farthest points in clusters  
* *Average linkage*: Average distance between all point pairs
* *Ward linkage*: Minimises within-cluster variance increase}

\notes{The choice of linkage criterion determines how we measure distance between clusters. Single linkage uses the minimum distance between any two points in different clusters, making it sensitive to outliers. Complete linkage uses the maximum distance, creating more compact clusters. Average linkage provides a balance, while Ward linkage minimizes the increase in within-cluster variance, often producing more balanced cluster sizes.}

\subsection{Ward's Criterion}

\slides{
* Ward's method minimizes the increase in within-cluster variance
* Mathematical formulation: $\Delta = \frac{n_i n_j}{n_i + n_j} \|\mathbf{c}_i - \mathbf{c}_j\|^2$
* Where $\mathbf{c}_i, \mathbf{c}_j$ are cluster centroids and $n_i, n_j$ are cluster sizes
* Creates compact, roughly spherical clusters
* Particularly effective for data with clear cluster structure}

\notes{Ward's criterion minimises the increase in within-cluster sum of squares (WCSS) when merging two clusters. The mathematical formulation is $\Delta = \frac{n_i n_j}{n_i + n_j} \|\mathbf{c}_i - \mathbf{c}_j\|^2$, where $\mathbf{c}_i$ and $\mathbf{c}_j$ are the centroids of clusters $i$ and $j$, and $n_i, n_j$ are their respective sizes. This formula balances the distance between cluster centroids with their sizes - larger clusters are penalized more heavily for being far apart, encouraging the formation of compact, well-separated groups.}

\slides{
* **Why Ward's works well:**
  * Minimises information loss during merging
  * Creates clusters with minimal internal variance
  * Produces balanced cluster sizes
  * Mathematically optimal for spherical clusters}

\notes{Ward's method chooses the merge that result in the smallest possible increase in total within-cluster variance. This means that at each step, we're making the locally optimal choice that preserves the most information about our data structure. The method is particularly effective when the underlying clusters are roughly spherical and well-separated. It creates compact, convex clusters. The weighting by cluster size ($\frac{n_i n_j}{n_i + n_j}$) ensures that we don't prematurely merge large clusters with small outliers, leading to more balanced and interpretable results.}

\subsection{Mathematical Derivation}

\slides{
* *Within-cluster sum of squares (WCSS):*
  * $WCSS = \sum_{i=1}^k \sum_{\mathbf{x} \in C_i} \|\mathbf{x} - \mathbf{c}_i\|^2$
* *Ward's criterion:* Minimise increase in WCSS when merging
* This is the same criterion as used for objective in $k$-means
* **Key insight:** For spherical clusters, this is equivalent to minimising centroid distance weighted by cluster sizes}

\notes{We can show that Ward's method is optimal for spherical clusters. We can derive the relationship between cluster merging and within-cluster variance. The within-cluster sum of squares (WCSS) measures the total squared distance from each point to its cluster centroid: $WCSS = \sum_{i=1}^k \sum_{\mathbf{x} \in C_i} \|\mathbf{x} - \mathbf{c}_i\|^2$. This is exactly the same objective function that $k$-means clustering minimises. When we merge two clusters, we want to minimise the increase in this total variance.}

\newslide{Mathematical Derivation of Ward Distance}

\slides{
* Start with two clusters $C_i$ and $C_j$ with centroids $\mathbf{c}_i, \mathbf{c}_j$
* After merging: new centroid 
  $$
  \mathbf{c}_{ij} = \frac{n_i \mathbf{c}_i + n_j \mathbf{c}_j}{n_i + n_j}
  $$
* Increase in WCSS: 
  $$
  \Delta = \frac{n_i n_j}{n_i + n_j} \|\mathbf{c}_i - \mathbf{c}_j\|^2
  $$}

\notes{Consider two clusters $C_i$ and $C_j$ with $n_i$ and $n_j$ points respectively, and centroids $\mathbf{c}_i$ and $\mathbf{c}_j$. When we merge them, the new centroid becomes $\mathbf{c}_{ij} = \frac{n_i \mathbf{c}_i + n_j \mathbf{c}_j}{n_i + n_j}$.}

\newslide{Mathematical Derivation - II}

\slides{
* *Step 1:* Original WCSS for separate clusters
  $$
  WCSS_{original} = \sum_{\mathbf{x} \in C_i} \|\mathbf{x} - \mathbf{c}_i\|^2 + \sum_{\mathbf{x} \in C_j} \|\mathbf{x} - \mathbf{c}_j\|^2
  $$
* *Step 2:* New WCSS after merging
  $$
  WCSS_{new} = \sum_{\mathbf{x} \in C_i \cup C_j} \|\mathbf{x} - \mathbf{c}_{ij}\|^2
  $$
* *Step 3:* Increase in WCSS
  $$
  \Delta = WCSS_{new} - WCSS_{original}
  $$}

\notes{The increase in WCSS is $\Delta = WCSS_{new} - WCSS_{original}$. Let's expand this step by step. For the new cluster, we have:}

\newslide{Mathematical Derivation - III}

\slides{
* *Expanding the new WCSS:*
  $$
  WCSS_{new} = \sum_{\mathbf{x} \in C_i} \|\mathbf{x} - \mathbf{c}_{ij}\|^2 + \sum_{\mathbf{x} \in C_j} \|\mathbf{x} - \mathbf{c}_{ij}\|^2
  $$
* **Key identity:** 
  $$
  \|\mathbf{x} - \mathbf{c}_{ij}\|^2 = \|\mathbf{x} - \mathbf{c}_i\|^2 + \|\mathbf{c}_i - \mathbf{c}_{ij}\|^2 + 2(\mathbf{x} - \mathbf{c}_i)^T(\mathbf{c}_i - \mathbf{c}_{ij})$$}

\notes{Using the identity $\|\mathbf{x} - \mathbf{c}_{ij}\|^2 = \|\mathbf{x} - \mathbf{c}_i\|^2 + \|\mathbf{c}_i - \mathbf{c}_{ij}\|^2 + 2(\mathbf{x} - \mathbf{c}_i)^T(\mathbf{c}_i - \mathbf{c}_{ij})$, we can expand the new WCSS. The cross-term $2(\mathbf{x} - \mathbf{c}_i)^T(\mathbf{c}_i - \mathbf{c}_{ij})$ sums to zero because $\sum_{\mathbf{x} \in C_i} (\mathbf{x} - \mathbf{c}_i) = 0$ by definition of centroid.}

\newslide{Mathematical Derivation - IV}

\slides{
* *After simplification:*
  $$
  WCSS_{new} = WCSS_{original} + n_i \|\mathbf{c}_i - \mathbf{c}_{ij}\|^2 + n_j \|\mathbf{c}_j - \mathbf{c}_{ij}\|^2
  $$
* *Substituting the centroid formula:*
  $$
  \mathbf{c}_{ij} = \frac{n_i \mathbf{c}_i + n_j \mathbf{c}_j}{n_i + n_j}
  $$
* **Final result:**
  $$
  \Delta = \frac{n_i n_j}{n_i + n_j} \|\mathbf{c}_i - \mathbf{c}_j\|^2
  $$}

\notes{We can manipulate to find that 
$$
\Delta = n_i \|\mathbf{c}_i - \mathbf{c}_{ij}\|^2 + n_j \|\mathbf{c}_j - \mathbf{c}_{ij}\|^2$. Substituting $\mathbf{c}_{ij} = \frac{n_i \mathbf{c}_i + n_j \mathbf{c}_j}{n_i + n_j}
$$ 
and simplifying, we get the Ward distance formula
$$
\Delta = \frac{n_i n_j}{n_i + n_j} \|\mathbf{c}_i - \mathbf{c}_j\|^2.
$$}

\newslide{Local Optimality}
\slides{
* *Why this works well for spherical clusters:*
  * Spherical clusters have minimal WCSS for given number of points
  * Ward's method makes *locally* optimal choices at each merge step
  * The weighting $\frac{n_i n_j}{n_i + n_j}$ prevents premature merging of large clusters}

\notes{For spherical clusters, the WCSS is minimised when points are as close as possible to their centroid. Ward's method makes locally optimal choices by always choosing the merge that results in the smallest possible increase in total variance. However, this is *greedy optimal*, it makes the best choice at each step without considering the global consequences. The weighting factor we derived, $\frac{n_i n_j}{n_i + n_j}$, ensures that merging two large clusters is penalised more heavily than merging small clusters, preventing the algorithm from prematurely combining large, well-separated groups. While Ward's method is not guaranteed to find the globally optimal hierarchical clustering, it often produces good results for spherical cluster structures.}

\newslide{Algorithm}

\slides{
* *Step 1*: Start with $\numData$ clusters (one per point)
* *Step 2*: Compute distance matrix between all clusters
* *Step 3*: Find and merge the two closest clusters
* *Step 4*: Update distance matrix
* *Step 5*: Repeat until one cluster remains}

\notes{The agglomerative hierarchical clustering algorithm follows a simple iterative process. We start with each data point as its own cluster, then repeatedly find the two closest clusters and merge them. After each merge, we update our distance matrix to reflect the new cluster structure. This process continues until all points belong to a single cluster, creating a complete merge history that we can visualize as a dendrogram.}

\loadcode{generate_cluster_data}{mlai}

\loadcode{ClusterModel}{mlai}
\loadcode{WardsMethod}{mlai}

\code{# Generate synthetic data with cluster structure
np.random.seed(24)
Y = generate_cluster_data(n_points_per_cluster=30)

ward = WardsMethod(X)
ward.fit()

linkage_matrix = ward.get_linkage_matrix()
print(f'Linkage matrix shape: {linkage_matrix.shape}')

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

mlai.write_figure(filename="hierarchical_clustering_000.svg", directory="\writeDiagramsDir/ml")}

\setupplotcode{from scipy.cluster.hierarchy import dendrogram}

\plotcode{# Plot dendrogram
fig, ax = plt.subplots(figsize=plot.one_figsize)
dendrogram(linkage_matrix, ax=ax)
ax.set_xlabel('Sample Index')
ax.set_ylabel('Distance')

plt.tight_layout()

mlai.write_figure(filename="hierarchical_clustering_001.svg", directory="\writeDiagramsDir/ml")
}


\figure{\columns{\includediagram{\diagramsDir/ml/hierarchical_clustering_000}{100%}}{\includediagram{\diagramsDir/ml/hierarchical_clustering_001}{100%}}{40%}{40%}}{Hierarchical clustering of some artificial data. On the left we have an artificially generated data set containing three clusters. On the right we can see the dendogram formed by clustering using Ward's criterion.}{hierarchical-clustering}


\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots("hierarchical_clustering_{counter:0>3}.svg", directory="\writeDiagramsDir/ml", 
                            text_top='hierarchical_clustering_{counter:0>3}.tex', counter=(0, 1))}

\notes{Note that the hierarchical clustering here doesn't always imply that the data was hierarchical in origin. It's a visualisation of distances between points and clusters. The longer lenghts in the dendogram imply larger distances. Next We'll demonstrate agglomerative clustering on the oil flow data set, which contains measurements from a multiphase flow facility.}

\include{_datasets/includes/oil-flow-data.md}
\include{_ml/includes/oil-flow-hierarchical-clustering.md}

\subsection{Phylogenetic Trees}
\slides{
* Hierarchical clustering of genetic sequence data
* Creates evolutionary trees showing species relationships
* Estimates common ancestors and mutation timelines
* Critical for tracking viral evolution and outbreaks
}
\notes{A powerful application of hierarchical clustering is in constructing phylogenetic trees from genetic sequence data. By comparing DNA/RNA sequences across species, we can reconstruct their evolutionary relationships and estimate when species diverged from common ancestors.[^commonancestor] The resulting tree structure, called a phylogeny, maps out the evolutionary history and relationships between organisms.

These phylogenetic methods go beyond simple linkage methods based on distance, they incorporate models of genetic mutation and molecular evolution. These models can estimate not just the structure of relationships, but also the timing of evolutionary divergence events based on mutation rates. This has important applications in tracking the origins and spread of rapidly evolving pathogens like Covid19, HIV and influenza viruses. Understanding viral phylogenies helps epidemiologists trace outbreak sources, track transmission patterns, and develop targeted containment strategies.}

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

\notes{Our psychological ability to form categories is far more sophisticated than hierarchical trees. Research in cognitive science has revealed that humans naturally form overlapping categories and learn abstract principles that guide classification. Josh Tenenbaum's work (see e.g. @Lake-emergence18) demonstrates how human concept learning combines multiple forms of inference through hierarchical Bayesian models that integrate similarity-based clustering with theory-based reasoning.}

\notes{In practice the simple methods we use for agglomerative clustering to merge clusters care often used for visualisation of the cluster structure even when we don't expect a hieararchy to be present (like the oil flow data and the artificial data above.}

\endif
