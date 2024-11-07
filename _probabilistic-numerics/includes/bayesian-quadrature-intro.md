\ifndef{bayesianQuadratureIntro}
\define{bayesianQuadratureIntro}

\editme

\section{Bayesian Quadrature}

\notes{Bayesian quadrature provides a probabilistic approach to numerical integration. Consider the problem of computing an integral:

$$F := \int f(x)d\nu(x)$$

where $\nu(x)$ is the measure we're integrating over.}

\subsection{Probabilistic Framework}

\notes{In the Bayesian framework [O'Hagan, 1991], we can express this as:

$$p(F, Y) = \int p(F|f)p(Y|f)p(f)df$$

This decomposes into:

$$p(F|f)p(Y|f)p(f) = \delta\left(F - \int_X f dx\right)\prod_i \delta(y_i - f(x_i))p(f)$$

The result is a Gaussian distribution for $p(F|Y)$ with mean $\mu_F$ and variance $k_F$.}

\subsection{Advantages}

\notes{This probabilistic approach offers several advantages:
* Uncertainty quantification in the integral estimate
* Principled way to select evaluation points
* Natural framework for incorporating prior knowledge
* Ability to reason about computational resource allocation}

\endif
