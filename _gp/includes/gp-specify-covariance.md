\ifndef{gpSpecifyCovariance}
\define{gpSpecifyCovariance}

\editme

\subsection{Gaussian Process}

\notes{In our \refnotes{session on Bayesian regression}{bayesian-regression} we sampled from the prior over paraemters. Through the properties of multivariate Gaussian densities this prior over parameters implies a particular density for our data observations, $\dataVector$. In this session we sampled directly from this distribution for our data, avoiding the intermediate weight-space representation. This is the approach taken by *Gaussian processes*. In a Gaussian process you specify the *covariance function* directly, rather than *implicitly* through a basis matrix and a prior over parameters. Gaussian processes have the advantage that they can be *nonparametric*, which in simple terms means that they can have *infinite* basis functions. In the lectures we introduced the *exponentiated quadratic* covariance, also known as the RBF or the Gaussian or the squared exponential covariance function. This covariance function is specified by}
$$
\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \exp\left( -\frac{\left\Vert \inputVector-\inputVector^\prime\right\Vert^2}{2\ell^2}\right),
$$
\notes{where $\left\Vert\inputVector - \inputVector^\prime\right\Vert^2$ is the squared distance between the two input vectors}
$$
\left\Vert\inputVector - \inputVector^\prime\right\Vert^2 = (\inputVector - \inputVector^\prime)^\top (\inputVector - \inputVector^\prime) 
$$
\notes{Let's build a covariance matrix based on this function. First we define the form of the covariance function,}

\loadcode{eq_cov}{mlai}

\notes{We can use this to compute *directly* the covariance for $\mappingFunctionVector$ at the points given by `x_pred`. Let's define a new function `K()` which does this,}

\loadcode{Kernel}{mlai}

\notes{Now we can image the resulting covariance,}

\code{kernel = mlai.Kernel(function=mlai.eq_cov, variance=1., lengthscale=10.)
K = kernel.K(x_pred, x_pred)}

\notes{To visualise the covariance between the points we can use the `imshow` function in matplotlib.}

\displaycode{fig, ax = plt.subplots(figsize=(8,8))
im = ax.imshow(K, interpolation='none')
fig.colorbar(im)}

\notes{Finally, we can sample functions from the marginal likelihood.}

\displaycode{fig, ax = plt.subplots(figsize=(8, 5))
for i in range(10):
    y_sample = np.random.multivariate_normal(mean=np.zeros(x_pred.size), cov=K)
    ax.plot(x_pred.flatten(), y_sample.flatten())}

\exercise{**Moving Parameters** Have a play with the parameters for this
covariance function (the lengthscale and the variance) and see what effects the
parameters have on the types of functions you observe.}


\endif
