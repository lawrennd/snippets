\ifndef{latentPhaseConstraints}
\define{latentPhaseConstraints}

\subsection{Initial Constraints and the Permissible Unfolding Domain}

\notes{We now summarise the constraints that define the initial domain from which the system unfolds. These constraints ensure the system begins in a regular, latent, low-entropy state, while preserving the potential for future variable emergence.}

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

\endif 