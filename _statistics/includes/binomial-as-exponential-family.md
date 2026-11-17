\ifndef{binomialAsExponentialFamily}
\define{binomialAsExponentialFamily}
\editme

\subsection{Binomial as Exponential Family}

\newslide{Binomial: Natural Parameter and $\psi$}

\slides{
$$
P(k\mid\theta)=\exp\bigl(k\,\theta-\psi(\theta)\bigr)\,h_0(k),\qquad k=0,\ldots,n
$$
* $\theta=\log\dfrac{\pi}{1-\pi}$,\quad $T(k)=k$
* $\psi(\theta)=n\log(1+e^{\theta})$,\quad $h_0(k)=\binom{n}{k}$
}

\notes{Binomial$(n,\pi)$ is $n$ i.i.d.\ Bernoulli trials counted. The natural parameter is the same logit as the Bernoulli,
$$
\theta=\log\frac{\pi}{1-\pi},\qquad T(k)=k,
$$
but the cumulant generating function scales with the number of trials,
$$
\psi(\theta)=n\log(1+e^{\theta}),
$$
and the base measure carries the combinatorial multiplicity $h_0(k)=\binom{n}{k}$. That multiplicity is the discrete density of states --- the same role $v^2$ played for Maxwell--Boltzmann. MaxEnt under a mean-count constraint *relative to plain counting measure* does *not* recover the binomial; MaxEnt relative to $\binom{n}{k}\,{\mathrm{d}}\#$ does. Same $\theta$ as Bernoulli; different prior weight on the count $k$. Mean and variance follow by differentiation: $\psi'(\theta)=n\pi$, $\psi''(\theta)=n\pi(1-\pi)$.}

\speakernotes{Point two begins here. Same $\theta$ as Bernoulli; $\psi$ is $n$ times the softplus. The new object is $h_0=\binom{n}{k}$: without that multiplicity you are not looking at the binomial. Say ``discrete density of states'' and move on --- Poisson repeats the lesson with $1/k!$.}

\endif
