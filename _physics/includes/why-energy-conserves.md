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

\newslide{Pendulum Animation}

\setupcode{import numpy as np}

\helpercode{def pendulum_energy(theta, omega):
    """Total energy: kinetic + potential"""
    kinetic = 0.5 * m * L**2 * omega**2
    potential = m * g * L * (1 - np.cos(theta))
    return kinetic + potential

def pendulum_dynamics(state, t):
    """Derivatives: [dθ/dt, dω/dt]"""
    theta, omega = state
    dtheta = omega
    domega = -(g/L) * np.sin(theta)  # From energy conservation!
    return np.array([dtheta, domega])
}

\code{# Simple pendulum: trading potential ↔ kinetic energy
# State: angle θ and angular velocity ω
# Energy: E = (1/2)mL²ω² + mgL(1-cos(θ))

# Parameters
g = 9.81  # gravity
L = 1.0   # length
m = 1.0   # mass

# Initial conditions: release from angle, zero velocity
theta0 = np.pi/3  # 60 degrees
omega0 = 0.0
initial_state = np.array([theta0, omega0])
initial_energy = pendulum_energy(theta0, omega0)

# Simulate using simple Euler method (Hamiltonian structure preserves energy well)
dt = 0.02
t_max = 5.0
num_steps = int(t_max / dt)

# Arrays to store trajectory
times = np.linspace(0, t_max, num_steps)
trajectory = np.zeros((num_steps, 2))
energies = np.zeros(num_steps)

# Integrate
state = initial_state.copy()
for i in range(num_steps):
    trajectory[i] = state
    energies[i] = pendulum_energy(state[0], state[1])
    # Simple symplectic Euler (preserves energy structure better)
    state[1] += pendulum_dynamics(state, times[i])[1] * dt
    state[0] += state[1] * dt

# Verify energy conservation
energy_drift = np.abs(energies - initial_energy).max()
print(f"Maximum energy drift: {energy_drift/initial_energy*100:.2f}%")}

\setupplotcode{import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mlai.utils import write_animation}

\plotcode{# Create animation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left: pendulum visualization
ax1.set_xlim(-1.2*L, 1.2*L)
ax1.set_ylim(-1.2*L, 0.2*L)
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.3)
ax1.set_title('Pendulum Motion')

# Right: energy over time
ax2.set_xlim(0, t_max)
ax2.set_ylim(0, initial_energy*1.2)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Energy (J)')
ax2.set_title('Energy Conservation')
ax2.grid(True, alpha=0.3)

# Add horizontal line for initial energy
ax2.axhline(initial_energy, color='k', linestyle='--', alpha=0.5, label='Initial E')
ax2.legend()

# Animation objects
line, = ax1.plot([], [], 'o-', lw=2, markersize=10, color='blue')
trace, = ax1.plot([], [], alpha=0.3, color='blue')
energy_line, = ax2.plot([], [], color='red', label='Total E')
kinetic_line, = ax2.plot([], [], color='green', alpha=0.5, label='Kinetic')
potential_line, = ax2.plot([], [], color='orange', alpha=0.5, label='Potential')

trace_x, trace_y = [], []

def init():
    line.set_data([], [])
    trace.set_data([], [])
    energy_line.set_data([], [])
    kinetic_line.set_data([], [])
    potential_line.set_data([], [])
    return line, trace, energy_line, kinetic_line, potential_line

def animate(i):
    # Pendulum position
    theta = trajectory[i, 0]
    x = [0, L*np.sin(theta)]
    y = [0, -L*np.cos(theta)]
    line.set_data(x, y)
    
    # Trace
    trace_x.append(x[1])
    trace_y.append(y[1])
    trace.set_data(trace_x[-50:], trace_y[-50:])  # Last 50 points
    
    # Energy plots
    t_slice = times[:i+1]
    energy_line.set_data(t_slice, energies[:i+1])
    
    # Separate kinetic and potential
    kinetic = 0.5 * m * L**2 * trajectory[:i+1, 1]**2
    potential = m * g * L * (1 - np.cos(trajectory[:i+1, 0]))
    kinetic_line.set_data(t_slice, kinetic)
    potential_line.set_data(t_slice, potential)
    
    return line, trace, energy_line, kinetic_line, potential_line

anim = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=num_steps, interval=20, 
                              blit=True, repeat=True)

# Save as GIF
write_animation(anim, "pendulum_energy_conservation.gif", 
               directory="\diagramsDir/physics",
               writer='pillow', fps=30)}

\newslide{}

\figure{\includediagram{\diagramsDir/physics/pendulum-energy-conservation}{80%}}{Pendulum energy conservation: the pendulum (left) trades potential and kinetic energy while total energy (red line, right) remains constant. Green shows kinetic energy, orange shows potential energy.}{fig-pendulum-energy-conservation}

\notes{This pendulum simulation uses.

1. **Energy formula**: $E = \frac{1}{2}mL^2\omega^2 + mgL(1-\cos\theta)$ (kinetic + potential)

2. **Dynamics from energy**: The equation $\frac{\text{d}\omega}{\text{d}t} = -\frac{g}{L}\sin\theta$ comes from energy conservation structure

3. **Trading energy**: Watch kinetic (green) and potential (orange) trade off while total (red) stays constant

4. **Geometric structure**: The antisymmetric structure we'll study ensures this conservation automatically

The animation shows the pendulum swinging with the energy plot demonstrating perfect conservation (or near-perfect with numerical drift).}

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

\newslide{The Naive Answer}

\notes{The naive answer is: "$\mathbf{v}$ must be perpendicular to $\nabla E$". This is true, but not very useful, the answer depends on the form of $E$.

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

