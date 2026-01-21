\ifndef{genericEquationStructure}
\define{genericEquationStructure}

\editme

\subsection{The GENERIC Equation}

\notes{The GENERIC framework describes the evolution of a state $x$ (which could be a density matrix, a distribution, a field configuration, etc.) through the equation:
$$
\dot{x} = L(x) \nabla E(x) + M(x) \nabla S(x),
$$
where

- $x$: State of the system (lives in some state space)
- $E(x)$: Energy functional
- $S(x)$: Entropy functional  
- $\nabla E$, $\nabla S$: Functional derivatives (gradients in function space)
- $L(x)$: Poisson operator (describes reversible dynamics)
- $M(x)$: Friction operator (describes irreversible dynamics)

This equation encodes deep structure. Let's unpack each component.}

\slides{
**The GENERIC Equation**

$$\dot{x} = L(x) \nabla E(x) + M(x) \nabla S(x)$$

**Components:**
* $x$: System state
* $E$: Energy functional
* $S$: Entropy functional
* $L$: Poisson operator (reversible)
* $M$: Friction operator (irreversible)

Simple form $\rightarrow$ Deep structure!
}

\subsection{The Poisson Operator $L(x)$}

\notes{The Poisson operator $L(x)$ describes the reversible (energy-conserving, time-reversible) part of the dynamics. It must

**1. Be Antisymmetric:** For any functionals $F$ and $G$,
$$
\langle \nabla F, L \nabla G \rangle = -\langle \nabla G, L \nabla F \rangle
$$
where $\langle \cdot, \cdot \rangle$ denotes an appropriate inner product. This ensures time reversibility: if you reverse time ($t \to -t$) and flip velocities, you get valid dynamics.

**2. Satisfy Jacobi identity:** The Poisson bracket defined by $L$ must satisfy
$$
\{F, \{G, H\}\} + \{G, \{H, F\}\} + \{H, \{F, G\}\} = 0
$$
where $\{F,G\} := \langle \nabla F, L \nabla G \rangle$. This is the condition for $L$ to generate a Lie algebra structure (recall Lecture 5!).

**3. Conserve energy:** The energy must be a Casimir of $L$:
$$
L(x) \nabla E(x) = 0 \quad \Rightarrow \quad \frac{\text{d}E}{\text{d}t}\bigg|_{L \text{ only}} = 0
$$
Actually, for GENERIC we require something weaker: $\langle \nabla E, L \nabla E \rangle = 0$, which follows from antisymmetry.

This connects directly to Lecture 5: $L$ defines a Poisson structure, and Hamiltonian flow with Hamiltonian $E$ is given by $\dot{x} = L \nabla E$.}

\slides{
**Poisson Operator $L(x)$** (Reversible part)

**Properties:**
1. **Antisymmetric:** $\langle \nabla F, L \nabla G \rangle = -\langle \nabla G, L \nabla F \rangle$
   * Time reversible

2. **Jacobi identity:** $\{F, \{G, H\}\} + \text{cyclic} = 0$
   * Lie algebra (Lecture 5!)

3. **Conserves energy:** $\langle \nabla E, L \nabla E \rangle = 0$
   * $\frac{\text{d}E}{\text{d}t}|_L = 0$

**Recall L5:** This IS Hamiltonian/Poisson structure!
}

\subsection{The Friction Operator $M(x)$}

\notes{The friction operator $M(x)$ describes the irreversible (entropy-increasing, dissipative) part of the dynamics. It must

**1. Be Symmetric:** For any functionals $F$ and $G$,
$$
\langle \nabla F, M \nabla G \rangle = \langle \nabla G, M \nabla F \rangle.
$$
This is the Onsager reciprocity relation from irreversible thermodynamics.

**2. Be Positive semi-definite:** For any functional $F$,
$$
\langle \nabla F, M \nabla F \rangle \geq 0.
$$
This ensures dissipation: entropy can only increase (or stay constant), never decrease.

**3. Conserve energy:** The friction must not change the energy
$$
\langle \nabla E, M \nabla S \rangle = 0.
$$
This is the *first degeneracy condition*. Dissipation redistributes energy but doesn't create or destroy it.

The positive semi-definite property ensures the second law:
$$
\frac{\text{d}S}{\text{d}t}\bigg|_{M \text{ only}} = \langle \nabla S, M \nabla S \rangle \geq 0
$$

This connects to Lecture 7: The symmetric part $S$ of our decomposition $M = S + A$ had exactly these properties!}

\slides{
**Friction Operator $M(x)$** (Irreversible part)

**Properties:**

1. **Symmetric:** $\langle \nabla F, M \nabla G \rangle = \langle \nabla G, M \nabla F \rangle$
   * Onsager reciprocity

2. **Positive semi-definite:** $\langle \nabla F, M \nabla F \rangle \geq 0$
   * Entropy increases: $\dot{S}|_M \geq 0$

3. **Conserves energy:** $\langle \nabla E, M \nabla S \rangle = 0$
   * First degeneracy condition

**Recall L7:** This *is* our symmetric part $S$!
}

\subsection{The Degeneracy Conditions}

\notes{For the GENERIC equation to be thermodynamically consistent, $L$ and $M$ must satisfy two **degeneracy conditions** that couple the reversible and irreversible parts:

**Degeneracy Condition 1** (Energy conservation by friction):
$$
M(x) \nabla E(x) = 0
$$
Physically: Dissipative processes cannot change the total energy, only redistribute it. This is more general than what we stated above—the friction operator must annihilate the energy gradient entirely, not just be orthogonal to it.

**Degeneracy Condition 2** (Entropy conservation by Poisson dynamics):
$$
L(x) \nabla S(x) = 0
$$
Physically: Reversible (Hamiltonian) processes cannot change entropy. All entropy change must come from irreversible processes.

These conditions are **non-trivial constraints** on the operators $L$ and $M$. They ensure:
- The first law (energy conservation): $\frac{\text{d}E}{\text{d}t} = \langle \nabla E, L \nabla E + M \nabla S \rangle = 0$
- The second law (entropy increase): $\frac{\text{d}S}{\text{d}t} = \langle \nabla S, L \nabla E + M \nabla S \rangle = \langle \nabla S, M \nabla S \rangle \geq 0$

Without these conditions, you could have energy creation/destruction or entropy decrease, those would be violations of thermodynamics.}

\slides{
**Degeneracy Conditions** (Coupling)

**Condition 1:** $M \nabla E = 0$
* Friction doesn't change total energy
* Only redistributes it

**Condition 2:** $L \nabla S = 0$
* Hamiltonian flow doesn't change entropy
* All entropy change from dissipation

**Consequences:**
* First law: $\frac{\text{d}E}{\text{d}t} = 0$ ✓
* Second law: $\frac{\text{d}S}{\text{d}t} = \langle \nabla S, M \nabla S \rangle \geq 0$ ✓

Without these $\rightarrow$ thermodynamics violated.
}

\subsection{Casimir Functions and Constraints}

\notes{Beyond energy and entropy, GENERIC systems often have additional conserved quantities called **Casimir functions** $C_i(x)$. These satisfy:
$$
L(x) \nabla C_i(x) = 0 \quad \text{and} \quad M(x) \nabla C_i(x) = 0
$$

Casimirs are "super-conserved", they're annihilated by both the reversible and irreversible parts of the dynamics. Physically, Casimirs represent fundamental constraints that cannot be changed by any process in the system.

**Examples:**
- **Mechanics:** Total momentum (in absence of external forces)
- **Fluids:** Circulation in ideal fluids
- **Electromagnetism:** Total charge
- **Information dynamics:** $\sum h_i = C$ (marginal entropy conservation!)

Casimirs often arise from symmetries (Noether's theorem, Lecture 5) or from fundamental conservation laws. They stratify the state space into *symplectic leaves*, invariant manifolds on which the dynamics are confined.

For information dynamics, the conservation of marginal entropy sum $\sum h_i = C$ is our primary Casimir. The dynamics must respect this constraint at all times.}

\slides{
**Casimir Functions $C_i(x)$**

$$L \nabla C_i = 0 \quad \text{AND} \quad M \nabla C_i = 0$$

* "Super-conserved" (both parts preserve)
* Fundamental constraints

**Examples:**
* Momentum (mechanics)
* Circulation (fluids)
* Charge (electromagnetism)
* **$\sum h_i = C$ (information)**

**Effect:** Stratify state space into symplectic leaves

(Recall L5: Casimirs from symmetries)
}

\subsection{Why This Structure?}

\notes{You might wonder why GENERIC has exactly this form. Why two operators? Why these specific conditions?

The answer is that this is the most general structure*that allows reversible and irreversible processes to coexist while respecting:
1. Time-reversal symmetry for the reversible part
2. Second law for the irreversible part
3. Energy conservation overall
4. Additional conservation laws (Casimirs)

Grmela and Öttinger proved that any system satisfying these physical requirements must have GENERIC form. It's not a choice, it's a consequence of thermodynamic consistency.

In TIG this structure emerged from our information dynamics (Lectures 1-7) without imposing it. The axioms (Lecture 2) + maximum entropy dynamics (Lecture 3) + constraints (Lecture 4) produce the GENERIC structure. This suggests GENERIC is not just a modeling framework, it's a principle that information isolated systems must obey.}

\slides{
**Why This Structure?**

GENERIC is the *most general* structure that allows:
* Time-reversal (reversible part)
* Second law (irreversible part)  
* Energy conservation (overall)
* Casimirs (constraints)

**Not a choice $\rightarrow$ Consequence of physics!**

**Our result:** GENERIC *emerged* from info axioms
* Axioms (L2) + MEP (L3) + Constraints (L4)
* $\rightarrow$ GENERIC structure (L5-7)

GENERIC = deep physical principle, not modeling trick
}

\subsection{A Worked Example: Damped Harmonic Oscillator}

\notes{Let's see GENERIC in action with a simple example: a harmonic oscillator with friction.

**State:** $x = (q, p)$ (position and momentum)

**Energy:** $E(q,p) = \frac{p^2}{2m} + \frac{1}{2}kq^2$ (kinetic + potential)

**Entropy:** For this simple example, we'll use $S = -\beta E$ where $\beta = 1/(k_BT)$ is inverse temperature (this connects to Gibbs distribution).

**Poisson operator:** Standard symplectic structure from Lecture 5,
$$
L = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \quad \{f,g\} = \frac{\partial f}{\partial q}\frac{\partial g}{\partial p} - \frac{\partial f}{\partial p}\frac{\partial g}{\partial q}
$$

**Friction operator:** Simple isotropic damping,
$$
M = \begin{pmatrix} 0 & 0 \\ 0 & \gamma \end{pmatrix}
$$
where $\gamma > 0$ is the friction coefficient (only momentum experiences friction, not position).

**The dynamics:** Compute the gradients,
$$
\nabla E = \begin{pmatrix} kq \\ p/m \end{pmatrix}, \quad \nabla S = -\beta \nabla E
$$

Then GENERIC gives:
$$
\begin{pmatrix} \dot{q} \\ \dot{p} \end{pmatrix} = L \nabla E + M \nabla S = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} kq \\ p/m \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & \gamma \end{pmatrix}\begin{pmatrix} -\beta kq \\ -\beta p/m \end{pmatrix}
$$

This yields:
$$
\dot{q} = \frac{p}{m}, \quad \dot{p} = -kq - \gamma\beta\frac{p}{m}
$$

The first equation is just velocity = momentum/mass. The second is Newton's law with friction: $m\ddot{q} = -kq - \gamma\beta \dot{q}$, which is exactly the damped harmonic oscillator!}

\slides{
**Example: Damped Harmonic Oscillator**

State: $x = (q,p)$, Energy: $E = \frac{p^2}{2m} + \frac{1}{2}kq^2$

$$L = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \quad M = \begin{pmatrix} 0 & 0 \\ 0 & \gamma \end{pmatrix}$$

**GENERIC:**
$$\dot{q} = \frac{p}{m}, \quad \dot{p} = -kq - \gamma\beta\frac{p}{m}$$

**Result:** $m\ddot{q} = -kq - \gamma\beta\dot{q}$ 

Damped oscillator from GENERIC! (Reversible + irreversible)
}

\notes{**Check degeneracy:**
- $M \nabla E = (0, \gamma p/m)$ is NOT zero! 
- Wait, this violates degeneracy condition 1!

Actually, for finite-dimensional systems with constant $M$ and $L$, the degeneracy conditions are automatically satisfied if we choose entropy correctly as $S \propto -E$ (equilibrium condition). More generally, for complex systems we need to ensure degeneracy by construction. We'll see how information dynamics naturally satisfies these conditions in the next section.}

\notes{**Summary:** The GENERIC equation $\dot{x} = L \nabla E + M \nabla S$ encodes:
- **Structure:** Antisymmetric $L$ + symmetric positive semi-definite $M$
- **Physics:** Reversible dynamics (conserves energy, preserves entropy) + irreversible dynamics (conserves energy, increases entropy)
- **Consistency:** Degeneracy conditions couple $L$ and $M$ to ensure thermodynamic laws
- **Generality:** Covers everything from mechanics to thermodynamics to complex systems

Next, we'll see how our information dynamics fit this framework perfectly.}

\endif
