\ifndef{commonDistributionsReview}
\define{commonDistributionsReview}
\editme

\subsection{Common Distributions}

\newslides{Named Distributions You Need}

\slides{Five families appear throughout the course. Know the support, the parameter, and one generative story for each.}

\notes{These are prerequisites restated, not new theory. Quiz 1 will ask recognition and simple calculations. Later weeks recover several of them as maximum-entropy distributions.}

\newslides{Bernoulli and Binomial}

\slidesincremental{
* Bernoulli($p$): single binary trial; $P(X=1)=p$
* Binomial($n,p$): $n$ i.i.d. Bernoulli trials; count of successes
* Mean $np$, variance $np(1-p)$
}

\notes{A fair coin is Bernoulli($1/2$). The two-state thermal system you meet next week is Bernoulli in disguise once energies are fixed.}

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
* Fixed by mean and variance; MaxEnt under those constraints (week 5)
* Multivariate form: mean vector and covariance matrix
}

\notes{Differential entropy of a Gaussian grows with $\sigma$ and can be negative — that subtlety waits until week 6. Today: recognise the density and the two parameters.}

\include{_ml/includes/univariate-gaussian.md}

\endif
