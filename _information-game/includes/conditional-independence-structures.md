\ifndef{conditionalIndependenceStructures}
\define{conditionalIndependenceStructures}

\editme

\subsection{Locality Through Conditional Independence}

\notes{One way to formalize the notion of locality in our information-theoretic framework is through conditional independence structures.}

\notes{When we have a small number of slow modes (M) that act as information reservoirs, they can induce conditional independence between subsets of fast variables (X), creating a form of locality.}

\notes{This approach connects our abstract information-theoretic framework to more intuitive notions of spatial organization and modularity without requiring an explicit spatial embedding.}

\slides{
* Few slow modes can induce conditional independence
* Creates effective locality and modularity
* Emerges naturally from eigenvalue structure
}

\newslide{Entropy Decomposition with Conditional Mutual Information}

\notes{We partition our fast variables X into subsets $X = \{X^1, X^2, ..., X^K\}$, where each $X^k$ might represent variables that are "close" to each other in some abstract sense.}

\notes{The joint entropy of the entire system can be decomposed as
$$
\begin{align}
S(X, M) &= S(M) + S(X|M)\\
&= S(M) + \sum_{k=1}^K S(X^k|M) - \sum_{k=1}^K \sum_{j<k} I(X^k; X^j|M).
\end{align}
$$
Here, $I(X^k; X^j|M)$ is the conditional mutual information between subsets $X^k$ and $X^j$ given M. This term quantifies how much dependence remains between these subsets after accounting for the information in the slow modes M.}

\slides{
* Joint entropy decomposition with subsets of X: $X = \{X^1, X^2, ..., X^K\}$
* $S(X, M) = S(M) + \sum_{k=1}^K S(X^k|M) - \sum_{k=1}^K \sum_{j<k} I(X^k; X^j|M)$
* Conditional mutual information $I(X^k; X^j|M)$ measures remaining dependencies
}

\newslide{Conditional Independence and Locality}

\notes{When the slow modes $M$  capture the global structure of the system, the conditional mutual information terms become very small,
$$
I(X^k; X^j|M) \approx 0 \quad \text{for } j \neq k.
$$
This means that different regions of the system become conditionally independent given the state of the slow modes,
$$
p(X^1, X^2, ..., X^K|M) \approx \prod_{k=1}^K p(X^k|M).
$$
This factorization gives us our notion of locality - each subsystem $X^k$ can be understood in terms of its relationship to the global slow modes $M$, with minimal direct influence from other subsystems.}

**This needs formalising**

\notes{The degree to which this factorization holds depends on the eigenvalue spectrum of the Fisher information matrix. When there's a clear separation between a few very small eigenvalues (corresponding to $M$) and the rest (corresponding to $X$), the factorization becomes more accurate.}

\slides{
* When $I(X^k; X^j|M) \approx 0$, we get conditional independence
* $p(X^1, X^2, ..., X^K|M) \approx \prod_{k=1}^K p(X^k|M)$
* Fast variables in different "regions" interact only through slow modes
* Creates effective locality without explicit spatial embedding
}

\newslide{Connection to Eigenvalue Structure}

\notes{The connection to the eigenvalue spectrum provides a formal link between the abstract mathematics of the game and intuitive notions of spatial organization.}

\notes{When the Fisher information matrix has a few eigenvalues that are much smaller than the rest (large separation of timescales), the corresponding eigenvectors define the slow modes $M$. These slow modes act as sufficient statistics for the interactions between different regions of the system.}

\notes{The conditional independence structure induced by these slow modes creates a graph structure of dependencies. Variables that remain conditionally dependent given $M$ are "closer" to each other than those that become conditionally independent.}

\notes{This is analogous to how in physics, systems with long-range interactions often have a small number of conserved quantities or order parameters (slow modes) that govern the large-scale behavior, while local fluctuations (fast modes) can be treated as approximately independent when conditioned on these global variables.}

\slides{
* Few small eigenvalues → strong conditional independence
* Eigenvectors of these slow modes define "information pathways"
* Creates natural graph structure of dependencies
* Analogous to order parameters in physical systems
}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import scipy.stats as stats
import mlai.plot as plot
import matplotlib.gridspec as gridspec
from matplotlib.colors import LinearSegmentedColormap
}

\helpercode{class ConditionalIndependenceDemo:
    def __init__(self, n_clusters=4, n_vars_per_cluster=5, n_slow_modes=2):
        """
        Demonstrate how slow modes induce conditional independence structures.
        
        Parameters:
        -----------
        n_clusters: int
            Number of variable clusters (regions)
        n_vars_per_cluster: int
            Number of variables in each cluster
        n_slow_modes: int
            Number of slow modes (information reservoir variables)
        """
        self.n_clusters = n_clusters
        self.n_vars_per_cluster = n_vars_per_cluster
        self.n_slow_modes = n_slow_modes
        self.n_total_vars = n_clusters * n_vars_per_cluster + n_slow_modes
        
        # Generate a precision matrix with block structure
        self.precision = self._generate_precision_matrix()
        self.covariance = np.linalg.inv(self.precision)
        
        # Compute eigendecomposition of the precision matrix
        self.eigenvalues, self.eigenvectors = np.linalg.eigh(self.precision)
        
        # Identify slow modes (smallest eigenvalues)
        self.slow_indices = np.argsort(self.eigenvalues)[:n_slow_modes]
        self.fast_indices = np.argsort(self.eigenvalues)[n_slow_modes:]
        
    def _generate_precision_matrix(self):
        """Generate a precision matrix with block structure and slow modes."""
        n = self.n_total_vars
        
        # Start with a block diagonal structure for fast variables
        precision = np.zeros((n, n))
        
        # Create blocks for each cluster
        for i in range(self.n_clusters):
            start_idx = i * self.n_vars_per_cluster
            end_idx = start_idx + self.n_vars_per_cluster
            
            # Within-cluster connections (strong precision = strong direct dependencies)
            block = np.random.uniform(0.7, 1.0, 
                                     (self.n_vars_per_cluster, self.n_vars_per_cluster))
            block = (block + block.T) / 2  # Make symmetric
            np.fill_diagonal(block, 1.0)  # Set diagonal to 1
            
            precision[start_idx:end_idx, start_idx:end_idx] = block
        
        # Add slow modes that connect across clusters
        slow_start = self.n_clusters * self.n_vars_per_cluster
        slow_end = n
        
        # Slow modes have connections to all fast variables
        for i in range(slow_start, slow_end):
            for j in range(slow_start):
                # Weaker connections but present
                precision[i, j] = precision[j, i] = np.random.uniform(0.1, 0.3)
        
        # Slow modes are also connected to each other
        slow_block = np.random.uniform(0.2, 0.4, 
                                      (self.n_slow_modes, self.n_slow_modes))
        slow_block = (slow_block + slow_block.T) / 2
        np.fill_diagonal(slow_block, 0.5)  # Smaller diagonal values = slower modes
        
        precision[slow_start:slow_end, slow_start:slow_end] = slow_block
        
        # Ensure the matrix is positive definite
        min_eig = np.min(np.linalg.eigvalsh(precision))
        if min_eig <= 0:
            precision += np.eye(n) * (abs(min_eig) + 0.01)
            
        return precision
    
    def compute_mutual_information_matrix(self, conditional_on_slow=False):
        """
        Compute pairwise mutual information between variables.
        
        Parameters:
        -----------
        conditional_on_slow: bool
            If True, compute conditional mutual information given slow modes
        
        Returns:
        --------
        mi_matrix: numpy array
            Matrix of (conditional) mutual information values
        """
        n_fast = self.n_clusters * self.n_vars_per_cluster
        mi_matrix = np.zeros((n_fast, n_fast))
        
        if conditional_on_slow:
            # Compute conditional mutual information given slow modes
            # Using Schur complement to get conditional distribution
            slow_idx = slice(n_fast, self.n_total_vars)
            fast_idx = slice(0, n_fast)
            
            # Extract blocks
            P_ff = self.precision[fast_idx, fast_idx]
            
            # Conditional precision of fast variables given slow variables is 
            # just the fast block of the precision matrix
            cond_precision = P_ff
            cond_covariance = np.linalg.inv(cond_precision)
            
            # Compute conditional mutual information from conditional covariance
            for i in range(n_fast):
                for j in range(i+1, n_fast):
                    # For multivariate Gaussian, conditional MI is related to partial correlation
                    partial_corr = -cond_precision[i, j] / np.sqrt(cond_precision[i, i] * cond_precision[j, j])
                    # Convert to mutual information
                    mi = -0.5 * np.log(1 - partial_corr**2)
                    mi_matrix[i, j] = mi_matrix[j, i] = mi
        else:
            # Compute unconditional mutual information
            for i in range(n_fast):
                for j in range(i+1, n_fast):
                    # Extract the 2x2 covariance submatrix
                    subcov = self.covariance[[i, j]][:, [i, j]]
                    
                    # For bivariate Gaussian, MI is related to correlation
                    corr = subcov[0, 1] / np.sqrt(subcov[0, 0] * subcov[1, 1])
                    # Convert correlation to mutual information
                    mi = -0.5 * np.log(1 - corr**2)
                    mi_matrix[i, j] = mi_matrix[j, i] = mi
        
        return mi_matrix
    
    def visualize_conditional_independence(self):
        """Visualize how slow modes induce conditional independence."""
        # Compute mutual information matrices
        mi_unconditional = self.compute_mutual_information_matrix(conditional_on_slow=False)
        mi_conditional = self.compute_mutual_information_matrix(conditional_on_slow=True)
        
        # Create a visualization
        fig = plt.figure(figsize=plot.big_wide_figsize)
        gs = gridspec.GridSpec(2, 3, height_ratios=[1, 1], width_ratios=[1, 1, 0.1])
        
        # Plot the precision matrix with block structure
        ax1 = plt.subplot(gs[0, 0])
        im1 = ax1.imshow(self.precision, cmap='viridis')
        ax1.set_title('Precision Matrix\nBlock structure with slow modes')
        ax1.set_xlabel('Variable index')
        ax1.set_ylabel('Variable index')
        
        # Add lines to delineate the blocks
        for i in range(1, self.n_clusters):
            idx = i * self.n_vars_per_cluster - 0.5
            ax1.axhline(y=idx, color='red', linestyle='-', linewidth=0.5)
            ax1.axvline(x=idx, color='red', linestyle='-', linewidth=0.5)
        
        # Add line to delineate slow modes
        idx = self.n_clusters * self.n_vars_per_cluster - 0.5
        ax1.axhline(y=idx, color='red', linestyle='-', linewidth=1.5)
        ax1.axvline(x=idx, color='red', linestyle='-', linewidth=1.5)
        
        # Plot eigenvalue spectrum
        ax2 = plt.subplot(gs[0, 1])
        ax2.plot(range(self.n_total_vars), np.sort(self.eigenvalues), 'o-')
        ax2.set_title('Eigenvalue Spectrum\nSmall eigenvalues = slow modes')
        ax2.set_xlabel('Index')
        ax2.set_ylabel('Eigenvalue')
        ax2.set_yscale('log')
        ax2.grid(True, alpha=0.3)
        
        # Indicate the separation of eigenvalues
        ax2.axvline(x=self.n_slow_modes-0.5, color='red', linestyle='--')
        ax2.axhspan(-0.1, self.eigenvalues[self.slow_indices].max()*1.1, 
                   color='blue', alpha=0.2)
        ax2.text(self.n_slow_modes/2, self.eigenvalues[self.slow_indices].max()/2, 
                'Slow Modes', ha='center')
        
        # Create a custom colormap that shows difference more clearly
        cmap = LinearSegmentedColormap.from_list('mi_diff', 
                                            [(0, 'blue'), (0.5, 'white'), (1, 'red')])
        
        # Plot unconditional mutual information
        ax3 = plt.subplot(gs[1, 0])
        im3 = ax3.imshow(mi_unconditional, cmap='inferno')
        ax3.set_title('Unconditional Mutual Information\nStrong dependencies between regions')
        ax3.set_xlabel('Fast variable index')
        ax3.set_ylabel('Fast variable index')
        
        # Add lines to delineate the clusters
        for i in range(1, self.n_clusters):
            idx = i * self.n_vars_per_cluster - 0.5
            ax3.axhline(y=idx, color='white', linestyle='-', linewidth=0.5)
            ax3.axvline(x=idx, color='white', linestyle='-', linewidth=0.5)
        
        # Plot conditional mutual information
        ax4 = plt.subplot(gs[1, 1])
        im4 = ax4.imshow(mi_conditional, cmap='inferno')
        ax4.set_title('Conditional Mutual Information\nWeaker dependencies after conditioning on slow modes')
        ax4.set_xlabel('Fast variable index')
        ax4.set_ylabel('Fast variable index')
        
        # Add lines to delineate the clusters
        for i in range(1, self.n_clusters):
            idx = i * self.n_vars_per_cluster - 0.5
            ax4.axhline(y=idx, color='white', linestyle='-', linewidth=0.5)
            ax4.axvline(x=idx, color='white', linestyle='-', linewidth=0.5)
        
        # Add colorbar
        cax = plt.subplot(gs[1, 2])
        cbar = plt.colorbar(im4, cax=cax)
        cbar.set_label('Mutual Information')
        
        plt.tight_layout()
        return fig
    
    def visualize_dependency_graphs(self, threshold=0.1):
        """
        Visualize dependency graphs with and without conditioning on slow modes.
        
        Parameters:
        -----------
        threshold: float
            Threshold for including edges in the graph
        """
        # Compute mutual information matrices
        mi_unconditional = self.compute_mutual_information_matrix(conditional_on_slow=False)
        mi_conditional = self.compute_mutual_information_matrix(conditional_on_slow=True)
        
        # Create dependency graphs
        n_fast = self.n_clusters * self.n_vars_per_cluster
        G_uncond = nx.Graph()
        G_cond = nx.Graph()
        
        # Add nodes
        for i in range(n_fast):
            cluster_id = i // self.n_vars_per_cluster
            # Position nodes in clusters
            angle = 2 * np.pi * (i % self.n_vars_per_cluster) / self.n_vars_per_cluster
            radius = 1.0
            x = (2 + cluster_id % 2) * 3 + radius * np.cos(angle)
            y = (cluster_id // 2) * 3 + radius * np.sin(angle)
            
            G_uncond.add_node(i, pos=(x, y), cluster=cluster_id)
            G_cond.add_node(i, pos=(x, y), cluster=cluster_id)
        
        # Add edges based on mutual information
        for i in range(n_fast):
            for j in range(i+1, n_fast):
                # Unconditional graph
                if mi_unconditional[i, j] > threshold:
                    G_uncond.add_edge(i, j, weight=mi_unconditional[i, j])
                
                # Conditional graph
                if mi_conditional[i, j] > threshold:
                    G_cond.add_edge(i, j, weight=mi_conditional[i, j])
        
        # Create a visualization
        fig = plt.figure(figsize=plot.big_wide_figsize)
        
        # Plot unconditional dependency graph
        ax1 = plt.subplot(1, 2, 1)
        pos_uncond = nx.get_node_attributes(G_uncond, 'pos')
        
        # Color nodes by cluster
        node_colors = [G_uncond.nodes[i]['cluster'] for i in G_uncond.nodes]
        
        # Draw nodes
        nx.draw_networkx_nodes(G_uncond, pos_uncond, 
                              node_color=node_colors, 
                              node_size=100,
                              cmap=plt.cm.tab10,
                              ax=ax1)
        
        # Draw edges with width proportional to mutual information
        edges = G_uncond.edges()
        edge_weights = [G_uncond[u][v]['weight']*3 for u, v in edges]
        
        nx.draw_networkx_edges(G_uncond, pos_uncond, 
                              width=edge_weights, 
                              alpha=0.6,
                              edge_color='gray',
                              ax=ax1)
        
        # Add node labels
        nx.draw_networkx_labels(G_uncond, pos_uncond, font_size=8, ax=ax1)
        
        ax1.set_title('Unconditional Dependency Graph\nMany cross-cluster dependencies')
        ax1.set_axis_off()
        
        # Plot conditional dependency graph
        ax2 = plt.subplot(1, 2, 2)
        pos_cond = nx.get_node_attributes(G_cond, 'pos')
        
        # Color nodes by cluster
        node_colors = [G_cond.nodes[i]['cluster'] for i in G_cond.nodes]
        
        # Draw nodes
        nx.draw_networkx_nodes(G_cond, pos_cond, 
                              node_color=node_colors, 
                              node_size=100,
                              cmap=plt.cm.tab10,
                              ax=ax2)
        
        # Draw edges with width proportional to conditional mutual information
        edges = G_cond.edges()
        edge_weights = [G_cond[u][v]['weight']*3 for u, v in edges]
        
        nx.draw_networkx_edges(G_cond, pos_cond, 
                              width=edge_weights, 
                              alpha=0.6,
                              edge_color='gray',
                              ax=ax2)
        
        # Add node labels
        nx.draw_networkx_labels(G_cond, pos_cond, font_size=8, ax=ax2)
        
        ax2.set_title('Conditional Dependency Graph\nMostly within-cluster dependencies remain')
        ax2.set_axis_off()
        
        plt.tight_layout()
        return fig
}

\code{
# Run the demonstration
np.random.seed(42)  # For reproducibility
demo = ConditionalIndependenceDemo(n_clusters=4, n_vars_per_cluster=5, n_slow_modes=2)
}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai
}

\plotcode{fig1 = demo.visualize_conditional_independence()

mlai.write_figure(filename='conditional-independence-matrices.svg', 
                  directory='\writeDiagramsDir/information-game')

fig2 = demo.visualize_dependency_graphs(threshold=0.1)

mlai.write_figure(filename='conditional-independence-graphs.svg', 
                  directory='\writeDiagramsDir/information-game')}

\newslide{Conditional Independence Visualization}

\figure{\includediagram{\diagramsDir/information-game/conditional-independence-matrices}{70%}}{Visualization of how conditioning on slow modes induces independence between clusters of fast variables.}{conditional-independence-matrices}

\newslide{Dependency Network Structure}

\figure{\includediagram{\diagramsDir/information-game/conditional-independence-graphs}{70%}}{Dependency graphs before and after conditioning on slow modes, showing the emergence of modularity.}{conditional-independence-graphs}

\notes{The visualisation demonstrates how conditioning on slow modes drastically reduces the mutual information between variables in different clusters, while preserving dependencies within clusters. This creates a modular structure where each cluster becomes nearly independent given the state of the slow modes.}

\notes{This modular organization emerges from the eigenvalue structure of the Fisher information matrix, without requiring any explicit spatial embedding or pre-defined notion of locality. The slow modes act as a information bottleneck that encodes the necessary global information while allowing local regions to operate semi-independently.}

\notes{In a physical system, structures like this manifest as the emergence of spatial patterns or functional modules that interact primarily through a small number of global variables. In a neural network, such structures correspond to the formation of specialized modules that handle different aspects of processing while communicating through a compressed global representation.}

\notes{The notions of locality in our framework are not about physical distance, but about the conditional independence structure induced by the slow modes of the system. This abstract notion of locality that can be applied to any system where information flows are important.}


\subsection{Information Topography}

\notes{Building on the conditional independence structure, we can define an "information topography" - a conceptual landscape that characterizes how information flows through the system.}

\notes{This topography emerges from the pattern of mutual information between variables and their dependency on the slow modes. We can visualize this as a landscape where.

1. The "elevation" corresponds to the conditional entropy of variables given the slow modes
2. The "valleys" or "channels" represent strong information pathways between variables
3. The "watersheds" or "ridges" separate regions that are conditionally independent given M}

\notes{Mathematically, we can define a distance metric between variables based on their conditional mutual information,
$$
d_I(X^i, X^j) = \frac{1}{I(X^i; X^j|M) + \epsilon}
$$
where $\epsilon$ is a small constant to avoid division by zero. Variables with higher conditional mutual information are "closer" in this information metric.}

\slides{
* Information topography: landscape of information flow
* "Distance" between variables: $d_I(X^i, X^j) = \frac{1}{I(X^i; X^j|M) + \epsilon}$
* Creates intuitive notions of "information watersheds" and "channels"
}

\subsection{Properties of Information Topography}

\notes{The information topography has several important properties.

1. It is non-Euclidean - the triangle inequality may not hold
2. It is dynamic - changes in the slow modes reshape the entire landscape
3. It is hierarchical - we can define different topographies at different scales by considering different subsets of the slow modes}

\notes{The eigenvalue spectrum of the Fisher information matrix directly shapes this topography. The larger the separation between the few smallest eigenvalues and the rest, the more pronounced the "ridges" in the topography, leading to stronger locality and modularity.}

\notes{This perspective allows us to quantify notions like "information distance" and "information barriers" without requiring an explicit spatial embedding, providing a framework for understanding modularity across different types of complex systems.}

\slides{
* Non-Euclidean, dynamic, and hierarchical
* Shaped by eigenvalue spectrum separation
* Quantifies "information distance" and "barriers"
* Provides unified view of modularity across systems
}

\helpercode{class InformationTopographyDemo:
    def __init__(self, conditional_mi_matrix, n_clusters, n_vars_per_cluster):
        """
        Visualize the information topography based on conditional mutual information.
        
        Parameters:
        -----------
        conditional_mi_matrix: numpy array
            Matrix of conditional mutual information values
        n_clusters: int
            Number of variable clusters
        n_vars_per_cluster: int
            Number of variables per cluster
        """
        self.cmi = conditional_mi_matrix
        self.n_clusters = n_clusters
        self.n_vars_per_cluster = n_vars_per_cluster
        self.n_vars = conditional_mi_matrix.shape[0]
        
    def compute_information_distance(self, epsilon=1e-6):
        """Convert conditional mutual information to a distance metric."""
        # Higher CMI = closer in information space
        # Lower CMI = further apart (conditional independence)
        distance = 1.0 / (self.cmi + epsilon)
        return distance
    
    def visualize_information_landscape(self):
        """Visualize the information topography as a landscape."""
        # Use multidimensional scaling to project the distance matrix to 2D
        from sklearn.manifold import MDS
        
        # Compute information distance matrix
        distance = self.compute_information_distance()
        
        # Apply MDS to embed in 2D space
        mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
        pos = mds.fit_transform(distance)
        
        # Create a visualization
        fig = plt.figure(figsize=plot.big_wide_figsize)
        
        # Plot the embedded points with cluster colors
        ax = fig.add_subplot(111)
        
        # Assign colors by cluster
        colors = plt.cm.tab10(np.linspace(0, 1, self.n_clusters))
        
        for i in range(self.n_vars):
            cluster_id = i // self.n_vars_per_cluster
            ax.scatter(pos[i, 0], pos[i, 1], c=[colors[cluster_id]], 
                      s=100, label=f"Cluster {cluster_id}" if i % self.n_vars_per_cluster == 0 else "")
            ax.text(pos[i, 0] + 0.02, pos[i, 1] + 0.02, str(i), fontsize=9)
        
        # Add connections based on conditional mutual information
        # Stronger connections = higher CMI = lower distance
        threshold = np.percentile(self.cmi[self.cmi > 0], 70)  # Only show top 30% strongest connections
        
        for i in range(self.n_vars):
            for j in range(i+1, self.n_vars):
                if self.cmi[i, j] > threshold:
                    # Line width proportional to mutual information
                    width = self.cmi[i, j] * 5
                    ax.plot([pos[i, 0], pos[j, 0]], [pos[i, 1], pos[j, 1]], 
                           'k-', alpha=0.5, linewidth=width)
        
        # Remove duplicate legend entries
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(), loc='best')
        
        ax.set_title('Information Topography: Variables Positioned by Information Distance')
        ax.set_xlabel('Dimension 1')
        ax.set_ylabel('Dimension 2')
        ax.grid(True, alpha=0.3)
        
        return fig
    
    def visualize_information_landscape_3d(self):
        """Visualize the information topography as a 3D landscape."""
        # Use multidimensional scaling to project the distance matrix to 2D
        from sklearn.manifold import MDS
        from scipy.interpolate import griddata
        
        # Compute information distance matrix
        distance = self.compute_information_distance()
        
        # Apply MDS to embed in 2D space
        mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
        pos = mds.fit_transform(distance)
        
        # Create a visualization
        fig = plt.figure(figsize=plot.big_wide_figsize)
        ax = fig.add_subplot(111, projection='3d')
        
        # Assign colors by cluster
        colors = plt.cm.tab10(np.linspace(0, 1, self.n_clusters))
        
        # Calculate "elevation" based on average distance to other points
        # Higher elevation = more isolated information-wise
        elevation = np.mean(distance, axis=1)
        
        # Normalize to [0,1] range
        elevation = (elevation - elevation.min()) / (elevation.max() - elevation.min())
        
        # Plot the points in 3D
        for i in range(self.n_vars):
            cluster_id = i // self.n_vars_per_cluster
            ax.scatter(pos[i, 0], pos[i, 1], elevation[i], 
                      c=[colors[cluster_id]], s=100, 
                      label=f"Cluster {cluster_id}" if i % self.n_vars_per_cluster == 0 else "")
            ax.text(pos[i, 0], pos[i, 1], elevation[i] + 0.05, str(i), fontsize=9)
        
        # Create a surface representing the information landscape
        # Grid the data
        xi = np.linspace(pos[:, 0].min(), pos[:, 0].max(), 100)
        yi = np.linspace(pos[:, 1].min(), pos[:, 1].max(), 100)
        X, Y = np.meshgrid(xi, yi)
        
        # Interpolate elevation for the grid
        Z = griddata((pos[:, 0], pos[:, 1]), elevation, (X, Y), method='cubic')
        
        # Plot the surface
        surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, linewidth=0)
        
        # Remove duplicate legend entries
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(), loc='best')
        
        ax.set_title('3D Information Topography: Elevation = Information Isolation')
        ax.set_xlabel('Dimension 1')
        ax.set_ylabel('Dimension 2')
        ax.set_zlabel('Information Isolation')
        
        return fig
}

\subsection{Information Topography Visualization}

\code{
# Create the information topography visualization
topo_demo = InformationTopographyDemo(
    demo.compute_mutual_information_matrix(conditional_on_slow=True),
    demo.n_clusters, 
    demo.n_vars_per_cluster
)}

\plotcode{fig3 = topo_demo.visualize_information_landscape()

mlai.write_figure(filename='information-topography-2d.svg', 
                  directory='\writeDiagramsDir/information-game')

fig4 = topo_demo.visualize_information_landscape_3d()

mlai.write_figure(filename='information-topography-3d.svg', 
                  directory='\writeDiagramsDir/information-game')}


\figure{\includediagram{\diagramsDir/information-game/information-topography-2d}{70%}}{Information topography visualized as a 2D landscape with points positioned according to information distance.}{information-topography-2d}

\newslide{3D Information Landscape}

\figure{\includediagram{\diagramsDir/information-game/information-topography-3d}{70%}}{3D visualization of the information landscape where elevation represents information isolation.}{information-topography-3d}

\notes{The visualizations show how the information topography naturally clusters variables that retain high conditional mutual information, creating "basins" of related variables separated by "ridges" of conditional independence. This emergentstructure is determined by the pattern of information flow in the system, particularly the slow modes.}

\notes{This topographical view offers a framework for understanding how complex systems naturally organize into modular structures, even in the absence of explicit design or spatial constraints. The information landscape reveals the natural "fault lines" along which a system can be decomposed and understood.}

\subsection{Temporal Markovian Decomposition}

\notes{The conditional independence framework we've developed for spatial or structural organization can be extended naturally to the temporal domain. Just as slow modes induce conditional independence between different regions in space, they also mediate dependencies between different points in time.}

\notes{If we divide $X$ into past/present $X_0$ and future $X_1$, we can analyze how information flows across time through the slow modes $M$. The entropy can be decomposed into a Markovian component, where $X_0$ and $X_1$ are conditionally independent given $M$, and a non-Markovian component. The conditional mutual information is 
$$
I(X_0; X_1 | M) = \sum_{x_0,x_1,m} p(x_0,x_1,m) \log \frac{p(x_0,x_1|m)}{p(x_0|m)p(x_1|m)},
$$
which measures the remaining dependency between past and future after accounting for the information stored in the slow modes. This provides a quantitative measure of how effectively $M$ serves as a memory that captures temporal dependencies.}

\slides{
- $X$ divided into past/present $X_0$ and future $X_1$
- Same slow modes that induce spatial modularity also mediate temporal dependencies
- Conditional mutual information:
  $$
  I(X_0; X_1 | M) = \sum_{x_0,x_1,m} p(x_0,x_1,m) \log \frac{p(x_0,x_1|m)}{p(x_0|m)p(x_1|m)}
  $$
- Measures dependency between past and future given memory state
}

\notes{When $I(X_0; X_1 | M) = 0$, the system becomes perfectly Markovian - the slow modes capture all dependencies between past and future. This is analogous to how these same slow modes create conditional independence between spatial regions. The eigenvalue structure of the Fisher information matrix that gives rise to spatial modularity also determines the temporal memory capacity of the system.}

\notes{Just as there is an information topography in space, we can define a temporal information landscape where "distance" corresponds to conditional mutual information between variables at different time points given $M$. Temporal watersheds emerge where the slow modes fail to bridge temporal dependencies, creating effective boundaries in the system's dynamics.}

\slides{
- Perfect Markovianity: $I(X_0; X_1 | M) = 0$
- Slow modes serve dual purpose:
  1. Creating spatial modularity through conditional independence
  2. Providing temporal memory that bridges past and future
- Eigenvalue spectrum determines both spatial and temporal structure
}

\notes{This framework highlights the tension in information processing systems. The slow modes must simultaneously:
1. Maintain minimal entropy (for efficiency)
2. Induce conditional independence between spatial regions (for modularity)
3. Capture temporal dependencies between past and future (for memory)

These competing objectives create an uncertainty principle: systems cannot simultaneously optimize for all three without trade-offs. Systems with strong spatial modularity may sacrifice temporal memory, while systems with excellent memory may require more complex slow mode structure.}

\slides{
- Fundamental tension between:
  - Minimal entropy in slow modes (efficiency)
  - Spatial conditional independence (modularity)
  - Temporal conditional independence (memory)
- Creates uncertainty principle with necessary trade-offs
}


\endif 