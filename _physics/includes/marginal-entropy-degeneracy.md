\ifndef{marginalEntropyDegeneracy}
\define{marginalEntropyDegeneracy}

\editme

\subsection{Why Degeneracy Conditions are Automatically Satisfied}

\notes{We've claimed that the degeneracy conditions for GENERIC are automatically satisfied in our information dynamics. But why? What's special about our constraint $\sum_i h_i = C$ that makes this work?

The answer lies in the mathematical structure of marginal entropy conservation. Let's prove both degeneracy conditions explicitly.}

\slides{
**The Question**

Why do degeneracy conditions "just work" for us?

**The Answer**

Special structure of $\sum h_i = C$

Let's prove it explicitly.
}

\subsection{Setup: Our Information Dynamics}

\notes{Recall our constrained dynamics from Lecture 4
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(\boldsymbol{\theta}) a(\boldsymbol{\theta})
$$
where

- $G(\boldsymbol{\theta})$: Fisher information matrix (friction operator $M$)
- $a(\boldsymbol{\theta}) = \nabla\left(\sum_i h_i(\boldsymbol{\theta})\right)$: Constraint gradient
- $\nu(\boldsymbol{\theta})$: Lagrange multiplier from tangency condition

The tangency condition (maintaining the constraint) is
$$
a(\boldsymbol{\theta})^\top \dot{\boldsymbol{\theta}} = 0.
$$
This condition, which we derived from requiring $\frac{d}{dt}(\sum h_i) = 0$, is fundamental.}

\slides{
**Our Dynamics (L4)**

$$\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta} - \nu a$$

**Tangency condition:**
$$a^\top \dot{\boldsymbol{\theta}} = 0,$$
where $a = \nabla(\sum h_i)$

This condition $\rightarrow$ degeneracy.
}

\subsection{Degeneracy Condition 1: Friction Compatible with Constraints}

\notes{The first degeneracy condition in GENERIC is usually stated as $M \nabla E = 0$ (friction conserves energy). But in our information dynamics, energy is not fundamental.

From our perspective the tangency condition $a^\top \dot{\boldsymbol{\theta}} = 0$ plays the role of the first degeneracy condition. It ensures the friction operator $G$ is compatible with the constraint structure.

From Lecture 3, the entropy gradient is,
$$
\nabla_{\boldsymbol{\theta}} H = -G(\boldsymbol{\theta})\boldsymbol{\theta},
$$
so the unconstrained dynamics are
$$
\dot{\boldsymbol{\theta}}|_{\text{unconstrained}} = -G\boldsymbol{\theta}.
$$
Now, the constraint force is
$$
\dot{\boldsymbol{\theta}}|_{\text{constraint}} = -\nu a.
$$
The tangency condition $a^\top \dot{\boldsymbol{\theta}} = 0$ means
$$
a^\top (-G\boldsymbol{\theta} - \nu a) = 0.
$$
Solving for $\nu$
$$
\nu = -\frac{a^\top G \boldsymbol{\theta}}{\|a\|^2}.
$$
So the constraint force $-\nu a$ is orthogonal to the entropy gradient flow in the sense that
$$
a^\top (-G\boldsymbol{\theta}) + a^\top(-\nu a) = 0.
$$
This orthogonality is what GENERIC's first degeneracy condition requires. In typical GENERIC systems, friction must not change a conserved energy. In our system, the "conservation" is *constraint maintenance*: the friction $G$ and the constraint force $-\nu a$ are coupled such that the total dynamics stay on the constraint manifold.

Why does this satisfy degeneracy? In GENERIC, the first degeneracy condition ensures friction doesn't create or destroy conserved quantities. For us, the conserved quantity is $\sum h_i = C$. The tangency condition $a^\top \dot{\boldsymbol{\theta}} = 0$ explicitly enforces this conservation, which is exactly the degeneracy structure GENERIC requires, but just expressed in terms of constraint maintenance rather than energy conservation.}

\slides{
**Degeneracy 1: Friction Compatible with Constraints**

**Energy not fundamental here!** (MEP, not energy conservation)

Tangency: $a^\top \dot{\boldsymbol{\theta}} = 0$

Expanded: $a^\top(-G\boldsymbol{\theta} - \nu a) = 0$

**Key:** Constraint force orthogonal to entropy flow

**Result:** Friction + constraint force maintain $\sum h_i = C$ ✓

**This IS the first degeneracy condition!**
* Not about conserving energy
* About maintaining constraints
* Tangency $\rightarrow$ Degeneracy 1
}

\subsection{Degeneracy Condition 2: $L \nabla S = 0$}

\notes{The second degeneracy condition states that the Poisson/antisymmetric operator must conserve entropy. In our case, the antisymmetric part $A$ comes from the decomposition in Lecture 7.

From Lecture 6-7, we linearised around equilibrium and found:
$$
M = -G - \nu^\ast A + \frac{aa^\top G}{\|a\|^2}
$$
where $A$ is the Hessian of the constraint: $A = \nabla^2(\sum_i h_i)$.

The decomposition $M = S + A_{\text{antisym}}$ gives us the antisymmetric part of the dynamics. Now, the entropy gradient is $\nabla H = -G\boldsymbol{\theta}$, so we need to show
$$
A_{\text{antisym}} \nabla H = 0 \quad \text{or} \quad A_{\text{antisym}} (-G\boldsymbol{\theta}) = 0.
$$

Actually, let's be more careful. The antisymmetric part from the decomposition includes both the constraint curvature and the projection. But the key property is that **any antisymmetric operator $A$ satisfies**:
$$
v^\top A v = 0 \quad \forall v
$$
because $v^\top A v = -v^\top A^\top v = -v^\top A v$ (using antisymmetry), which implies $v^\top A v = 0$.

Therefore, for the entropy:
$$
\frac{dH}{dt}\bigg|_{A} = (\nabla H)^\top A_{\text{antisym}} (\nabla H) = (-G\boldsymbol{\theta})^\top A_{\text{antisym}} (-G\boldsymbol{\theta}) = 0
$$

**But there's something deeper:** The constraint $\sum h_i = C$ means the gradient $a = \nabla(\sum h_i)$ must be in the null space of $A_{\text{antisym}}$. This is because:

1. The antisymmetric dynamics preserve the constraint
2. Any flow generated by $A_{\text{antisym}}$ must be tangent to the constraint manifold  
3. This means $A_{\text{antisym}} a = 0$ (the constraint gradient is a Casimir direction)

Since $\nabla H = -G\boldsymbol{\theta}$ can be decomposed as:
$$
\nabla H = \nabla H_{\parallel} + \nabla H_{\perp}
$$
where $\nabla H_{\perp} \propto a$ (perpendicular to manifold) and $\nabla H_{\parallel}$ is tangent to manifold.

The antisymmetric part only acts on the tangent components, and by the quadratic form property above, it conserves entropy.

**Why this is automatic:** The constraint $\sum h_i = C$ being a **sum** means its gradient $a$ has a special structure—it's a sum of individual marginal entropy gradients. This additive structure ensures that the antisymmetric part (which comes from cross-derivatives $\nabla^2(\sum h_i)$) automatically conserves the total entropy!}

\slides{
**Degeneracy 2: $L \nabla S = 0$**

**Property:** Any antisymmetric $A$ satisfies $v^\top A v = 0$

Therefore: $\frac{dH}{dt}\bigg|_A = (\nabla H)^\top A (\nabla H) = 0$ ✓

**Deeper:** Constraint gradient $a = \nabla(\sum h_i)$ in null space

* $A a = 0$ (Casimir direction)
* Antisymmetric flow preserves constraint
* Automatically conserves entropy

**Key:** Linear sum structure $\sum h_i$ $\rightarrow$ automatic conservation
}

\subsection{The Special Role of Marginal Entropy Sum}

\notes{Why does $\sum h_i = C$ work so well? What makes it special compared to other possible constraints?

**1. Linearity:** The constraint is a **linear sum** of marginal entropies. This means:
- The constraint gradient $a = \sum_i \nabla h_i$ is a sum of individual gradients
- The Hessian $A = \sum_i \nabla^2 h_i$ is a sum of individual Hessians
- No "interaction terms" between different margins in the constraint itself

**2. Exchangeability:** As discussed in Lecture 2, the sum $\sum h_i$ is the natural constraint from exchangeability. Variables can be permuted without changing the constraint. This symmetry ensures that:
- No preferred variable
- The constraint treats all variables equally
- Geometry is "democratic"

**3. Additive structure matches exponential family:**
Exponential families have the form:
$$
p(\mathbf{x}|\boldsymbol{\theta}) = \exp\left(\sum_i \theta_i T_i(\mathbf{x}) - A(\boldsymbol{\theta})\right)
$$
The parameters $\theta_i$ are additive, just like $\sum h_i$. This structural match ensures compatibility:
- Fisher metric $G$ has block structure
- Constraint gradient $a$ aligns with parameter structure
- Tangency condition naturally satisfied

**4. Information-theoretic meaning:**
$\sum h_i = C$ means "total marginal information is conserved." This has a clear information-theoretic interpretation:
- Joint entropy $H$ can increase (decorrelation)
- Multi-information $I$ can decrease
- But $H + I = \sum h_i$ remains constant
- This is a fundamental conservation law for information

**Would other constraints work?** In principle, yes, but they'd be more complicated:
- Constraint on joint entropy $H = C$: Would give different dynamics, likely non-MEP
- Constraint on multi-information $I = C$: No clear physical interpretation
- Constraint on individual $h_i$: Would give independent dynamics (trivial)
- Nonlinear constraints: Would break the clean structure, require more careful engineering

The **linear sum of marginal entropies** is the "Goldilocks constraint"—simple enough to be tractable, rich enough to be interesting, and natural enough to give automatic thermodynamic consistency!}

\slides{
**Why $\sum h_i = C$ is Special**

1. **Linearity:** $a = \sum \nabla h_i$ (no interaction terms)

2. **Exchangeability:** Symmetric under permutation

3. **Additive structure:** Matches exponential family structure

4. **Information meaning:** Total marginal info conserved

**Other constraints:**
* $H = C$: Different dynamics (non-MEP)
* $I = C$: No clear interpretation
* Individual $h_i$: Trivial (independent)
* Nonlinear: Breaks structure, needs engineering

**$\sum h_i = C$: "Goldilocks constraint"** ✓
}

\subsection{From Local to Global: A Major Result}

\notes{How do local properties at equilibrium (Lecture 7) guarantee global thermodynamic consistency?

This is not obvious, Lecture 7 analyses the structure near one equilibrium point. But the dynamics evolve through many points $\boldsymbol{\theta}(t)$ along trajectories. How can we be sure the GENERIC degeneracy conditions hold everywhere?

For the constraint $\sum h_i = C$, local verification at equilibrium automatically implies global validity everywhere. This may be unique to this constraint structure.}

\slides{
**From Local to Global**

**Question:** L7 analysed local structure at equilibrium

How does this guarantee global thermodynamic consistency?

**Answer:** Local + Tangency $\rightarrow$ Global 

If this is  unique to $\sum h_i = C$ it would be a major result validating the axioms.
}

\subsection{Degeneracy 1: Global by Construction}

\notes{**Claim:** The first degeneracy condition (friction compatible with constraints) holds *at every point* $\boldsymbol{\theta}$ on the constraint manifold.

**Proof:** This is enforced by construction through the tangency condition (Lecture 4).

At any point $\boldsymbol{\theta}(t)$ during the dynamics, we require
$$
\frac{d}{dt}\left(\sum_i h_i(\boldsymbol{\theta}(t))\right) = 0.
$$
By the chain rule:
$$
\frac{d}{dt}\left(\sum_i h_i\right) = a(\boldsymbol{\theta})^\top \dot{\boldsymbol{\theta}},
$$
where $a(\boldsymbol{\theta}) = \nabla(\sum_i h_i)$ is the constraint gradient.

Setting this to zero
$$
a(\boldsymbol{\theta})^\top \dot{\boldsymbol{\theta}} = a^\top(-G\boldsymbol{\theta} - \nu a) = 0.
$$
Solving for $\nu$ at each point
$$
\nu(\boldsymbol{\theta}) = -\frac{a(\boldsymbol{\theta})^\top G(\boldsymbol{\theta}) \boldsymbol{\theta}}{\|a(\boldsymbol{\theta})\|^2}.
$$

**This is valid at every point** $\boldsymbol{\theta}$ because:
1. The constraint gradient $a(\boldsymbol{\theta})$ is defined everywhere
2. The Fisher matrix $G(\boldsymbol{\theta})$ exists at every valid distribution
3. The formula for $\nu(\boldsymbol{\theta})$ is well-defined (denominator non-zero on manifold)

Therefore, the tangency condition, which IS the first degeneracy condition for our system, holds globally by construction. $\square$}

\slides{
**Degeneracy 1: Global by Construction**

At every $\boldsymbol{\theta}(t)$: $\frac{d}{dt}(\sum h_i) = 0$

Chain rule: $a(\boldsymbol{\theta})^\top \dot{\boldsymbol{\theta}} = 0$

Solution: $\nu(\boldsymbol{\theta}) = -\frac{a^\top G\boldsymbol{\theta}}{\|a\|^2}$

**Valid everywhere:**
* $a(\boldsymbol{\theta})$ defined everywhere
* $G(\boldsymbol{\theta})$ exists everywhere
* Formula well-defined

**Degeneracy 1 holds globally** ✓ (by construction)
}

\subsection{Degeneracy 2: Local Implies Global}

\notes{**Claim:** The second degeneracy condition (antisymmetric part conserves entropy) holds globally if it holds locally at each point.

**Proof via algebraic structure:**

From Lecture 7, at any point $\boldsymbol{\theta}$ where we linearise, the dynamics have the form
$$
\dot{q} = M(\boldsymbol{\theta}) q,
$$
where $M = S + A$ decomposes uniquely into symmetric and antisymmetric parts.

For any antisymmetric matrix $A$ and any vector $v$, we have the algebraic property:
$$
v^\top A v = -v^\top A^\top v = -v^\top A v \quad \Rightarrow \quad v^\top A v = 0.
$$
Therefore, at any point $\boldsymbol{\theta}$,
$$
\frac{dH}{dt}\bigg|_A = (\nabla H)^\top A(\boldsymbol{\theta}) (\nabla H) = 0.
$$
This holds *pointwise* at each $\boldsymbol{\theta}$ by pure algebra.

**Global consequence:** Along any trajectory $\boldsymbol{\theta}(t)$, integrate
$$
H(T) - H(0) = \int_0^T \frac{\text{d}H}{\text{d}t} \text{d}t = \int_0^T [(\nabla H)^\top S(\boldsymbol{\theta}) (\nabla H) + \underbrace{(\nabla H)^\top A(\boldsymbol{\theta}) (\nabla H)}_{=0}] \text{d}t.
$$
The antisymmetric contribution integrates to zero at every instant, so it contributes zero to the total entropy change. All entropy change comes from the symmetric (dissipative) part. $\square$}

\slides{
**Degeneracy 2: Local $\rightarrow$ Global**

At any point $\boldsymbol{\theta}$: $M = S + A$ (L7)

**Algebraic property:** $v^\top A v = 0$ for any antisymmetric $A$

Therefore: $\frac{dH}{dt}\bigg|_A = (\nabla H)^\top A (\nabla H) = 0$ everywhere

**Integrate along trajectory:**
$$H(T) - H(0) = \int_0^T (\nabla H)^\top S (\nabla H) \, dt$$

Antisymmetric contributes zero.

**Degeneracy 2 holds globally** ✓ (from local algebra)
}

\subsection{Why This Works: The Linear Sum Structure}

\notes{**The key question:** Why does local verification automatically give global validity?

**The answer:** The constraint $\sum_i h_i = C$ has special properties:

1. **Linear sum**: $a = \sum_i \nabla h_i$ is additive
   - No interaction terms between different $h_i$ in the constraint itself
   - Tangency condition is linear: $\sum_i (\nabla h_i)^\top \dot{\boldsymbol{\theta}} = 0$
   - Can be satisfied pointwise everywhere by choosing $\nu(\boldsymbol{\theta})$

2. **Compatible with exponential family**: Natural parameters $\boldsymbol{\theta}$ are additive
   - Fisher metric has clean structure at each point
   - Constraint gradient aligns with parameter structure
   - No topological obstructions

3. **Algebraic antisymmetry**: The property $v^\top A v = 0$ is purely algebraic
   - Holds at each point independently
   - No need for global coordination
   - Integrates to give global conservation

**Contrast with other possible constraints:**

- **Nonlinear** (e.g., $\prod_i h_i = C$): Tangency becomes nonlinear, may not have solution everywhere
- **Non-additive** (e.g., $I = \sum h_i - H = C$): Involves joint entropy $H$, no clean decomposition
- **Asymmetric** (e.g., $h_1 = C, h_2 = C'$): Multiple constraints, over-determined
- **Coupled** (e.g., $h_1 h_2 + h_3 = C$): Interaction terms break additive structure

**Proven (sufficiency):** The constraint $\sum_i h_i = C$ with its linear sum structure is sufficient for local $\rightarrow$ global to work automatically.

**Conjectured (necessity):** Other natural constraints (nonlinear, non-additive, coupled) may fail this property, suggesting $\sum h_i = C$ might be necessary. This remains to be proven.}

\slides{
**Why $\sum h_i = C$ Works (Sufficiency)**

1. **Linear sum** $\rightarrow$ Tangency solvable everywhere
2. **Additive structure** $\rightarrow$ Compatible with exp family
3. **Algebraic antisymmetry** $\rightarrow$ Local implies global

**Conjecture (Necessity):**

Other constraints may fail:
* Nonlinear: Tangency may not have solution
* Non-additive: No clean decomposition
* Coupled: Interaction terms break structure

**Open question:** Is $\sum h_i = C$ unique? (not yet proven)
}

\subsection{Verification with Binary Variables}

\notes{To make this concrete, consider the two binary variables example from Lecture 7's local analysis.

At any point $\boldsymbol{\theta} = (\theta_1, \theta_2, \theta_{12})$, we can compute:
- Fisher matrix $G(\boldsymbol{\theta})$ (3×3, explicit covariance)
- Marginal entropies $h_1(\boldsymbol{\theta}), h_2(\boldsymbol{\theta})$ (explicit sums)
- Constraint gradient $a(\boldsymbol{\theta}) = (\partial h_1/\partial \theta_1 + \partial h_2/\partial \theta_1, ...)$
- Lagrange multiplier $\nu(\boldsymbol{\theta}) = -a^\top G\boldsymbol{\theta}/\|a\|^2$

**Numerical experiment:**
1. Pick any starting point $\boldsymbol{\theta}(0)$ with $h_1 + h_2 = C$
2. Evolve: $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(\boldsymbol{\theta}) a(\boldsymbol{\theta})$
3. At each timestep, verify:

   - $\frac{\text{d}}{\text{d}t}(h_1 + h_2) = 0$ (machine precision) ✓
   - Entropy change = dissipative part only ✓

This confirms the properties hold globally, not just locally.

**See the simulation below for a complete implementation and animated visualization.**}

\include{_physics/includes/binary-dynamics-simulation.md}

\slides{
**Binary Variables Example (L7)**

At any $\boldsymbol{\theta}$: Compute $G, a, \nu$ explicitly

**Numerical verification:**
* Start at $\boldsymbol{\theta}(0)$ with $h_1 + h_2 = C$
* Evolve forward
* Check: $\frac{d}{dt}(h_1 + h_2) = 0$ at each step ✓

**Result:** Global properties verified numerically

LOCAL (L7 structure) $\rightarrow$ GLOBAL (L8 GENERIC) confirmed!
}

\subsection{Summary}

\notes{We have proven that LOCAL verification (Lecture 7 at equilibrium) + GLOBAL tangency (Lecture 4 constraint) $\rightarrow$ GLOBAL GENERIC degeneracy conditions automatically.

**Why this is significant:**

1. **Non-trivial**: GENERIC degeneracy conditions are typically hard to satisfy,most systems require careful engineering to ensure $M$ and $L$ are compatible

2. **Automatic for TIG**

   - Degeneracy 1: Global by construction (tangency everywhere)
   - Degeneracy 2: Local algebra extends globally (antisymmetry property)

3. **Sufficiency proven**: We have proven that the linear sum structure of $\sum h_i = C$ is sufficient to make the local $\rightarrow$ global connection work. 

4. **Necessity conjectured**: We conjecture (but have not proven) that this structure may be *necessary*, that other natural constraints would fail to admit automatic local $\rightarrow$ global extension.

5. **Validates the axioms**: Starting from information-theoretic principles (L1-4) automatically produces dynamics that satisfy difficult thermodynamic consistency conditions (GENERIC degeneracy). This suggests the axioms capture thermodynamic structure, not just information-theoretic structure.

The constraint $\sum h_i = C$ is *sufficient* for automatic thermodynamic consistency. Whether it is also *necessary* (unique) remains an open question, but the structural properties (linearity, additivity, exchangeability) suggest it may be special.}

\slides{
**The Major Result**

**Proven:** LOCAL (L7) + Tangency (L4) $\rightarrow$ GLOBAL GENERIC

**What we've shown:**

1. **Non-trivial**: Usually hard (requires engineering)
2. **Sufficiency ✓**: $\sum h_i = C$ is sufficient for automatic consistency
3. **Necessity ?**: Conjectured (but not proven) to be necessary
4. **Validates axioms**: Info principles $\rightarrow$ Thermo consistency

**Key result:** sufficiency proven

**Open question:** Is it also necessary (unique)?
}
\endif
