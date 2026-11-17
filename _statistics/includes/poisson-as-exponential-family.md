\ifndef{poissonAsExponentialFamily}
\define{poissonAsExponentialFamily}
\editme

\subsection{Poisson as Exponential Family}

\newslide{Poisson: Why $h_0$ Is Not Optional}

\slides{
$$
P(k\mid\theta)=\exp\bigl(k\,\theta-\psi(\theta)\bigr)\,h_0(k),\qquad k\in\mathbb{N}_0
$$

* $\theta=\log\lambda$,\quad $T(k)=k$,\quad $\psi(\theta)=e^{\theta}$
* $h_0(k)=1/k!$ --- without it, mean-count MaxEnt is *geometric*, not Poisson
}

\notes{Poisson($\lambda$) has probability mass
$$
P(k)=\frac{\lambda^k e^{-\lambda}}{k!}.
$$
In exponential-family coordinates the rate becomes a natural parameter through $\theta=\log\lambda$, the count is the sufficient statistic $T(k)=k$, and the cumulant generating function is simply
$$
\psi(\theta)=e^{\theta}=\lambda.
$$
The factorial in the denominator is the base measure $h_0(k)=1/k!$ with respect to counting measure on $\mathbb{N}_0$. This is the sharpest discrete illustration of the Weeks 4--5 story: the exponential tilt $\exp(\theta\,T-\psi)$ is only half the model; the base $h_0$ is the other half. MaxEnt under a fixed mean count *relative to plain counting measure* ($h_0=1$) yields a geometric distribution. MaxEnt relative to $h_0=1/k!$ yields Poisson. Same constraint, different measure, different family --- the discrete counterpart of Lebesgue versus $v^2\mathrm{d}v$. Differentiating recovers the familiar moments: $\psi'(\theta)=\lambda$ and $\psi''(\theta)=\lambda$ (mean equals variance).}

\speakernotes{Point two, sharpened. Board $h_0=1/k!$ beside Bernoulli's $h_0=1$. One sentence: counting prior gave Bernoulli; combinatorial measure gives Poisson. Do not derive the geometric MaxEnt unless asked --- naming the contrast is enough.}

\endif
