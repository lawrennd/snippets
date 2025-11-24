\ifndef{iPlusHEqualsC}
\define{iPlusHEqualsC}

\editme

\subsection{The $I + H = C$ Structure}

\notes{We have established four axioms, with the fourth axiom stating that the sum of marginal entropies is conserved,
$$
\sum_{i=1}^N h_i = C.
$$
This conservation law is the heart of The Inaccessible Game, but to understand its dynamical implications, we need to rewrite it in a more revealing form.}

\slides{
**The Fourth Axiom:**
$$
\sum_{i=1}^N h_i = C
$$

*What does this conservation imply for dynamics?*
}

\subsection{Multi-Information: Measuring Correlation}

\notes{The **multi-information** (or **total correlation**), introduced by @Watanabe-multiinformation60, measures how much the variables in a system are correlated. It is defined as,
$$
I = \sum_{i=1}^N h_i - H,
$$
where $H$ is the **joint entropy** of the full system:
$$
H = -\sum_{\mathbf{x}} p(\mathbf{x}) \log p(\mathbf{x}).
$$

The multi-information has a clear interpretation:
- **$I = 0$**: The variables are completely independent. The joint entropy equals the sum of marginal entropies.
- **$I > 0$**: The variables are correlated. Some information is "shared" between variables, so the joint entropy is less than the sum of marginals.
- **$I$ is maximal**: The variables are maximally correlated (in the extreme case, deterministically related).

Multi-information is always non-negative ($I \geq 0$) and measures how much knowing one variable tells you about others.}

\slides{
**Multi-Information:**
$$
I = \sum_{i=1}^N h_i - H
$$

* $I = 0$: Independent variables
* $I > 0$: Correlated variables
* Larger $I$ = more correlation

*Measures "shared information"*
}

\subsection{The Information Action Principle: $I + H = C$}

\notes{Using the definition of multi-information, we can rewrite our conservation law. From $I = \sum_{i=1}^N h_i - H$, we have:
$$
\sum_{i=1}^N h_i = I + H.
$$
Therefore, the fourth axiom $\sum_{i=1}^N h_i = C$ becomes:
$$
I + H = C.
$$

This is an *information action principle*. It says that multi-information plus joint entropy is conserved. This equation sits behind the dynamics of the Inaccessible Game.}

\slides{
**Information Action Principle:**
$$
I + H = C
$$

*Conserved quantity splits into two parts*

**Analogy to classical mechanics:**

* Energy: $T + V = E$
* Information: $I + H = C$
}

\newslide{Physical Analogy}

\notes{This equation has the structure of an action principle in classical mechanics. In physics, total energy is conserved and splits into two parts,
$$
T + V = E,
$$
where $T$ is kinetic energy and $V$ is potential energy.

The analogy for The Inaccessible Game is.

- **Multi-information $I$** plays the role of *potential energy*. It represents "stored" correlation structure. High $I$ means variables are tightly coupled, like a compressed spring.
- **Joint entropy $H$** plays the role of *kinetic energy*. It represents "dispersed" or "free" information. High $H$ means the probability distribution is spread out, with maximal uncertainty.

Just as a classical system evolves from high potential energy to high kinetic energy (a ball rolling down a hill), the idea in the Inaccessible Game will be that the information system evolves from high correlation (high $I$) to high entropy (high $H$).}

\slides{
| Classical Mechanics | Information System |
|---------------------|-------------------|
| Kinetic energy $T$ | Joint entropy $H$ |
| Potential energy $V$ | Multi-information $I$ |
| Conservation: $T + V = E$ | Conservation: $H + I = C$ |

*System "rolls downhill" from correlation to entropy*
}

\subsection{The Information Relaxation Principle}

\notes{The $I + H = C$ structure suggests a *relaxation principle*: systems naturally evolve from states of high correlation (high $I$, low $H$) toward states of low correlation (low $I$, high $H$).

Why? Our inspiration is that the second law of thermodynamics tells us that entropy increases. If we want to introduce dynamics in the game, increasing entropy provides an obvious way to do that. Since $I + H = C$ is constant, if $H$ increases, $I$ must decrease. The system *breaks down correlations* to increase entropy.

This is analogous to how physical systems relax from non-equilibrium states (low $T$, high $V$) to equilibrium (high $T$, low $V$). A compressed spring releases its stored energy. A hot object in a cold room disperses its energy. In information systems, correlated structure dissipates into entropy.}

\slides{
**Information Relaxation:**

* Second law: Entropy increases ($\dot{H} > 0$)
* Conservation: $I + H = C$ (constant)
* Therefore: Correlation decreases ($\dot{I} < 0$)

**Physical intuition:**

* Compressed spring $\rightarrow$ released energy
* Correlated variables $\rightarrow$ independent variables
* Potential $\rightarrow$ kinetic
}

\newslide{Visualisation: Relaxation Dynamics}

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

The system relaxes from the first state to the second, conserving $I + H = 2$ bits throughout. Let's visualize this relaxation:}

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

\newslide{Information Relaxation Dynamics}

\figure{\includediagram{\diagramsDir/information-game/i-plus-h-relaxation}{80%}}{Left: Multi-information $I$ decreases as joint entropy $H$ increases, conserving $I + H = C$. The colored regions show how the conserved quantity splits between correlation (red) and entropy (blue). Right: Marginal entropies remain constant throughout, making the system inaccessible to external observation.}{i-plus-h-relaxation}

\notes{The visualisation shows the trade-off: as the system relaxes, correlation structure (multi-information) is converted into entropy. The total $I + H = C$ remains constant (black dashed line), but the system evolves from a state dominated by correlation to one dominated by entropy.

The marginal entropies $h_1$ and $h_2$ stay constant throughout this evolution. An external observer measuring only marginal entropies would see no change—the system is informationally isolated, hence "inaccessible."}

\slides{
**Key Features:**

* Multi-information $I$ decreases (correlations break)
* Joint entropy $H$ increases (disorder grows)
* Conservation: $I + H = C$ (black line)
* Marginals: $h_1$, $h_2$ constant (inaccessible!)

*Internal reorganisation invisible to external observer*
}

\subsection{Connection to Marginal Entropy Conservation}

\notes{Why does this structure conserve marginal entropies? Recall that from Baez's axioms, any change in entropy of a subsystem represents "information loss" to an external observer. If the observer learns nothing about the system (information isolation), then
$$
\Delta\left(\sum_{i=1}^N h_i\right) = 0.
$$
The $I + H = C$ formulation provides our dynamics clear: as the system evolves, *correlations are traded for entropy*. The marginal entropies remain fixed (so an external observer learns nothing), while internally the system reorganises from a correlated state to an uncorrelated state.

Importantly, information conservation doesn't mean nothing changes,  it means the changes are *internal redistributions* that leave marginal entropies (and hence external information) unchanged. The system is inaccessible to the outside because its dynamics preserve $\sum h_i$ which means they preserve $I + H$.}

\slides{
**Key Insight:**

Conservation $\sum h_i = C$ $\iff$ $I + H = C$

* External view: Marginals constant (inaccessible)
* Internal view: $I \leftrightarrow H$ (dynamic redistribution)

**Dynamics = trading correlation for entropy**
}

\subsection{Why This Matters for Dynamics}

\notes{The $I + H = C$ structure immediately tells us:

1. **Direction of evolution**: Systems move from high $I$ to high $H$ (correlation to entropy).

2. **Constrained dynamics**: Not all paths through probability space are allowed. Only those preserving $I + H = C$ are accessible.

3. **Physical interpretation**: The split into $I$ (correlation/potential) and $H$ (entropy/kinetic) gives us a sense of what's happening, later we will parameterise directly through natural parameters $\boldsymbol{\theta}$ (from Lecture 1).

4. **Variational principle**: The action-like structure hints that we can derive dynamics from a variational principle, just as Lagrangian mechanics derives equations of motion from the principle of least action.

In the next section, we'll see how information relaxation, i.e. the tendency to move from high $I$ to high $H$, leads to maximum entropy production dynamics in the natural parameter space.}

\slides{
**Implications:**

1. Direction: High $I$ $\rightarrow$ High $H$
2. Constraint: Only paths with $I + H = C$ allowed
3. Coordinates: $I$ and $H$ are natural
4. Variational principle: Derive dynamics from conservation
}

\endif
