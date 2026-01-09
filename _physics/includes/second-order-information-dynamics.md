\ifndef{secondOrderInformationDynamics}
\define{secondOrderInformationDynamics}

\editme

\subsection{Second-Order Dynamics Near Equilibrium}

\notes{From Lecture 6, we derived the linearised dynamics near an equilibrium point $\boldsymbol{\theta}^\ast$
$$
\dot{q} = Mq,
$$
where $q = \boldsymbol{\theta} - \boldsymbol{\theta}^\ast$ is a small perturbation and
$$
M = -G - \nu^\ast A + \frac{aa^\top G}{\|a\|^2}.
$$
But what is the *leading-order* behavior? Let's look more carefully at the perturbation expansion of the constrained dynamics.}

\slides{
**Recall from Lecture 6**

Linearised dynamics: $\dot{q} = Mq$

Matrix
$$
M = -G - \nu^\ast A + \frac{aa^\top G}{\|a\|^2}
$$

**Question:** What happens at leading order?
}

\subsection{The Perturbation Expansion}

\notes{The constrained maximum entropy production dynamics are
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(t) a(\boldsymbol{\theta}),
$$
where $\nu(t)$ enforces the tangency condition $a(\boldsymbol{\theta})^\top \dot{\boldsymbol{\theta}} = 0$.

Near equilibrium, we expand to different orders in $\|q\| = \|\boldsymbol{\theta} - \boldsymbol{\theta}^\ast\|$.

**Define the reduced field on the constraint manifold:**
$$
F(\boldsymbol{\theta}) = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(\boldsymbol{\theta}) a(\boldsymbol{\theta}),
$$
where $\nu(\boldsymbol{\theta})$ is chosen such that $a(\boldsymbol{\theta})^\top F(\boldsymbol{\theta}) = 0$ (tangency).

At $\boldsymbol{\theta} = \boldsymbol{\theta}^\ast + q$, the Taylor expansion gives:
$$
F(\boldsymbol{\theta}^\ast + q) = \Pi_\parallel S q + \mathcal{B}(q) + O(\|q\|^3)
$$
where

- $\Pi_\parallel = I - \frac{aa^\top}{\|a\|^2}$ projects onto the constraint tangent space
- $S = \nabla^2 \mathcal{L}|_{\boldsymbol{\theta}^\ast,\nu^\ast}$ is the Hessian of the Lagrangian (symmetric matrix)
- $\mathcal{B}(q) = O(\|q\|^2)$ contains quadratic corrections}

\slides{
**Perturbation Expansion**

Reduced field: $F(\boldsymbol{\theta}) = -G\boldsymbol{\theta} - \nu a$

At $\boldsymbol{\theta} = \boldsymbol{\theta}^\ast + q$
$$
F(\boldsymbol{\theta}^\ast + q) = \Pi_\parallel S q + \mathcal{B}(q) + O(\|q\|^3)
$$

* $S = \nabla^2 \mathcal{L}$ (symmetric)
* $\mathcal{B}(q) = O(\|q\|^2)$ (quadratic corrections)
}

\subsection{Second-Order: Pure Dissipation}

\notes{**Key insight:** At second order (linear in $q$), the dynamics are
$$
\dot{q} \approx \Pi_\parallel S q.
$$
Crucially, $S$ is a **symmetric matrix**. This means the leading-order dynamics are purely dissipative.

**Entropy production:** The rate of change of joint entropy is
$$
\dot{H} = -\boldsymbol{\theta}^\top G \boldsymbol{\theta} \approx -q^\top S q + O(\|q\|^3)
$$
Since $S$ is symmetric, $q^\top S q$ is a quadratic form. For a stable equilibrium, $S$ is negative definite (or negative semidefinite on the tangent space), so:
$$
\dot{H} = -q^\top S q \geq 0
$$
This is *entropy production*, the system dissipates toward equilibrium, consistent with the second law of thermodynamics.

**No conservative dynamics yet:** At this order, there are no rotations, no Hamiltonian flow, no energy-conserving oscillations. Only dissipation toward the equilibrium.}

\slides{
**Leading Order: Purely Symmetric**

$$
\dot{q} \approx \Pi_\parallel S q
$$

**Properties:**
* $S$ symmetric $\rightarrow$ purely dissipative
* Entropy production: $\dot{H} \approx -q^\top S q \geq 0$
* No conservative/Hamiltonian component
* Consistent with second law

**Physical picture:** Relaxation toward equilibrium
}

\subsection{Why Is This the Gaussian Regime?}

\notes{The second-order approximation corresponds to the **Gaussian regime** we discussed in the last lecture.

In a Gaussian distribution:
- All cumulants of order 3 and higher vanish
- The dynamics are completely determined by the covariance (Fisher information $G$)
- The perturbation expansion truncates at second order

So when we say "near equilibrium in the Gaussian regime," we mean:
1. Small perturbations ($\|q\| \ll 1$)
2. The distribution is approximately Gaussian (third and higher cumulants negligible)
3. The dynamics are well-approximated by $\dot{q} \approx \Pi_\parallel S q$

This is the Laplace approximation: near any stationary point, a distribution looks approximately Gaussian, and we can analyze stability using second-order (quadratic) information.}

\slides{
**Connection to Gaussian Regime**

Gaussian distribution:
* All cumulants $\geq 3$ vanish
* Dynamics fully determined by $G$ (covariance)
* Expansion truncates at second order

**Laplace approximation:**
* Near equilibrium ≈ Gaussian
* Stability from second-order analysis
* Justifies linear perturbation theory
}

\subsection{Stability Analysis}

\notes{The eigenvalues of $\Pi_\parallel S \Pi_\parallel$ (restricted to the tangent space) determine stability:

**Stable equilibrium:** All eigenvalues have negative real parts
- Perturbations decay exponentially
- System returns to $\boldsymbol{\theta}^\ast$

**Unstable equilibrium:** At least one eigenvalue has positive real part
- Perturbations grow
- System moves away from $\boldsymbol{\theta}^\ast$

**Marginal stability:** Some eigenvalues are zero
- Slow modes or conservation laws
- Need higher-order analysis

At second order, with $S$ symmetric, all eigenvalues are *real*. There are no imaginary parts, hence no oscillations, just exponential growth or decay.}

\slides{
**Stability from $\Pi_\parallel S \Pi_\parallel$**

Eigenvalues determine behavior:

* Negative $\rightarrow$ stable (decay)
* Positive $\rightarrow$ unstable (growth)
* Zero $\rightarrow$ marginal (slow modes)

**Second-order:** All eigenvalues real
* No oscillations
* Pure exponential dynamics
}

\notes{**Summary:** At second order (Gaussian regime), the dynamics near equilibrium are purely dissipative. The symmetric matrix $S$ drives entropy production and relaxation toward equilibrium. This is standard perturbation theory, but it's not the full story. In the next section, we'll see how non-Gaussian effects and constraint geometry introduce conservative dynamics at higher order.

**Note on locality:** This analysis is a local linearisation around a reference point (typically, but not necessarily, an equilibrium). For general systems, the matrices $S$, $A$, and $M$ vary with position on the manifold as both the Fisher information $G(\boldsymbol{\theta})$ and the constraint gradient $a(\boldsymbol{\theta})$ depend on $\boldsymbol{\theta}$. The GENERIC decomposition applies locally at each point, revealing how the balance between dissipative and conservative dynamics varies across parameter space.}

\endif

\endif
