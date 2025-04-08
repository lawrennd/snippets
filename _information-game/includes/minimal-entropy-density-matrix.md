\ifndef{minimalEntropyDensityMatrix}
\define{minimalEntropyDensityMatrix}

\editme

\subsection{Variational Derivation of the Initial Curvature Structure}

We will determine constraints on the Fisher Information Matrix $G(\boldsymbol{\theta})$ that are consistent with the system’s unfolding rules and internal information geometry. We follow Jaynes [@Jaynes-] in solving a variational problem that captures the allowed structure of the system’s origin (minimal entropy) state.

This document walks through the derivation of the minimal entropy configuration using Jaynes's free-form variational principle. We aim to derive the form of the density matrix or distribution directly from information-theoretic constraints. The goal is also to make the process accessible to those unfamiliar with Jaynes’s original maximum entropy formalism.

A density matrix has the form
$$
\rho(\boldsymbol{\theta}) = \frac{1}{Z(\boldsymbol{\theta})} \exp\left( \sum_i \theta_i H_i \right)
$$
where $Z(\boldsymbol{\theta}) = \mathrm{tr}\left[\exp\left( \sum_i \theta_i H_i \right)\right]$ and $\boldsymbol{\theta} \in \mathbb{R}^d$, $H_i$ are Hermitian observables. 

\subsection{Jaynesian Derivation of Minimal Entropy Configuration}

Jaynes proposed that statistical mechanics problems should be treated as problems of inference. One assigns a probability distribution (or density matrix in the quantum case) that is maximally noncommittal with respect to missing information, subject to known constraints.

While Jaynes applied this idea to derive the *maximum entropy* configuration given constraints, here we adapt it to derive the *minimum entropy* configuration, under an assumption of zero initial entropy bounded by a maximum entropy of $N$ bits.


Let $\rho$ be a density matrix describing the state of a system. The von Neumann entropy is,
$$
S[\rho] = -\mathrm{tr}(\rho \log \rho),
$$
we wish to *minimize* $S[\rho]$, subject to constraints that encode the resolution bounds.

In the game we assume that the system begins in a state of minimal entropy, the state cannot be a delta function (no singularities, so it must obey a resolution constraint $\varepsilon$) and the entropy is bounded above by $N$ bits: $S[\rho] \leq N$.

We apply a variational principle where we minimise
$$
S[\rho] = -\mathrm{tr}(\rho \log \rho)
$$
subject to normalization, $\mathrm{tr}(\rho) = 1$, a resolution constraint, $\mathrm{tr}(\rho \hat{X}^2) \geq \epsilon^2$ and/or $\mathrm{tr}(\rho \hat{P}^2) \geq \delta^2$, and other optional moment or dual-space constraints

We introduce Lagrange multipliers $\lambda_0$, $\lambda_x$, $\lambda_p$ for these constraints and define the Lagrangian
$$
\mathcal{L}[\rho] = -\mathrm{tr}(\rho \log \rho)
+ \lambda_0 (\mathrm{tr}(\rho) - 1)
- \lambda_x (\mathrm{tr}(\rho \hat{X}^2) - \epsilon^2)
- \lambda_p (\mathrm{tr}(\rho \hat{P}^2) - \delta^2).
$$

To find the extremum, we take the functional derivative and set it to zero,
$$
\frac{\delta \mathcal{L}}{\delta \rho} = -\log \rho - 1 - \lambda_x \hat{X}^2 - \lambda_p \hat{P}^2 + \lambda_0 = 0
$$
and solving for $\rho$ gives
$$
\rho = \frac{1}{Z} \exp\left(-\lambda_x \hat{X}^2 - \lambda_p \hat{P}^2\right)
$$
where the partition function (which ensures normalisation) is
$$
Z = \mathrm{tr}\left[\exp\left(-\lambda_x \hat{X}^2 - \lambda_p \hat{P}^2\right)\right]
$$
This is the quantum analogue of a *Gaussian distribution*, which is consistent with the minimum entropy distribution under uncertainty constraints.

The Lagrange multipliers $\lambda_x, \lambda_p$ enforce lower bounds on variance. These define the natural parameters as $\theta_x = -\lambda_x$ and $\theta_p = -\lambda_p$ in the exponential family form $\rho(\boldsymbol{\theta}) \propto \exp(\boldsymbol{\theta} \cdot \mathbf{H})$. The form of $\rho$ is a density matrix. The curvature (second derivative) of $\log Z$ gives the Fisher Information matrix $G$. Steepest ascent trajectories in $\boldsymbol{\theta}$ space will trace the system's entropy dynamics.

For next steps we need to compute $G$ from $\log Z$ to explore the information geometry. From this we should verify that the following conditions hold,
$$
\left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \right| < \varepsilon \quad \text{for all } i
$$
which implies that all variables remain latent at initialization.

The Hermitians have a *non-commuting observable pair* constraint,
$$
  [H_i, H_j] \neq 0,
$$
which is equivalent to an *uncertainty relation*,
$$
  \mathrm{Var}(H_i) \cdot \mathrm{Var}(H_j) \geq C > 0,
$$
and ensures that we have *bounded curvature*
$$
\mathrm{tr}(G(\boldsymbol{\theta})) \geq \gamma > 0.
$$

We can then use $\varepsilon$ and $N$ to define initial thresholds and maximum resolution and examine how variables decouple and how saddle-like regions emerge as the landscape unfolds through gradient ascent.

This constrained minimization problem yields the *structure of the initial density matrix* $\rho(\boldsymbol{\theta}_0)$ and the *permissible curvature geometry* $G(\boldsymbol{\theta}_0)$ and a constraint-consistent basis of observables $\{H_i\}$ that have a quadratic form. This ensures the system begins in a *regular, latent, low-entropy state*.

This serves as the foundational configuration from which entropy ascent and symmetry-breaking transitions emerge.

\endif
