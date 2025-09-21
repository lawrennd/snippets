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

def single_linkage_distance(cluster1, cluster2):
    """Calculate single linkage distance between two clusters"""
    min_dist = np.inf
    for point1 in cluster1:
        for point2 in cluster2:
            dist = np.sqrt(np.sum((point1 - point2)**2))
            min_dist = min(min_dist, dist)
    return min_dist

def hierarchical_clustering_step(data, clusters, linkage='single'):
    """Perform one step of hierarchical clustering"""
    if len(clusters) <= 1:
        return clusters, None, None
    
    # Find the two closest clusters
    min_dist = np.inf
    merge_i, merge_j = 0, 1
    
    for i in range(len(clusters)):
        for j in range(i+1, len(clusters)):
            if linkage == 'single':
                dist = single_linkage_distance(clusters[i], clusters[j])
            else:
                # For simplicity, use single linkage for now
                dist = single_linkage_distance(clusters[i], clusters[j])
            
            if dist < min_dist:
                min_dist = dist
                merge_i, merge_j = i, j
    
    # Merge the two closest clusters
    new_clusters = []
    for k, cluster in enumerate(clusters):
        if k != merge_i and k != merge_j:
            new_clusters.append(cluster)
        elif k == merge_i:
            new_clusters.append(clusters[merge_i] + clusters[merge_j])
    
    return new_clusters, merge_i, merge_j}

\code{# Generate small synthetic data for testing
np.random.seed(42)
# Create just 6 points in 2 clear clusters
Y = np.array([
    [1, 1], [1.2, 1.1], [1.1, 0.9],  # Cluster 1
    [3, 3], [3.2, 3.1], [3.1, 2.9]   # Cluster 2
])

print(f"Data points: {Y.shape[0]} points")
print("Points:")
for i, point in enumerate(Y):
    print(f"  Point {i}: ({point[0]:.1f}, {point[1]:.1f})")

# Initialize: each point is its own cluster
clusters = [[point] for point in Y]
merge_history = []
distances = []

print(f"\nStarting with {len(clusters)} clusters")
print("Running hierarchical clustering...")

# Run hierarchical clustering for just a few steps
step = 0
max_steps = 3  # Just do 3 merges for testing

while len(clusters) > 1 and step < max_steps:
    old_clusters = [cluster.copy() for cluster in clusters]
    clusters, merge_i, merge_j = hierarchical_clustering_step(Y, clusters)
    
    if merge_i is not None and merge_j is not None:
        # Calculate distance between the clusters that were merged
        if merge_i < len(old_clusters) and merge_j < len(old_clusters):
            dist = single_linkage_distance(old_clusters[merge_i], old_clusters[merge_j])
        else:
            dist = 0
        
        merge_history.append((merge_i, merge_j))
        distances.append(dist)
        
        print(f"  Step {step+1}: Merged clusters {merge_i} and {merge_j}, distance = {dist:.3f}")
        print(f"    Remaining clusters: {len(clusters)}")
        step += 1

print(f"Final result: {len(clusters)} cluster(s)")
print(f"Total merge steps: {len(merge_history)}")}

\setupplotcode{from matplotlib import pyplot as plt
import mlai
from mlai import plot}

\plotcode{# Create simple figure focusing on data points
fig, ax = plt.subplots(figsize=(8, 6))

# Set up the plot
ax.set_xlabel('$y_1$')
ax.set_ylabel('$y_2$')
ax.grid(True, alpha=0.3)

# Plot initial data points with labels
h_points = []
h_lines = []  # Track connecting lines
h_centers = []  # Track cluster centers
for i, point in enumerate(Y):
    h = ax.plot(point[0], point[1], '.', color='black', markersize=12, alpha=0.8)
    h_points.append(h[0])
    # Add point labels
    ax.annotate(f'{i}', (point[0], point[1]), xytext=(5, 5), 
                textcoords='offset points', fontsize=10, fontweight='bold')

ax.set_xlim(0.5, 3.5)
ax.set_ylim(0.5, 3.5)

# Save initial plot
counter = 0
mlai.write_figure_caption(counter, 'Initial data points - each point is its own cluster', 
                         filestub="hierarchical_clustering", ext="svg", directory="\writeDiagramsDir/ml")

# Now run the clustering step by step
clusters = [[point] for point in Y]
step = 0
max_steps = 5  # Need 5 steps to go from 6 points to 1 cluster

while len(clusters) > 1 and step < max_steps:
    # Store old clusters before merging
    old_clusters = [cluster.copy() for cluster in clusters]
    
    # Perform one merge step
    clusters, merge_i, merge_j = hierarchical_clustering_step(Y, clusters)
    
    if merge_i is not None and merge_j is not None:
        print(f"Visualising step {step+1}: merging clusters {merge_i} and {merge_j}")
        
        # Get the points that were merged
        cluster_i_points = old_clusters[merge_i]
        cluster_j_points = old_clusters[merge_j]
        
        # Step 1: Show connection (draw lines between points being merged)
        current_lines = []
        
        # Handle case where clusters might be single points (cluster centers) or arrays of points
        if len(cluster_i_points) == 1 and len(cluster_j_points) == 1:
            # Both are single points (could be cluster centers)
            point_i = cluster_i_points[0]
            point_j = cluster_j_points[0]
            line = ax.plot([point_i[0], point_j[0]], [point_i[1], point_j[1]], 
                         'r-', linewidth=3, alpha=0.7)
            current_lines.append(line[0])
        else:
            # At least one cluster has multiple points, draw lines between all combinations
            for point_i in cluster_i_points:
                for point_j in cluster_j_points:
                    line = ax.plot([point_i[0], point_j[0]], [point_i[1], point_j[1]], 
                                 'r-', linewidth=3, alpha=0.7)
                    current_lines.append(line[0])
        
        # Store the lines for later hiding
        h_lines.extend(current_lines)
        
        counter += 1
        mlai.write_figure_caption(counter, f'Step {step+1}: Connect clusters {merge_i} and {merge_j}', 
                                 filestub="hierarchical_clustering", ext="svg", directory="\writeDiagramsDir/ml")
        
        # Step 2: Show merge (replace individual points with cluster center)
        # Calculate the center of the merged cluster
        all_merged_points = cluster_i_points + cluster_j_points
        cluster_center = np.mean(all_merged_points, axis=0)
        
        # Hide the individual points that were merged by setting their data to empty
        print(f"  Hiding points that were merged...")
        points_to_hide = []
        
        # Check if we're merging individual data points (not cluster centers)
        if len(cluster_i_points) > 1 or len(cluster_j_points) > 1:
            # We're merging individual data points, hide them
            for i, point in enumerate(Y):
                # Check if this point is in either of the merged clusters
                in_cluster_i = any(np.allclose(point, cluster_point, atol=1e-10) for cluster_point in cluster_i_points)
                in_cluster_j = any(np.allclose(point, cluster_point, atol=1e-10) for cluster_point in cluster_j_points)
                
                if in_cluster_i or in_cluster_j:
                    h_points[i].set_data([], [])  
                    points_to_hide.append(i)
                    print(f"    Hiding point {i}: {point}")
        else:
            # We're merging cluster centers, don't hide individual data points
            print(f"    Merging cluster centers, not hiding individual data points")
        
        print(f"  Hidden {len(points_to_hide)} points: {points_to_hide}")
        
        # Hide the connecting lines from this step when the cluster center appears
        for line in current_lines:
            line.set_data([], [])
        
        # Hide old cluster centers that were merged
        # When we merge clusters, we need to hide the centers that represent the individual clusters being merged
        print(f"  Checking which centers to hide...")
        centers_to_hide = []
        
        # Check each existing center to see if it's being merged
        for i, center in enumerate(h_centers):
            center_pos = center.get_data()
            if len(center_pos[0]) > 0:  # Center is still visible
                center_x, center_y = center_pos[0][0], center_pos[1][0]
                center_point = np.array([center_x, center_y])
                
                # Check if this center is in either of the merged clusters
                in_cluster_i = any(np.allclose(center_point, cluster_point, atol=1e-10) for cluster_point in cluster_i_points)
                in_cluster_j = any(np.allclose(center_point, cluster_point, atol=1e-10) for cluster_point in cluster_j_points)
                
                if in_cluster_i or in_cluster_j:
                    center.set_data([], [])  # Hide the center
                    centers_to_hide.append(i)
                    print(f"    Hiding center {i}: {center_point}")
        
        print(f"  Hidden {len(centers_to_hide)} centers: {centers_to_hide}")
        
        # Add the new cluster center
        center = ax.plot(cluster_center[0], cluster_center[1], 'o', color='red', markersize=12, 
                        markeredgecolor='red', markeredgewidth=2)
        h_centers.append(center[0])
        
        # Add annotation for the cluster center
        ax.annotate(f'C{step+1}', (cluster_center[0], cluster_center[1]), 
                   xytext=(0, -20), textcoords='offset points', 
                   fontsize=12, fontweight='bold', ha='center')
        
        counter += 1
        mlai.write_figure_caption(counter, f'Step {step+1}: Merge into cluster center', 
                                 filestub="hierarchical_clustering", ext="svg", directory="\writeDiagramsDir/ml")
        
        step += 1}

\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots("hierarchical_clustering_{counter:0>3}.svg", directory="\writeDiagramsDir/ml", 
                            text_top='hierarchical_clustering_{counter:0>3}.tex', counter=(0, 10))}


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
