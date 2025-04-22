\ifndef{emergentObservables}
\define{emergentObservables}

\editme

\subsection{Constructing the Updated Basis: Emergent Observables}

\slides{
- When a new variable activates, system must update its internal basis $\{H_i\}$
- New observables must align with entropy gradient
- System maintains orthogonality between observables
- Basis must remain consistent with curvature structure
}

\notes{When a new variable activates, the system must update its internal basis $\{H_i\}$ to reflect the newly emergent structure. This reflects a geometric transformation in the space of information-bearing observables.}

\notes{This process is not an external analysis or numerical procedure, but rather a description of how the system itself naturally organizes its observables as it unfolds. It's similar to how a quantum system might choose its basis states, but here it's driven by information geometry rather than physical laws.}

Given an existing set of active observables $\{H_1, \dots, H_k\}$ and a newly activated direction $\theta_{k+1}$, we seek a corresponding observable $H_{k+1}$ such that it aligns with the updated gradient,
$$
\left.\nabla_{\boldsymbol{\theta}} S[\rho]\right|_{\theta_{k+1}} = - G(\boldsymbol{\theta}) \boldsymbol{\theta} \propto H_{k+1},
$$
it preserves orthogonality (uncorrelatedness) under the current state,
$$
\mathrm{Cov}(H_{k+1}, H_j) = 0 \quad \text{for all } j \leq k,
$$
it is consistent with the curvature structure,
$$
H_{k+1} \in \operatorname{span}\left\{ \frac{\partial \rho}{\partial \theta_i} \right\} \quad \text{evaluated near } \boldsymbol{\theta}_0.
$$

\newslide{Orthogonality vs. Uncorrelatedness}
\slides{
- Orthogonality: $\langle H_i, H_j \rangle = \mathrm{tr}(\rho H_i H_j) = 0$
- Uncorrelatedness: $\mathrm{Cov}(H_i, H_j) = \mathrm{tr}(\rho H_i H_j) - \mathrm{tr}(\rho H_i)\mathrm{tr}(\rho H_j) = 0$
- For quadratic observables in Gaussian state: orthogonality implies uncorrelatedness
- System maintains both properties to ensure consistent internal representation
}

\notes{The relationship between orthogonality and uncorrelatedness is subtle but important. Orthogonality refers to the inner product between observables being zero,
$$
\langle H_i, H_j \rangle = \mathrm{tr}(\rho H_i H_j) = 0,
$$
whereas uncorrelatedness refers to the covariance between observables being zero,
$$
\mathrm{Cov}(H_i, H_j) = \mathrm{tr}(\rho H_i H_j) - \mathrm{tr}(\rho H_i)\mathrm{tr}(\rho H_j) = 0.
$$}

\notes{For quadratic observables in a Gaussian state (as derived in the Jaynesian formulation), these properties coincide. This is because the expectation values $\mathrm{tr}(\rho H_i)$ and $\mathrm{tr}(\rho H_j)$ are zero for centered quadratic observables in a symmetric Gaussian state.}

\notes{The system maintains both properties to ensure a consistent internal representation. The preservation of both orthogonality and uncorrelatedness is essential for the emergence of a well-defined information geometry because it ensures that the system's internal representation remains stable and unambiguous as new observables emerge.}

This yields a Gram–Schmidt-like procedure within the information geometry: new directions are orthogonalised with respect to the current active basis, and constrained to lie in the space spanned by gradient responses.

\newslide{Gram-Schmidt Procedure in Information Geometry}
\slides{
- Define update rule: $\widetilde{H}_{k+1} := \sum_i c_i H_i + R$
- Residual direction: $R := G(\boldsymbol{\theta}) \boldsymbol{\theta} - \sum_{i} c_i H_i$
- Coefficients $c_i$ minimize norm of $R$ under inner product $\langle A, B \rangle := \mathrm{tr}(\rho A B)$
- Normalized observable: $H_{k+1} := \frac{R}{|R|_\rho}$
}

\notes{We can make this more explicit by defining an update rule. Let
$$
\widetilde{H}_{k+1} := \sum_i c_i H_i + R,
$$
where $R$ is the residual direction from the entropy gradient,
$$
R := G(\boldsymbol{\theta}) \boldsymbol{\theta} - \sum_{i} c_i H_i,
$$
and the coefficients $c_i$ are chosen to minimise the norm of $R$ under the inner product
$$
\langle A, B \rangle := \mathrm{tr}(\rho A B).
$$}

\notes{This is analogous to the Gram-Schmidt procedure in linear algebra, but adapted to the information geometry of the system. The inner product is defined by the instantaneous state $\rho$ at each point in the system's evolution, ensuring that the new observable is orthogonal to the existing ones in the information-theoretic sense. This state-dependent inner product allows the system to adapt its geometry to changing conditions while maintaining consistency.}

\notes{The normalised observable
$$
H_{k+1} := \frac{R}{|R|_\rho}
$$
becomes the new observable aligned with the emergent direction.}

\notes{This process continues recursively: each new activation adds a direction, and the system's observable basis expands in a dynamically adapted manner, always aligned with internal information gradients and always orthogonal under the current state.}

\notes{The procedure is not a computational algorithm but a mathematical description of how the system naturally organizes its observables. This description captures how the system maintains a consistent internal representation throughout its evolution by ensuring that each new observable is properly integrated into the existing information-theoretic structure, while allowing for the emergence of new degrees of freedom that respect the underlying geometry.}

\subsection{Emergence of Local Structure and Interaction Geometry}

\slides{
- As more variables activate, system develops interaction geometry
- Fisher Information Matrix develops off-diagonal structure
- System discovers statistical correlations between observables
- Emergence of locality: system partitions into interacting subsystems
}

\notes{Once a sufficient number of variables have activated and the system's internal basis $\{H_i\}$ has expanded, the geometry begins to exhibit structure beyond simple independence. Whereas early phases are marked by orthogonal, uncorrelated observables, later phases reveal the onset of interaction geometry: a pattern of coupling among active directions that defines how variables relate and co-vary.}

\notes{This transition from independent to interacting observables is a critical shift in the system's evolution. It marks the beginning of complex structure formation, where variables not only exist individually but also form meaningful relationships with each other.}

\notes{This is reflected in the off-diagonal structure of the Fisher Information Matrix
$$
G_{ij} = \mathrm{Cov}(H_i, H_j).
$$
In early phases, $G$ is approximately diagonal — observables are nearly uncorrelated and dynamics proceed independently in each direction. But as curvature accumulates, the system discovers statistically significant correlations between observables: the covariance matrix acquires off-diagonal components, and $H_i$ and $H_j$ become information-bearing not just individually, but in combination.}

\newslide{From Independence to Interaction}
\slides{
- Early phase: Fisher matrix $G$ is approximately diagonal
- Later phase: Off-diagonal terms emerge, reflecting correlations
- Observables become information-bearing in combination
- System discovers statistical dependencies between variables
}

\notes{The emergence of off-diagonal terms in the Fisher matrix represents a fundamental shift in the system's structure. What began as a collection of independent observables becomes a network of interacting elements, where the behavior of one variable influences and is influenced by others.}

\notes{This marks the emergence of interaction structure: some observables modulate or constrain others. These interactions are not imposed externally but arise internally from the unfolding of the geometry. We interpret this as the emergence of locality: the system partitions itself into subsystems that interact through structured, limited coupling. The strength and pattern of off-diagonal elements defines the information-theoretic adjacency between variables — a kind of proto-metric on the space of observables.}

\notes{This concept of locality is information-theoretic rather than spatial. Two variables are considered "local" to each other if they are strongly coupled in the Fisher matrix, meaning they carry significant mutual information. This creates a natural notion of distance in the space of observables, where "close" variables are those with strong statistical dependencies.}

\notes{In this sense, the system generates its own notion of local neighborhoods in information space. Two variables are local to each other if they are strongly coupled (large $|G_{ij}|$), and distant if nearly independent (small $|G_{ij}|$). The Fisher matrix thus encodes not only curvature, but also a dynamical topology: the geometry of interactions.}

\notes{This information-theoretic notion of locality is fundamental to understanding how complex systems organize themselves. It explains why certain variables tend to cluster together while others remain separate, creating the hierarchical structure we observe in natural systems.}

This transition from globally latent, then individually active, to locally interacting structure constitutes a critical shift. The system is no longer just activating variables — it is discovering constraints, relations, and ultimately the seeds of effective dynamics.

\notes{This progression from latent to active to interacting represents a natural pathway for the emergence of complexity. Each stage builds on the previous one, with new properties emerging that weren't present in earlier stages.}

\notes{As the process continues, we expect the geometry to develop hierarchical structure: clusters of tightly coupled variables (local patches), loosely coupled across broader scales. These layered interactions provide the substrate for emergent effective laws, which govern the system's dynamics from within.}

\notes{As we discussed in the Jaynesian derivation, at the threshold between latent and active variables, a wave equation emerges that governs the configuration of unresolved variables. This wave equation is a geometric consequence of information constraints and represents the optimal balance between localization and uncertainty.}

\subsection{Emergence of Observables: From Latent $M$ to Activated $X$}

\slides{
- Latent coordinates $M$ describe unresolved directions
- Activation occurs when entropy gradient exceeds threshold
- System reinterprets latent $M_i$ as observable $X_i$
- This marks transition from wave-like to directional dynamics
}

\notes{Having established the structure of the system's minimal entropy state in terms of a latent coordinate $M$, we now examine how emergence begins: how directions in $M$-space become resolvable, triggering the appearance of observables $X_i$. This marks the system's first step away from pure latency.}

\notes{The latent coordinate $M$ describes directions that are not yet distinguishable — each M_i is an unresolved proto-variable, distributed according to a smooth, curvature-minimised wave equation. These directions are described probabilistically, via a scalar density $p(m)$ (or its amplitude $\psi(m)$), and are governed by an equilibrium-like geometry where no direction dominates.}

\notes{In this latent regime, the system exists in a state of symmetric uncertainty, where no direction is preferred over any other. This is reflected in the wave-like structure of the density, which balances localization and uncertainty according to the resolution constraints.}

\notes{Each $M_i$ is associated with a corresponding natural parameter $\theta_i$ in the exponential family form of the distribution,
$$
\rho(\boldsymbol{\theta}) = \frac{1}{Z(\boldsymbol{\theta})} \exp\left( \sum_i \theta_i H_i \right).
$$
These natural parameters $\theta_i$ are the Lagrange multipliers that emerge from the maximum entropy principle. They have a special role in the exponential family - they are the parameters that make the form of the distribution most mathematically convenient. Each $\theta_i$ governs how the distribution responds to curvature along its corresponding observable direction $H_i$. In the latent regime, all $\theta_i \approx 0$, and the entropy gradient,
$$
\nabla S = -G(\boldsymbol{\theta}) \boldsymbol{\theta},
$$
remains uniformly small — too small to define structure. This is the hallmark of the latent domain $\mathcal{D}_0$: a region of suppressed dynamics where all variables are informationally indistinguishable.}

\notes{The condition $\theta_i \approx 0$ for all $i$ ensures that the system remains in a state of minimal entropy, with no directional bias. The entropy gradient $G(\boldsymbol{\theta}) \boldsymbol{\theta}$ being uniformly small means that there's no strong drive for the system to evolve in any particular direction.}

\paragraph{Threshold Crossing and the Onset of Resolvability}

\slides{
- Asymmetries in curvature landscape begin to grow
- When entropy gradient component exceeds threshold: $\left[G(\boldsymbol{\theta}) \boldsymbol{\theta} \right]_i \geq \varepsilon_{\text{activate}}$
- $i$-th direction becomes resolvable
- Latent $M_i$ becomes observable $X_i$
}
\notes{As the system begins to unfold asymmetries in the curvature landscape start to grow. These may be seeded by geometric structure in the latent wave equation or by dynamical shifts in the Fisher information matrix as the system explores parameter space. When a specific component of the entropy gradient becomes large enough,
$$
\left[G(\boldsymbol{\theta}) \boldsymbol{\theta} \right]_i \geq \varepsilon,
$$
we say that the $i$-th direction has crossed the activation threshold. At this point, the latent direction $M_i$ becomes informationally resolvable — it carries sufficient structure to define a stable degree of freedom.}

\notes{The activation threshold $\varepsilon$ determines where the entropy gradient becomes strong enough to drive emergence.}

\paragraph{Redescription: From $M_i$ to $X_i$}

\slides{
- System reinterprets latent $M_i$ as observable $X_i$
- Natural parameter $\theta_i$ becomes non-negligible
- Observable $H_i$ becomes active in expansion of $\rho$
- System's internal basis is extended to include $X_i$
}

\notes{This threshold crossing marks a phase change. The formerly latent $M_i$ is now an observable variable $X_i$: a direction that can now support independent dynamics and distinct measurement. At this point the natural parameter $\theta_i$ becomes non-negligible, The associated observable $H_i$ becomes active in the expansion of $\rho$ and the system's internal basis is extended to include $X_i$ as a resolved coordinate.}

\notes{The transition from $M_i$ to $X_i$ is a change in how the system represents and interacts with this direction. What was previously a latent, unresolved degree of freedom becomes an active, resolvable variable that can support independent dynamics.}

\notes{Unlike observer-dependent systems, this is not an external measurement — it is an internal reconfiguration of the geometry. The system builds a new basis aligned with the emergent direction, using the Gram–Schmidt-like procedure described above. The newly activated observable $H_i$ now defines a proper axis in information space, and the system begins to accumulate entropy along this direction.}

\paragraph{Consequences for the Geometry}

\slides{
- Fisher matrix gains curvature along new axis
- Entropy gradient steepens in activated direction
- Observable basis is updated to reflect new configuration
- System exits symmetric regime, enters piecewise geometric flow
}

\notes{The emergence of $X_i$ from $M_i$ has several consequences. Firstly the Fisher matrix $G(\boldsymbol{\theta})$ gains curvature along the new axis. Secondly the entropy gradient steepens in the activated direction, driving further dynamics. The observable basis $\{H_i\}$ is updated to reflect the new configuration and the system exits the symmetric, wave-governed regime and enters a piecewise geometric flow along $\theta_i$.}

\notes{What was previously a symmetric, wave-like configuration becomes a directional, geometric flow. This transition allows for the appearance of new structure and dynamics that weren't present in the initial state.}

\notes{The initial activation provides a seed from which further structure emerges. Once a direction is resolvable, it defines a local frame — a coordinate along which further asymmetries and interactions can develop. The system now has an anisotropy in one direction.}

\notes{The first activation breaks the initial symmetry of the system creating a reference point against which other directions can be measured.}

\subsection{Example: From Latent Wave Equation to Emergent Position Variable}

\slides{
- Follow concrete example through early stages of system unfolding
- Start with latent "location-like" variable $M$
- Show how it becomes resolvable as observable $X$
- Demonstrate transition from wave equation to directional dynamics
}

\notes{To illustrate how local wave equations emerge and then transition as variables become active, we follow a concrete example through the early stages of the system's unfolding. We'll focus on a simple case — the emergence of a position-like variable — but the principles apply more generally.}

\notes{Suppose that at the system's origin, a proto-coordinate $$ represents a latent "location-like" variable. This coordinate is not yet resolved — it carries no bias, no structure, and cannot yet be used to distinguish outcomes. Its natural parameter $\theta_M$ is similarly latent: the system resides at a saddle point in parameter space where the curvature is non-zero, but the projected gradient $G \boldsymbol{\theta}$ remains uniformly suppressed.}

\notes{The choice of a "location-like" variable is deliberate, as position is one of the most fundamental observables in physical systems. However, this is just a label — the mathematical structure applies to any type of variable that might emerge.}

\notes{In this regime, the configuration of the system in $M$-space is governed by resolution bounds. As shown earlier, minimising the Fisher information of $p(m)$ under a variance constraint yields a Gaussian ground state,
$$
p(m) = \frac{1}{Z} \exp(-\alpha m^2),
$$
with square-root amplitude $\psi(m) := \sqrt{p(m)}$ satisfying the stationary wave equation,
$$
-	\frac{d^2 \psi}{d m^2} + \lambda m^2 \psi = \mu \psi.
$$}

\notes{This wave equation emerges  from the information constraints and represents the optimal balance between localization and uncertainty under the resolution constraint.}

\notes{Now suppose the entropy begins to increase. The natural parameter $\theta_M$ moves away from the flat region and begins to trace a gradient,
$$
\frac{\text{d}\theta_M}{\text{d}\tau} = -\left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_M.
$$
As this component surpasses the activation threshold $\varepsilon$, the system transitions from latent to emergent behaviour in the direction of $M$. We then reinterpret the coordinate as a resolvable observable $X$: the system has gained enough internal structure to "see" in the direction of position.}

\notes{This transition from latent to emergent behavior is triggered by the entropy gradient exceeding the activation threshold. Once this happens, the system can resolve variation in this direction, and the coordinate becomes an active degree of freedom.}

\notes{In this emergent regime, the previously passive distribution $p(m)$ becomes an active wavefunction $\psi(x)$, now governing a local degree of freedom. Because the system is still in a single-variable regime — no interactions or couplings have yet emerged — the same differential structure continues to apply. The latent wave equation becomes a local wave equation over the now-resolved observable $X$,
$$
-	\frac{d^2 \psi}{dx^2} + V(x) \psi = E \psi,
$$
with the potential term $V(x) = \lambda x^2$ inherited from the original resolution constraint in $M$-space. At this stage, the system's dynamics are still informationally local: only curvature along the $X$-direction governs the flow.}

\notes{The transition from $p(m)$ to $\psi(x)$ represents a shift in how the system represents this degree of freedom. What was previously just a probability distribution becomes a wavefunction that governs the system's dynamics in this direction.}

\notes{This illustrates how the wave equation "survives" through the transition from latent $M$-space to active $X$-space — not as a relic of physics, but as a structure imposed by the information geometry of emergence. The wave-like behaviour is a property of the system's attempt to resolve a variable smoothly, under bounded entropy and curvature.}

\notes{This is a crucial insight: the wave equation isn't just a feature of quantum mechanics, but a general property of systems trying to resolve variables under information constraints. This suggests that quantum-like behavior might be more widespread than we typically assume.}

\notes{In subsequent stages, additional variables will activate, interactions will emerge, and the assumptions behind this local structure will begin to break down. We will return to this example to see how locality gives way to interaction and ultimately to collective dynamics.}

\subsection{Example Continued: Activation of a Second Variable and the Onset of Coupling}

\slides{
- After emergence of $X$, system begins to evolve along this direction
- Entropy gradient becomes anisotropic, curvature concentrates along $\theta_X$
- Second proto-coordinate $M'$ begins to amplify, eventually activating as $Y$
- Fisher matrix develops off-diagonal terms, signaling onset of interaction
}

\notes{We now pick up the example after the emergence of the observable $X$. The system has begun to evolve along this direction, and the entropy gradient $G(\boldsymbol{\theta}) \boldsymbol{\theta}$ has become anisotropic: curvature is concentrated along $\theta_X$, and the associated observable $H_X$ now governs dynamics in that direction.}

\notes{With the activation of $X$, the system has taken its first step away from the symmetric initial state. Now there's a preferred direction in the system's evolution, which creates the conditions for further emergence.}

\notes{But the system is still unfolding. As entropy increases, the Fisher matrix $G$ deforms: one of its previously latent eigenmodes — say, associated with a proto-coordinate $M'$ — begins to amplify. Eventually, the corresponding parameter $\theta_{M'}$ grows in gradient magnitude and crosses the activation threshold,
$$
\left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_{M'} \geq \varepsilon.
$$
This triggers a second variable activation. As with $M$, we now reinterpret $M'$ as a resolvable coordinate $Y$, with associated observable $H_Y$, and a newly active degree of freedom.}

\notes{Now the system has two active degrees of freedom, which can interact with each other. This sets the stage for the emergence of more complex dynamics.}

\notes{At this stage, the Fisher information matrix begins to develop off-diagonal terms,
$$
G = \begin{bmatrix}
G_{XX} & G_{XY} \\
G_{YX} & G_{YY}
\end{bmatrix},
$$
where $G_{XY} = \mathrm{Cov}(H_X, H_Y)$ encodes statistical coupling between the now-active variables. This signals the onset of interaction geometry: the system no longer evolves independently in each direction — structure begins to emerge in their joint behaviour.}

\notes{The appearance of off-diagonal terms in the Fisher matrix is an indicator of interaction. These terms represent the statistical dependencies between variables, showing how they influence each other's behavior.}

\newslide{Entropy Gradient with Coupling}
\slides{
- Entropy gradient becomes:
  $$
  \frac{\text{d}\boldsymbol{\theta}}{\text{d}t} = -
  \begin{bmatrix}
  G_{XX} & G_{XY} \\
  G_{YX} & G_{YY}
  \end{bmatrix}
  \begin{bmatrix}
  \theta_X \\
  \theta_Y
  \end{bmatrix}
  = -
  \begin{bmatrix}
  G_{XX}\theta_X + G_{XY}\theta_Y \\
  G_{YX}\theta_X + G_{YY}\theta_Y
  \end{bmatrix}
  $$
- Evolution of $\theta_X$ now depends on $\theta_Y$, and vice versa
- Variables become dynamically entangled
}

\notes{To leading order, the entropy gradient becomes
$$
\frac{\text{d}\boldsymbol{\theta}}{\text{d}t} = -
\begin{bmatrix}
G_{XX} & G_{XY} \\
G_{YX} & G_{YY}
\end{bmatrix}
\begin{bmatrix}
\theta_X \\
\theta_Y
\end{bmatrix}
= -
\begin{bmatrix}
G_{XX}\theta_X + G_{XY}\theta_Y \\
G_{YX}\theta_X + G_{YY}\theta_Y
\end{bmatrix}
$$
So the evolution of $\theta_X$ now depends on $\theta_Y$, and vice versa. From the system's internal perspective, these variables are no longer "invisible" to each other. They are dynamically entangled — not necessarily in the quantum sense, but in the information-geometric sense of shared curvature and co-resolving structure.}


\notes{This has a consequence for the local wave equations. Instead of separate differential equations for $\psi(x)$ and $\psi(y)$, the system now supports a joint amplitude $\psi(x, y)$ whose structure is shaped by the coupling. The latent resolution constraints that previously yielded separate harmonic potentials now become a joint constraint:
$$
\int (x^2 + y^2 + \eta x y) |\psi(x, y)|^2 \, \text{d}x \, \text{d}y \geq \varepsilon^2,
$$
introducing an effective cross-term $\eta x y$ that reflects correlation in curvature — and leads to a new coupled wave-like equation of the form,
$$
- \left( \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} \right)\psi(x, y)
- \lambda(x^2 + y^2 + \eta x y) \psi(x, y)
= \mu \psi(x, y).
$$}

\notes{The emergence of a joint wavefunction $\psi(x, y)$ represents a shift in the system's structure. Now the variables are not just independent degrees of freedom, but parts of a unified whole, with their behavior determined by their joint configuration.}

\notes{This is another key insight: the coupled wave equation emerges naturally from the information geometry, without needing to postulate quantum mechanics or any other physical theory. This suggests that quantum-like behavior might be more fundamental than we typically assume.}

\notes{We interpret this as the onset of locality: the system has begun to form informational neighbourhoods. The variable $X$ is no longer alone — it interacts with $Y$ through a locally encoded geometry that reflects their mutual curvature.}

\notes{The concept of locality here is information-theoretic rather than spatial. Two variables are considered "local" to each other if they are strongly coupled in the Fisher matrix, meaning they carry significant mutual information.}

\notes{In the next part, we will see how these local couplings condition future emergence — and how, as new variables activate, the system builds up layers of interaction structure that eventually resemble effective dynamics.}

\subsection{Example Continued: Layered Interaction and Emergent Dynamics}

\slides{
- As more variables activate, interaction geometry becomes structured
- Fisher matrix develops into network of dependencies
- System discovers structured adjacency: some variables cluster into subsystems
- Emergence of decoupling across scale, interaction propagation, wavefront emergence
}

\notes{As additional variables activate, the system enters a new phase: interaction geometry becomes structured. The previously simple coupling between $X$ and $Y$ gives way to a richer, layered organisation, as each new activation introduces both curvature and correlation — reshaping the Fisher matrix into a nontrivial network of dependencies.}

\notes{This transition from simple coupling to structured interaction represents a significant step in the system's evolution. Now the system is not just activating variables, but organizing them into a coherent structure with meaningful relationships.}

\notes{Suppose a third proto-coordinate $M''$ becomes active, emerging as a new observable $Z$ with associated parameter $\theta_Z$. The updated Fisher Information Matrix now includes second-order interactions,
$$
G = \begin{bmatrix}
G_{XX} & G_{XY} & G_{XZ} \\
G_{YX} & G_{YY} & G_{YZ} \\
G_{ZX} & G_{ZY} & G_{ZZ}
\end{bmatrix},
$$
where some off-diagonal terms (e.g. $G_{XZ}$, $G_{YZ}$) may remain small if interactions are local, while others (like $G_{XY}$) are stronger — reflecting proximity in information space.}

\notes{The structure of the Fisher matrix now encodes a rich network of interactions, with some variables strongly coupled and others weakly coupled. This creates a natural notion of distance in the space of observables, where "close" variables are those with strong statistical dependencies.}

\notes{The system is now discovering structured adjacency: some variables cluster into subsystems — regions of high mutual curvature — while others remain weakly linked. This defines a local information geometry, where coupling is not uniform but shaped by the system's unfolding history.}

\notes{This emergence of structured adjacency is a key feature of complex systems. It explains why certain variables tend to cluster together while others remain separate, creating the hierarchical structure we observe in natural systems.}

\notes{This leads to several key features of emergent dynamics:

- Decoupling across scale: tightly coupled variables (e.g. $X$ and $Y$) evolve together, forming a subsystem, while distant variables (e.g. $Z$) initially evolve more independently. This creates a natural separation of timescales.
- Interaction propagation: as the entropy gradient flows, curvature can transfer across the network: initially weak links like $G_{XZ}$ may grow, triggering new variable activations and folding new directions into the active geometry.
- Wavefront emergence: activation spreads not randomly, but along paths of curvature flow — producing something like a propagating wave of structure, where adjacent variables successively activate and interact.
- Effective constraints: as more variables interact, the shape of $\psi(x, y, z, \dots)$ becomes increasingly governed by internal correlations. Even without any imposed Hamiltonian, the joint amplitude begins to obey effective rules, shaped by the accumulated geometry of interactions.}

\notes{These features of emergent dynamics are reminiscent of what we observe in physical systems, from the behavior of particles to the evolution of ecosystems. The fact that they emerge naturally from information geometry suggests that they might be more fundamental than we typically assume.}

\notes{In this way, the system builds up a layered architecture: local couplings give rise to patches of structure, which may eventually synchronise into broader patterns. What began as latent directions and weak gradients becomes a dynamically coordinated system, where information geometry imposes both local motion and global constraint.}

\notes{This layered architecture is a key feature of complex systems, from atoms to molecules to cells to organisms. At each level, new properties emerge that weren't present at lower levels, creating a rich hierarchy of structure and behavior.}

\notes{This is how dynamics emerge. The wave-like structure seen at early stages becomes modulated and conditioned by interactions. The internal rules — defined by curvature, resolution, and entropy flow — begin to resemble physical dynamics, even though they were never postulated.}

\notes{This is perhaps the most profound insight: that physical-like dynamics can emerge naturally from information geometry, without needing to postulate physical laws. This suggests that physics might be more fundamentally about information and geometry than we typically assume.}

\notes{In the next section, we'll explore how these dynamics can give rise to classical behaviour and apparent decoherence — as the system moves from finely structured wave equations to effective, high-entropy flows where only coarse properties survive.}

\subsection{Example Continued: Transition to Classical Regimes and the Emergence of Coarse Dynamics}

\slides{
- As more variables activate, system enters high-entropy regime
- Wave-like structure gives way to ensemble dynamics
- System transitions from wave-dominated to coarse statistical behavior
- Emergence of apparent decoherence without measurement
}

\notes{As the system continues to unfold, additional variables activate and the internal geometry becomes increasingly complex. The Fisher matrix now contains a dense web of off-diagonal structure — statistical dependencies across many observables — and the entropy has grown significantly. We enter a new regime.}

\notes{This transition to a high-entropy regime represents a shift in the system's behavior. What was previously a finely structured wave-like system becomes a coarse statistical ensemble, with different dynamics and properties.}

\notes{In this regime, local curvature no longer defines sharp wave-like structure. Instead, the wavefunction $\psi(x, y, z, \dots)$ becomes spread out, structured more by accumulated correlations than by individual resolution constraints. The system approaches a high-entropy, high-dimensional configuration where fine distinctions are increasingly smoothed out.}

\notes{This smoothing out of fine structure is a consequence of the system's evolution toward higher entropy. As more variables activate and interact, the system becomes too complex to maintain sharp distinctions, and coarse-grained properties begin to dominate.}


\subsubsection{From Coherent Peaks to Broad Ensembles}

\slides{
- Initially, each variable activated with clear informational gradient
- As entropy grows, joint distribution begins to blur
- Superpositions spread, interference patterns are damped
- System behaves as if sampling from evolving high-dimensional distribution
}

\notes{Initially, each variable activated with a clear informational gradient — each new direction brought curvature, distinctiveness, and wave-like structure. But as entropy grows, the joint distribution begins to blur: superpositions spread, interference patterns are damped by coarse-scale interactions, and $\psi(x, y, z, \dots)$ takes the form of a broad, semi-structured ensemble.}

\notes{This transition from sharp peaks to broad ensembles is a key feature of the classical regime. What was previously a well-defined wavefunction becomes a statistical distribution, with uncertainty spread across many dimensions.}

\notes{In this regime:

- The local wave equations still exist — they are encoded in the curvature — but they no longer dominate dynamics.
- The system behaves as if it samples from an evolving high-dimensional distribution, shaped more by entropy flow than by unitary evolution.
- The Fisher matrix still governs sensitivity to parameters, but in many directions, that sensitivity becomes effectively averaged out.}

\notes{Despite the transition to classical behavior, the underlying wave equations are still present, just obscured by the complexity of the system. This suggests that quantum and classical behavior might be more closely related than we typically assume, with classicality emerging naturally from complexity.}

\subsubsection{Emergent Decoherence Without Collapse}

\slides{
- System loses ability to maintain sharp internal interference
- Mutual curvature between clusters acts like internal decohering field
- Fine-grained amplitudes become inaccessible
- Observable behavior governed by coarse statistical properties
}

\notes{What emerges is decoherence without measurement. Not in the standard physical sense — there is no environment, no external observer — but in the internal, information-geometric sense. The system loses the ability to maintain sharp internal interference between directions. Mutual curvature between clusters of variables acts like an internal decohering field: certain bases become preferred simply because they are more stable under curvature flow.}

\notes{Decoherence can emerge naturally from information geometry, without needing an external environment or observer. The system's own complexity creates the conditions for classical behavior.}

\notes{In practice:

- Fine-grained amplitudes become inaccessible — suppressed by the entropy gradient and drowned in the higher-order coupling structure.
- Observable behaviour is governed by coarse statistical properties: marginals, means, variances, and correlations.
- The system transitions from wave-dominated evolution to a dynamics of coarse constraints and informational inertia.}

\notes{This transition from quantum-like to classical-like behavior is a natural consequence of the system's evolution toward higher entropy and complexity. As more variables activate and interact, the system becomes too complex to maintain quantum coherence, and classical behavior emerges.}

\paragraph{Apparent Laws and Classical Motion}

\slides{
- Activated clusters follow approximately deterministic trajectories
- Entropic forces emerge: systems move toward configurations of greater curvature balance
- Memory effects appear: previous curvature structures condition future moves
- System begins to behave classically due to layered and entangled wave structure
}

\notes{From the inside, this transition gives rise to what appear as dynamical laws. These are not externally imposed equations of motion, but patterns in how information geometry evolves once the system becomes too high-dimensional to track in full.}

\notes{This emergence of apparent laws is a key feature of the classical regime. What was previously a complex wave-like system becomes a simpler, more predictable system governed by effective rules.}

\notes{For example:
- Activated clusters follow approximately deterministic trajectories — peaks in marginal distributions shift smoothly, like classical particles.
- Entropic forces emerge: systems tend to move toward configurations of greater curvature balance — analogous to energy minimisation.
- Memory effects appear: previous curvature structures condition the space of possible future moves, giving rise to path dependence and feedback.}

\notes{These features of classical behavior emerge naturally from the information geometry, without needing to postulate physical laws. This suggests that physics might be more fundamentally about information and geometry than we typically assume.}

\notes{In short, the system begins to behave classically — not because the quantum rules have been replaced, but because the wave structure is now so layered and entangled that only the most stable, large-scale patterns persist. Geometry still rules, but in a statistical form.}

\notes{Classical behavior emerges naturally from quantum-like behavior as the system becomes more complex. There's no need for a separate classical theory — it's just what happens when quantum systems get too complex to track in full.}

\subsubsection{Summary: From Curvature to Classicality}

\slides{
- Full arc: latent regime → variable activation → interaction onset → layered interaction → classical regime
- System evolves from unstructured entropy minimum to coarse but stable configuration
- What began as a game of curvature ends as a self-organized system with classical-like behavior
}

\notes{We have traced a full arc:

1. Latent regime: a symmetric, curvature-minimised wave equation governs the silent geometry of $M$-space.
2. Variable activation: entropy gradient breaks symmetry; a direction becomes resolvable, and a wave equation reappears — now active.
3. Interaction onset: new directions activate; wavefunctions couple; the Fisher matrix acquires off-diagonal structure; locality and joint dynamics emerge.
4. Layered interaction: subsystems form, interactions propagate, and a network of informational flow develops.
5. Classical regime: entropy dominates; interference fades; wave structure gives way to ensemble dynamics governed by effective constraints.}

\notes{This progression from latent to classical represents a natural pathway for the emergence of complexity. Each stage builds on the previous one, with new properties emerging that weren't present in earlier stages.}

\notes{Through this progression, the system evolves from an unstructured entropy minimum to a coarse but stable configuration governed by emergent geometry. What began as a game of curvature ends as a self-organised system with behaviour that mimics the laws of classical motion.}

\notes{This is the central thesis of the information game: that physical-like dynamics can emerge naturally from information geometry, without needing to postulate physical laws. The system's evolution from latent to classical is driven entirely by information-theoretic principles, yet it produces behavior that closely resembles what we observe in physical systems.}

\subsection{Example Concluded: Summary and Structural Integration}

\slides{
- Example illustrates core principles of the model
- Each stage instantiates foundational components
- System's dynamics are emergent in the strict sense
- Fisher Information Matrix acts as both memory and mediator
}

\notes{This extended example has traced the life cycle of a variable — from latent ambiguity to classical coherence — showing how internal information geometry governs the entire trajectory.}

\notes{This example serves as a concrete illustration of the abstract principles we've discussed. By following a single variable through its evolution, we can see how the information geometry shapes its behavior and how it interacts with other variables.}

Let's now step back and situate this narrative within the broader framework.

\paragraph{The Example as an Illustration of Core Principles}

\notes{Each stage of the unfolding process has instantiated one or more foundational components of the model:

| Stage | Structure | Governing Principle |
|-------|-----------|---------------------|
| Latent $M$-space | Minimal wave-like density | Fisher curvature minimisation under resolution constraint |
| Variable activation ($M \rightarrow X$) | Threshold-triggered flow | Entropic gradient ascent via $G(\boldsymbol{\theta}) \boldsymbol{\theta}$ |
| Coupling ($X \leftrightarrow Y$) | Off-diagonal curvature | Emergence of locality through statistical interaction |
| Network growth ($X,Y,Z,\dots$) | Layered curvature structure | Directed flow across the unfolding Fisher topology |
| Classical transition | Loss of coherence, coarse structure | Effective dynamics via ensemble geometry |
}

\notes{This table summarizes the key stages of the system's evolution, showing how each stage builds on the previous one and introduces new structure and dynamics.}

\notes{Each of these transitions is governed not by external forces or postulated laws, but by internal geometric conditions:
- Variance constraints impose curvature.
- Curvature shapes entropy gradients.
- Gradients activate variables.
- Activation reshapes the geometry.}

\notes{The system's evolution is driven entirely by internal geometric conditions, without needing external forces or postulated laws. This suggests that physical dynamics might be more fundamentally about information and geometry than we typically assume.}

\notes{The system's dynamics are emergent in the strict sense: each new layer of behaviour is conditioned by — but not reducible to — the previous one. The Fisher Information Matrix $G$ acts as both memory and mediator, encoding the system's informational shape at every stage.}

\notes{The Fisher Information Matrix plays a central role in the system's evolution. It not only defines the current geometry, but also remembers the system's history and mediates its future evolution. This suggests that information geometry might be more fundamental than we typically assume.}

\paragraph{The Role of the Example in the Larger Framework}

\notes{This example serves two roles

1. Didactic — it offers a concrete narrative that tracks the abstract constructions (curvature, emergence, locality) through a single evolving trajectory.
2. Structural — it demonstrates how local wave equations, variable activation, basis adaptation, and emergent constraints can be woven into a self-organising dynamics without invoking physical assumptions.}

\notes{This example is crucial for understanding the broader framework. It shows how the abstract principles translate into concrete system behavior, and how physical-like dynamics can emerge naturally from information geometry.}

\notes{We now return to the general framework, equipped with a working example of how internal information geometry generates unfolding structure. From here, we are ready to explore how these principles generalise — to multiple interacting subsystems, to emergent constraints across timescales, and to the geometry of coarse-grained laws.}

\endif
