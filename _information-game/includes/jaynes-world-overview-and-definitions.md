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
- Partition at time $t$:
  - Active variables $X(t)$: contributing to entropy
  - Latent variables $M(t)$: information reservoir
}

\notes{
Let $Z = \{Z_1, Z_2, \dots, Z_n\}$ be the full set of system variables. At game turn $t$, define a partition where $X(t) \subseteq Z$: are active variables (currently contributing to entropy) and  $M(t) = Z \setminus X(t)$: latent or frozen variables that are stored in the form of an *information reservoir* (Barato-stochastic14,@Parrondo-thermodynamics15).}


\subsubsection{Representation via Density Matrix}

\slides{
- System state: $\rho(\boldsymbol{\theta}) = \frac{1}{Z(\boldsymbol{\theta})} \exp\left( \sum_i \theta_i H_i \right)$
- Entropy: $S(\boldsymbol{\theta}) = A(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \nabla A(\boldsymbol{\theta})$
- Fisher Information: $G_{ij}(\boldsymbol{\theta}) = \frac{\partial^2 A}{\partial \theta_i \partial \theta_j}$
}

\notes{We'll argue that the configuration space must be represented by a  density matrix,
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

\notes{We define our system to have a *maximum entropy* of $N$ bits. If the dimension $d$ of the parameter space is fixed, this implies a *minimum detectable resolution* in natural parameter space,
$$
\varepsilon \sim \frac{1}{2^N},
$$
where changes in natural parameters smaller than $\varepsilon$ are treated as *invisible* by the system. As a result, system dynamics exhibit *discrete, detectable transitions* between distinguishable states.

Note if the dimension $d$ scales with $N$ (e.g., $d = \alpha N$ for some constant $\alpha$), then the resolution constraint becomes more complex. In this case, the volume of distinguishable states $(\varepsilon)^d$ must equal $2^N$, which leads to $\varepsilon = 2^{1/\alpha}$, a constant independent of $N$. This suggests that as the system's entropy capacity grows, it maintains a constant resolution while exponentially increasing the number of distinguishable states.}

\subsection{Dual Role of Parameters and Variables}

\slides{
- Each variable $Z_i$ has:
  - Generator $H_i$
  - Natural parameter $\theta_i$
- Active parameters evolve with $|\dot{\theta}_i| \geq \varepsilon$
}

\notes{Each variable $Z_i$ is associated with a generator $H_i$, and a natural parameter $\theta_i$. When we say a parameter $\theta_i \in X(t)$, we mean that the component of the system associated with $H_i$ is active at time $t$ and its parameter is evolving with $|\dot{\theta}_i| \geq \varepsilon$. This comes from the duality  *variables*, *observables*, and *natural parameters* that we find in exponential family representations and we also see in a density matrix representation.}


\subsection{Core Axiom: Entropic Dynamics}

\slides{
- System evolves by steepest ascent in entropy
  $$
  \frac{d\boldsymbol{\theta}}{dt} = -G(\boldsymbol{\theta}) \boldsymbol{\theta}
  $$
- Follows the gradient of entropy in parameter space
}

\notes{Our core axiom is that the system evolves by steepest ascent in entropy. The gradient of the density matrix with respect to the natural parameters is given by
$$
\nabla S[\rho] = -G(\boldsymbol{\theta}) \boldsymbol{\theta}
$$
and so we set
$$
\frac{d\boldsymbol{\theta}}{dt} = -G(\boldsymbol{\theta}) \boldsymbol{\theta}
$$}

\subsection{Constructed Quantities and Lemmas}

\subsubsection{Variable Partition}
$$
X(t) = \left\{ i \mid \left| \frac{\text{d}\theta_i}{\text{d}t} \right| \geq \varepsilon \right\}, \quad M(t) = Z \setminus X(t)
$$

\slides{
- Active variables: $X(t) = \left\{ i \mid \left| \frac{\text{d}\theta_i}{\text{d}t} \right| \geq \varepsilon \right\}$
- Latent variables: $M(t) = Z \setminus X(t)$
- Partition changes as system evolves
}

\subsubsection{Fisher Information Matrix Partitioning}

\slides{
- Partition $G(\boldsymbol{\theta})$ into active/latent blocks
- $G_{XX}$: Information geometry of active variables
- $G_{MM}$: Structure of latent reservoir
- $G_{XM}$: Cross-coupling between domains
}

\notes{We partition the Fisher Information Matrix $G(\boldsymbol{\theta})$ according to the active variables $X(t)$ and latent information reservoir $M(t)$:
$$
G(\boldsymbol{\theta}) = 
\begin{pmatrix}
G_{XX} & G_{XM} \\
G_{MX} & G_{MM}
\end{pmatrix}
$$
where $G_{XX}$ represents the information geometry within active variables, $G_{MM}$ within the latent reservoir, and $G_{XM} = G_{MX}^\top$ captures the cross-coupling between active and latent components. This partitioning reveals how information flows between observable dynamics and the latent structure.}


\subsection{Lemma 1: Form of the Minimal Entropy Configuration}

\slides{
- Minimal entropy state: $\rho(\boldsymbol{\theta}_0) = \frac{1}{Z(\boldsymbol{\theta}_0)} \exp\left( \sum_i \theta_{0i} H_i \right)$
- All parameters sub-threshold: $|\dot{\theta}_{0i}| < \varepsilon$
- Regular, continuous, and detectable above resolution scale
}

\notes{The minimal-entropy state compatible with the system's resolution constraint and regularity condition is represented by a density matrix of the exponential form:
$$
\rho(\boldsymbol{\theta}_0) = \frac{1}{Z(\boldsymbol{\theta}_0)} \exp\left( \sum_i \theta_{0i} H_i \right),
$$
where $\boldsymbol{\theta}_0 \approx \boldsymbol{0}$, and all components $\theta_{0i}$ are sub-threshold:
$$
|\dot{\theta}_{0i}| < \varepsilon
$$

This state minimizes entropy under the constraint that it remains regular, continuous, and detectable only above a resolution scale $\varepsilon \sim \frac{1}{2^N}$. Its structure can be derived via a *minimum-entropy* analogue of Jaynes' formalism, using the same density matrix geometry but inverted optimization.}


\subsubsection{Lemma 2: Symmetry Breaking}

\slides{
- If $\theta_k \in M(t)$ and $|\dot{\theta}_k| \geq \varepsilon$, then $\theta_k \in X(t + \delta)$
- Latent variables can become active when their rate of change exceeds threshold
- Mechanism for emergence of new active variables
}

\notes{If $\theta_k \in M(t)$ and $|\dot{\theta}_k| \geq \varepsilon$, then
$$
\theta_k \in X(t + \delta.
$$}


\subsubsection{Entropy-Time}

\slides{
- Entropy-time: $\tau(t) := S_{X(t)}(t)$
- Measures accumulated entropy of active variables
}

\notes{
$$
\tau(t) := S_{X(t)}(t)
$$
}

\notes{\subsubsection{Lemma 3: Monotonicity of Entropy-Time}

$$
\tau(t_2) \geq \tau(t_1) \quad \text{for all } t_2 > t_1
$$}

\newslide{Monotonicity of Entropy-Time}
\slides{
- $\tau(t_2) \geq \tau(t_1)$ for all $t_2 > t_1$
- Entropy-time always increases
- Implies irreversibility of the system
}

\subsubsection{Corollary: Irreversibility}
\newslide{Irreversibility}
\slides{
- $\tau(t)$ increases monotonically
- Prevents time-reversal globally
- Provides an arrow of time for the system
}

\notes{
$\tau(t)$ increases monotonically, preventing time-reversal globally.}



\subsection{Conjecture: Frieden-Analogous Extremal Flow}

\slides{
- When latent-to-active flow $\Psi(t)$ is extremal, system exhibits critical slowing
- System entropy separates into active variables $I = S[\rho_X]$ and "intrinsic information" $J = S[\rho_{X|M}]$
- Analogous to Frieden's extreme physical information principle $\delta(I - J) = 0$
}

\notes{At points where the latent-to-active flow functional $\Psi(t)$ is locally extremal (e.g., $\frac{d \boldsymbol{\theta}_M}{dt} \approx 0 $), the system may exhibit critical slowing where information resevoir variables are slow relative to active variables. It may be possible to separate the system entropy into active variables and, $I = S[\rho_X]$ and "intrinsic information" $J= S[\rho_{X|M}]$ allowing us to create an information analogous to  B. Roy Frieden's extreme physical information (Frieden-physics98) which allows derivation of locally valid differential equations that depend on the *information topography*.}


\endif
