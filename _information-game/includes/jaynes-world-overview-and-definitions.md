\ifndef{jaynesWorldOverviewAndDefinitions}
\define{jaynesWorldOverviewAndDefinitions}

\editme

\subsection{Jaynes' World}
\slides{
- System governed by probability and entropy
- Framework for observer-free dynamics and entropy-based emergence
- Aim: better understanding of the notion of an "information topography"
}

\notes{This game explores how structure, time, causality, and locality might emerge within a system governed solely by internal information-theoretic constraints. The hope is that it can serve as

- A *research framework* for observer-free dynamics and entropy-based emergence,
- A *conceptual tool* for exploring the notion of an information topography: A landscape in which information flows under constraints.}


\subsection{Definitions and Global Constraints}

\subsubsection{System Structure}

\slides{
- Full set of variables: $Z = \{Z_1, Z_2, \dots, Z_n\}$
- Partition at system time $\tau$:
  - Active variables $X(\tau)$: contributing to entropy
  - Latent variables $M(\tau)$: information reservoir
}

\notes{
Let $Z = \{Z_1, Z_2, \dots, Z_n\}$ be the full set of system variables. At game turn $\tau$, define a partition where $X(\tau) \subseteq Z$: are active variables (currently contributing to entropy) and  $M(\tau) = Z \setminus X(\tau)$: latent or frozen variables that are stored in the form of an *information reservoir* (@Barato-stochastic14,@Parrondo-thermodynamics15).}


\subsubsection{Representation via Density Matrix}

\slides{
- System state: $\rho(\boldsymbol{\theta}) = \frac{1}{Z(\boldsymbol{\theta})} \exp\left( \sum_i \theta_i H_i \right)$
- Entropy: $S(\boldsymbol{\theta}) = A(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \nabla A(\boldsymbol{\theta})$
- where $A(\boldsymbol{\theta}) = \log Z(\boldsymbol{\theta})$
- Fisher Information: $G_{ij}(\boldsymbol{\theta}) = \frac{\partial^2 A}{\partial \theta_i \partial \theta_j}$
}

\notes{We'll argue that the configuration space must be represented by a density matrix,
$$
\rho(\boldsymbol{\theta}) = \frac{1}{Z(\boldsymbol{\theta})} \exp\left( \sum_i \theta_i H_i \right),
$$
where $\boldsymbol{\theta} \in \mathbb{R}^d$ are the natural parameters, each $H_i$ is a Hermitian operator associated with the observables and the partition function is given by $Z(\boldsymbol{\theta}) = \mathrm{Tr}[\exp(\sum_i \theta_i H_i)]$.

From this we can see that the *log-partition function*, which has an interpretation as the cummulant generating function, is
$$
A(\boldsymbol{\theta}) = \log Z(\boldsymbol{\theta})
$$
and the von Neumann *entropy* is
$$
S(\boldsymbol{\theta}) = A(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \nabla A(\boldsymbol{\theta}).
$$
We can show that the *Fisher Information Matrix* is
$$
G_{ij}(\boldsymbol{\theta}) = \frac{\partial^2 A}{\partial \theta_i \partial \theta_j}.
$$}


\subsubsection{Entropy Capacity and Resolution}

\slides{
- Maximum entropy: $N$ bits
- Minimum detectable resolution: $\varepsilon$
- System dynamics show discrete, detectable transitions
}

\notes{We define our system to have a *maximum entropy* of $N$ bits. This implies a *minimum detectable resolution* in natural parameter space which we denote by $\varepsilon$. Changes in natural parameters smaller than $\varepsilon$ are treated as *invisible* bin the system. As a result, system dynamics exhibit *discrete, detectable transitions* between distinguishable states.}

\subsection{Dual Role of Parameters and Variables}

\slides{
- Each variable $Z_i$ has:
  - Generator $H_i$
  - Natural parameter $\theta_i$
- Active parameters evolve if $|\dot{\theta}_i| \geq \varepsilon$
}

\notes{Each variable $Z_i$ is associated with a generator $H_i$, and a natural parameter $\theta_i$. When we say a parameter $\theta_i \in X(\tau)$, we mean that the component of the system associated with $H_i$ is active at time $\tau$ and its parameter is evolving with $|\dot{\theta}_i| \geq \varepsilon$. This comes from the duality between *variables* and *natural parameters* that we find in density matrix representations.[^exponential]

[^exponential]: We also see this duality in *exponential family* distributions.}


\subsection{Core Axiom: Entropic Dynamics}

\slides{
- System evolves by steepest ascent in entropy
  $$
  \frac{d\boldsymbol{\theta}}{d\tau} = -G(\boldsymbol{\theta}) \boldsymbol{\theta}
  $$
- Follows the gradient of entropy in parameter space
}

\notes{The game evolves by steepest ascent in entropy. The gradient of the density matrix with respect to the natural parameters is given by
$$
\nabla S[\rho] = -G(\boldsymbol{\theta}) \boldsymbol{\theta}
$$
and so we set
$$
\frac{d\boldsymbol{\theta}}{d\tau} = -G(\boldsymbol{\theta}) \boldsymbol{\theta}
$$}

\subsection{Constructed Quantities and Lemmas}

\subsubsection{Variable Partition}
$$
X(\tau) = \left\{ i \mid \left| \frac{\text{d}\theta_i}{\text{d}\tau} \right| \geq \varepsilon \right\}, \quad M(\tau) = Z \setminus X(\tau)
$$

\slides{
- Active variables: $X(\tau) = \left\{ i \mid \left| \frac{\text{d}\theta_i}{\text{d}\tau} \right| \geq \varepsilon \right\}$
- Latent variables: $M(\tau) = Z \setminus X(\tau)$
- Partition can change as system evolves
}

\subsubsection{Fisher Information Matrix Partitioning}

\slides{
- Partition $G(\boldsymbol{\theta})$ into active/latent blocks
- $G_{XX}$: Information geometry of active variables
- $G_{MM}$: Structure of latent reservoir
- $G_{XM}$: Cross-coupling between domains
}

\notes{We partition the Fisher Information Matrix $G(\boldsymbol{\theta})$ according to the active variables $X(\tau)$ and (latent) information reservoir $M(\tau)$
$$
G(\boldsymbol{\theta}) = 
\begin{bmatrix}
G_{XX} & G_{XM} \\
G_{MX} & G_{MM}
\end{bmatrix}
$$
where $G_{XX}$ represents the information geometry within active variables, $G_{MM}$ within the latent reservoir, and $G_{XM} = G_{MX}^\top$ captures the cross-coupling between active and latent components. This partitioning governs how information flows between observed dynamics and the latent structure.}


\subsection{Lemma 1: Form of the Minimal Entropy Configuration}

\slides{
- Minimal entropy state: $\rho(\boldsymbol{\theta}_o) = \frac{1}{Z(\boldsymbol{\theta}_o)} \exp\left( \sum_i \theta_{oi} H_i \right)$
- All parameters sub-threshold: $|\dot{\theta}_{oi}| < \varepsilon$
- Regular, continuous, and detectable above resolution scale
}

\notes{The minimal-entropy state that is compatible with the system's resolution constraint and regularity condition is represented by a density matrix of the exponential form,
$$
\rho(\boldsymbol{\theta}_o) = \frac{1}{Z(\boldsymbol{\theta}_o)} \exp\left( \sum_i \theta_{oi} H_i \right),
$$
where all components $\theta_{oi}$ are sub-threshold
$$
|\dot{\theta}_{oi}| < \varepsilon.
$$
This state minimises entropy under the constraint that it remains regular, continuous, and detectable only above a resolution scale $\varepsilon $. Its structure can be derived via a *minimum-entropy* analogue of Jaynes' maximum entropy formalism [@Jaynes-information63], using the same density matrix geometry but inverted optimization.}


\subsubsection{Lemma 2: Symmetry Breaking}

\slides{
- If $\theta_k \in M(\tau)$ and $|\dot{\theta}_k| \geq \varepsilon$, then $\theta_k \in X(\tau + \delta)$
- Latent variables can become active when their rate of change exceeds threshold
- Mechanism for emergence of new active variables
}

\notes{If $\theta_k \in M(\tau)$ and $|\dot{\theta}_k| \geq \varepsilon$, then
$$
\theta_k \in X(\tau + \delta \tau).
$$}

\subsubsection{Perceived Time}

\slides{
- Entropy-time: $t(\tau) := S_{X(\tau)}(\tau)$
- Measures accumulated entropy of active variables
}

\notes{
The system evolves in two time scales:

1. *System time* $\tau$: the external time parameter in which the system evolves according to
$$
t(\tau) := S_{X(\tau)}(\tau)
$$

2. *Perceived time* $t$: the internal time that measures the accumulated entropy of active variables, defined as
$$
t(\tau) := S_{X(\tau)}(\tau)
$$

The relationship between these time scales is given by
$$
\frac{\text{d}t}{\text{d}\tau} = \boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta} = -\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}]
$$

This reveals that perceived time flows at different rates depending on the information content of the system. In regions where parameters are strongly aligned with entropy change, perceived time flows rapidly relative to system time. In regions where parameters are weakly coupled to entropy change, perceived time flows slowly.
}

\notes{\subsubsection{Lemma 3: Monotonicity of Perceived Time}

$$
t(\tau_2) \geq t(\tau_1) \quad \text{for all } \tau_2 > \tau_1
$$}

\newslide{Monotonicity of Perceived Time}
\slides{
- $t(\tau_2) \geq t(\tau_1)$ for all $\tau_2 > \tau_1$
- Perceived time always increases
- Implies irreversibility of the system
}

\subsubsection{Corollary: Irreversibility}

\slides{
- $t(\tau)$ increases monotonically
- Prevents time-reversal globally
- Provides an arrow of time for the system
}

\notes{
1. $t(\tau)$ increases monotonically, preventing time-reversal globally.}

2. In regions where parameters are weakly coupled to entropy change (low $\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}]$), perceived time flows slowly.

3. At critical points where parameters become orthogonal to the entropy gradient ($\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}] \approx 0$), the time parameterization approaches singularity indicating phase transitions in the system's information structure.
}

\subsection{Conjecture: Frieden-Analogous Extremal Flow}

\slides{
- When latent-to-active flow is extremal, system exhibits critical slowing
- System entropy separates into active variables $I = S[\rho_X]$ and "intrinsic information" $J = S[\rho_{X|M}]$
- Analogous to @Frieden-physics98 extreme physical information principle $\delta(I - J) = 0$ 
}

\notes{At points where the latent-to-active flow functional is locally extremal (e.g., $\frac{d \boldsymbol{\theta}_M}{d\tau} \approx 0 $), the system may exhibit critical slowing where information resevoir variables are slow relative to active variables. It may be possible to separate the system entropy into active variables and, $I = S[\rho_X]$ and "intrinsic information" $J= S[\rho_{X|M}]$ allowing us to create an information analogous to  B. Roy Frieden's extreme physical information (@Frieden-physics98) which allows derivation of locally valid differential equations that depend on the *information topography*.}


\endif
