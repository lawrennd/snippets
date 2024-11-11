\ifndef{clustering}
\define{clustering}

\editme

\subsection{Clustering}

\newslide{Clustering}

* Common approach for grouping data points
* Assigns data points to discrete groups
* Examples include:
  * Animal classification
  * Political affiliation grouping

\notes{Clustering is a common approach to data analysis, though we will not cover it in great depth in this course. The fundamental idea is to associate each data point $\dataVector_{i, :}$ with one of $k$ different discrete groups. This approach raises interesting questions - for instance, when clustering animals into groups, we might ask whether animal traits are truly discrete or continuous in nature. Similar questions arise when clustering political affiliations.

Humans seem to have a natural affinity for discrete clustering approaches. This makes clustering particularly useful when collaborating with biologists, who often think in terms of discrete categories. However, we should be mindful that this preference for discrete categories may sometimes oversimplify continuous variations in data.}

\newslide{Clustering vs Vector Quantisation}

* Clustering expects gaps between groups in data density
* Vector quantization may not require density gaps
* For practical purposes, both involve:
  * Allocating points to groups
  * Determining optimal number of groups

\notes{There is a subtle but important distinction between clustering and vector quantisation. In true clustering, we typically expect to see reductions in data density between natural groups - essentially, gaps in the data that separate different clusters. This definition isn't universally applied though, and vector quantization may partition data without requiring such density gaps. For our current discussion, we'll treat them similarly, focusing on the common challenges they share: how to allocate points to groups and, more challengingly, how to determine the optimal number of groups.}

\newslide{$k$-means Clustering}

* Simple iterative clustering algorithm
* Key steps:
  1. Initialize with random centers
  2. Assign points to nearest center
  3. Update centers as cluster means
  4. Repeat until stable

\notes{The $k$-means algorithm provides a straightforward approach to clustering data. It requires two key elements: a set of $k$ cluster centres and a way to assign each data point to a cluster. The algorithm follows a simple iterative process:

1. First, initialize cluster centres by randomly selecting $k$ data points
2. Assign each data point to its nearest cluster centre
3. Update each cluster centre by computing the mean of all points assigned to it
4. Repeat steps 2 and 3 until the cluster assignments stop changing

This process is intuitive and relatively easy to implement, though it comes with certain limitations.}

\newslide{Objective Function}

* Minimizes sum of squared distances:
  $$
  E=\sum_{j=1}^K \sum_{i\ \text{allocated to}\ j}  \left(\dataVector_{i, :} - \meanVector_{j, :}\right)^\top\left(\dataVector_{i, :} - \meanVector_{j, :}\right)
  $$
* Solution not guaranteed to be global or unique
* Represents a non-convex optimization problem

\notes{The $k$-means algorithm works by minimizing an objective function that measures the sum of squared Euclidean distances between each point and its assigned cluster center. This objective function can be written mathematically as shown above, where $\meanVector_{j, :}$ represents the mean of cluster $j$.

It's important to understand that while this algorithm will always converge to a minimum, this minimum is not guaranteed to be either global or unique. The optimization problem is non-convex, meaning there can be multiple local minima. Different initializations of the cluster centers can lead to different final solutions, which is one of the key challenges in applying $k$-means clustering in practice.}

\setupcode{import mlai
import numpy as np
import os}

\helpercode{def write_plot(counter, caption):
    directory = "\writeDiagramsDir/ml"
    filestub = f"kmeans_clustering_{counter:0>3}"
    mlai.write_figure(filestub+".svg", directory=directory)
    f = open(os.path.join(directory,filestub) + '.md', 'w')
    f.write(caption)
    f.close()}

\setupplotcode{from matplotlib import pyplot as plt
from mlai import plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
fontsize = 20

num_clust_points = 30

Y = np.vstack([np.random.normal(size=(num_clust_points, 2)) + 2.5,
       np.random.normal(size=(num_clust_points, 2)) - 2.5,
       np.random.normal(size=(num_clust_points, 2)) + np.array([2.5, -2.5])])

centre_inds = np.random.permutation(Y.shape[0])[:3]
centres = Y[centre_inds, :]

ax.cla()

ax.plot(Y[:, 0], Y[:, 1], '.', color=[0, 0, 0], markersize=10)
ax.set_xlabel('$y_1$')
ax.set_ylabel('$y_2$')
ax.set_title('Data')
counter=0
write_plot(counter, 'Data set to be analyzed. Initialize cluster centres.')
ax.plot(centres[:, 0], centres[:, 1], 'o', color=[0,0,0], linewidth=3, markersize=12)    
counter+=1
write_plot(counter, 'Allocate each point to the cluster with the nearest centre')
i = 0

for i in range(10):
    dist_mat = ((Y[:, :, None] - centres.T[None, :, :])**2).sum(1)
    ind = dist_mat.argmin(1)
    ax.cla()
    ax.plot(Y[ind==0, 0], Y[ind==0, 1], 'x', color= [1, 0, 0], markersize=10)
    ax.plot(Y[ind==1, 0], Y[ind==1, 1], 'o', color=[0, 1, 0], markersize=10)
    ax.plot(Y[ind==2, 0], Y[ind==2, 1], '+', color=[0, 0, 1], markersize=10)
    c = ax.plot(centres[:, 0], centres[:, 1], 'o', color=[0,0, 0], markersize=12, linewidth=3)
    ax.set_xlabel('$y_1$',fontsize=fontsize)
    ax.set_ylabel('$y_2$',fontsize=fontsize)
    ax.set_title('Iteration ' + str(i))
    counter+=1
    write_plot(counter, 'Update each centre by setting to the mean of the allocated points.')
    for j in range(centres.shape[0]):
          centres[j, :] = np.mean(Y[ind==j, :], 0)
    c[0].set_data(centres[:, 0], centres[:, 1])
    counter+=1
    write_plot(counter, 'Allocate each data point to the nearest cluster centre.')}

\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots("kmeans_clustering_{counter:0>3}.svg", directory="\writeDiagramsDir/ml", 
                            text_top='kmeans_clustering_{counter:0>3}.tex', counter=(0, 21))}


\setupplotcode{import matplotlib.pyplot as plt
import numpy as np
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=(5,5))

num_centres = 20
num_data = 200
centres = np.random.normal(size=(num_centres, 2))
w = np.random.normal(size=(num_centres, 2))*0.1
alloc = np.random.randint(0, num_centres, size=(num_data))
sigma = np.random.normal(size=(num_centres, 1))*0.05
epsilon = np.random.normal(size=(num_data,2))*sigma[alloc, :]

Y = w[alloc, :]*np.random.normal(size=(num_data, 1)) + centres[alloc, :] + epsilon

ax.plot(Y[:, 0], Y[:, 1], 'rx')
ax.set_xlabel('$y_1$', fontsize=20)
ax.set_ylabel('$y_2$', fontsize=20)

mlai.write_figure("cluster_data00.svg", directory="\writeDiagramsDir/ml/")
pi_vals = np.linspace(-np.pi, np.pi, 200)[:, None]
for i in range(num_centres):
    ax.plot(centres[i, 0], centres[i, 1], 'o', markersize=5, color=[0, 0, 0], linewidth=2)
    x = np.hstack([np.sin(pi_vals), np.cos(pi_vals)])
    L = np.linalg.cholesky(np.outer(w[i, :],w[i, :]) + sigma[i]**2*np.eye(2))
    el = np.dot(x, L.T)
    ax.plot(centres[i, 0] + el[:, 0], centres[i, 1] + el[:, 1], linewidth=2, color=[0,0,0])
mlai.write_figure("cluster_data01.svg", directory="\writeDiagramsDir/ml/")}

\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('cluster_data{counter:0>2}.svg', directory='\writeDiagramsDir/ml', counter=(0, 1))}


\slides{
* *Task*: associate data points with different labels.
* Labels are *not* provided by humans.
* Process is intuitive for humans - we do it naturally.}

\notes{Clustering methods associate data points with different labels that are allocated by the computer rather than provided by human annotators. This process is quite intuitive for humans - we naturally cluster our observations of the real world. For example, we cluster animals into groups like birds, mammals, and insects. While these labels can be provided by humans, they were originally invented through a clustering process. With computational clustering, we want to recreate that process of label invention.}

\newslide{Platonic Ideals}
\slides{
* Greek philosopher Plato considered the concept of ideals
* The Platonic ideal bird is the most bird-like bird
* In clustering, we find these ideals as cluster centers
* Data points are allocated to their nearest center}

\notes{When thinking about ideas, the Greek philosopher Plato considered the concept of Platonic ideals - the most quintessential version of a thing, like the most bird-like bird or chair-like chair. In clustering, we aim to define different categories by finding their Platonic ideals (cluster centers) and allocating each data point to its nearest center. This allows computers to form categorizations of data at scales too large for human processing.}

\newslide{Mathematical Formulation} 
\slides{
* Represent objects as data vectors $\inputVector_i$
* Represent cluster centers as vectors $\meanVector_j$
* Define similarity/distance between objects and centers
* Distance function: $\distanceScalar_{ij} = \mappingFunction(\inputVector_i, \meanVector_j)$}

\notes{To implement clustering computationally, we need to mathematically represent both our objects and cluster centers as vectors ($\inputVector_i$ and $\meanVector_j$ respectively) and define a notion of either similarity or distance between them. The distance function $\distanceScalar_{ij} = \mappingFunction(\inputVector_i, \meanVector_j)$ measures how far each object is from potential cluster centers. For example, we might cluster customers by representing them through their purchase history and measuring their distance to different customer archetypes.}

\subsection{Squared Distance}
\slides{
* Common choice: squared distance
$$
\distanceScalar_{ij} = (\inputVector_i - \meanVector_j)^2
$$
* Goal: find centers close to many data points}

\notes{A commonly used distance metric is the squared distance: $\distanceScalar_{ij} = (\inputVector_i - \meanVector_j)^2$. This metric appears frequently in machine learning - we saw it earlier measuring prediction errors in regression, and here it measures dissimilarity between data points and cluster centers.}


\newslide{Objective Function}
\slides{
* Given similarity measure, need number of  cluster centers, $\numComps$.
* Find their location by allocating each center to a sub-set of the points and minimizing the sum of the squared errors,}\notes{Once we have decided on the distance or similarity function, we can decide a number of cluster centers, $K$. We find their location by allocating each center to a sub-set of the points and minimizing the sum of the squared errors,}
$$
\errorFunction(\meanMatrix) = \sum_{i \in \mathbf{i}_j} (\inputVector_i - \meanVector_j)^2
$$
\slides{here $\mathbf{i}_j$ is all indices of  data points allocated to the $j$th center.}\notes{where the notation $\mathbf{i}_j$ represents all the indices of each data point which has been allocated to the $j$th cluster represented by the center $\meanVector_j$.}

\subsection{$k$-Means Clustering}
\slides{
* *$k$-means clustering* is simple and quick to implement.
* Very *initialisation* sensitive.
}

\newslide{Initialisation}
\slides{
* Initialisation is the process of selecting a starting set of parameters.
* Optimisation result can depend on the starting point.
* For $k$-means clustering you need to choose an initial set of centers.
* Optimisation surface has many local optima, algorithm gets stuck in ones near initialisation.}
\notes{One approach to minimizing this objective function is known as *$k$-means clustering*. It is simple and relatively quick to implement, but it is an initialization sensitive algorithm. Initialization is the process of choosing an initial set of parameters before optimization. For $k$-means clustering you need to choose an initial set of centers. In $k$-means clustering your final set of clusters is very sensitive to the initial choice of centers. For more technical details on $k$-means clustering you can watch a video of Alex Ihler introducing the algorithm here.}

\subsection{$k$-Means Clustering}

\slides{
\define{\width}{40%}
\define{animationName}{kmeans-clustering}
\startanimation{\animationName}{1}{26}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_001}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_002}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_003}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_004}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_005}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_006}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_007}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_008}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_009}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_010}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_011}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_012}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_013}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_014}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_015}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_016}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_017}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_018}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_019}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_020}{\width}}{\animationName}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_021}{\width}}{\animationName}
\endanimation

*Clustering with the $k$-means clustering algorithm.*
}

\notes{\figure{\includediagram{\diagramsDir/ml/kmeans_clustering_020}{\width}}{Clustering with the $k$-means clustering algorithm.}{kmeans-clustering-020}}

\newslide{$k$-Means Clustering}

\figure{\includeyoutube{mfqmoUN-Cuw}{600}{450}}{$k$-means clustering by Alex Ihler.}{k-means-clustering}

\slides{*$k$-means clustering by Alex Ihler*}


\subsection{Hierarchical Clustering}

\slides{
* Form taxonomies of the cluster centers
* Like humans apply to animals, to form *phylogenies*
* Builds a tree structure showing relationships between data points
* Two main approaches:
    * Agglomerative (bottom-up): Start with individual points and merge
    * Divisive (top-down): Start with one cluster and split
}

\notes{Other approaches to clustering involve forming taxonomies of the cluster centers, like humans apply to animals, to form trees. Hierarchical clustering builds a tree structure showing the relationships between data points. We'll demonstrate agglomerative clustering on the oil flow data set, which contains measurements from a multiphase flow facility.}

\include{_datasets/includes/oil-flow-data.md}

\setupcode{import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import pods}

\code{# Perform hierarchical clustering
linked = linkage(X, 'ward')  # Ward's method for minimum variance}

\setupplotcode{from matplotlib import pyplot as plt
from mlai import plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
dendrogram(linked,
           orientation='top',
           distance_sort='descending',
           show_leaf_counts=True,
           labels=[f'Class {y}' for y in Y],
           ax=ax)
ax.set_title('Hierarchical Clustering of Oil Flow Data')
ax.set_xlabel('Sample Index')
ax.set_ylabel('Distance')
plt.tight_layout()
mlai.write_figure('hierarchical-clustering-oil.svg', directory='\writeDiagramsDir/dimred')}

\figure{\includediagram{\diagramsDir/dimred/hierarchical-clustering-oil}{80%}}{Hierarchical clustering applied to oil flow data. The dendrogram shows how different flow regimes are grouped based on their measurement similarities. The three main flow regimes (homogeneous, annular, and laminar) should form distinct clusters.}{hierarchical-clustering-oil}

\notes{In this example, we've applied hierarchical clustering to the oil flow data set. The data contains measurements from different flow regimes in a multiphase flow facility. The dendrogram shows how measurements naturally cluster into different flow types. Ward's linkage method is used as it tends to create compact, evenly-sized clusters. You can learn more about agglomerative clustering in this video from Alex Ihler.}

\figure{\includeyoutube{OcoE7JlbXvY}{600}{450}}{Hierarchical Clustering by Alex Ihler.}{alex-ihler-hierarchical-clustering}

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

\subsection{Other Clustering Approaches}

\slides{
* Spectral clustering: Graph-based non-convex clustering
* Dirichlet process: Infinite, non-parametric clustering
}

\notes{Spectral clustering (@Shi:normalized00,@Ng:spectral02) is a powerful technique that uses eigenvalues of similarity matrices to perform dimensionality reduction before clustering. Unlike k-means, it can identify clusters of arbitrary shape, making it effective for complex data like image segmentation or social networks.

The Dirichlet process provides a Bayesian framework for clustering without pre-specifying the number of clusters. It's particularly valuable in scenarios where new, previously unseen categories may emerge over time. For example, in species discovery, it can model the probability of finding new species while accounting for known ones. This "infinite clustering" property makes it well-suited for open-ended learning problems where the total number of categories is unknown.}


\endif
