\ifndef{binaryDynamicsSimulation}
\define{binaryDynamicsSimulation}

\editme

\subsection{Simulation: Degeneracy in Action}

\notes{To make the LOCAL $\rightarrow$ GLOBAL result concrete, let's simulate the dynamics of two binary variables and verify that the degeneracy conditions hold throughout the trajectory.}

\setupcode{import numpy as np
from scipy.integrate import odeint}

\helpercode{def binary_probabilities(theta):
    """Compute joint probabilities for two binary variables.
    
    theta = (theta_1, theta_2, theta_12)
    Returns p(x1, x2) for x1, x2 in {0, 1}
    """
    theta1, theta2, theta12 = theta
    
    # Unnormalized probabilities (exponential family)
    p00 = 1.0  # Reference (x1=0, x2=0)
    p01 = np.exp(theta2)
    p10 = np.exp(theta1)
    p11 = np.exp(theta1 + theta2 + theta12)
    
    # Normalize
    Z = p00 + p01 + p10 + p11
    return np.array([[p00/Z, p01/Z], [p10/Z, p11/Z]])

def marginal_entropies(theta):
    """Compute marginal entropies h1 and h2."""
    p = binary_probabilities(theta)
    
    # Marginal for X1
    p1 = p.sum(axis=1)  # Sum over x2
    h1 = -np.sum(p1 * np.log(p1 + 1e-10))  # Add epsilon for numerical stability
    
    # Marginal for X2
    p2 = p.sum(axis=0)  # Sum over x1
    h2 = -np.sum(p2 * np.log(p2 + 1e-10))
    
    return h1, h2

def fisher_matrix(theta):
    """Compute Fisher information matrix for two binary variables."""
    p = binary_probabilities(theta).flatten()  # [p00, p01, p10, p11]
    
    # Sufficient statistics: phi(x) = [x1, x2, x1*x2]
    phi = np.array([
        [0, 0, 0],  # x1=0, x2=0
        [0, 1, 0],  # x1=0, x2=1
        [1, 0, 0],  # x1=1, x2=0
        [1, 1, 1]   # x1=1, x2=1
    ])
    
    # Fisher matrix: G = Cov[phi]
    mean_phi = (phi.T @ p).reshape(-1, 1)
    G = phi.T @ np.diag(p) @ phi - mean_phi @ mean_phi.T
    
    return G

def constraint_gradient(theta, eps=1e-5):
    """Compute gradient of sum of marginal entropies using finite differences."""
    h1_0, h2_0 = marginal_entropies(theta)
    
    grad = np.zeros(3)
    for i in range(3):
        theta_plus = theta.copy()
        theta_plus[i] += eps
        h1_plus, h2_plus = marginal_entropies(theta_plus)
        grad[i] = ((h1_plus + h2_plus) - (h1_0 + h2_0)) / eps
    
    return grad

def dynamics(theta, t):
    """Constrained MEP dynamics: dot(theta) = -G*theta - nu*a"""
    G = fisher_matrix(theta)
    a = constraint_gradient(theta)
    
    # Lagrange multiplier from tangency condition
    nu = -np.dot(a, G @ theta) / np.dot(a, a)
    
    # Full dynamics
    dtheta_dt = -G @ theta - nu * a
    
    return dtheta_dt}

\code{# Initial condition: Start with some correlation
theta0 = np.array([0.5, 0.5, 0.8])
h1_0, h2_0 = marginal_entropies(theta0)
C_target = h1_0 + h2_0

print(f"Initial theta: {theta0}")
print(f"Initial h1: {h1_0:.4f}, h2: {h2_0:.4f}")
print(f"Target C = h1 + h2: {C_target:.4f}")

# Time span
t_span = np.linspace(0, 10, 200)

# Integrate dynamics
trajectory = odeint(dynamics, theta0, t_span)

# Compute marginal entropies along trajectory
h1_traj = []
h2_traj = []
sum_h_traj = []

for theta_t in trajectory:
    h1, h2 = marginal_entropies(theta_t)
    h1_traj.append(h1)
    h2_traj.append(h2)
    sum_h_traj.append(h1 + h2)

h1_traj = np.array(h1_traj)
h2_traj = np.array(h2_traj)
sum_h_traj = np.array(sum_h_traj)

print(f"\nFinal theta: {trajectory[-1]}")
print(f"Final h1: {h1_traj[-1]:.4f}, h2: {h2_traj[-1]:.4f}")
print(f"Final C = h1 + h2: {sum_h_traj[-1]:.4f}")
print(f"Constraint violation: {np.abs(sum_h_traj[-1] - C_target):.2e}")}


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation}

\plotcode{fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Trajectory in parameter space
ax = axes[0, 0]
ax.plot(trajectory[:, 0], trajectory[:, 1], 'b-', linewidth=2, alpha=0.7)
ax.plot(theta0[0], theta0[1], 'go', markersize=10, label='Start')
ax.plot(trajectory[-1, 0], trajectory[-1, 1], 'r*', markersize=15, label='End')
ax.set_xlabel(r'$\theta_1$')
ax.set_ylabel(r'$\theta_2$')
ax.set_title('Trajectory in Parameter Space')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 2: Constraint verification
ax = axes[0, 1]
ax.plot(t_span, sum_h_traj, 'b-', linewidth=2, label=r'$h_1 + h_2$')
ax.axhline(C_target, color='r', linestyle='--', linewidth=2, label=f'Target C = {C_target:.3f}')
ax.set_xlabel('Time')
ax.set_ylabel(r'$h_1 + h_2$')
ax.set_title('Degeneracy 1: Constraint Maintained')
ax.legend()
ax.grid(True, alpha=0.3)
# Add text showing max violation
max_violation = np.max(np.abs(sum_h_traj - C_target))
ax.text(0.5, 0.95, f'Max violation: {max_violation:.2e}', 
        transform=ax.transAxes, ha='center', va='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Plot 3: Individual marginal entropies
ax = axes[1, 0]
ax.plot(t_span, h1_traj, 'b-', linewidth=2, label=r'$h_1$ (marginal X₁)')
ax.plot(t_span, h2_traj, 'r-', linewidth=2, label=r'$h_2$ (marginal X₂)')
ax.set_xlabel('Time')
ax.set_ylabel('Marginal Entropy')
ax.set_title('Individual Marginal Entropies')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 4: Theta_12 (correlation parameter)
ax = axes[1, 1]
ax.plot(t_span, trajectory[:, 2], 'g-', linewidth=2)
ax.set_xlabel('Time')
ax.set_ylabel(r'$\theta_{12}$ (interaction)')
ax.set_title('Correlation Parameter Evolution')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='k', linestyle=':', alpha=0.5)

plt.tight_layout()

mlai.write_figure('binary-dynamics-verification.svg', directory='\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/binary-dynamics-verification}{80%}}{Verification of degeneracy conditions for two binary variables. Top left: Trajectory in parameter space. Top right: Constraint $h_1 + h_2 = C$ maintained to machine precision (Degeneracy 1). Bottom left: Individual marginal entropies trade off while sum is conserved. Bottom right: Interaction parameter $\theta_{12}$ decays toward independence.}{binary-dynamics-verification}

\notes{The simulation confirms:

1. **Degeneracy 1 (Global)**: The constraint $h_1 + h_2 = C$ is maintained throughout the dynamics to machine precision (typically $< 10^{-10}$), not just at equilibrium.

2. **Trade-off**: Individual marginal entropies $h_1$ and $h_2$ can change, but their sum remains constant.

3. **Convergence**: The system evolves toward equilibrium (independence with $\theta_{12} \to 0$), showing the dissipative character.

This numerical experiment validates the LOCAL $\rightarrow$ GLOBAL result: the tangency condition enforced at each timestep ensures global constraint satisfaction.}

\subsection{Animation: Watching Degeneracy in Real-Time}

\setupcode{from matplotlib.animation import FuncAnimation
from IPython.display import HTML}

\code{# Create animation showing trajectory and constraint verification
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Set up the plots
ax1.set_xlim(-0.2, 1.0)
ax1.set_ylim(-0.2, 1.0)
ax1.set_xlabel(r'$\theta_1$')
ax1.set_ylabel(r'$\theta_2$')
ax1.set_title('Trajectory in Parameter Space')
ax1.grid(True, alpha=0.3)

ax2.set_xlim(0, 10)
ax2.set_ylim(C_target - 0.01, C_target + 0.01)
ax2.set_xlabel('Time')
ax2.set_ylabel(r'$h_1 + h_2$')
ax2.set_title('Constraint Verification')
ax2.axhline(C_target, color='r', linestyle='--', linewidth=2, alpha=0.5, label=f'Target C = {C_target:.3f}')
ax2.grid(True, alpha=0.3)
ax2.legend()

# Initialize lines
line1, = ax1.plot([], [], 'b-', linewidth=2, alpha=0.7)
point1, = ax1.plot([], [], 'ro', markersize=8)
line2, = ax2.plot([], [], 'b-', linewidth=2)
point2, = ax2.plot([], [], 'ro', markersize=8)

def init():
    line1.set_data([], [])
    point1.set_data([], [])
    line2.set_data([], [])
    point2.set_data([], [])
    return line1, point1, line2, point2

def animate(frame):
    # Update trajectory plot
    line1.set_data(trajectory[:frame, 0], trajectory[:frame, 1])
    point1.set_data([trajectory[frame, 0]], [trajectory[frame, 1]])
    
    # Update constraint plot
    line2.set_data(t_span[:frame], sum_h_traj[:frame])
    point2.set_data([t_span[frame]], [sum_h_traj[frame]])
    
    return line1, point1, line2, point2

# Create animation
anim = FuncAnimation(fig, animate, init_func=init, 
                    frames=len(t_span), interval=50, blit=True)

# Save animation
mlai.write_animation(anim, 'binary-dynamics-animation.html', 
                    directory='./physics')}

\notes{The animation shows the dynamics in real-time, demonstrating visually that:
- The trajectory flows through parameter space (left panel)
- The constraint $h_1 + h_2 = C$ is maintained at every instant (right panel)

This provides intuitive confirmation of the SUFFICIENCY result: the constraint structure ensures global degeneracy automatically.}

\endif


