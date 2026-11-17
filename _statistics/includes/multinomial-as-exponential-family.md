\ifndef{multinomialAsExponentialFamily}
\define{multinomialAsExponentialFamily}
\editme

\subsection{Multinomial as Exponential Family}

\newslide{Multinomial / Categorical: Natural Parameters and $\psi$}

\slides{
$$
P(\mathbf{x}\mid\boldsymbol{\theta})=\exp\bigl(\boldsymbol{\theta}\!\cdot\! T(\mathbf{x})-\psi(\boldsymbol{\theta})\bigr)\,h_0(\mathbf{x})
$$
* $\theta_j=\log\dfrac{\pi_j}{\pi_K}$,\quad $T=(x_1,\ldots,x_{K-1})$
* $\psi(\boldsymbol{\theta})=n\log\bigl(1+\sum_{j=1}^{K-1}e^{\theta_j}\bigr)$
* Categorical: $n=1$, $h_0=1$; multinomial: $h_0=\dfrac{n!}{x_1!\cdots x_K!}$
}

\notes{A categorical distribution on $K$ exclusive labels is a multinomial with a single trial ($n=1$). Write the outcome as a one-hot vector $\mathbf{x}$ with $\sum_{j=1}^K x_j=1$. Because of the simplex constraint we use $K-1$ free natural parameters,
$$
\theta_j=\log\frac{\pi_j}{\pi_K},\qquad j=1,\ldots,K-1,
$$
with sufficient statistics $T(\mathbf{x})=(x_1,\ldots,x_{K-1})$ and cumulant generating function
$$
\psi(\boldsymbol{\theta})=\log\Bigl(1+\sum_{j=1}^{K-1}e^{\theta_j}\Bigr)
$$
(the log-sum-exp that recovers $\pi_K=1/\bigl(1+\sum_j e^{\theta_j}\bigr)$). For $n$ independent trials the counts $\mathbf{x}$ are multinomial: the same $\boldsymbol{\theta}$ and $T$, but
$$
\psi(\boldsymbol{\theta})=n\log\Bigl(1+\sum_{j=1}^{K-1}e^{\theta_j}\Bigr)
$$
and base measure $h_0(\mathbf{x})=n!/(x_1!\cdots x_K!)$. Softmax regression is this family with features in place of the raw one-hot.}

\speakernotes{Same two-point moral: categorical $h_0=1$ is counting on the labels; multinomial multiplicity is density of states again. Categorical is $n=1$. Same log-sum-exp $\psi$ as softmax. Do not open the unconstrained $K$-parameter chart live.}

\endif
