\ifndef{tangencyAdditivityTheorem}
\define{tangencyAdditivityTheorem}

\editme

\subsection{Tangency-Additivity Theorem: Formalizing Part 1}

\notes{This section provides a rigorous formalization of the claim that **global solvability of the tangency condition requires marginal-additive constraint structure**. This is the critical step in proving necessity.}

\subsubsection{Setup and Notation}

\notes{**Exponential Family:**

Consider a multivariate exponential family with $n$ variables $x = (x_1, \ldots, x_n)$ and natural parameters $\boldsymbol{\theta} \in \mathbb{R}^d$:
$$
p(x|\boldsymbol{\theta}) = \exp\left(\boldsymbol{\theta}^\top T(x) - A(\boldsymbol{\theta})\right)m(x)
$$

**Fisher Information Matrix:**
$$
G_{jk}(\boldsymbol{\theta}) = \text{Cov}_\boldsymbol{\theta}[T_j(x), T_k(x)] = \frac{\partial^2 A}{\partial\theta_j\partial\theta_k}
$$

$G$ is positive definite everywhere in the interior of the natural parameter space.}

\notes{**Conservation Constraint:**

We impose a smooth constraint:
$$
C(\boldsymbol{\theta}) = C_0
$$

with constraint gradient $a(\boldsymbol{\theta}) = \nabla C(\boldsymbol{\theta}) \neq 0$ everywhere on the constraint manifold.}

\notes{**Entropy Gradient Flow:**

The unconstrained dynamics follow entropy gradient ascent:
$$
\dot{\boldsymbol{\theta}}^{\text{free}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}
$$

Note: $-G\boldsymbol{\theta} = \nabla H$ where $H$ is the differential entropy.}

\notes{**Tangency Condition:**

For the constrained dynamics to preserve $C(\boldsymbol{\theta}) = C_0$, we need:
$$
a(\boldsymbol{\theta})^\top \dot{\boldsymbol{\theta}} = 0
$$

The **$G$-orthogonal projector** onto the tangent space $\{v : a^\top v = 0\}$ is:
$$
\Pi_\parallel = I - G^{-1}a(a^\top G^{-1}a)^{-1}a^\top
$$

For a general vector field $b(\boldsymbol{\theta})$ (e.g., $b = -G\boldsymbol{\theta}$), the projected dynamics are:
$$
\dot{\boldsymbol{\theta}} = \Pi_\parallel b = b - G^{-1}a\,\nu
$$

where the Lagrange multiplier is:
$$
\nu(\boldsymbol{\theta}) = (a^\top G^{-1}a)^{-1} a^\top b
$$

This is **always solvable** as long as $a \neq 0$ and $G$ is positive definite, so existence of $\nu$ is not the issue.}

\subsubsection{Definition: Automatic GENERIC Degeneracy}

\notes{**Definition 1 (Automatic GENERIC Degeneracy):**

We say a constraint $C(\boldsymbol{\theta}) = C_0$ admits **automatic GENERIC degeneracy** if:

1. **Smooth Foliation**: The constraint defines a smooth foliation of parameter space. The co-distribution $\mathrm{span}\{\nabla C\}$ is of constant rank.

2. **Involutivity**: The tangent distribution $\mathcal{D}(\boldsymbol{\theta}) = \ker a(\boldsymbol{\theta})^\top$ is **involutive** (closed under Lie brackets): for any smooth vector fields $X, Y$ tangent to the constraint manifold, their Lie bracket $[X,Y]$ is also tangent.

3. **Foliation Invariance**: The constraint foliation is invariant under the admissible GENERIC flows. That is, for dynamics:
   $$\dot{\boldsymbol{\theta}} = L\nabla E + M\nabla S$$
   where $M = G$ (Fisher information) and $L$ is antisymmetric, the GENERIC degeneracy conditions:
   $$M\nabla E = 0, \quad L\nabla S = 0$$
   are satisfied automatically for appropriate energy $E$ and entropy $S = H$.
   
   *Note*: The second condition $L\nabla H = 0$ is equivalent to the orthogonality requirement $\nabla C^\top G^{-1}\nabla H = 0$ when $M = G$, which ensures the antisymmetric (conservative) part of the dynamics preserves entropy.

4. **Robustness**: These properties hold not just for a single distribution, but are **robust to turning on arbitrarily small interactions** in families that admit an independence limit.}

\notes{**Remark:** Condition (4) is crucial—it prevents trivial cases where constraints work only for exactly product (independent) distributions. "Automatic" means the structure survives perturbations.}

\subsubsection{Independence-Limit Setup}

\notes{**Block Structure:**

Consider an exponential family with block sufficient statistics:
$$
T(x) = \big(T^{(1)}(x_1), \ldots, T^{(n)}(x_n), T^{(\text{int})}(x)\big)
$$

where $T^{(i)}(x_i)$ are marginal sufficient statistics and $T^{(\text{int})}(x)$ captures interactions.

The natural parameters are:
$$
\boldsymbol{\theta} = \big(\boldsymbol{\theta}^{(1)}, \ldots, \boldsymbol{\theta}^{(n)}, \varepsilon \boldsymbol{\theta}^{(\text{int})}\big)
$$

where $\varepsilon$ is a small coupling parameter.}

\notes{**Independence Limit ($\varepsilon \to 0$):**

As $\varepsilon \to 0$, the distribution factorizes:
$$
p(x|\boldsymbol{\theta}) \to \prod_{i=1}^n p_i(x_i|\boldsymbol{\theta}^{(i)})
$$

The Fisher information becomes block-diagonal:
$$
G(\varepsilon) = \begin{pmatrix} G^{(1)} &  &  &  0 \\  & \ddots &  &  \\  &  & G^{(n)} &  \\ 0 &  &  & G^{(\text{int})} \end{pmatrix} + O(\varepsilon)
$$

where $G^{(i)}$ is the Fisher information for the $i$-th marginal.}

\subsubsection{Theorem 1: Independence-Limit Additivity}

\notes{**Theorem 1 (Additivity from Robustness):**

*Consider an exponential family admitting an independence limit $\varepsilon \to 0$ with Fisher information $G(\varepsilon) = \mathrm{diag}(G^{(1)}, \ldots, G^{(n)}, G^{(\text{int})}) + O(\varepsilon)$.*

*Suppose the constraint $C(\boldsymbol{\theta}) = C_0$ defines a foliation that is invariant under the projected dynamics for* **every** *smooth local vector field $b$ supported in a single block $i$, and this holds for all sufficiently small $\varepsilon > 0$.*

*Then $C$ must have marginal-additive structure:*
$$
C(\boldsymbol{\theta}) = \sum_{i=1}^n C_i(\boldsymbol{\theta}^{(i)}) + C^{(\text{int})}(\varepsilon\boldsymbol{\theta}^{(\text{int})})
$$
*near $\varepsilon = 0$, where each $C_i$ depends only on $\boldsymbol{\theta}^{(i)}$.*

*Furthermore, if we require invariance as $\varepsilon \to 0$ (no interaction dependence), then $C^{(\text{int})} \to$ const and:*
$$
C(\boldsymbol{\theta}) = \sum_{i=1}^n C_i(\boldsymbol{\theta}^{(i)})
$$
*exactly.*}

\notes{**Proof:**

We prove that invariance under all local flows forces mixed partials to vanish.

**Step 1: Mixed Partials Test**

For $C$ to be marginal-additive, we need:
$$
\frac{\partial^2 C}{\partial \theta_\alpha \partial \theta_\beta} = 0
$$
whenever $\theta_\alpha \in \boldsymbol{\theta}^{(i)}$ and $\theta_\beta \in \boldsymbol{\theta}^{(j)}$ with $i \neq j$.

We will show that any non-zero mixed partial implies that a purely local flow in block $i$ changes the normal direction in block $j$, violating tangency invariance. Therefore, the constraint is not robust under local GENERIC flows.

**Step 2: Mixed Partials Create Obstruction**

Suppose $C$ has a non-zero mixed partial:
$$
\frac{\partial^2 C}{\partial\theta_\alpha^{(i)}\partial\theta_\beta^{(j)}} \neq 0
$$
for some $\theta_\alpha^{(i)} \in \boldsymbol{\theta}^{(i)}$ and $\theta_\beta^{(j)} \in \boldsymbol{\theta}^{(j)}$ with $i \neq j$.

Consider a local flow $b^{(i)}$ in block $i$ with component along $\theta_\alpha^{(i)}$. Under this flow, the constraint gradient evolves as:
$$
\frac{d}{dt}\left(\frac{\partial C}{\partial \theta_\beta^{(j)}}\right) = \frac{\partial^2 C}{\partial\theta_\alpha^{(i)}\partial\theta_\beta^{(j)}} \cdot \frac{d\theta_\alpha^{(i)}}{dt} \neq 0
$$

This means the $j$-component of the constraint gradient $\nabla C$ changes under a purely $i$-local flow.

**Key Problem:** For foliation invariance, the constraint gradient $\nabla C$ must remain within the direct sum of marginal subspaces under all local flows. But the mixed partial causes a purely $i$-local flow to inject a component into the $j$-direction, violating this requirement.

Therefore, all mixed partials must vanish:
$$
\frac{\partial^2 C}{\partial\theta_\alpha^{(i)}\partial\theta_\beta^{(j)}} = 0 \quad \forall i \neq j
$$

**Step 3: Conclusion - Additivity**

Vanishing mixed partials means $C$ can be written as:
$$
C(\boldsymbol{\theta}) = \sum_{i=1}^n C_i(\boldsymbol{\theta}^{(i)}) + \text{const}
$$

where each $C_i$ depends only on the parameters $\boldsymbol{\theta}^{(i)}$ for block $i$.

This completes the proof of additivity from robustness. ∎}

\notes{**Remark (Intuition):** The key insight is that **non-additive constraints fight against the factorization structure of exponential families**. When variables become independent, the Fisher metric $G$ naturally factorizes (becomes block-diagonal). A non-additive constraint gradient $a$ does **not** respect this factorization, creating incompatibility in the tangency equation.}

\subsubsection{Corollary: Marginal-Additive Form}

\notes{**Corollary 1:**

*For a constraint $C(\boldsymbol{\theta}) = \sum_i C_i(\boldsymbol{\theta}^{(i)})$ to admit automatic tangency, each $C_i$ must be a functional of the $i$-th marginal distribution $p_i(x_i|\boldsymbol{\theta})$ only.*

**Proof:** This follows from Theorem 1 and the requirement that $C_i(\boldsymbol{\theta}^{(i)})$ must be well-defined as $\boldsymbol{\theta}$ varies. In exponential families, functionals of the marginal $p_i(x_i|\boldsymbol{\theta})$ are naturally parametrized by the marginal parameters $\boldsymbol{\theta}^{(i)}$. Any dependence on parameters outside $\boldsymbol{\theta}^{(i)}$ would couple $C_i$ to other marginals, violating the additive structure required by Theorem 1. ∎}

\subsubsection{Alternative Formulation: Integrability Condition}

\notes{We can reformulate Theorem 1 using differential geometry, providing an alternative characterization.}

\notes{**Theorem 2 (Integrability Characterization):**

*Let $\mathcal{M} = \{C(\boldsymbol{\theta}) = C_0\}$ be the constraint manifold. The constrained dynamics:*
$$
\dot{\boldsymbol{\theta}} = \Pi_\parallel(G(\boldsymbol{\theta})\boldsymbol{\theta})
$$
*where $\Pi_\parallel = I - G^{-1}a(a^\top G^{-1}a)^{-1}a^\top$ is the tangent space projector, are well-defined and smooth on $\mathcal{M}$ if and only if the distribution:*
$$
\mathcal{D} = \{T_{\boldsymbol{\theta}}\mathcal{M} : \boldsymbol{\theta} \in \mathcal{M}\}
$$
*is integrable (involutive) and the projection of the entropy gradient flow onto $\mathcal{D}$ is globally defined.*

*For exponential families, this holds if and only if $C$ has marginal-additive structure.*}

\notes{**Proof:**

The tangent distribution is exactly $\mathcal{D} = \ker(\nabla C^\top)$. By the Frobenius theorem, integrability of $\mathcal{D}$ is equivalent to $C(\boldsymbol{\theta})$ being locally a function of independent coordinates. When the Fisher metric factorizes (as in the independence limit), this is equivalent to additivity over marginals.

**Part (a): Integrability Requirement**

A distribution $\mathcal{D}$ is integrable (by Frobenius theorem) if and only if for any two vector fields $X, Y$ tangent to $\mathcal{M}$, their Lie bracket $[X, Y]$ is also tangent:
$$
X, Y \in \mathcal{D} \implies [X, Y] \in \mathcal{D}
$$

For our constraint manifold, a vector $v$ is tangent if $a^\top v = 0$. The Lie bracket condition becomes:
$$
a^\top[X, Y] = X(a^\top Y) - Y(a^\top X) - (a^\top X)(dY) + (a^\top Y)(dX) = 0
$$

Since $X, Y$ are tangent: $a^\top X = a^\top Y = 0$, this simplifies to:
$$
X(a^\top Y) - Y(a^\top X) = 0
$$

**Part (b): Marginal-Additive Structure Ensures Integrability**

If $C = \sum_i C_i(\boldsymbol{\theta}^{(i)})$, then:
$$
a = \nabla C = \sum_i \nabla C_i
$$

where each $\nabla C_i$ has support only on $\boldsymbol{\theta}^{(i)}$ (parameters for the $i$-th marginal).

Consider vector fields $X, Y$ tangent to $\mathcal{M}$. We can decompose:
$$
X = \sum_i X^{(i)}, \quad Y = \sum_j Y^{(j)}
$$

where $X^{(i)}$ has support only on $\boldsymbol{\theta}^{(i)}$.

The Lie bracket is:
$$
[X, Y] = \sum_{i,j} [X^{(i)}, Y^{(j)}]
$$

**Key Property:** For $i \neq j$ (disjoint parameter subsets), we have $[X^{(i)}, Y^{(j)}] = 0$ (commutativity).

Therefore:
$$
[X, Y] = \sum_i [X^{(i)}, Y^{(i)}]
$$

Each term $[X^{(i)}, Y^{(i)}]$ is tangent to the constraint because:
$$
(\nabla C_i)^\top [X^{(i)}, Y^{(i)}] = X^{(i)}((\nabla C_i)^\top Y^{(i)}) - Y^{(i)}((\nabla C_i)^\top X^{(i)}) = 0
$$

(since $X^{(i)}$ and $Y^{(i)}$ are tangent to the $i$-th marginal constraint).

Summing over $i$:
$$
a^\top [X, Y] = \sum_i (\nabla C_i)^\top [X^{(i)}, Y^{(i)}] = 0
$$

Thus $[X, Y]$ is tangent, proving integrability.

**Part (c): Non-Additive Structure Violates Integrability**

If $C$ is not marginal-additive, then $\nabla C$ cannot be decomposed into independent marginal contributions. This means there exist vector fields $X, Y$ tangent to $\mathcal{M}$ such that their Lie bracket $[X, Y]$ has a component in the $a$ direction (not tangent).

Specifically, if $\partial^2 C/\partial\theta_i\partial\theta_j \neq 0$ for $i \neq j$, then vector fields varying $\theta_i$ and $\theta_j$ will have non-zero Lie bracket in the direction perpendicular to $\mathcal{M}$.

This violates integrability, preventing a global foliation.

**Part (d): Connection to Automatic Tangency**

The failure of integrability implies that the tangent space "twists" as we move along $\mathcal{M}$. This twisting means the projector $\Pi_\parallel(\boldsymbol{\theta})$ varies in an incompatible way with the entropy gradient $-G\boldsymbol{\theta}$, creating singularities in the projected flow.

This is precisely the obstruction identified in Theorem 1. ∎}

\subsubsection{Summary of Part 1}

\notes{**What We've Proven:**

1. **Theorem 1 (Additivity Requirement):** Automatic tangency requires marginal-additive constraint structure.

2. **Corollary 1:** Each term in the additive constraint must be a functional of a single marginal distribution.

3. **Theorem 2 (Integrability):** This requirement is equivalent to an integrability condition from differential geometry.

**Intuition:** Non-additive constraints create "twisting" that fights against the natural factorization structure of exponential families, causing singularities or discontinuities in the Lagrange multiplier $\nu(\boldsymbol{\theta})$.}

\notes{**Next Step:** We've established that $C = \sum_i C_i(\boldsymbol{\theta}^{(i)})$ where each $C_i$ is a functional of $p_i(x_i|\boldsymbol{\theta})$. In Part 2, we must prove that **$C_i = h_i$ (marginal entropy)** is the unique functional (up to monotonic transformation) compatible with exponential family structure and GENERIC dynamics.}

\endif

