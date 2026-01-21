\ifndef{hamiltonianFlow}
\define{hamiltonianFlow}

\editme

\subsection{Hamiltonian Flow}

\notes{We've defined Poisson brackets as $\{f, g\} = (\nabla f)^\top A \nabla g$ where $A$ is antisymmetric. Now we use this structure to generate dynamics—the evolution of a system over time.}

\subsubsection{Evolution from Brackets}

\notes{Given an energy function (called the *Hamiltonian*) $H(\mathbf{x})$, the system evolves according to,
$$
\dot{\mathbf{x}} = A \nabla H.
$$
This is called **Hamiltonian flow**. The velocity at each point is determined by the energy gradient, filtered through the antisymmetric structure $A$.

For any observable $f(\mathbf{x})$, its rate of change is:
$$
\frac{\text{d}f}{\text{d}t} = (\nabla f)^\top \dot{\mathbf{x}} = (\nabla f)^\top A \nabla H = \{f, H\}.
$$
Time evolution is given by the Poisson bracket with the Hamiltonian.}

\slides{
**Hamiltonian Flow:**
$$
\dot{\mathbf{x}} = A \nabla H
$$

**Observable evolution:**
$$
\frac{\text{d}f}{\text{d}t} = \{f, H\}
$$

*Time evolution = Poisson bracket with energy*
}

\newslide{Energy Conservation Proof}

\notes{Now we can prove energy is conserved. The rate of energy change is:
$$
\frac{\text{d}H}{\text{d}t} = \{H, H\},
$$
but by antisymmetry of the Poisson bracket: $\{H, H\} = -\{H, H\}$. This is only possible if $\{H, H\} = 0$.

Therefore: $\frac{\text{d}H}{\text{d}t} = 0$ and energy is automatically conserved.

This is the reason why Hamiltonian systems conserve energy: the antisymmetric structure of the Poisson bracket makes self-interaction impossible.}

\slides{
**Energy Conservation:**
$$
\frac{\text{d}H}{\text{d}t} = \{H, H\} = -\{H, H\} = 0
$$

* Follows from antisymmetry
* Automatic, not imposed
* Geometric consequence
}

\subsection{Hamilton's Equations}

\notes{For the canonical Poisson bracket (with state $\mathbf{x} = (\mathbf{q}, \mathbf{p})$ and $A = \begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}$), Hamiltonian flow gives  *Hamilton's equations*,
$$
\dot{\mathbf{q}} = \frac{\partial H}{\partial \mathbf{p}}, \quad \dot{\mathbf{p}} = -\frac{\partial H}{\partial \mathbf{q}}.
$$

**Interpretation:**

- Position changes in the direction of momentum gradient
- Momentum changes opposite to position gradient (force = $\nabla H$)

These are equivalent to Newton's laws $F = ma$, but expressed in a geometric form that makes conservation laws and symmetries manifest.}

\slides{
*Hamilton's Equations (Canonical):*
$$
\dot{\mathbf{q}} = \frac{\partial H}{\partial \mathbf{p}}
$$
$$
\dot{\mathbf{p}} = -\frac{\partial H}{\partial \mathbf{q}}
$$

* $\mathbf{q}$ follows momentum gradient
* $\mathbf{p}$ follows force (negative position gradient)
* Equivalent to Newton's laws
* Geometric form reveals structure
}

\newslide{Phase Space Geometry}

\notes{Hamiltonian flow lives in *phase space*, the space of all possible states $(\mathbf{q}, \mathbf{p})$. Each point in phase space represents a complete state of the system.

Key geometric properties:

1. **Flow preserves energy**: Trajectories stay on energy surfaces $H(\mathbf{q}, \mathbf{p}) = E$.

2. **Symplectic structure**: The antisymmetric matrix $A$ defines a geometric structure called a *symplectic form*. Hamiltonian flow preserves this structure.

3. **Volume preservation (Liouville's theorem)**: Phase space "volume" (properly defined) is conserved along flow. If you track a region of initial conditions, its volume stays constant even as it deforms.

These aren't separate facts, they're all consequences of the antisymmetric Poisson structure.}

\slides{
**Phase Space Geometry:**
* Space of states $(\mathbf{q}, \mathbf{p})$
* Flow on energy surfaces
* Symplectic structure preserved
* Volume preserved (Liouville)

*All from antisymmetric structure*
}

\subsection{Example: Harmonic Oscillator}

\notes{Consider a simple harmonic oscillator: a mass $m$ attached to a spring with stiffness $k$. 

**State:** position $q$ and momentum $p$

**Hamiltonian (energy):**
$$
H(q, p) = \frac{p^2}{2m} + \frac{kq^2}{2}
$$

**Hamilton's equations:**
$$
\dot{q} = \frac{\partial H}{\partial p} = \frac{p}{m}, \quad \dot{p} = -\frac{\partial H}{\partial q} = -kq
$$

**Interpretation:**
- Velocity = momentum / mass (definition)
- Force = -kq (Hooke's law)

Combining: $\ddot{q} = \dot{p}/m = -kq/m$, which gives $\ddot{q} + \omega^2 q = 0$ with $\omega = \sqrt{k/m}$.

This is the standard oscillator equation. Solution: $q(t) = A \cos(\omega t + \phi)$ and $p(t) = -m\omega A \sin(\omega t + \phi)$.

Let's visualize the phase space flow:}

\setupcode{import numpy as np}

\code{# Harmonic oscillator parameters
m = 1.0  # mass
k = 1.0  # spring constant
omega = np.sqrt(k/m)  # natural frequency

# Hamiltonian (total energy)
def hamiltonian(q, p):
    return p**2 / (2*m) + k * q**2 / 2

# Hamilton's equations
def hamilton_flow(t, state):
    q, p = state
    dq_dt = p / m           # ∂H/∂p
    dp_dt = -k * q          # -∂H/∂q
    return np.array([dq_dt, dp_dt])

# Integrate several trajectories with different initial energies
from scipy.integrate import solve_ivp

t_span = (0, 15)
t_eval = np.linspace(0, 15, 500)

# Different initial conditions (different energies)
initial_conditions = [
    np.array([1.0, 0.0]),    # E ≈ 0.5
    np.array([1.5, 0.0]),    # E ≈ 1.125
    np.array([2.0, 0.0]),    # E = 2.0
]

trajectories = []
for ic in initial_conditions:
    sol = solve_ivp(hamilton_flow, t_span, ic, t_eval=t_eval, 
                    method='RK45', rtol=1e-8)
    trajectories.append(sol)
    E_initial = hamiltonian(ic[0], ic[1])
    E_final = hamiltonian(sol.y[0, -1], sol.y[1, -1])
    print(f"Initial: q={ic[0]:.2f}, p={ic[1]:.2f}, E={E_initial:.6f}")
    print(f"Final:   q={sol.y[0,-1]:.2f}, p={sol.y[1,-1]:.2f}, E={E_final:.6f}")
    print(f"ΔE = {abs(E_final - E_initial):.2e}\n")}

\setupplotcode{import matplotlib.pyplot as plt
from mlai.utils import write_figure}

\plotcode{fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Left panel: Phase space portrait
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.3)
ax1.axhline(y=0, color='k', linewidth=0.5)
ax1.axvline(x=0, color='k', linewidth=0.5)

colors = ['blue', 'green', 'red']
for i, (sol, color) in enumerate(zip(trajectories, colors)):
    q = sol.y[0]
    p = sol.y[1]
    E = hamiltonian(initial_conditions[i][0], initial_conditions[i][1])
    
    ax1.plot(q, p, color=color, linewidth=2, label=f'E = {E:.2f}')
    
    # Mark starting point
    ax1.plot(q[0], p[0], 'o', color=color, markersize=8)
    
    # Add arrow to show direction
    idx = len(q) // 4
    ax1.annotate('', xy=(q[idx+5], p[idx+5]), xytext=(q[idx], p[idx]),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))

# Draw energy contours
q_grid = np.linspace(-2.5, 2.5, 100)
p_grid = np.linspace(-2.5, 2.5, 100)
Q, P = np.meshgrid(q_grid, p_grid)
E_grid = hamiltonian(Q, P)

contours = ax1.contour(Q, P, E_grid, levels=[0.5, 1.125, 2.0], 
                       colors=['blue', 'green', 'red'], 
                       linestyles='--', alpha=0.3, linewidths=1)

ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)
ax1.set_xlabel('Position q')
ax1.set_ylabel('Momentum p')
ax1.set_title('Phase Space: Circular Orbits at Constant Energy')
ax1.legend()

# Right panel: Energy conservation over time
ax2.grid(True, alpha=0.3)

for i, (sol, color) in enumerate(zip(trajectories, colors)):
    t = sol.t
    E = hamiltonian(sol.y[0], sol.y[1])
    E_mean = np.mean(E)
    
    ax2.plot(t, (E - E_mean) / E_mean * 1e6, color=color, linewidth=2,
            label=f'E = {E_mean:.2f}')

ax2.set_xlabel('Time t')
ax2.set_ylabel('Relative energy error (ppm)')
ax2.set_title('Energy Conservation: ΔE/E over Time')
ax2.legend()
ax2.set_ylim(-1, 1)

plt.tight_layout()

write_figure('harmonic-oscillator-phase-space.svg', directory='\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/harmonic-oscillator-phase-space}{80%}}{Left: Phase space trajectories for the harmonic oscillator at three different energy levels. Each orbit is a perfect circle, demonstrating that energy surfaces in phase space are closed curves. The antisymmetric structure ensures flow is tangent to these curves (energy conserved). Right: Numerical verification of energy conservation—errors are at machine precision level, confirming the Hamiltonian flow preserves energy.}{harmonic-oscillator-phase-space}

\notes{The phase space portrait reveals the geometric structure:
- **Circular orbits**: Each energy level corresponds to a circular trajectory in $(q, p)$ space
- **Foliation**: Phase space is "foliated" (layered) by these energy surfaces
- **Tangent flow**: The Hamiltonian vector field $A \nabla H$ is everywhere tangent to these circles
- **Conservation**: Points on a circle stay on that circle forever—this is what energy conservation means geometrically

The harmonic oscillator is the prototypical "integrable" system: its phase space is completely foliated by closed curves, and its dynamics are perfectly periodic.}

\slides{
**Harmonic Oscillator:**
$$
H = \frac{p^2}{2m} + \frac{kq^2}{2}
$$

*Hamilton's equations:*
$$
\dot{q} = \frac{p}{m}, \quad \dot{p} = -kq
$$

*Solution:* $q(t) = A\cos(\omega t + \phi)$

*Phase space: circular orbits*

*Energy conserved to machine precision*
}

\newslide{Phase Space Portrait}

\notes{In phase space, the harmonic oscillator traces out ellipses. Each ellipse corresponds to a fixed energy $E = H(q, p)$.

- Small energy $\rightarrow$ small ellipse (gentle oscillation)
- Large energy $\rightarrow$ large ellipse (vigorous oscillation)
- All trajectories are closed loops (periodic motion)

The flow rotates around the origin at angular frequency $\omega$. Higher energy orbits are larger but have the same period—this is special to harmonic oscillators.

The antisymmetric structure ensures trajectories never cross (uniqueness of solutions) and energy surfaces are preserved. The geometry completely determines the dynamics.}

\slides{
**Phase Space Picture:**
* Trajectories = ellipses
* Each ellipse = constant energy
* Clockwise rotation, frequency $\omega$
* Never cross (uniqueness)
* Geometry determines dynamics
}

\subsection{Beyond Simple Systems}

\notes{The Hamiltonian formalism extends far beyond simple mechanical systems:

1. **Many particles**: Each particle contributes $(q_i, p_i)$ to phase space. The antisymmetric structure naturally extends.

2. **Fields**: Infinite-dimensional systems (like electromagnetic fields) have Hamiltonian formulations where the "phase space" is a function space.

3. **Constraints**: Systems with constraints (e.g., rigid body motion) can be handled by restricting to constraint surfaces in phase space.

4. **Information systems**: As we'll see, probability distributions can be viewed as living in a Hamiltonian-like structure, even without obvious "position" and "momentum" variables.

The power of the Hamiltonian approach is its generality: antisymmetric structure + energy function $\rightarrow$ complete dynamics.}

\slides{
**Extensions:**
* Many particles $\rightarrow$ high-dimensional phase space
* Fields $\rightarrow$ infinite dimensions
* Constraints $\rightarrow$ restricted surfaces
* Information systems $\rightarrow$ probability geometry

*Key:* Antisymmetric structure + energy $\rightarrow$ dynamics
}

\newslide{Connection to GENERIC}

\notes{In real systems, we often have both:
- **Hamiltonian part** (antisymmetric $A$): Conserves energy, reversible
- **Dissipative part** (symmetric $G$): Increases entropy, irreversible

The full dynamics combine both:
$$
\dot{\mathbf{x}} = A \nabla H + G \nabla S
$$

where $H$ is energy and $S$ is entropy. This is the GENERIC structure we'll study in Lecture 8.

For The Inaccessible Game:
- $G$ is the Fisher information matrix (we've studied this)
- $A$ is the antisymmetric Poisson structure (we're learning now)
- Both are needed for realistic information dynamics

Hamiltonian mechanics gives us the $A$ part; entropy maximization gives us the $G$ part.}

\slides{
**Preview: GENERIC**
$$
\dot{\mathbf{x}} = A \nabla H + G \nabla S
$$

*Hamiltonian:* $A$ (energy conserving)

*Dissipative:* $G$ (entropy increasing)

*TIG needs both* (Lecture 8)
}

\addreading{@Marsden:book99}{Chapter 2.6: Hamiltonian Flows}
\addreading{@Marsden:book99}{Chapter 5.4: Hamiltonian Systems}
\addreading{@Marsden:book99}{Chapter 10.3: Properties of Hamiltonian Flows}
\endif
