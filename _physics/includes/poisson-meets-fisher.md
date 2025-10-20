\ifndef{poissonMeetsFisher}
\define{poissonMeetsFisher}

\editme

\subsection{When Poisson Meets Fisher}

\notes{We've introduced two of the key structures we need.
- **Fisher information** $G(\boldsymbol{\theta})$ (symmetric): drives entropy maximization
- **Poisson brackets** with $A$ (antisymmetric): drives energy conservation

What happens when both are present? This leads to GENERIC (General Equation for Non-Equilibrium Reversible-Irreversible Coupling), a framework from non-equilibrium thermodynamics introduced by Grmela and Öttinger (@Grmela-dynamics97; @Ottinger-beyond05) for systems with both reversible (energy-conserving) and irreversible (entropy-producing) dynamics.}

\subsubsection{Two Types of Change}

\notes{Real systems exhibit two types of change:

**1. Irreversible (Dissipative)**
- Entropy increases
- Information spreads
- Correlations decay
- "Arrow of time"
- Example: Heat diffusion, mixing

**2. Reversible (Conservative)**
- Energy conserved
- Structure preserved
- Oscillations, rotations
- Time-symmetric
- Example: Pendulum, planetary orbits

Most real systems have *both*. A damped pendulum dissipates energy (irreversible) while exhibiting oscillatory structure (reversible remnant). A spinning top precesses (reversible) while friction slows it down (irreversible).}

\slides{
**Two Types of Change:**

*Irreversible:*
* Entropy increases
* Dissipative
* Arrow of time
* Fisher metric $G$

*Reversible:*
* Energy conserved
* Conservative
* Time-symmetric  
* Poisson structure $A$
}

\subsection{GENERIC: The Full Picture}

\notes{The **GENERIC** structure (General Equation for Non-Equilibrium Reversible-Irreversible Coupling) combines both:
$$
\dot{\mathbf{x}} = A \nabla E + G \nabla S
$$

where:
- $E(\mathbf{x})$ = energy function
- $S(\mathbf{x})$ = entropy function
- $A$ = antisymmetric matrix (Poisson structure)
- $G$ = symmetric positive-definite matrix (metric)

This single equation describes evolution that is partially reversible (the $A$ term) and partially irreversible (the $G$ term).}

\slides{
**GENERIC Structure:**
$$
\dot{\mathbf{x}} = A \nabla E + G \nabla S
$$

$A \nabla E$ $\rightarrow$ reversible (energy conserving)

$G \nabla S$ $\rightarrow$ irreversible (entropy increasing)

*One equation, both types*
}

\newslide{Degeneracy Requirements}

\notes{For GENERIC to be consistent, $A$ and $G$ must satisfy *degeneracy conditions*:

**Condition 1:** Energy conserved by dissipative part:
$$
G \nabla E = \mathbf{0}
$$
The entropy-driven dynamics doesn't change energy.

**Condition 2:** Entropy conserved by conservative part:
$$
A \nabla S = \mathbf{0}
$$
The energy-driven dynamics doesn't change entropy.

These conditions ensure the two parts don't "fight" each other. The reversible part preserves what the irreversible part changes, and vice versa. They operate in complementary directions.}

\slides{
**Degeneracy Conditions:**
$$
G \nabla E = \mathbf{0}
$$
$$
A \nabla S = \mathbf{0}
$$

* Reversible preserves entropy
* Irreversible preserves energy
* Complementary directions
* No "fighting"
}

\subsection{Information Dynamics}

\notes{For The Inaccessible Game, we'll see (in Lecture 8):

**Energy:** Related to multi-information $I = \sum h_i - H$

**Entropy:** The joint entropy $H$

**Fisher metric $G$:** We've already studied this—it appears in $\nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}$

**Poisson structure $A$:** Encodes the constraints and conservation laws

The full dynamics
$$
\dot{\boldsymbol{\theta}} = -A(\boldsymbol{\theta}) \nabla I - G(\boldsymbol{\theta})\boldsymbol{\theta}.
$$
The Fisher part ($-G\boldsymbol{\theta}$) increases entropy. The Poisson part ($-A \nabla I$) redistributes information while preserving constraints.}

\slides{
**Information Dynamics:**

*Energy:* Multi-information $I$

*Entropy:* Joint $H$

*Fisher $G$:* Entropy increase

*Poisson $A$:* Redistribution + constraints

$$
\dot{\boldsymbol{\theta}} = -A \nabla I - G\boldsymbol{\theta}
$$
}

\newslide{Why Both Are Needed}

\notes{Why can't we just have entropy maximization alone?

**Without Poisson structure:**
- System would maximize entropy without constraint
- All variables would decorrelate completely
- No interesting structure would emerge
- Universe would be uniform soup

**With Poisson structure:**
- Constraints enforced (e.g., $\sum h_i = C$)
- Structure can emerge within constraints
- Regimes form and persist
- Rich dynamics possible

The Poisson structure creates the "inaccessible game": it defines what's forbidden, what's conserved, and therefore what complexity can emerge within those constraints.

Fisher drives change. Poisson constrains it. Together: constrained evolution toward maximum entropy.}

\slides{
**Why Both:**

*Only Fisher:*
* Unconstrained growth
* Everything decorrelates
* Uniform soup
* Boring

*Fisher + Poisson:*
* Constrained evolution
* Structure emerges
* Regimes persist
* Interesting!

*Poisson makes it "inaccessible"*
}

\subsection{Preview of Lecture 8}

\notes{In Lecture 8, we'll develop the full GENERIC framework for information dynamics. We'll see:

1. **How to construct $A$** from information-theoretic principles
2. **The role of Casimirs** in enforcing conservation ($\sum h_i = C$)
3. **Local vs. global Hamiltonians** and why information systems are locally Hamiltonian
4. **Perturbation analysis** showing how reversible and irreversible parts separate
5. **Regime emergence** from the interplay between $A$ and $G$

For now, the key message: Hamiltonian structure (Poisson brackets) is not just for mechanics. It's a fundamental geometric tool for understanding constrained dynamics in any system—including information systems.}

\slides{
**Lecture 8 Preview:**
* Construct $A$ for information systems
* Casimirs enforce conservation
* Local Hamiltonian structure
* Reversible/irreversible separation
* Regime emergence

*Poisson brackets: fundamental geometric tool*
}

\subsection{Summary: Symmetric and Antisymmetric}

\notes{We can now appreciate the full picture:

**Symmetric (Fisher):**
- Positive-definite metric $G$
- Gradient flow: $\dot{\mathbf{x}} = G \nabla S$
- Increases entropy
- Dissipative
- Irreversible

**Antisymmetric (Poisson):**
- Antisymmetric matrix $A$
- Hamiltonian flow: $\dot{\mathbf{x}} = A \nabla E$
- Conserves energy (and Casimirs)
- Conservative
- Reversible

**Together (GENERIC):**
$$
\dot{\mathbf{x}} = A \nabla E + G \nabla S
$$
- Both types of dynamics
- Degeneracy conditions couple them
- Rich behavior from simple structure

The mathematics is elegant: two matrices with opposite symmetry properties generate complementary types of dynamics that together describe complex systems.}

\slides{
**Summary:**

*Symmetric $G$:*
* Dissipative
* Entropy ↑
* Irreversible

*Antisymmetric $A$:*
* Conservative
* Energy conserved
* Reversible

*Together:* Rich constrained dynamics

*Mathematics:* Opposite symmetries $\rightarrow$ complementary dynamics
}

\endif

