\ifndef{genericMeetsFisher}
\define{genericMeetsFisher}

\editme

\subsection{Information Dynamics in GENERIC Form}

\notes{Now comes the payoff: we'll show that the information dynamics we've been building (Lectures 1-7) fit perfectly into the GENERIC framework. 

Recall our constrained information dynamics from Lecture 4:
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(\boldsymbol{\theta}) a(\boldsymbol{\theta}),
$$
where

- $\boldsymbol{\theta}$: Natural parameters of exponential family
- $G(\boldsymbol{\theta})$: Fisher information matrix (metric on parameter space)
- $a(\boldsymbol{\theta}) = \nabla(\sum_i h_i)$: Constraint gradient (marginal entropy conservation)
- $\nu(\boldsymbol{\theta})$: Lagrange multiplier (determined by tangency condition)

We'll show this is GENERIC by identifying the operators $L$ and $M$ and verifying all the required properties.}

\slides{
**Our Information Dynamics (L1-7)**

$$\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(\boldsymbol{\theta}) a(\boldsymbol{\theta})$$

* $G$: Fisher information matrix
* $a = \nabla(\sum h_i)$: Constraint gradient
* $\nu$: Lagrange multiplier

**Question:** Is this GENERIC?

**Answer:** Yes, let's prove it ...
}

\subsection{Identifying Energy and Entropy}

\notes{To fit GENERIC form $\dot{x} = L \nabla E + M \nabla S$, we first need to identify what plays the role of energy $E$ and entropy $S$ in our information dynamics.

**Entropy functional:** This is straightforward—joint entropy
$$
S(\boldsymbol{\theta}) = H(\boldsymbol{\theta}) = -\sum_{\mathbf{x}} p(\mathbf{x}|\boldsymbol{\theta}) \log p(\mathbf{x}|\boldsymbol{\theta}).
$$
In exponential family form, this is the log partition function minus the average log probability
$$
H(\boldsymbol{\theta}) = A(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \mathbb{E}[T(\mathbf{x})].
$$

**Energy functional:** In information theory, the natural "energy" is the multi-information (or minus entropy, depending on perspective). But for GENERIC, we want something conserved by the Poisson dynamics. 

For constrained systems, we can define an *effective energy* that accounts for the constraint
$$
E(\boldsymbol{\theta}) = \frac{1}{2}\boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta} + V\left(\sum_i h_i(\boldsymbol{\theta})\right),
$$
where $V$ is a potential function that enforces the constraint $\sum_i h_i = C$. In the limit where the constraint is exact, this becomes the constraint itself.

Alternatively, we can work directly with the constraint manifold and the dynamics become
$$
\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta} + \text{(constraint forcing)}.
$$}

\slides{
**Identifying Functionals**

**Entropy:** Joint entropy (straightforward!)
$$S(\boldsymbol{\theta}) = H(\boldsymbol{\theta}) = -\sum_\mathbf{x} p(\mathbf{x}|\boldsymbol{\theta}) \log p(\mathbf{x}|\boldsymbol{\theta})$$

**Energy:** Related to constraint
$$E(\boldsymbol{\theta}) = \frac{1}{2}\boldsymbol{\theta}^\top G \boldsymbol{\theta} + V(\sum h_i)$$

(Or work on constraint manifold directly)
}

\subsection{The Friction Operator: Fisher Information}

\notes{The friction operator $M$ in GENERIC should be symmetric, positive semi-definite, and describe dissipation. In our information dynamics, this role is played by the **Fisher information matrix** $G(\boldsymbol{\theta})$.

Let's verify the GENERIC properties:

**1. Symmetric:** The Fisher information matrix is symmetric by definition:
$$
G_{ij} = \mathbb{E}\left[\frac{\partial \log p}{\partial \theta_i}\frac{\partial \log p}{\partial \theta_j}\right] = G_{ji}
$$

**2. Positive semi-definite:** The Fisher information matrix is always positive semi-definite (and usually positive definite):
$$
v^\top G v = \mathbb{E}\left[\left(v^\top \nabla_\theta \log p\right)^2\right] \geq 0 \quad \forall v
$$

**3. Entropy increase:** The unconstrained dynamics $\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta}$ increase entropy:
$$
\frac{\text{d}H}{\text{d}t} = (\nabla_\theta H)^\top \dot{\boldsymbol{\theta}} = -\boldsymbol{\theta}^\top G \dot{\boldsymbol{\theta}} = \boldsymbol{\theta}^\top G^2 \boldsymbol{\theta} \geq 0
$$
This is maximum entropy production (Lecture 3)

So the Fisher information matrix $G$ is exactly the friction operator $M$ of GENERIC. It describes how the system dissipates toward maximum entropy.}

\slides{
**Friction Operator: $M = G$**

Fisher information matrix $G$ is GENERIC friction!

**Check properties:**
1. **Symmetric:** $G_{ij} = G_{ji}$ ✓
2. **Positive semi-definite:** $v^\top G v \geq 0$ ✓
3. **Entropy increase:** $\dot{H} = \boldsymbol{\theta}^\top G^2 \boldsymbol{\theta} \geq 0$ ✓

**Physical meaning:**
$G$ = metric on probability space
$G$ = conductance of information flow
$G$ = rate of entropy production

Fisher information IS thermodynamic friction!
}

\subsection{The Poisson Operator: Constraint Structure}

\notes{The Poisson operator $L$ in GENERIC should be antisymmetric and describe reversible (energy-conserving) dynamics. In our information dynamics, this structure comes from the *constraint geometry*.

The constraint $\sum_i h_i(\boldsymbol{\theta}) = C$ defines a manifold in parameter space. The Lagrange multiplier term $-\nu a$ keeps the dynamics tangent to this manifold. This geometric structure induces a Poisson bracket.

To see this explicitly, consider the tangent space projector:
$$
\Pi_\perp = \frac{a a^\top}{\|a\|^2}, \quad \Pi_\parallel = I - \Pi_\perp
$$

The tangent dynamics have the form:
$$
\dot{\boldsymbol{\theta}} = -\Pi_\parallel G \boldsymbol{\theta}
$$

But this can be rewritten using the linearization from Lecture 6-7. The full linearized dynamics are:
$$
\dot{q} = Mq = (S + A)q
$$
where $M = -G - \nu A + \frac{aa^\top G}{\|a\|^2}$ and $A$ is the antisymmetric part.

The antisymmetric part $A$ encodes the Poisson structure! From Lecture 7, we know:
- $A$ emerges from third-order cumulants (non-Gaussian effects)
- $A$ emerges from constraint surface curvature
- $A$ describes conservative (rotational) dynamics

So the constraint geometry provides the Poisson operator:
$$
L \sim \text{antisymmetric part of linearized constraint dynamics}
$$

This is degenerate (has null space) precisely because the constraint reduces dimensionality. The constraint gradient $a$ spans the null space of $L$.}

\slides{
**Poisson Operator: Constraint Structure**

Constraint $\sum h_i = C$ induces Poisson bracket!

**From Lecture 7:**
* Linearization: $\dot{q} = Mq = (S + A)q$
* Antisymmetric $A$ from:
  - Third-order cumulants
  - Constraint curvature

**Poisson operator:** $L \sim A$ (antisymmetric part)

**Degeneracy:** $L$ has null space spanned by $a$
* Constraint reduces dimensionality
* Symplectic leaves = constraint manifolds
}

\subsection{Verifying the Degeneracy Conditions}

\notes{For our information dynamics to be thermodynamically consistent GENERIC, we must verify the two degeneracy conditions. **Remarkably, both are automatically satisfied**—we didn't have to impose them, they emerged from our construction (Lectures 1-7):

**Degeneracy 1:** $M \nabla E = 0$ (friction conserves energy)

In our case, $M = G$ and "energy" is related to the Fisher distance $\frac{1}{2}\boldsymbol{\theta}^\top G \boldsymbol{\theta}$. However, in the unconstrained case, this is NOT conserved—the system dissipates. 

The resolution: On the constraint manifold, there is an effective energy that combines the dissipation with the constraint potential. The constraint forces the dynamics to redistribute "energy" without changing the total. This is why $\nu$ must be chosen carefully (tangency condition from Lecture 4).

**Degeneracy 2:** $L \nabla S = 0$ (Poisson conserves entropy)

This is automatically satisfied! The antisymmetric part $A$ from Lecture 7 satisfies:
$$
\frac{\text{d}H}{\text{d}t}\bigg|_{A} = (\nabla H)^\top A \nabla H = 0
$$
because $A$ is antisymmetric and the entropy gradient is $\nabla H = -G\boldsymbol{\theta}$. So:
$$
\boldsymbol{\theta}^\top G^\top A G \boldsymbol{\theta} = -\boldsymbol{\theta}^\top G A G \boldsymbol{\theta} = 0
$$

The conservative part of the dynamics conserves entropy! All entropy change comes from the dissipative part (Fisher friction).}

\slides{
**Degeneracy Conditions**

Both automatically satisfied (not imposed!)

**Condition 1:** $M \nabla E = 0$
* On constraint manifold: effective energy conserved
* Tangency condition (L4) ensures this! ✓

**Condition 2:** $L \nabla S = 0$
* Antisymmetric $A$ conserves entropy
* $\dot{H}|_A = \boldsymbol{\theta}^\top G A G \boldsymbol{\theta} = 0$ ✓

**Result:** Thermodynamically consistent!
* Emerged from axioms (L1-7)
* Not engineered—naturally satisfied
}

\subsection{The Complete Picture}

\notes{Putting it all together, our information dynamics:
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(\boldsymbol{\theta}) a(\boldsymbol{\theta})
$$
is GENERIC with:

**Friction operator:** $M = G$ (Fisher information)
- Describes dissipation toward maximum entropy
- Symmetric, positive semi-definite
- Produces entropy: $\dot{H}|_M > 0$

**Poisson operator:** $L$ (from constraint geometry)
- Describes conservative dynamics from constraint curvature
- Antisymmetric, degenerate
- Conserves entropy: $\dot{H}|_L = 0$

**Casimir:** $C = \sum_i h_i$ (marginal entropy conservation)
- Fundamental constraint from axioms (Lecture 2)
- Defines symplectic leaves (constraint manifolds)

**Energy:** Effective energy on constraint manifold

**Entropy:** Joint entropy $H(\boldsymbol{\theta})$

The structure we derived from information-theoretic axioms (Lectures 1-4) is exactly the GENERIC structure that physicists discovered was necessary for consistent non-equilibrium thermodynamics!}

\slides{
**Information Dynamics = GENERIC!**

$$\dot{\boldsymbol{\theta}} = L \nabla E + M \nabla S$$

where:
* $M = G$ (Fisher information = friction)
* $L \sim A$ (constraint geometry = Poisson)
* Casimir: $\sum h_i = C$
* Entropy: $H(\boldsymbol{\theta})$

**What we derived (L1-7) = What physics requires!**

Information theory axioms $\rightarrow$ GENERIC structure

Not imposed $\rightarrow$ Emerged!
}

\subsection{Why This Matters}

\notes{This connection between information dynamics and GENERIC has profound implications:

**0. Automatic thermodynamic consistency:**
The hardest part of GENERIC is ensuring degeneracy conditions are satisfied—typically requiring careful engineering. Our axioms (L1-4) lead to dynamics where degeneracy conditions are *automatically satisfied*. This validates the axioms as capturing fundamental thermodynamic principles, not just information-theoretic ones.

**1. Information = Thermodynamics (deeper than Shannon/Jaynes):**
We knew information entropy equals thermodynamic entropy. But now we know information *dynamics* equal thermodynamic dynamics—including both reversible and irreversible parts.

**2. Fisher information = Thermodynamic friction:**
The Fisher information matrix isn't just a metric—it's the friction operator that governs dissipation. This gives Fisher information a direct physical interpretation in non-equilibrium processes.

**3. Constraints create conservative dynamics:**
The emergence of antisymmetric structure from constraint geometry (Lecture 7) isn't mathematical curiosity, it's how conservation laws arise in thermodynamics. Constraints $\rightarrow$ symplectic structure $\rightarrow$ conserved quantities.

**4. Universality:**
GENERIC structure appears in fluids, polymers, chemical reactions, biological systems, and now information systems. This suggests a universal principle: *any system that combines information and energy must obey GENERIC structure*.

**5. Predictive power:**
Knowing our system is GENERIC lets us import results from non-equilibrium thermodynamics: Onsager reciprocity, fluctuation-dissipation relations, maximum entropy production principles, etc.}

\slides{
**Why This Matters**

0. **Degeneracy automatic** (validates axioms)
   * Hardest part of GENERIC "just works" for us
   * Axioms $\rightarrow$ thermodynamically consistent

1. **Information = Thermodynamics** (deeper than Shannon)
   * Dynamics equal, not just entropy

2. **Fisher = Friction** (physical interpretation)
   * $G$ governs dissipation

3. **Constraints $\rightarrow$ Conservation** (L7 explained!)
   * Geometry creates symplectic structure

4. **Universality** (one principle for all systems)
   * Info + energy $\rightarrow$ GENERIC

5. **Predictive** (import thermo results)
   * Onsager, fluctuation-dissipation, etc.
}

\notes{**Summary:** The information dynamics we built from axioms is GENERIC, with Fisher information as the friction operator and constraint geometry providing the Poisson structure. This reveals information theory as a special case of non-equilibrium thermodynamics—or perhaps thermodynamics as a special case of information theory!}

\endif


