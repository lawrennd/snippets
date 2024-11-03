\ifndef{innerProductsToRepresentations}
\define{innerProductsToRepresentations}

\editme

\section{Converting between Inner Products and Distances}

\notes{There are two key ways we can represent relationships between points: through distances between points (forming a distance matrix) and through inner products between points (forming a Gram matrix). Here we'll show how to convert between these representations and how to recover a possible vectorial representation.}

\subsection{Distance and Gram Matrices}

\notes{We will refer to the Euclidean distance matrix as $\distanceMatrix$ where individual elements are given by:

$$\distanceMatrix_{ij}^2 = d_{ij}^2 = \sum_{k=1}^d (y_{ki} - y_{kj})^2 = \dataVector_i^\top \dataVector_i + \dataVector_j^\top \dataVector_j - 2\dataVector_i^\top \dataVector_j$$

where $d$ is the dimensionality of the representation. We will then refer to the inner-product matrix (or the Gram matrix) $\kernelMatrix$ as:

$$\kernelMatrix_{ij} = \kernelScalar_{ij} = \sum_{k=1}^d y_{ki}y_{kj} = \dataVector_i^\top \dataVector_j$$

This leads to the simple relationship:

$$d_{ij}^2 = \kernelScalar_{ii} + \kernelScalar_{jj} - 2\kernelScalar_{ij}$$}

\subsection{Centering Constraint}

\notes{In the algorithmic part we will in general only be able to determine the representation up to an affine transform. To fix one degree of freedom we will enforce the constraint that the data is centered. For the Gram matrix this means:

$$\sum_{i=1}^N \kernelScalar_{ij} = \sum_{i=1}^N \dataVector_i^\top \dataVector_j = \left(\sum_{i=1}^N \dataVector_i^\top\right)\dataVector_j = 0$$}

\subsection{Converting Distance to Gram Matrix}

\notes{Our task is to express a general element in the Gram matrix $\kernelScalar_{ij}$ completely in terms of distances. We can do this by first noting that:

$$\kernelScalar_{ij} = \frac{1}{2}(\kernelScalar_{ii} + \kernelScalar_{jj} - d_{ij}^2)$$

This means that we only need to find a representation for the diagonal elements of the Gram matrix to "correct" the distance.

We will do this by using the centering constraint which will allow us to isolate the diagonal elements:

$$\kernelScalar_{ij} = \frac{1}{2}(\kernelScalar_{ii} + \kernelScalar_{jj} - d_{ij}^2)$$

$$\sum_{i=1}^N \kernelScalar_{ij} = \sum_{i=1}^N \frac{1}{2}(\kernelScalar_{ii} + \kernelScalar_{jj} - d_{ij}^2)$$

$$0 = \frac{1}{2}\left(N \kernelScalar_{jj} + \sum_{i=1}^N \kernelScalar_{ii} - \sum_{i=1}^N d_{ij}^2\right)$$

$$\sum_{i=1}^N d_{ij}^2 = \sum_{i=1}^N \kernelScalar_{ii} + N \kernelScalar_{jj}$$

$$\kernelScalar_{jj} = \frac{1}{N}\left(\sum_{i=1}^N d_{ij}^2 - \sum_{i=1}^N \kernelScalar_{ii}\right)$$}

\subsection{Computing the Trace}

\notes{We will now re-write the trace of the Gram matrix using the distance matrix by adding a sum over the remaining index:

$$\sum_{i=1}^N d_{ij}^2 = \sum_{i=1}^N \kernelScalar_{ii} + N \kernelScalar_{jj}$$

$$\sum_{i=1}^N \sum_{j=1}^N d_{ij}^2 = \sum_{i=1}^N \sum_{j=1}^N \kernelScalar_{ii} + \sum_{j=1}^N N \kernelScalar_{jj}$$

$$\sum_{i=1}^N \sum_{j=1}^N d_{ij}^2 = N\sum_{i=1}^N \kernelScalar_{ii} + N\sum_{i=1}^N \kernelScalar_{jj}$$

$$\sum_{i=1}^N \sum_{j=1}^N d_{ij}^2 = 2N\sum_{i=1}^N \kernelScalar_{ii}$$

$$\frac{1}{2N}\sum_{i=1}^N \sum_{j=1}^N d_{ij}^2 = \sum_{i=1}^N \kernelScalar_{ii} = \text{trace}(\kernelMatrix)$$}

\subsection{Recovering Vector Representation}

\notes{Now that we can convert between a distance matrix and a Gram matrix, we can easily find a possible vectorial representation that could have generated this matrix through eigendecomposition:

$$\kernelMatrix = \dataMatrix\dataMatrix^\top = \eigenvectorMatrix\eigenvalueMatrix\eigenvectorMatrix^\top$$
$$= (\eigenvectorMatrix\eigenvalueMatrix^{\frac{1}{2}})(\eigenvalueMatrix^{\frac{1}{2}}\eigenvectorMatrix^\top)$$
$$= (\eigenvectorMatrix\eigenvalueMatrix^{\frac{1}{2}})(\eigenvectorMatrix\eigenvalueMatrix^{\frac{1}{2}})^\top$$

This means we can choose our representation that generated the Gram matrix to be:

$$\dataMatrix = \eigenvectorMatrix\eigenvalueMatrix^{\frac{1}{2}}$$}

\endif
