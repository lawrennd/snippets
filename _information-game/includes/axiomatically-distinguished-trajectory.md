\ifndef{axiomaticallyDistinguishedTrajectory}
\define{axiomaticallyDistinguishedTrajectory}

\editme

\subsection{Axiomatically Distinguished}

\notes{The direction of maximum entropy ascent is the unique steepest-ascent direction in the Fisher (Riemannian) metric. No external structure — no Hamiltonian, no clock, no spatial coordinates — is needed to specify it. The trajectory is *axiomatically distinguished*: uniquely identifiable from within the game's own axioms [@Lawrence-inaccessible25].}

\slides{
> A choice is axiomatically distinguished if it is uniquely identifiable within the game's axioms — without external structure such as Hamiltonians, clocks, or coordinates.
}

\newslide{Maximum Entropy Production}

\slides{
* Maximum entropy production: unique in Fisher metric
* Constraint: marginal entropy conservation
}

\notes{The information relaxation principle says the game evolves by maximising joint entropy production subject to the marginal entropy constraint $\sum_i h_i = C$. In natural parameter space the joint entropy gradient is
$$
\nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}.
$$
We enforce the constraint via a Lagrange multiplier $\nu(\tau)$, giving constrained dynamics
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} + \nu(\tau)\,\mathbf{a}(\boldsymbol{\theta}),
$$
where $\mathbf{a}(\boldsymbol{\theta}) = \nabla\!\sum_i h_i$ is the constraint gradient and $\nu(\tau)$ is determined by requiring $\mathbf{a}^\top\dot{\boldsymbol{\theta}} = 0$ (the constraint is maintained). Here $\tau$ is *game time*, the affine parameter tracking progress along the trajectory.}

\newslide{Maximum Entropy Production}

\slides{
Maximise
$$
\frac{\text{d}H}{\text{d}\tau}
$$
subject to $\sum_i h_i = C$
}

\subsection{GENERIC-like Structure}

\notes{To understand the local structure of the dynamics we linearise around any point $\boldsymbol{\theta}^*$ on the constraint manifold. Writing $\mathbf{q} = \boldsymbol{\theta} - \boldsymbol{\theta}^*$, the linearised flow is
$$
\dot{\mathbf{q}} = M\mathbf{q} + O(\|\mathbf{q}\|^2), \qquad M = S + A,
$$
where $S = \tfrac{1}{2}(M + M^\top)$ is symmetric (positive-semidefinite) and $A = \tfrac{1}{2}(M - M^\top)$ is antisymmetric. The symmetric part drives entropy production; the antisymmetric part generates entropy-conserving, rotation-like redistribution of information. This decomposition is the GENERIC (General Equation for Non-Equilibrium Reversible--Irreversible Coupling) structure of @Grmela-dynamics97 and @Ottinger-beyond05, and it emerges automatically from the constraint geometry rather than being imposed by hand [@Lawrence-inaccessible25].}

\slides{
* Linearise around $\boldsymbol{\theta}^*$
* $\mathbf{q} = \boldsymbol{\theta} - \boldsymbol{\theta}^*$
}
\newslide{Linearised Flow}

\slides{
$$\dot{\mathbf{q}} = M\mathbf{q}$$
where $M = S + A$

* $S$ is symmetric and irreversible (entropy production)
* *$A$ is antisymmetric and reversible (entropy-conserving)
}

\notes{The ratio $\|A\|/\|S\|$ varies across the constraint manifold and determines the local character of the dynamics. When $\|S\| \gg \|A\|$ the system is in a thermodynamic regime: dissipation dominates and entropy is produced rapidly. When $\|A\| \gtrsim \|S\|$ the system is in a mechanical regime: conservative, rotation-like dynamics dominate. The information topography — the landscape of the Fisher information $G(\boldsymbol{\theta})$ — governs how these regimes are distributed.}

\endif
