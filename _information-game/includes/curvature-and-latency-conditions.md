\ifndef{curvatureAndLatencyConditions}
\define{curvatureAndLatencyConditions}

\editme

\subsection{Curvature and Latency Conditions}

\notes{The Fisher Information Matrix $G(\boldsymbol{\theta})$ describes the local curvature of the log-partition function $\log Z(\boldsymbol{\theta})$ and thus characterises how sharply peaked the distribution $\rho(\boldsymbol{\theta})$ is in different directions. Higher curvature reflects greater sensitivity to changes in the parameters — more 'informative' directions in the landscape.}

At the system's origin, all degrees of freedom are latent — no variable has yet emerged. This means that the projection of curvature along the direction of each parameter must be small. We express this as a constraint on the vector $G(\boldsymbol{\theta}) \boldsymbol{\theta}$, requiring
$$
\left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \right| < \varepsilon \quad \text{for all } i.
$$
This ensures that the entropy gradient, proportional to $G(\boldsymbol{\theta}) \boldsymbol{\theta}$, remains too shallow to trigger emergence in any direction — preserving the latent symmetry of the system at $\boldsymbol{\theta}_0$.
This condition also has a geometric interpretation, $\boldsymbol{\theta}_0$ must lie near a saddle point or a flat region of the entropy landscape. The curvature is non-zero and globally bounded (from the uncertainty constraint), but its projection is uniformly suppressed across all directions.

\subsection{Initial Constraints and the Permissible Unfolding Domain}

We now summarise the constraints that define the initial domain from which the system unfolds. These constraints ensure the system begins in a regular, latent, low-entropy state, while preserving the potential for future variable emergence.

We impose two key global conditions:

1. *Entropy bound*:
   $$
   S[\rho(\boldsymbol{\theta})] \leq N,
   $$
   where $N$ specifies the total informational capacity of the system. At the origin $\boldsymbol{\theta}_0$, the entropy is minimal — but the system must remain within this global entropy budget throughout its evolution.

2. *Directional latency*:
   $$
   \left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta} \right]_i \right| < \varepsilon \quad \text{for all } i.
   $$
   This enforces the condition that no direction in parameter space dominates initially, preserving symmetry and avoiding premature emergence.

These two constraints together define a *feasible region* in parameter space: a domain $\mathcal{D}_0 \subset \mathbb{R}^d$ where entropy remains low and gradients are uniformly shallow. In thermodynamics the entropy would be referred to as subextensive, i.e. it remains below capacity and does not yet scale with effective dimensionality.

We interpret this region as a *latent pregeometry*: a structure defined not by explicit variables, but by information-theoretic curvature and bounded resolution. Emergence proceeds only when a trajectory moves outside this domain, at which point curvature accumulates along a dominant direction and a variable 'activates'.

The game therefore begins in $\mathcal{D}_0$, where entropy gradients are present but too shallow to drive evolution. The unfolding process is triggered by internal perturbations or transitions that move the system into a steeper region of the entropy landscape — breaking the initial symmetry and initiating variable formation.

\subsection{Gradient Ascent and the Initiation of Emergence}

Once the system leaves the latent domain \(\mathcal{D}_0\), it enters a region where curvature gradients become directionally amplified. In this region, the entropy gradient,
$$
\nabla S[\rho(\boldsymbol{\theta})] = G(\boldsymbol{\theta}) \boldsymbol{\theta},
$$
becomes sufficiently steep in one or more directions to drive dynamical activation. This transition marks the onset of emergence.

The dynamics can be understood as entropic gradient ascent in the space of natural parameters $\boldsymbol{\theta}$, where the flow is governed by the information geometry encoded in the Fisher Information Matrix. At each point, the steepest ascent direction is given by
$$
\frac{\text{d}\boldsymbol{\theta}}{\text{d}t} \propto \nabla S[\rho] = G(\boldsymbol{\theta}) \boldsymbol{\theta}.
$$

This defines a deterministic flow field over parameter space. In regions of uniform curvature, the system evolves slowly and symmetrically. The system's ability to resolve a specific direction corresponds to a rise in distinguishability, reflected in the local curvature profile. When one direction becomes locally dominant (i.e. the eigenvalues of $G(\boldsymbol{\theta})$ become asymmetric), the flow breaks symmetry and accelerates along that axis (i.e. a specific direction in $\boldsymbol{\theta}$-space becomes energetically or informationally preferred). A variable emerges.

This process — emergence through spontaneous asymmetry in the curvature — does not require an external observer or measurement collapse. Instead, it is an internal dynamical effect of the geometry itself. A direction in $\boldsymbol{\theta}$-space becomes statistically distinguishable from the others: it carries more information and thus breaks the latent symmetry.

To characterise this transition more precisely, we track the growth of the entropy gradient component-wise
$$
\left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \geq \varepsilon_{\text{activate}}.
$$
at which point the $i$-th degree of freedom becomes resolvable. This threshold crossing defines a *variable activation event*.

We can now begin to think of the system as flowing through a dynamically unfolding geometry: curvature concentrates, variables activate, and a new basis of observables $\{H_i'\}$ emerges adaptively. These are not fixed beforehand, but arise from the internal information dynamics.

\endif
