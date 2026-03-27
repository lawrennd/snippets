\ifndef{pendulumAnimation}
\define{pendulumAnimation}

\editme

\subsection{Pendulum Animation}

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

# Simulate using Störmer-Verlet method (symplectic integrator, preserves energy)
dt = 0.02
t_max = 5.0
num_steps = int(t_max / dt)

# Arrays to store trajectory
times = np.linspace(0, t_max, num_steps)
trajectory = np.zeros((num_steps, 2))
energies = np.zeros(num_steps)

# Integrate using Störmer-Verlet (symplectic, time-reversible)
# Half-step omega, full-step theta, half-step omega — preserves energy to machine precision
theta, omega = initial_state
for i in range(num_steps):
    trajectory[i] = [theta, omega]
    energies[i] = pendulum_energy(theta, omega)
    omega_half = omega - 0.5 * (g/L) * np.sin(theta) * dt
    theta = theta + omega_half * dt
    omega = omega_half - 0.5 * (g/L) * np.sin(theta) * dt

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
write_animation(anim, "pendulum-energy-conservation.gif", 
               directory="\writeDiagramsDir/physics",
               writer='pillow', fps=30)}

\newslide{}

\figure{\includegif{\diagramsDir/physics/pendulum-energy-conservation}{80%}}{Pendulum energy conservation: the pendulum (left) trades potential and kinetic energy while total energy (red line, right) remains constant. Green shows kinetic energy, orange shows potential energy.}{pendulum-energy-conservation}

\notes{This pendulum simulation uses.

1. **Energy formula**: $E = \frac{1}{2}mL^2\omega^2 + mgL(1-\cos\theta)$ (kinetic + potential)

2. **Dynamics from energy**: The equation $\frac{\text{d}\omega}{\text{d}t} = -\frac{g}{L}\sin\theta$ comes from energy conservation structure

3. **Trading energy**: Watch kinetic (green) and potential (orange) trade off while total (red) stays constant

4. **Geometric structure**: The antisymmetric structure we'll study ensures this conservation automatically

5. **Störmer-Verlet integrator**: The simulation uses a symplectic, time-reversible integrator — each step splits the velocity update into two half-steps either side of the position update, preserving the Hamiltonian structure and keeping energy drift at machine precision level.

The animation shows the pendulum swinging with the energy plot demonstrating near-perfect conservation.}

\endif
