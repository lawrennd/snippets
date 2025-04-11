\ifndef{jaynesianDerivationMinimalEntropy}
\define{jaynesianDerivationMinimalEntropy}

\editme

\subsection{Jaynesian Derivation of Minimal Entropy Configuration}

\notes{Jaynes proposed that statistical mechanics problems should be treated as problems of inference. One assigns a probability distribution (or density matrix) that is maximally noncommittal with respect to missing information, subject to known constraints.}

\notes{While Jaynes applied this idea to derive the *maximum entropy* configuration given constraints, here we adapt it to derive the *minimum entropy* configuration, under an assumption of zero initial entropy bounded by a maximum entropy of $N$ bits.}

\notes{Let $\rho$ be a density matrix describing the state of a system. The von Neumann entropy is,
$$
S[\rho] = -\mathrm{tr}(\rho \log \rho),
$$
we wish to *minimize* $S[\rho]$, subject to constraints that encode the resolution bounds.}

\notes{In the game we assume that the system begins in a state of minimal entropy, the state cannot be a delta function (no singularities, so it must obey a resolution constraint $\varepsilon$) and the entropy is bounded above by $N$ bits: $S[\rho] \leq N$.}

\notes{We apply a variational principle where we minimise
$$
S[\rho] = -\mathrm{tr}(\rho \log \rho)
$$
subject to normalization, $\mathrm{tr}(\rho) = 1$, a resolution constraint, $\mathrm{tr}(\rho \hat{X}^2) \geq \epsilon^2$ and/or $\mathrm{tr}(\rho \hat{P}^2) \geq \delta^2$, and other optional moment or dual-space constraints}

\notes{We introduce Lagrange multipliers $\lambda_0$, $\lambda_x$, $\lambda_p$ for these constraints and define the Lagrangian
$$
\mathcal{L}[\rho] = -\mathrm{tr}(\rho \log \rho)
+ \lambda_0 (\mathrm{tr}(\rho) - 1)
- \lambda_x (\mathrm{tr}(\rho \hat{X}^2) - \epsilon^2)
- \lambda_p (\mathrm{tr}(\rho \hat{P}^2) - \delta^2).
$$}

\notes{To find the extremum, we take the functional derivative and set it to zero,
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
This is a Gaussian state for a density matrix, which is consistent with the minimum entropy distribution under uncertainty constraints.}

\notes{The Lagrange multipliers $\lambda_x, \lambda_p$ enforce lower bounds on variance. These define the natural parameters as $\theta_x = -\lambda_x$ and $\theta_p = -\lambda_p$ in the exponential family form $\rho(\boldsymbol{\theta}) \propto \exp(\boldsymbol{\theta} \cdot \mathbf{H})$. The form of $\rho$ is a density matrix. The curvature (second derivative) of $\log Z$ gives the Fisher Information matrix $G$. Steepest ascent trajectories in $\boldsymbol{\theta}$ space will trace the system's entropy dynamics.}

\notes{Next we compute $G$ from $\log Z$ to explore the information geometry. From this we should verify that the following conditions hold,
$$
\left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \right| < \varepsilon \quad \text{for all } i
$$
which implies that all variables remain latent at initialization.}

\notes{The Hermitians have a *non-commuting observable pair* constraint,
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
$$}

\notes{We can then use $\varepsilon$ and $N$ to define initial thresholds and maximum resolution and examine how variables decouple and how saddle-like regions emerge as the landscape unfolds through gradient ascent.}

\notes{This constrained minimization problem yields the *structure of the initial density matrix* $\rho(\boldsymbol{\theta}_0)$ and the *permissible curvature geometry* $G(\boldsymbol{\theta}_0)$ and a constraint-consistent basis of observables $\{H_i\}$ that have a quadratic form. This ensures the system begins in a *regular, latent, low-entropy state*.

\notes{This is the configuration from which entropy ascent and symmetry-breaking transitions emerge.}

\endif 
