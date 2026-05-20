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

\endif
