\ifndef{gpdistfunc}
\define{gpdistfunc}
\editme

\include{_gp/includes/gaussian-predict-index-one-and-two.md}

\subsection{Uluru}

\figure{\includejpg{\diagramsDir/gp/799px-Uluru_Panorama}}{Uluru, the sacred rock in Australia. If we think of it as a probability density, viewing it from this side gives us one *marginal* from the density. Figuratively speaking, slicing through the rock would give a conditional density.}{uluru-as-probability}

\notes{When viewing these contour plots, I sometimes find it helpful to think of Uluru, the prominent rock formation in Australia. The rock rises above the surface of the plane, just like a probability density rising above the zero line. The rock is three dimensional, but when we view Uluru from the classical position, we are looking at one side of it. This is equivalent to viewing the marginal density. 

The joint density can be viewed from above, using contours. The conditional density is equivalent to *slicing* the rock. Uluru is a holy rock, so this has to be an imaginary slice. Imagine we cut down a vertical plane orthogonal to our view point (e.g. coming across our view point). This would give a profile of the rock, which when renormalized, would give us the conditional distribution, the value of conditioning would be the location of the slice in the direction we are facing.}

\subsection{Prediction of $\mappingFunction_2$ from $\mappingFunction_1$}
\notes{Of course in practice, rather than manipulating mountains physically, the advantage of the Gaussian density is that we can perform these manipulations mathematically. 

Prediction of $\mappingFunction_2$ given $\mappingFunction_1$ requires the *conditional density*, $p(\mappingFunction_2|\mappingFunction_1)$.}\slides{
* Conditional density is *also* Gaussian.}\notes{Another remarkable property of the Gaussian density is that this conditional distribution is *also* guaranteed to be a Gaussian density. It has the form,}
$$
p(\mappingFunction_2|\mappingFunction_1) = \gaussianDist{\mappingFunction_2}{\frac{\kernelScalar_{1, 2}}{\kernelScalar_{1, 1}}\mappingFunction_1}{ \kernelScalar_{2, 2} - \frac{\kernelScalar_{1,2}^2}{\kernelScalar_{1,1}}}
$$\slides{
where covariance of joint density is given by}\notes{where we have assumed that the covariance of the original joint density was given by}
$$
\kernelMatrix = \begin{bmatrix} \kernelScalar_{1, 1} & \kernelScalar_{1, 2}\\ \kernelScalar_{2, 1} & \kernelScalar_{2, 2}.\end{bmatrix}
$$

\notes{Using these formulae we can determine the conditional density for any of the elements of our vector $\mappingFunctionVector$. For example, the variable $\mappingFunction_8$ is less correlated with $\mappingFunction_1$ than $\mappingFunction_2$. If we consider this variable we see the conditional density is more diffuse.}

\include{_gp/includes/gaussian-predict-index-one-and-eight.md}

\newslide{Details}

* The single contour of the Gaussian density represents the \colorblue{joint distribution, $p(\mappingFunction_1, \mappingFunction_8)$}

. . .

* We observe a value for \colorgreen{$\mappingFunction_1=-?$}

. . .
	
* Conditional density: \colorred{$p(\mappingFunction_8|\mappingFunction_1=?)$}.

\newslide{Multivariate Conditional Density}

* Prediction of $\mappingFunctionVector_*$ from $\mappingFunctionVector$.

* Multivariate conditional density is *also* Gaussian. 
  $$
  p(\mappingFunctionVector_*|\mappingFunctionVector) = {\mathcal{N}\left(\mappingFunctionVector_*|\kernelMatrix_{*,\mappingFunctionVector}\kernelMatrix_{\mappingFunctionVector,\mappingFunctionVector}^{-1}\mappingFunctionVector,\kernelMatrix_{*,*}-\kernelMatrix_{*,\mappingFunctionVector} \kernelMatrix_{\mappingFunctionVector,\mappingFunctionVector}^{-1}\kernelMatrix_{\mappingFunctionVector,*}\right)}
  $$

* Here covariance of joint density is given by
  $$
  \kernelMatrix= \begin{bmatrix} \kernelMatrix_{\mappingFunctionVector, \mappingFunctionVector} & \kernelMatrix_{*, \mappingFunctionVector}\\ \kernelMatrix_{\mappingFunctionVector, *} & \kernelMatrix_{*, *}\end{bmatrix}
  $$

\newslide{Multivariate Conditional Density}

* Prediction of $\mappingFunctionVector_*$ from $\mappingFunctionVector$.

* Multivariate conditional density is *also* Gaussian. 
  $$
  p(\mappingFunctionVector_*|\mappingFunctionVector) = {\mathcal{N}\left(\mappingFunctionVector_*|\meanVector,\conditionalCovariance\right)}
  $$
  $$
  \meanVector= \kernelMatrix_{*,\mappingFunctionVector}\kernelMatrix_{\mappingFunctionVector,\mappingFunctionVector}^{-1}\mappingFunctionVector
  $$
  $$
  \conditionalCovariance = \kernelMatrix_{*,*}-\kernelMatrix_{*,\mappingFunctionVector} \kernelMatrix_{\mappingFunctionVector,\mappingFunctionVector}^{-1}\kernelMatrix_{\mappingFunctionVector,*}
  $$

\newslide{Prediction with Correlated Gaussians}

* Here covariance of joint density is given by
  $$
  \kernelMatrix= \begin{bmatrix} \kernelMatrix_{\mappingFunctionVector, \mappingFunctionVector} & \kernelMatrix_{*, \mappingFunctionVector}\\ \kernelMatrix_{\mappingFunctionVector, *} & \kernelMatrix_{*, *}\end{bmatrix}
  $$

\endif
