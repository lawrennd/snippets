\ifndef{genericFrameworkIntro}
\define{genericFrameworkIntro}

\editme

\subsection{The GENERIC Framework}

\notes{We've seen something emerge from lectures 5-7:

- **Lecture 5:** Hamiltonian/Poisson structure describes energy-conserving dynamics (antisymmetric operators)
- **Lecture 6:** Linearisation around equilibrium reveals structure of dynamics
- **Lecture 7:** Any dynamics matrix decomposes uniquely as $M = S + A$ where $S$ is symmetric (dissipative) and $A$ is antisymmetric (conservative)

This emergence comes from the geometry of constrained information dynamics. The structure is *not unique to information theory*. It appears throughout physics whenever systems combine reversible and irreversible processes.}

\slides{
**What We've Seen Emerge**

Lecture 5: Energy conservation $\rightarrow$ antisymmetric $A$

Lecture 6-7: Linearisation $\rightarrow$ $M = S + A$ split

**Question:** Is this structure universal?

**Answer:** YES! $\rightarrow$ GENERIC framework
}

\subsection{Historical Context: Non-Equilibrium Thermodynamics}

\notes{In the 1980s-90s, researchers in non-equilibrium thermodynamics faced a challenge: How do you describe systems that are *simultaneously*:
- **Reversible** (like mechanical systems, governed by Hamilton's equations)
- **Irreversible** (like thermodynamic systems, governed by entropy increase)

Examples of such systems:
- **Fluid dynamics:** Conservation of momentum (reversible) + viscosity (irreversible)
- **Chemical reactions:** Reaction kinetics (reversible) + diffusion (irreversible)
- **Complex materials:** Elastic deformation (reversible) + plastic flow (irreversible)

Two researchers, Miroslav Grmela and Hans Christian Öttinger, independently developed a unified framework in the 1990s that they called **GENERIC**: *General Equation for Non-Equilibrium Reversible-Irreversible Coupling* [@Grmela-dynamics97;@Ottinger-generic97;@Ottinger-beyond05].}

\slides{
**Non-Equilibrium Challenge (1980s-90s)**

Real systems are *both*:
* Reversible (mechanics, conservation laws)
* Irreversible (thermodynamics, dissipation)

**Examples:**
* Fluids: momentum conservation + viscosity
* Reactions: kinetics + diffusion
* Materials: elasticity + plasticity

**Solution:** GENERIC framework (@Grmela-dynamics97, @Ottinger-generic97)
}

\subsection{What Problem Does GENERIC Solve?}

\notes{Classical mechanics and classical thermodynamics seemed to describe fundamentally different worlds:

**Classical Mechanics (Hamiltonian)**

- Time reversible: $t \to -t$ gives valid dynamics
- Energy conserved: $\frac{\text{d}E}{\text{d}t} = 0$
- Phase space volume conserved (Liouville's theorem)
- Described by antisymmetric operators (Poisson brackets)

**Classical Thermodynamics**

- Time irreversible: entropy always increases
- Energy dissipated: $\frac{\text{d}S}{\text{d}t} \geq 0$
- Systems evolve toward equilibrium
- Described by symmetric operators (friction, diffusion)

**The Problem:** Real systems do BOTH simultaneously! A pendulum with friction conserves angular momentum (reversible) while losing energy to heat (irreversible). How do you write down equations that respect both structures at once?}

\slides{
**Two Worlds?**

| Classical Mechanics | Classical Thermodynamics |
|----------|---------|
| Time reversible | Time irreversible |
| Energy conserved | Entropy increases |
| Antisymmetric ops | Symmetric ops |
| Poisson structure | Dissipation |

**Problem:** Real systems do *both*.

*Pendulum with friction*: Angular momentum (reversible) + heat loss (irreversible)
}

\subsection{The GENERIC Answer: Coexistence Requires Structure}

\notes{GENERIC provides the answer: reversible and irreversible processes can coexist in the same system, but only if they satisfy certain *compatibility conditions*. These conditions ensure

1. Energy and entropy are consistently defined
2. The second law of thermodynamics holds ($\dot{S} \geq 0$)
3. Conserved quantities (like energy, momentum) remain conserved
4. Casimir functions (constraints) are respected

Importantly you can't just add reversible and irreversible parts arbitrarily, they must be *coupled through degeneracy conditions* that enforce thermodynamic consistency.

 In typical GENERIC applications, ensuring the degeneracy conditions are satisfied is challenging, you must carefully engineer both operators to be compatible. But in our case (Lectures 1-7), the degeneracy conditions emerge automatically from the constraint geometry. We didn't impose them, they pop out as a consequence of starting from information-theoretic axioms. When we check in Lecture 8, they're already satisfied. This strongly suggests our axioms capture something fundamental about thermodynamic consistency.}

\slides{
**GENERIC Answer**

Reversible + Irreversible can coexist

**Requirements:**
1. Consistent energy & entropy
2. Second law: $\dot{S} \geq 0$
3. Conserved quantities respected
4. Constraints (Casimirs) obeyed

**Key:** Can't add arbitrarily $\rightarrow$ need *degeneracy conditions*

**Remarkable:** In typical GENERIC, degeneracy conditions are HARD to satisfy (must engineer carefully)

**Our approach (L1-7):** Degeneracy conditions emerge automatically! ✓

(Axioms $\rightarrow$ geometry $\rightarrow$ thermodynamic consistency)
}

\subsection{Why "GENERIC" Matters for Information Dynamics}

\notes{You might wonder: "Why do we care about a framework from non-equilibrium thermodynamics in a course on information dynamics?"

The structure that emerged from pure information theory (lectures 1-7) is identical to the structure that physicists discovered was necessary for consistent non-equilibrium thermodynamics.

This suggests something deep:
- Information dynamics *is* thermodynamics (we've known this since Shannon and Jaynes)
- But more: information dynamics *is also* a dynamical system with conserved quantities
- The GENERIC structure is the inevitable consequence of combining these two aspects

When we derived $\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta} - \nu a$ from information-theoretic principles, we were actually deriving a GENERIC system! The Fisher information $G$ plays the role of the "friction" operator, and the constraint dynamics provide the "Poisson" structure.}

\slides{
**Why GENERIC for Information Dynamics?**

Structure we *derived* (L1-7) = Structure physicists *discovered* (GENERIC)

**Deep connection:**
* Information dynamics = thermodynamics (Shannon/Jaynes)
* Information dynamics = dynamical system (constraints)
* GENERIC = inevitable consequence of combining both

**Our system:** $\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta} - \nu a$
* $G$: Fisher information (friction/dissipation)
* $\nu a$: Constraint dynamics (reversible structure)

We've been building GENERIC from scratch!
}

\subsection{Preview: Structure of the GENERIC Equation}

\notes{In the next sections, we'll see the full GENERIC equation:
$$
\dot{x} = L(x) \nabla E(x) + M(x) \nabla S(x)
$$
where:
- $L(x)$: Poisson operator (antisymmetric, describes reversible dynamics)
- $M(x)$: Friction operator (symmetric positive semi-definite, describes irreversible dynamics)
- $E(x)$: Energy functional (conserved by $L$ dynamics)
- $S(x)$: Entropy functional (increased by $M$ dynamics)

And we'll see how our information dynamics fit perfectly into this form, with:
- Fisher information matrix $G$ playing the role of $M$
- Constraint structure providing the Poisson operator $L$
- Marginal entropy conservation giving us Casimir functions

The structure we built from axioms (lectures 1-4) is GENERIC. The decomposition we derived from linearization (lectures 6-7) reveals its form.}

\slides{
**Coming Up: The GENERIC Equation**

$$\dot{x} = L(x) \nabla E(x) + M(x) \nabla S(x)$$

* $L$: Poisson (antisymmetric, reversible)
* $M$: Friction (symmetric, irreversible)
* $E$: Energy (conserved by $L$)
* $S$: Entropy (increased by $M$)

**Our information dynamics:**
* $G \leftrightarrow M$ (Fisher = friction)
* Constraints $\leftrightarrow L$ (structure)
* $\sum h_i = C$ (Casimirs)

Structure we built = GENERIC!
}

\notes{**Historical note:** The original GENERIC papers [@Grmela-dynamics97;@Ottinger-generic97] emerged from studies of complex fluids and polymers. It has since been applied to

- Viscoelastic materials
- Multiphase flows
- Chemical reaction networks  
- Biological systems
- Plasma physics

The framework is now recognized as a fundamental structure in non-equilibrium statistical mechanics. Our contribution is showing it emerges naturally from information-theoretic first principles.}

\endif
