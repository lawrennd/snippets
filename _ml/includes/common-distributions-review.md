\ifndef{commonDistributionsReview}
\define{commonDistributionsReview}
\editme

\subsection{Common Distributions}

\newslide{Named Distributions You Need}

\slides{Five families recur across modelling. Know the support, the parameter, and one generative story for each.}

\notes{These are prerequisites restated, not new theory. The Gaussian (and the categorical) reappear later as maximum-entropy distributions under ordinary moment constraints. The Poisson is maximum-entropy only relative to the base measure $1/k!$, and the binomial only relative to $\binom{n}{k}$. Among distributions on the non-negative integers with a fixed mean, the maximum-entropy one is the geometric. Week 4's point that ``the discretisation is the measure'' --- Jaynes's $m$ --- is the reason those caveats exist.}

\newslide{Bernoulli and Binomial}

\slidesincremental{
* Bernoulli($p$): single binary trial; $P(X=1)=p$
* Binomial($n,p$): $n$ i.i.d. Bernoulli trials; count of successes
* Mean $np$, variance $np(1-p)$
}

\notes{A fair coin is Bernoulli($1/2$). A two-state thermal system with fixed energies is Bernoulli once occupation probabilities are written down. Binomial$(n,p)$ is $n$ independent Bernoulli trials, $P(K=k)=\binom{n}{k}p^k(1-p)^{n-k}$, with mean $np$.}

\newslide{Poisson and Multinomial}

\slidesincremental{
* Poisson($\lambda$): counts in a fixed interval; mean $=$ variance $=\lambda$
* Multinomial($n,\mathbf{p}$): $n$ trials into $K$ categories; generalises the binomial
* Categories are exclusive; $\sum_k p_k = 1$
}

\notes{Poisson$(\lambda)$ is a count model with mean equal to variance. Multinomial$(n,\mathbf{p})$ is $n$ trials into $K$ exclusive categories; the binomial is the $K=2$ case.}

\include{_ml/includes/poisson-distribution.md}

\newslide{Gaussian}

\slidesincremental{
* $\mathcal{N}(\mu,\sigma^2)$: continuous density on $\mathbb{R}$
* Fixed by mean and variance; MaxEnt under those constraints
* Multivariate form: mean vector and covariance matrix
}

\notes{Differential entropy of a Gaussian grows with $\sigma$ and can be negative. For a review, recognise the density and the two parameters.}

\include{_ml/includes/univariate-gaussian.md}

\endif
