\ifndef{linearisationGeneralVsEquilibrium}
\define{linearisationGeneralVsEquilibrium}

\editme

\subsection{Linearisation: Beyond Equilibrium}

\notes{In Lecture 6, we learned how to linearise the constrained dynamics around an equilibrium point $\boldsymbol{\theta}^\ast$ where $\dot{\boldsymbol{\theta}}^\ast = 0$. This gave us clean dynamics for perturbations:
$$
\dot{q} = Mq, \quad q = \boldsymbol{\theta} - \boldsymbol{\theta}^\ast
$$
where $M$ is the linearisation matrix (Jacobian of the dynamics at $\boldsymbol{\theta}^\ast$).

But what if we want to understand the flow structure at a point where the system is *not* in equilibrium? Can we still linearise? And if so, what changes?}

\slides{
**Recall from Lecture 6**

Equilibrium linearisation:
* Point: $\boldsymbol{\theta}^\ast$ where $\dot{\boldsymbol{\theta}} = 0$
* Perturbation: $q = \boldsymbol{\theta} - \boldsymbol{\theta}^\ast$
* Dynamics: $\dot{q} = Mq$

**Question:** What about non-equilibrium points?
}

\subsection{General Linearisation at Any Point}

\notes{The answer is yes! We can linearise around **any point** $\boldsymbol{\theta}_0$ on the constraint manifold, whether it's an equilibrium or not.

Recall the general constrained dynamics:
$$
\dot{\boldsymbol{\theta}} = F(\boldsymbol{\theta}) = -G(\boldsymbol{\theta})\boldsymbol{\theta} - \nu(\boldsymbol{\theta}) a(\boldsymbol{\theta})
$$

For a small deviation $\delta\boldsymbol{\theta} = \boldsymbol{\theta} - \boldsymbol{\theta}_0$ from some reference point $\boldsymbol{\theta}_0$, Taylor expansion gives:
$$
\dot{\boldsymbol{\theta}} = F(\boldsymbol{\theta}_0) + \frac{\partial F}{\partial \boldsymbol{\theta}}\bigg|_{\boldsymbol{\theta}_0} \delta\boldsymbol{\theta} + O(\|\delta\boldsymbol{\theta}\|^2)
$$

Define the Jacobian matrix:
$$
M(\boldsymbol{\theta}_0) = \frac{\partial F}{\partial \boldsymbol{\theta}}\bigg|_{\boldsymbol{\theta}_0}
$$

Then the linearised dynamics are:
$$
\dot{\boldsymbol{\theta}} \approx F(\boldsymbol{\theta}_0) + M(\boldsymbol{\theta}_0) \delta\boldsymbol{\theta}
$$

The key observation: this works at **any** point $\boldsymbol{\theta}_0$, not just equilibria!}

\slides{
**General Linearisation**

At any point $\boldsymbol{\theta}_0$:

Taylor expand: $\dot{\boldsymbol{\theta}} \approx F(\boldsymbol{\theta}_0) + M(\boldsymbol{\theta}_0)\delta\boldsymbol{\theta}$

where
* $F(\boldsymbol{\theta}_0) = \dot{\boldsymbol{\theta}}|_{\boldsymbol{\theta}_0}$ (drift)
* $M(\boldsymbol{\theta}_0) = \partial F/\partial\boldsymbol{\theta}|_{\boldsymbol{\theta}_0}$ (Jacobian)
* $\delta\boldsymbol{\theta} = \boldsymbol{\theta} - \boldsymbol{\theta}_0$

Works **everywhere**, not just equilibria!
}

\subsection{What Changes at Non-Equilibrium Points?}

\notes{The difference between equilibrium and non-equilibrium linearisation is simple but important:

**At equilibrium** ($\boldsymbol{\theta}^\ast$ where $F(\boldsymbol{\theta}^\ast) = 0$):
$$
\dot{\boldsymbol{\theta}} \approx M(\boldsymbol{\theta}^\ast) q, \quad q = \boldsymbol{\theta} - \boldsymbol{\theta}^\ast
$$
- No constant drift term
- Pure linear dynamics
- Perturbations evolve according to $M$ alone

**At general point** ($\boldsymbol{\theta}_0$ where $F(\boldsymbol{\theta}_0) \neq 0$):
$$
\dot{\boldsymbol{\theta}} \approx F(\boldsymbol{\theta}_0) + M(\boldsymbol{\theta}_0) \delta\boldsymbol{\theta}
$$
- Constant drift $F(\boldsymbol{\theta}_0)$ carries the system along the flow
- Linear corrections $M\delta\boldsymbol{\theta}$ describe how nearby trajectories diverge/converge/rotate relative to the reference trajectory

**Physical interpretation:** At a non-equilibrium point, you're sitting on a "moving platform" (the flow $F(\boldsymbol{\theta}_0)$) and watching how nearby trajectories behave relative to you. The matrix $M$ tells you whether they come closer, move away, or rotate around you as you all flow together.}

\slides{
**Equilibrium vs Non-Equilibrium**

| Property | Equilibrium $\boldsymbol{\theta}^\ast$ | General $\boldsymbol{\theta}_0$ |
|----------|------------------|-----------------|
| Drift | $F = 0$ | $F \neq 0$ |
| Dynamics | $\dot{q} = Mq$ | $\dot{\boldsymbol{\theta}} = F_0 + M\delta\boldsymbol{\theta}$ |
| Interpretation | Perturbations evolve | Relative to flow |

**Key:** $M$ describes **local flow structure** everywhere!
}

\subsection{Why Does the Jacobian $M$ Matter?}

\notes{You might wonder: "If there's a constant drift term at non-equilibrium points, why do we care about $M$?"

The answer is that $M$ reveals the **local geometry of the flow**:

1. **Stability/Instability**: Even with drift, $M$ tells us if nearby trajectories converge toward or diverge away from the reference trajectory. Real eigenvalues of $M$ give exponential convergence/divergence rates.

2. **Rotation/Oscillation**: Imaginary eigenvalues of $M$ tell us if the flow exhibits local rotation or spiraling, independent of the drift direction.

3. **Universal decomposition**: At every point, we can decompose $M = S + A$ where $S$ is symmetric and $A$ is antisymmetric. This decomposition is **always valid** because it's purely mathematical—any square matrix has a unique such decomposition.

4. **Physical meaning**: The symmetric part $S$ describes how "volume" in phase space contracts or expands (dissipation). The antisymmetric part $A$ describes how trajectories rotate around each other (conservation). This interpretation holds at every point, whether equilibrium or not.

In today's lecture, we'll focus on this decomposition $M = S + A$ and what it reveals about the structure of information dynamics.}

\slides{
**Why $M$ Matters Everywhere**

Even with drift $F(\boldsymbol{\theta}_0)$, the Jacobian $M$ reveals:

1. **Local stability** (do nearby trajectories converge?)
2. **Rotation/oscillation** (do they spiral?)
3. **Universal decomposition** $M = S + A$
   * $S$: symmetric (dissipation, volume change)
   * $A$: antisymmetric (rotation, conservation)

**Today's focus:** Understanding $M = S + A$
}

\subsection{Equilibrium as a Special Case}

\notes{From this perspective, equilibrium points are not privileged—they're just the special case where $F(\boldsymbol{\theta}^\ast) = 0$, so the drift term vanishes and we have pure linear dynamics.

Why did we study equilibria first in Lecture 6? Two reasons:

1. **Pedagogical**: Equilibria are conceptually simpler (no drift term), making them ideal for introducing linearisation techniques.

2. **Practical**: At equilibrium, we can study long-time behavior without the system "drifting away." This makes equilibrium analysis particularly useful for understanding steady states and stability.

But now we can appreciate that the linearisation framework—and the decomposition $M = S + A$ we'll study today—applies **everywhere** on the constraint manifold. The flow structure is richer than equilibria alone can reveal.}

\slides{
**Equilibrium: Just a Special Case**

$$
F(\boldsymbol{\theta}^\ast) = 0 \quad \Rightarrow \quad \text{drift vanishes}
$$

Why study equilibria first?
* Pedagogically simpler (no drift)
* Long-time behavior clear

But the framework is **general**:
* Linearisation: works anywhere
* Decomposition $M = S + A$: works anywhere
* Physical interpretation: works anywhere

**Flow structure is everywhere!**
}

\notes{**Summary:** Linearisation is not restricted to equilibria. At any point $\boldsymbol{\theta}_0$ on the constraint manifold, we can linearise to get $\dot{\boldsymbol{\theta}} \approx F(\boldsymbol{\theta}_0) + M(\boldsymbol{\theta}_0)\delta\boldsymbol{\theta}$. The Jacobian $M$ captures the local flow geometry, and its decomposition $M = S + A$ reveals the balance between dissipative and conservative dynamics at that point. Equilibria are just the special case where the drift term $F$ vanishes, simplifying the analysis but not fundamentally changing the structure. In today's lecture, we'll explore this decomposition and see what it tells us about information dynamics.}

\endif

