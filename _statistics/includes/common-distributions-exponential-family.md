\ifndef{commonDistributionsExponentialFamily}
\define{commonDistributionsExponentialFamily}
\editme

\subsection{Common Distributions as Exponential Families}

\newslide{Week 1 Families, Exponential-Family Form}

\slides{Each named distribution from the probability review is an exponential family: natural parameter $\boldsymbol{\theta}$, statistic $T$, cumulant generator $\psi$.}

\slidesincremental{
* Form: $p(x\mid\boldsymbol{\theta})=\exp\bigl(\boldsymbol{\theta}\!\cdot\! T(x)-\psi(\boldsymbol{\theta})\bigr)\,h_0(x)$
* $\psi$ is the log partition --- its derivatives are the cumulants of $T$
* $h_0$: counting, $\binom{n}{k}$, $1/k!$, or Lebesgue --- the measure from Weeks 4--5
}

\notes{Week 1 named five families without writing them in natural coordinates: Bernoulli, binomial, Poisson, multinomial/categorical, and Gaussian. Each is MaxEnt for its moment constraints relative to an appropriate base measure $h_0$, so each belongs to the exponential family
$$
p(x\mid\boldsymbol{\theta})=\exp\bigl(\boldsymbol{\theta}\cdot T(x)-\psi(\boldsymbol{\theta})\bigr)\,h_0(x).
$$
The slides below record, for each family, the natural parameter(s) $\boldsymbol{\theta}$, the sufficient statistic $T$, and the cumulant generating function $\psi$. Where $h_0$ is non-constant (binomial multiplicity, Poisson $1/k!$), that is the discrete density of states already flagged in the counting-measure discussion.}

\speakernotes{Callback to the Week 1 named list. Live spine can stay at Bernoulli / Gaussian / canonical; walk the others if clock allows, otherwise leave as slide bank.}

\newslide{Bernoulli and Binomial}

\slidesincremental{
* Bernoulli: $\theta=\mathrm{logit}(\pi)$, $\psi=\log(1+e^{\theta})$
* Binomial: same $\theta$; $\psi=n\log(1+e^{\theta})$; $h_0=\binom{n}{k}$
}

\include{_statistics/includes/bernoulli-as-exponential-family.md}
\include{_statistics/includes/binomial-as-exponential-family.md}

\newslide{Poisson and Multinomial}

\slidesincremental{
* Poisson: $\theta=\log\lambda$, $\psi=e^{\theta}$, $h_0=1/k!$
* Categorical / multinomial: $\theta_j=\log(\pi_j/\pi_K)$, $\psi=n\,\mathrm{logsumexp}$
}

\include{_statistics/includes/poisson-as-exponential-family.md}
\include{_statistics/includes/multinomial-as-exponential-family.md}

\newslide{Gaussian}

\slidesincremental{
* $T=(y,y^2)$; $\theta_1=\mu/\sigma^2$, $\theta_2=-1/(2\sigma^2)$
* $\psi$ is quadratic in $\theta_1$ and logarithmic in $\theta_2$
* Known-variance case: one parameter, $\psi(\theta)=\tfrac12\sigma^2\theta^2$
}

\include{_statistics/includes/gaussian-as-exponential-family.md}

\endif
