\ifndef{gaussianAsExponentialFamily}
\define{gaussianAsExponentialFamily}
\editme

\subsection{Gaussian as Exponential Family}

\newslide{Gaussian: Natural Parameters and $\psi$}

\slides{
$$
p(y\mid\boldsymbol{\theta})=\exp\bigl(\theta_1 y+\theta_2 y^2-\psi(\boldsymbol{\theta})\bigr)
$$
* $\theta_1=\dfrac{\mu}{\sigma^2}$,\quad $\theta_2=-\dfrac{1}{2\sigma^2}$,\quad $T(y)=(y,y^2)$
* $\psi(\theta_1,\theta_2)=-\dfrac{\theta_1^2}{4\theta_2}-\dfrac12\log(-2\theta_2)-\dfrac12\log(2\pi)$
}

\notes{The univariate Gaussian $\mathcal{N}(\mu,\sigma^2)$ is MaxEnt under fixed mean and variance, so it belongs to a two-parameter exponential family. Expanding the quadratic energy gives natural parameters
$$
\theta_1=\frac{\mu}{\sigma^2},\qquad \theta_2=-\frac{1}{2\sigma^2},
$$
sufficient statistics $T(y)=(y,y^2)$, and cumulant generating function
$$
\psi(\theta_1,\theta_2)=-\frac{\theta_1^2}{4\theta_2}-\frac12\log(-2\theta_2)-\frac12\log(2\pi).
$$
(The base measure is Lebesgue; the $(2\pi)$ factor sits in $\psi$.) Differentiating recovers the moments: $\nabla\psi=(\mu,\mu^2+\sigma^2)$. With *known* variance the family collapses to one parameter, $\theta=\mu/\sigma^2$, $T(y)=y$, and $\psi(\theta)=\tfrac12\sigma^2\theta^2$ (up to an additive constant independent of $\theta$). The multivariate case replaces $\theta_1$ by $\Sigma^{-1}\boldsymbol{\mu}$ and $\theta_2$ by $-\tfrac12\Sigma^{-1}$ acting on $yy^\top$.}

\speakernotes{Two numbers on the slide: precision-weighted mean and minus half precision. $\psi$ is the ugly formula; board only $\eta=\nabla\psi$ if asked.}

\endif
