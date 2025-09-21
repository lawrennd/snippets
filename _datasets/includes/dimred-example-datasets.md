\ifndef{dimredExampleDatasets}
\define{dimredExampleDatasets}

\editme

\subsection{Example Data Sets}

\newslide{Sanity Check}

\slides{**Data sampled from independent Gaussian distribution**

* If dimensions are independent, we expect low variance, Gaussian behavior
    for the distribution of squared distances.

**Distance distribution for a Gaussian with $\dataDim=1000$, $\numData=1000$**}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.stats import gamma
import mlai
import mlai.plot as plot}

\helpercode{def plot_squared_distances(Y, title, figsize=None):
    """Plot squared distances between points in Y"""
    if figsize is None:
        figsize = plot.big_figsize
    
    # Compute pairwise squared distances
    distances = pdist(Y, metric='sqeuclidean')
    
    # Create histogram
    fig, ax = plt.subplots(figsize=figsize)
    n, bins, patches = ax.hist(distances, bins=50, density=True, alpha=0.7, color='blue')
    
    # Theoretical gamma distribution
    d = Y.shape[1]  # dimension
    mean_dist = np.mean(distances)
    x_theory = np.linspace(0, np.max(distances), 100)
    gamma_pdf = gamma.pdf(x_theory, d/2, scale=2*mean_dist/d)
    ax.plot(x_theory, gamma_pdf, 'r-', linewidth=2, label='Theoretical Gamma')
    
    ax.set_xlabel('Squared Distance')
    ax.set_ylabel('Density')
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    return fig, ax}

\plotcode{# Generate 1000D Gaussian data
np.random.seed(42)
Y = np.random.randn(1000, 1000)
fig, ax = plot_squared_distances(Y, 'Gaussian Distances (1000D, 1000 points)')

mlai.write_figure(filename='gaussian-distances-1000.svg', 
                  directory='\writeDiagramsDir/dimred')}


\figure{\inputdiagram{\diagramsDir/dimred/gaussian-distances-1000}{40%}}{A good match betwen theory and the samples for a 1000 dimensional Gaussian distribution.}



\newslide{Sanity Check}

\slides{**Same data generation, but fewer data points.**

* If dimensions are independent, we expect low variance, Gaussian behaviour
    for the distribution of squared distances.
  
**Distance distribution for a Gaussian with $\dataDim=1000$}, \emph{$\numData=100$**}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.stats import gamma
import mlai
import mlai.plot as plot}

\plotcode{# Generate 1000D Gaussian data with 100 points
np.random.seed(42)
Y = np.random.randn(100, 1000)
fig, ax = plot_squared_distances(Y, 'Gaussian Distances (1000D, 100 points)')

mlai.write_figure(filename='gaussian-distances-100.svg', 
                  directory='\writeDiagramsDir/dimred')}

\figure{\includediagram{\diagramsDir/dimred/gaussian-distances-100}{40%}}{A good match betwen theory and the samples for a 100 dimensional Gaussian distribution.}

\include{_datasets/includes/oil-flow-data.md}
\includesquareddistance{oil-flow}{Simulation of oil flow}{}

\include{_datasets/includes/osu-run1-data.md}
\includesquareddistance{osu-run1}{Ohio State University motion capture}{}


\include{_datasets/includes/spellman-yeast-data.md}
\includesquareddistance{spellman-yeast}{Spellman yeast cell cycle}{}

\include{_datasets/includes/della-gatta-gene-data.md}
\includesquareddistance{della-gatta-gene}{Della Gatta gene expression}{}

\include{_datasets/includes/grid-corpus-vowels-data.md}
\includesquareddistance{grid-corpus-vowles}{Grid corpus vowels}{}

\include{_datasets/includes/robot-wireless-data.md}
\includesquareddistance{robot-wireless}{Robot wireless navigation}{}

\newslide{Where does practice depart from our theory?}

\slides{* The situation for real data does not reflect what we expect.
* Real data exhibits greater variances on interpoint distances.
  *  Somehow the real data seems to have a smaller effective dimension.
* Let's look at another $\dataDim=1000$.}

\newslide{1000-D Gaussian}

\slides{**Distance distribution for a different Gaussian with $\dataDim=1000$**}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.stats import gamma, multivariate_normal
import mlai
import mlai.plot as plot}

\code{# Create low-rank covariance matrix
np.random.seed(42)
W = np.random.randn(1000, 2)
cov_matrix = W @ W.T + 1e-2 * np.eye(1000)

# Sample from correlated Gaussian
mean = np.zeros(1000)
Y = np.random.multivariate_normal(mean, cov_matrix, 1000)

# Plot first version
fig1, ax1 = plot_squared_distances(Y, 'Correlated Gaussian (1000D)')
mlai.write_figure(figure='correlated-gaussian-distances-1000.svg', 
                  directory='\writeDiagramsDir/dimred')

# Normalize data to have variance 1 for each dimension
varY = np.var(Y, axis=0)
stdY = np.sqrt(varY)
Y_normalized = Y / stdY

# Compute distances
distances = pdist(Y_normalized, metric='sqeuclidean')
v = distances[distances > 1e-10]  # Remove very small distances

# Normalize distances
v = 2 * v / np.mean(v)

# Create histogram
fig2, ax2 = plt.subplots(figsize=plot.big_figsize)
vals, x = np.histogram(v, bins=50, density=True)
x_centers = (x[:-1] + x[1:]) / 2
ax2.bar(x_centers, vals, alpha=0.7, color='blue', width=x[1]-x[0])

# Theoretical gamma distribution (assuming effective dimension of 2)
x_theory = np.linspace(0, 6, 100)
gamma_pdf = gamma.pdf(x_theory, W.shape[1]/2, scale=W.shape[1]/4)
ax2.plot(x_theory, gamma_pdf, 'k-', linewidth=3, label='Theoretical (d=2)')

ax2.set_xlim([0, 6])
ax2.set_xlabel('squared distance')
ax2.set_ylabel('density')
ax2.set_title('Normalized Correlated Gaussian Distances')
ax2.legend()
ax2.grid(True, alpha=0.3)

mlai.write_figure(filename='correlated-gaussian-distances2.svg', 
                  directory='\writeDiagramsDir/dimred')}

\figure{\includediagram{\diagramsDir/dimred/correlated-gaussian-distances2}{40%}Interpoint squared distance distribution for Gaussian with $\dataDim=1000$.}{correlated-gaussian-distances2}

\newslide{}

\slides{1. Gaussian has a specific low rank covariance matrix $\covarianceMatrix=\mappingMatrix\mappingMatrix^{\top}+\dataStd^{2}\eye$.
    
2. Take $\dataStd^{2}=1e-2$ and sample $\mappingMatrix\in\Re^{1000\times2}$
     from $\gaussianSamp{0}{1}$.

3. Theoretical curve taken assuming dimensionality of 2.}


\endif
