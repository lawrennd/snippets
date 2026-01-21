\ifndef{harmonicOscillatorGenericExample}
\define{harmonicOscillatorGenericExample}

\editme

\subsection{Example: Harmonic Oscillator GENERIC Dynamics}

\notes{To see the GENERIC decomposition $M = S + A$ in action, let's analyze a simple physical system: the harmonic oscillator with thermalisation. This demonstrates how reversible (Hamiltonian) and irreversible (dissipative) dynamics emerge from the constraint geometry.}

\slides{
**Harmonic Oscillator with Thermalisation**

* Position $x$ and momentum $p$ variables
* Constraint: $h(X) + h(P) = C$ (entropy conservation)
* Dynamics: $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(\boldsymbol{\theta})a(\boldsymbol{\theta})$
}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import inv
from scipy.integrate import odeint}

\helpercode{def marginal_entropy_gaussian(theta):
    """Compute Shannon entropy for Gaussian with natural parameter theta (precision)"""
    if theta <= 0:
        return np.inf
    sigma_sq = 1.0 / theta  # variance = 1/precision
    return 0.5 * (1 + np.log(2*np.pi*sigma_sq))

def fisher_gaussian_2d(theta_xx, theta_pp, theta_xp):
    """Fisher information matrix for 2D Gaussian in natural parameters"""
    # Convert to covariance matrix
    prec_matrix = np.array([[theta_xx, theta_xp], 
                            [theta_xp, theta_pp]])
    if np.linalg.det(prec_matrix) <= 0:
        return None
    cov_matrix = inv(prec_matrix)
    
    # Fisher information in natural parameter space
    # For exponential family: G_ij = Cov[phi_i, phi_j]
    # For Gaussian: sufficient statistics are [x^2/2, p^2/2, xp]
    sigma_xx, sigma_pp = cov_matrix[0,0], cov_matrix[1,1]
    sigma_xp = cov_matrix[0,1]
    
    G = np.array([
        [sigma_xx**2/2, sigma_xp**2, sigma_xx*sigma_xp],
        [sigma_xp**2, sigma_pp**2/2, sigma_pp*sigma_xp],
        [sigma_xx*sigma_xp, sigma_pp*sigma_xp, (sigma_xx*sigma_pp + sigma_xp**2)]
    ])
    
    return G

def constraint_gradient_gaussian(theta_xx, theta_pp, theta_xp, eps=1e-5):
    """Compute gradient of h(X) + h(P)"""
    h_base = marginal_entropy_gaussian(theta_xx) + marginal_entropy_gaussian(theta_pp)
    
    grad = np.zeros(3)
    # d/d theta_xx
    h_plus = marginal_entropy_gaussian(theta_xx + eps) + marginal_entropy_gaussian(theta_pp)
    grad[0] = (h_plus - h_base) / eps
    
    # d/d theta_pp  
    h_plus = marginal_entropy_gaussian(theta_xx) + marginal_entropy_gaussian(theta_pp + eps)
    grad[1] = (h_plus - h_base) / eps
    
    # d/d theta_xp (correlation doesn't affect marginals)
    grad[2] = 0.0
    
    return grad

def harmonic_dynamics(theta, t, k=1.0, m=1.0, T=1.0):
    """Constrained MEP dynamics for harmonic oscillator"""
    theta_xx, theta_pp, theta_xp = theta
    
    G = fisher_gaussian_2d(theta_xx, theta_pp, theta_xp)
    if G is None:
        return np.zeros(3)
    
    a = constraint_gradient_gaussian(theta_xx, theta_pp, theta_xp)
    
    # Tangency condition: a^T G theta + a^T G a nu = 0
    numerator = a @ (G @ theta)
    denominator = a @ (G @ a)
    
    if abs(denominator) < 1e-10:
        nu = 0.0
    else:
        nu = -numerator / denominator
    
    # Dynamics
    dtheta = -(G @ theta) - nu * a
    
    return dtheta}

\notes{Starting from an out-of-equilibrium state (cold $x$, hot $p$), the system evolves toward thermal equilibrium while maintaining the entropy constraint.}

\code{# Physical parameters
k = 1.0      # Spring constant
m = 1.0      # Mass
T = 1.0      # Temperature
beta = 1.0 / T

# Equilibrium values
theta_xx_eq = beta * k
theta_pp_eq = beta / m
theta_xp_eq = 0.0

print(f"Equilibrium: θ_xx = {theta_xx_eq:.3f}, θ_pp = {theta_pp_eq:.3f}, θ_xp = 0")

# Initial condition: OUT of equilibrium (cold x, hot p)
theta_init = np.array([2.0 * theta_xx_eq,  # Cold x (small variance)
                       0.5 * theta_pp_eq,  # Hot p (large variance)  
                       0.0])               # No correlation

print(f"Initial:     θ_xx = {theta_init[0]:.3f}, θ_pp = {theta_init[1]:.3f}, θ_xp = 0")

# Simulate
t_span = np.linspace(0, 10, 200)
theta_trajectory = odeint(harmonic_dynamics, theta_init, t_span)

# Compute entropy conservation
h_x = np.array([marginal_entropy_gaussian(th) for th in theta_trajectory[:, 0]])
h_p = np.array([marginal_entropy_gaussian(th) for th in theta_trajectory[:, 1]])
h_total = h_x + h_p

print(f"\nEntropy conservation check:")
print(f"  Initial h(X) + h(P) = {h_total[0]:.6f}")
print(f"  Final   h(X) + h(P) = {h_total[-1]:.6f}")
print(f"  Variation: {np.std(h_total):.2e}")}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top left: Trajectory in parameter space
ax = axes[0, 0]
ax.plot(theta_trajectory[:, 0], theta_trajectory[:, 1], 'b-', linewidth=2, alpha=0.7)
ax.plot(theta_init[0], theta_init[1], 'go', markersize=10, label='Initial')
ax.plot(theta_xx_eq, theta_pp_eq, 'r*', markersize=15, label='Equilibrium')
ax.set_xlabel(r'$\theta_{xx}$ (x precision)', fontsize=14)
ax.set_ylabel(r'$\theta_{pp}$ (p precision)', fontsize=14)
ax.set_title('Trajectory in Parameter Space', fontsize=16)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)

# Top right: Entropy conservation
ax = axes[0, 1]
ax.plot(t_span, h_total, 'k-', linewidth=2, label='$h(X) + h(P)$')
ax.axhline(y=h_total[0], color='r', linestyle='--', alpha=0.5, label='Initial value')
ax.set_xlabel('Time', fontsize=14)
ax.set_ylabel('Total Entropy', fontsize=14)
ax.set_title('Constraint Maintenance', fontsize=16)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)

# Bottom left: Individual entropies
ax = axes[1, 0]
ax.plot(t_span, h_x, 'b-', linewidth=2, label='$h(X)$ (position)')
ax.plot(t_span, h_p, 'r-', linewidth=2, label='$h(P)$ (momentum)')
ax.set_xlabel('Time', fontsize=14)
ax.set_ylabel('Marginal Entropy', fontsize=14)
ax.set_title('Entropy Exchange', fontsize=16)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)

# Bottom right: Variances (physical space)
sigma_xx = 1.0 / theta_trajectory[:, 0]
sigma_pp = 1.0 / theta_trajectory[:, 1]
ax = axes[1, 1]
ax.plot(t_span, sigma_xx, 'b-', linewidth=2, label=r'$\sigma_x^2$')
ax.plot(t_span, sigma_pp, 'r-', linewidth=2, label=r'$\sigma_p^2$')
ax.axhline(y=1.0/theta_xx_eq, color='b', linestyle='--', alpha=0.5)
ax.axhline(y=1.0/theta_pp_eq, color='r', linestyle='--', alpha=0.5)
ax.set_xlabel('Time', fontsize=14)
ax.set_ylabel('Variance', fontsize=14)
ax.set_title('Approach to Equipartition', fontsize=16)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()

mlai.write_figure('harmonic-oscillator-generic-dynamics.svg', 
                  directory='\writeDiagramsDir/information-game')}

\figure{\includediagram{\diagramsDir/information-game/harmonic-oscillator-generic-dynamics}{80%}}{Harmonic oscillator GENERIC dynamics. Top left: Trajectory in parameter space from out-of-equilibrium initial state toward thermal equilibrium. Top right: Total entropy $h(X) + h(P)$ conserved throughout evolution. Bottom left: Individual marginal entropies exchange while maintaining sum. Bottom right: Variances approach equipartition theorem values (both equal to 1.0 at equilibrium).}{harmonic-oscillator-generic-dynamics}

\notes{This demonstrates the GENERIC structure.

- **Symmetric part $S$**: Drives system toward equilibrium (equipartition)
- **Antisymmetric part $A$**: Would create oscillations (suppressed here by strong damping)
- **Constraint**: Maintained exactly throughout evolution via Lagrange multiplier $\nu$

The system exhibits thermalisation—energy flows from the "hot" momentum degree of freedom to the "cold" position degree of freedom until equipartition is reached.}

\slides{
**Key Features:**

* Entropy conservation: $h(X) + h(P) = C$ maintained
* Thermalisation: Cold → hot exchange until equilibrium
* GENERIC decomposition: $M = S + A$
* Equilibrium: Equipartition theorem satisfied
}
\endif
