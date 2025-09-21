\ifndef{tSneIntro}
\define{tSneIntro}

\editme

\subsection{t-SNE}

\notes{t-Distributed Stochastic Neighbor Embedding (t-SNE) is a dimensionality reduction technique that focuses on preserving local structure. It converts distances between points into probabilities and tries to match these probabilities in the low-dimensional space.}

\notes{The idea in t-SNE is to convert distances in data space into probabilities. This is done through two stages. First a neighbourhood graph is formed, so each point, $i$, is related to its $k$ nearest neighbours.}

\notes{If the squared distances between two data points are given by $\distanceScalar_{i,j}^2$, then the probability of point $i$ linking to point $j$ is given by,
$$
p(r_{i,j} | \distanceMatrix) = \pi_{i,j} =  \frac{\exp -\frac{\distanceScalar_{i,j}^2}{2\sigma^2}}{\sum_{k\in \neighborhood{i}}\exp -\distanceScalar_{i,j}}
$$
where $r_{i,j} = 1$ if the two points are linked, $\pi_{i,j}$ is the probability of that link and the neighbourhood of $i$ is given by $\mathscr{N}(i)$.}

\notes{This is compared with probabilities in *latent* space which are given by 
$$
p(s_{i,j} | \latentDistanceMatrix) = q_{i,j} = (1 + \latentDistanceScalar_{i,j})^(-1)}{\sum_{k\in \neighborhood{i}}/ (1 + \latentDistanceScalar_{i, k})^(-1)},
$$
where $s_{i,j} = 1$ if two points are linked in the latent space and $q_{i,j}$ is the probability of that link. The latent distances are given by
$$
\latentDistanceScalar_{i,j} = (\latentVector_{i, :} - \latentVector_{j, :})^\top*\latentVector_{i, :} - \latentVector_{j, :}).
$$}

\notes{$t$-SNE then minimises the KL divergence between these two link distributions.
$$
\errorFunction(\latentMatrix} = \sum_i \sum_{j\in\neighborhood{i}} p_{i,k} \log \frac{p_{i,k}}{q_{i,k}}
$$}

\slides{
* Converts distances to probabilities
* Uses t-distribution in low-dimensional space
* Excellent for visualization
* Computationally intensive
* Results depend on perplexity parameter
}

\notes{The approach was originally proposed by @Hinton-sne02, then later modified using the $t$-distribution in the latent space by @Maaten-tsne08.}

\notes{The basic idea is to minimise the Kullback-Leibler divergence between a distribution defined in the latent space and a distribution defined in the data space. The distribution is over neighbours in each space, by definition the probability of point $j$ being selected as a neighbor of point $i$ is:

$$p_{j|i} = \frac{\exp(-\|\dataVector_i - \dataVector_j\|^2/2\sigma_i^2)}{\sum_{k \neq i} \exp(-\|\dataVector_i - \dataVector_k\|^2/2\sigma_i^2)}$$

where $\sigma_i$ is chosen to achieve a desired perplexity. In the low-dimensional space, a t-distribution is used instead:

$$q_{ij} = \frac{(1 + \|\latentVector_i - \latentVector_j\|^2)^{-1}}{\sum_{k \neq l} (1 + \|\latentVector_k - \latentVector_l\|^2)^{-1}}$$}

\setupcode{from sklearn.manifold import TSNE}

\loadcode{tsne_example}{mlai.plot}

\undef{oilFlowData}
\include{_datasets/includes/oil-flow-data.md}

\setupplotcode{import matplotlib.pyplot as plt
import mlai
from mlai import plot}

\plotcode{tsne_example(X, Y)
mlai.write_figure('t-sne-oil-flow.svg', directory='\writeDiagramsDir/dimred')}

\newslide{t-SNE Embedding of Oil Flow Data}

\figure{\includediagram{\diagramsDir/dimred/t-sne-oil-flow}{80%}}{t-SNE embedding of the oil flow data.}{t-sne-oil-flow}

\notes{The perplexity parameter in t-SNE effectively controls how to balance attention between local and global aspects of the data. It can be interpreted as a smooth measure of the effective number of neighbors.}

\endif
