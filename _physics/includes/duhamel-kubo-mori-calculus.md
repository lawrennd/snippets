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

\subsubsection{The Duhamel formula (Fréchet derivative of the matrix exponential)}

\notes{Let $K(\theta)$ be a matrix depending smoothly on parameters $\theta$, and let $F_i=\partial K/\partial \theta_i$.

In general, $F_i e^{K} \neq e^{K}F_i$, so we use the Duhamel formula (also called the Fréchet derivative of the matrix exponential):
$$
\frac{\partial}{\partial \theta_i} e^{K(\theta)}
= \int_0^1 e^{(1-s)K(\theta)}\, F_i\, e^{sK(\theta)}\,\text{d}s.
$$

You can read the parameter $s\in[0,1]$ as "how far through the exponential you insert the derivative". It is an \emph{ordering} device, not a time variable.

In the matrix functions literature this is written as the Fréchet derivative $L_{\exp}(K, F_i)$, meaning the directional derivative of $\exp$ at $K$ in direction $F_i$. The integral representation follows from solving the variation-of-constants ODE for $\frac{d}{ds}(e^{-sK} e^{(K+\epsilon F)s})$ and integrating from 0 to 1—the real connection to Duhamel's classical principle for inhomogeneous ODEs.}

\slides{
**Duhamel formula (Fréchet derivative):**

$$
\partial_i e^{K}
=\int_0^1 e^{(1-s)K}F_i e^{sK}\,\mathrm{d}s
$$

Also written: $L_{\exp}(K,F_i)$ (directional derivative)
}

\subsubsection{How to compute the Fréchet derivative efficiently}

\notes{The integral $\int_0^1 e^{(1-s)K}F\,e^{sK}\,\text{d}s$ is not evaluated by numerical quadrature in practice. For small-to-medium matrices, there is a beautiful block-matrix trick:

$$
L_{\exp}(K,F) = \exp\begin{pmatrix}K & F \\ 0 & K\end{pmatrix}_{(1,2)}
$$

where the subscript $(1,2)$ denotes the upper-right $n\times n$ block of the $2n\times 2n$ exponential. This reduces the Fréchet derivative to a single matrix exponential of twice the size.

For ML practitioners: this means automatic differentiation through `expm` (matrix exponential) can be implemented efficiently using standard algorithms (Padé approximation after scaling-and-squaring). Modern frameworks like JAX and PyTorch use variants of this approach.

**Numerical note:** The exponential map can be ill-conditioned when $K$ has widely separated eigenvalues or large imaginary parts (common for Hamiltonians $K=-iHt$). The BKM metric inherits this conditioning—relevant for quantum natural gradient optimization.}

\slides{
**Computational trick:**

$$L_{\exp}(K,F)=\exp\begin{pmatrix}K&F\\0&K\end{pmatrix}_{(1,2)}$$

One $2n\times 2n$ matrix exponential!

**For ML:** autodiff through `expm` uses this trick
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
In the quantum literature this is the Bogoliubov--Kubo--Mori (BKM) metric. Explicitly, it has the integral representation:
$$
G_{ij}=\int_0^1 \text{tr}\big(\rho^{1-s}(F_i-\langle F_i\rangle)\rho^s(F_j-\langle F_j\rangle)\big)\,\text{d}s,
$$
where $\rho=e^K/\text{tr}(e^K)$ and $\langle F_i\rangle=\text{tr}(\rho F_i)$. This is the Kubo--Mori inner product on the tangent space. The $s$-integral performs a specific symmetrisation that handles noncommutativity.

**Key observation:** In the commutative case, $\rho^{1-s}F\rho^s=F\rho$ for all $s$, so the integral collapses to $\text{tr}(\rho F_iF_j)-\text{tr}(\rho F_i)\text{tr}(\rho F_j)=\text{Cov}(F_i,F_j)$. The classical Fisher metric is recovered. The $s$-integral is precisely the minimal extension needed for noncommutativity.

For us, the useful message is simple:

- $\psi$ is still a scalar function of real parameters,
- so its Hessian is a symmetric positive matrix,
- it governs local linear response / geometry just like classical Fisher information,
- and the BKM form is one of many possible quantum Fisher metrics (the monotone metrics classified by Petz)—it's the canonical one from exponential families and thermodynamic linear response.}

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
