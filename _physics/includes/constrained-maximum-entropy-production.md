\ifndef{constrainedMaximumEntropyProduction}
\define{constrainedMaximumEntropyProduction}

\editme

\subsection{Constrained Maximum Entropy Production}

\notes{We've established that $I + H = C$ must be conserved, and that the system naturally evolves toward higher entropy. But *how* does it evolve? What determines the specific path through information space?}

\notes{Our answer comes from an *information relaxation principle*: of all paths that conserve $\sum_i h_i = C$, the system follows the one that maximizes entropy production $\dot{H}$.}

\slides{
**Information Relaxation Principle:**

Among all paths with $\sum h_i = C$:

$$\text{Follow path that maximizes } \dot{H}$$

*Steepest entropy ascent on constraint surface*
}

\subsection{Unconstrained vs Constrained Dynamics}

\notes{Without the constraint, maximum entropy production would simply be gradient ascent on $H$. For exponential families, the entropy gradient is
$$
\nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}
$$
where $G = \nabla^2\cumulantGeneratingFunction$ is the Fisher information. Pure MEP would give:
$$
\dot{\boldsymbol{\theta}} = \nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}.
$$}

\notes{This is the natural gradient flow in the information geometry. The system would flow toward the maximum entropy state at $\boldsymbol{\theta} = \mathbf{0}$.}

\slides{
**Unconstrained MEP:**

$$\dot{\boldsymbol{\theta}} = \nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}$$

* Natural gradient ascent
* Flows to $\boldsymbol{\theta} = \mathbf{0}$ (max entropy)
* No constraint enforcement
}

\newslide{Adding the Constraint}

\notes{But we must respect $\sum_i h_i = C$ at all times. This constraint defines a manifold in parameter space. We need to project the MEP flow onto the tangent space of this constraint manifold.}

\notes{Using a Lagrangian formulation:
$$
\mathscr{L}(\boldsymbol{\theta}, \nu) = -H(\boldsymbol{\theta}) + \nu\left(\sum_{i=1}^n h_i - C\right)
$$
where $\nu$ is a Lagrange multiplier (note we use $-H$ since Lagrangians are minimized by convention).}

\slides{
**Lagrangian Formulation:**

$$\mathscr{L}(\boldsymbol{\theta}, \nu) = -H + \nu\left(\sum h_i - C\right)$$

* $\nu$: Lagrange multiplier
* Enforces constraint
* Projects onto tangent space
}

\subsection{The Constrained Dynamics}

\notes{The constrained dynamics become:
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} + \nu(\tau) \mathbf{a}(\boldsymbol{\theta})
$$
where $\mathbf{a}(\boldsymbol{\theta}) = \sum_i \nabla h_i(\boldsymbol{\theta})$ is the constraint gradient and $\tau$ is "game time" parametrising the trajectory.}

\notes{The Lagrange multiplier $\nu(\tau)$ is *time-dependent*, it varies along the trajectory to maintain the constraint. Since the constraint must be satisfied at all times:
$$
\frac{\text{d}}{\text{d}\tau}\left(\sum_i h_i\right) = 0
$$
we can use the chain rule:
$$
\mathbf{a}(\boldsymbol{\theta})^\top \dot{\boldsymbol{\theta}} = 0.
$$}

\slides{
**Constrained Dynamics:**

$$\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta} + \nu(\tau) \mathbf{a}$$

where $\mathbf{a} = \nabla\left(\sum_i h_i\right)$

**Constraint maintenance:**
$$\mathbf{a}^\top \dot{\boldsymbol{\theta}} = 0$$
}

\subsection{Solving for the Lagrange Multiplier}

\notes{Substituting the dynamics into the constraint maintenance condition:
$$
\mathbf{a}^\top\left(-G\boldsymbol{\theta} + \nu \mathbf{a}\right) = 0
$$
we can solve for $\nu$:
$$
\nu(\tau) = \frac{\mathbf{a}^\top G\boldsymbol{\theta}}{\|\mathbf{a}\|^2}.
$$}

\notes{This allows us to write the dynamics in projection form:
$$
\dot{\boldsymbol{\theta}} = -\Pi_\parallel G\boldsymbol{\theta}
$$
where
$$
\Pi_\parallel = \mathbf{I} - \frac{\mathbf{a}\mathbf{a}^\top}{\|\mathbf{a}\|^2}
$$
is the projection matrix onto the constraint tangent space.}

\slides{
**Solution:**

$$\nu(\tau) = \frac{\mathbf{a}^\top G\boldsymbol{\theta}}{\|\mathbf{a}\|^2}$$

**Projection Form:**

$$\dot{\boldsymbol{\theta}} = -\Pi_\parallel G\boldsymbol{\theta}$$

where $\Pi_\parallel$ projects onto tangent space
}

\subsection{Physical Interpretation}

\notes{This has a nice physical interpretation.

- **$-G\boldsymbol{\theta}$:** The "natural" direction to maximise entropy
- **$\nu \mathbf{a}$:** The "constraint force" that keeps the system on the manifold
- **$\nu(\tau)$:** Measures how much the natural flow "wants" to leave the constraint surface

When $\nu \approx 0$, the constraint gradient is nearly orthogonal to the flow, i.e. the system is naturally moving along the constraint surface. When $|\nu|$ is large, the natural flow is trying to leave the surface and significant constraint force is needed to keep it on track.}

\slides{
**Physical Picture:**

* $-G\boldsymbol{\theta}$: natural entropy gradient
* $\nu\mathbf{a}$: constraint force
* $\nu$ small: flow naturally tangent
* $\nu$ large: flow fights constraint

*Balance between geometry and constraint*
}

\notes{As we'll see next, this tension between the information geometry and the constraint structure is what generates the GENERIC-like decomposition into dissipative and conservative parts.}

\endif
\endif
