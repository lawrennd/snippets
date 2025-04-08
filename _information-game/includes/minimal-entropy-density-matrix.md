\ifndef{minimalEntropyDensityMatrix}
\define{minimalEntropyDensityMatrix}

\editme

\subsection{Variational Derivation of the Initial Curvature Structure}

We will determine constraints on the Fisher Information Matrix $G(\boldsymbol{\theta})$ that are consistent with the system’s unfolding rules and internal information geometry. We follow Jaynes [@Jaynes-] in solving a variational problem that captures the allowed structure of the system’s origin (minimal entropy) state.

The density matrix is
$$
\rho(\boldsymbol{\theta}) = \frac{1}{Z(\boldsymbol{\theta})} \exp\left( \sum_i \theta_i H_i \right)
$$
where $Z(\boldsymbol{\theta}) = \mathrm{tr}\left[\exp\left( \sum_i \theta_i H_i \right)\right]$ and $\boldsymbol{\theta} \in \mathbb{R}^d$, $H_i$ are Hermitian observables

Our objective is to minimse the von Neumann entropy
$$
S(\rho) = -\mathrm{tr}(\rho \log \rho)
$$
subject to the following constraints. First *normalisation and positivity*
\[
\mathrm{tr}(\rho) = 1, \quad \rho \succeq 0.
\]
Secondly an entropy capacity constraint, 
$$
S(\rho) \leq N
$$
which sets the system’s maximal information content.

That is associated with a resolution threshold,
$$
\left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \right| < \varepsilon \quad \text{for all } i
$$
which ensures that all variables remain latent at initialization.

To avoid delta-function like states we can impose one of, a *non-commuting observable pair* constraint,
$$
  [H_i, H_j] \neq 0,
$$
an *uncertainty relation*,
$$
  \mathrm{Var}(H_i) \cdot \mathrm{Var}(H_j) \geq C > 0,
$$
or 
*bounded curvature*
$$
\mathrm{tr}(G(\boldsymbol{\theta})) \geq \gamma > 0.
$$

Solving this constrained minimization problem yields the *structure of the initial density matrix* $\rho(\boldsymbol{\theta}_0)$, the *permissible curvature geometry* $G(\boldsymbol{\theta}_0)$, a constraint-consistent basis of observables $\{H_i\}$, and ensures the system begins in a *regular, latent, low-entropy state*.

This serves as the foundational configuration from which entropy ascent and symmetry-breaking transitions emerge.

\endif
