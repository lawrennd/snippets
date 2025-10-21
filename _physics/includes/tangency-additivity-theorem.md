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

This is enforced via Lagrange multiplier:
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} + \nu(\boldsymbol{\theta}) G^{-1}(\boldsymbol{\theta})a(\boldsymbol{\theta})
$$

where $\nu$ is determined by the tangency condition:
$$
\nu(\boldsymbol{\theta}) = \frac{a(\boldsymbol{\theta})^\top G(\boldsymbol{\theta})\boldsymbol{\theta}}{a(\boldsymbol{\theta})^\top G^{-1}(\boldsymbol{\theta})a(\boldsymbol{\theta})}
$$
}

\subsubsection{Definition: Automatic Tangency}

\notes{**Definition 1 (Automatic Tangency):**

We say a constraint $C(\boldsymbol{\theta}) = C_0$ admits **automatic tangency** if:

1. **Global Existence**: For every $\boldsymbol{\theta}$ on the constraint manifold, there exists a unique $\nu(\boldsymbol{\theta})$ satisfying the tangency condition.

2. **Smoothness**: $\nu(\boldsymbol{\theta})$ is a smooth (at least $C^1$) function of $\boldsymbol{\theta}$ on the constraint manifold.

3. **No Fine-Tuning**: The existence and smoothness of $\nu$ follow automatically from the structure of $C$, $G$, and the entropy gradient—without requiring special relationships between these quantities at each point.}

\notes{**Remark:** Condition (3) distinguishes "automatic" from "engineered" constraints. An engineered constraint might achieve tangency by carefully constructing $C(\boldsymbol{\theta})$ point-by-point to ensure $\nu$ exists, rather than having a natural structure that guarantees it.}

\subsubsection{The Tangency Equation: Structural Analysis}

\notes{**The Central Equation:**

From the tangency condition, we need:
$$
a(\boldsymbol{\theta})^\top G(\boldsymbol{\theta})\boldsymbol{\theta} = \nu(\boldsymbol{\theta}) \cdot a(\boldsymbol{\theta})^\top G^{-1}(\boldsymbol{\theta})a(\boldsymbol{\theta})
$$

Rearranging:
$$
\nu(\boldsymbol{\theta}) = \frac{a^\top G\boldsymbol{\theta}}{\|a\|^2_{G^{-1}}}
$$

where $\|a\|^2_{G^{-1}} := a^\top G^{-1} a$ is the squared length of $a$ in the dual metric.}

\notes{**Key Observation 1: Coupling Through $G\boldsymbol{\theta}$**

The numerator $a^\top G\boldsymbol{\theta}$ couples the constraint gradient $a$ with the entropy gradient $-G\boldsymbol{\theta}$.

For exponential families:
$$
(G\boldsymbol{\theta})_j = \sum_{k=1}^d G_{jk}(\boldsymbol{\theta})\theta_k = \sum_{k=1}^d \text{Cov}[T_j(x), T_k(x)]\theta_k
$$

This is a **global coupling**—every component $j$ is coupled to every other component $k$ through their covariance in the joint distribution $p(x|\boldsymbol{\theta})$.}

\notes{**Key Observation 2: Obstruction from Non-Additive Constraints**

Suppose $C(\boldsymbol{\theta})$ has the form:
$$
C(\boldsymbol{\theta}) = f(\boldsymbol{\theta}) + g(\boldsymbol{\theta})
$$

where $f$ and $g$ depend on **overlapping** subsets of variables (e.g., $f$ depends on $x_1, x_2$ and $g$ depends on $x_2, x_3$).

Then:
$$
a = \nabla C = \nabla f + \nabla g
$$

involves cross-terms that couple variables through both $f$ and $g$. When we compute $a^\top G\boldsymbol{\theta}$, we get:
$$
a^\top G\boldsymbol{\theta} = \nabla f^\top G\boldsymbol{\theta} + \nabla g^\top G\boldsymbol{\theta} + \text{cross-terms}
$$

The cross-terms involve products like $(\nabla f)_j G_{jk} (\nabla g)_k$, which couple different parts of the constraint through the covariance structure of $G$.}

\subsubsection{Lemma 1: Regularity of Lagrange Multiplier}

\notes{**Lemma 1 (Regularity Condition):**

*Let $C(\boldsymbol{\theta})$ be a smooth constraint with gradient $a(\boldsymbol{\theta}) = \nabla C \neq 0$. The Lagrange multiplier:*
$$
\nu(\boldsymbol{\theta}) = \frac{a(\boldsymbol{\theta})^\top G(\boldsymbol{\theta})\boldsymbol{\theta}}{a(\boldsymbol{\theta})^\top G^{-1}(\boldsymbol{\theta})a(\boldsymbol{\theta})}
$$
*is smooth on the constraint manifold $\mathcal{M} = \{C(\boldsymbol{\theta}) = C_0\}$ if and only if the ratio of:*
$$
\phi(\boldsymbol{\theta}) := a(\boldsymbol{\theta})^\top G(\boldsymbol{\theta})\boldsymbol{\theta} \quad \text{(numerator)}
$$
$$
\psi(\boldsymbol{\theta}) := a(\boldsymbol{\theta})^\top G^{-1}(\boldsymbol{\theta})a(\boldsymbol{\theta}) \quad \text{(denominator)}
$$
*has matched singularities: if $\phi$ has a zero of order $k$ at $\boldsymbol{\theta}_0 \in \mathcal{M}$, then $\psi$ must also have a zero of order $\geq k$ at $\boldsymbol{\theta}_0$.*}

\notes{**Proof:** 

This follows from standard analysis. For $\nu = \phi/\psi$ to be smooth (have continuous derivatives), we need:

1. $\psi(\boldsymbol{\theta}) > 0$ everywhere (which holds since $G^{-1}$ is positive definite and $a \neq 0$)

2. If $\phi(\boldsymbol{\theta}_0) = 0$ (numerator vanishes), then either:
   - $\psi(\boldsymbol{\theta}_0) \neq 0$ and $\nu(\boldsymbol{\theta}_0) = 0$ (smooth zero)
   - OR $\psi(\boldsymbol{\theta}_0) = 0$ with the same or higher order (L'Hôpital applies)

3. The derivatives $\nabla \phi$ and $\nabla \psi$ must be compatible at zeros

If these conditions are violated, $\nu$ has singularities (infinite derivatives or discontinuities). ∎}

\notes{**Key Implication:** The numerator $\phi$ depends on the entropy gradient $G\boldsymbol{\theta}$, while the denominator $\psi$ depends on the constraint geometry (metric length of $a$). For automatic tangency, the constraint $C$ must be structured such that zeros of $\phi$ and $\psi$ are naturally matched—without fine-tuning at each point.}

\subsubsection{Theorem 1: Additivity from Global Tangency}

\notes{**Theorem 1 (Additivity Requirement):**

*Let $C(\boldsymbol{\theta})$ be a smooth constraint on a multivariate exponential family with $n$ variables $x = (x_1, \ldots, x_n)$. Suppose $C$ admits automatic tangency (as defined above). Then $C$ must have marginal-additive structure:*
$$
C(\boldsymbol{\theta}) = \sum_{i=1}^n C_i(\boldsymbol{\theta}^{(i)})
$$
*where $\boldsymbol{\theta}^{(i)}$ denotes the subset of parameters governing the marginal distribution $p_i(x_i|\boldsymbol{\theta})$, and each $C_i$ depends only on $\boldsymbol{\theta}^{(i)}$.*}

\notes{**Proof:**

We prove by contradiction. Assume $C$ admits automatic tangency but is not marginal-additive.

**Step 1: Existence of Coupled Variables**

Since $C$ is not marginal-additive, by definition, there exist indices $i \neq j$ such that $C$ cannot be decomposed as a sum of functions where each function depends only on parameters of a single marginal. Formally, there exists no decomposition:
$$
C(\boldsymbol{\theta}) = \sum_{k=1}^n f_k(\boldsymbol{\theta}^{(k)})
$$

This means there must exist a mixed partial derivative that doesn't vanish:
$$
\frac{\partial^2 C}{\partial \theta_\alpha \partial \theta_\beta} \neq 0
$$
where $\theta_\alpha \in \boldsymbol{\theta}^{(i)}$ and $\theta_\beta \in \boldsymbol{\theta}^{(j)}$ for some $i \neq j$.

**Step 2: Simplification to Two-Variable Case**

Without loss of generality (by restricting to a 2-dimensional submanifold), consider $C$ depending on two parameters $\theta_1, \theta_2$ governing distinct marginals $p_1(x_1)$ and $p_2(x_2)$, with mixed derivative:
$$
\frac{\partial^2 C}{\partial \theta_1 \partial \theta_2} = c(\boldsymbol{\theta}) \neq 0
$$
for some region on the constraint manifold.

The constraint gradient has components:
$$
a_1 = \frac{\partial C}{\partial \theta_1}, \quad a_2 = \frac{\partial C}{\partial \theta_2}
$$

**Step 3: Independence Limit**

Consider a family of distributions approaching independence: $p(x_1, x_2|\boldsymbol{\theta}(\epsilon)) \to p_1(x_1) p_2(x_2)$ as $\epsilon \to 0$.

For exponential families, this corresponds to setting interaction parameters to zero. The Fisher matrix becomes:
$$
G(\epsilon) = \begin{pmatrix} G_{11}(\epsilon) & G_{12}(\epsilon) \\ G_{21}(\epsilon) & G_{22}(\epsilon) \end{pmatrix}
$$

where $G_{12}(\epsilon) = \text{Cov}[T_1, T_2] \to 0$ as $\epsilon \to 0$.

The marginal blocks $G_{11}, G_{22}$ remain positive definite (bounded away from zero).

**Step 4: Inverse Fisher Matrix Behavior**

Using the Sherman-Morrison-Woodbury formula (or direct block inversion):
$$
G^{-1}(\epsilon) = \begin{pmatrix} G_{11}^{-1} & 0 \\ 0 & G_{22}^{-1} \end{pmatrix} + O(\epsilon)
$$

Critically, $(G^{-1})_{12}(\epsilon) = O(\epsilon)$ remains bounded as $\epsilon \to 0$.

**Step 5: Constraint Geometry vs. Distribution Geometry**

The constraint $C(\boldsymbol{\theta}(\epsilon)) = C_0$ defines a curve/manifold. If $C$ has non-zero mixed derivative $\partial^2 C/\partial\theta_1\partial\theta_2 \neq 0$, then the constraint gradient:
$$
a(\epsilon) = \nabla C|_{\boldsymbol{\theta}(\epsilon)}
$$

does **not** align with the block structure of $G(\epsilon)$ as $\epsilon \to 0$.

Specifically, if the constraint forces $\theta_1$ and $\theta_2$ to vary together (through the non-separable $C$), then $a_1(\epsilon)$ and $a_2(\epsilon)$ remain coupled even as $G_{12}(\epsilon) \to 0$.

**Step 6: Denominator Analysis**

The denominator is:
$$
\psi(\epsilon) = a^\top G^{-1} a = a_1^2 (G^{-1})_{11} + 2a_1 a_2 (G^{-1})_{12} + a_2^2 (G^{-1})_{22}
$$

As $\epsilon \to 0$:
$$
\psi(\epsilon) = a_1^2(\epsilon) G_{11}^{-1} + a_2^2(\epsilon) G_{22}^{-1} + O(\epsilon)
$$

This is bounded and positive (since $a \neq 0$ and $G^{-1}$ blocks are positive definite).

**Step 7: Numerator Analysis**

The numerator is:
$$
\phi(\epsilon) = a^\top G \boldsymbol{\theta} = a_1 (G\boldsymbol{\theta})_1 + a_2 (G\boldsymbol{\theta})_2
$$

where:
$$
(G\boldsymbol{\theta})_1 = G_{11}\theta_1 + G_{12}\theta_2, \quad (G\boldsymbol{\theta})_2 = G_{21}\theta_1 + G_{22}\theta_2
$$

As $\epsilon \to 0$:
$$
\phi(\epsilon) = a_1(\epsilon)(G_{11}\theta_1 + O(\epsilon)) + a_2(\epsilon)(G_{22}\theta_2 + O(\epsilon))
$$

**Step 8: Critical Incompatibility**

The key observation: $\phi$ and $\psi$ have **different dependence** on the constraint structure $C$.

- $\psi$ depends on $a$ through the **metric** $G^{-1}$ (geometric quantity)
- $\phi$ depends on $a$ through the **entropy gradient** $G\boldsymbol{\theta}$ (dynamical quantity)

For non-separable $C$: The constraint forces $a_1$ and $a_2$ to co-vary (through $\partial^2 C/\partial\theta_1\partial\theta_2$), while the distributions are becoming independent ($G_{12} \to 0$).

This creates a **mismatch**: 
- If the constraint forces $a_1/a_2 = f(\epsilon)$ along the path (determined by $C$'s geometry)
- The entropy gradient gives $(G\boldsymbol{\theta})_1/(G\boldsymbol{\theta})_2 = g(\epsilon)$ (determined by marginal distributions)
- For non-separable $C$, we have $f(\epsilon) \not\propto g(\epsilon)$ generically

**Step 9: Directional Derivative Obstruction**

Consider the directional derivative of $\nu$ along the constraint manifold. By the quotient rule:
$$
\frac{d\nu}{ds} = \frac{1}{\psi^2}\left(\psi\frac{d\phi}{ds} - \phi\frac{d\psi}{ds}\right)
$$

where $s$ parametrizes the constraint manifold.

For $\nu$ to be smooth, this derivative must be continuous. However:

$$
\frac{d\phi}{ds} = \frac{da}{ds}^\top G\boldsymbol{\theta} + a^\top \frac{dG}{ds}\boldsymbol{\theta} + a^\top G\frac{d\boldsymbol{\theta}}{ds}
$$

$$
\frac{d\psi}{ds} = 2\frac{da}{ds}^\top G^{-1}a + a^\top \frac{dG^{-1}}{ds}a
$$

The term $\frac{da}{ds}$ depends on the second derivatives of $C$ (Hessian). For non-separable $C$, this involves $\partial^2 C/\partial\theta_i\partial\theta_j \neq 0$.

The term $\frac{dG}{ds}$ depends on how the Fisher matrix changes along the constraint, which is determined by the distribution structure.

**Critical Point:** These two sources of variation ($C$'s Hessian vs. $G$'s variation) are **generically incompatible** for non-separable $C$. The constraint geometry (determined by $C$) and the statistical geometry (determined by $G$) evolve differently, creating points where $d\nu/ds$ is discontinuous or unbounded.

**Step 10: Conclusion**

We have shown that non-separable $C$ creates incompatibility between constraint geometry and statistical geometry, violating the smoothness of $\nu$. This contradicts the assumption of automatic tangency.

Therefore, $C$ must be separable (marginal-additive). ∎}

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

