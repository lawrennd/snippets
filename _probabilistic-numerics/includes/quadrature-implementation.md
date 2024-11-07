\ifndef{quadratureImplementation}
\define{quadratureImplementation}

\editme

\section{Quadrature Implementation}

\notes{The implementation of Bayesian quadrature involves several key components that bridge probabilistic reasoning with numerical computation.}

\subsection{Choice of Covariance}

\notes{A critical decision in Bayesian quadrature is the choice of covariance function. For many problems, we might use:

$$p(f) = \mathcal{GP}\left(0, \theta^2(\min(x,x') - \kappa)\right)$$

This choice leads to interesting connections with classical numerical methods.}

\subsection{Quadrature Rule}

\notes{The posterior mean estimate for the integral under this prior becomes:

$$E[F] = E_{p(f|Y)}\int f(x)dx = \sum_{i=1}^{N-1} \frac{x_{i+1} - x_i}{2}(f(x_{i+1}) + f(x_i))$$

This reveals that:
* The standard trapezoidal rule emerges naturally
* The algorithm is tied to our beliefs about the function
* We get uncertainty estimates "for free"}

\notes{This is known as the "probabilistic trapezoidal rule" and demonstrates how classical numerical methods can be viewed as special cases of probabilistic approaches.}

\endif
