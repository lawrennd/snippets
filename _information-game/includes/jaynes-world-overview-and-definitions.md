\ifndef{jaynesWorldOverviewAndDefinitions}
\define{jaynesWorldOverviewAndDefinitions}

\editme

\subsection{Jaynes' World}
\slides{
- Configuration is primary; parameters emerge from monitoring choices
- Distribution captures uncertainty about possible configurations
- Framework for observer-free dynamics and entropy-based emergence
}

\notes{This framework explores how structure, time, causality, and locality might emerge from representation through a  *configuration* and our *uncertainty about configuration*. The configuration—how variables actually relate to each other—is ontologically primary. All mathematical structures (parameters, distributions, entropy measures) emerge as consequences of tracking our uncertainty about which configuration is actual.

The system serves as:
- A *research framework* for observer-free dynamics and entropy-based emergence
- A *conceptual tool* for exploring information topography: landscapes where uncertainty about configuration evolves under constraints}

\subsection{Fundamental Structure: Configuration and Uncertainty}

\subsubsection{Configuration as Primary Reality}

\slides{
- Configuration: actual structural relationships between variables
- Primary ontological reality, independent of observation
- Parameters and mathematics are epistemic tools for tracking configuration
}

\notes{The *configuration* represents the state of structural relationships between system components. This is the reality that exists independently of our methods for observing or describing it. The mathematical representations--parameters, operators, entropy measures--are epistemic tools that emerge from our attempts to track configuration changes.}

\subsubsection{Uncertainty Distribution Over Configurations}

\slides{
- Density matrix $\rho$: uncertainty about which configuration is actual
- Not the configuration itself, but probability over possible configurations
- Von Neumann entropy: amount of uncertainty/disorder in our knowledge
}

\notes{A density matrix $\rho$ represents our *uncertainty about which configuration is actual*. The density matrix is defined over the space of possible configurations, it not a description of any particular configuration. The von Neumann entropy $S[\rho] = -\mathrm{tr}(\rho \log \rho)$ measures the amount of uncertainty in our knowledge—--equivalently, the amount of disorder in the space of possible configurations.}

\subsection{Emergence of Mathematical Structure}

\subsubsection{Exponential Family as Inevitable Consequence}

\slides{
- Exponential family form emerges automatically
- Result of minimizing uncertainty subject to resolution constraints
- Natural parameters $\theta_i$ are Lagrange multipliers from optimization
}

\notes{The exponential family-style representation for the density matrix is not a choice but a consequence of seeking the minimum uncertainty about configuration subject to resolution constraints. Minimising this uncertainty (maximising entropy) while preserving certain constraint information, the method of Lagrange multipliers automatically produces the form,
$$
\rho(\boldsymbol{\theta}) = \frac{1}{Z(\boldsymbol{\theta})} \exp\left( \sum_i \theta_i H_i \right),
$$
the *natural parameters* $\boldsymbol{\theta}$ emerge as the Lagrange multipliers needed to enforce our constraints on uncertainty.}

\subsubsection{System Structure Through Uncertainty Dynamics}

\slides{
- Full set of variables: $Z = \{Z_1, Z_2, \dots, Z_n\}$
- Partition emerges from uncertainty resolution:
  - Active variables $X(\tau)$: resolvable above threshold $\varepsilon$
  - Latent variables $M(\tau)$: uncertainty reservoir below threshold
}

\notes{Let $Z = \{Z_1, Z_2, \dots, Z_n\}$ be variables describing possible configurations. At any point in the system's evolution, our ability to resolve uncertainty partitions these into $X(\tau) \subseteq Z$ that are active variables where uncertainty gradients exceed resolution threshold $\varepsilon$ and $M(\tau) = Z \setminus X(\tau)$, latent variables forming an *information reservoir* where uncertainty changes remain below threshold (@Barato-stochastic14,@Parrondo-thermodynamics15)}.

\subsubsection{Derived Mathematical Objects}

\slides{
- Log-partition function: $A(\boldsymbol{\theta}) = \log Z(\boldsymbol{\theta})$
- Von Neumann entropy: $S(\boldsymbol{\theta}) = A(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \nabla A(\boldsymbol{\theta})$
- Fisher Information: $G_{ij}(\boldsymbol{\theta}) = \frac{\partial^2 A}{\partial \theta_i \partial \theta_j}$
- All emerge from uncertainty minimization, not imposed assumptions
}

\notes{The mathematical structures follow from the uncertainty framework, the *log-partition function* (which is a cumulant generating function) has the form,
$$
A(\boldsymbol{\theta}) = \log Z(\boldsymbol{\theta})
$$
and the *von Neumann entropy* measures uncertainty about the configuration:,
$$
S(\boldsymbol{\theta}) = A(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \nabla A(\boldsymbol{\theta})
$$
with the *Fisher Information Matrix* capturing the uncertainty geometry,
$$
G_{ij}(\boldsymbol{\theta}) = \frac{\partial^2 A}{\partial \theta_i \partial \theta_j}
$$
These choices arise from our uncertainty measures about configuration possibilities.}

\subsubsection{Resolution Constraints and Discrete Structure}

\slides{
- Maximum uncertainty capacity: $N$ bits
- Minimum detectable resolution: $\varepsilon$  
- Discrete transitions emerge from continuous underlying uncertainty
}

\notes{We limit the total number of configurations by bounding the system capacity ($N$ bits maximum). This in turn implies a minimum detectable resolution $\varepsilon$ in the uncertainty space.}

<!-- how does this disrete nature "leak" into the parameters ... the variables are discrete .. the parameters are emerging from tracking configurations. Are they also discrete or are they continuous? If they were discrete then changes in uncertainty gradients smaller than $\varepsilon$ would drive configuration changes. This would create detectable transitions in an otherwise continuous uncertainty landscape—explaining how discrete structure emerges from continuous foundations. -->

\subsection{Uncertainty-Driven Dynamics}

\subsubsection{Core Principle: Uncertainty Resolution}

\slides{
- System evolves to resolve uncertainty about configuration
- Steepest ascent in entropy = fastest uncertainty resolution
  $$
  \frac{\text{d}\boldsymbol{\theta}}{\text{d}\tau} = -G(\boldsymbol{\theta}) \boldsymbol{\theta}
  $$
- Parameters track this uncertainty resolution process
}


<!-- can we justify the instantaneous maximum entropy better. Previoyusly this was the udnrlying rule. But in the new view of configurations can we suggest why the instantaneous maximum entorpy gradient is fundamental?? that would imply that the system evolves to maximize entropy—equivalently, to most efficiently resolve uncertainty about configuration. The gradient flow,
$$
\frac{\text{d}\boldsymbol{\theta}}{\text{d}\tau} = -G(\boldsymbol{\theta}) \boldsymbol{\theta}
$$
would represent steepest ascent in the entropy landscape. Regall that the parameters $\boldsymbol{\theta}$ are not fundamental quantities but tracking variables that monitor this uncertainty resolution process.-->

\subsubsection{Variable Activation Through Uncertainty Thresholds}

\slides{
- Active variables: $X(\tau) = \left\{ i \mid \left| \frac{\text{d}\theta_i}{\text{d}\tau} \right| \geq \varepsilon \right\}$
- Activation occurs when uncertainty gradients exceed resolution threshold
- Configuration changes manifest as parameter threshold crossings
}

\notes{Variables become active when uncertainty gradients about their associated configuration aspects exceed the resolution threshold,
$$
X(\tau) = \left\{ i \mid \left| \frac{\text{d}\theta_i}{\text{d}\tau} \right| \geq \varepsilon \right\}, \quad M(\tau) = Z \setminus X(\tau).
$$
This activation represents the point where uncertainty about particular configuration aspects becomes resolvable and can drive further uncertainty resolution.}

\subsubsection{Information Geometry of Uncertainty Evolution}

\slides{
- Fisher matrix partitioning reflects uncertainty structure
- $G_{XX}$: resolvable uncertainty geometry  
- $G_{MM}$: latent uncertainty reservoir
- $G_{XM}$: coupling between resolved and unresolved uncertainty
}

\notes{The Fisher Information Matrix partitions according to uncertainty resolvability,
$$
G(\boldsymbol{\theta}) = 
\begin{bmatrix} 
G_{XX} & G_{XM} \\ 
G_{MX} & G_{MM} 
\end{bmatrix},
$$
where $G_{XX}$ describes the geometry of resolvable uncertainty, $G_{MM}$ the structure of the latent uncertainty reservoir, and $G_{XM}$ the coupling between resolved and unresolved aspects. This partitioning governs how uncertainty resolution propagates through the configuration space.}

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

\notes{At points where the latent-to-active flow functional is locally extremal (e.g., $\frac{\text{d} \boldsymbol{\theta}_M}{\text{d}\tau} \approx 0 $), the system may exhibit critical slowing where information resevoir variables are slow relative to active variables. It may be possible to separate the system entropy into active variables and, $I = S[\rho_X]$ and "intrinsic information" $J= S[\rho_{X|M}]$ allowing us to create an information analogous to  B. Roy Frieden's extreme physical information (@Frieden-physics98) which allows derivation of locally valid differential equations that depend on the *information topography*.}


\endif
