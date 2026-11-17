\ifndef{exponentialFamilyEntropyFisher}
\define{exponentialFamilyEntropyFisher}

\editme

\subsection{Entropy of an Exponential Family}

\notes{Once $p$ is written as an exponential family, Shannon entropy collapses to an algebraic identity in $\psi$ and $\boldsymbol{\eta}$. That identity is the bridge to Fisher information: the same $\log p$ whose expectation is $-H$ has a score whose second moment is $\nabla^2\psi$.}

\newslide{Entropy: the Lovely Form}

\slides{
$$
\log p(x\mid\boldsymbol{\theta})=\boldsymbol{\theta}\cdot T(x)-\psi(\boldsymbol{\theta})
$$
}

\slidesincremental{
* Take $-\mathbb{E}[\log p]$: $H=\psi-\boldsymbol{\theta}\cdot\boldsymbol{\eta}$ when $h_0=1$
* with $\boldsymbol{\eta}=\nabla\psi=\langle T\rangle$
* In general: $H=\psi-\boldsymbol{\theta}\cdot\boldsymbol{\eta}-\mathbb{E}[\log h_0(X)]$
}

\speakernotes{Board the two-line derivation for $h_0=1$. $\log p=\theta\cdot T-\psi$; expectation kills $T$ to $\eta$; $H=\psi-\theta\cdot\eta$. After Poisson / binomial, state the general correction $-\mathbb{E}[\log h_0]$ once so nobody applies the short form to a Poisson. Today the boarded algebra uses $h_0=1$ on the allowed set.}

\notes{Write $\log p(x\mid\boldsymbol{\theta})=\boldsymbol{\theta}\cdot T(x)-\psi(\boldsymbol{\theta})+\log h_0(x)$. When the base is counting measure on the allowed set ($h_0=1$), Shannon entropy collapses to
\begin{align}
H(\boldsymbol{\theta})
&=-\mathbb{E}_{\boldsymbol{\theta}}[\log p(X\mid\boldsymbol{\theta})]
=\psi(\boldsymbol{\theta})-\boldsymbol{\theta}\cdot\mathbb{E}_{\boldsymbol{\theta}}[T(X)]
=\psi(\boldsymbol{\theta})-\boldsymbol{\theta}\cdot\boldsymbol{\eta},
\end{align}
with $\boldsymbol{\eta}=\nabla\psi$. In general the base survives as
\begin{align}
H(\boldsymbol{\theta})=\psi(\boldsymbol{\theta})-\boldsymbol{\theta}\cdot\boldsymbol{\eta}-\mathbb{E}_{\boldsymbol{\theta}}[\log h_0(X)],
\end{align}
so the short form $H=\psi-\theta\cdot\eta$ is the $h_0=1$ special case (Bernoulli, categorical, Jaynes' die), not a licence to drop $1/k!$ from a Poisson. Equivalently, when $h_0=1$, $H=-\psi^*(\boldsymbol{\eta})$ where $\psi^*$ is the Legendre conjugate of $\psi$. That is the form that makes the next differentiation step cheap.}

\newslide{Fisher from the Same $\log p$}

\slides{Differentiate once; take a second moment.}

\slidesincremental{
* Score: $\nabla_{\boldsymbol{\theta}}\log p = T-\boldsymbol{\eta}$
* $\mathbb{E}[\mathrm{score}]=0$; $G=\mathbb{E}[\mathrm{score}\,\mathrm{score}^\top]=\mathrm{Cov}[T]$
* But $\boldsymbol{\eta}=\nabla\psi$, so $G=\nabla^2\psi$
}

\speakernotes{LO8 punchline as a calculation, not a slogan. Score $=T-\eta$ is immediate from $\log p=\theta\cdot T-\psi$. Squaring and taking expectation is Fisher. Differentiating $\eta=\nabla\psi$ again is the Hessian. Same matrix three ways: Cov, Fisher, $\nabla^2\psi$.}

\notes{Differentiate $\log p=\boldsymbol{\theta}\cdot T-\psi$ under the expectation:
$$
\nabla_{\boldsymbol{\theta}}\log p(x\mid\boldsymbol{\theta})=T(x)-\nabla\psi(\boldsymbol{\theta})=T(x)-\boldsymbol{\eta}.
$$
The score has mean zero. Fisher's information matrix is the second moment of the score,
$$
G_{ij}(\boldsymbol{\theta})=\mathbb{E}_{\boldsymbol{\theta}}[\partial_i\log p\,\partial_j\log p]=\mathrm{Cov}_{\boldsymbol{\theta}}[T]_{ij}.
$$
Differentiating $\boldsymbol{\eta}=\nabla\psi$ once more yields the same matrix as a Hessian: $G=\nabla^2\psi$. So the cumulant-generating property *is* the Fisher metric on an exponential family --- which follows from the entropy calculation.}

\endif
