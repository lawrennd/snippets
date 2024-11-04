\ifndef{similarityTransform}
\define{similarityTransform}

\editme

\section{Similarity Transforms}

\notes{Before we dive into the derivations of MDS and PCA, we need to establish some important mathematical foundations around similarity transforms and eigendecompositions.}

\notes{Let's assume we have two linear maps $\mappingMatrix_A$ and $\mappingMatrix_B$ and a change-of-basis transformation $\mappingMatrix_P$ that maps from basis $A$ to $B$. This means we have the following relationship between the different maps:}

\slides{
* Two linear maps $\mappingMatrix_A$ and $\mappingMatrix_B$ 
* Change-of-basis transformation $\mappingMatrix_P$: $A \rightarrow B$
* Maps relate as follows:}

\notes{The relationship between the maps can be visualized as:}

$$
\begin{array}{ccc}
\mappingVector_A & \rightarrow & \mappingMatrix_A \mappingVector_A \\
\mappingMatrix_P \downarrow & & \uparrow \mappingMatrix_P^{-1} \\
\mappingVector_B & \rightarrow & \mappingMatrix_B \mappingVector_B \\
& \mappingMatrix_B &
\end{array}
$$

\notes{Now we can write up the relationship between the two linear maps:

$$\mappingMatrix_B \mappingVector_B = \mappingMatrix_P(\mappingMatrix_A \mappingVector_A) = \mappingMatrix_P(\mappingMatrix_A(\mappingMatrix_P^{-1}\mappingVector_B)) = (\mappingMatrix_P\mappingMatrix_A \mappingMatrix_P^{-1})\mappingVector_B$$

This means that we have the following relationship between the two linear maps:

$$\mappingMatrix_B = \mappingMatrix_P\mappingMatrix_A \mappingMatrix_P^{-1}$$

which we refer to as saying that the maps are similar or $\mappingMatrix_A \sim \mappingMatrix_B$.}

\subsection{Properties of Similar Matrices}

\notes{Similar matrices have several important properties that will be useful for our derivations:

If $\aMatrix \sim \bMatrix$ then:
1. $\text{det}(\aMatrix) = \text{det}(\bMatrix)$ 
2. $\text{trace}(\aMatrix) = \text{trace}(\bMatrix)$
3. $\aMatrix^m \sim \bMatrix^m, m \in \mathbb{Z}^+$
4. $\aMatrix$ invertible if and only if $\bMatrix$ invertible

In other words, the determinant, trace and invertibility are invariant under similarity.}

\subsection{Spectral Decomposition}

\notes{The most commonly used similarity transform is the spectral decomposition where one of the matrices is diagonal:

$$\aMatrix = \eigenvectorMatrix\eigenvalueMatrix \eigenvectorMatrix^{-1}$$

where:
$$\eigenvalueMatrix_{ij} = \begin{cases} 0 & i \neq j \\ \eigenvalue_i & i = j \end{cases}$$

and $\eigenvectorMatrix\eigenvectorMatrix^T = \identityMatrix \Rightarrow \eigenvectorMatrix^{-1} = \eigenvectorMatrix^T$

One of the nice properties of the eigendecomposition is that it provides a simple way of writing any square matrix as a sum of rank 1 matrices:

$$\mappingMatrix = \sum_{i=1}^N \eigenvalue_i \eigenvectorScalar_i \eigenvectorScalar_i^T$$

The spectral theorem states that all symmetric real matrices have a diagonal matrix they are similar to.}

\endif
