\ifndef{stationaryPointsEquilibria}
\define{stationaryPointsEquilibria}

\editme

\subsection{Stationary Points and Equilibria}

\notes{The constrained dynamics eventually reach equilibrium—points where $\dot{\boldsymbol{\theta}} = 0$. Understanding these stationary points is key when predicting the behaviour of an information system under conservation constraints.}

\slides{
**Question:** When does $\dot{\boldsymbol{\theta}} = 0$?

**Answer:** At equilibria—stationary points of constrained dynamics
}

\subsection{Condition for Stationary Points}

\notes{Recall the constrained dynamics,
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(t) a(\boldsymbol{\theta}).
$$
For a stationary point, we need $\dot{\boldsymbol{\theta}} = 0$,
$$
G(\boldsymbol{\theta})\boldsymbol{\theta} + \nu a(\boldsymbol{\theta}) = 0.
$$
This equation, combined with the constraint $\sum h_i(\boldsymbol{\theta}) = C$, determines the equilibrium configuration.

Two cases are particularly important.

**Case 1: $\nu = 0$**  
Then $G\boldsymbol{\theta} = 0$. Since $G$ is positive definite (Fisher information), this requires $\boldsymbol{\theta} = 0$. This is the *maximum entropy state* with all natural parameters zero, the uniform distribution over all configurations.

**Case 2: $\nu \neq 0$**  
Then $G\boldsymbol{\theta} = -\nu a$. The entropy gradient is exactly balanced by the constraint force. These are *constrained equilibria* where entropy would like to increase further, but the constraint prevents it.}

\slides{
**Stationary Condition:**
$$
G\boldsymbol{\theta} + \nu a = 0
$$

**Two cases:**

1. $\nu = 0$: Maximum entropy ($\boldsymbol{\theta} = 0$)
2. $\nu \neq 0$: Constrained equilibrium

*Constraint balances entropy gradient*
}

\subsection{Maximum Entropy Equilibrium}

\notes{When $\nu = 0$ and $\boldsymbol{\theta} = 0$, we're at the *unconstrained maximum entropy state*. For exponential families, $\boldsymbol{\theta} = 0$ corresponds to whatever our reference measure $m(x)$ is with no bias from the sufficient statistics.

Properties of this equilibrium:
- **Highest possible entropy** $H$
- **Lowest possible multi-information** $I = 0$ (variables are independent)
- **All marginal entropies equal**: $h_i = h$ for all $i$
- **Satisfies conservation**: $\sum h_i = Nh = C$ requires $h = C/N$

This is the "thermal equilibrium" of information, maximum disorder, zero correlations. The system reaches this state if started at any point on the constraint manifold and evolved under MEP dynamics.

What this state actually looks like depends on the reference measure and the domain of each variable, which we haven't yet specified for the general inaccessible game.}

\slides{
**Maximum Entropy Equilibrium:**

* $\boldsymbol{\theta} = 0$ (reference measure, no bias)
* $I = 0$ (independent variables)
* $h_i = C/N$ (equal marginals)
* Maximum $H$, minimum $I$

*Thermal equilibrium of information*
}

\subsection{Constrained Equilibria}

\notes{Also interesting are equilibria with $\nu \neq 0$. From $G\boldsymbol{\theta} = -\nu a$.
$$
\boldsymbol{\theta} = -\nu G^{-1} a
$$
This says the natural parameters point along $G^{-1}a$—the constraint gradient transformed by the inverse Fisher metric.

Substituting into the formula for $\nu$
$$
\nu = -\frac{a^\top G\boldsymbol{\theta}}{a^\top a} = -\frac{a^\top G(-\nu G^{-1}a)}{a^\top a} = \frac{\nu a^\top a}{a^\top a} = \nu.
$$
This is consistent (as it must be), but doesn't directly tell us $\nu$'s value. To find the equilibrium, we must also satisfy the constraint
$$
\sum_{i=1}^N h_i(\boldsymbol{\theta}) = C.
$$
This gives a nonlinear equation that determines both $\boldsymbol{\theta}$ and $\nu$ at equilibrium. Generally, this requires numerical solution.}

\slides{
**Constrained Equilibria:**

At equilibrium: $\boldsymbol{\theta} = -\nu G^{-1} a$

Plus constraint: $\sum h_i(\boldsymbol{\theta}) = C$

**Two equations, two unknowns** ($\boldsymbol{\theta}$, $\nu$)

*Generally requires numerical solution*
}

\subsection{Local vs. Global Equilibria}

\notes{The constrained dynamics can have multiple equilibria:

**Global maximum**: The point $\boldsymbol{\theta} = 0$ (maximum entropy, $\nu = 0$) is the global equilibrium under the constraint. The entropy function $H(\boldsymbol{\theta})$ is strictly concave with a unique maximum at $\boldsymbol{\theta} = 0$. All trajectories eventually reach this state in the absence of barriers.

**Constrained equilibria**: Points where $\dot{\boldsymbol{\theta}} = 0$ with $\nu \neq 0$. These aren't local maxima of the entropy function itself (which has only one maximum), but rather points where the constraint force balances the entropy gradient. The constraint prevents the system from reaching the global maximum.

Since $H(\boldsymbol{\theta})$ is strictly concave, $G$ is positive definite, and therefore $-\Pi_\parallel G$ should have negative eigenvalues in all tangent directions. This suggests all constrained equilibria are stable attractors, not true saddle points.

However, the system can exhibit **critical slowing** near equilibria where some eigenvalues of $-\Pi_\parallel G$ are very small. These slow modes create long-lived transient structures (see Lecture 9), even though they're technically stable equilibria rather than saddles.

The distinction matters: true saddle points would be unstable and repel trajectories. Critical slowing creates slow convergence to stable equilibria, temporarily trapping information in certain modes.}

\slides{
**Types of Equilibria:**

* **Global max**: $\boldsymbol{\theta} = 0$ ($H$ strictly concave)
* **Constrained**: $\nu \neq 0$ (all should be stable!)
* **Critical slowing**: Small eigenvalues $\rightarrow$ slow modes

*No true saddles if $H$ strictly concave and $G$ positive definite*

*Slow modes from small eigenvalues, not instability*
}

\subsection{Stability Analysis}

\notes{To determine if an equilibrium is stable, we linearise the dynamics around it. Let $\boldsymbol{\theta} = \boldsymbol{\theta}_{\text{eq}} + \delta\boldsymbol{\theta}$ where $|\delta\boldsymbol{\theta}|$ is small.

The linearised dynamics are:
$$
\delta\dot{\boldsymbol{\theta}} \approx -\Pi_\parallel(\boldsymbol{\theta}_{\text{eq}}) G(\boldsymbol{\theta}_{\text{eq}}) \delta\boldsymbol{\theta},
$$
where $\Pi_\parallel = I - \frac{aa^\top}{a^\top a}$ is the tangent space projector.

The stability depends on the eigenvalues of $-\Pi_\parallel G$:
- **Negative eigenvalues**: Stable modes (exponential convergence)
- **Small negative eigenvalues**: Slow modes (critical slowing)
- **Zero eigenvalue**: Constraint direction (marginal stability)

The constraint direction always has zero eigenvalue because $\Pi_\parallel a = 0$. We only care about eigenvalues in the tangent space.

Since $H$ is strictly concave, $G$ is positive definite. Therefore $-\Pi_\parallel G$ should have all negative eigenvalues in tangent directions, making all constrained equilibria stable. The question is not *whether* they're stable, but *how fast* they converge—modes with small eigenvalues create critical slowing.}

\slides{
**Stability:**

Linearised: $\delta\dot{\boldsymbol{\theta}} \approx -\Pi_\parallel G \delta\boldsymbol{\theta}$

Since $G$ positive definite $\rightarrow$ all eigenvalues negative

* Large $|\lambda|$: Fast convergence
* Small $|\lambda|$: Critical slowing
* Zero: Constraint direction

*All equilibria stable; speed varies by mode*
}

\subsection{Example: Two-Variable System}

\notes{Consider two binary variables with constraint $h_1 + h_2 = C$.

**Maximum entropy equilibrium**: Both variables uniform, $h_1 = h_2 = C/2$. This corresponds to $\theta_1 = \theta_2 = 0$ (no preference for 0 or 1) and $\theta_{12} = 0$ (no interaction).

**Constrained equilibrium**: Suppose we impose $C < 2\log 2$ (less than maximum possible). Then the maximum entropy configuration isn't achievable. Instead, the system settles into a configuration where:
- Marginals are biased: $h_1, h_2 < \log 2$
- Some correlation may exist: $I > 0$
- Constraint satisfied: $h_1 + h_2 = C$
- Lagrange multiplier: $\nu \neq 0$

The exact configuration depends on the specific value of $C$ and requires solving the equilibrium equations.}

\slides{
**Two-Variable Example:**

*Max entropy ($C = 2\log 2$):*
* $h_1 = h_2 = \log 2$ (uniform)
* $I = 0$ (independent)
* $\nu = 0$

*Constrained ($C < 2\log 2$):*
* $h_1, h_2 < \log 2$ (biased)
* $I > 0$ (correlated)
* $\nu \neq 0$
}

\subsection{Critical Slowing Near Equilibria}

\notes{As the system approaches equilibrium, the dynamics slow down. This is **critical slowing**—a universal feature of gradient systems near stationary points.

Near equilibrium:
$$
\|\dot{\boldsymbol{\theta}}\| = \|G\boldsymbol{\theta} + \nu a\| \approx \text{const} \cdot \|\boldsymbol{\theta} - \boldsymbol{\theta}_{\text{eq}}\|
$$

The closer we get to equilibrium, the slower the evolution. This has important consequences:

1. **Long relaxation times**: The system takes a long time to fully reach equilibrium
2. **Slow modes**: Modes with small eigenvalues evolve very slowly
3. **Emergent timescale hierarchy**: Different modes relax at different rates

The slowest modes correspond to directions with small projected Fisher information—these are the directions where the constraint and entropy gradient nearly align, so little "force" is available to drive dynamics.}

\slides{
**Critical Slowing:**

Near equilibrium: $\|\dot{\boldsymbol{\theta}}\| \to 0$

**Consequences:**

* Long relaxation times
* Slow modes with small eigenvalues
* Emergent timescale hierarchy

*Different modes relax at different rates*
}

\subsection{Equilibria and Regime Structure}

\notes{The pattern of equilibria determines the *regime structure* of the information system. We will explore this in the remainder of the course.

**Basins of attraction**: Regions of parameter space that flow to the same equilibrium define regimes. Different initial conditions in the same basin exhibit similar long-term behavior.

**Hierarchy of timescales**: Fast modes quickly reach quasi-equilibrium in their directions, while slow modes create long-lived transient structures. This hierarchy is key to emergence.

Understanding equilibria is thus not just about final states—it's about understanding the structure of the entire dynamical landscape.}

\slides{
**Regime Structure:**

* Basins of attraction $\rightarrow$ regimes
* Timescale hierarchy $\rightarrow$ emergence
* Slow modes $\rightarrow$ long-lived structures

*Equilibria organize the whole dynamical landscape*

**Preview:** Later lectures on regimes and emergence
}

\subsection{Summary: Stationary Points}

\notes{**Key results:**

1. **Equilibrium condition**: $G\boldsymbol{\theta} + \nu a = 0$ with $\sum h_i = C$

2. **Maximum entropy**: $\boldsymbol{\theta} = 0$, $\nu = 0$, $I = 0$ (global attractor)

3. **Constrained equilibria**: $\nu \neq 0$, $I > 0$ (all stable if $H$ strictly concave)

4. **Stability**: All equilibria stable; eigenvalues of $-\Pi_\parallel G$ all negative

5. **Critical slowing**: Dynamics slow near equilibria due to small eigenvalues

6. **Regime structure**: Pattern of equilibria and timescale hierarchy determines emergent behavior

The next lecture (Lecture 5) will introduce the Poisson bracket structure, showing how conservation emerges from antisymmetric dynamics. Then in later lectures, we'll study perturbations around these equilibria to understand regime transitions.}

\slides{
**Summary:**

* Equilibria: $G\boldsymbol{\theta} + \nu a = 0$
* Maximum entropy: $\boldsymbol{\theta} = 0$ (global)
* All equilibria stable (if $H$ strictly concave)
* Critical slowing: small eigenvalues $\rightarrow$ slow modes
* Timescale hierarchy $\rightarrow$ regimes

**Next:** Poisson brackets (conservation structure)
}

\endif

