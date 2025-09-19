\ifndef{otherClustering}
\define{otherClustering}

\editme

\subsection{Other Clustering Approaches}

\slides{
* Spectral clustering: Graph-based non-convex clustering
* Dirichlet process: Infinite, non-parametric clustering
}

\notes{Spectral clustering (@Shi:normalized00,@Ng:spectral02) is a powerful technique that uses eigenvalues of similarity matrices to perform dimensionality reduction before clustering. Unlike k-means, it can identify clusters of arbitrary shape, making it effective for complex data like image segmentation or social networks.

The Dirichlet process provides a Bayesian framework for clustering without pre-specifying the number of clusters. It's particularly valuable in scenarios where new, previously unseen categories may emerge over time. For example, in species discovery, it can model the probability of finding new species while accounting for known ones. This "infinite clustering" property makes it well-suited for open-ended learning problems where the total number of categories is unknown.}

\endif
