\ifndef{pcaProbabilistic}
\define{pcaProbabilistic}

\editme

\section{Probabilistic PCA}

\notes{Principal Component Analysis (PCA) is often introduced algorithmically, but here we'll derive it through a probabilistic model. This will help us understand the assumptions underlying PCA and make connections to MDS clearer.}

\subsection{The Model}

\notes{In unsupervised learning, we observe a set of data $\dataMatrix$ and make an assumption that this data has been generated from a latent representation $\latentMatrix$ through some mapping $\mappingFunction(\cdot)$ such that:

$$\dataVector_i = \mappingFunction(\latentVector_i)$$

Our task is to recover both the latent representation and the mapping. This appears to be an ill-posed problem, as one simple solution would be to set the mapping to be the identity, making the latent and observed data identical.

To make progress, we need to add some form of supervision or constraint that indicates what kind of representation we're looking for. A common scenario is seeking a lower dimensional representation of the data.}

\subsection{Linear Gaussian Model}

\notes{In PCA, we assume a standard Gaussian likelihood:

$$p(\dataMatrix|\latentMatrix) = \gaussianDist{\dataMatrix}{\latentMatrix\mappingMatrix^\top + \boldsymbol{\mu}}{\noiseStd^{-1}\eye}$$

where $\mappingMatrix \in \Re^{\dataDim \times \latentDim}$ is our linear transformation matrix and $\boldsymbol{\mu}$ is a constant offset. We then use Gaussian priors over both the weights $\mappingMatrix$ and the latent coordinates $\latentMatrix$, leading to the joint distribution:

$$p(\dataMatrix, \mappingMatrix, \latentMatrix) = p(\dataMatrix|\mappingMatrix, \latentMatrix)p(\latentMatrix)p(\mappingMatrix)$$

Our aim is to derive the posterior distribution over the unknown parameters $\mappingMatrix$ and $\latentMatrix$. To do this we need to marginalize out these parameters from the joint:

$$p(\dataMatrix) = \int p(\dataMatrix|\mappingMatrix, \latentMatrix)p(\latentMatrix)p(\mappingMatrix)$$}

\subsection{Model Choice}

\notes{The integral above is not tractable for both $\mappingMatrix$ and $\latentMatrix$. We need to choose which variable to integrate out and which to optimize. Given $\numData$ data points and a $\latentDim$-dimensional latent representation:

* $\mappingMatrix \in \Re^{\dataDim \times \latentDim}$
* $\latentMatrix \in \Re^{\numData \times \latentDim}$

Assuming $\numData > \dataDim$, it makes sense to integrate out $\latentMatrix$ while we optimize $\mappingMatrix$. This also allows us to obtain the posterior distribution $p(\latentVector|\dataVector)$ which we need for inferring latent locations of new data points.}

\subsection{Joint Distribution}

\notes{We can derive the joint distribution of a pair of points, $\dataVector$ and $\latentVector$, since we know their product will be Gaussian:

$$p(\dataVector, \latentVector|\mappingMatrix) = \gaussianDist{\begin{bmatrix}\dataVector \\ \latentVector\end{bmatrix}}{\begin{bmatrix}\boldsymbol{\mu} \\ \zerosVector\end{bmatrix}}{\begin{bmatrix}\mappingMatrix\mappingMatrix^\top + \noiseStd^{-2}\eye & \mappingMatrix \\ \mappingMatrix^\top & \eye\end{bmatrix}}$$

From this joint distribution, we can derive the marginal over the observed data and the conditional distribution over the latent space using the Gaussian identities:

$$p(\dataVector|\mappingMatrix) = \gaussianDist{\dataVector}{\boldsymbol{\mu}}{\mappingMatrix\mappingMatrix^\top + \noiseStd^{-2}\eye}$$

$$p(\latentVector|\dataVector, \mappingMatrix) = \gaussianDist{\latentVector}{\mappingMatrix^\top(\mappingMatrix\mappingMatrix^\top + \noiseStd^{-2}\eye)^{-1}(\dataVector - \boldsymbol{\mu})}{\eye - \mappingMatrix^\top(\mappingMatrix\mappingMatrix^\top + \noiseStd^{-2}\eye)^{-1}\mappingMatrix}$$}

\subsection{Maximum Likelihood Solution}

\notes{The maximum likelihood solution can be reached by taking the derivatives of the marginal likelihood and finding its stationary points. When we do this, we get the following solution:

$$\hat{\mappingMatrix} = \eigenvectorMatrix(\eigenvalueMatrix - \noiseStd^{-2}\eye)$$

$$\hat{\noiseStd^{2}} = \frac{1}{\dataDim}\sum_{j=1}^\dataDim \lambda_j$$

where $\eigenvalueMatrix$ and $\eigenvectorMatrix$ come from the eigendecomposition of the sample covariance matrix:

$$\covarianceMatrix = \frac{1}{\numData-1}(\dataMatrix - \boldsymbol{\mu})^\top(\dataMatrix - \boldsymbol{\mu}) = \eigenvectorMatrix\eigenvalueMatrix\eigenvectorMatrix^\top$$}

\notes{So the Maximum Likelihood solution is simply choosing the mapping to be the eigenvectors of the sample covariance matrix multiplied by the eigenvalues corrected by the noise variance. If we assume no noise in the data $\noiseStd^2 \to 0$ then it's just the eigenvectors.}

\subsection{Model vs Algorithm}

\notes{In many textbooks, this solution is explained as PCA and interpreted as finding a similar matrix to the sample covariance and choosing the linear subspace with maximum variance. While this interpretation is valid, it misses the key point: we have made clear probabilistic assumptions in reaching this solution.

By specifying $p(\latentMatrix)$, we have stated that we believe the data to be normally distributed. PCA should only be applied when this assumption is reasonable. The probabilistic formulation makes these assumptions explicit, while the algorithmic view can obscure them.

Furthermore, having a clear model makes it much easier to extend PCA to non-linear cases. With this presentation, extending to the GP-LVM becomes natural: rather than integrating out $\latentMatrix$, we place a Gaussian process prior over $\mappingFunction$ and integrate it out instead.}

\endif
