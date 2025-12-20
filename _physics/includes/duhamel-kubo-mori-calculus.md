\ifndef{duhamelKuboMoriCalculus}
\define{duhamelKuboMoriCalculus}

\editme

\subsection{Computation Layer: Duhamel / Kubo--Mori Calculus}

\notes{Once we switch to the quantum (noncommutative) setting, we still want to do the same kinds of calculations as in the classical exponential family:

- differentiate the log-partition function,
- compute Fisher-like metrics,
- linearise dynamics,
- and (ultimately) simulate trajectories.

Noncommutativity introduces one new technical obstacle: matrices do not commute, so differentiating an operator exponential is not the same as “pulling down the derivative” as in the scalar case.

The Duhamel/Kubo--Mori formulas are the standard way to do these derivatives cleanly. The key pedagogical point is: this is \emph{computation}, not additional structure. The structure came from invariance (what reversible maps must look like); Duhamel calculus is how we actually compute within that structure.}

\slides{
**Computation layer:** how to differentiate $e^{K(\theta)}$

Noncommuting matrices $\Rightarrow$ Duhamel integral
}

\subsubsection{The Duhamel formula (derivative of a matrix exponential)}

\notes{Let $K(\theta)$ be a matrix depending smoothly on parameters $\theta$, and let $F_i=\partial K/\partial \theta_i$.

In general, $F_i e^{K} \neq e^{K}F_i$, so we use the Duhamel formula:
$$
\frac{\partial}{\partial \theta_i} e^{K(\theta)}
= \int_0^1 e^{(1-s)K(\theta)}\, F_i\, e^{sK(\theta)}\,\text{d}s.
$$

You can read the parameter $s\in[0,1]$ as “how far through the exponential you insert the derivative”. It is an \emph{ordering} device, not a time variable.}

\slides{
**Duhamel formula:**

$$
\partial_i e^{K}
=\int_0^1 e^{(1-s)K}F_i e^{sK}\,\mathrm{d}s
$$
}

\subsubsection{Kubo--Mori derivatives and the BKM metric (quantum Fisher information)}

\notes{In an exponential-family chart, we write
$$
\rho(\theta)=\exp\!\big(K(\theta)-\psi(\theta)\big),
\qquad \psi(\theta)=\log\text{tr}\,e^{K(\theta)}.
$$

The same object that plays the role of Fisher information in the classical case appears as the Hessian of $\psi$:
$$
G_{ij}(\theta)=\frac{\partial^2 \psi}{\partial \theta_i\partial \theta_j}.
$$
In the quantum literature this is (one form of) the Bogoliubov--Kubo--Mori (BKM) metric; it can be expressed in several equivalent ways involving operator orderings.

For us, the useful message is simple:

- $\psi$ is still a scalar function of real parameters,
- so its Hessian is a symmetric positive matrix,
- and it governs local linear response / geometry just like classical Fisher information.}

\subsubsection{Why Lie closure makes things tractable}

\notes{The Duhamel integrals look scary until you pick a basis adapted to the problem.

If your operators $\{F_a\}$ close under commutation (a Lie algebra),
$$
[F_a,F_b]= i\sum_c f_{abc}F_c,
$$
then conjugating by $e^{sK}$ stays inside the same finite-dimensional span:
$$
e^{sK}F_a e^{-sK}\in \text{span}\{F_b\}.
$$
So the Duhamel integrals can be reduced to finite-dimensional linear algebra on coefficients (often via BCH identities).

Again: the "Lie closure" choice is an implementation trick for computation, not a new physical axiom.}

\slides{
**Lie closure helps compute:**

- $e^{sK}F_a e^{-sK}$ stays in span$(F)$
- Duhamel integrals reduce to linear algebra
}

\subsubsection{A common confusion: the Duhamel parameter is not time}

\notes{Quantum statistical mechanics often uses an “imaginary time” parameter in KMS formulas. It is easy to confuse:

- the real-time parameter that labels reversible evolution,
- the entropy-time parameter used for steepest ascent,
- and the ordering parameters (like $s\in[0,1]$) that appear in Duhamel/Kubo--Mori representations.

In this course, we treat $s$ as a purely computational ordering parameter. It is not a dynamical clock.}

\endif

