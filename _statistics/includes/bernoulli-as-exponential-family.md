\ifndef{bernoulliAsExponentialFamily}
\define{bernoulliAsExponentialFamily}
\editme

\subsection{Bernoulli as Exponential Family}

\newslide{Bernoulli: Natural Parameter and $\psi$}

\slides{
$$
P(x\mid\theta)=\exp\bigl(x\,\theta-\psi(\theta)\bigr),\qquad x\in\{0,1\}
$$
* $\theta=\log\dfrac{\pi}{1-\pi}$,\quad $T(x)=x$
* $\psi(\theta)=\log(1+e^{\theta})$
}

\notes{A Bernoulli($\pi$) trial with $P(X=1)=\pi$ is already in exponential-family form once we take the logit as the natural parameter,
$$
\theta=\log\frac{\pi}{1-\pi},\qquad T(x)=x,\qquad \psi(\theta)=\log(1+e^{\theta}).
$$
The base measure is counting measure on $\{0,1\}$ ($h_0=1$). Recovering the mean parameter is the logistic map: $\pi=\sigma(\theta)=e^{\theta}/(1+e^{\theta})$, and $\psi'(\theta)=\pi$. The two-level thermal system with energies $0$ and $\varepsilon$ is the same family with $\theta=-\beta\varepsilon$.}

\speakernotes{One slide. Logit is $\theta$; softplus is $\psi$. Same object as the two-level system.}

\endif
