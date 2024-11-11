\ifndef{highDimensionalEffects}
\define{highDimensionalEffects}

\editme

\subsection{High Dimensional Data Effects}

\notes{In high dimensional spaces, our intuitions from everyday three dimensional space can fail dramatically. There are two major effects that occur:

1. All data moves to a "shell" at one standard deviation from the mean (known as the "curse of dimensionality")
2. Distances between points become constant

Let's explore these effects with some experiments.}

\slides{
* High dimensional spaces behave very differently from our 3D intuitions
* Two key effects:
  * Data moves to a "shell" at one standard deviation from mean
  * Distances between points become constant
* Let's see this experimentally
}

\setupcode{import numpy as np
import mlai.plot as plot
import matplotlib.pyplot as plt
import mlai}

\code{# Generate high-dimensional Gaussian data
d = 1000  # dimensions
n = 100   # number of points
Y = np.random.normal(size=(n, d))

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.distance_distribution(Y, title=f'Distance Distribution for {d}-D Gaussian Data', ax=ax)
mlai.write_figure('high-d-distances.svg', directory='\writeDiagramsDir/dimred')}

\newslide{Pairwise Distances in High-D Gaussian Data}

\figure{\includediagram{\diagramsDir/dimred/high-d-distances}{80%}}{Distribution of pairwise distances between points in high-dimensional Gaussian data. The red line shows the theoretical gamma distribution.}{high-d-distances}

\notes{This plot shows the distribution of pairwise distances between points in our high-dimensional Gaussian data. The red line shows the theoretical prediction - a gamma distribution with shape parameter d/2 and scale 2/d. The close match between theory and practice demonstrates how in high dimensions, distances between random points become highly concentrated around a particular value.}

\newslide{Pairwise Distances in High-D Gaussian Data}
\slides{
* Plot shows pairwise distances in high-D Gaussian data
* Red line: theoretical gamma distribution
* Notice tight concentration of distances
}

\subsection{Structured High Dimensional Data}

\notes{Now let's look at what happens when we introduce structure into our high-dimensional data. We'll create data that actually lies in a lower-dimensional space, but embedded in high dimensions.}

\slides{
* What about data with underlying structure?
* Let's create data that lies on a 2D manifold
* Embed it in 1000D space
}

\code{# Generate data that lies on a 2D manifold embedded in 1000D
W = np.random.normal(size=(d, 2))  # 2D latent directions
latent = np.random.normal(size=(n, 2))  # 2D latent points
Y_structured = latent @ W.T  # Project to high dimensions

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.distance_distribution(Y_structured, 
                         title='Distance Distribution for Structured High-D Data', 
                         ax=ax)
mlai.write_figure('structured-high-d-distances.svg', directory='\writeDiagramsDir/dimred')}

\newslide{Pairwise Distances in Structured High-D Data}

\figure{\includediagram{\diagramsDir/dimred/structured-high-d-distances}{80%}}{Distribution of pairwise distances for structured high-dimensional data. The distribution differs significantly from pure high-dimensional data, reflecting the underlying 2D structure.}{structured-high-d-distances}

\notes{Notice how the distance distribution for the structured data deviates significantly from what we would expect for truly high-dimensional data. Instead of matching the theoretical curve for 1000-dimensional data, it more closely resembles what we would expect for 2-dimensional data. This is because despite living in a 1000-dimensional space, the data actually has an intrinsic dimensionality of 2.

This effect is exactly what we observe in real datasets - they typically have much lower intrinsic dimensionality than their ambient dimension would suggest. This is why dimensionality reduction techniques like PCA can be so effective: they help us discover and work with this lower-dimensional structure.}

\newslide{Pairwise Distances in Structured High-D Data}
\slides{
* Distance distribution differs from pure high-D case
* Matches 2D theoretical curve better than 1000D
* Real data often has low intrinsic dimensionality
* This is why PCA and other dimension reduction works!
}

\codeassignment{Generate your own high-dimensional dataset with known structure and visualize its distance distribution. Try varying the intrinsic dimensionality (e.g. use 3D or 4D latent space) and observe how the distance distribution changes. What happens if you add some noise to the structured data?}{30}

\endif
