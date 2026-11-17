\ifndef{poissonAsExponentialFamily}
\define{poissonAsExponentialFamily}
\editme

\subsection{Poisson as Exponential Family}

\newslide{Poisson: Natural Parameter and $\psi$}

\slides{
$$
P(k\mid\theta)=\exp\bigl(k\,\theta-\psi(\theta)\bigr)\,h_0(k),\qquad k\in\mathbb{N}_0
$$
* $\theta=\log\lambda$,\quad $T(k)=k$
* $\psi(\theta)=e^{\theta}$,\quad $h_0(k)=1/k!$
}

\notes{Poisson($\lambda$) has probability mass
$$
P(k)=\frac{\lambda^k e^{-\lambda}}{k!}.
$$
In exponential-family coordinates the rate becomes a natural parameter through $\theta=\log\lambda$, the count is the sufficient statistic $T(k)=k$, and the cumulant generating function is simply
$$
\psi(\theta)=e^{\theta}=\lambda.
$$
The factorial in the denominator is the base measure $h_0(k)=1/k!$; without it, MaxEnt under a mean-count constraint would give a geometric distribution, not a Poisson. Differentiating recovers the familiar moments: $\psi'(\theta)=\lambda$ and $\psi''(\theta)=\lambda$ (mean equals variance).}

\speakernotes{Emphasise $h_0=1/k!$. The Week 4--5 measure story is why Poisson is not MaxEnt under plain counting measure.}

\endif
