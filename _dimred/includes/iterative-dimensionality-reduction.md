\ifndef{iterativeDimensionalityReduction}
\define{iterativeDimensionalityReduction}

\editme

\subsection{Iterative Dimensionality Reduction}

\notes{While spectral methods like PCA and classical MDS provide analytical solutions through eigendecomposition, many dimensionality reduction problems require iterative optimization approaches. These methods can often capture more complex relationships in the data but come at the cost of potentially getting stuck in local optima.}

\slides{
* Spectral methods (PCA, MDS) give analytical solutions
* Iterative methods optimize objective functions
  * Can capture more complex relationships
  * May find local optima
  * More computationally intensive
}

\subsection{Stress Functions}

\notes{A key concept in iterative dimensionality reduction is the stress function, which measures how well the low-dimensional representation preserves relationships in the original data. The classic Kruskal stress function is:
$$
\text{stress} = \sqrt{\frac{\sum_{i<j} (\distanceScalar_{ij} - \latentDistanceScalar_{ij})^2}{\sum_{i<j} \distanceScalar_{ij}^2}},
$$
where $\distanceScalar_{ij}$ are the original distances and $\latentDistanceScalar_{ij}$ are the distances in the reduced space.}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
import mlai.plot as plot}

\loadcode{kruskal_stress}{mlai}

\notes{Different stress functions place different emphasis on preserving local versus global structure. For example, Sammon mapping modifies the stress function to give more weight to preserving small distances:

$$\text{stress}_{\text{Sammon}} = \frac{1}{\sum_{i<j} \distanceScalar_{ij}} \sum_{i<j} \frac{(\distanceScalar_{ij} - \latentDistanceScalar_{ij})^2}{\distanceScalar_{ij}}$$}

\endif
