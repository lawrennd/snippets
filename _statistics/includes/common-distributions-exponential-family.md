\ifndef{commonDistributionsExponentialFamily}
\define{commonDistributionsExponentialFamily}
\editme

\subsection{Common Distributions as Exponential Families}

\newslide{Week 1 Families, Exponential-Family Form}

\slides{Each named distribution from the probability review is an exponential family --- and each carries a base measure $h_0$.}

\slidesincremental{
* Form: $p=\exp\bigl(\boldsymbol{\theta}\!\cdot\! T-\psi\bigr)\,h_0$
* Two stories for $h_0$: counting prior ($h_0=1$) versus combinatorial / continuum measure
* Bernoulli, categorical: plain counting on the labels
* Binomial, Poisson, multinomial: result is a macroscopic of a microscopic sum
* Gaussian: Lebesgue (continuous counterpart of #)
}

\notes{Week 1 named five families without writing them in natural coordinates: Bernoulli, binomial, Poisson, multinomial/categorical, and Gaussian. Each is MaxEnt for its moment constraints relative to an appropriate base measure $h_0$, so each belongs to the exponential family
$$
p(x\mid\boldsymbol{\theta})=\exp\bigl(\boldsymbol{\theta}\cdot T(x)-\psi(\boldsymbol{\theta})\bigr)\,h_0(x).
$$
The slides below record, for each family, the natural parameter(s) $\boldsymbol{\theta}$, the sufficient statistic $T$, the cumulant generating function $\psi$, and --- the point of this block --- which $h_0$ is in force. Two emphases run through the tour. First, when $h_0=1$ (Bernoulli; categorical $n=1$), the base is counting measure: every allowed label has prior weight one, the same unnoticed prior as $H=\log N-\mathrm{KL}(P\|u)$. Second, when $h_0$ is non-constant (binomial $\binom{n}{k}$, Poisson $1/k!$, multinomial $n!/\prod_j x_j!$), that factor is the discrete density of states: same moment constraints relative to plain $\#$ would give a *different* family. Gaussian uses Lebesgue --- the continuum counterpart of $\#$.}

\speakernotes{Callback to the Week 1 named list. Protect two sentences: (1) Bernoulli $h_0=1$ *is* counting measure as prior; (2) Poisson $1/k!$ / binomial $\binom{n}{k}$ show why the family carries an $h_0$ at all. Live spine: Bernoulli then Poisson (or binomial) for the contrast; Gaussian for Lebesgue. Multinomial if clock allows.}

\newslide{Bernoulli and Binomial}

\slides{Same $\theta$; different $h_0$. That is the measure story in one pair.}

\slidesincremental{
* Bernoulli: $\theta=\mathrm{logit}(\pi)$, $\psi=\log(1+e^{\theta})$, $h_0=1$ (counting)
* Binomial: same $\theta$; $\psi=n\log(1+e^{\theta})$; $h_0=\binom{n}{k}$ (multiplicity)
}

\include{_statistics/includes/bernoulli-as-exponential-family.md}
\include{_statistics/includes/binomial-as-exponential-family.md}

\newslide{Poisson and Multinomial}

\slides{Poisson makes the non-constant $h_0$ unavoidable: without $1/k!$ you do not get Poisson.}

\slidesincremental{
* Poisson: $\theta=\log\lambda$, $\psi=e^{\theta}$, $h_0=1/k!$
* Categorical: $h_0=1$ (counting again); multinomial: $h_0=n!/\prod_j x_j!$
}

\include{_statistics/includes/poisson-as-exponential-family.md}
\include{_statistics/includes/multinomial-as-exponential-family.md}

\newslide{Gaussian}

\slides{Continuous close: $h_0$ is Lebesgue --- the continuum counterpart of $\#$.}

\slidesincremental{
* $T=(y,y^2)$; $\theta_1=\mu/\sigma^2$, $\theta_2=-1/(2\sigma^2)$
* $h_0$: Lebesgue (not counting; not $1/k!$)
* $\psi$ is quadratic in $\theta_1$ and logarithmic in $\theta_2$
}

\include{_statistics/includes/gaussian-as-exponential-family.md}

\endif
