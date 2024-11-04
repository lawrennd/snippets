\ifndef{rankNullity}
\define{rankNullity}

\editme

\section{Rank-Nullity Theorem}

\notes{The rank-nullity theorem provides a fundamental relationship between dimensionality representations that will be crucial for understanding dimensionality reduction methods.}

\notes{We will refer to two different representations of the data:

1. The original representation in its raw form where the dimensionality we talk about is the degrees of freedom of the representation
2. The canonical representation of the data which captures the true degrees of freedom in the data

An example would be a line in a two dimensional representation, where the canonical representation is one-dimensional, or in a non-linear case the classic swiss-roll data which is two-dimensional but embedded in a representation of three dimensions.}

\subsection{The Theorem}

\notes{Given two vector spaces $\inputSpace$ and $\mathcal{B}$ and a transformation $\mappingFunction: \inputSpace \rightarrow \mathcal{B}$, the rank-nullity theorem states:

$$\text{Rank}(\mappingFunction) + \text{Nullity}(\mappingFunction) = \text{dim}(\inputSpace)$$

where:

- $\text{Rank}(\mappingFunction)$ is the dimensionality of the image of $\mappingFunction$ 
- $\text{Nullity}(\mappingFunction)$ is the dimensionality of the kernel of $\mappingFunction$

For linear maps this becomes quite simple. Say that we have a map $\mappingMatrix \in \mathbb{R}^{m\times n}$, this will lead to:

$$\text{Rank}(\mappingMatrix)_{\text{min}(m,n)} + \text{Nullity}(\mappingMatrix)_{\text{max}(0,n-m)} = n$$}

\figure{\includediagram{\diagramsDir/dimred/rank-nullity-concept}{80%}}{The kernel and image of a linear map. From [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Kernel_and_image_of_linear_map.svg).}{rank-nullity-concept}

\subsection{Implications for Dimensionality Reduction}

\notes{The task of any dimensionality reduction method is to find a map, explicit or implicit, that makes the nullity of the transformation to be the domain where the data have no variations. This means that the image of the transformation is the canonical representation of the data.

In the world of noise and applications, we are likely to have a scenario where we want to remove variations from the original representation that we do not want represented in our embedding. This is where machine learning diverges from pure mathematics, as it requires assumptions about what variations should be removed.

This differentiation between mathematics and machine learning arises because we need to make some assumptions about what we want to remove, and this is where it starts getting very interesting as this requires models. The assumptions we make about what variations to remove will lead to different dimensionality reduction approaches.}

\endif
