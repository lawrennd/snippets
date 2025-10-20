\ifndef{casimirFunctions}
\define{casimirFunctions}

\editme

\subsection{Casimir Functions and Degeneracy}

\notes{So far we've assumed the antisymmetric matrix $A$ can be "any" antisymmetric matrix. But what if $A$ is degenerate, i.e. not full rank? This leads to *Casimir functions*, which are key to understanding constrained Hamiltonian systems.}

\subsubsection{When $A$ is Degenerate}

\notes{A **Casimir function** is a function $C(\mathbf{x})$ that has zero Poisson bracket with ALL other functions:
$$
\{C, f\} = 0 \quad \text{for all } f
$$

This means
$$
\{C, H\} = 0 \quad \text{for ANY Hamiltonian } H.
$$
So $\dot{C} = \{C, H\} = 0$, Casimir functions are conserved along all Hamiltonian flows, regardless of which Hamiltonian you choose.

**When do Casimirs exist?** When the matrix $A$ is *degenerate* (not full rank). If $A$ has a non-trivial kernel:
$$
\ker(A) = \{\mathbf{v} : A\mathbf{v} = \mathbf{0}\} \neq \{\mathbf{0}\}.
$$
Then any function $C$ whose gradient lies in this kernel is a Casimir,
$$
\nabla C \in \ker(A) \quad \Rightarrow \quad \{C, f\} = (\nabla C)^\top A (\nabla f) = \mathbf{0}^\top (\nabla f) = 0.
$$

**Intuition:** Casimirs are "super-conserved" - they're conserved for ANY choice of dynamics, not just one specific Hamiltonian. They represent fundamental constraints on the geometry of phase space that no Hamiltonian flow can violate.}

\slides{
**Casimir Functions:**

$C$ satisfies: $\{C, f\} = 0$ for ALL $f$

* Conserved for ANY Hamiltonian
* "Super-conserved" quantities
* Exist when $A$ is degenerate
* Restrict accessible phase space
}

\newslide{Definition of Casimir Functions}

\notes{A function $C(\mathbf{x})$ is a **Casimir function** if it Poisson-commutes with every function
$$
\{C, f\} = 0 \quad \text{for all } f.
$$

Equivalently: $A \nabla C = \mathbf{0}$, i.e., $\nabla C \in \ker(A)$.

**Physical meaning:** Casimir functions are automatically conserved by *any* Hamiltonian flow. They don't depend on the choice of energy function $H$—they're conserved by the structure of $A$ itself.

Think of them as "built-in" conservation laws that come from the geometry, not from the dynamics.}

\slides{
**Casimir Function:**
$$
\{C, f\} = 0 \quad \forall f.
$$

Equivalently: $A \nabla C = \mathbf{0}$

* Conserved by *any* Hamiltonian
* From geometry, not dynamics
* "Built-in" conservation laws
}

\subsection{Example: Angular Momentum}

\notes{Consider a rigid body rotating in 3D space. The state is the angular momentum vector $\mathbf{L} = (L_1, L_2, L_3)$.

The Poisson bracket structure for angular momentum is:
$$
\{L_i, L_j\} = \epsilon_{ijk} L_k,
$$
where $\epsilon_{ijk}$ is the Levi-Civita symbol (antisymmetric tensor).

In matrix form, this corresponds to
$$
A = \begin{pmatrix}
0 & L_3 & -L_2 \\
-L_3 & 0 & L_1 \\
L_2 & -L_1 & 0
\end{pmatrix}.
$$

Notice: $A$ depends on the state $\mathbf{L}$.

**The Casimir:** Consider $C = |\mathbf{L}|^2 = L_1^2 + L_2^2 + L_3^2$. Then
$$
A \nabla C = A \begin{pmatrix} 2L_1 \\ 2L_2 \\ 2L_3 \end{pmatrix} = 2 \begin{pmatrix} L_3 L_2 - L_2 L_3 \\ L_1 L_3 - L_3 L_1 \\ L_2 L_1 - L_1 L_2 \end{pmatrix} = \mathbf{0}
$$
So the magnitude of angular momentum is a Casimir! It's conserved regardless of which Hamiltonian drives the rotation.}

\slides{
**Rigid Body Example:**

*State:* $\mathbf{L}$ (angular momentum)

*Poisson bracket:* $\{L_i, L_j\} = \epsilon_{ijk} L_k$

*Casimir:* $C = |\mathbf{L}|^2$

Always conserved, any rotation!
}

\newslide{Why Casimirs Matter}

\notes{Casimir functions are connected to degeneracy and constraints.

1. **Constraint manifolds**: The system is confined to surfaces where Casimirs are constant. For angular momentum, the system stays on a sphere $|\mathbf{L}|^2 = \text{const}$.

2. **Reduced dynamics**: Instead of evolving in the full space, dynamics happen on these constrained surfaces called *symplectic leaves*.

3. **Information conservation**: For The Inaccessible Game, **the sum of marginal entropies $\sum h_i = C$ is a Casimir**! It's conserved by the Hamiltonian structure itself.

4. **Degeneracy is natural**: Many physical systems have degenerate Poisson structures. This isn't a defect, it's a feature that encodes their conservation laws.}

\slides{
**Why Casimirs Matter:**
* Confine to constraint surfaces
* Dynamics on symplectic leaves
* **TIG:** $\sum h_i = C$ is a Casimir!
* Degeneracy encodes conservation
}

\subsection{Symplectic Leaves}

\notes{When $A$ is degenerate, phase space decomposes into *symplectic leaves*, submanifolds on which the Poisson structure is non-degenerate.

**Intuitive picture:** 
- Each leaf is a surface where all Casimirs are constant
- On each leaf, Hamiltonian dynamics work "normally" (non-degenerate)
- Different leaves don't communicate—you can't jump between them

For the angular momentum example:
- Each sphere $|\mathbf{L}|^2 = r^2$ is a symplectic leaf
- Dynamics on each sphere are independent
- The leaves foliate (fill up) the entire space

This geometric picture will be crucial for understanding The Inaccessible Game: information conservation defines the leaves, and dynamics happen within each leaf.}

\slides{
**Symplectic Leaves:**
* Submanifolds where $A$ non-degenerate
* Defined by constant Casimirs
* Dynamics confined to each leaf
* Leaves foliate space

*TIG:* Leaves = surfaces $\sum h_i = C$
}

\newslide{Computing Casimirs}

\notes{How do you find Casimir functions? Solve:
$$
A \nabla C = \mathbf{0}.
$$
This is a system of PDEs. The dimension of the space of Casimirs equals $\dim(\ker(A))$.

**For information systems:** If we have $n$ variables and the antisymmetric structure has a $k$-dimensional kernel, we get $k$ independent Casimirs. These might be:
- Conservation of total marginal entropy
- Conservation of subsystem entropies
- Other information-theoretic invariants

Finding these Casimirs can be the key to understanding what's truly conserved in a system.}

\slides{
**Finding Casimirs:**
$$
A \nabla C = \mathbf{0}
$$

* System of PDEs
* \# Casimirs = $\dim(\ker(A))$
* For information systems: entropy invariants
* Key to understanding conservation
}

\subsection{Interlude: Noether's Theorem}

\notes{Before connecting Casimirs to symmetries, we need one of the most beautiful results in physics: *Noether's theorem* (@Noether-invariante18).

**The idea:** Every continuous symmetry of a physical system gives rise to a conservation law.

**Examples:**
- **Translation symmetry** (physics is the same everywhere in space) $\rightarrow$ conservation of momentum
- **Rotation symmetry** (physics is the same in all directions) $\rightarrow$ conservation of angular momentum  
- **Time translation** (physics is the same at all times) $\rightarrow$ conservation of energy

**How it works:** If you have a transformation that leaves the Lagrangian (or Hamiltonian) unchanged, then there's a quantity that stays constant along trajectories. The transformation "generates" the conserved quantity.

For Hamiltonian systems, if $H$ is symmetric under some transformation, then the generator of that transformation is conserved: $\{G, H\} = 0$ means $\dot{G} = 0$.

This gives us a connection between geometry and physics: the structure of spacetime (its symmetries) determines what quantities are conserved.}

\slides{
**Noether's Theorem (1918):**

*Continuous symmetry $\rightarrow$ conservation law*

Examples:
* Translation $\rightarrow$ momentum
* Rotation $\rightarrow$ angular momentum
* Time translation $\rightarrow$ energy

*Symmetries of $H$ generate conserved quantities*
}

\subsection{Connection to Noether's Theorem}

\notes{There's a deep connection between Casimirs and symmetries through Noether's theorem.

For Hamiltonian systems:
- **Noether symmetries**: Symmetries of $H$ $\rightarrow$ conserved quantities (momentum, angular momentum, etc.)
- **Casimirs**: Conserved quantities from Poisson structure, independent of $H$

Casimirs are even more fundamental: they're conserved regardless of the Hamiltonian. They represent symmetries of the *Poisson structure itself*, not just of a particular energy function.

For The Inaccessible Game, the information conservation $\sum h_i = C$ can be viewed as a Casimir arising from the exchangeability symmetry: all variables are treated equivalently.}

\slides{
**Noether's Theorem Connection:**

*Symmetries of $H$* → conserved quantities

*Casimirs* → conserved by structure

*More fundamental:* Independent of $H$

*TIG:* Exchangeability → $\sum h_i = C$ is Casimir
}

\subsection{Preview: GENERIC Structure}

\notes{In Lecture 8, we'll see that realistic dynamics combine
$$
\dot{\mathbf{x}} = A \nabla H + G \nabla S
$$
when both $A$ (antisymmetric) and $G$ (symmetric Fisher metric) are present, Casimirs of $A$ are still conserved if
$$
G \nabla C = \mathbf{0}.
$$
For The Inaccessible Game, $\sum h_i$ is a Casimir of the antisymmetric part, and the Fisher metric $G$ is chosen to ensure this constraint is preserved. This is the geometric heart of how information conservation works.

Casimir functions are the bridge between conservation laws and geometric structure, exactly what we need for understanding constrained information dynamics.}

\slides{
**Preview: GENERIC**
$$
\dot{\mathbf{x}} = A \nabla H + G \nabla S
$$

*Casimirs conserved if:* $G \nabla C = \mathbf{0}$

*TIG:* Both $A$ and $G$ preserve $\sum h_i$

*Casimirs = bridge between conservation & geometry*
}

\endif

