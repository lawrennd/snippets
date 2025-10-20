\ifndef{lagrangeMultipliersReview}
\define{lagrangeMultipliersReview}

\editme

\subsection{Lagrange Multipliers: A Primer}

\notes{In Lecture 3, we derived the maximum entropy production dynamics $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}$ and noted this assumes the system structure automatically preserves marginal entropies. For more general cases, we need to **explicitly enforce** the conservation constraint $\sum h_i = C$.

This is where Lagrange multipliers come in. Lagrange multipliers are a standard technique from constrained optimisation that we'll adapt to constrained dynamics.}

\slides{
**Problem from Lecture 3:**

* Dynamics: $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}$
* Assumes marginal entropy conservation "just works"
* Need general framework for explicit constraints

**Solution:** Lagrange multipliers
}

\subsection{Review: Constrained Optimisation}

\notes{Consider a simple optimisation problem:
$$
\text{minimize } f(\mathbf{x}) \text{ subject to } g(\mathbf{x}) = c
$$

The Lagrangian method introduces an auxiliary variable $\lambda$ (the Lagrange multiplier)
$$
\mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) + \lambda(g(\mathbf{x}) - c).
$$
At the optimum, both conditions must hold,
\begin{align}
\nabla_{\mathbf{x}} \mathcal{L} &= \nabla f + \lambda \nabla g = 0 \\
\frac{\partial \mathcal{L}}{\partial \lambda} &= g(\mathbf{x}) - c = 0.
\end{align}
The first equation says: the gradient of $f$ must be perpendicular to the constraint surface (pointing along $\nabla g$). The second equation enforces the constraint itself.}

\slides{
**Standard Lagrange Multipliers:**
$$
\mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) + \lambda(g(\mathbf{x}) - c)
$$

**Optimality conditions:**

* $\nabla f + \lambda \nabla g = 0$ (gradient perpendicular to constraint)
* $g(\mathbf{x}) = c$ (constraint satisfied)
}

\newslide{Geometric Interpretation}

\notes{The key geometric insight is that at a constrained optimum the gradient of the objective function must be perpendicular to the constraint surface. If it isn't, we could move along the constraint surface to improve the objective.

Think of climbing a hill i.e. (maximise elevation $f$) while staying on a path (constraint $g = c$). At the highest point on the path, the elevation gradient points off the path, perpendicular to it.}

\slides{
**Geometric Picture:**

*Gradient $\nabla f$ perpendicular to constraint surface*

* If not perpendicular → could improve $f$ while staying on constraint
* Multiplier $\lambda$ measures "strength" of constraint
}

\subsection{From Optimisation to Dynamics}

\notes{For The Inaccessible Game, we're not solving a static optimization problem, we want **dynamics** that continuously maintain a constraint. 

Consider evolving parameters $\boldsymbol{\theta}(t)$ subject to:
$$
\sum_{i=1}^N h_i(\boldsymbol{\theta}(t)) = C \quad \text{for all } t
$$

Taking the time derivative
$$
\frac{\text{d}}{\text{d}t}\left(\sum_{i=1}^N h_i\right) = \sum_{i=1}^N \nabla_{\boldsymbol{\theta}} h_i \cdot \dot{\boldsymbol{\theta}} = a(\boldsymbol{\theta})^\top \dot{\boldsymbol{\theta}} = 0,
$$
where we've defined the **constraint gradient**:
$$
a(\boldsymbol{\theta}) := \sum_{i=1}^N \nabla_{\boldsymbol{\theta}} h_i(\boldsymbol{\theta}).
$$
This is an *implicit constraint*: if we start on the constraint manifold ($\sum h_i = C$) and ensure $a^\top \dot{\boldsymbol{\theta}} = 0$, we stay on the manifold forever.}

\slides{
**Constraint Maintenance:**
$$
\sum h_i(\boldsymbol{\theta}(t)) = C \quad \forall t
$$

**Implicit form:**
$$
a(\boldsymbol{\theta})^\top \dot{\boldsymbol{\theta}} = 0
$$

where $a(\boldsymbol{\theta}) = \sum_i \nabla h_i$

*Stay on constraint surface by moving tangent to it*
}

\subsection{Tangent Space Projection}

\notes{The constraint $a^\top \dot{\boldsymbol{\theta}} = 0$ says we must move **tangent** to the constraint manifold. We can decompose any vector into components parallel and perpendicular to $a$:

**Perpendicular (normal) component:**
$$
v_\perp = \frac{a a^\top}{\|a\|^2} v = \frac{aa^\top}{a^\top a} v
$$

**Parallel (tangent) component:**
$$
v_\parallel = v - v_\perp = \left(I - \frac{aa^\top}{a^\top a}\right) v =: \Pi_\parallel v
$$

The matrix $\Pi_\parallel = I - \frac{aa^\top}{a^\top a}$ is the *tangent space projector*. It ensures any dynamics stay on the constraint manifold.

The tangent space projector has the following properties.

1. **Kills normal component**: $\Pi_\parallel a = 0$, meaning it projects out any component along the constraint gradient
2. **Idempotent**: $\Pi_\parallel^2 = \Pi_\parallel$, meaning applying it twice is the same as applying it once
3. **Preserves tangent vectors**: If $a^\top v = 0$ (i.e., $v$ is already tangent), then $\Pi_\parallel v = v$

These properties ensure that $\Pi_\parallel$ acts as a true projection operator onto the tangent space of the constraint manifold.}

\slides{
**Tangent Space Projector:**
$$
\Pi_\parallel = I - \frac{aa^\top}{a^\top a}
$$

**Properties:**

* $\Pi_\parallel a = 0$ (kills normal component)
* $\Pi_\parallel^2 = \Pi_\parallel$ (idempotent)
* If $a^\top v = 0$ then $\Pi_\parallel v = v$

*Projects any vector onto tangent space*
}

\subsection{Lagrangian for Dynamics}

\notes{For The Inaccessible Game, we want to maximize entropy $H$ while conserving marginal entropies. The Lagrangian is
$$
\mathcal{L}(\boldsymbol{\theta}, \nu) = -H(\boldsymbol{\theta}) + \nu\left(\sum_{i=1}^N h_i(\boldsymbol{\theta}) - C\right).
$$
We use $-H$ because by convention Lagrangians are minimised. The Lagrange multiplier $\nu$ (we use $\nu$ instead of $\lambda$ to avoid confusion with eigenvalues) enforces the constraint.

Recall that $I + H = C$, so maximising $H$ is equivalent to minimising multi-information $I$. We could  write the Lagrangian as
$$
\mathcal{L}(\boldsymbol{\theta}, \nu) = I(\boldsymbol{\theta}) + \nu\left(\sum_{i=1}^N h_i(\boldsymbol{\theta}) - C\right).
$$
This makes explicit the information relaxation picture: we're minimising correlation structure (multi-information) subject to the conservation constraint.

The key difference from static optimisation: *$\nu$ becomes a function of time*, $\nu(t)$. It adjusts dynamically to keep the system on the constraint manifold as it evolves.}

\slides{
**Information Lagrangian:**
$$
\mathcal{L}(\boldsymbol{\theta}, \nu) = -H(\boldsymbol{\theta}) + \nu\left(\sum h_i - C\right)
$$

* $-H$: Minimize negative entropy = maximize entropy
* $\nu$: Lagrange multiplier (time-dependent!)
* Constraint: $\sum h_i = C$

*$\nu(t)$ adjusts to maintain constraint during evolution*
}

\subsection{Constrained Gradient Flow}

\notes{Taking the gradient of the Lagrangian with respect to $\boldsymbol{\theta}$:
$$
\nabla_{\boldsymbol{\theta}} \mathcal{L} = -\nabla H + \nu \sum_{i=1}^N \nabla h_i = -\nabla H + \nu a(\boldsymbol{\theta})
$$

For maximum entropy production under the constraint, we follow (negative) gradient flow:
$$
\dot{\boldsymbol{\theta}} = -\nabla_{\boldsymbol{\theta}} \mathcal{L} = \nabla H - \nu a(\boldsymbol{\theta})
$$

Recall that for exponential families, $\nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}$. This gives
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(t) a(\boldsymbol{\theta}).
$$
This is the *constrained information dynamics**. The first term drives entropy increase. The second term (the "constraint force") keeps us on the manifold $\sum h_i = C$.}

\slides{
**Constrained Dynamics:**
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(t) a(\boldsymbol{\theta})
$$

* First term: MEP (entropy increase)
* Second term: Constraint force (maintains $\sum h_i = C$)
* $\nu(t)$: Adjusts to enforce constraint

*Two competing forces: increase entropy vs. stay on manifold*
}

\newslide{Why Constraint Maintenance Works}

\notes{Let's verify this dynamics maintains the constraint. Take the time derivative of $\sum h_i$,
$$
\frac{\text{d}}{\text{d}t}\left(\sum h_i\right) = a^\top \dot{\boldsymbol{\theta}} = a^\top(-G\boldsymbol{\theta} - \nu a)
$$

We need this to be zero. Solving for $\nu$ we have,
$$
a^\top(-G\boldsymbol{\theta} - \nu a) = 0 \implies \nu = -\frac{a^\top G\boldsymbol{\theta}}{a^\top a}.
$$
This means that $\nu(t)$ is completely determined by requiring constraint maintenance. We don't choose it arbitrarily, the marginal information conservation constraint itself dictates its value at each moment.

Substituting back
$$
\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta} + \frac{a^\top G\boldsymbol{\theta}}{a^\top a} a = -\left(I - \frac{aa^\top}{a^\top a}\right)G\boldsymbol{\theta} = -\Pi_\parallel G\boldsymbol{\theta}.
$$
The dynamics are the entropy gradient *projected onto the tangent space* of the constraint manifold.}

\slides{
**Constraint Maintenance:**

Require: $a^\top \dot{\boldsymbol{\theta}} = 0$

$$
\nu(t) = -\frac{a^\top G\boldsymbol{\theta}}{a^\top a}
$$

**Result:**
$$
\dot{\boldsymbol{\theta}} = -\Pi_\parallel G\boldsymbol{\theta}
$$

*Projected entropy gradient stays on manifold*
}

\subsection{Summary: Lagrangian Formulation}

\notes{The Lagrangian approach to constrained information dynamics gives us:

1. **Constraint**: $\sum h_i(\boldsymbol{\theta}) = C$ maintained for all time
2. **Lagrangian**: $\mathcal{L} = -H + \nu(\sum h_i - C)$
3. **Dynamics**: $\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta} - \nu a$
4. **Multiplier**: $\nu(t) = -\frac{a^\top G\boldsymbol{\theta}}{a^\top a}$ (determined by constraint)
5. **Geometric picture**: Projected gradient flow $\dot{\boldsymbol{\theta}} = -\Pi_\parallel G\boldsymbol{\theta}$

This framework can handle any constraint of the form $g(\boldsymbol{\theta}) = c$ as the same maths would apply. For The Inaccessible Game, the specific constraint is marginal entropy conservation.

In the next sections, we'll explore the properties of $\nu(t)$, how it evolves, what it represents physically, and what happens at stationary points where $\dot{\boldsymbol{\theta}} = 0$.}

\slides{
**Key Results:**

* Constrained dynamics: $\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta} - \nu a$
* Multiplier: $\nu = -\frac{a^\top G\boldsymbol{\theta}}{a^\top a}$ (automatic!)
* Geometric: $\dot{\boldsymbol{\theta}} = -\Pi_\parallel G\boldsymbol{\theta}$ (projected)

**Next:** Properties of $\nu(t)$ and equilibria
}

\endif

