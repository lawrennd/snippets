\ifndef{gaussianSampleStatistics}
\define{gaussianSampleStatistics}

\editme

\subsection{Sampling from a Gaussian}

\notes{Let's test the relationship between samples and the true mean numerically. First we will draw 200 samples from a standard normal.}

\code{w_vec = np.random.normal(size=200)}

\notes{We can compute the mean of these samples and their variance}

\code{print('w sample mean is ', w_vec.mean())
print('w sample variance is ', w_vec.var())}

\notes{These are close to zero (the mean) and one (the variance) as you'd expect. Now compute the mean and variance of the scaled version,}

\code{phi = 7
f_vec = phi*w_vec
print('True mean should be phi*0 = 0.')
print('True variance should be phi*phi*1 = ', phi*phi)
print('f sample mean is ', f_vec.mean())
print('f sample variance is ', f_vec.var())}

\notes{If you increase the number of samples then you will see that the sample mean and the sample variance begin to converge towards the true mean and the true variance. Obviously adding an offset to a sample from `np.random.normal` will change the mean. So if you want to sample from a Gaussian with mean `mu` and standard deviation `sigma` one way of doing it is to sample from the standard normal and scale and shift the result, so to sample a set of $\mappingScalar$ from a Gaussian with mean $\meanScalar$ and variance $\alpha$,
$$\mappingScalar \sim \gaussianSamp{\meanScalar}{\alpha}$$
We can simply scale and offset samples from the *standard normal*.}

\code{mu = 4 # mean of the distribution
alpha = 2 # variance of the distribution
w_vec = np.random.normal(size=200)*np.sqrt(alpha) + mu
print('w sample mean is ', w_vec.mean())
print('w sample variance is ', w_vec.var())}

\notes{Here the `np.sqrt` is necesssary because we need to multiply by the standard deviation and we specified the variance as `alpha`. So scaling and offsetting a Gaussian distributed variable keeps the variable Gaussian, but it effects the mean and variance of the resulting variable. }

\notes{To get an idea of the overall shape of the resulting distribution, let's do the same thing with a histogram of the results.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot}


\plotcode{# First the standard normal
z_vec = np.random.normal(size=1000) # by convention, in statistics, z is often used to denote samples from the standard normal
w_vec = z_vec*np.sqrt(alpha) + mu
# plot normalized histogram of w, and then normalized histogram of z on top
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.hist(w_vec, bins=30, density=True)
ax.hist(z_vec, bins=30, density=True)
_ = ax.legend(('$w$', '$z$'))}

\notes{Now re-run this histogram with 100,000 samples and check that the both histograms look qualitatively Gaussian.
}

\subsection{Scaling Gaussian-distributed Variables}

\notes{First, let's consider the case where we have one data point and one feature in our basis set. In otherwords $\mappingFunctionVector$ would be a scalar, $\mappingVector$ would be a scalar and $\basisMatrix$ would be a scalar. In this case we have}
$$
\mappingFunction = \basisScalar \mappingScalar
$$
\notes{If $\mappingScalar$ is drawn from a normal density,}
$$
\mappingScalar \sim \gaussianSamp{\meanScalar_\mappingScalar}{c_\mappingScalar}
$$
\notes{and $\basisScalar$ is a scalar value which we are given, then properties of the Gaussian density tell us that}
$$
\basisScalar \mappingScalar \sim \gaussianSamp{\basisScalar\meanScalar_\mappingScalar}{\basisScalar^2c_\mappingScalar}
$$



\endif
