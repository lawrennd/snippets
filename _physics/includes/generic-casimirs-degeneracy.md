\ifndef{genericCasimirsDegeneracy}
\define{genericCasimirsDegeneracy}

\editme

\subsection{Casimirs in GENERIC Context}

\notes{In Lecture 5, we introduced Casimir functions as "super-conserved" quantities that Poisson brackets with everything to zero. In GENERIC, Casimirs play an even more fundamental role—they're quantities conserved by *both* the reversible and irreversible parts of the dynamics.

**Definition:** A function $C(x)$ is a Casimir of a GENERIC system if
$$
L(x) \nabla C(x) = 0 \quad \text{AND} \quad M(x) \nabla C(x) = 0.
$$
This means
$$
\frac{\text{d}C}{\text{d}t} = \langle \nabla C, L \nabla E + M \nabla S \rangle = 0.
$$
Casimirs are conserved regardless of whether the system is in equilibrium or far from equilibrium, whether dissipation is active or not, whether energy is being redistributed or not. They're the most fundamental constraints on the system.}

\slides{
**Casimirs in GENERIC**

$$L \nabla C = 0 \quad \text{AND} \quad M \nabla C = 0$$

**Meaning:**

* Conserved by reversible part (Poisson)
* Conserved by irreversible part (friction)
* **Most fundamental constraints**

**Always conserved:**

* Equilibrium or non-equilibrium
* With or without dissipation
* Regardless of energy redistribution
}

\subsection{Examples of Casimirs}

\notes{Casimirs appear throughout physics and reflect fundamental symmetries or conservation laws

**Classical Mechanics:**

- **Total momentum** $\mathbf{P} = \sum_i \mathbf{p}_i$ (in absence of external forces)
  - Conserved by Hamiltonian flow (Noether's theorem from translation symmetry)
  - Conserved by friction (friction acts in relative coordinates)
  
- **Total angular momentum** $\mathbf{L} = \sum_i \mathbf{r}_i \times \mathbf{p}_i$ (in absence of external torques)
  - Conserved by Hamiltonian flow (rotational symmetry)
  - Magnitude $|\mathbf{L}|^2$ is Casimir (recall Lecture 5)

**Fluid Dynamics:**

- **Circulation** $\Gamma = \oint \mathbf{v} \cdot \text{d}\mathbf{l}$ in ideal fluids
  - Kelvin's circulation theorem
  - Survives even with viscosity (in certain limits)

**Electromagnetism:**

- **Total charge** $Q = \int \rho(\mathbf{r}) \text{d}^3\mathbf{r}$
  - Conserved by Maxwell's equations (gauge symmetry)
  - Conserved by dissipation (charge doesn't disappear)

**Information Dynamics:**

- **Marginal entropy sum** $\sum_i h_i(\boldsymbol{\theta}) = C$
  - Conserved by axioms (Lecture 2)
  - Defines the constraint manifold
  - This is THE fundamental Casimir for TIG!}

\slides{
**Examples of Casimirs**

| System | Casimir | Symmetry |
|--------|---------|----------|
| Mechanics | Momentum $\mathbf{P}$ | Translation |
| Mechanics | Angular mom $\mathbf{L}$ | Rotation |
| Fluids | Circulation $\Gamma$ | Kelvin's theorem |
| EM | Total charge $Q$ | Gauge |
| **Information** | **$\sum h_i = C$** | **Axioms** |

Information Casimir = constraint from Lecture 2!
}

\subsection{Degeneracy and Symplectic Leaves}

\notes{Casimirs cause *degeneracy* in the Poisson operator $L$: the operator has a non-trivial null space. This has a beautiful geometric interpretation.

Consider a Casimir $C(x)$. Since $L \nabla C = 0$, the gradient $\nabla C$ is in the null space of $L$. This means the Poisson brackets cannot "see" variations in the $C$ direction—the dynamics are restricted to surfaces of constant $C$.

**Symplectic Leaves:** The level sets $\{x : C_i(x) = c_i\}$ for all Casimirs $C_i$ form *symplectic leaves*, submanifolds on which the dynamics live. Each leaf has its own symplectic structure (non-degenerate Poisson bracket).

For a system with $n$ dimensions and $k$ independent Casimirs

- Null space of $L$ is $k$-dimensional
- Symplectic leaves are $(n-k)$-dimensional
- On each leaf, $L$ restricted is non-degenerate

**Physical interpretation:** Casimirs "fold" the phase space into layers. Dynamics cannot jump between layers, they're confined to move within a single symplectic leaf. Different leaves can have completely different dynamical behavior.}

\slides{
**Degeneracy $\rightarrow$ Symplectic Leaves**

Casimir $C$ $\rightarrow$ $L \nabla C = 0$ $\rightarrow$ null space

**Geometric picture:**

* Level sets: $\{x : C_i = c_i\}$ for all Casimirs
* Form **symplectic leaves** (submanifolds)
* Dynamics confined to single leaf
* Can't jump between leaves

**Dimensions:**

* $n$ dimensions total
* $k$ independent Casimirs
* Leaves are $(n-k)$-dimensional

Phase space "folded" into layers!
}

\subsection{Information Casimir: Marginal Entropy Conservation}

\notes{For our information dynamics, the primary Casimir is:
$$
C(\boldsymbol{\theta}) = \sum_{i=1}^n h_i(\boldsymbol{\theta})
$$
where $h_i(\boldsymbol{\theta})$ is the marginal entropy of the $i$-th variable.

Let's verify this is truly a Casimir.

**Conserved by friction ($M = G$)**

The constraint gradient is $a = \nabla C = \nabla(\sum_i h_i)$. By construction (tangency condition from Lecture 4), the Lagrange multiplier $\nu$ is chosen so that:
$$
a^\top \dot{\boldsymbol{\theta}} = 0
$$
This means $a^\top M \nabla S = 0$ when restricted to the constraint manifold. The friction operator conserves the marginal entropy sum.

**Conserved by Poisson ($L$)**

The antisymmetric part $A$ from Lecture 7 satisfies $Aa = 0$ or $a^\top A = 0$ (the constraint gradient is in the null space). This ensures:
$$
a^\top L \nabla E = 0
$$

So $\sum_i h_i$ is indeed a Casimir—conserved by both parts of the dynamics!

**Geometric meaning:** The constraint manifold $\{\boldsymbol{\theta} : \sum_i h_i(\boldsymbol{\theta}) = C\}$ is a symplectic leaf. All information dynamics occur on this leaf. Different values of $C$ give different leaves with potentially different dynamics.}

\slides{
**Information Casimir: $\sum h_i = C$**

**Verify Casimir:**

1. **Friction:** Tangency condition (L4) $\rightarrow$ $a^\top M \nabla S = 0$ ✓
2. **Poisson:** $a$ in null space (L7) $\rightarrow$ $a^\top L \nabla E = 0$ ✓

**Geometric meaning:**

* Constraint manifold $\{\sum h_i = C\}$ = symplectic leaf
* All dynamics on this leaf
* Different $C$ $\rightarrow$ different leaves $\rightarrow$ different behavior

**Origin:** Axioms (Lecture 2) $\rightarrow$ Casimir structure
}

\subsection{Multiple Casimirs}

\notes{In general, GENERIC systems can have multiple independent Casimirs. For information dynamics, we have established:

**Proven Casimir:** $\sum_i h_i = C$ (from axioms, Lecture 2)

This is the constraint that our dynamics preserve. Whether there are additional Casimirs in information dynamics depends on the specific system structure and would need to be proven case-by-case.

**General principle:** Each independent Casimir further constrains the dynamics, reducing the dimensionality of the symplectic leaf on which the dynamics evolve. The dynamics are confined to the intersection of level sets: $\{x : C_i(x) = c_i \text{ for all Casimirs } C_i\}$.}

\slides{
**Multiple Casimirs**

**Proven for TIG:** $\sum h_i = C$ (from axioms)

**General principle**

* Each Casimir reduces dimensionality
* Dynamics confined to level sets
* Multiple Casimirs $\rightarrow$ smaller leaf

**For TIG:** Additional Casimirs need case-by-case proof
}

\subsection{Why Degeneracy is Essential}

\notes{You might wonder: "Why does GENERIC require degeneracy? Why can't we have non-degenerate $L$ and $M$?"

The answer is thermodynamic consistency. If $L$ were non-degenerate (invertible), then:

- Every function could be changed by Hamiltonian flow
- No true conserved quantities except energy
- But we know real systems have conserved quantities (momentum, charge, etc.)

Similarly, if there were no Casimirs:

- The friction could change everything
- No fundamental constraints
- But we know information systems must conserve $\sum h_i$ (from axioms)

Degeneracy is how the system "remembers" its constraints and symmetries. The Casimirs are the "memory" of the axioms that defined the system.

For information dynamics:
- Axiom 4 (marginal entropy conservation) $\rightarrow$ Casimir $\sum h_i = C$
- Casimir $\rightarrow$ Degeneracy in $L$ and $M$
- Degeneracy $\rightarrow$ Symplectic leaf structure
- Leaf structure $\rightarrow$ Constrained dynamics

The whole edifice depends on degeneracy!}

\slides{
**Why Degeneracy Essential?**

**Without degeneracy:**
* No true conserved quantities (except E)
* No fundamental constraints
* Thermodynamically inconsistent!

**Degeneracy ensures:**
* Symmetries preserved
* Constraints respected
* Axioms "remembered"

**For information:**
* Axiom 4 $\rightarrow$ Casimir $\sum h_i$
* Casimir $\rightarrow$ Degeneracy
* Degeneracy $\rightarrow$ Leaf structure
* Leaves $\rightarrow$ Constrained dynamics

Degeneracy = feature, not bug!
}

\subsection{Practical Implications}

\notes{Understanding Casimirs and degeneracy has practical implications for analyzing and simulating information dynamics:

**1. Dimension reduction:**
Each Casimir reduces the effective dimensionality by one. For large systems, this can be substantial. A system with 100 parameters and 10 Casimirs effectively lives in a 90-dimensional space.

**2. Numerical stability:**
Casimirs provide natural "sanity checks" for numerical simulations. If $\sum h_i$ drifts away from its initial value, you know your integrator is violating the constraints.

**3. Perturbation theory:**
Small perturbations transverse to symplectic leaves decay quickly (dissipation). Perturbations within leaves can persist (conservative dynamics). This creates a separation of timescales.

**4. Equilibrium structure:**
Equilibria must satisfy both $L \nabla E = 0$ and $M \nabla S = 0$ on the symplectic leaf. The Casimirs determine which leaf, and within that leaf the equilibrium is unique (for nice systems).

**5. Regime transitions:**
What happens if a Casimir value changes (e.g., injecting or removing particles, changing total entropy)? The system jumps to a different symplectic leaf with potentially different dynamics. This can cause phase transitions or regime changes.}

\slides{
**Practical Implications**

1. **Dimension reduction**
   * $k$ Casimirs $\rightarrow$ $(n-k)$ effective dimensions

2. **Numerical stability**
   * Casimirs = sanity checks for simulations

3. **Perturbation theory**
   * Transverse: decay (dissipation)
   * Within: persist (conservation)
   * $\rightarrow$ Timescale separation

4. **Equilibrium structure**
   * Leaf + energy/entropy $\rightarrow$ unique equilibrium

5. **Regime transitions**
   * Change Casimir $\rightarrow$ jump leaves $\rightarrow$ new dynamics
}

\notes{**Summary:** Casimirs are the most fundamental conserved quantities in GENERIC, conserved by both reversible and irreversible dynamics. They create degeneracy in the operators, stratify phase space into symplectic leaves, and encode the system's fundamental constraints. For information dynamics, marginal entropy conservation $\sum h_i = C$ is the primary Casimir, arising directly from the axioms and defining the constraint manifold on which all dynamics occur.}
\endif
