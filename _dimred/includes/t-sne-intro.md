\ifndef{tSneIntro}
\define{tSneIntro}

\editme

\subsection{t-SNE}

\notes{t-Distributed Stochastic Neighbor Embedding (t-SNE) is a dimensionality reduction technique that focuses on preserving local structure. It converts distances between points into probabilities and tries to match these probabilities in the low-dimensional space.}

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
