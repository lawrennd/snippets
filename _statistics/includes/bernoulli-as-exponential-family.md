\ifndef{bernoulliAsExponentialFamily}
\define{bernoulliAsExponentialFamily}
\editme

\subsection{Bernoulli as Exponential Family}

\newslide{Bernoulli: Natural Parameter and $\psi$}

\slides{
$$
P(x\mid\theta)=\exp\bigl(x\,\theta-\psi(\theta)\bigr)\,h_0(x),\qquad x\in\{0,1\}
$$
* $\theta=\log\dfrac{\pi}{1-\pi}$,\quad $T(x)=x$
* $\psi(\theta)=\log(1+e^{\theta})$,\quad $h_0(x)=1$ (counting on $\{0,1\}$)
}

\notes{A Bernoulli($\pi$) trial with $P(X=1)=\pi$ is already in exponential-family form once we take the logit as the natural parameter,
$$
\theta=\log\frac{\pi}{1-\pi},\qquad T(x)=x,\qquad \psi(\theta)=\log(1+e^{\theta}).
$$
The base density is $h_0(x)=1$: counting measure on the two labels. That is the unnoticed prior from the counting-measure slide --- each of $\{0,1\}$ has weight one, so Shannon $H$ on a Bernoulli is $\log 2-\mathrm{KL}(P\|u)$ with $u$ uniform on those two outcomes. Recovering the mean parameter is the logistic map: $\pi=\sigma(\theta)=e^{\theta}/(1+e^{\theta})$, and $\psi'(\theta)=\pi$. The two-level thermal system with energies $0$ and $\varepsilon$ is the same family with $\theta=-\beta\varepsilon$.}

\speakernotes{Point one of two. Write $h_0=1$ on the board: Bernoulli *is* MaxEnt relative to counting measure. Logit is $\theta$; softplus is $\psi$. Same object as the two-level system. Binomial / Poisson next flip $h_0$ away from 1.}

\endif
