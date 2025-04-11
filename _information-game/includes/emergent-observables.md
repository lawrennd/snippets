\ifndef{emergentObservables}
\define{emergentObservables}

\editme

\subsection{Constructing the Updated Basis: Emergent Observables}

When a new variable activates, the system must update its internal basis $\{H_i\}$ to reflect the newly emergent structure. This reflects a geometric transformation in the space of information-bearing observables.

Given an existing set of active observables $\{H_1, \dots, H_k\}$ and a newly activated direction $\theta_{k+1}$, we seek a corresponding observable $H_{k+1}$ such that it aligns with the updated gradient,
$$
\left.\nabla_{\boldsymbol{\theta}} S[\rho]\right|{\theta{k+1}} = G(\boldsymbol{\theta}) \boldsymbol{\theta} \propto H_{k+1},
$$
it preserves orthogonality (uncorrelatedness) under the current state,
$$
\mathrm{Cov}(H_{k+1}, H_j) = 0 \quad \text{for all } j \leq k,
$$
it is consistent with the curvature structure,
$$
H_{k+1} \in \operatorname{span}\left{ \frac{\partial \rho}{\partial \theta_i} \right} \quad \text{evaluated near } \boldsymbol{\theta}_0.
$$
This yields a Gram–Schmidt-like procedure within the information geometry: new directions are orthogonalised with respect to the current active basis, and constrained to lie in the space spanned by gradient responses.

We can make this more explicit by defining an update rule. Let
$$
\widetilde{H}{k+1} := \sum{i} c_i H_i + R,
$$
where $R$ is the residual direction from the entropy gradient,
$$
R := G(\boldsymbol{\theta}) \boldsymbol{\theta} - \sum_{i} c_i H_i,
$$
and the coefficients $c_i$ are chosen to minimise the norm of $R$ under the inner product
$$
\langle A, B \rangle := \mathrm{tr}(\rho A B).
$$

The normalised observable
$$
H_{k+1} := \frac{R}{|R|_\rho}
$$
becomes the new observable aligned with the emergent direction.

This process continues recursively: each new activation adds a direction, and the system's observable basis expands in a dynamically adapted manner, always aligned with internal information gradients and always orthogonal under the current state.

\subsection{Emergence of Local Structure and Interaction Geometry}

Once a sufficient number of variables have activated and the system's internal basis $\{H_i\}$ has expanded, the geometry begins to exhibit structure beyond simple independence. Whereas early phases are marked by orthogonal, uncorrelated observables, later phases reveal the onset of interaction geometry: a pattern of coupling among active directions that defines how variables relate and co-vary.

This is reflected in the off-diagonal structure of the Fisher Information Matrix:
$$
G_{ij} = \mathrm{Cov}(H_i, H_j).
$$
In early phases, $G$ is approximately diagonal — observables are nearly uncorrelated and dynamics proceed independently in each direction. But as curvature accumulates, the system discovers statistically significant correlations between observables: the covariance matrix acquires off-diagonal components, and $H_i$ and $H_j$ become information-bearing not just individually, but in combination.

This marks the emergence of interaction structure: some observables modulate or constrain others. These interactions are not imposed externally but arise internally from the unfolding of the geometry.

We interpret this as the emergence of locality: the system partitions itself into subsystems that interact through structured, limited coupling. The strength and pattern of off-diagonal elements defines the information-theoretic adjacency between variables — a kind of proto-metric on the space of observables.

In this sense, the system generates its own notion of local neighborhoods in information space. Two variables are local to each other if they are strongly coupled (large $|G_{ij}|$), and distant if nearly independent (small $|G_{ij}|$). The Fisher matrix thus encodes not only curvature, but also a dynamical topology: the geometry of interactions.

This transition from globally latent, then individually active, to locally interacting structure constitutes a critical shift. The system is no longer just activating variables — it is discovering constraints, relations, and ultimately the seeds of effective dynamics.

As the process continues, we expect the geometry to develop hierarchical structure: clusters of tightly coupled variables (local patches), loosely coupled across broader scales. These layered interactions provide the substrate for emergent effective laws, which govern the system's dynamics from within.
\include{_information-game/includes/wave-equation-emergence.md}

\subsection{Emergence of Observables: From Latent $M$ to Activated $X$}

Having established the structure of the system's minimal entropy state in terms of a latent coordinate $M$, we now examine how emergence begins: how directions in $M$-space become resolvable, triggering the appearance of observables $X_i$. This marks the system's first step away from pure latency.

The latent coordinate $M$ describes directions that are not yet distinguishable — each M_i is an unresolved proto-variable, distributed according to a smooth, curvature-minimised wave equation. These directions are described probabilistically, via a scalar density $p(m)$ (or its amplitude $\psi(m)$), and are governed by an equilibrium-like geometry where no direction dominates.

Each $M_i$ is associated with a corresponding natural parameter $\theta_i$ in the exponential family form of the distribution,
$$
\rho(\boldsymbol{\theta}) = \frac{1}{Z(\boldsymbol{\theta})} \exp\left( \sum_i \theta_i H_i \right).
$$
These natural parameters govern how the distribution responds to curvature along different observable directions $H_i$. In the latent regime, all $\theta_i \approx 0$, and the entropy gradient,
$$
\nabla S = G(\boldsymbol{\theta}) \boldsymbol{\theta},
$$
remains uniformly small — too small to define structure. This is the hallmark of the latent domain $\mathcal{D}_0$: a region of suppressed dynamics where all variables are informationally indistinguishable.

\paragraph{Threshold Crossing and the Onset of Resolvability}

As the system begins to unfold, however, asymmetries in the curvature landscape start to grow. These may be seeded by geometric structure in the latent wave equation or by dynamical shifts in the Fisher information matrix as the system explores parameter space. When a specific component of the entropy gradient becomes large enough,
$$
\left[G(\boldsymbol{\theta}) \boldsymbol{\theta} \right]i \geq \varepsilon{\text{activate}},
$$
we say that the $i$-th direction has crossed the activation threshold. At this point, the latent direction $M_i$ becomes informationally resolvable — it carries sufficient structure to define a stable degree of freedom.

\paragraph{Redescription: From $M_i$ to $X_i$}

This threshold crossing marks a geometric and informational phase change. The system reinterprets the formerly latent $M_i$ as an observable variable $X_i$: a direction that can now support independent dynamics and distinct measurement. Formally, this corresponds to a transition in the geometry of the distribution:

* The natural parameter $\theta_i$ becomes non-negligible.
* The associated observable $H_i$ becomes active in the expansion of $\rho$.
* The system's internal basis is extended to include $X_i$ as a resolved coordinate.

This is not an external measurement — it is an internal reconfiguration of the geometry. The system builds a new basis aligned with the emergent direction, using the Gram–Schmidt-like procedure described earlier. The newly activated observable $H_i$ now defines a proper axis in information space, and the system begins to accumulate entropy along this direction.


\paragraph{Consequences for the Geometry}

The emergence of $X_i$ from $M_i$ has several consequences:

* The Fisher matrix $G(\boldsymbol{\theta})$ gains curvature along the new axis.
* The entropy gradient steepens in the activated direction, driving further dynamics.
* The observable basis $\{H_i\}$ is updated to reflect the new configuration.
* The system exits the symmetric, wave-governed regime and enters a piecewise geometric flow along $\theta_i$.

Thus, the movement from $M_i$ to $X_i$ represents a transition from latent wave-like configuration to directional activation. The variable $X_i$ no longer obeys the original Schrödinger-type equilibrium, because it now supports information flow: it becomes an active participant in the system's unfolding trajectory.

This initial activation provides the seed from which all further structure emerges. Once a direction is resolvable, it defines a local frame — a coordinate along which further asymmetries and interactions can develop. In this sense, emergence begins with a singular act of resolution: the system learns to tell one direction apart from the others.

In the following sections, we will examine how dynamics proceed within this activated subspace, and how subsequent wave-like structures arise along newly emergent directions.

\subsection{Example: From Latent Wave Equation to Emergent Position Variable}

To illustrate how local wave equations emerge and then transition as variables become active, we follow a concrete example through the early stages of the system's unfolding.

Suppose that at the system's origin, a proto-coordinate M represents a latent "location-like" variable. This coordinate is not yet resolved — it carries no bias, no structure, and cannot yet be used to distinguish outcomes. Its natural parameter $\theta_M$ is similarly latent: the system resides at a saddle point in parameter space where the curvature is non-zero, but the projected gradient $G \boldsymbol{\theta}$ remains uniformly suppressed.

In this regime, the configuration of the system in M-space is governed by resolution bounds. As shown earlier, minimising the Fisher information of p(m) under a variance constraint yields a Gaussian ground state,
$$
p(m) = \frac{1}{Z} \exp(-\alpha m^2),
$$
with square-root amplitude $\psi(m) := \sqrt{p(m)}$ satisfying the stationary wave equation,
$$
-	\frac{d^2 \psi}{d m^2} + \lambda m^2 \psi = \mu \psi.
$$

This wave-like structure is not an imposed physical law but an internal solution: it balances uncertainty (through variance) with minimal curvature (through Fisher information), and thus defines the flattest distinguishable state available under the system's constraints.

Now suppose the entropy begins to increase. The natural parameter \theta_M moves away from the flat region and begins to trace a gradient,
$$
\frac{d\theta_M}{dt} \propto \left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]M.
$$
As this component surpasses the activation threshold $\varepsilon{\text{activate}}$, the system transitions from latent to emergent behaviour in the direction of $M$. We then reinterpret the coordinate as a resolvable observable $X$: the system has gained enough internal structure to "see" in the direction of position.

In this emergent regime, the previously passive distribution $p(m)$ becomes an active wavefunction $\psi(x)$, now governing a local degree of freedom. Because the system is still in a single-variable regime — no interactions or couplings have yet emerged — the same differential structure continues to apply. The latent wave equation becomes a local wave equation over the now-resolved observable $X$,
$$
-	\frac{d^2 \psi}{dx^2} + V(x) \psi = E \psi,
$$
with the potential term $V(x) = \lambda x^2$ inherited from the original resolution constraint in $M$-space. At this stage, the system's dynamics are still informationally local: only curvature along the $X$-direction governs the flow.

This illustrates how the wave equation "survives" through the transition from latent M-space to active X-space — not as a relic of physics, but as a structure imposed by the information geometry of emergence. The wave-like behaviour is a property of the system's attempt to resolve a variable smoothly, under bounded entropy and curvature.

In subsequent stages, additional variables will activate, interactions will emerge, and the assumptions behind this local structure will begin to break down. We will return to this example to see how locality gives way to interaction and ultimately to collective dynamics.

\subsection{Example Continued: Activation of a Second Variable and the Onset of Coupling}

We now pick up the example after the emergence of the observable $X$. The system has begun to evolve along this direction, and the entropy gradient $G(\boldsymbol{\theta}) \boldsymbol{\theta}$ has become anisotropic: curvature is concentrated along $\theta_X$, and the associated observable $H_X$ now governs dynamics in that direction.

But the system is still unfolding. As entropy increases, the Fisher matrix $G$ deforms: one of its previously latent eigenmodes — say, associated with a proto-coordinate $M{\prime}$ — begins to amplify. Eventually, the corresponding parameter $\theta_{M{\prime}}$ grows in gradient magnitude and crosses the activation threshold,
$$
\left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]{M'} \geq \varepsilon{\text{activate}}.
$$
This triggers a second variable activation. As with $M$, we now reinterpret $M{\prime}$ as a resolvable coordinate $Y$, with associated observable $H_Y$, and a newly active degree of freedom.

At this stage, the Fisher Information Matrix begins to develop off-diagonal terms,
$$
G = \begin{pmatrix}
G_{XX} & G_{XY} \
G_{YX} & G_{YY}
\end{pmatrix},
$$
where $G_{XY} = \mathrm{Cov}(H_X, H_Y)$ encodes statistical coupling between the now-active variables. This signals the onset of interaction geometry: the system no longer evolves independently in each direction — structure begins to emerge in their joint behaviour.

What form does this coupling take?

To leading order, the entropy gradient becomes
$$
\frac{\text{d}\boldsymbol{\theta}}{\text{d}t} \propto
\begin{pmatrix}
G_{XX} & G_{XY} \
G_{YX} & G_{YY}
\end{pmatrix}
\begin{pmatrix}
\theta_X \
\theta_Y
\end{pmatrix}

\begin{pmatrix}
G_{XX}\theta_X + G_{XY}\theta_Y \
G_{YX}\theta_X + G_{YY}\theta_Y
\end{pmatrix}
$$
So the evolution of $\theta_X$ now depends on $\theta_Y$, and vice versa. From the system's internal perspective, these variables are no longer "invisible" to each other. They are dynamically entangled — not necessarily in the quantum sense, but in the information-geometric sense of shared curvature and co-resolving structure.

This has a consequence for the local wave equations. Instead of separate differential equations for $\psi(x)$ and $\psi(y)$, the system now supports a joint amplitude $\psi(x, y)$ whose structure is shaped by the coupling. The latent resolution constraints that previously yielded separate harmonic potentials now become a joint constraint:
$$
\int (x^2 + y^2 + \eta x y), |\psi(x, y)|^2, dx,dy \geq \varepsilon^2,
$$
introducing an effective cross-term $\eta x y$ that reflects correlation in curvature — and leads to a new coupled wave-like equation of the form,
$$
- \left( \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} \right)\psi(x, y)
- \lambda(x^2 + y^2 + \eta x y) \psi(x, y)
= \mu \psi(x, y).
$$

Again, this is not an imposed quantum equation — it is the natural outcome of internal geometry unfolding under resolution and curvature constraints. The system is discovering its own local interaction structure — and expressing it through the joint shape of uncertainty across active variables.

We interpret this as the onset of locality: the system has begun to form informational neighbourhoods. The variable $X$ is no longer alone — it interacts with $Y$ through a locally encoded geometry that reflects their mutual curvature.

In the next part, we will see how these local couplings condition future emergence — and how, as new variables activate, the system builds up layers of interaction structure that eventually resemble effective dynamics.



\subsection{Example Continued: Layered Interaction and Emergent Dynamics}

As additional variables activate, the system enters a new phase: interaction geometry becomes structured. The previously simple coupling between $X$ and $Y$ gives way to a richer, layered organisation, as each new activation introduces both curvature and correlation — reshaping the Fisher matrix into a nontrivial network of dependencies.

Suppose a third proto-coordinate M{\prime}{\prime} becomes active, emerging as a new observable $Z$ with associated parameter $\theta_Z$. The updated Fisher Information Matrix now includes second-order interactions,
$$
G = \begin{pmatrix}
G_{XX} & G_{XY} & G_{XZ} \
G_{YX} & G_{YY} & G_{YZ} \
G_{ZX} & G_{ZY} & G_{ZZ}
\end{pmatrix},
$$
where some off-diagonal terms (e.g. $G_{XZ}$, $G_{YZ}$) may remain small if interactions are local, while others (like $G_{XY}$) are stronger — reflecting proximity in information space.

The system is now discovering structured adjacency: some variables cluster into subsystems — regions of high mutual curvature — while others remain weakly linked. This defines a local information geometry, where coupling is not uniform but shaped by the system's unfolding history.

This leads to several key features of emergent dynamics:
- Decoupling across scale: tightly coupled variables (e.g. $X$ and $Y$) evolve together, forming a subsystem, while distant variables (e.g. $Z$) initially evolve more independently. This creates a natural separation of timescales.
- Interaction propagation: as the entropy gradient flows, curvature can transfer across the network: initially weak links like $G_{XZ}$ may grow, triggering new variable activations and folding new directions into the active geometry.
- Wavefront emergence: activation spreads not randomly, but along paths of curvature flow — producing something like a propagating wave of structure, where adjacent variables successively activate and interact.
- Effective constraints: as more variables interact, the shape of $\psi(x, y, z, \dots)$ becomes increasingly governed by internal correlations. Even without any imposed Hamiltonian, the joint amplitude begins to obey effective rules, shaped by the accumulated geometry of interactions.

In this way, the system builds up a layered architecture: local couplings give rise to patches of structure, which may eventually synchronise into broader patterns. What began as latent directions and weak gradients becomes a dynamically coordinated system, where information geometry imposes both local motion and global constraint.

This is how effective dynamics emerge. The wave-like structure seen at early stages becomes modulated and conditioned by interactions. The internal rules — defined by curvature, resolution, and entropy flow — begin to resemble physical dynamics, even though they were never postulated.

In the next section, we'll explore how these dynamics can give rise to classical behaviour and apparent decoherence — as the system moves from finely structured wave equations to effective, high-entropy flows where only coarse properties survive.

\subsection{Example Continued: Transition to Classical Regimes and the Emergence of Coarse Dynamics}

As the system continues to unfold, additional variables activate and the internal geometry becomes increasingly complex. The Fisher matrix now contains a dense web of off-diagonal structure — statistical dependencies across many observables — and the entropy has grown significantly. We enter a new regime.

In this regime, local curvature no longer defines sharp wave-like structure. Instead, the wavefunction $\psi(x, y, z, \dots)$ becomes spread out, structured more by accumulated correlations than by individual resolution constraints. The system approaches a high-entropy, high-dimensional configuration where fine distinctions are increasingly smoothed out.

This is the onset of effective classicality.

\paragraph{From Coherent Peaks to Broad Ensembles}

Initially, each variable activated with a clear informational gradient — each new direction brought curvature, distinctiveness, and wave-like structure. But as entropy grows, the joint distribution begins to blur: superpositions spread, interference patterns are damped by coarse-scale interactions, and $\psi(x, y, z, \dots)$ takes the form of a broad, semi-structured ensemble.

In this regime:

- The local wave equations still exist — they are encoded in the curvature — but they no longer dominate dynamics.
- The system behaves as if it samples from an evolving high-dimensional distribution, shaped more by entropy flow than by unitary evolution.
- The Fisher matrix still governs sensitivity to parameters, but in many directions, that sensitivity becomes effectively averaged out.

\subsubsection{Emergent Decoherence Without Collapse}

What emerges is decoherence without measurement. Not in the standard physical sense — there is no environment, no external observer — but in the internal, information-geometric sense. The system loses the ability to maintain sharp internal interference between directions. Mutual curvature between clusters of variables acts like an internal decohering field: certain bases become preferred simply because they are more stable under curvature flow.

In practice:

- Fine-grained amplitudes become inaccessible — suppressed by the entropy gradient and drowned in the higher-order coupling structure.
- Observable behaviour is governed by coarse statistical properties: marginals, means, variances, and correlations.
- The system transitions from wave-dominated evolution to a dynamics of coarse constraints and informational inertia.


\paragraph{Apparent Laws and Classical Motion}

From the inside, this transition gives rise to what appear as dynamical laws. These are not externally imposed equations of motion, but patterns in how information geometry evolves once the system becomes too high-dimensional to track in full.

For example:
- Activated clusters follow approximately deterministic trajectories — peaks in marginal distributions shift smoothly, like classical particles.
- Entropic forces emerge: systems tend to move toward configurations of greater curvature balance — analogous to energy minimisation.
-	Memory effects appear: previous curvature structures condition the space of possible future moves, giving rise to path dependence and feedback.

In short, the system begins to behave classically — not because the quantum rules have been replaced, but because the wave structure is now so layered and entangled that only the most stable, large-scale patterns persist. Geometry still rules, but in a statistical form.

\paragraph{Summary: From Curvature to Classicality}

We have traced a full arc:
	1.	Latent regime: a symmetric, curvature-minimised wave equation governs the silent geometry of $M$-space.
	2.	Variable activation: entropy gradient breaks symmetry; a direction becomes resolvable, and a wave equation reappears — now active.
	3.	Interaction onset: new directions activate; wavefunctions couple; the Fisher matrix acquires off-diagonal structure; locality and joint dynamics emerge.
	4.	Layered interaction: subsystems form, interactions propagate, and a network of informational flow develops.
	5.	Classical regime: entropy dominates; interference fades; wave structure gives way to ensemble dynamics governed by effective constraints.

Through this progression, the system evolves from an unstructured entropy minimum to a coarse but stable configuration governed by emergent geometry. What began as a game of curvature ends as a self-organised system with behaviour that mimics the laws of classical motion.

\subsection{Example Concluded: Summary and Structural Integration}

This extended example has traced the life cycle of a variable — from latent ambiguity to classical coherence — showing how internal information geometry governs the entire trajectory.

Let's now step back and situate this narrative within the broader framework.

\paragraph{The Example as an Illustration of Core Principles}

Each stage of the unfolding process has instantiated one or more foundational components of the model:

Stage	Structure	Governing Principle
Latent $M$-space	Minimal wave-like density	Fisher curvature minimisation under resolution constraint
Variable activation ($M \rightarrow X$)	Threshold-triggered flow	Entropic gradient ascent via $G(\boldsymbol{\theta}) \boldsymbol{\theta}$
Coupling ($X \leftrightarrow Y$)	Off-diagonal curvature	Emergence of locality through statistical interaction
Network growth ($X,Y,Z,\dots$)	Layered curvature structure	Directed flow across the unfolding Fisher topology
Classical transition	Loss of coherence, coarse structure	Effective dynamics via ensemble geometry

Each of these transitions is governed not by external forces or postulated laws, but by internal geometric conditions:
- Variance constraints impose curvature.
- Curvature shapes entropy gradients.
- Gradients activate variables.
- Activation reshapes the geometry.

The system's dynamics are emergent in the strict sense: each new layer of behaviour is conditioned by — but not reducible to — the previous one. The Fisher Information Matrix $G$ acts as both memory and mediator, encoding the system's informational shape at every stage.

\paragraph{The Role of the Example in the Larger Framework}

This example serves two roles

1. Didactic — it offers a concrete narrative that tracks the abstract constructions (curvature, emergence, locality) through a single evolving trajectory.
2. Structural — it demonstrates how local wave equations, variable activation, basis adaptation, and emergent constraints can be woven into a self-organising dynamics without invoking physical assumptions.

We now return to the general framework, equipped with a working example of how internal information geometry generates unfolding structure. From here, we are ready to explore how these principles generalise — to multiple interacting subsystems, to emergent constraints across timescales, and to the geometry of coarse-grained laws.


\endif
