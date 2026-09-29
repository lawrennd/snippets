\ifndef{commonDistributionsReview}
\define{commonDistributionsReview}
\editme

\subsection{Common Distributions}

\newslides{Named Distributions You Need}

\slides{Five families recur across modelling. Know the support, the parameter, and one generative story for each.}

\notes{These are prerequisites restated, not new theory. Several of them reappear later as maximum-entropy distributions under moment constraints.}

\newslides{Bernoulli and Binomial}

\slidesincremental{
* Bernoulli($p$): single binary trial; $P(X=1)=p$
* Binomial($n,p$): $n$ i.i.d. Bernoulli trials; count of successes
* Mean $np$, variance $np(1-p)$
}

\notes{A fair coin is Bernoulli($1/2$). A two-state thermal system with fixed energies is Bernoulli once occupation probabilities are written down.}

\newslides{Poisson and Multinomial}

\slidesincremental{
* Poisson($\lambda$): counts in a fixed interval; mean $=$ variance $=\lambda$
* Multinomial($n,\mathbf{p}$): $n$ trials into $K$ categories; generalises the binomial
* Categories are exclusive; $\sum_k p_k = 1$
}

\include{_ml/includes/poisson-distribution.md}

\newslides{Gaussian}

\slidesincremental{
* $\mathcal{N}(\mu,\sigma^2)$: continuous density on $\mathbb{R}$
* Fixed by mean and variance; MaxEnt under those constraints
* Multivariate form: mean vector and covariance matrix
}

\notes{Differential entropy of a Gaussian grows with $\sigma$ and can be negative. For a review, recognise the density and the two parameters.}

\include{_ml/includes/univariate-gaussian.md}

\endif
