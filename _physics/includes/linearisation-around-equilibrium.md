\ifndef{linearisationAroundEquilibrium}
\define{linearisationAroundEquilibrium}

\editme

\subsection{Standard Perturbation Analysis}

\notes{We want to understand dynamics near an equilibrium point $\boldsymbol{\theta}^\ast$. The standard approach: perturb slightly and linearise.

**Setup:** Let $q(t) = \boldsymbol{\theta}(t) - \boldsymbol{\theta}^\ast$ be the small deviation from equilibrium. Our goal is to find the leading-order dynamics for $q(t)$.

Recall from Lecture 4 that the constrained dynamics are:
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(t) a(\boldsymbol{\theta})
$$
where
- $G(\boldsymbol{\theta})$ is the Fisher information matrix
- $\nu(t)$ is the Lagrange multiplier
- $a(\boldsymbol{\theta}) = \sum_i \nabla h_i(\boldsymbol{\theta})$ is the constraint gradient

At equilibrium $\boldsymbol{\theta}^\ast$, we have $\dot{\boldsymbol{\theta}}^\ast = 0$, which means
$$
G(\boldsymbol{\theta}^\ast)\boldsymbol{\theta}^\ast + \nu^\ast a(\boldsymbol{\theta}^\ast) = 0
$$
for some value $\nu^\ast$.}

\slides{
**Perturbation Setup**

Equilibrium: $\boldsymbol{\theta}^\ast$ where $\dot{\boldsymbol{\theta}} = 0$

**Perturb:** $\boldsymbol{\theta}(t) = \boldsymbol{\theta}^\ast + q(t)$ where $|q| \ll 1$

**Dynamics**
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(t) a(\boldsymbol{\theta})
$$

**At equilibrium**
$$
G(\boldsymbol{\theta}^\ast)\boldsymbol{\theta}^\ast + \nu^\ast a(\boldsymbol{\theta}^\ast) = 0
$$
}

\subsection{Linearisation in the Gaussian Regime}

\notes{In the Gaussian regime, we make a crucial simplification: *the Fisher information matrix $G$ is constant*. This is because for Gaussians, $G = \Sigma^{-1}$ (the inverse covariance), which doesn't depend on the natural parameters once we're in the exponential family representation.

With constant $G$, we have $G(\boldsymbol{\theta}) = G(\boldsymbol{\theta}^\ast) = G$ for all nearby points.

Now substitute $\boldsymbol{\theta} = \boldsymbol{\theta}^\ast + q$:
$$
\dot{q} = \dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta}^\ast + q)(\boldsymbol{\theta}^\ast + q) - \nu(t) a(\boldsymbol{\theta}^\ast + q)
$$

Using $G$ constant
$$
\dot{q} = -G\boldsymbol{\theta}^\ast - Gq - \nu(t) a(\boldsymbol{\theta}^\ast + q).
$$
At equilibrium, $G\boldsymbol{\theta}^\ast = -\nu^\ast a(\boldsymbol{\theta}^\ast)$, so
$$
\dot{q} = -Gq + \nu^\ast a(\boldsymbol{\theta}^\ast) - \nu(t) a(\boldsymbol{\theta}.^\ast + q)
$$
Now we need to expand $a(\boldsymbol{\theta}^\ast + q)$ to first order in $q$.}

\slides{
**Gaussian Regime: $G$ constant**

Substitute $\boldsymbol{\theta} = \boldsymbol{\theta}^\ast + q$
$$
\dot{q} = -Gq + \nu^\ast a(\boldsymbol{\theta}^\ast) - \nu(t) a(\boldsymbol{\theta}^\ast + q).
$$

*Need:* Expand $a(\boldsymbol{\theta}^\ast + q)$ and $\nu(t)$ to first order.
}

\subsection{First-Order Expansion}

\notes{The constraint gradient expands as:
$$
a(\boldsymbol{\theta}^\ast + q) = a(\boldsymbol{\theta}^\ast) + A q + O(q^2)
$$
where $A$ is the Hessian matrix
$$
A_{ij} = \frac{\partial^2}{\partial \theta_i \partial \theta_j}\left(\sum_k h_k\right)\bigg|_{\boldsymbol{\theta}^\ast} = \sum_k \frac{\partial^2 h_k}{\partial \theta_i \partial \theta_j}\bigg|_{\boldsymbol{\theta}^\ast}.
$$
The Lagrange multiplier also changes with $q$. To first order, we can write $\nu(t) = \nu^\ast + \delta\nu(t)$ where $\delta\nu$ is determined by the constraint.

Recall from Lecture 4 that the constraint requires $a(\boldsymbol{\theta})^\top \dot{\boldsymbol{\theta}} = 0$. Differentiating with respect to time
$$
a(\boldsymbol{\theta})^\top \dot{q} = 0.
$$

Substituting our linearised dynamics and solving for $\delta\nu$ (keeping only first-order terms), we get
$$
\delta\nu = -\frac{a^\top G q}{\|a\|^2}
$$
where $a = a(\boldsymbol{\theta}^\ast)$ for notational simplicity.}

\slides{*First-Order Expansion*

Constraint gradient: $a(\boldsymbol{\theta}^\ast + q) \approx a(\boldsymbol{\theta}^\ast) + A q$ where $A = \nabla^2(\sum_k h_k)|_{\boldsymbol{\theta}^\ast}$.

Lagrange multiplier: $\nu(t) = \nu^\ast + \delta\nu(t)$

From constraint $a^\top \dot{q} = 0$
$$
\delta\nu \approx -\frac{a^\top G q}{\|a\|^2}.
$$
}

\subsection{The Linearised Dynamics Matrix}

\notes{Putting everything together and keeping only first-order terms in $q$
$$
\dot{q} = -Gq - (\nu^\ast + \delta\nu)(a + Aq).
$$
Expanding and dropping $O(q^2)$ terms
$$
\dot{q} = -Gq - \nu^\ast a - \nu^\ast Aq - \delta\nu \, a,
$$
but at equilibrium, $-Gq|_{q=0} = \nu^\ast a$, so the constant terms cancel. Using $\delta\nu = -\frac{a^\top G q}{\|a\|^2}$,
$$
\dot{q} = -Gq - \nu^\ast Aq + \frac{a a^\top G q}{\|a\|^2}.
$$

Define the **linearisation matrix**,
$$
M = -G - \nu^\ast A + \frac{a a^\top G}{\|a\|^2}.
$$
The linearised dynamics are simply
$$
\dot{q} = M q.
$$
This is standard linear system dynamics. The eigenvalues of $M$ determine stability, and the eigenvectors give the normal modes.}

\slides{**Linearised Dynamics**

$$
\dot{q} = M q
$$

Where the *linearisation matrix* is
$$
M = -G - \nu^\ast A + \frac{a a^\top G}{\|a\|^2}
$$
}

\newslide{}

\slides{
**Components:**

* $-G$: Entropy gradient (dissipative)
* $-\nu^\ast A$: Constraint curvature
* $\frac{aa^\top G}{\|a\|^2}$: Constraint maintenance (projector)

**Next lecture:** Decompose $M = S + A$ into symmetric/antisymmetric parts
}

\subsection{Geometric Interpretation}

\notes{Let's understand what each term in $M$ means:

1. **$-G$**: The entropy gradient contribution. In the unconstrained case ($\nu^\ast = 0$), this would be the full dynamics—steepest entropy ascent.

2. **$-\nu^\ast A$**: The constraint curvature. This term arises because the constraint surface itself curves. The second derivatives of marginal entropies encode how the constraint manifold bends.

3. **$\frac{aa^\top G}{\|a\|^2}$**: The constraint maintenance term. This is a projection operator that ensures dynamics stay tangent to the constraint manifold. Recall from Lecture 4 the tangent space projector $\Pi_\parallel = I - \frac{aa^\top}{\|a\|^2}$. This term is the residual from maintaining the constraint dynamically.

**Key insight:** Even though we're near equilibrium and doing linear analysis, the constraint geometry (encoded in $A$ and $a$) still plays a crucial role. The dynamics aren't just "entropy gradient"—they're entropy gradient projected onto and curved by the constraint manifold.}

\slides{**Geometric Picture**

$M = -G - \nu^\ast A + \frac{aa^\top G}{\|a\|^2}$

Three contributions:

1. **Entropy gradient** ($-G$): Push toward higher entropy
2. **Constraint curvature** ($-\nu^\ast A$): Constraint manifold bends  
3. **Constraint projection** ($\frac{aa^\top G}{\|a\|^2}$): Stay on manifold

**Key point:** Constraint geometry matters even in linear regime!
}

\subsection{Summary: From Equilibrium to Linear Dynamics}

\notes{**What we've done:**

1. Started with constrained MEP dynamics
2. Focused on Gaussian regime (computable, physically motivated)
3. Perturbed around equilibrium: $\boldsymbol{\theta} = \boldsymbol{\theta}^\ast + q$
4. Linearised to first order: $\dot{q} = Mq$
5. Found explicit form for $M$ in terms of $G$, $A$, and $a$

**What we've learned:**

- Near equilibrium, dynamics are linear
- Matrix $M$ encodes entropy gradient, constraint curvature, and constraint projection
- Gaussian regime makes everything explicit and computable

**What's next**

The matrix $M$ can be decomposed as $M = S + A$ where $S$ is symmetric and $A$ is antisymmetric. This decomposition gives:

- Antisymmetric part: Conservative/Hamiltonian dynamics
- Symmetric part: Dissipative/gradient dynamics

This is the emergence of the GENERIC structure from information geometry.}

\slides{
**Summary**

Near equilibrium in Gaussian regime:
$$
\dot{q} = Mq, \quad M = -G - \nu^\ast A + \frac{aa^\top G}{\|a\|^2}
$$

**Achieved:**

* Standard perturbation analysis ✓
* Explicit linearisation matrix ✓
* Geometric interpretation ✓

**Next:** Decompose $M = S + A$ $\rightarrow$ Conservative/Dissipative split
}

\endif

