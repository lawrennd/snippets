\ifndef{conservativeDissipativeEmergence}
\define{conservativeDissipativeEmergence}

\editme

\subsection{Beyond Second Order: Conservative Dynamics Emerge}

\notes{We saw that at second order, the dynamics are purely dissipative: $\dot{q} \approx \Pi_\parallel S q$ with $S$ symmetric.

But what happens when we include the next-order corrections? Perhaps surprisingly, *conservative (Hamiltonian) dynamics emerge* from the geometry of information.}

\slides{
**Beyond Gaussian Regime**

Second order: $\dot{q} = \Pi_\parallel S q$ (purely dissipative)

**Question:** What happens at higher order?

**Answer:** Conservative dynamics emerge!
}

\subsection{Third-Order Corrections}

\notes{Recall the full expansion:
$$
F(\boldsymbol{\theta}^\ast + q) = \Pi_\parallel S q + \mathscr{B}(q) + O(\|q\|^3)
$$
The quadratic correction term $\mathscr{B}(q) = O(\|q\|^2)$ has two sources.

**1. Third cumulants (non-Gaussian effects)**
$$
\mathscr{B}_{\text{cumulant}}(q) = \Pi_\parallel \left(\frac{1}{2} T[q,q]\right),
$$
where $T = \nabla^3 \mathscr{L}|_{\boldsymbol{\theta}^\ast,\nu^\ast}$ is the third-order tensor (fully symmetric). The contraction $T[q,q]$ gives a vector with components $[T[q,q]]_i = \sum_{jk} T_{ijk} q_j q_k$.

**2. Constraint curvature**
$$
\mathscr{B}_{\text{curvature}}(q) = \left(\frac{\partial \Pi_\parallel}{\partial \boldsymbol{\theta}}\bigg|_{\boldsymbol{\theta}^\ast}[q]\right) S q.
$$
The projector $\Pi_\parallel(\boldsymbol{\theta})$ depends on $\boldsymbol{\theta}$ through $a(\boldsymbol{\theta})$. As we move along the constraint manifold, the tangent space rotates—this is curvature.

Both terms are $O(\|q\|^2)$, so they're smaller than the leading $O(\|q\|)$ dissipative term. But their *structure* is fundamentally different.}

\slides{
**Quadratic Corrections: $\mathscr{B}(q) = O(\|q\|^2)$**

Two sources:

**1. Third cumulants**
$$
\Pi_\parallel\left(\frac{1}{2}T[q,q]\right)
$$
* $T = \nabla^3 \mathscr{L}$ (non-Gaussian effects)

**2. Constraint curvature**
$$
\left(\frac{\partial \Pi_\parallel}{\partial \boldsymbol{\theta}}[q]\right) Sq
$$
* Tangent space rotates along manifold
}

\subsection{The Jacobian and Antisymmetry}

\notes{To get linearised dynamics, we need the Jacobian of $F$ at $\boldsymbol{\theta}^\ast$
$$
\nabla F(\boldsymbol{\theta}^\ast) = \frac{\partial F}{\partial \boldsymbol{\theta}}\bigg|_{\boldsymbol{\theta}^\ast} = \Pi_\parallel S + \nabla \mathscr{B}(0)
$$

**Key observation:** Although $S$ is symmetric and $T$ is fully symmetric, their combination through the projector $\Pi_\parallel$ and the curvature terms creates an *antisymmetric component* in $\nabla \mathscr{B}(0)$.

Why? Two reasons:

1. **Third cumulants under projection:** When we project the third-order tensor $T[q,q]$ onto the tangent space and then take its Jacobian, the result is not symmetric. The tensor $T$ encodes how the distribution deviates from Gaussian, and these deviations create rotational tendencies.

2. **Curvature of the constraint:** The derivative of the projector $\partial_{\boldsymbol{\theta}} \Pi_\parallel$ introduces geometric Berry-like phases. As perturbations move along the curved constraint manifold, they pick up geometric rotations.

Define the antisymmetric part
$$
A := \frac{1}{2}\left(\nabla \mathscr{B}(0) - \nabla \mathscr{B}(0)^\top\right).
$$
This is **generically non-zero** when

- The distribution is non-Gaussian ($T \neq 0$)
- The constraint surface is curved ($\nabla a \neq 0$)
}

\slides{
**Linearised Dynamics**

Jacobian: $\nabla F(\boldsymbol{\theta}^\ast) = \Pi_\parallel S + \nabla \mathscr{B}(0)$

**Antisymmetric part emerges:**
$$
A = \frac{1}{2}\left(\nabla \mathscr{B}(0) - \nabla \mathscr{B}(0)^\top\right)
$$

**Sources:**
* Third cumulants (non-Gaussian)
* Constraint curvature (geometry)

**Result:** $A \neq 0$ generically!
}

\subsection{The GENERIC Decomposition}

\notes{The complete linearised dynamics decompose as:
$$
\nabla F(\boldsymbol{\theta}^\ast) = \underbrace{\Pi_\parallel S \Pi_\parallel}_{\text{symmetric}} + \underbrace{A}_{\text{antisymmetric}}
$$
This is the **GENERIC decomposition** (General Equation for Non-Equilibrium Reversible-Irreversible Coupling), studied extensively in non-equilibrium thermodynamics.

**Symmetric part** ($\Pi_\parallel S \Pi_\parallel$):
- Dissipative / gradient flow
- Drives entropy production: $\dot{H} \sim q^\top (\Pi_\parallel S \Pi_\parallel) q$
- Eigenvalues real (exponential decay/growth)
- "Irreversible" component

**Antisymmetric part** ($A$):
- Conservative / Hamiltonian flow  
- No entropy production: $q^\top A q = 0$ for all $q$
- Eigenvalues purely imaginary (oscillations)
- "Reversible" component

The dynamics near equilibrium are:
$$
\dot{q} = (\Pi_\parallel S \Pi_\parallel + A) q
$$
combining dissipation with conservative flow.}

\slides{
**GENERIC Decomposition**

$$
\nabla F = \underbrace{\Pi_\parallel S \Pi_\parallel}_{\text{dissipative}} + \underbrace{A}_{\text{conservative}}
$$

**Symmetric:** 
* Entropy production
* Real eigenvalues
* Irreversible

**Antisymmetric:**
* Energy-conserving
* Imaginary eigenvalues
* Reversible

**Together:** Damped oscillations + rotation
}

\subsection{Physical Interpretation}

\notes{Why does this matter? The GENERIC structure reveals that *information dynamics naturally exhibit both thermodynamic and mechanical behavior*

**Thermodynamic (from $S$)**

- System dissipates toward maximum entropy
- Irreversible approach to equilibrium
- Second law of thermodynamics
- Arises from Gaussian/second-order effects

**Mechanical (from $A$)**

- Energy-conserving rotations
- Reversible oscillations
- Poisson structure (recall Lecture 5!)
- Arises from non-Gaussian/geometric effects

This isn't imposed, it emerges from the mathematics:

1. Start with constrained maximum entropy production
2. Expand near equilibrium
3. Leading order: symmetric (dissipative)
4. Next order: antisymmetric part appears
5. Result: Mixed dissipative-conservative dynamics

**Connection to physics:** Many physical systems have this structure

- Damped harmonic oscillator: $\ddot{x} + \gamma \dot{x} + \omega^2 x = 0$
- Fluid dynamics with viscosity and vorticity
- Chemical reactions with detailed balance
- Non-equilibrium thermodynamics

The information geometry *automatically* generates this structure.}

\slides{
**Physical Picture**

**GENERIC = Thermodynamics + Mechanics**

From $S$:
* Dissipation
* Entropy production
* Second law

From $A$:
* Conservation
* Oscillations
* Hamiltonian structure

**Emerges naturally** from information geometry!
}

\subsection{Connection to Poisson Brackets}

\notes{Recall from Lecture 5 that Poisson brackets encode Hamiltonian dynamics. The antisymmetric operator $A$ defines a Poisson structure on the constraint tangent space.

For any two functions $f, g$ on the tangent space, the Poisson bracket is:
$$
\{f, g\} = (\nabla f)^\top A (\nabla g)
$$

This satisfies

- Antisymmetry: $\{f, g\} = -\{g, f\}$
- Jacobi identity (when $A$ comes from a proper Hamiltonian structure)
- Conservation: If $\{f, H\} = 0$, then $f$ is conserved along Hamiltonian flow

The antisymmetric part $A$ might be **degenerate** (not full rank), meaning

- Some directions have no Hamiltonian flow (Casimirs)
- The system is "partially Hamiltonian"
- This is typical when third cumulants are weak or constraint curvature is small

As the system moves away from the Gaussian regime (stronger non-Gaussian features), $A$ becomes larger relative to $S$, and conservative dynamics become more important.}

\slides{
**Poisson Structure**

Antisymmetric $A$ defines Poisson bracket:
$$
\{f, g\} = (\nabla f)^\top A (\nabla g)
$$

**Properties:**

* Antisymmetry: $\{f, g\} = -\{g, f\}$
* Generates Hamiltonian flow
* May be degenerate (Casimirs)

**Away from Gaussian:** $A$ grows, more conservative
}

\notes{**Summary:** The GENERIC structure—decomposition into dissipative and conservative parts. This is not assumed but *derived* from constrained maximum entropy production. The symmetric part emerges at second order (Gaussian regime), while the antisymmetric part appears at third order from non-Gaussian effects and constraint geometry. This decomposition reveals that information dynamics exhibit both thermodynamics (irreversible) and mechanics (reversible).}
\endif
