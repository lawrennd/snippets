\ifndef{genericDecompositionExample}
\define{genericDecompositionExample}

\editme

\subsection{Computational Example: Binary Variables Decomposition}

\notes{Let's make the GENERIC decomposition concrete by computing it explicitly for the two binary variables example from Lecture 6.

We'll analyse the local flow structure at a point on the constraint manifold: $\boldsymbol{\theta} = (0.3, -0.2, 0.1)$. This is *not* an equilibrium point (the dynamics $\dot{\boldsymbol{\theta}} \neq 0$ here), which makes it more representative of general flow behavior.

At this point, we:

1. Compute the Fisher information matrix $G(\boldsymbol{\theta})$
2. Compute the constraint gradient $a(\boldsymbol{\theta}) = \nabla(h_1 + h_2)$
3. Determine the Lagrange multiplier $\nu$ from the tangency condition
4. Compute the linearisation matrix $M = \partial F/\partial \boldsymbol{\theta}$ where $F(\boldsymbol{\theta}) = -G\boldsymbol{\theta} - \nu a$
5. Decompose $M = S + A$ to reveal the GENERIC structure

This analysis reveals how information flows through this region of parameter space.}

\slides{
**Computational Example**

Analyze at $\boldsymbol{\theta} = (0.3, -0.2, 0.1)$

Steps:
1. Compute $G(\boldsymbol{\theta})$, $a(\boldsymbol{\theta})$
2. Find $\nu$ from tangency
3. Linearize: $M = \partial F/\partial \boldsymbol{\theta}$
4. Decompose: $M = S + A$

Reveals local flow structure
}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm}

\code{# Define helper functions for computing system properties
def compute_marginals_binary(theta1, theta2, theta12):
    """Compute marginal probabilities for 2D binary exponential family"""
    logits = np.array([0, theta1, theta2, theta1 + theta2 + theta12])
    log_Z = np.logaddexp.reduce(logits)
    probs = np.exp(logits - log_Z)
    p1 = np.array([probs[0] + probs[2], probs[1] + probs[3]])
    p2 = np.array([probs[0] + probs[1], probs[2] + probs[3]])
    return p1, p2, probs

def compute_fisher_binary(theta1, theta2, theta12):
    """Compute Fisher information matrix"""
    _, _, probs = compute_marginals_binary(theta1, theta2, theta12)
    phi_vals = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 1]])
    mean_phi = probs @ phi_vals
    cov_matrix = sum(p * np.outer(phi, phi) for p, phi in zip(probs, phi_vals))
    return cov_matrix - np.outer(mean_phi, mean_phi)

def marginal_entropy(p):
    """Compute Shannon entropy"""
    p_clean = p[p > 1e-10]
    return -np.sum(p_clean * np.log(p_clean))

def compute_constraint_gradient(theta1, theta2, theta12, eps=1e-5):
    """Numerically compute ∇(h₁ + h₂)"""
    p1, p2, _ = compute_marginals_binary(theta1, theta2, theta12)
    h_base = marginal_entropy(p1) + marginal_entropy(p2)
    grad = np.zeros(3)
    for i, delta in enumerate([np.array([eps,0,0]), np.array([0,eps,0]), np.array([0,0,eps])]):
        p1_p, p2_p, _ = compute_marginals_binary(
            theta1 + delta[0], theta2 + delta[1], theta12 + delta[2])
        h_plus = marginal_entropy(p1_p) + marginal_entropy(p2_p)
        grad[i] = (h_plus - h_base) / eps
    return grad

# Analyze at a typical (non-equilibrium) point
theta = np.array([0.3, -0.2, 0.1])

print(f"Analyzing at θ = {theta}\n")

# Compute system properties at this point
G = compute_fisher_binary(theta[0], theta[1], theta[2])
a = compute_constraint_gradient(theta[0], theta[1], theta[2])

# Compute Lagrange multiplier from tangency condition
F_unconstrained = -G @ theta
nu = -np.dot(F_unconstrained, a) / np.dot(a, a)

# Dynamics at this point
F = F_unconstrained - nu * a

print(f"ν = {nu:.4f}")
print(f"||F(θ)|| = {np.linalg.norm(F):.4f} (non-zero, not equilibrium)\n")

# Compute linearization M = ∂F/∂θ numerically
eps_diff = 1e-5
M = np.zeros((3, 3))
for i in range(3):
    theta_plus = theta.copy()
    theta_plus[i] += eps_diff
    G_plus = compute_fisher_binary(theta_plus[0], theta_plus[1], theta_plus[2])
    a_plus = compute_constraint_gradient(theta_plus[0], theta_plus[1], theta_plus[2])
    F_unc_plus = -G_plus @ theta_plus
    nu_plus = -np.dot(F_unc_plus, a_plus) / np.dot(a_plus, a_plus)
    F_plus = F_unc_plus - nu_plus * a_plus
    M[:, i] = (F_plus - F) / eps_diff

print("Linearization matrix M = ∂F/∂θ:")
print(M)
print(f"\nM is {'symmetric' if np.allclose(M, M.T) else 'NOT symmetric'}")
}

\notes{Now decompose $M$ into symmetric and antisymmetric parts:
$$
S = \frac{1}{2}(M + M^\top), \quad A = \frac{1}{2}(M - M^\top)
$$
}

\code{# Symmetric and antisymmetric decomposition
S = (M + M.T) / 2
A = (M - M.T) / 2

print("\nSymmetric part S:")
print(S)
print(f"\nFrobenius norm ||S||_F = {np.linalg.norm(S, 'fro'):.4f}")

print("\nAntisymmetric part A:")
print(A)
print(f"Frobenius norm ||A||_F = {np.linalg.norm(A, 'fro'):.4f}")

# Verify decomposition
print(f"\nVerify S + A = M: {np.allclose(S + A, M)}")
print(f"Verify S^T = S: {np.allclose(S, S.T)}")
print(f"Verify A^T = -A: {np.allclose(A, -A.T)}")
}

\subsection{Eigenvalue Analysis}

\notes{Now let's examine the eigenvalues of each part to see the dissipative vs conservative structure.}

\code{# Compute eigenvalues
eigs_M = np.linalg.eigvals(M)
eigs_S = np.linalg.eigvals(S)
eigs_A = np.linalg.eigvals(A)

print("Eigenvalues of M (full system):")
for i, lam in enumerate(eigs_M):
    print(f"  λ_{i+1} = {lam.real:.4f} + {lam.imag:.4f}i")

print("\nEigenvalues of S (symmetric part):")
for i, lam in enumerate(eigs_S):
    print(f"  λ_{i+1} = {lam.real:.4f} (real)")
    
print("\nEigenvalues of A (antisymmetric part):")
for i, lam in enumerate(eigs_A):
    print(f"  λ_{i+1} = {lam.real:.4f} + {lam.imag:.4f}i")
}

\notes{**Observations:**

1. **$S$ has real eigenvalues** (as expected for symmetric matrices). All three eigenvalues are negative (~-0.03, ~-0.44, ~-0.85), indicating that in the absence of the antisymmetric part, trajectories would converge toward this point. This describes the local dissipative structure.

2. **$A$ has purely imaginary eigenvalues** (as expected for antisymmetric matrices). The imaginary parts (~±0.012i) give the local oscillatory/rotational frequency. The antisymmetric part is relatively small ($\|A\|/\|S\| \approx 0.017$) at this point.

3. **$M$ combines both**: real parts from $S$ (growth/decay), imaginary parts from $A$ (oscillation/rotation). Together they describe how perturbations evolve in this neighborhood of parameter space.

The small ratio $\|A\|/\|S\|$ indicates that at this point, dissipative effects strongly dominate over rotational ones. This is typical for regions where the system is close to Gaussian behavior. At other points on the manifold (especially with tighter constraints or stronger correlations), the antisymmetric part can become more prominent.}

\subsection{Where Does the Antisymmetric Part Come From?}

\notes{To understand the origin of the antisymmetric component, let's compare the constrained and unconstrained dynamics.}

\code{# Compare: Unconstrained vs Constrained
print("Constrained vs Unconstrained Comparison:")
print("=" * 50)

# Unconstrained dynamics: dθ/dt = -Gθ (no constraint)
M_unconstrained = -G

print("\nUnconstrained: dθ/dt = -Gθ")
print("  Jacobian M = -G (Fisher matrix only)")

S_unc = (M_unconstrained + M_unconstrained.T) / 2
A_unc = (M_unconstrained - M_unconstrained.T) / 2

print(f"  ||S|| = {np.linalg.norm(S_unc, 'fro'):.4f}")
print(f"  ||A|| = {np.linalg.norm(A_unc, 'fro'):.4f}")
print(f"  Is M symmetric? {np.allclose(M_unconstrained, M_unconstrained.T)}")

print("\nConstrained: dθ/dt = -Gθ - νa (with h₁+h₂=C)")
print("  Jacobian includes constraint terms")
print(f"  ||S|| = {np.linalg.norm(S, 'fro'):.4f}")
print(f"  ||A|| = {np.linalg.norm(A, 'fro'):.4f}")
print(f"  Is M symmetric? {np.allclose(M, M.T)}")

print("\n" + "=" * 50)
print("Conclusion: A emerges from constraint geometry!")
}

\notes{**Key insight:** Without constraints, the dynamics $\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta}$ have a **symmetric** Jacobian $M = -G$. There is no antisymmetric part ($A = 0$), only pure dissipation toward maximum entropy.

With the marginal entropy constraint $h_1 + h_2 = C$, the dynamics become $\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta} - \nu a$. The Lagrange multiplier $\nu$ varies with position (to enforce tangency), and the constraint gradient $a$ varies with position (constraint surface curvature). These create additional terms in the Jacobian:
$$
M = \frac{\partial F}{\partial \boldsymbol{\theta}} = -G + \text{(constraint terms)}
$$

The constraint terms break the symmetry, introducing an antisymmetric component $A \neq 0$. This is the **geometric origin** of conservative dynamics: the constraint surface curves through parameter space, creating geometric phases (Berry-like effects) that manifest as rotation/oscillation.

**Physical interpretation:** As trajectories move along the curved constraint manifold, they experience geometric "twisting" from the constraint geometry. This is analogous to parallel transport on a curved surface—even if you move in what feels like a "straight line" locally, the curvature causes rotation. This geometric effect is precisely what the antisymmetric part $A$ captures.}

\slides{
**Origin of Antisymmetric Part**

Unconstrained: $\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta}$
* $M = -G$ (symmetric)
* $A = 0$ (no rotation)

Constrained: $\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta} - \nu a$
* Constraint terms break symmetry
* $A \neq 0$ (rotation emerges!)

**Constraint geometry creates conservative dynamics**
}

\subsubsection{Visualizing Unconstrained vs Constrained Flow}

\notes{Let's visualize the difference between unconstrained and constrained dynamics to see how the constraint creates rotational flow.}

\plotcode{# Compare unconstrained vs constrained trajectories
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Time span and initial conditions
t_span = np.linspace(0, 5, 100)
initial_points = [
    np.array([0.3, -0.2, 0.1]),
    np.array([0.2, 0.1, -0.05]),
    np.array([-0.1, 0.2, 0.05]),
]

# Left: Unconstrained dynamics (pure -Gθ)
ax = axes[0]
ax.set_title('Unconstrained: dθ/dt = -Gθ')
ax.set_xlabel('θ₁')
ax.set_ylabel('θ₂')

for theta0 in initial_points:
    # Unconstrained flow
    trajectory = np.array([expm(M_unconstrained * t) @ theta0 for t in t_span])
    ax.plot(trajectory[:, 0], trajectory[:, 1], 'b-', alpha=0.6, linewidth=2)
    ax.plot(theta0[0], theta0[1], 'ro', markersize=6)

ax.plot(0, 0, 'k*', markersize=12, label='θ=0 (max entropy)')
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_aspect('equal', adjustable='box')

# Right: Constrained dynamics (with constraint forcing)
ax = axes[1]
ax.set_title('Constrained: dθ/dt = -Gθ - νa')
ax.set_xlabel('θ₁')
ax.set_ylabel('θ₂')

for theta0 in initial_points:
    # Constrained flow (using M from earlier computation)
    trajectory = np.array([expm(M * t) @ theta0 for t in t_span])
    ax.plot(trajectory[:, 0], trajectory[:, 1], 'g-', alpha=0.6, linewidth=2)
    ax.plot(theta0[0], theta0[1], 'ro', markersize=6)

ax.plot(0, 0, 'k*', markersize=12, label='θ=0')
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_aspect('equal', adjustable='box')

plt.tight_layout()
mlai.write_figure('unconstrained-vs-constrained-flow.svg', 
                  directory='\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/unconstrained-vs-constrained-flow}{80%}}{Comparison of unconstrained vs constrained dynamics. Left: Without constraints, flow is purely radial toward θ=0 (symmetric $M=-G$, no antisymmetric part). Right: With constraint $h_1+h_2=C$, flow includes rotational component from constraint geometry (antisymmetric part $A \neq 0$).}{unconstrained-vs-constrained-flow}

\notes{**Observations:**

**Unconstrained (left):** Trajectories flow radially toward θ=0, following pure gradient descent on entropy. The dynamics are symmetric—no rotation, just convergence. This is pure dissipation.

**Constrained (right):** Trajectories flow along the constraint surface with a tangential component. The constraint forces the flow to bend, creating rotational motion. This geometric bending is what creates the antisymmetric part $A$.

The difference between these two panels is precisely the effect of constraint geometry. The antisymmetric part doesn't exist in unconstrained dynamics—it emerges from the requirement to stay on the curved constraint manifold.}

\slides{
**Unconstrained vs Constrained Flow**

\includediagram{\diagramsDir/physics/unconstrained-vs-constrained-flow}{70%}

* Left: Pure radial flow (A = 0)
* Right: Flow with rotation (A ≠ 0)
* Constraint geometry creates antisymmetric component!
}

\subsection{Phase Space Trajectories}

\notes{Let's visualize how trajectories evolve under the three different dynamics to see the difference between dissipative, conservative, and combined flow.}

\setupplotcode{import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch}

\plotcode{# Create figure with three subplots
fig, axes = plt.subplots(1, 3, figsize=(14, 4))

# Time evolution (extended to show rotation from A)
t_span = np.linspace(0, 30, 200)

# Initial conditions (small perturbations)
q0_list = [
    np.array([0.1, 0.0, 0.0]),
    np.array([0.0, 0.1, 0.0]),
    np.array([0.05, 0.05, 0.0])
]

colors = ['blue', 'red', 'green']
dynamics = [
    ("Pure dissipation (S only)", S),
    ("Pure rotation (A only)", A),
    ("Combined (M = S + A)", M)
]

for ax, (title, matrix) in zip(axes, dynamics):
    ax.set_title(title)
    ax.set_xlabel(r'$q_1$')
    ax.set_ylabel(r'$q_2$')
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='k', linewidth=0.5)
    ax.axvline(0, color='k', linewidth=0.5)
    
    # Plot trajectories for each initial condition
    for q0, color in zip(q0_list, colors):
        trajectory = np.array([expm(matrix * t) @ q0 for t in t_span])
        
        # Plot trajectory
        ax.plot(trajectory[:, 0], trajectory[:, 1], 
                color=color, alpha=0.6, linewidth=1.5)
        
        # Mark start point
        ax.plot(q0[0], q0[1], 'o', color=color, markersize=6)
        
        # Arrow showing direction
        if len(trajectory) > 10:
            mid = len(trajectory) // 2
            dx = trajectory[mid+5, 0] - trajectory[mid, 0]
            dy = trajectory[mid+5, 1] - trajectory[mid, 1]
            ax.arrow(trajectory[mid, 0], trajectory[mid, 1], 
                    dx*0.8, dy*0.8,
                    head_width=0.01, head_length=0.01, 
                    fc=color, ec=color, alpha=0.6)
    
    ax.set_aspect('equal', adjustable='box')

plt.tight_layout()
mlai.write_figure('generic-decomposition-trajectories.svg', 
                  directory='\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/generic-decomposition-trajectories}{80%}}{Phase space trajectories showing: (left) pure dissipation from $S$ - all trajectories decay to origin; (center) pure rotation from $A$ - trajectories circulate without decay; (right) combined dynamics from $M = S+A$ - heavily damped rotation toward equilibrium.}{generic-decomposition-trajectories}

\notes{**Key insights from the visualisation:**

Note: The trajectories are shown over an extended time ($t \in [0, 30]$) to make the rotation from $A$ clearly visible. The oscillation period is approximately $2\pi/0.012 \approx 524$ time units, so we see only a small fraction of a full cycle.

1. **Pure $S$ dynamics (left)**: Trajectories decay toward the origin. This is pure dissipation—the symmetric part drives convergence. All eigenvalues of $S$ are real and negative at this point.

2. **Pure $A$ dynamics (centre)**: Trajectories circulate with conserved norm $\|q\|$. This is conservative dynamics—pure rotation with no dissipation. Eigenvalues of $A$ are purely imaginary.

3. **Combined $M = S + A$ dynamics (right)**: Trajectories spiral inward, combining decay (from $S$) with rotation (from $A$). This is the GENERIC structure: dissipation + conservation working together.

**Why is the antisymmetric effect weak here?** At this point in parameter space, $\|A\|/\|S\| \approx 0.017$. The system is in a regime where dissipative behavior strongly dominates. The antisymmetric part emerges from third-order corrections (third cumulants and constraint geometry). At other points—especially with tighter constraints or stronger correlations—the antisymmetric part becomes more prominent.}

\slides{**Phase Space Behavior**

\includediagram{\diagramsDir/physics/generic-decomposition-trajectories}{70%}

* Left: $S$ only $\rightarrow$ pure decay
* Center: $A$ only $\rightarrow$ pure rotation
* Right: $M = S+A$ $\rightarrow$ damped spiral

**GENERIC = Dissipation + Conservation**
}

\subsection{Energy Analysis}

\notes{Let's also look at how a simple "energy-like" quantity $E(q) = \frac{1}{2}q^\top q$ (just the squared norm) evolves under each dynamics.}

\code{# Compute energy evolution for one trajectory
q0 = np.array([0.1, 0.08, 0.0])
t_span = np.linspace(0, 30, 200)

energies = {}
for name, matrix in [("S", S), ("A", A), ("M", M)]:
    traj = np.array([expm(matrix * t) @ q0 for t in t_span])
    energies[name] = 0.5 * np.sum(traj**2, axis=1)
}

\plotcode{fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(t_span, energies["S"], label='S only (dissipation)', 
        linewidth=2, color='blue')
ax.plot(t_span, energies["A"], label='A only (rotation)', 
        linewidth=2, color='red', linestyle='--')
ax.plot(t_span, energies["M"], label='M = S + A (combined)', 
        linewidth=2, color='green')

ax.set_xlabel('Time t')
ax.set_ylabel(r'Energy $E(q) = \frac{1}{2}||q||^2$')
ax.set_title('Energy Evolution Under Different Dynamics')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_ylim([0, None])

mlai.write_figure('generic-energy-evolution.svg', 
                  directory='\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/generic-energy-evolution}{70%}}{Energy evolution showing: (blue) pure $S$ dynamics monotonically decrease energy; (red dashed) pure $A$ dynamics conserve energy; (green) combined $M$ dynamics show damped oscillations with overall energy decrease.}{generic-energy-evolution}

\notes{The energy plot clearly shows:
- **Pure $S$**: Monotonic decay to zero (pure dissipation)
- **Pure $A$**: Constant energy (pure conservation)
- **Combined $M$**: Oscillations with overall decay (dissipation + conservation)

This is exactly the GENERIC structure: the symmetric part drives irreversible energy dissipation, while the antisymmetric part creates reversible oscillations.}

\notes{**Summary:** This computational example demonstrates that the GENERIC decomposition $M = S + A$ isn't just abstract mathematics, it reveals the local structure of dynamical flow in parameter space. The symmetric part $S$ controls growth/decay directions, while the antisymmetric part $A$ controls rotation and oscillation. Together they describe how perturbations evolve in the neighborhood of the analysis point.

The linearization $M = \partial F/\partial \boldsymbol{\theta}$ varies across the parameter manifold (both $G(\boldsymbol{\theta})$ and $a(\boldsymbol{\theta})$ depend on position), making the GENERIC decomposition truly local. However, the insight holds everywhere: information dynamics naturally decompose into dissipative (thermodynamic) and conservative (mechanical) components, with the balance between them varying across the manifold depending on local geometry and constraint tightness.}

\endif


