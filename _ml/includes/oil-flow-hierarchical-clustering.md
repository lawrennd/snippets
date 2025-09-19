\ifndef{oilFlowHierarchicalClustering}
\define{oilFlowHierarchicalClustering}


\editme

\subsection{Hierarchical Clustering of Oil Flow Data}

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
           leaf_rotation=45,  # Rotate labels
           leaf_font_size=8,  # Reduce font size
           ax=ax)
ax.set_xlabel('Sample Index')
ax.set_ylabel('Distance')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
plt.tight_layout()
mlai.write_figure('hierarchical-clustering-oil.svg', directory='\writeDiagramsDir/dimred')}

\figure{\includediagram{\diagramsDir/dimred/hierarchical-clustering-oil}{60%}}{Hierarchical clustering applied to oil flow data. The dendrogram shows how different flow regimes are grouped based on their measurement similarities. The three main flow regimes (homogeneous, annular, and laminar) should form distinct clusters.}{hierarchical-clustering-oil}

\notes{In this example, we've applied hierarchical clustering to the oil flow data set. The data contains measurements from different flow regimes in a multiphase flow facility. The dendrogram shows how measurements naturally cluster into different flow types. Ward's linkage method is used as it tends to create compact, evenly-sized clusters. 
\endif
