\ifndef{inducingVariablesDemo}
\define{inducingVariablesDemo}
\editme

\notes{
\subsection{A Simple Regression Problem}

Here we set up a simple one dimensional regression problem. The input locations, $\inputMatrix$, are in two separate clusters. The response variable, $\dataVector$, is sampled from a Gaussian process with an exponentiated quadratic covariance.}

\setupcode{import numpy as np
from mlai import Kernel, eq_cov, GP, SparseGP, SCG}

\setupcode{np.random.seed(101)}

\code{N = 50
noise_var = 0.01
X = np.zeros((50, 1))
X[:25, :] = np.linspace(0,3,25)[:,None] # First cluster of inputs/covariates
X[25:, :] = np.linspace(7,10,25)[:,None] # Second cluster of inputs/covariates

# Sample response variables from a Gaussian process with exponentiated quadratic covariance.
k = Kernel(eq_cov)
y = np.random.multivariate_normal(np.zeros(N),k.K(X)+np.eye(N)*np.sqrt(noise_var)).reshape(-1,1)}

\notes{First we perform a full Gaussian process regression on the data. We create a GP model, `m_full`, and fit it to the data, plotting the resulting fit.}

\code{kernel_full = Kernel(eq_cov)
m_full = GP(X, y, sigma2=1.0, kernel=kernel_full)
_ = SCG().optimize(m_full) # Optimize parameters of covariance function}

\setupdisplaycode{import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot 
from mlai.gp_tutorial import gpplot}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2)
xlim = ax.get_xlim()
ylim = ax.get_ylim()
mlai.write_figure(figure=fig,
                  filename='sparse-demo-full-gp.svg',
                  directory='\writeDiagramsDir/gp/')}

\newslide{Full Gaussian Process Fit}

\figure{\includediagram{\diagramsDir/gp/sparse-demo-full-gp}{80%}}{Full Gaussian process fitted to the data set.}{sparse-demo-full-gp}

\notes{Now we set up the inducing variables, $\mathbf{u}$. Each inducing variable has its own associated input index, $\mathbf{Z}$, which lives in the same space as $\inputMatrix$. Here we are using the true covariance function parameters to generate the fit. With `optimize_Z=False`, the inducing inputs stay fixed while noise and kernel hyperparameters remain free.}

\code{kern = Kernel(eq_cov)
Z = np.hstack(
        (np.linspace(2.5,4.,3),
        np.linspace(7,8.5,3)))[:,None]
m = SparseGP(X, y, Z, sigma2=noise_var, kernel=kern, optimize_Z=False)
print(m)}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2, xlim=xlim, ylim=ylim)
mlai.write_figure(figure=fig,
                  filename='sparse-demo-constrained-inducing-6-unlearned-gp.svg', 
                  directory='\writeDiagramsDir/gp/')}

\newslide{Inducing Variable Fit}

\figure{\includediagram{\diagramsDir/gp/sparse-demo-constrained-inducing-6-unlearned-gp}{80%}}{Sparse Gaussian process fitted with six inducing variables, no optimization of parameters or inducing variables.}{sparse-demo-constrained-inducing-6-unlearned-gp}

\code{_ = SCG().optimize(m)
print(m)}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2, xlim=xlim, ylim=ylim)
mlai.write_figure(figure=fig,
                  filename='sparse-demo-constrained-inducing-6-learned-gp.svg',
                  directory='\writeDiagramsDir/gp/')}

\newslide{Inducing Variable Param Optimize}

\figure{\includediagram{\diagramsDir/gp/sparse-demo-constrained-inducing-6-learned-gp}{80%}}{Gaussian process fitted with inducing variables fixed and parameters optimized}{sparse-demo-constrained-inducing-6-learned-gp}

\notes{Next we free the inducing inputs. A new sparse model starts from the same $\mathbf{Z}$ and hyperparameters, now with `optimize_Z=True`, so scaled conjugate gradients can move the inducing locations as well.}

\code{kern_free = Kernel(eq_cov, **dict(m.kernel.parameters))
m = SparseGP(X, y, m.Z.copy(), sigma2=m.sigma2, kernel=kern_free, optimize_Z=True)
_ = SCG().optimize(m)}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2,xlim=xlim, ylim=ylim)
mlai.write_figure(figure=fig,
                  filename='sparse-demo-unconstrained-inducing-6-gp.svg', 
                  directory='\writeDiagramsDir/gp/')}

\newslide{Inducing Variable Full Optimize}

\figure{\includediagram{\diagramsDir/gp/sparse-demo-unconstrained-inducing-6-gp}{80%}}{Gaussian process fitted with location of inducing variables and parameters both optimized}{sparse-demo-unconstrained-inducing-6-gp}

\notes{Now we will vary the number of inducing points used to form the approximation.}

\code{M = 8
Z8 = np.random.rand(M,1)*12
kern8 = Kernel(eq_cov, **dict(m.kernel.parameters))
m = SparseGP(X, y, Z8, sigma2=m.sigma2, kernel=kern8, optimize_Z=True)
_ = SCG().optimize(m)}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m, ax=ax, xlabel='$x$', ylabel='$y$', fontsize=20, portion=0.2, xlim=xlim, ylim=ylim)
mlai.write_figure(figure=fig,
                  filename='sparse-demo-sparse-inducing-8-gp.svg', 
                  directory='\writeDiagramsDir/gp/')}

\slides{
\newslide{Eight Optimized Inducing Variables}

\includediagram{\diagramsDir/gp/sparse-demo-sparse-inducing-8-gp}

\newslide{Full Gaussian Process Fit}

\includediagram{\diagramsDir/gp/sparse-demo-full-gp}
}

\figure{\includediagram{\diagramsDir/gp/sparse-demo-sparse-inducing-8-gp}{80%}
\includediagram{\diagramsDir/gp/sparse-demo-full-gp}{80%}}{Comparison of the full Gaussian process fit with a sparse Gaussian process using eight inducing varibles. Both inducing variables and parameters are optimized.}{sparse-demo-sparse-inducing-8}

\notes{And we can compare the probability of the result to the full model.}
\code{print(m.log_likelihood(), m_full.log_likelihood())}


\endif
