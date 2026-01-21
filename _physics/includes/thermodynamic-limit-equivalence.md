\ifndef{thermodynamicLimitEquivalence}
\define{thermodynamicLimitEquivalence}

\editme

\subsection{Energy-Entropy Equivalence in the Thermodynamic Limit}

\notes{We've seen that marginal entropy conservation $\sum_i h_i = C$ leads to GENERIC-like structure. But how does this connect to traditional thermodynamics with energy conservation? The answer lies in the thermodynamic limit.}

\subsubsection{The Energy-Entropy Question}

\notes{In real GENERIC systems, it's not marginal entropy that's conserved but extensive thermodynamic energy $E$. Can we show that, under specific conditions, the marginal entropy constraint asymptotically singles out the same degeneracy direction as energy conservation?

In other words, does the constraint gradient $\nabla(\sum_i h_i)$ become parallel to $\nabla E$ in appropriate limits?}

\slides{
**Question:**

Does $\nabla\left(\sum h_i\right) \parallel \nabla E$ ?

*Connects information to thermodynamics*
}

\subsection{Conditions for Equivalence}

\notes{The equivalence requires specific scaling properties. Using multi-information $I = \sum_i h_i - H$, we can write:
$$
\nabla\left(\sum_i h_i\right) = \nabla I + \nabla H.
$$}

\notes{*Our requirement:* Along certain directions (order parameters), the multi-information gradient must scale *intensively* while entropy gradients scale *extensively*.

Specifically, consider a macroscopic order parameter $m$ (like magnetization in a spin system). The requirement is:
- $\nabla_m I = \mathscr{O}(1)$ (intensive)
- $\nabla_m H = \mathscr{O}(n)$ (extensive)
- $\nabla_m(\sum_i h_i) = \mathscr{O}(n)$ (extensive)

where $n$ is the number of variables.}

\slides{
**Scaling Requirements:**

Along order parameter $m$:
* $\nabla_m I = \mathscr{O}(1)$ — intensive
* $\nabla_m H = \mathscr{O}(n)$ — extensive  
* $\nabla_m\left(\sum h_i\right) = \mathscr{O}(n)$ — extensive

As $n \to \infty$: intensive correction negligible
}

\newslide{Asymptotic Parallelism}

\notes{When this scaling holds:
$$
\nabla_m\left(\sum_i h_i\right) = \nabla_m H + \nabla_m I = \mathscr{O}(n) + \mathscr{O}(1).
$$

In the thermodynamic limit $n \to \infty$, the $\mathscr{O}(1)$ correction from multi-information becomes negligible:
$$
\nabla_m\left(\sum_i h_i\right) \parallel \nabla_m H.
$$}

\slides{
**In Thermodynamic Limit:**

$$\nabla_m\left(\sum h_i\right) = \underbrace{\nabla_m H}_{\mathscr{O}(n)} + \underbrace{\nabla_m I}_{\mathscr{O}(1)}$$

$$\Rightarrow \nabla_m\left(\sum h_i\right) \parallel \nabla_m H$$

*Intensive correction vanishes relative to extensive term*
}

\subsection{Connecting to Energy}

\notes{For exponential families, the entropy gradient in expectation parameters $\boldsymbol{\mu} = \langle T(\mathbf{x})\rangle$ is:
$$
\nabla_{\boldsymbol{\mu}} H = \boldsymbol{\theta}
$$
where $\boldsymbol{\theta}$ are the natural parameters.}

\notes{Now define an energy functional as:
$$
E(\mathbf{x}) = -\boldsymbol{\alpha}^\top T(\mathbf{x})
$$
where $\boldsymbol{\alpha}$ is chosen such that $\boldsymbol{\theta} = -\beta\boldsymbol{\alpha}$. This gives:
$$
\nabla_{\boldsymbol{\mu}} E = -\boldsymbol{\alpha} = \frac{\boldsymbol{\theta}}{\beta} = \frac{\nabla_{\boldsymbol{\mu}} H}{\beta}.
$$}

\notes{Therefore
$$
\nabla E \parallel \nabla H \parallel \nabla\left(\sum_i h_i\right)
$$
along the macroscopic direction in the thermodynamic limit.}

\slides{
**Energy Definition:**

Choose $E(\mathbf{x}) = -\boldsymbol{\alpha}^\top T(\mathbf{x})$ with $\boldsymbol{\theta} = -\beta\boldsymbol{\alpha}$

$$\Rightarrow \nabla E = \frac{\nabla H}{\beta}$$

**Result:**
$$\boxed{\nabla E \parallel \nabla H \parallel \nabla\left(\sum h_i\right)}$$

$\beta$ emerges as inverse temperature
}

\subsection{When Does This Hold?}

\notes{The equivalence requires:

1. **Macroscopic order parameter:** There exists a low-dimensional direction (like total magnetisation $m = \sum_i x_i$) that captures system-wide behavior

2. **Bounded correlations:** The correlation length $\xi$ remains finite (away from criticality), ensuring $\nabla_m I$ stays intensive

3. **Translation invariance:** Symmetry ensures marginal entropies are identical conditioned on the order parameter

4. **Thermodynamic limit:** Number of variables $n \to \infty$}

\slides{
**Requirements:**

1. Macroscopic order parameter exists (e.g. magnetism)
2. Finite correlation length ($\xi < \infty$)
3. Translation invariance
4. Large system ($n \to \infty$)

*Not all systems satisfy these*
}

\notes{Not all systems satisfy these conditions. Near critical points, correlations diverge and the intensive scaling breaks down. In small systems, $\mathscr{O}(1)$ corrections matter. But for many physically relevant systems—bulk matter far from phase transitions—the equivalence holds and provides a bridge between information theory and thermodynamics.}

\subsection{Implications}

\notes{This equivalence has several implications:

1. **Information $\leftrightarrow$ Thermodynamics:** Energy conservation and marginal entropy conservation become equivalent statements in appropriate limits

2. **Temperature emergence:** The parameter $\beta$ emerges as inverse temperature from the information geometry, not imposed from thermodynamics

3. **Landauer's principle:** Can be derived from information conservation via this equivalence

4. **Wheeler's "it from bit":** Suggests thermodynamics might emerge from information-theoretic principles}

\slides{
**Implications:**

* Energy = Information (in limit)
* Temperature emerges from geometry
* Landauer derivable
* "It from bit" justified

**Reverses usual logic:**
$$\text{Information theory} \Rightarrow \text{Thermodynamics}$$
}

\endif
