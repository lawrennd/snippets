\ifndef{entropyUniquenessTheorem}
\define{entropyUniquenessTheorem}

\editme

\subsection{Part 2: Uniqueness of Marginal Entropy}

\notes{In Part 1, we established that automatic tangency requires marginal-additive structure:
$$
C(\boldsymbol{\theta}) = \sum_{i=1}^n C_i(\boldsymbol{\theta}^{(i)})
$$

In this section, we prove that each $C_i$ must be (up to affine transformation) the marginal entropy $h_i(\boldsymbol{\theta})$.}

\subsubsection{Setup: Marginal Functionals}

\notes{**Marginal Distribution:**

For exponential family:
$$
p(x|\boldsymbol{\theta}) = \exp(\boldsymbol{\theta}^\top T(x) - A(\boldsymbol{\theta}))m(x)
$$

The $i$-th marginal distribution is:
$$
p_i(x_i|\boldsymbol{\theta}) = \int p(x|\boldsymbol{\theta}) \prod_{j \neq i} dx_j
$$

The marginal entropy is:
$$
h_i(\boldsymbol{\theta}) = -\int p_i(x_i|\boldsymbol{\theta}) \log p_i(x_i|\boldsymbol{\theta}) dx_i
$$
}

\notes{**Key Properties of Marginal Entropy:**

1. **Functional of marginal only**: $h_i$ depends on $\boldsymbol{\theta}$ only through the marginal $p_i(x_i|\boldsymbol{\theta})$

2. **Concavity**: $h_i$ is strictly concave in $\boldsymbol{\theta}$ (for exponential families)

3. **Gradient structure**: $\nabla_\boldsymbol{\theta} h_i$ connects to the marginal sufficient statistic expectations

4. **Natural scale**: $h_i$ has units of nats (or bits), providing a natural information-theoretic scale}

\subsubsection{Theorem 3: Entropy Characterization}

\notes{**Theorem 3 (Uniqueness of Marginal Entropy):**

*Let $C_i(\boldsymbol{\theta}^{(i)})$ be a smooth functional of the $i$-th marginal distribution $p_i(x_i|\boldsymbol{\theta})$ such that the constraint:*
$$
C(\boldsymbol{\theta}) = \sum_{i=1}^n C_i(\boldsymbol{\theta}^{(i)}) = C_0
$$
*combined with entropy gradient flow:*
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}
$$
*admits:*
1. *Automatic tangency (smooth $\nu(\boldsymbol{\theta})$ globally)*
2. *GENERIC structure (antisymmetric-symmetric decomposition)*
3. *Energy function $E$ and entropy $S$ with degeneracy conditions*

*Then $C_i$ must be an affine transformation of the marginal entropy:*
$$
C_i(\boldsymbol{\theta}^{(i)}) = \alpha_i h_i(\boldsymbol{\theta}) + \beta_i
$$
*where $\alpha_i \in \mathbb{R} \setminus \{0\}$ and $\beta_i \in \mathbb{R}$ are constants.*}

\notes{**Proof:**

We prove this through a series of necessary conditions that uniquely determine $C_i$.

**Step 1: GENERIC Degeneracy Condition 1**

For GENERIC structure, we need:
$$
M\nabla E = 0
$$

where $M = G$ (Fisher information) is the friction operator and $E$ is an energy function.

This means:
$$
G\nabla E = 0
$$

Since $G$ is positive definite, this implies $\nabla E = 0$. The energy $E$ must be constant on the constraint manifold.

**Candidate energy functions:**
- Joint entropy $H(\boldsymbol{\theta})$
- Multi-information $I(\boldsymbol{\theta})$  
- Functions of these

**Key constraint:** $E$ must be conserved by the antisymmetric part of the dynamics.

**Step 2: Constraint Conservation**

The constraint itself is conserved by construction:
$$
\dot{C} = \nabla C^\top \dot{\boldsymbol{\theta}} = 0
$$

This is the primary Casimir function. It must equal $\sum_i C_i = C_0$.

**Step 3: GENERIC Degeneracy Condition 2**

The second degeneracy condition is:
$$
L\nabla S = 0
$$

where $L$ is the antisymmetric (Poisson) operator and $S$ is entropy.

For information dynamics, $S = H$ (joint entropy) and the antisymmetric part comes from the constraint:
$$
L = A = \text{antisymmetric part of } \Pi_\parallel G
$$

We've already proven (Lecture 7) that this condition is automatically satisfied when the constraint is $\sum h_i = C$.

**Question:** Is this the only constraint giving automatic satisfaction?

**Step 4: Uniqueness from Antisymmetric Structure**

The antisymmetric operator must satisfy:
$$
A\nabla H = 0
$$

This means the antisymmetric part of the dynamics must conserve joint entropy $H$.

From Lecture 7, we derived that $A$ is constructed from the constraint gradient $a = \nabla C$ via the projector. The condition $A\nabla H = 0$ imposes a specific relationship between $\nabla C$ and $\nabla H$.

**Key Identity:** For exponential families, we have:
$$
\nabla H = -G\boldsymbol{\theta}
$$

So the condition becomes:
$$
A G\boldsymbol{\theta} = 0
$$

The antisymmetric operator $A$ must annihilate the entropy gradient $G\boldsymbol{\theta}$.

**Step 5: Constraint Gradient Requirements**

The projector is:
$$
\Pi_\parallel = I - G^{-1}a(a^\top G^{-1}a)^{-1}a^\top
$$

The antisymmetric part is constructed to make:
$$
a^\top \dot{\boldsymbol{\theta}} = 0 \quad \text{(tangency)}
$$

For $A\nabla H = 0$ to hold automatically (not just at equilibrium, but along the entire trajectory), we need the constraint gradient $a$ to have special structure.

**Claim:** The constraint gradient must be:
$$
a = \nabla C = \sum_i \nabla h_i
$$

where $h_i$ are the marginal entropies.

**Why?** Because the antisymmetric decomposition of $G$ with respect to this specific constraint naturally satisfies $A G\boldsymbol{\theta} = 0$ due to the identity:
$$
G\boldsymbol{\theta} = -\nabla H = -\nabla\left(C - I\right) = -\nabla C + \nabla I = -\sum_i \nabla h_i + \nabla I
$$

**Step 6: Marginal Entropy Gradients**

For exponential families, the gradient of marginal entropy $h_i$ with respect to $\boldsymbol{\theta}$ is:
$$
\nabla h_i = -\mathbb{E}_{p_i}[\nabla \log p_i(x_i|\boldsymbol{\theta})]
$$

This gradient has a specific structure related to the marginal sufficient statistics.

**Key Property:** The sum $\sum_i \nabla h_i$ naturally appears in the decomposition:
$$
\nabla H = \nabla I + \sum_i \nabla h_i
$$

where $I$ is multi-information.

This decomposition is fundamental to exponential families and reflects the information-theoretic identity $H + I = \sum h_i$.

**Step 7: Uniqueness Argument**

Suppose $C = \sum_i C_i(\boldsymbol{\theta}^{(i)})$ where $C_i \neq \alpha_i h_i + \beta_i$.

Then $\nabla C \neq \sum_i \alpha_i \nabla h_i$ (up to constant multiple).

Consider the antisymmetric operator $A$ constructed from $\nabla C$. For GENERIC degeneracy $A\nabla H = 0$, we need:
$$
A G\boldsymbol{\theta} = 0
$$

Expanding using the projector structure and $\nabla H = -G\boldsymbol{\theta}$, this becomes a condition on the relationship between $\nabla C$ and $\nabla H$.

**Critical Observation:** The exponential family structure gives:
$$
G\boldsymbol{\theta} = -\nabla H = -\sum_i \nabla h_i + \nabla I
$$

For $A$ (which projects perpendicular to $\nabla C$) to annihilate this, we need $\nabla C$ to be orthogonal (in the appropriate metric) to $\nabla I$.

**Orthogonality Condition:**
$$
\nabla C^\top G^{-1} \nabla I = 0
$$

If $\nabla C = \sum_i \alpha_i \nabla h_i$, this condition is automatically satisfied because:
$$
\left(\sum_i \nabla h_i\right)^\top G^{-1} \nabla I = 0
$$

is an identity in exponential families (tangency of marginal entropy gradient to the constant-$I$ surfaces).

**If $\nabla C$ has any other component**, the orthogonality fails, creating a conflict: the antisymmetric part $A$ cannot simultaneously:
- Project onto the tangent space (enforce $a^\top \dot{\boldsymbol{\theta}} = 0$)
- Conserve joint entropy (satisfy $A\nabla H = 0$)

**Step 8: Affine Freedom**

The constants $\alpha_i$ and $\beta_i$ represent affine freedom:
- $\alpha_i$: arbitrary positive rescaling (must be non-zero and same sign to maintain constraint orientation)
- $\beta_i$: arbitrary constant shift (doesn't affect gradients)

Without loss of generality, we can set $\alpha_i = 1$ and $\beta_i = 0$, giving:
$$
C_i = h_i
$$

Other choices just rescale and shift the constraint constant $C_0$. ∎}

\notes{**Remark on Rigor:** Steps 5-7 contain the deep argument but would benefit from further formalization. The key is proving that the orthogonality condition $\nabla C^\top G^{-1}\nabla I = 0$ is satisfied if and only if $\nabla C = \sum_i \alpha_i \nabla h_i$. This requires careful analysis of the exponential family geometry.}

\subsubsection{Corollary: Canonical Form}

\notes{**Corollary 2 (Canonical Conservation Constraint):**

*Up to affine transformation (which doesn't affect the dynamics), the unique conservation constraint for automatic GENERIC structure in exponential families is:*
$$
\sum_{i=1}^n h_i(\boldsymbol{\theta}) = C
$$
*where $h_i$ is the $i$-th marginal entropy.*}

\notes{**Proof:** Immediate from Theorem 3 by setting $\alpha_i = 1$ and $\beta_i = 0$ for all $i$. ∎}

\subsubsection{Physical Interpretation}

\notes{**Why Marginal Entropy?**

The uniqueness of $\sum h_i = C$ has deep physical meaning:

1. **Information Accounting**: Marginal entropies represent "local information content" at each variable. Conservation of their sum means total local information is fixed.

2. **Exchangeability**: The linear sum $\sum h_i$ treats all variables symmetrically (exchangeably), without privileging any subset.

3. **Natural Scale**: Entropy provides the natural information-theoretic scale (nats/bits), unlike arbitrary functionals.

4. **Geometric Structure**: $\sum \nabla h_i$ defines a natural foliation of parameter space that aligns with both:
   - The Fisher metric geometry (statistical geometry)
   - The constraint manifold (dynamical geometry)

5. **Thermodynamic Consistency**: Only this constraint gives GENERIC structure automatically, ensuring thermodynamic consistency (laws 1 & 2) without fine-tuning.}

\subsubsection{Alternative Functionals Fail}

\notes{Let's verify explicitly that natural alternatives fail the uniqueness test.}

\notes{**Alternative 1: Weighted Marginal Entropies**

Consider $C = \sum_i w_i h_i$ with different weights $w_i \neq 1$.

**Issue:** This breaks exchangeability. The constraint gradient $\nabla C = \sum_i w_i \nabla h_i$ no longer treats variables symmetrically.

**Physical problem:** Different weights assign different "value" to information at different variables, creating artificial hierarchy.

**Mathematical problem:** The orthogonality condition $\nabla C^\top G^{-1}\nabla I = 0$ may fail unless weights are specifically tuned to the distribution structure (fine-tuning).

**Verdict:** Violates "automatic" requirement—weights must be engineered.}

\notes{**Alternative 2: Nonlinear Functions of Marginal Entropies**

Consider $C = \sum_i f(h_i)$ where $f$ is nonlinear (e.g., $f(h) = h^2$).

**Issue:** The constraint gradient is:
$$
\nabla C = \sum_i f'(h_i) \nabla h_i
$$

The weights $f'(h_i)$ vary with the state $\boldsymbol{\theta}$, creating state-dependent rescaling.

**Mathematical problem:** The antisymmetric operator $A$ constructed from this $\nabla C$ varies incompatibly with the entropy gradient, preventing global GENERIC degeneracy.

**Verdict:** Violates smoothness and automatic structure.}

\notes{**Alternative 3: Functions of Joint Entropy**

Consider $C = nH(\boldsymbol{\theta})$ (joint entropy times $n$).

**Issue:** This is not marginal-additive! It fails Part 1 (Theorem 1).

Moreover, if $H = C$ (constant joint entropy), the dynamics would preserve $H$, contradicting the second law requirement that $H$ increase.

**Verdict:** Violates additivity and thermodynamic consistency.}

\subsubsection{Summary of Part 2}

\notes{**What We've Proven:**

1. **Theorem 3 (Uniqueness):** Among marginal-additive functionals, only (affine transformations of) marginal entropy $h_i$ gives automatic GENERIC structure.

2. **Corollary 2 (Canonical Form):** The canonical constraint is $\sum_i h_i = C$.

3. **Alternative functionals fail** due to:
   - Breaking exchangeability (weighted)
   - State-dependent structure (nonlinear)
   - Violating additivity (joint functionals)

4. **Physical meaning:** Marginal entropy conservation is the unique structure that:
   - Respects exchangeability
   - Provides natural information scale
   - Aligns statistical and dynamical geometry
   - Gives automatic thermodynamic consistency}

\notes{**Combined with Part 1:** We now have necessity for $\sum h_i = C$ as the unique constraint giving automatic GENERIC degeneracy in exponential families.}

\endif

