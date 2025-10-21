\ifndef{poissonBracketsDefinition}
\define{poissonBracketsDefinition}

\editme

\subsection{Poisson Brackets: Definition}

\notes{We've seen that antisymmetric structure ensures energy conservation. Now we formalise this through *Poisson brackets*, which provide the underlying algebraic structure for Hamiltonian mechanics.}

\subsubsection{The Bracket Operation}

\notes{Given an antisymmetric matrix $A(\mathbf{x})$ (which may depend on state $\mathbf{x}$), we define the *Poisson bracket* of two functions $f, g: \mathbb{R}^n \rightarrow \mathbb{R}$ as:
$$
\{f, g\} = (\nabla f)^\top A \nabla g = \sum_{i,j} A_{ij} \frac{\partial f}{\partial x_i} \frac{\partial g}{\partial x_j}
$$
This operation takes two functions and produces a new function. Think of it as measuring "how $f$ and $g$ interact" through the antisymmetric structure $A$.}

\slides{
**Poisson Bracket:**
$$
\{f, g\} = (\nabla f)^\top A \nabla g
$$

* Input: Two functions $f$, $g$
* Output: New function $\{f, g\}$
* Structure: Antisymmetric matrix $A$

*Measures interaction between observables*
}

\subsection{Properties of Poisson Brackets}

\newslide{1. Antisymmetry}

\notes{**Antisymmetry:** The bracket is antisymmetric in its arguments:
$$
\{f, g\} = -\{g, f\}
$$

**Proof:** Since $A^\top = -A$:
$$
\{g, f\} = (\nabla g)^\top A \nabla f = (\nabla f)^\top A^\top \nabla g = -(\nabla f)^\top A \nabla g = -\{f, g\}.
$$

**Consequence:** $\{f, f\} = 0$ for any function $f$. In particular, $\{E, E\} = 0$, consistent with energy conservation.}

\slides{
**1. Antisymmetry:**
$$
\{f, g\} = -\{g, f\}
$$

→ $\{f, f\} = 0$

→ $\{E, E\} = 0$. (energy conserves itself)
}

\newslide{2. Bilinearity}

\notes{**Bilinearity:** The bracket is linear in each argument
$$
\{af + bg, h\} = a\{f, h\} + b\{g, h\}
$$
$$
\{f, ag + bh\} = a\{f, g\} + b\{f, h\}.
$$
This follows from linearity of differentiation and matrix multiplication.}

\slides{
**2. Bilinearity:**
$$
\{af + bg, h\} = a\{f, h\} + b\{g, h\}
$$

* Linear in each argument
* Follows from $\nabla$ linearity
}

\newslide{3. Leibniz Rule}

\notes{**Leibniz Rule (Product Rule):** The bracket satisfies
$$
\{fg, h\} = f\{g, h\} + \{f, h\}g.
$$
This says the bracket acts like a derivation, it satisfies the product rule. This property is crucial for interpreting $\{f, E\}$ as the "time derivative" of $f$ along Hamiltonian flow.}

\slides{
**3. Leibniz Rule:**
$$
\{fg, h\} = f\{g, h\} + \{f, h\}g
$$

* Bracket acts like a derivative
* Product rule holds
* Key for Hamiltonian evolution
}

\newslide{4. Jacobi Identity}

\notes{**Jacobi Identity:** The bracket satisfies a more subtle property
$$
\{\{f, g\}, h\} + \{\{g, h\}, f\} + \{\{h, f\}, g\} = 0
$$
This is a consistency condition that ensures the bracket structure is "coherent." It's analogous to the associativity property for multiplication, but adapted for the antisymmetric bracket structure.

The Jacobi identity is what makes Poisson brackets form a *Lie algebra*, a structure in mathematics and physics. We won't prove it here (the proof requires checking derivatives carefully), but it's always satisfied when $A$ is antisymmetric and satisfies certain smoothness conditions.}

\newslide{What is a Lie Algebra?}

\notes{Think of a Lie algebra as "the algebra of infinitesimal transformations." 

**The intuition:** When you have continuous symmetries (like rotations, translations, or time evolution), you can study them in two ways:
- **Global transformations** (finite rotations, moving distances) - these multiply like a group
- **Infinitesimal transformations** (tiny nudges, derivatives) - these add like a vector space

A Lie algebra is the infinitesimal version. Instead of "rotate by 45°", think "rotate by an infinitesimal amount in this direction." These infinitesimal transformations are linear, so they're much easier to work with than the full nonlinear group.

**What they're for:** The bracket operation (like the Poisson bracket) tells you how two infinitesimal symmetries interact. For example:
- An infinitesimal rotation around x-axis + infinitesimal rotation around y-axis
- Doesn't quite get you back where you started
- The "mismatch" is measured by their bracket

This shows up everywhere: quantum mechanics (commutators), Poisson brackets (classical mechanics), neural networks (tangent spaces to manifolds), control theory (drift and control). Once you understand the pattern, you see it in many areas of mathematics.

For us: Poisson brackets form a Lie algebra, which means they capture the infinitesimal structure of conserved quantities and symmetries.}

\slides{
**Lie Algebra Intuition:**
* Infinitesimal transformations
* "Tiny nudges" not "finite moves"
* Bracket = how two nudges interact
* Appear everywhere in physics/math
* Poisson brackets form one
}

\notes{
\subsection{A Simple 2D Example}

Let's see this concretely with 2D rotations. A rotation by angle $\theta$ is given by the matrix
$$
R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
$$
This is the "finite transformation" view. Now let's look at the infinitesimal version. For tiny $\epsilon$
$$
R(\epsilon) \approx \begin{pmatrix} 1 & -\epsilon \\ \epsilon & 1 \end{pmatrix} = I + \epsilon \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
$$
The matrix $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ is the *generator*, it's the Lie algebra element. 

You can recover the finite rotation by "exponentiating" the generator. The *matrix exponential* $e^{\theta J}$ is defined by the power series (just like the scalar exponential),
$$
R(\theta) = e^{\theta J} = I + \theta J + \frac{\theta^2}{2!} J^2 + \frac{\theta^3}{3!} J^3 + \ldots,
$$
or equivalently, it's the limit of taking many tiny steps:
$$
e^{\theta J} = \lim_{n \to \infty} \left(I + \frac{\theta}{n} J\right)^n.
$$
This is the Lie algebra perspective: store the generator $J$ (linear, simple) and exponentiate to get the finite transformation (nonlinear). The visualization below shows this limiting process.

We visualise this in the figure below.
}

\setupcode{import numpy as np}

\code{# Generator for 2D rotations
J = np.array([[0, -1], 
              [1, 0]])

# A point to rotate
v = np.array([1, 0])

# Finite rotation by pi/3
theta = np.pi / 3
R_finite = np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

# Build the same rotation from many infinitesimal steps
n_steps = 20
epsilon = theta / n_steps

# Starting point
path = [v]
v_current = v.copy()

for i in range(n_steps):
    # Infinitesimal rotation: R(ε) ≈ I + εJ
    R_infinitesimal = np.eye(2) + epsilon * J
    v_current = R_infinitesimal @ v_current
    path.append(v_current.copy())

path = np.array(path)

# Final point using finite rotation
v_final = R_finite @ v

print(f"Finite rotation result: ({v_final[0]:.4f}, {v_final[1]:.4f})")
print(f"Built from infinitesimals: ({v_current[0]:.4f}, {v_current[1]:.4f})")
print(f"Difference: {np.linalg.norm(v_final - v_current):.6f}")}

\setupplotcode{import matplotlib.pyplot as plt
from mlai.utils import write_figure}

\plotcode{fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left panel: The generator and infinitesimal rotation
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.3)
ax1.axhline(y=0, color='k', linewidth=0.5)
ax1.axvline(x=0, color='k', linewidth=0.5)

# Original vector
ax1.arrow(0, 0, v[0], v[1], head_width=0.1, head_length=0.1, 
          fc='blue', ec='blue', linewidth=2, label='Original')

# Infinitesimal rotation
v_small = (np.eye(2) + 0.3 * J) @ v
ax1.arrow(0, 0, v_small[0], v_small[1], head_width=0.1, head_length=0.1,
          fc='red', ec='red', linewidth=2, alpha=0.7, label='After tiny rotation')

# Show the generator action: J·v (perpendicular)
Jv = J @ v
ax1.arrow(v[0], v[1], 0.3*Jv[0], 0.3*Jv[1], head_width=0.08, head_length=0.08,
          fc='green', ec='green', linewidth=2, label='Generator J·v')

ax1.set_xlim(-0.5, 1.5)
ax1.set_ylim(-0.5, 1.5)
ax1.legend(loc='upper left')
ax1.set_title('Lie Algebra View: Generator J and Infinitesimal Rotation')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

# Right panel: Building finite rotation from infinitesimals
ax2.set_aspect('equal')
ax2.grid(True, alpha=0.3)
ax2.axhline(y=0, color='k', linewidth=0.5)
ax2.axvline(x=0, color='k', linewidth=0.5)

# Draw the path
ax2.plot(path[:, 0], path[:, 1], 'o-', color='orange', alpha=0.5, 
         markersize=4, label=f'{n_steps} tiny steps')

# Original and final vectors
ax2.arrow(0, 0, v[0], v[1], head_width=0.1, head_length=0.1,
          fc='blue', ec='blue', linewidth=2, label='Start')
ax2.arrow(0, 0, v_final[0], v_final[1], head_width=0.1, head_length=0.1,
          fc='red', ec='red', linewidth=2, label=f'After rotation by π/3')

# Draw the arc for the finite rotation
angles = np.linspace(0, theta, 50)
arc = np.array([[np.cos(a), np.sin(a)] for a in angles])
ax2.plot(arc[:, 0], arc[:, 1], '--', color='gray', alpha=0.5, linewidth=1)

ax2.set_xlim(-0.5, 1.5)
ax2.set_ylim(-0.5, 1.5)
ax2.legend(loc='upper left')
ax2.set_title('Finite Rotation = Exponentiate the Generator: $e^{\\theta J}$')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

plt.tight_layout()

write_figure('lie-algebra-rotation-example.svg', directory='\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/lie-algebra-rotation-example}{80%}}{*Left*: The generator $J$ defines the infinitesimal rotation—it points perpendicular to the current position (tangent to the circle). *Right*: A finite rotation is built by exponentiating the generator, equivalent to taking many tiny steps. The Lie algebra is the "linearised" view of rotations.}{lie-algebra-rotation-example}

\notes{The figure gives the insight on Lie algebras. 
- **Left**: The generator $J$ acts on a vector by rotating it infinitesimally. The direction is perpendicular (tangent to the circular orbit).
- **Right**: A finite rotation of 60° is built by applying many tiny rotations. The limit as steps → ∞ is $e^{\theta J}$.

This is why Lie algebras are powerful: they linearise the nonlinear group structure, making calculations tractable while preserving the essential geometry.}

\slides{
**4. Jacobi Identity:**
$$
\{\{f, g\}, h\} + \{\{g, h\}, f\} + \{\{h, f\}, g\} = 0
$$

* Consistency condition
* Makes brackets a *Lie algebra*
* Always satisfied for smooth antisymmetric $A$
* (Proof omitted - technical)
}

\subsection{The Canonical Poisson Bracket}

\notes{The most famous example is the *canonical Poisson bracket* in classical mechanics. For a system with position $\mathbf{q} = (q_1, \ldots, q_n)$ and momentum $\mathbf{p} = (p_1, \ldots, p_n)$, we have state $\mathbf{x} = (\mathbf{q}, \mathbf{p})$.

The canonical antisymmetric matrix is:
$$
A = \begin{pmatrix} 0 & I_n \\ -I_n & 0 \end{pmatrix}
$$
where $I_n$ is the $n \times n$ identity matrix.

This gives the canonical Poisson bracket:
$$
\{f, g\} = \sum_{i=1}^n \left( \frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i} \right)
$$

This is the foundation of Hamiltonian mechanics.

**Why "canonical"?** Just as natural parameters are the canonical coordinates for exponential families\noteFootnote{Recall from Lecture 1: natural parameters $\boldsymbol{\theta}$ are the coordinates where the Fisher information metric takes its simplest form and the statistical geometry is clearest.}, the $(q, p)$ coordinates are canonical for Hamiltonian systems. Darboux's theorem guarantees that for any symplectic manifold, you can always find local coordinates where the Poisson bracket takes this standard form, it's the "natural" coordinate system for the geometry of phase space.}

\slides{
**Canonical Example (Mechanics):**

*State:* $\mathbf{x} = (\mathbf{q}, \mathbf{p})$ (position, momentum)

*Matrix:*
$$
A = \begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}
$$

*Bracket:*
$$
\{f, g\} = \sum_i \left( \frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i} \right)
$$
}

\newslide{Fundamental Brackets}

\notes{In the canonical case, the fundamental brackets are:
$$
\{q_i, q_j\} = 0, \quad \{p_i, p_j\} = 0, \quad \{q_i, p_j\} = \delta_{ij}
$$

These express that:
- Positions don't interact with each other (through Hamiltonian structure)
- Momenta don't interact with each other
- Each position interacts with its conjugate momentum

These "fundamental brackets" completely determine all other brackets through bilinearity and the Leibniz rule.}

\slides{
**Fundamental Brackets:**
$$
\{q_i, q_j\} = 0
$$
$$
\{p_i, p_j\} = 0
$$
$$
\{q_i, p_j\} = \delta_{ij}
$$

* Positions don't interact
* Momenta don't interact  
* Position-momentum pairs interact
* Determines all other brackets
}

\subsection{Beyond Canonical Form}

\notes{The canonical bracket is special, but not all Hamiltonian systems have this form. More generally:

1. **Curved spaces**: When the system lives on a manifold (not just $\mathbb{R}^{2n}$), the Poisson structure must be adapted to the geometry.

2. **Degenerate structures**: The matrix $A$ may not have full rank. This creates *Casimir functions* (next section).

3. **Information systems**: For information dynamics, we'll see Poisson brackets appear naturally from the geometry of probability distributions, even when there's no obvious "position" or "momentum."

The key is the antisymmetric structure $A$ and the properties it satisfies, not the specific canonical form.}

\slides{
**Beyond Canonical:**

* Curved spaces → adapt to geometry
* Degenerate $A$ → Casimirs (next)
* Information systems → from probability geometry

*Key:* Antisymmetric structure, not specific form
}

\addreading{@Marsden:book99}{Chapter 2.7: Poisson Brackets}
\addreading{@Marsden:book99}{Chapter 3.3: Examples: Poisson Brackets and Conserved Quantities}
\addreading{@Marsden:book99}{Chapter 5.5: Poisson Brackets on Symplectic Manifolds}
\addreading{@Marsden:book99}{Chapter 10.1-10.2: The Definition of Poisson Manifolds}

\endif

