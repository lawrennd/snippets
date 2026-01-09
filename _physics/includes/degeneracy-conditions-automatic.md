\ifndef{degeneracyConditionsAutomatic}
\define{degeneracyConditionsAutomatic}

\editme

\subsection{Automatic Degeneracy Conditions}

\notes{A remarkable feature of the inaccessible game is that the GENERIC degeneracy conditions, which are typically difficult to impose and verify, emerge *automatically* from the constraint structure.}

\subsubsection{The GENERIC Degeneracy Requirements}

\notes{Recall that standard GENERIC requires two degeneracy conditions for thermodynamic consistency:

**Degeneracy 1:** The entropy should be conserved by the reversible dynamics:
$$
A(\boldsymbol{\theta})\nabla H(\boldsymbol{\theta}) = 0
$$

**Degeneracy 2:** The energy should be conserved by the irreversible dynamics:
$$
S(\boldsymbol{\theta})\nabla E(\boldsymbol{\theta}) = 0
$$}

\notes{In most GENERIC applications, constructing operators $A$ and $S$ that satisfy both conditions requires significant effort. You must carefully design the operators to ensure the degeneracies hold at every point in state space.}

\slides{
**Standard GENERIC Degeneracies:**

1. $A\nabla H = 0$ (antisymmetric conserves entropy)
2. $S\nabla E = 0$ (symmetric conserves energy)

**Problem:** Hard to construct $A$, $S$ satisfying both.

*Usually requires careful hand-crafting*
}

\subsection{First Degeneracy: Automatic from Tangency}

\notes{In our framework, the first degeneracy $A\nabla H = 0$ holds automatically at every point on the constraint manifold. It comes from the constraint maintenance requirement:
$$
\mathbf{a}^\top \dot{\boldsymbol{\theta}} = 0
$$
where $\mathbf{a} = \nabla\left(\sum_i h_i\right)$ is the constraint gradient.}

\notes{This ensures that the dynamics remain tangent to the constraint surface at all times. The antisymmetric part $A$ inherits this tangency because it generates rotations on the constraint manifold. Since rotations conserve everything (by definition $\mathbf{z}^\top A\mathbf{z} = 0$ for antisymmetric $A$), and the rotations stay on the constraint surface, the first degeneracy is automatically satisfied.}

\slides{
**First Degeneracy (Automatic):**

Constraint maintenance: $\mathbf{a}^\top\dot{\boldsymbol{\theta}} = 0$

$\Rightarrow$ Dynamics tangent to surface

$\Rightarrow$ Antisymmetric part conserves entropy

$$\boxed{A\nabla H = 0 \text{ holds automatically}}$$

*By construction, not by assumption!*
}

\subsection{Second Degeneracy: From Constraint Gradient}

\notes{The second degeneracy is where our framework departs from standard GENERIC. In standard formulations, one requires $S\nabla E = 0$ where $E$ is thermodynamic energy. This must be verified case-by-case.}

\notes{In our framework, the marginal entropy constraint $\sum_i h_i = C$ plays the role that energy conservation plays in GENERIC. The constraint gradient $\mathbf{a}$ defines the degeneracy direction along which the dissipative operator vanishes:
$$
S\mathbf{a} = 0 \equiv S\nabla\left(\sum_i h_i\right) = 0.
$$}

\notes{This follows from the constraint tangency requirement: the symmetric part cannot have a component along the constraint gradient because that would violate conservation.}

\slides{
**Second Degeneracy (From Constraint):**

Our constraint: $\sum h_i = C$

$$S\nabla\left(\sum h_i\right) = 0$$

*Marginal entropy plays role of energy*

In thermodynamic limit: $\nabla\left(\sum h_i\right) \parallel \nabla E$
}

\newslide{Energy-Entropy Equivalence}

\notes{In Section 4 of the paper, we show that under certain conditions in the thermodynamic limit, the constraint gradient becomes asymptotically parallel to an energy gradient:
$$
\nabla\left(\sum_i h_i\right) \parallel \nabla E.
$$}

\notes{When this equivalence holds, our automatically-derived degeneracy condition $S\nabla(\sum_i h_i) = 0$ becomes equivalent to the standard GENERIC condition $S\nabla E = 0$. This connects our information-theoretic framework to classical thermodynamics.}

\slides{
**Thermodynamic Limit:**

$$\nabla\left(\sum h_i\right) \parallel \nabla E$$

Therefore:
$$S\mathbf{a} = 0 \Leftrightarrow S\nabla E = 0$$

*Information framework $\rightarrow$ classical thermodynamics*
}

\subsection{Why This Matters}

\notes{The automatic emergence of degeneracy conditions is profound because:

1. *No hand-crafting required:* We don't need to guess the form of $A$ and $S$ and verify they satisfy degeneracies. The structure emerges from the constrained dynamics.

2. *Global validity:* The degeneracies hold everywhere on the constraint manifold by construction, not just at specific points or in special cases.

3. *Information-first foundation:* Instead of starting with energy and thermodynamics and deriving information-theoretic properties, we start with information conservation and *derive* thermodynamic structure.

4. *Fundamental principle:* This suggests GENERIC is not just a modelling framework but a fundamental principle that information-isolated systems must obey.}

\slides{
**Why Automatic Matters:**

1. No guesswork—structure emerges
2. Global validity—true everywhere
3. Information-first foundation
4. GENERIC as fundamental principle

**Flips the usual derivation:**
$$\text{Information axioms} \Rightarrow \text{Thermodynamics}$$
}

\notes{In Grmela and Öttinger's original work, satisfying the degeneracy conditions requires careful construction (see e.g. Chapter 4 of @Ottinger-beyond05). The fact that they emerge automatically in our framework suggests that marginal entropy conservation has special geometric significance for non-equilibrium dynamics.}

\endif
\endif
