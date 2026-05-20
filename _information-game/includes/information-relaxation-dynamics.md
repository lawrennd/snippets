\ifndef{informationRelaxationDynamics}
\define{informationRelaxationDynamics}

\editme

\subsection{Information Relaxation Dynamics}

\notes{Consider a simple two-variable system with binary variables $X_1$ and $X_2$:

**High correlation state** (high $I$, low $H$):
$$
p(X_1=0, X_2=0) = 0.5, \quad p(X_1=1, X_2=1) = 0.5
$$
The variables are perfectly correlated. Marginal entropies: $h_1 = h_2 = 1$ bit. Joint entropy: $H = 1$ bit. Multi-information: $I = 1 + 1 - 1 = 1$ bit.

**Low correlation state** (low $I$, high $H$):
$$
p(X_1, X_2) = 0.25 \text{ for all four combinations}
$$
The variables are independent. Marginal entropies: $h_1 = h_2 = 1$ bit. Joint entropy: $H = 2$ bits. Multi-information: $I = 1 + 1 - 2 = 0$ bits.

The system relaxes from the first state to the second, conserving $I + H = 2$ bits throughout. Let's visualise this relaxation:}

\setupcode{import numpy as np}


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
from mlai.utils import write_figure}

\helpercode{def compute_binary_entropies(p00, p01, p10, p11):
    """Compute marginal entropies, joint entropy, and multi-information"""
    # Marginal distributions
    p0_ = p00 + p01  # P(X1=0)
    p1_ = p10 + p11  # P(X1=1)
    p_0 = p00 + p10  # P(X2=0)
    p_1 = p01 + p11  # P(X2=1)
    
    # Marginal entropies (in nats, using natural log)
    def h(p):
        if p == 0 or p == 1:
            return 0
        return -p * np.log(p) - (1-p) * np.log(1-p)
    
    h1 = h(p0_)
    h2 = h(p_0)
    
    # Joint entropy
    H = 0
    for p in [p00, p01, p10, p11]:
        if p > 0:
            H -= p * np.log(p)
    
    # Multi-information
    I = h1 + h2 - H
    
    return h1, h2, H, I

def relaxation_path(alpha):
    """
    Interpolate between correlated and independent states
    alpha = 0: fully correlated
    alpha = 1: independent
    Keeps marginals at 0.5 throughout
    """
    # Correlated state: p00 = p11 = 0.5
    # Independent state: all four = 0.25
    p00 = 0.5 * (1 - alpha) + 0.25 * alpha
    p11 = 0.5 * (1 - alpha) + 0.25 * alpha
    p01 = 0.25 * alpha
    p10 = 0.25 * alpha
    
    return p00, p01, p10, p11
}

\code{# Generate relaxation trajectory
n_steps = 100
alphas = np.linspace(0, 1, n_steps)

h1_vals = []
h2_vals = []
H_vals = []
I_vals = []

for alpha in alphas:
    p00, p01, p10, p11 = relaxation_path(alpha)
    h1, h2, H, I = compute_binary_entropies(p00, p01, p10, p11)
    h1_vals.append(h1)
    h2_vals.append(h2)
    H_vals.append(H)
    I_vals.append(I)

h1_vals = np.array(h1_vals)
h2_vals = np.array(h2_vals)
H_vals = np.array(H_vals)
I_vals = np.array(I_vals)
C_vals = I_vals + H_vals  # Should be constant
}

\plotcode{fig, (ax1, ax2) = plt.subplots(1, 2, figsize=plot.big_wide_figsize)

# Left plot: I and H over time
time = np.arange(n_steps)
ax1.plot(time, I_vals, 'r-', linewidth=2, label='Multi-information $I$')
ax1.plot(time, H_vals, 'b-', linewidth=2, label='Joint entropy $H$')
ax1.plot(time, C_vals, 'k--', linewidth=2, alpha=0.7, label='$I + H = C$')
ax1.fill_between(time, 0, I_vals, alpha=0.2, color='red', label='Correlation')
ax1.fill_between(time, I_vals, C_vals, alpha=0.2, color='blue', label='Entropy')
ax1.set_xlabel('Time (arbitrary units)')
ax1.set_ylabel('Information (nats)')
ax1.set_title('Information Relaxation: $I$ → $H$')
ax1.legend(loc='center right')
ax1.grid(True, alpha=0.3)

# Right plot: Marginal entropies (constant)
ax2.plot(time, h1_vals, 'g-', linewidth=2, label='$h_1$ (marginal)')
ax2.plot(time, h2_vals, 'm-', linewidth=2, label='$h_2$ (marginal)', linestyle='--')
ax2.plot(time, h1_vals + h2_vals, 'k-', linewidth=2, label='$h_1 + h_2 = C$')
ax2.set_xlabel('Time (arbitrary units)')
ax2.set_ylabel('Entropy (nats)')
ax2.set_title('Marginal Entropies: Conserved')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
mlai.write_figure(filename='i-plus-h-relaxation.svg', 
                  directory='\writeDiagramsDir/information-game')}


\figure{\includediagram{\diagramsDir/information-game/i-plus-h-relaxation}{80%}}{Left: Multi-information $I$ decreases as joint entropy $H$ increases, conserving $I + H = C$. The colored regions show how the conserved quantity splits between correlation (red) and entropy (blue). Right: Marginal entropies remain constant throughout, making the system inaccessible to external observation.}{i-plus-h-relaxation}

\notes{The visualisation shows the trade-off: as the system relaxes, correlation structure (multi-information) is converted into entropy. The total $I + H = C$ remains constant (black dashed line), but the system evolves from a state dominated by correlation to one dominated by entropy.

The marginal entropies $h_1$ and $h_2$ stay constant throughout this evolution. An external observer measuring only marginal entropies would see no change—the system is informationally isolated, hence "inaccessible."}

\endif
