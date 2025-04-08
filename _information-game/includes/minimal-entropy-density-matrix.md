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

Jaynes proposed that statistical mechanics problems should be treated as problems of inference. One assigns a probability distribution (or density matrix) that is maximally noncommittal with respect to missing information, subject to known constraints.

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
This is formally analogous to a Gaussian state for a density matrix, which is consistent with the minimum entropy distribution under uncertainty constraints.

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

\subsection{Fisher Information Matrix}

We’ll now derive the form of the Fisher Information Matrix $G(\boldsymbol{\theta})$ from the partition function:
$$
Z(\boldsymbol{\theta}) = \mathrm{tr}\left[\exp\left(\sum_i \theta_i H_i \right)\right]
$$
We'll proceed by differentiating with respect to $\theta_i$ for the expectation values, then compute the second derivative to get the Fisher Information Matrix, 
$$
G_{ij} = \partial^2 \log Z / \partial \theta_i \partial \theta_j.
$$
which we'll then link to the  curvature.

First we differentiate $\log Z(\boldsymbol{\theta})$ with respect to $\theta_i$,
$$
Z(\boldsymbol{\theta}) = \mathrm{tr}\left[ e^{\sum_j \theta_j H_j} \right]
$$
Taking the derivative of $\log Z$ with respect to $\theta_i$, we apply the chain rule to the definition of $\log Z$,
$$
\frac{\partial \log Z}{\partial \theta_i} = \frac{1}{Z} \frac{\partial Z}{\partial \theta_i}
= \frac{1}{Z} \mathrm{tr}\left[ H_i \, e^{\sum_j \theta_j H_j} \right]
$$
So we have
$$
\frac{\partial \log Z}{\partial \theta_i} = \mathrm{tr}(\rho H_i) = \langle H_i \rangle
$$
This is the expected value of $H_i$ under the current distribution $\rho(\boldsymbol{\theta})$. 

We now compute the second derivative of $\log Z(\boldsymbol{\theta})$ to obtain the Fisher Information Matrix elements $G_{ij}$, using the definition
$$
G_{ij} = \frac{\partial^2 \log Z}{\partial \theta_i \partial \theta_j}
$$
by differentiating the  expression
$$
\frac{\partial \log Z}{\partial \theta_i} = \mathrm{tr}(\rho H_i),
$$
through another application of the product and chain rules. The second derivative then is
$$
\frac{\partial^2 \log Z}{\partial \theta_i \partial \theta_j}
= \frac{\partial}{\partial \theta_j} \mathrm{tr}(\rho H_i)
= \mathrm{tr}\left( \frac{\partial \rho}{\partial \theta_j} H_i \right)
$$
We can compute $\frac{\partial \rho}{\partial \theta_j}$ since
$\rho = \frac{1}{Z} e^{\sum_k \theta_k H_k}$,
we can use the product rule
$$
\frac{\partial \rho}{\partial \theta_j}
= \frac{\partial}{\partial \theta_j} \left( \frac{1}{Z} e^{\sum_k \theta_k H_k} \right)
= -\frac{1}{Z^2} \frac{\partial Z}{\partial \theta_j} e^{\sum_k \theta_k H_k} \cdot \frac{1}{Z} \frac{\partial}{\partial \theta_j} \left( e^{\sum_k \theta_k H_k} \right)
$$
For the second term we use the operator identity for the exponential derivative,
$$
\frac{\partial \rho}{\partial \theta_j} = \rho \left( H_j - \langle H_j \rangle \right)
$$
giving 
$$
G_{ij} = \mathrm{tr} \left[ \rho (H_j - \langle H_j \rangle) H_i \right]
= \langle H_i H_j \rangle - \langle H_i \rangle \langle H_j \rangle
$$
or in other words the Fisher Information Matrix is the covariance matrix,
$$
G_{ij} = \mathrm{Cov}(H_i, H_j).
$$

This reflects a structural property of the model: the log-partition function $\log Z(\boldsymbol{\theta})$ acts as a cumulant generating function for the observables $H_i$. Its second derivatives yield the covariance matrix of the observables (i.e., the second cumulants correspond to variances and covariances).
This induces a natural Riemannian geometry on the parameter space. The Fisher Information Matrix $G(\boldsymbol{\theta})$ encodes local curvature and sensitivity to variations in the natural parameters $\boldsymbol{\theta}$.

\subsection{Curvature and Latency Conditions}

The Fisher Information Matrix $G(\boldsymbol{\theta})$ describes the local curvature of the log-partition function $\log Z(\boldsymbol{\theta})$ and thus characterises how sharply peaked the distribution $\rho(\boldsymbol{\theta})$ is in different directions. Higher curvature reflects greater sensitivity to changes in the parameters — more 'informative' directions in the landscape.

At the system’s origin, all degrees of freedom are latent — no variable has yet emerged. This means that the projection of curvature along the direction of each parameter must be small. We express this as a constraint on the vector $G(\boldsymbol{\theta}) \boldsymbol{\theta}$, requiring
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

\subsection{Variable Activation and Basis Update}

As the system ascends the entropy landscape, the curvature becomes increasingly asymmetric. When the entropy gradient along a particular direction surpasses a threshold, that direction becomes dynamically resolvable — a variable activates.

We define a variable activation event as the point where the $i$-th component of the entropy gradient reaches order unity,
$$
\left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]i \geq \varepsilon{\text{activate}}.
$$
Here $\varepsilon_{\text{activate}}$ defines a threshold above which the system can resolve variation in the $i$-th direction with sufficient information gain. This marks a transition from latent to emergent status.

When this happens, the corresponding parameter $\theta_i$ becomes an active degree of freedom, and the associated observable $H_i$ becomes internally resolvable. The system’s effective observable basis $\{H_i\}$ is updated — either by extension or rotation — to reflect the newly emergent structure.

This update is not arbitrary. The new basis must remain consistent with the information geometry — that is, the Fisher matrix $G(\boldsymbol{\theta})$ must remain positive definite and aligned with the updated entropy gradients. One may think of this as a local frame adaptation: the system reorganizes its observables to align with the current information flow.

This leads to a piecewise unfolding of structure. Within each phase, a subset of variables is active and governs dynamics, when a new variable activates, the dimensionality of the effective system increases, each activation increases entropy, reorganizes curvature, and shifts the system’s trajectory.

Over time, this defines a staged emergence process, in which new variables appear sequentially as the system climbs through successive regions of increasing entropy and asymmetry. The basis $\{H_i\}$ is thus not globally fixed, but emerges dynamically as a function of the internal information landscape.

\endif
