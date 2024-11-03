\ifndef{nonlinearExtensions}
\define{nonlinearExtensions}

\editme

\section{Non-linear Extensions}

\notes{Having established the equivalence between MDS and PCA in the linear case, we can now explore how their different perspectives lead to different approaches for non-linear dimensionality reduction.}

\subsection{Non-linear MDS Approaches}

\notes{The MDS formulation naturally leads to extensions based on modifying how distances between points are computed. Instead of using Euclidean distances in the original space, we can attempt to approximate distances along a manifold.}

\subsubsection{Isomap}

\notes{One of the simplest approaches is Isomap, which makes the assumption that locally (between nearby points) the Euclidean distance is a good approximation of the distance along the manifold. The algorithm proceeds as follows:

1. Construct a neighborhood graph by connecting each point to its $k$ nearest neighbors
2. Compute Euclidean distances between connected points
3. For non-connected points, compute the shortest path in the graph
4. Apply classical MDS to the resulting distance matrix

This approach allows us to "unroll" manifolds like the Swiss roll, where Euclidean distances between distant points don't reflect the true structure of the data.}

\subsubsection{Maximum Variance Unfolding}

\notes{A more sophisticated approach is Maximum Variance Unfolding (MVU), which makes use of the fact that the set of positive definite matrices is convex. MVU formulates a semidefinite program that learns the Gram matrix subject to constraints that preserve local distances:

1. Construct a neighborhood graph as in Isomap
2. Optimize for a Gram matrix that:
   * Maximizes the trace (spreading points apart)
   * Maintains distances between neighboring points
   * Is positive semidefinite
   * Centers the data

This provides a principled way to learn the Gram matrix while respecting local structure.}

\subsection{Model-based Non-linear Extensions}

\notes{The probabilistic interpretation of PCA suggests a different approach to non-linearization: replacing the linear mapping with a non-linear function while maintaining the probabilistic framework.}

\subsubsection{Gaussian Process Latent Variable Model}

\notes{The GP-LVM emerges naturally from the probabilistic PCA model by:

1. Replacing the linear mapping $\mappingMatrix$ with a non-linear function $\mappingFunction$
2. Placing a Gaussian process prior over $\mappingFunction$
3. Integrating out $\mappingFunction$ instead of $\latentMatrix$

This gives us the marginal likelihood:

$$p(\dataMatrix|\latentMatrix) = \prod_{j=1}^{\dataDim} \gaussianDist{\dataVector_{:,j}}{\zerosVector}{\kernelMatrix}$$

where $\kernelMatrix$ is constructed from the latent points $\latentMatrix$. We can then optimize this likelihood with respect to $\latentMatrix$ to find the latent representation.}

\subsection{Comparing the Approaches}

\notes{The key difference between these approaches lies in what they make explicit:

* MDS-based approaches make local geometric assumptions explicit
    * Easier to understand geometrically
    * Can be more intuitive for visualization
    * Often rely on discrete approximations (graphs)
    * Harder to extend to new points

* Model-based approaches make statistical assumptions explicit
    * Clear probabilistic interpretation
    * Natural handling of uncertainty
    * Easy to extend to new points
    * Can be harder to understand geometrically

In practice, the choice between these approaches often depends on the specific application and what type of assumptions are easier to verify or more appropriate for the domain.}

\subsection{Recent Developments}

\notes{Understanding these different perspectives has led to new hybrid approaches that try to combine their strengths:

* Locally Linear Latent Variable Models
* Gaussian Process Latent Variable Models with back-constraints
* Deep Gaussian Processes

These methods attempt to maintain both the geometric intuition of MDS-based approaches and the probabilistic rigor of model-based approaches.}

\notes{The key insight is that having two different routes to the same solution in the linear case provides us with two different perspectives for extension to the non-linear case. This has enriched our understanding of dimensionality reduction and led to a variety of complementary approaches.}

\endif
