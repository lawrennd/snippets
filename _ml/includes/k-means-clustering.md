\ifndef{kMeansClustering}
\define{kMeansClustering}

\editme

\subsection{$k$-means Clustering}

\newslide{Mathematical Formulation} 
\slides{
* Represent objects as data vectors $\inputVector_i$
* Represent cluster centres as vectors $\meanVector_j$
* Define similarity/distance between objects and centres
* Distance function: $\distanceScalar_{ij} = \mappingFunction(\inputVector_i, \meanVector_j)$}

\notes{To implement clustering computationally, we need to mathematically represent both our objects and cluster centres as vectors ($\inputVector_i$ and $\meanVector_j$ respectively) and define a notion of either similarity or distance between them. The distance function $\distanceScalar_{ij} = \mappingFunction(\inputVector_i, \meanVector_j)$ measures how far each object is from potential cluster centres. For example, we might cluster customers by representing them through their purchase history and measuring their distance to different customer archetypes.}

\subsection{Squared Distance}
\slides{
* Common choice: squared distance
$$
\distanceScalar_{ij} = (\inputVector_i - \meanVector_j)^2
$$
* Goal: find centres close to many data points}

\notes{A commonly used distance metric is the squared distance: $\distanceScalar_{ij} = (\inputVector_i - \meanVector_j)^2$. This metric appears frequently in machine learning - we saw it earlier measuring prediction errors in regression, and here it measures dissimilarity between data points and cluster centres.}


\newslide{Objective Function}
\slides{
* Given similarity measure, need number of  cluster centres, $\numComps$.
* Find their location by allocating each center to a sub-set of the points and minimizing the sum of the squared errors,}\notes{Once we have decided on the distance or similarity function, we can decide a number of cluster centres, $K$. We find their location by allocating each center to a sub-set of the points and minimizing the sum of the squared errors,}
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
* For $k$-means clustering you need to choose an initial set of centres.
* Optimisation surface has many local optima, algorithm gets stuck in ones near initialisation.}
\notes{One approach to minimizing this objective function is known as *$k$-means clustering*. It is simple and relatively quick to implement, but it is an initialization sensitive algorithm. Initialization is the process of choosing an initial set of parameters before optimization. For $k$-means clustering you need to choose an initial set of centres. In $k$-means clustering your final set of clusters is very sensitive to the initial choice of centres. For more technical details on $k$-means clustering you can watch a video of Alex Ihler introducing the algorithm here.}

\newslide{$k$-means Algorithm}

\slides{* Simple iterative clustering algorithm
* Key steps:
  1. Initialize with random centres
  2. Assign points to nearest center
  3. Update centres as cluster means
  4. Repeat until stable}

\notes{The $k$-means algorithm provides a straightforward approach to clustering data. It requires two key elements: a set of $k$ cluster centres and a way to assign each data point to a cluster. The algorithm follows a simple iterative process:

1. First, initialize cluster centres by randomly selecting $k$ data points
2. Assign each data point to its nearest cluster centre
3. Update each cluster centre by computing the mean of all points assigned to it
4. Repeat steps 2 and 3 until the cluster assignments stop changing

This process is intuitive and relatively easy to implement, though it comes with certain limitations.}

\newslide{Objective Function}

\slides{* Minimizes sum of squared distances:
  $$
  E=\sum_{j=1}^K \sum_{i\ \text{allocated to}\ j}  \left(\dataVector_{i, :} - \meanVector_{j, :}\right)^\top\left(\dataVector_{i, :} - \meanVector_{j, :}\right)
  $$
* Solution not guaranteed to be global or unique
* Represents a non-convex optimization problem}

\notes{The $k$-means algorithm works by minimizing an objective function that measures the sum of squared Euclidean distances between each point and its assigned cluster center. This objective function can be written mathematically as shown above, where $\meanVector_{j, :}$ represents the mean of cluster $j$.

It's important to understand that while this algorithm will always converge to a minimum, this minimum is not guaranteed to be either global or unique. The optimization problem is non-convex, meaning there can be multiple local minima. Different initializations of the cluster centres can lead to different final solutions, which is one of the key challenges in applying $k$-means clustering in practice.}

\loadcode{generate_cluster_data}{mlai}
\loadcode{dist2}{mlai}
\loadcode{kmeans_assignments}{mlai}
\loadcode{kmeans_update}{mlai}
\loadcode{kmeans_objective}{mlai}

\setupcode{import numpy as np}
\code{# Generate synthetic data with cluster structure
np.random.seed(24)
Y = generate_cluster_data(n_points_per_cluster=30)

# Initialize cluster centres from first cluster
# Note: this is a *bad* initialisation so we can observe algorithm.
nclusters = 3
centres = Y[:nclusters, :].copy()}

\code{# Run k-means algorithm for several iterations
niters = 10
centres_store = [centres.copy()]  # Store initial centres
objective_store = [kmeans_objective(Y, centres)]  # Calculate initial objective

print(f"Initial objective: {objective_store[0]:.2f}")
print("Running k-means algorithm...")

for iteration in range(niters):
    centres, assignments = kmeans_update(Y, centres)
    objective = kmeans_objective(Y, centres)
    
    print(f"  Iteration {iteration+1}: objective = {objective:.2f}")
    
    # Store results for plotting
    centres_store.append(centres.copy())
    objective_store.append(objective)

print(f"Final objective: {objective_store[-1]:.2f}")
print(f"Objective improvement: {objective_store[0] - objective_store[-1]:.2f}")}


\setupplotcode{from matplotlib import pyplot as plt
import mlai
from mlai import plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
colors = ['red', 'green', 'blue']  # Colors for each cluster
markers = ['x', 'o', '+']  # Different markers for each cluster

centres = centres_store[0]
objective = objective_store[0]

# Plot initial data
h_data = ax.plot(Y[:, 0], Y[:, 1], '.', color='black', markersize=10, alpha=0.6)[0]
ax.set_xlabel('$y_1$')
ax.set_ylabel('$y_2$')
ax.grid(True, alpha=0.3)

# Save initial plot
counter = 0
mlai.write_figure_caption(counter, 'Data set to be analysed and initialise cluster centres.', filestub="kmeans_clustering", ext="svg", directory="\writeDiagramsDir/ml")

# Plot initial centres
h_centres = ax.plot(centres_store[0][:, 0], centres_store[0][:, 1], 'o', color='black', 
        linewidth=3, markersize=12)[0]

counter += 1
mlai.write_figure_caption(counter, 'Allocate each point to the cluster with the nearest centre', filestub="kmeans_clustering", ext="svg", directory="\writeDiagramsDir/ml")

# Compute initial assignments
assignments = kmeans_assignments(Y, centres)

# Initialize plot handles for each cluster
h_points = [None]*nclusters
h_data.set_data([], [])
for cluster_id in range(nclusters):
    cluster_mask = assignments == cluster_id
    if np.any(cluster_mask):  # Only plot if cluster has points
        h_points[cluster_id] = ax.plot(Y[cluster_mask, 0], Y[cluster_mask, 1], 
                markers[cluster_id], color=colors[cluster_id], 
                markersize=10, alpha=0.7)[0]  # Get the Line2D object

counter += 1
mlai.write_figure_caption(counter, 'Initial centre allocations', filestub="kmeans_clustering", ext="svg", directory="\writeDiagramsDir/ml")
for iteration in range(len(centres_store)-1):
    centres = centres_store[iteration+1]
    assignments = kmeans_assignments(Y, centres)
    objective = objective_store[iteration+1]
    
    # Update centres plot
    h_centres.set_data(centres[:, 0], centres[:, 1])
	
    # Save plot for animation
    counter += 1
    print(f"Plot {counter}")
    mlai.write_figure_caption(counter, f'Iteration {iteration + 1}: Update centres to mean of assigned points', filestub="kmeans_clustering", ext="svg", directory="\writeDiagramsDir/ml")
	
    
    # Update data points for each cluster
    for cluster_id in range(nclusters):
        cluster_mask = assignments == cluster_id
        if np.any(cluster_mask):  # Only update if cluster has points
            if h_points[cluster_id] is None:
                # Create new plot handle if it doesn't exist
                h_points[cluster_id] = ax.plot(Y[cluster_mask, 0], Y[cluster_mask, 1], 
                     markers[cluster_id], color=colors[cluster_id], 
                     markersize=10, alpha=0.7)[0]
            else:
                # Update existing plot handle
                h_points[cluster_id].set_data(Y[cluster_mask, 0], Y[cluster_mask, 1])
        else:
            # Hide cluster if it has no points
            if h_points[cluster_id] is not None:
                h_points[cluster_id].set_data([], [])
    
    # Save plot for animation
    counter += 1
    print(f"Plot {counter}")
    mlai.write_figure_caption(counter, f'Iteration {iteration + 1}: Update assignments to centres', filestub="kmeans_clustering", ext="svg", directory="\writeDiagramsDir/ml")}
    
    
\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots("kmeans_clustering_{counter:0>3}.svg", directory="\writeDiagramsDir/ml", 
                            text_top='kmeans_clustering_{counter:0>3}.tex', counter=(0, 22))}

\newslide{$k$-Means Clustering}

\slides{
\define{\width}{40%}
\define{animationName}{kmeans-clustering}
\startanimation{\animationName}{0}{22}{$k$-means}
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_000}{\width}}{\animationName}
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
\newframe{\includediagram{\diagramsDir/ml/kmeans_clustering_022}{\width}}{\animationName}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/kmeans_clustering_022}{\width}}{Clustering with the $k$-means clustering algorithm.}{kmeans-clustering-022}}

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




\endif
