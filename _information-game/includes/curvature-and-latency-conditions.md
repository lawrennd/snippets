\ifndef{curvatureAndLatencyConditions}
\define{curvatureAndLatencyConditions}

\editme

\subsection{Curvature and Latency Conditions}

\notes{The Fisher Information Matrix $G(\boldsymbol{\theta})$ describes the local curvature of the log-partition function $\log Z(\boldsymbol{\theta})$ and thus characterises how sharply peaked the distribution $\rho(\boldsymbol{\theta})$ is in different directions. Higher curvature reflects greater sensitivity to changes in the parameters — more 'informative' directions in the landscape.}

\notes{At the system's origin, all degrees of freedom are latent — no variable has yet emerged. This means that the projection of curvature along the direction of each parameter must be small. We express this as a constraint on the vector $G(\boldsymbol{\theta}) \boldsymbol{\theta}$, requiring
$$
\left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \right| < \varepsilon \quad \text{for all } i.
$$
This condition is derived from the resolution-constrained entropy formulation, where $\varepsilon$ is the resolution threshold that determines when a parameter component becomes dynamically active. It ensures that the entropy gradient, proportional to $G(\boldsymbol{\theta}) \boldsymbol{\theta}$, remains too shallow to trigger emergence in any direction — preserving the latent symmetry of the system at $\boldsymbol{\theta}_0$.}

\notes{This condition also has a geometric interpretation, $\boldsymbol{\theta}_0$ must lie near a saddle point or a flat region of the entropy landscape. The curvature is non-zero and globally bounded (from the uncertainty constraint), but its projection is uniformly suppressed across all directions.}

\subsection{Initial Constraints and the Permissible Unfolding Domain}

\notes{We now summarise the constraints that define the initial domain from which the system unfolds. These constraints ensure the system begins in a regular, latent, low-entropy state, while preserving the potential for future variable emergence.}

\notes{We imposed a constraint on the maximum entropy and now we also consider the directional latency.

1. *Entropy bound*:
   $$
   S[\rho(\boldsymbol{\theta})] \leq N,
   $$
   where $N$ specifies the total informational capacity of the system. At the origin $\boldsymbol{\theta}_o$, the entropy is minimal — but the system must remain within this global entropy budget throughout its evolution.

2. *Directional latency*:
   $$
   \left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta} \right]_i \right| < \varepsilon \quad \text{for all } i.
   $$
   This enforces the condition that no direction in parameter space dominates initially, preserving symmetry and avoiding premature emergence. This constraint is a consequence of the resolution-constrained entropy formulation, where $\varepsilon$ represents the minimum resolvable gradient magnitude.

These two constraints together define a *feasible region* in parameter space: a domain $\mathcal{D}_o \subset \mathbb{R}^d$ where entropy remains low and gradients are uniformly shallow. In thermodynamics the entropy would be referred to as subextensive, i.e. it remains below capacity and does not yet scale with effective dimensionality.}

\notes{We interpret this region as a *latent pregeometry*: a structure defined not by explicit variables, but by information-theoretic curvature and bounded resolution. Emergence proceeds only when a trajectory moves outside this domain, at which point curvature accumulates along a dominant direction and a variable 'activates'.}

\notes{The game therefore begins in $\mathcal{D}_o$, where entropy gradients are present but too shallow to drive evolution. The unfolding process is triggered by internal perturbations or transitions that move the system into a steeper region of the entropy landscape — breaking the initial symmetry and initiating variable formation.}

\subsection{Gradient Ascent and the Initiation of Emergence}

\notes{Once the system leaves the latent domain \(\mathcal{D}_o\), it enters a region where curvature gradients become directionally amplified. In this region, the entropy gradient,
$$
\nabla S[\rho(\boldsymbol{\theta})] = - \boldsymbol{\theta}^\top G(\boldsymbol{\theta}),
$$
becomes sufficiently steep in one or more directions to drive dynamical activation. This transition marks the onset of emergence.}

\notes{The dynamics can be understood as entropic gradient ascent in the space of natural parameters $\boldsymbol{\theta}$, where the flow is governed by the information geometry encoded in the Fisher Information Matrix. At each point, the steepest ascent direction is given by
$$
\dot{\boldsymbol{\theta}}_i = 
\begin{cases}
-[G(\boldsymbol{\theta})\boldsymbol{\theta}]_i & \text{if } |[G(\boldsymbol{\theta})\boldsymbol{\theta}]_i| \geq \varepsilon \\
0 & \text{otherwise}
\end{cases}
$$
This formulation explicitly shows that emergence is fundamentally tied to crossing the resolution threshold $\varepsilon$, not just to the absolute steepness of gradients. Components with gradient magnitudes below $\varepsilon$ remain fixed, creating a discrete, quantized evolution process.}

\notes{This process — emergence through spontaneous asymmetry in the curvature — does not require an external observer or measurement collapse. Instead, it is an internal dynamical effect of the geometry itself. A direction in $\boldsymbol{\theta}$-space becomes statistically distinguishable from the others: it carries more information and thus breaks the latent symmetry.}

\notes{To characterise this transition more precisely, we track the growth of the entropy gradient component-wise
$$
\left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \geq \varepsilon_{\text{activate}}.
$$
at which point the $i$-th degree of freedom becomes resolvable. This threshold crossing defines a *variable activation event*.}

\notes{We can now begin to think of the system as flowing through a dynamically unfolding geometry: curvature concentrates, variables activate, and a new basis of observables $\{H_i'\}$ emerges adaptively. These are not fixed beforehand, but arise from the internal information dynamics.}

\endif
