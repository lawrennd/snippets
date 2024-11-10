\ifndef{highDimensionalDataReal}
\define{highDimensionalDataReal}

\editme

\subsection{High Dimensional Effects in Real Data}

\notes{We've seen how high-dimensional random data behaves in a very specific way, with highly concentrated distance distributions. Now let's examine some real datasets to see how they differ.}

\setupcode{import numpy as np
import mlai.plot as plot
import matplotlib.pyplot as plt
import pods}

\notes{First let's look at a motion capture dataset, which despite having high dimension, is constrained by the physics of human movement.}

\code{data = pods.datasets.osu_run1()
Y = data['Y']

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.distance_distribution(Y, title='Distance Distribution for Motion Capture Data', ax=ax)}

\notes{Notice how the distance distribution is much more spread out than we would expect for random high-dimensional data. This suggests that the motion capture data has much lower intrinsic dimensionality than its ambient dimension, due to the physical constraints of human movement.}

\subsection{Oil Flow Data}

\notes{Now let's look at the oil flow dataset, which contains measurements from gamma densitometry sensors.}

\code{data = pods.datasets.oil()
Y = data['X']

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.distance_distribution(Y, title='Distance Distribution for Oil Flow Data', ax=ax)}

\notes{Again we see a deviation from what we would expect for random high-dimensional data. The oil flow data shows clear structure in its distance distribution, reflecting the physical constraints of fluid dynamics that govern the system.}

\subsection{Implications for Dimensionality Reduction}

\notes{These examples demonstrate why dimensionality reduction can be so effective on real datasets:

1. Real data typically has strong constraints (physical, biological, economic, etc.) that restrict it to a lower-dimensional manifold
2. This manifold structure is revealed by the distribution of pairwise distances
3. Dimensionality reduction techniques like PCA can discover and exploit this structure

When we see a distance distribution that deviates from theoretical predictions for random high-dimensional data, it suggests that dimensionality reduction might be particularly effective.}

\endif
