\ifndef{differentialEntropyChangeOfVariables}
\define{differentialEntropyChangeOfVariables}

\editme

\subsection{How Differential Entropy Transforms}

\slides{Continuous entropy is not invariant under reparametrisation.}

\notes{Define differential entropy $h(X)=-\int f_X(x)\ln f_X(x)\,dx$. For a smooth invertible map $y=g(x)$, probability conservation requires $f_Y(y)\,|dy|=f_X(x)\,|dx|$, so
\begin{align}
f_Y(y)=\frac{f_X(x)}{|g'(x)|}.
\end{align}
Substitute into $h(Y)$ and change the integration variable back to $x$:
\begin{align}
h(Y)
  &= -\int f_Y(y)\ln f_Y(y)\,dy
   = -\int f_X(x)\ln\frac{f_X(x)}{|g'(x)|}\,dx
   = h(X)+\mathbb{E}\bigl[\ln|g'(X)|\bigr].
\end{align}
The shift is the average log-Jacobian.}

\slidesmall{
$$
h(Y)=h(X)+\mathbb{E}\bigl[\ln|g'(X)|\bigr]
$$
}

\slidesincremental{
* Linear rescaling: $h(aX)=h(X)+\ln|a|$
* Changing units (m/s $\to$ km/s) changes $h$
* $h$ can be negative (narrow Gaussian) — not Shannon uncertainty
}

\speakernotes{Board the one-line derivation. Emphasise: $\ln f$ takes the log of a density with units, so something is missing. Week 5: MaxEnt ``Gaussian maximises entropy for fixed variance'' is relative to the chosen coordinate.}

\notes{For a linear map $y=ax+b$ with $a\neq 0$, the formula collapses to $h(aX)=h(X)+\ln|a|$. Because a density $f$ has units of inverse length (or inverse speed), $\ln f$ is the log of a dimensionful quantity. That is a symptom that differential entropy secretly depends on a reference scale. Even the claim that a Gaussian maximises entropy at fixed variance is relative to the variable you chose: fixing $\mathrm{Var}(v_x)$ and fixing $\mathrm{Var}(v_x^3)$ yield different maximisers.}

\newslide{Maxwell Speed Versus Component}

\slides{The two Maxwell--Boltzmann entropies differ by the log-Jacobian of the speed map.}

\slidesmall{
$$
h(v_x)=\tfrac12\ln(2\pi e\sigma^2),
\qquad
h(s)=\ln(\sigma\sqrt{2\pi})+\gamma-\tfrac12
$$
}

\slidesincremental{
* $\sigma=1$: $h(v_x)\approx 1.419$, $h(s)\approx 0.996$ nats
* Different random variables, each against Lebesgue in its own coordinate
* $h(\mathbf{v})-h(s)=\mathbb{E}[\ln(4\pi s^2)]$ --- log of the shell volume
}

\notes{With scale $\sigma=\sqrt{kT/m}$, a single Gaussian component has $h(v_x)=\tfrac12\ln(2\pi e\sigma^2)=\ln(\sigma\sqrt{2\pi})+\tfrac12$. The Maxwell speed law has
\begin{align}
h(s)=\ln(\sigma\sqrt{2\pi})+\gamma-\tfrac12,
\end{align}
where $\gamma$ is Euler's constant. For $\sigma=1$ these are approximately $1.419$ and $0.996$ nats. Neither number is ``the'' entropy of the gas; each is entropy of a different random variable against Lebesgue measure in its own coordinate.

The three-dimensional Cartesian density and the speed density are related by the shell volume $f_s(s)\,{\mathrm{d}}s = f(\mathbf{v})\,{\mathrm{d}}^3v$ with ${\mathrm{d}}^3v = 4\pi s^2\,{\mathrm{d}}s$. Taking logarithms and expectations gives
\begin{align}
h(\mathbf{v})-h(s)=\mathbb{E}\bigl[\ln(4\pi s^2)\bigr].
\end{align}
That expectation is the log-Jacobian (the Radon--Nikodym factor) of the speed map after the angles have been integrated. The discrete analogue is the average log-ratio of bin widths for a 1--1 reparametrisation; grouping Cartesian cubes into shells is a separate, entropy-decreasing move.}

\endif
