\ifndef{mdsPcaEquivalence}
\define{mdsPcaEquivalence}

\editme

\section{Equivalence between MDS and PCA}

\notes{We can derive a simple equivalence between MDS and PCA in the linear setting. While MDS diagonalizes the $\numData \times \numData$ Gram matrix $\dataMatrix\dataMatrix^\top$, PCA diagonalizes the $\dataDim \times \dataDim$ sample covariance matrix $\frac{1}{\numData-1}\dataMatrix^\top\dataMatrix$. We'll show the connection between these diagonalizations and how their eigenvectors relate.}

\subsection{Connecting the Eigendecompositions}

\notes{Starting from the Gram matrix eigendecomposition
$$
\kernelMatrix = \dataMatrix\dataMatrix^\top = \eigenvectorMatrix\eigenvalueMatrix\eigenvectorMatrix^\top$$
$$(\dataMatrix\dataMatrix^\top)\eigenvectorScalar_i = \eigenvalue_i\eigenvectorScalar_i
$$
Multiplying both sides by $\frac{1}{\numData-1}\dataMatrix^\top$ on the left,
$$
\frac{1}{\numData-1}\dataMatrix^\top(\dataMatrix\dataMatrix^\top)\eigenvectorScalar_i = \eigenvalue_i\frac{1}{\numData-1}\dataMatrix^\top\eigenvectorScalar_i
$$
$$
\frac{1}{\numData-1}(\dataMatrix^\top\dataMatrix)\dataMatrix^\top\eigenvectorScalar_i = \eigenvalue_i\frac{1}{\numData-1}\dataMatrix^\top\eigenvectorScalar_i
$$
$$
\covarianceMatrix(\dataMatrix^\top\eigenvectorScalar_i) = \frac{\eigenvalue_i}{\numData-1}(\dataMatrix^\top\eigenvectorScalar_i)
$$
}

\notes{Looking at this last equation, we can see this is exactly the behavior of an eigendecomposition of $\covarianceMatrix$ where:
* The eigenvalue is $\frac{\eigenvalue_i}{\numData-1}$
* The corresponding eigenvector is $\dataMatrix^\top\eigenvectorScalar_i$

Importantly, as the scaling of the MDS eigenvalue only depends on $\numData$, the order of the eigenvalues remains the same.}

\subsection{Orthonormalization}

\notes{One detail remains: the eigenvectors should form an orthonormal basis. While we know $\eigenvectorMatrix$ does so, we need to verify this for $\dataMatrix^\top\eigenvectorScalar_i$. For orthogonality
$$
(\dataMatrix^\top\eigenvectorScalar_i)^\top(\dataMatrix^\top\eigenvectorScalar_i) = \eigenvectorScalar_i^\top\dataMatrix\dataMatrix^\top\eigenvectorScalar_i = \eigenvalue_i
$$
To achieve normalization, we can scale the vectors:
$$
\left(\frac{1}{\sqrt{\eigenvalue_i}}\dataMatrix^\top\eigenvectorScalar_i\right)^\top\left(\frac{1}{\sqrt{\eigenvalue_i}}\dataMatrix^\top\eigenvectorScalar_i\right) = 1
$$}

\subsection{Equivalence in Embeddings}

\notes{We can now directly compare the embeddings from both methods. If we take the eigenvector corresponding to the largest eigenvalue $\eigenvectorScalar_1$

MDS embedding:
$$\latentVector_{\text{MDS}} = \eigenvectorScalar_1\sqrt{\eigenvalue_1}$$

PCA embedding (projecting the data onto the eigenvector):
$$\latentVector_{\text{PCA}} = \dataMatrix\left(\frac{\dataMatrix^\top\eigenvectorScalar_1}{\sqrt{\eigenvalue_1}}\right) = \frac{\dataMatrix\dataMatrix^\top\eigenvectorScalar_1}{\sqrt{\eigenvalue_1}} = \frac{\eigenvalue_1\eigenvectorScalar_1}{\sqrt{\eigenvalue_1}} = \sqrt{\eigenvalue_1}\eigenvectorScalar_1$$

Thus the embeddings of the two methods are identical.}

\subsection{Rank-Nullity Connection}

\notes{This equivalence shouldn't be surprising when we consider the rank-nullity theorem. For data $\dataMatrix \in \Re^{\numData \times \dataDim}$, the sample covariance $\covarianceMatrix \in \Re^{\dataDim \times \dataDim}$ has maximum rank $\dataDim$ while for MDS we work with the Gram matrix $\kernelMatrix \in \Re^{\numData \times \numData}$.

However, the maximum rank of the Gram matrix is not $\numData$ as it is generated from data that only has $\dataDim$ degrees of freedom. Therefore its rank is the same as the covariance matrix
$$
\text{Rank}(\dataMatrix^\top\dataMatrix) = \text{Rank}(\dataMatrix\dataMatrix^\top)
$$}

\subsection{Implications}

\notes{This equivalence is important because PCA was derived as a probabilistic model with clear interpretable assumptions. We can now translate these assumptions to MDS

1. MDS is also implicitly assuming Gaussian-distributed data
2. The Frobenius norm minimization in MDS corresponds to maximum likelihood estimation under this Gaussian assumption
3. Both methods are finding the same linear subspace that maximizes variance

The key difference emerges when we consider non-linear extensions:

* From PCA we have a clear model that can be extended to non-linear functions through GPs (leading to GP-LVM)
* From MDS we typically create non-linear versions by modifying the distance calculations between points

The model-based approach of PCA makes its assumptions explicit and provides a clearer path to principled non-linear extensions.}

\endif
