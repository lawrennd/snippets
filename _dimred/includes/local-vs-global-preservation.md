\ifndef{localVsGlobalPreservation}
\define{localVsGlobalPreservation}

\editme

\subsection{Local vs Global Structure Preservation}

\notes{An important consideration in dimensionality reduction is whether to focus on preserving local or global structure. Local methods like LLE and t-SNE excel at preserving local neighborhood relationships but may distort global structure, while methods like classical MDS attempt to preserve all pairwise distances.}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
import mlai.plot as plot}

\loadcode{generate_swiss_roll}{mlai}

\plotcode{# Generate and plot Swiss roll
X, t = generate_swiss_roll()
fig = plt.figure(figsize=plot.big_wide_figsize)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=t, cmap=plt.cm.viridis)
ax.view_init(10, -70)
ax.set_title('Swiss Roll: Example of Global Structure')}

\notes{The Swiss roll is a classic example where preserving only local structure can fail. Points that are close in the ambient space may be far apart on the manifold - this is known as the "short-circuiting" problem.}

\figure{\includediagram{\diagramsDir/dimred/short-circuit-problem}}{The short-circuiting problem occurs when points that are close in the ambient space are actually far apart on the manifold.}{short-circuit-problem}

\endif
