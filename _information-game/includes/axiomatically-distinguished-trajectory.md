\ifndef{axiomaticallyDistinguishedTrajectory}
\define{axiomaticallyDistinguishedTrajectory}

\editme

\subsection{Axiomatically Distinguished Trajectory}

\notes{The information relaxation principle says the game evolves by maximising joint entropy production subject to the marginal entropy constraint $\sum_i h_i = C$. In natural parameter space the joint entropy gradient is
$$
\nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}.
$$
We enforce the constraint via a Lagrange multiplier $\nu(\tau)$, giving constrained dynamics
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} + \nu(\tau)\,\mathbf{a}(\boldsymbol{\theta}),
$$
where $\mathbf{a}(\boldsymbol{\theta}) = \nabla\!\sum_i h_i$ is the constraint gradient and $\nu(\tau)$ is determined by requiring $\mathbf{a}^\top\dot{\boldsymbol{\theta}} = 0$ (the constraint is maintained). Here $\tau$ is *game time*, the affine parameter tracking progress along the trajectory.}

\slidesincremental{
* Maximise $\dot{H}$ subject to $\sum_i h_i = C$
* Constrained dynamics:
$$\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} + \nu(\tau)\,\mathbf{a}(\boldsymbol{\theta})$$
* $\mathbf{a} = \nabla\sum_i h_i$: constraint gradient
* $\nu(\tau)$: Lagrange multiplier, determined by $\mathbf{a}^\top\dot{\boldsymbol{\theta}}=0$
}

\subsection{GENERIC-like Structure}

\notes{To understand the local structure of the dynamics we linearise around any point $\boldsymbol{\theta}^*$ on the constraint manifold. Writing $\mathbf{q} = \boldsymbol{\theta} - \boldsymbol{\theta}^*$, the linearised flow is
$$
\dot{\mathbf{q}} = M\mathbf{q} + O(\|\mathbf{q}\|^2), \qquad M = S + A,
$$
where $S = \tfrac{1}{2}(M + M^\top)$ is symmetric (positive-semidefinite) and $A = \tfrac{1}{2}(M - M^\top)$ is antisymmetric. The symmetric part drives entropy production; the antisymmetric part generates entropy-conserving, rotation-like redistribution of information. This decomposition is the GENERIC (General Equation for Non-Equilibrium Reversible--Irreversible Coupling) structure of @Grmela-dynamics97 and @Ottinger-beyond05, and it emerges automatically from the constraint geometry rather than being imposed by hand [@Lawrence-inaccessible25].}

\slides{
$$M = S + A, \qquad \dot{\mathbf{q}} = M\mathbf{q}$$

| Part | Type | Role |
|------|------|------|
| $S$ (symmetric) | Irreversible | Entropy production |
| $A$ (antisymmetric) | Reversible | Entropy-conserving rotation |

*Emerges from constraint geometry — not imposed*
}

\newslide{Thermodynamic vs Mechanical Regimes}

\notes{The ratio $\|A\|/\|S\|$ varies across the constraint manifold and determines the local character of the dynamics. When $\|S\| \gg \|A\|$ the system is in a thermodynamic regime: dissipation dominates and entropy is produced rapidly. When $\|A\| \gtrsim \|S\|$ the system is in a mechanical regime: conservative, rotation-like dynamics dominate. The information topography — the landscape of the Fisher information $G(\boldsymbol{\theta})$ — governs how these regimes are distributed.}

\slidesincremental{
* $\|S\| \gg \|A\|$: thermodynamic regime — rapid entropy production
* $\|A\| \gtrsim \|S\|$: mechanical regime — oscillatory, reversible
* Ratio $\|A\|/\|S\|$ varies across constraint manifold

*Fisher information $G(\boldsymbol{\theta})$ defines the information topography*
}

\subsection{Axiomatically Distinguished}

\notes{The direction of maximum entropy ascent is the unique steepest-ascent direction in the Fisher (Riemannian) metric. No external structure — no Hamiltonian, no clock, no spatial coordinates — is needed to specify it. The trajectory is *axiomatically distinguished*: uniquely identifiable from within the game's own axioms [@Lawrence-inaccessible25].}

\slides{
> A choice is axiomatically distinguished if it is uniquely identifiable within the game's axioms — without external structure such as Hamiltonians, clocks, or coordinates.

* Maximum entropy direction: unique in Fisher metric
* Constraint: marginal entropy conservation
* Together: unique trajectory through information geometry
}

\endif
