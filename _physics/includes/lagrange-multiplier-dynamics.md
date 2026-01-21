\ifndef{lagrangeMultiplierDynamics}
\define{lagrangeMultiplierDynamics}

\editme

\subsection{Dynamics of the Lagrange Multiplier $\nu(t)$}

\notes{We've seen that the Lagrange multiplier is determined by the constraint
$$
\nu(t) = -\frac{a(\boldsymbol{\theta})^\top G(\boldsymbol{\theta})\boldsymbol{\theta}}{a(\boldsymbol{\theta})^\top a(\boldsymbol{\theta})},
$$
where $a(\boldsymbol{\theta}) = \sum_i \nabla h_i(\boldsymbol{\theta})$ is the constraint gradient. But what does $\nu(t)$ represent physically? How does it evolve? And what determines its value?}

\slides{
**Lagrange Multiplier:**
$$
\nu(t) = -\frac{a^\top G\boldsymbol{\theta}}{a^\top a}
$$

**Questions:**

* What does $\nu$ represent?
* How does it evolve?
* What controls its magnitude?
}

\subsection{Physical Interpretation of $\nu$}

\notes{Lagrange multipliers such as $\nu(t)$ can have several interpretations

**1. Constraint force magnitude**: Recall the dynamics:
$$
\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta} - \nu a
$$
The term $\nu a$ is a force along the constraint normal direction. The magnitude $|\nu|$ tells us how strongly the constraint is pulling against the entropy-driven flow.

**2. Shadow price**: In economics, Lagrange multipliers represent "shadow prices", the marginal cost of tightening a constraint. Here, $\nu$ measures how much entropy production we "sacrifice" to maintain marginal entropy conservation. In Amazon such shadow prices represented, e.g. the cost per unit of new fulfilment centre construction.

**3. Tension in the system**: When $\nu$ is large, the constraint is "fighting" hard against the natural entropy flow. When $\nu$ is small, the entropy flow is nearly compatible with the constraint.}

\slides{
**Three Interpretations:**

1. **Constraint force**: Magnitude of $-\nu a$ term
2. **Shadow price**: Cost of enforcing constraint
3. **Tension**: How hard constraint "pulls"

*All equivalent—different physical pictures*
}

\subsection{Evolution of $\nu(t)$}

\notes{Since $\nu$ depends on $\boldsymbol{\theta}(t)$, $G(\boldsymbol{\theta}(t))$, and $a(\boldsymbol{\theta}(t))$, it evolves implicitly as the system moves,
$$
\dot{\nu} = \frac{\text{d}}{\text{d}t}\left(-\frac{a^\top G\boldsymbol{\theta}}{a^\top a}\right).
$$
This is complicated because all three components change. But we can understand the behavior qualitatively.

**When $|\nu|$ is large**: The constraint is strongly active. The entropy gradient has a large component perpendicular to the constraint surface, so significant "force" is needed to project it back.

**When $|\nu|$ is small**: The entropy gradient is nearly tangent to the constraint surface already. The system is "naturally" moving in a constraint-compatible direction.

**When $|\nu| = 0$**: Special case, see the next section on stationary points.}

\slides{**Evolution:**
$$
\dot{\nu} = \frac{\text{d}}{\text{d}t}\left(-\frac{a^\top G\boldsymbol{\theta}}{a^\top a}\right)
$$

* $|\nu|$ large: Constraint strongly active
* $|\nu|$ small: Nearly compatible flow
* $\nu = 0$: Stationary point (equilibrium)
}

\subsection{Geometric Picture: Angle Between Gradients}

\notes{A useful geometric picture: $\nu$ is related to the angle between $-G\boldsymbol{\theta}$ (the unconstrained entropy gradient) and the constraint surface.

Consider the projection formula:
$$
\nu = -\frac{a^\top G\boldsymbol{\theta}}{a^\top a}
$$

The numerator $a^\top G\boldsymbol{\theta}$ is the component of $-G\boldsymbol{\theta}$ perpendicular to the constraint surface (along $a$). The denominator $a^\top a = |a|^2$ normalizes by the constraint gradient magnitude.

So
$$
\nu = -\frac{\|-G\boldsymbol{\theta}\| \cos\theta}{\|a\|},
$$
where $\theta$ is the angle between $-G\boldsymbol{\theta}$ and $a$.

**When the angle is small** ($\cos\theta \approx 1$): The entropy gradient points nearly along the constraint normal. We need large $|\nu|$ to redirect it.

**When the angle is near $90^\degrees$** ($\cos\theta \approx 0$): The entropy gradient is nearly tangent already. Small $|\nu|$ suffices.}

\slides{
**Geometric Formula:**
$$
\nu \propto -\frac{\cos\theta}{\|a\|}
$$
where $\theta$ = angle between $-G\boldsymbol{\theta}$ and $a$

* Small angle: Entropy pulls off surface $\rightarrow$ large $|\nu|$
* Near 90°: Entropy tangent to surface $\rightarrow$ small $|\nu|$
}

\subsection{Computing $\nu(t)$ in Practice: A Major Computational Challenge}

\notes{To compute $\nu(t)$ at any moment, we need three ingredients:

1. **Current parameters** $\boldsymbol{\theta}(t)$

2. **Fisher information** $G(\boldsymbol{\theta})$

3. **Constraint gradient** $a(\boldsymbol{\theta}) = \sum_i \nabla h_i(\boldsymbol{\theta})$

**The computational nightmare**: Computing $\nabla h_i$ is horrifically difficult for general distributions. Each marginal entropy $h_i$ requires:
$$
h_i = -\sum_{x_i} p_i(x_i) \log p_i(x_i), \quad p_i(x_i) = \sum_{x_{\neg i}} p(\mathbf{x}|\boldsymbol{\theta})
$$
This marginalisation over $N-1$ variables is at worst case *exponentially expensive* in the system size. For $N$ binary variables, each marginal requires summing over $2^{N-1}$ configurations.

Then the gradient
$$
\nabla_{\boldsymbol{\theta}} h_i = -\mathbb{E}_{\boldsymbol{\theta}}\left[(T(X) - \boldsymbol{\mu}(\boldsymbol{\theta})) \log p_i(X_i|\boldsymbol{\theta})\right]
$$
involves expectations of log marginals, which themselves required exponentially many operations to compute.

Let's contrast this with the type of constraints we find in classical mechanics. There energy conservation constraints are typically *linear* or at most quadratic,
$$
E = \frac{1}{2}m\mathbf{v}^2 + V(\mathbf{x}) = \text{const}
$$
Computing $\nabla E$ is trivial rather than computing $\nabla(\sum h_i)$ requires potentially exponentially complex marginalisations. 

The solution is to explore the *Gaussian* regime. When marginals are approximately Gaussian with variance $\sigma_i^2$:
$$
\nabla_{\boldsymbol{\theta}} h_i \approx \frac{1}{2\sigma_i^2} \text{cov}_{\boldsymbol{\theta}}[(X_i - \mu_i)^2, T(X)]
$$
This is tractable because Gaussian marginals have closed-form expressions. For Gaussians, the covariance matrix $\Sigma = G^{-1}$ and:
$$
h_i = \frac{1}{2}\log(2\pi e \Sigma_{ii}) = \frac{1}{2}\log(2\pi e [G^{-1}]_{ii})
$$
We can compute $\nabla h_i$ by differentiating this expression, that's still nontrivial, but polynomial rather than exponential in complexity.

What gives us any hope that such an approximation should work? Well the Gaussian distribution is the maximum entropy distribution for distributions with finite variance. So it may be that the maximum entropy dynamics lead us to such regimes.

THh bottom line is that we really only have hope of computing $\nu(t)$ in special regimes like Gaussian distributions or systems with strong independence structure. For general high-dimensional exponential families, the constraint is computationally intractable.}

\slides{
**Computing $\nu$: Exponentially Hard!**

Need $a = \sum_i \nabla h_i$ where each $h_i$ requires marginalizing $N-1$ variables

* $N$ binary variables → $2^{N-1}$ operations per marginal!
* Classical mechanics: $\nabla E$ is trivial (linear/quadratic)
* Information: $\nabla(\sum h_i)$ is exponentially expensive

**Only tractable in:**
* Gaussian regime (closed form)
* Strong independence structure

*Nonlinear constraints are much harder than linear ones*
}

\subsection{Example: Simple Two-Variable System}

\notes{Consider a system with two binary variables $X_1, X_2$ with natural parameters $\boldsymbol{\theta} = (\theta_1, \theta_2, \theta_{12})$ for the marginals and interaction.

The constraint is $h_1 + h_2 = C$. Near independence, the constraint gradient simplifies:
$$
a \approx \left(\frac{\partial h_1}{\partial \theta_1}, \frac{\partial h_2}{\partial \theta_2}, 0\right)
$$

The interaction parameter $\theta_{12}$ doesn't directly affect marginal entropies (to first order), so the constraint is "slack" in that direction.

The Fisher information for a bivariate Bernoulli is
$$
G = \begin{pmatrix}
p_1(1-p_1) & p_{12} - p_1p_2 & \ldots \\
p_{12} - p_1p_2 & p_2(1-p_2) & \ldots \\
\vdots & \vdots & \ddots
\end{pmatrix}.
$$
Computing $\nu$ explicitly requires evaluating $a^\top G\boldsymbol{\theta} / a^\top a$ with these specific forms. The key insight: $\nu$ will be large when the marginals are changing rapidly (large $|\partial h_i/\partial \theta_i|$) and small when they're nearly constant.}

\slides{
**Two-Variable Example:**

* Parameters: $(\theta_1, \theta_2, \theta_{12})$
* Constraint: $h_1 + h_2 = C$
* Gradient: $a \approx (\partial h_1/\partial\theta_1, \partial h_2/\partial\theta_2, 0)$

*Interaction $\theta_{12}$ is "unconstrained" direction*

$\nu$ large when marginals changing fast
}

\subsection{Sign of $\nu$ and Direction of Constraint Force}

\notes{The sign of $\nu$ tells us the direction of the constraint force relative to the entropy gradient.

$$
\nu = -\frac{a^\top G\boldsymbol{\theta}}{a^\top a}
$$

**If $\nu > 0$**: The constraint force $-\nu a$ points opposite to $a$, meaning it reduces marginal entropies. This happens when the unconstrained entropy flow would increase $\sum h_i$ beyond $C$.

**If $\nu < 0$**: The constraint force $-\nu a$ points along $a$, increasing marginal entropies. This happens when the unconstrained flow would decrease $\sum h_i$ below $C$.

**If $\nu = 0$**: No constraint force needed, we're at a stationary point.

The constraint acts like a spring: it pulls back when you try to leave the manifold, but doesn't care which direction you move along it.}

\slides{
**Sign of $\nu$:**

* $\nu > 0$: Force opposes increasing $\sum h_i$
* $\nu < 0$: Force opposes decreasing $\sum h_i$
* $\nu = 0$: Stationary point (no force needed)

*Constraint maintains $\sum h_i = C$ from both sides*
}

\subsection{Connection to Hamiltonian Structure}

\notes{Looking ahead to Lecture 5, the Lagrange multiplier plays a role in the Hamiltonian formulation. In Hamiltonian mechanics, constraints define the phase space geometry.

For *The Inaccessible Game*, the constraint $\sum h_i = C$ defines a submanifold of the full parameter space. The dynamics $\dot{\boldsymbol{\theta}} = -\Pi_\parallel G\boldsymbol{\theta}$ are intrinsic to this submanifold.

The Lagrange multiplier $\nu$ is related to the "momentum" conjugate to the constraint. When we introduce the full Poisson bracket structure, we'll see that $\nu$ emerges naturally from the antisymmetric part of the dynamics (conservation) while $G$ emerges from the symmetric part (dissipation).

This is a preview of the GENERIC framework (Lecture 8), where Hamiltonian and gradient dynamics coexist.}

\slides{
**Preview: Hamiltonian Connection**

* Constraint defines submanifold
* $\nu$ related to conjugate momentum
* Poisson bracket structure (Lecture 5)
* GENERIC framework (Lecture 8)

*Lagrange multipliers bridge optimization and Hamiltonian mechanics*
}

\subsection{Summary: Understanding $\nu(t)$}

\notes{The Lagrange multiplier $\nu(t)$ is not a free parameter, it's determined by the constraint and the current state,
$$
\nu(t) = -\frac{a(\boldsymbol{\theta})^\top G(\boldsymbol{\theta})\boldsymbol{\theta}}{a(\boldsymbol{\theta})^\top a(\boldsymbol{\theta})}.
$$

**Key insights:**
1. $\nu$ measures the "strength" of constraint enforcement
2. Large $|\nu|$: Entropy flow conflicts strongly with constraint
3. Small $|\nu|$: Flow is nearly constraint-compatible
4. $\nu = 0$: Stationary point (equilibrium)
5. Sign of $\nu$ indicates direction of constraint force

Understanding $\nu(t)$ is key when analysing the behaviour of constrained information systems. It tells us when the system is "fighting" its constraints and when it's flowing naturally along the constraint manifold.}

\slides{
**Key Points:**

* $\nu$ auto-determined by constraint
* Magnitude: strength of enforcement
* Sign: direction of force
* $\nu = 0$: equilibrium

*Bridge between gradient flow and constrained geometry*
}
\endif
