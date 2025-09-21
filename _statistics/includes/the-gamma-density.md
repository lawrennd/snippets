\ifndef{theGammaDensity}
\define{theGammaDensity}

\editme

\subsection{The Gamma Density}

\notes{  The Gamma is a density over positive numbers. It has the
  form
  \[ 
  \gammaDist{x}{a}{b}=\frac{b^{a}}{\Gamma\left(a\right)}x^{a-1}e^{-bx},
  \] 
  where $a$ is known as the shape parameter and $b$ is known as a rate
  parameter. The function $\Gamma\left(a\right)$ is known as the gamma
  function and is defined through the following indefinite integral,
  \[
  \Gamma\left(a\right)=\int_{0}^{\infty}x^{a-1}e^{-x}\text{d}x.
  \]
  The mean of the gamma density is given by
  \[ 
  \expectationDist{x}{\gammaDist{x}{a}{b}}=\frac{a}{b}
  \] 
  and the variance is given by
  \[
  \varianceDist{x}{\gammaDist{x}{a}{b}}=\frac{a}{b^{2}}.
  \] 
  Sometimes the density is defined in terms of a scale parameter,
  $\beta=b^{-1}$, instead of a rate. Confusingly, this parameter is
  also often denoted by ``$b$''. For example, the statistics toolbox
  in \textsc{Matlab} defines things this way. The gamma density
  generalizes several important special cases including the
  exponential density with rate $b$, $\expDist{x}{b}$, which is the
  specific case where the shape parameter is taken to be $a=1$. The
  chi-squared density with one degree of freedom, denoted
  $\chiSquaredDist{1}{x}$, is the special case where the shape
  parameter is taken to be $a=\frac{1}{2}$ and the rate parameter is
  $b=\frac{1}{2}$.

  The gamma density is the conjugate density for the inverse variance
  (precision) of a Gaussian density. See \refbox{box:conjugacy} for
  more on conjugacy in Bayesian inference.

  Gamma random variables have the property that, if multiple gamma
  variates are sampled from a density with the same rate, $b$, and
  shape parameters $\left\{a_k\right\}^\dataDim_{k=1}$, then the sum
  of those variates is also Gamma distributed with rate parameter $b$
  and shape parameter $a^\prime = \sum_{k=1}^\dataDim a_k$.}

\endif
