\ifndef{integrationExample}
\define{integrationExample}

\editme

\subsection{Integration Example}

\notes{Consider a concrete example of probabilistic integration. We want to compute:

$$F := \int_{-3}^3 e^{-(sin(3x))^2-x^2} dx$$

This integral has several interesting properties:

* $f(x)$ is strictly positive, therefore $F > 0$
* $f(x)$ is bounded above by $e^{-x^2}$
* Therefore, $0 < F < \sqrt{\pi}$}

\subsection{Probabilistic Solution}

\notes{We can approach this problem by:

1. Placing a Gaussian process prior over $f(x)$
2. Conditioning on function evaluations
3. Computing the induced distribution over the integral

The posterior mean of this distribution gives us our estimate, while the posterior variance quantifies our uncertainty.}

\endif
