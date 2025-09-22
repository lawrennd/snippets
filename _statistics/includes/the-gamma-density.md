\ifndef{theGammaDensity}
\define{theGammaDensity}

\editme

\subsection{The Gamma Density}

\notes{The Gamma is a density over positive numbers. It has the
form
$$ 
\gammaDist{x}{a}{b}=\frac{b^{a}}{\Gamma\left(a\right)}x^{a-1}e^{-bx},
$$ 
where $a$ is known as the shape parameter and $b$ is known as a rate
parameter. The function $\Gamma\left(a\right)$ is known as the gamma
function and is defined through the following indefinite integral,
$$
\Gamma\left(a\right)=\int_{0}^{\infty}x^{a-1}e^{-x}\text{d}x.
$$
The mean of the gamma density is given by
$$ 
\expectationDist{x}{\gammaDist{x}{a}{b}}=\frac{a}{b}
$$ 
and the variance is given by
$$
\varianceDist{x}{\gammaDist{x}{a}{b}}=\frac{a}{b^{2}}.
$$ 
Sometimes the density is defined in terms of a scale parameter,
$\beta=b^{-1}$, instead of a rate. Confusingly, this parameter is
also often denoted by "$b$". For example, the statistics toolbox
in Matlab defines things this way. The gamma density
generalises several important special cases including the
exponential density with rate $b$, $\expDist{x}{b}$, which is the
specific case where the shape parameter is taken to be $a=1$. The
chi-squared density with one degree of freedom, denoted
$\chiSquaredDist{1}{x}$, is the special case where the shape
parameter is taken to be $a=\frac{1}{2}$ and the rate parameter is
$b=\frac{1}{2}$.

The gamma density is the conjugate density for the inverse variance
(precision) of a Gaussian density.

Gamma random variables have the property that, if multiple gamma
variates are sampled from a density with the same rate, $b$, and
shape parameters $\left\{a_k\right\}^\dataDim_{k=1}$, then the sum
of those variates is also Gamma distributed with rate parameter $b$
and shape parameter $a^\prime = \sum_{k=1}^\dataDim a_k$.}

\newslide{Gamma Density Formula}

\slides{
  \aligncenter{$$\gammaDist{x}{a}{b}=\frac{b^{a}}{\Gamma\left(a\right)}x^{a-1}e^{-bx}$$}
  
  * Shape parameter: $a$ (controls form)
  * Rate parameter: $b$ (controls scale)
  * Gamma function: $\Gamma\left(a\right)=\int_{0}^{\infty}x^{a-1}e^{-x}\text{d}x$
  }

\newslide{Gamma Properties}
\slides{
  * Mean: $\frac{a}{b}$, 
  * Variance: $\frac{a}{b^{2}}$
  * Support: $x > 0$ (positive numbers only)
  }

\notes{\subsection{Summary}}

\notes{The gamma density is a flexible probability distribution over positive numbers with two parameters: shape ($a$) and rate ($b$). The shape parameter controls the form of the distribution, while the rate parameter controls the scale. The mean and variance are both proportional to the shape parameter, with the mean being $a/b$ and variance being $a/b^2$. The gamma function $\Gamma(a)$ serves as the normalizing constant.}

\newslide{Special Cases}
\slides{ 
  * Exponential
    $a=1$ $\rightarrow$ $\expDist{x}{b}$
  * $\chi^2$ (chi-squared, 1 df) 
    $a=\frac{1}{2}, b=\frac{1}{2}$ $\rightarrow$ $\chiSquaredDist{1}{x}$
}

\newslide{Other Important Applications}
\slides{
  * Conjugate prior for Gaussian precision (inverse variance)
  * Modeling waiting times and lifetimes
}

\notes{The gamma density generalizes several important distributions. When the shape parameter $a=1$, it becomes the exponential distribution with rate $b$. When $a=\frac{1}{2}$ and $b=\frac{1}{2}$, it becomes the chi-squared distribution with one degree of freedom. The gamma distribution is particularly important in Bayesian statistics as the conjugate prior for the precision (inverse variance) of Gaussian distributions, making it essential for Bayesian inference about variance parameters.}

\newslide{Additive Property}

\slides{
  * If 
  $$
  x_k \sim \text{Gamma}(a_k, b)
  $$ 
  for $k=1,\ldots,\dataDim$
  * Then 
  $$
  \sum_{k=1}^\dataDim x_k \sim \text{Gamma}(\sum_{k=1}^d a_k, b)
  $$
}

\newslide{Warning: Parameterisation Confusion}

\slides{
  * Rate parameter: $b$ (used here)
  * Scale parameter: $\beta = b^{-1}$ (alternative)
  * Watch out for different software conventions.
}
\notes{Gamma distributions have a useful additive property: the sum of independent gamma random variables with the same rate parameter is also gamma distributed, with the shape parameter being the sum of the individual shape parameters. This property is crucial for many applications in statistics and probability. However, be careful with parameterization - some software uses a scale parameter $\beta = b^{-1}$ instead of the rate parameter $b$, which can lead to confusion when implementing gamma distributions in different programming environments.}

\endif
