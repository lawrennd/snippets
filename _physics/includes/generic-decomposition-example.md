\ifndef{genericDecompositionExample}
\define{genericDecompositionExample}

\editme

\subsection{Computational Example: Binary Variables Decomposition}

\notes{Let's make the GENERIC decomposition concrete by computing it explicitly for the two binary variables example from Lecture 6.

**Recall the setup:** At equilibrium $\boldsymbol{\theta}^\ast = (0, 0, 0)$ (uniform distribution), we computed the Fisher information matrix
$$
G = \begin{pmatrix}
1/4 & 0 & 1/8 \\
0 & 1/4 & 1/8 \\
1/8 & 1/8 & 3/16
\end{pmatrix}.
$$
For this maximum entropy equilibrium, $\nu^\ast = 0$ and the constraint gradient is $a = (a_1, a_1, 0)$ where $a_1 < 0$ (since increasing $\theta_i$ decreases entropy from maximum).

The linearisation matrix is
$$
M = -G + \frac{aa^\top G}{\|a\|^2}
$$
Let's compute this and decompose it into $S + A$ parts.}

\slides{
**Computational Example**

Binary variables at equilibrium:
$$
G = \begin{pmatrix}
1/4 & 0 & 1/8 \\
0 & 1/4 & 1/8 \\
1/8 & 1/8 & 3/16
\end{pmatrix}
$$

Compute: $M = -G + \frac{aa^\top G}{\|a\|^2}$

Decompose: $M = S + A$
}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm}

\code{# Fisher information at equilibrium
G = np.array([
    [1/4, 0, 1/8],
    [0, 1/4, 1/8],
    [1/8, 1/8, 3/16]
])

# Constraint gradient (approximate for uniform marginals)
# Increasing theta_i decreases entropy from max, so a_1 < 0
a = np.array([-0.25, -0.25, 0.0])

# Linearization matrix M
# For maximum entropy equilibrium: nu* = 0
# M = -G + (a a^T G) / ||a||^2
M = -G + np.outer(a, a @ G) / (a @ a)

print("Linearization matrix M:")
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

1. *$S$ has real eigenvalues* (as expected for symmetric matrices)
2. *$A$ has purely imaginary eigenvalues* (as expected for antisymmetric matrices)
3. *$M$ combines both*: real parts from $S$ (dissipation), imaginary parts from $A$ (oscillation)

At this maximum entropy equilibrium, the antisymmetric part is relatively small (the system is nearly Gaussian), so the dynamics are dominated by dissipation.}

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
                  directory='\writeDiagrams/physics')}

\figure{\includediagram{\diagramsDir/physics/generic-decomposition-trajectories}{80%}}{Phase space trajectories showing: (left) pure dissipation from $S$ - all trajectories decay to origin; (center) pure rotation from $A$ - trajectories circulate without decay; (right) combined dynamics from $M = S+A$ - damped rotation spiraling toward equilibrium.}{generic-decomposition-trajectories}

\notes{**Key insights from the visualization:**

Note: The trajectories are shown over an extended time ($t \in [0, 30]$) to make the rotation from $A$ clearly visible. The oscillation period is approximately $2\pi/0.088 \approx 71$ time units, so we see about 0.4 cycles.

1. **Pure $S$ dynamics (left)**: Trajectories decay exponentially toward the origin. This is pure dissipation—entropy production drives the system to equilibrium. All eigenvalues are real and negative.

2. **Pure $A$ dynamics (center)**: Trajectories circulate without approaching the origin. This is conservative dynamics—no entropy production, just rotation on the constraint manifold. The norm $\|q\|$ is perfectly conserved. Eigenvalues are purely imaginary.

3. **Combined $M = S + A$ dynamics (right)**: Trajectories spiral inward. The symmetric part causes decay while the antisymmetric part causes rotation. This is the GENERIC structure: dissipation + conservation = damped oscillation.

**Why is the antisymmetric effect weak here?** At this particular equilibrium (maximum entropy with $\nu^\ast = 0$), we're deep in the Gaussian regime where $\|A\|/\|S\| \approx 0.37$. The antisymmetric part emerges from third-order corrections (third cumulants and constraint curvature). If we moved to equilibria with tighter constraints ($\nu > 0$) or more non-Gaussian distributions, the antisymmetric part would become more prominent, and mechanical behavior would dominate.}

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
                  directory='\writeDiagrams/physics')}

\figure{\includediagram{\diagramsDir/physics/generic-energy-evolution}{70%}}{Energy evolution showing: (blue) pure $S$ dynamics monotonically decrease energy; (red dashed) pure $A$ dynamics conserve energy; (green) combined $M$ dynamics show damped oscillations with overall energy decrease.}{generic-energy-evolution}

\notes{The energy plot clearly shows:
- **Pure $S$**: Monotonic decay to zero (pure dissipation)
- **Pure $A$**: Constant energy (pure conservation)
- **Combined $M$**: Oscillations with overall decay (dissipation + conservation)

This is exactly the GENERIC structure: the symmetric part drives irreversible energy dissipation, while the antisymmetric part creates reversible oscillations.}

\notes{**Summary:** This computational example demonstrates that the GENERIC decomposition $M = S + A$ isn't just abstract mathematics, it has a dynamical meaning. The symmetric part $S$ controls stability and dissipation, while the antisymmetric part $A$ controls rotation and oscillation. Together they combine to create the rich dynamics we see in physical and information-theoretic systems.}

\endif


