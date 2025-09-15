\ifndef{mdsDerivation}
\define{mdsDerivation}

\editme

\section{Multi-Dimensional Scaling}

\notes{Multi-Dimensional Scaling (MDS) is a classical approach to dimensionality reduction that works directly with similarities or proximities between entities. The goal is to find a geometric configuration that preserves these relationships.}

\subsection{The MDS Objective}

\notes{Given $\numData$ entities and a matrix of proximity relationships between them $\distanceMatrix$ where $\distanceMatrix_{ij}$ is the relationship between entity $i$ and $j$, our task is to find an embedding $\dataMatrix = [\dataVector_1, \ldots, \dataVector_\numData]$ such that $\|\dataVector_i - \dataVector_j\|_{L2} \approx \delta_{ij}$.

In MDS this is formulated as minimizing the Frobenius norm between the given proximity matrix $\distanceMatrix$ and the one calculated directly from the embedding $\latentDistanceMatrix$ where $\latentDistanceMatrix_{ij} = \|\dataVector_i - \dataVector_j\|_{L2}$:

$$\hat{\dataMatrix} = \argmin_{\dataMatrix} \|\latentDistanceMatrix - \distanceMatrix\|_F$$}

\subsection{Properties of the Frobenius Norm}

\notes{The Frobenius norm is the generalization of the Euclidean norm to matrices. The general element-wise norm for matrices $L_{p,q}$ takes the form:

$$\|\mappingMatrix\|_{p,q} = \left(\sum_{j=1}^n \left(\sum_{i=1}^m |m_{ij}|^p\right)^{\frac{q}{p}}\right)^{\frac{1}{q}}$$

where the Frobenius norm is the case where $p = q = 2$. For a square diagonal matrix, the Frobenius norm is just the square root of the sum of the squares of the diagonal elements:

$$\|\mappingMatrix\|_F = \sqrt{\text{trace}(\mappingMatrix^\top\mappingMatrix)} = \sqrt{\text{trace}(\mappingMatrix^2)}$$}

\subsection{MDS Solution}

\notes{Using the properties of similar matrices that we established earlier, if $\aMatrix \sim \bMatrix$ then $\aMatrix^2 \sim \bMatrix^2$ and the trace is invariant under similarity. This means that if we diagonalize a matrix through its eigendecomposition, the Frobenius norm is simply the square root of the sum of the eigenvalues.

Using this, we can rewrite the MDS optimization problem:

$$\argmin_{\latentDistanceMatrix} \|\latentDistanceMatrix - \distanceMatrix\|_F^2 = \argmin_{\latentDistanceMatrix} \text{trace}(\latentDistanceMatrix - \distanceMatrix)^2$$

Now we will write $\distanceMatrix$ using its eigendecomposition and also rewrite $\latentDistanceMatrix$ using a similar matrix:

$$\argmin_{\mappingMatrix, \hat{\eigenvalueMatrix}} \text{trace}(\mappingMatrix\hat{\eigenvalueMatrix}\mappingMatrix^\top - \eigenvectorMatrix\eigenvalueMatrix\eigenvectorMatrix^\top)^2$$

Using the fact that the trace is invariant under similarity transform, we can pre and post multiply with the known eigenvectors of the proximity matrix:

$$\argmin_{\mappingMatrix, \hat{\eigenvalueMatrix}} \text{trace}(\eigenvectorMatrix^\top(\mappingMatrix\hat{\eigenvalueMatrix}\mappingMatrix^\top - \eigenvectorMatrix\eigenvalueMatrix\eigenvectorMatrix^\top)\eigenvectorMatrix)^2$$
$$= \argmin_{\mappingMatrix, \hat{\eigenvalueMatrix}} \text{trace}(\eigenvectorMatrix^\top\mappingMatrix\hat{\eigenvalueMatrix}\mappingMatrix^\top\eigenvectorMatrix - \eigenvalueMatrix)^2$$}

\notes{From the above we can see that we have a diagonal matrix $\eigenvalueMatrix$ that we want to match by choosing $\mappingMatrix$ and $\hat{\eigenvalueMatrix}$. This means that as $\hat{\eigenvalueMatrix}$ is diagonal, the minima will be achieved when $\eigenvectorMatrix^\top\mappingMatrix = \identityMatrix$. This leads to:

$$\argmin_{\mappingMatrix, \hat{\eigenvalueMatrix}} \text{trace}(\eigenvectorMatrix^\top\mappingMatrix\hat{\eigenvalueMatrix}\mappingMatrix^\top\eigenvectorMatrix - \eigenvalueMatrix)^2 = \argmin_{\hat{\eigenvalueMatrix}} \text{trace}(\hat{\eigenvalueMatrix} - \eigenvalueMatrix)^2$$
$$= \sum_{i=1}^N (\hat{\lambda}_i - \lambda_i)^2$$}

\subsection{Rank-Constrained Solution}

\notes{To provide a rank $\latentDim$ approximation $\latentDistanceMatrix$ to $\distanceMatrix$ we should therefore match the largest $\latentDim$ eigenvalues and choose
$$
\latentDistanceMatrix = \sum_{j=1}^\latentDim \lambda_i \eigenvectorScalar_j \eigenvectorScalar_i^\top
$$
where the eigenvalues have been sorted such that $\lambda_i \geq \lambda_j$ when $i < j$. This leads to the following error of the embedding:
$$
\|\latentDistanceMatrix - \distanceMatrix\|_F = \sqrt{\sum_{i=\latentDim+1}^\numData \lambda_i^2}
$$}

\endif
