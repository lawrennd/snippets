\ifndef{whyEnergyConserves}
\define{whyEnergyConserves}

\editme

\subsection{Why Energy Conservation?}

\notes{So far we've studied entropy-driven dynamics: systems that maximise entropy subject to conservation of marginal entropies. But there's another type of dynamics in physics: systems that conserve energy.

Consider a frictionless pendulum. It swings back and forth endlessly, trading potential energy (height) for kinetic energy (speed). At the highest point: maximum potential, zero kinetic. At the lowest point: zero potential, maximum kinetic. Total energy stays constant.

Or think of a planet orbiting a star: it speeds up as it falls closer (gaining kinetic energy), slows down as it climbs away (losing kinetic energy). But the total energy—kinetic plus gravitational potential—never changes.

These are fundamental laws underlying our physics, they are conservation laws. The next step in our mathematical development is to explore the structure underlying this conservation and its connection to geometric principles.

What mathematical structure enforces energy conservation? The answer will lead us to *Poisson brackets* and *Hamiltonian mechanics*.}

\slides{
**Two Types of Dynamics:**
* Entropy-driven (dissipative)
* Energy-conserving (Hamiltonian)

*Question:* What structure ensures energy conservation?
}
\include{_physics/includes/pendulum-animation.md}

\subsubsection{A Simple Question}

\notes{Consider a dynamical system with state $\mathbf{x} \in \mathbb{R}^n$ and an energy function $E(\mathbf{x})$. The system evolves according to:
$$
\dot{\mathbf{x}} = \mathbf{v}(\mathbf{x})
$$
where $\mathbf{v}$ is some velocity field.

The rate of energy change is
$$
\frac{\text{d}E}{\text{d}t} = (\nabla E)^\top \dot{\mathbf{x}} = (\nabla E)^\top \mathbf{v}
$$

**Question:** What condition on $\mathbf{v}$ ensures energy is conserved, i.e., $\frac{\text{d}E}{\text{d}t} = 0$?}

\slides{
**Energy Change Rate:**
$$
\frac{\text{d}E}{\text{d}t} = (\nabla E)^\top \mathbf{v}
$$

*Want:* $\frac{\text{d}E}{\text{d}t} = 0$ for all energy functions

*Need:* Structure on $\mathbf{v}$
}

\newslide{One Answer}

\notes{One answer would be that "$\mathbf{v}$ must be perpendicular to $\nabla E$". The inner product between two perpendicular vectors is zero. This answer is correct, but doesn't turn out to be useful. because the  answer depends on the form of $E$, it's not general.

We want something stronger: a structure that conserves *any* energy function we might choose. This means the structure must be built into the dynamics itself, independent of $E$.}

\slides{
**Naive answer:** $\mathbf{v} \perp \nabla E$

*Problem:* Depends on $E$

**Better:** Structure that conserves *any* energy function
}

\subsection{Antisymmetric Structure}

\notes{Here's the insight: suppose the velocity field has the form:
$$
\mathbf{v} = A(\mathbf{x}) \nabla E
$$
where $A(\mathbf{x})$ is an $n \times n$ matrix that depends on state.

Then
$$
\frac{\text{d}E}{\text{d}t} = (\nabla E)^\top A \nabla E
$$
is a quadratic form in $\nabla E$. When is a quadratic form always zero?}

\slides{
**Velocity structure:**
$$
\mathbf{v} = A(\mathbf{x}) \nabla E
$$

**Energy rate:**
$$
\frac{\text{d}E}{\text{d}t} = (\nabla E)^\top A \nabla E
$$

*Quadratic form in $\nabla E$*
}

\newslide{Antisymmetry Kills Quadratics}

\notes{A quadratic form $\mathbf{v}^\top A \mathbf{v}$ is always zero if and only if $A$ is *antisymmetric*
$$
A^\top = -A
$$

**Proof:** If $A^\top = -A$, then:
$$
\mathbf{v}^\top A \mathbf{v} = \mathbf{v}^\top (-A)^\top \mathbf{v} = -(A \mathbf{v})^\top \mathbf{v} = -\mathbf{v}^\top A \mathbf{v}
$$
This can only be true if $\mathbf{v}^\top A \mathbf{v} = 0$.

So antisymmetry of $A$ guarantees energy conservation for *any* energy function $E$.}

\slides{
**Key insight:**
$$
A^\top = -A \quad \Rightarrow \quad (\nabla E)^\top A \nabla E = 0
$$

*Proof:*
$$
\mathbf{v}^\top A \mathbf{v} = \mathbf{v}^\top (-A^\top) \mathbf{v} = -\mathbf{v}^\top A \mathbf{v}
$$

→ Antisymmetry ensures conservation
}

\subsection{The Geometric Picture}

\notes{Antisymmetric matrices have useful geometric properties. In 2D, an antisymmetric matrix looks like
$$
A = \begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix}
$$
This represents a $90^\degree$ rotation (scaled by $a$). The flow $\dot{\mathbf{x}} = A \nabla E$ moves perpendicular to the energy gradient, it follows contours of constant energy.

In higher dimensions, antisymmetric matrices define *skew-symmetric* transformations that preserve volumes and represent generalised rotations. Energy-conserving dynamics live on these geometric structures.}

\slides{
**2D Example:**
$$
A = \begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix}
$$

* $90^\degree$ rotation
* Flow perpendicular to $\nabla E$
* Follows energy contours
* Conserves area

*Higher dimensions:* Generalised rotations
}

\newslide{Why This Matters for Information}

\notes{We've been studying entropy-driven dynamics where systems flow downhill on the information landscape or equivalently uphill on the entropy landscape (maximise entropy). That's *dissipative* dynamics.

But real systems often have both:
- **Dissipative part**: Increases entropy, driven by Fisher metric
- **Conservative part**: Preserves energy, driven by antisymmetric structure

The combination of these two structures is called **GENERIC** (General Equation for Non-Equilibrium Reversible-Irreversible Coupling), which we'll study in Lecture 8.

For now, understand that antisymmetric structure is the geometric foundation for energy-conserving (Hamiltonian) dynamics. This complements the symmetric structure (Fisher information) we've been studying.}

\slides{
**Two Structures:**

*Symmetric (Fisher $G$):*
* Entropy maximization
* Dissipative
* Increases disorder

*Antisymmetric ($A$):*
* Energy conservation  
* Conservative
* Preserves structure

→ *GENERIC: Both together* (Lecture 8)
}

\subsection{Preview: Poisson Brackets}

\notes{This antisymmetric structure is formalized through *Poisson brackets*. For any two functions $f$ and $g$, we define
$$
\{f, g\} = (\nabla f)^\top A \nabla g.
$$
This bracket operation captures the interaction between observables in a Hamiltonian system. When $f = E$ (energy), we have
$$
\dot{g} = \{g, E\}.
$$
This says: "The rate of change of any observable $g$ is given by its Poisson bracket with energy."

In the next section, we'll develop this idea fully and see why Poisson brackets provide the natural language for Hamiltonian mechanics.}

\slides{
**Preview: Poisson Brackets**
$$
\{f, g\} = (\nabla f)^\top A \nabla g
$$

**Evolution:**
$$
\dot{g} = \{g, E\}
$$

*Natural language for Hamiltonian mechanics*

*Next: Full development*
}

\addreading{@Marsden:book99}{Chapter 2.6: Hamiltonian Flows}
\addreading{@Marsden:book99}{Chapter 5.4: Hamiltonian Systems}
\endif
