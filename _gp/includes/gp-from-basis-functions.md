\ifndef{gpFromBasisFunctions}
\define{gpFromBasisFunctions}

\editme

\subsection{Marginal Likelihood}

\notes{To understand the Gaussian process we're going to build on our
understanding of the marginal likelihood for Bayesian regression. In
the session on \refnotes{Bayesian regression}{bayesian-regression} we
sampled directly from the weight vector, $\mappingVector$ and applied
it to the basis matrix $\basisMatrix$ to obtain a sample from the
prior and a sample from the posterior. It is often helpful to think of
modeling techniques as *generative* models. To give some thought as to
what the process for obtaining data from the model is. From the
perspective of Gaussian processes, we want to start by thinking of
basis function models, where the parameters are sampled from a prior,
but move to thinking about sampling from the marginal likelihood
directly.}

\slides{* Build on our understanding of marginal likelihood.}

\include{_ml/includes/prior-sampling-basis.md}


\subsection{Function Space View}

\notes{The process we have used to generate the samples is a
two stage process. To obtain each function, we first generated a sample from the
prior,
$$
\weightVector \sim \gaussianSamp{\zerosVector}{\alpha \eye}
$$
then if we compose our basis matrix, $\basisMatrix$ from the basis
functions associated with each row then we get,
$$
\basisMatrix = \begin{bmatrix}\basisVector(\inputVector_1) \\ \vdots \\
\basisVector(\inputVector_\numData)\end{bmatrix}
$$
then we can write down the vector of function values, as evaluated at
$$
\mappingFunctionVector = \begin{bmatrix} \mappingFunction_1
\\ \vdots \\  \mappingFunction_\numData\end{bmatrix}
$$
in the form
$$
\mappingFunctionVector = \basisMatrix\weightVector.
$$}

\slides{$$
\weightVector \sim \gaussianSamp{\zerosVector}{\alpha \eye}
$$
$$
\basisMatrix = \begin{bmatrix}\basisVector(\inputVector_1) \\ \vdots \\
\basisVector(\inputVector_\numData)\end{bmatrix}
$$
$$
\mappingFunctionVector = \begin{bmatrix} \mappingFunction_1
\\ \vdots \\  \mappingFunction_\numData\end{bmatrix}
$$
$$
\mappingFunctionVector = \basisMatrix\weightVector.
$$}

\newslide{}

\notes{Now we can use standard properties of multivariate Gaussians to
write down the probability density that is implied over
$\mappingFunctionVector$. In particular we know that if
$\weightVector$ is sampled from a multivariate normal (or multivariate
Gaussian) with covariance $\alpha \eye$ and zero mean, then assuming
that $\basisMatrix$ is a deterministic matrix (i.e. it is not sampled
from a probability density) then the vector $\mappingFunctionVector$
will also be distributed according to a zero mean multivariate normal
as follows,}
$$
\mappingFunctionVector \sim \gaussianSamp{\zerosVector}{\alpha \basisMatrix\basisMatrix^\top}.
$$
\newslide{}

\notes{The question now is, what happens if we sample
$\mappingFunctionVector$ directly from this density, rather than first
sampling $\weightVector$ and then multiplying by $\basisMatrix$. Let's
try this. First of all we define the covariance as}
$$
\kernelMatrix = \alpha
\basisMatrix\basisMatrix^\top.
$$
\slides{```{.python}
K = alpha*Phi_pred@Phi_pred.T
```}
\code{K = alpha*Phi_pred@Phi_pred.T}

\notes{Now we can use the `np.random.multivariate_normal` command for
sampling from a multivariate normal with covariance given by
$\kernelMatrix$ and zero mean,}

\newslide{}

\slides{\slidesmall{```
K = alpha*Phi_pred@Phi_pred.T
f_sample = np.random.multivariate_normal(mean=np.zeros(x_pred.size), cov=K)
```}}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
for i in range(10):
    f_sample = np.random.multivariate_normal(mean=np.zeros(x_pred.size), cov=K)
    ax.plot(x_pred.flatten(), f_sample.flatten(), linewidth=2)
	
mlai.write_figure('gp-sample-basis-function.svg', directory='\writeDiagramsDir/kern')}

\figure{\includediagram{\diagramsDir/kern/gp-sample-basis-function}{80%}}{Samples directly from the covariance function implied by the basis function based covariance, $\alpha \basisMatrix\basisMatrix^\top$.}{gp-sample-basis-function}

\newslide{}

\notes{The samples appear very similar to those which we obtained
indirectly. That is no surprise because they are effectively drawn
from the same mutivariate normal density. However, when sampling
$\mappingFunctionVector$ directly we created the covariance for
$\mappingFunctionVector$. We can visualise the form of this covaraince
in an image in python with a colorbar to show scale.}

\newslide{}

\setupplotcode{import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
im = ax.imshow(K, interpolation='none')
fig.colorbar(im)

mlai.write_figure('basis-covariance-function.svg', directory='\writeDiagramsDir/kern')}

\figure{\includediagram{\diagramsDir/kern/basis-covariance-function}{60%}}{Covariance of the function implied by the basis set $\alpha\basisMatrix\basisMatrix^\top$.}{basis-covariance-function}

\newslide{}

\notes{This image is the covariance expressed between different points
on the function. In regression we normally also add independent
Gaussian noise to obtain our observations $\dataVector$,}
$$
\dataVector = \mappingFunctionVector + \boldsymbol{\epsilon}
$$
\notes{where the noise is sampled from an independent Gaussian distribution with
variance $\dataStd^2$,}
$$
\epsilon \sim \gaussianSamp{\zerosVector}{\dataStd^2\eye}.
$$
\notes{we can use properties of Gaussian variables, i.e. the fact that
sum of two Gaussian variables is also Gaussian, and that it's covariance is
given by the sum of the two covariances, whilst the mean is given by the sum of
the means, to write down the marginal likelihood,}
$$
\dataVector \sim \gaussianSamp{\zerosVector}{\basisMatrix\basisMatrix^\top +\dataStd^2\eye}.
$$
\notes{Sampling directly from this density gives us the noise
corrupted functions,}

\newslide{}

\setupplotcode{import mlai}
\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
K = alpha*Phi_pred@Phi_pred.T + sigma2*np.eye(x_pred.size)
for i in range(10):
    y_sample = np.random.multivariate_normal(mean=np.zeros(x_pred.size), cov=K)
    ax.plot(x_pred.flatten(), y_sample.flatten())
	
mlai.write_figure('gp-sample-basis-function-plus-noise.svg', 
                  directory='\writeDiagramsDir/kern')}

\figure{\includediagram{\diagramsDir/kern/gp-sample-basis-function-plus-noise}{80%}}{Samples directly from the covariance function implied by the noise corrupted basis function based covariance, $\alpha \basisMatrix\basisMatrix^\top + \dataStd^2 \eye$.}{gp-sample-basis-functions-plus-noise}

\notes{where the effect of our noise term is to roughen the sampled
functions, we can also increase the variance of the noise to see a
different effect,}

\newslide{}

\code{sigma2 = 1.
K = alpha*Phi_pred@Phi_pred.T + sigma2*np.eye(x_pred.size)}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
for i in range(10):
    y_sample = np.random.multivariate_normal(mean=np.zeros(x_pred.size), cov=K)
    plt.plot(x_pred.flatten(), y_sample.flatten())
	
mlai.write_figure('gp-sample-basis-function-plus-large-noise.svg', 
                  directory='\writeDiagramsDir/kern')}

\figure{\includediagram{\diagramsDir/kern/gp-sample-basis-function-plus-large-noise}{80%}}{Samples directly from the covariance function implied by the noise corrupted basis function based covariance, $\alpha \basisMatrix\basisMatrix^\top + \eye$.}{gp-sample-basis-functions-plus-large-noise}

\writeAssignment{**Function Space Reflection** How do you include the noise term when sampling in the weight space point of view?}{}{10}

\endif
