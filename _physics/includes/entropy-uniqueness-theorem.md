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

\notes{**Exponential Family Assumptions:**

We assume a regular minimal exponential family with base measure $m(x)$ independent of $\boldsymbol{\theta}$:
$$
p(x|\boldsymbol{\theta}) = \exp(\boldsymbol{\theta}^\top T(x) - A(\boldsymbol{\theta}))m(x)
$$

In this setting, the entropy gradient has the structure $\nabla H = -G\boldsymbol{\theta}$ where $H$ is the differential entropy and $G$ is the Fisher information matrix.

**Marginal Distribution:**

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

2. **Concavity**: $h_i$ is concave in $\boldsymbol{\theta}$ (for exponential families)

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
C_i(\boldsymbol{\theta}^{(i)}) = \alpha_i h_i(\boldsymbol{\theta}^{(i)}) + \beta_i
$$
*where $\alpha_i \in \mathbb{R} \setminus \{0\}$ and $\beta_i \in \mathbb{R}$ are constants.*}

\notes{**Proof:**

We prove this through a series of necessary conditions that uniquely determine $C_i$.

**Step 1: GENERIC Degeneracy Requirements**

For GENERIC structure $\dot{\boldsymbol{\theta}} = L\nabla E + M\nabla S$, we need:
$$
M\nabla E = 0, \quad L\nabla S = 0
$$

where:
- $M$ is the friction operator (symmetric, positive semi-definite)
- $L$ is the Poisson operator (antisymmetric)
- $E$ is energy, $S$ is entropy

For information dynamics:
- $M = G$ (Fisher information)
- $S = H$ (joint entropy)
- The antisymmetric part $L$ emerges from the constraint projector

**Important:** We do **not** use $M = G$ to infer $\nabla E = 0$ (which would trivialise the energy). The uniqueness proof relies only on the orthogonality condition in Step 3.

**Step 2: The Key Degeneracy - Conservation of Joint Entropy**

The critical condition is:
$$
L\nabla H = 0
$$

where $\nabla H = -G\boldsymbol{\theta}$ is the joint entropy gradient.

This says: the antisymmetric (conservative) part of the dynamics must conserve joint entropy $H$.

From Lecture 7, we proved this is automatically satisfied when $C = \sum h_i$. Now we ask: **Is this the unique constraint with this property?**

**Step 3: Orthogonality Condition**

For automatic degeneracy, the constraint gradient $a = \nabla C$ must satisfy an orthogonality condition with respect to $\nabla H$.

**Derivation:** For the projected flow $\dot{\boldsymbol{\theta}} = \Pi b$ with the $G$-orthogonal projector
$$
\Pi = I - G^{-1}a(a^\top G^{-1}a)^{-1}a^\top, \quad a = \nabla C
$$
onto the tangent space $\ker a^\top$, the antisymmetric part that enforces tangency annihilates $\nabla H$ if and only if
$$
\nabla C^\top G^{-1}\nabla H = 0.
$$

(This is just the GENERIC degeneracy condition $L\nabla H = 0$ expressed via the $G$-orthogonal projector. See Lecture 7 for the full construction.)

This orthogonality is the key to uniqueness.

**Step 4: Independence Limit and Entropy Decomposition**

From Part 1, we have $C = \sum_i C_i(\boldsymbol{\theta}^{(i)})$. 

In the independence limit $\varepsilon \to 0$ where $G = \mathrm{diag}(G^{(1)}, \ldots, G^{(n)}) + O(\varepsilon)$, the entropy gradients have block structure.

For exponential families, the **key identity** is:
$$
\nabla H(\boldsymbol{\theta}) = -G(\boldsymbol{\theta})\boldsymbol{\theta}
$$

The multi-information is $I = \sum_i h_i - H$, so:
$$
\nabla I = \sum_i \nabla h_i - \nabla H
$$

Rearranging:
$$
\nabla H = \sum_i \nabla h_i - \nabla I
$$

At $\varepsilon = 0$ (independence):
- $\nabla h_i = -G^{(i)}\boldsymbol{\theta}^{(i)}$ (block-supported in block $i$)
- $\nabla I = 0 + O(\varepsilon)$ (vanishes as interactions turn off)
- Therefore: $\nabla H = \sum_i \nabla h_i$ at leading order

**Step 5: Annihilator Lemma (Product Fisher Geometry)**

In the independence limit $G = \bigoplus_i G^{(i)}$, define the $G^{-1}$-inner product on block $i$:
$$
\langle u, v \rangle_i := u^\top (G^{(i)})^{-1} v
$$

**Lemma:** $\nabla h_i$ is the Riesz representer of $-\boldsymbol{\theta}^{(i)}$:
$$
(G^{(i)})^{-1}\nabla h_i = -\boldsymbol{\theta}^{(i)}
$$

Consider any antisymmetric operator $L^{(i)}$ supported on block $i$ such that $L^{(i)}\nabla h_i = 0$. The image of such operators is contained in $(\mathrm{span}\{\nabla h_i\})^{\perp_i}$ (orthogonal w.r.t. $\langle \cdot, \cdot \rangle_i$).

**Key Fact:** The set of vectors annihilated by **all** such antisymmetric $L^{(i)}$ (i.e., $L^{(i)}v = 0$ for every $L^{(i)}$ with $L^{(i)}\nabla h_i = 0$) is exactly $\mathrm{span}\{\nabla h_i\}$.

*Proof (by construction):* If $v \notin \mathrm{span}\{\nabla h_i\}$, choose $v \in (\mathrm{span}\{\nabla h_i\})^{\perp_i} \setminus \{0\}$ (explicitly orthogonal to $\nabla h_i$), then pick $w \in (\mathrm{span}\{\nabla h_i\})^{\perp_i}$ with $\langle w, v \rangle_i \neq 0$, and define:
$$
L^{(i)}u := \langle u, v \rangle_i w - \langle u, w \rangle_i v
$$

Then $L^{(i)}$ is antisymmetric, $L^{(i)}\nabla h_i = 0$ (since $\nabla h_i \perp w, v$), but $L^{(i)}v = \langle v, v \rangle_i w \neq 0$. Hence only $v \in \mathrm{span}\{\nabla h_i\}$ can be annihilated by all such $L^{(i)}$. ∎

**Step 6: Application to Constraint Gradient**

For **automatic degeneracy**, we require:
- $L\nabla H = 0$ (antisymmetric part conserves joint entropy)
- This must hold for **every** block-supported antisymmetric $L = \bigoplus_i L^{(i)}$ with $L^{(i)}\nabla h_i = 0$ in each block

At $\varepsilon = 0$, we have $\nabla H = \sum_i \nabla h_i$, so the condition $L\nabla H = 0$ becomes:
$$
\sum_i L^{(i)}\nabla h_i = 0
$$

This is automatically satisfied when $L^{(i)}\nabla h_i = 0$ for each $i$.

For the constraint, we also need $L\nabla C = 0$ for the same class of operators. With $\nabla C = \sum_i \nabla C_i$:
$$
\sum_i L^{(i)}\nabla C_i = 0 \quad \text{for all } L^{(i)} \text{ with } L^{(i)}\nabla h_i = 0
$$

Since the blocks are independent and the equation must hold for **all** choices of such $L^{(i)}$ in each block, we conclude:
$$
L^{(i)}\nabla C_i = 0 \quad \text{for all } L^{(i)} \text{ with } L^{(i)}\nabla h_i = 0
$$

**Step 7: Uniqueness from Annihilator**

By the annihilator lemma (Step 5), if $L^{(i)}\nabla C_i = 0$ for every antisymmetric $L^{(i)}$ satisfying $L^{(i)}\nabla h_i = 0$, then:
$$
\nabla C_i \in \mathrm{span}\{\nabla h_i\}
$$

Therefore:
$$
\nabla C_i = \alpha_i \nabla h_i
$$

for some constant $\alpha_i \neq 0$ (independent of $\boldsymbol{\theta}^{(i)}$ on each connected component).

Integrating:
$$
C_i(\boldsymbol{\theta}^{(i)}) = \alpha_i h_i(\boldsymbol{\theta}^{(i)}) + \beta_i
$$

This establishes uniqueness (up to affine transformation).

**Step 8: Extension to Small Coupling**

For small $\varepsilon > 0$, the span condition $\nabla C_i \in \mathrm{span}\{\nabla h_i\}$ persists by continuity of the kernels and images of $L^{(i)}(\varepsilon)$ and nondegeneracy of $\langle \cdot, \cdot \rangle_i$. The annihilator argument remains robust.

Therefore $C_i(\varepsilon) = \alpha_i(\varepsilon) h_i(\varepsilon) + \beta_i(\varepsilon)$ with $\alpha_i(\varepsilon)$ nonzero and continuous. Any global monotone rescalings can be absorbed into the constraint level $C_0$.

**Step 9: Affine Freedom**

The constants $\alpha_i$ and $\beta_i$ represent affine freedom:
- $\alpha_i$: arbitrary non-zero rescaling (must not be zero)
- $\beta_i$: arbitrary constant shift (doesn't affect gradients)

**Sign convention:** A global rescaling $C \mapsto \gamma C + \delta$ with $\gamma > 0$ preserves the constraint foliation orientation. Allowing mixed signs in $\{\alpha_i\}$ changes the orientation componentwise; while mathematically valid, the robustness condition (invariance under local flows in the independence limit) typically requires all $\alpha_i$ to share the same sign. After a global monotone reparametrization, we can assume all $\alpha_i > 0$.

Without loss of generality, we can set $\alpha_i = 1$ and $\beta_i = 0$, giving:
$$
C_i = h_i
$$

Other choices just rescale and shift the constraint constant $C_0$. ∎}

\subsubsection{Corollary: Canonical Form}

\notes{**Corollary 2 (Canonical Conservation Constraint):**

*Up to affine transformation (which doesn't affect the dynamics), the unique conservation constraint for automatic GENERIC structure in exponential families is:*
$$
\sum_{i=1}^n h_i(\boldsymbol{\theta}^{(i)}) = C
$$
*where $h_i(\boldsymbol{\theta}^{(i)})$ is the $i$-th marginal entropy, depending on $\boldsymbol{\theta}$ only through the marginal parameters $\boldsymbol{\theta}^{(i)}$.*}

\notes{**Proof:** Immediate from Theorem 3 by setting $\alpha_i = 1$ and $\beta_i = 0$ for all $i$. ∎}

\notes{**Remark (Monotone Transformations):**

When we say "up to affine transformation," we mean:

1. **Global monotone reparametrizations** like $f(\sum_i h_i) = C'$ preserve the constraint leaves (same foliation, different level sets).

2. **Componentwise non-affine** transformations like $\sum_i f_i(h_i) = C'$ are **ruled out** by the state-dependent weight argument (Alternative 2 above). Only affine $f_i$ (constant coefficients $\alpha_i$) survive the annihilator test.

Therefore, the canonical form $\sum_i h_i = C$ is unique up to global scaling and shift, not componentwise transformations.}

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

\notes{**Alternative 1: Multi-Information Conservation ($I = C$)**

Consider $I = \sum_i h_i - H = C$ (multi-information constant).

**The gradient at $\varepsilon = 0$:**

The multi-information gradient is:
$$
\nabla I = \sum_i \nabla h_i - \nabla H
$$

In the independence limit where $G = \mathrm{diag}(G^{(1)}, \ldots, G^{(n)})$:
$$
\nabla H = -G\boldsymbol{\theta} = -\sum_i G^{(i)}\boldsymbol{\theta}^{(i)}
$$

and:
$$
\nabla h_i = -G^{(i)}\boldsymbol{\theta}^{(i)}
$$

Therefore
$$
\nabla I = \sum_i \left(-G^{(i)}\boldsymbol{\theta}^{(i)}\right) - \left(-\sum_i G^{(i)}\boldsymbol{\theta}^{(i)}\right) = 0
$$
exactly at $\varepsilon = 0$.

**Critical Obstruction:** At $\varepsilon = 0$, $\nabla I = 0$ exactly. For $\varepsilon > 0$, $\nabla I$ is purely interaction-supported and cannot be written as $\sum_i \alpha_i \nabla h_i$ with **constant** $\alpha_i$.

**Annihilator Test:** Since $\nabla I$ vanishes at $\varepsilon = 0$ and is purely interaction-supported for $\varepsilon > 0$, it cannot lie in $\bigoplus_i \mathrm{span}\{\nabla h_i\}$ with constant coefficients. Hence it fails the annihilator/additivity test.

**Verdict:** Fails additivity (Part 1). Not marginal-additive at leading order.}

\notes{**Alternative 2: Nonlinear Functions of Marginal Entropies**

Consider $C = \sum_i h_i^2$ (quadratic in marginal entropies).

**The gradient:**
$$
\nabla C = \sum_i 2h_i \nabla h_i
$$

The state-dependent weights $2h_i$ create incompatibility.

**Two-Block Example:**

Take two blocks with entropies $h_1(\boldsymbol{\theta}^{(1)})$ and $h_2(\boldsymbol{\theta}^{(2)})$. Consider two different local flows:

1. Flow $b^{(1)}$ supported in block 1 increases $h_1$ by $\delta$
2. Flow $b^{(2)}$ supported in block 2 increases $h_2$ by $\delta$

The constraint normal direction is $\nabla C = 2h_1 \nabla h_1 + 2h_2 \nabla h_2$.

Under flow $b^{(1)}$:
- $h_1 \to h_1 + \delta$
- The normal direction changes to $2(h_1+\delta) \nabla h_1 + 2h_2 \nabla h_2$
- Relative weight: $(h_1+\delta) : h_2$

Under flow $b^{(2)}$:
- $h_2 \to h_2 + \delta$
- The normal direction changes to $2h_1 \nabla h_1 + 2(h_2+\delta) \nabla h_2$
- Relative weight: $h_1 : (h_2+\delta)$

**Incompatibility:** The two flows map the constraint leaves to different foliations (different normal bundle structures). For foliation invariance, all local flows must preserve the same leaf structure, but the state-dependent weights $\phi_i'(h_i) = 2h_i$ prevent this.

**Annihilator Test:** The state-dependent weights mean $\nabla C \notin \bigoplus_i \mathrm{span}\{\nabla h_i\}$ with **constant** coefficients. The annihilator condition requires constant $\alpha_i$ (Step 7), ruling out any nonlinear $\phi_i$ unless $\phi_i'$ is constant, i.e., $\phi_i$ is affine.

**Verdict:** Violates the annihilator/uniqueness requirement. Only affine $\phi_i$ (constant weights) survive.}

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

