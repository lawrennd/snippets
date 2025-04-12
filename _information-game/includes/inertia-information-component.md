\ifndef{informationInertiaComponent}
\define{informationInertiaComponent}

\editme

\section{Information Inertia: Memory-Based Dynamics in Maximum Entropy Systems}

\slides{
* Inertial properties emerge from information reservoirs
* Temporal structure creates memory effects through mutual information
* Classical conservation laws arise naturally from information geometry
}

\notes{The maximum entropy game reveals how inertial properties can emerge within information-theoretic systems. By partitioning the system into temporal components, we can see how classical physics-like behaviors emerge without imposed external laws.}

\subsection{Temporal Partitioning of Information Space}

\slides{
* Partition variables into: past/present ($X_0$), future ($X_1$), and latent ($M$)
* Joint entropy decomposes via conditional mutual information
* Information flow diagram reveals memory structure
}

\notes{To understand inertia in information-theoretic terms, we partition the system variables into three components:}
$$
\begin{aligned}
X_0 &: \text{Past and present active variables} \\
X_1 &: \text{Future active variables} \\
M &: \text{Latent information reservoir}
\end{aligned}
$$

\notes{The joint entropy of this system can be decomposed as:}
$$
S(X_0, X_1, M) = S(X_0) + S(X_1|X_0,M) + S(M|X_0) - I(X_1;M|X_0)
$$

\notes{This decomposition reveals a crucial term: $I(X_1;M|X_0)$, the conditional mutual information between future states and the latent reservoir, given the past. This term quantifies precisely the information carried forward in time beyond what's determined by the current observable state—the essence of inertial memory.}

\subsection{Inertia as Conditional Mutual Information}

\slides{
* Inertial mass: $M_{\text{inertial}} \sim I(X_1;M|X_0)$
* Resistance to change encoded in information coupling
* Explains persistence without invoking material properties
}

\notes{In the density matrix formulation with Fisher Information Matrix $G(\boldsymbol{\theta})$, the inertial properties manifest in the coupling blocks between temporal partitions:}
$$
G = \begin{pmatrix}
G_{X_0X_0} & G_{X_0M} & G_{X_0X_1} \\
G_{MX_0} & G_{MM} & G_{MX_1} \\
G_{X_1X_0} & G_{X_1M} & G_{X_1X_1}
\end{pmatrix}
$$

\notes{The inertial coupling is captured primarily by $G_{X_1M}$, which determines how future states are influenced by the latent reservoir. This gives rise to the effective inertial mass:}
$$
M_{\text{inertial}} \sim I(X_1;M|X_0)
$$

\notes{This formulation explains why objects appear to maintain their state of motion: the latent variables $M$ store information that constrains future states $X_1$ beyond what's determined by current observables $X_0$. The larger the conditional mutual information, the greater the system's resistance to changes in motion—exactly what we observe as inertial mass.}

\subsection{Entropy Gradient Dynamics with Memory}

\slides{
* System evolves via: $\frac{d\boldsymbol{\theta}}{dt} = G(\boldsymbol{\theta})\boldsymbol{\theta}$
* Inertial term: $G_{X_1M}\boldsymbol{\theta}_M$ couples future to latent reservoir
* Creates persistent trajectories resembling Newton's laws
}

\notes{For a system evolving via entropy gradient ascent according to:}
$$
\frac{d\boldsymbol{\theta}}{dt} = G(\boldsymbol{\theta})\boldsymbol{\theta}
$$

\notes{The dynamics of future variables are governed by:}
$$
\frac{d\boldsymbol{\theta}_{X_1}}{dt} = G_{X_1X_0}\boldsymbol{\theta}_{X_0} + G_{X_1M}\boldsymbol{\theta}_{M} + G_{X_1X_1}\boldsymbol{\theta}_{X_1}
$$

\notes{Here we can identify three distinct contributions:}
$$
\begin{aligned}
G_{X_1X_0}\boldsymbol{\theta}_{X_0} &: \text{Direct causal influence (position-dependent forces)} \\
G_{X_1M}\boldsymbol{\theta}_{M} &: \text{Inertial influence (momentum-like persistence)} \\
G_{X_1X_1}\boldsymbol{\theta}_{X_1} &: \text{Self-interaction (potential energy terms)}
\end{aligned}
$$

\notes{As the system approaches the classical regime described in Jaynes' World, these terms stabilize into recognizable forms that mirror Newton's laws of motion. The inertial term $G_{X_1M}\boldsymbol{\theta}_{M}$ ensures that objects in motion tend to stay in motion, not because of material properties, but because information about their trajectory is stored in the latent reservoir $M$ and influences future states.}



\subsection{Conservation Laws from Information Structure}

\slides{
* Linear momentum: Information preserved in translational modes
* Angular momentum: Information preserved in rotational couplings
* Conservation arises from conditional mutual information invariants
}

\notes{The framework explains why certain quantities appear conserved in classical systems. Conservation laws emerge when the conditional mutual information $I(X_1;M|X_0)$ maintains invariant structures during system evolution. For example:}

\notes{1. **Linear Momentum Conservation**: When the conditional mutual information between future position and latent velocity variables remains constant during free evolution.}

\notes{2. **Angular Momentum Conservation**: When the conditional mutual information preserves rotational coupling information between spatial coordinates.}

\notes{3. **Energy Conservation**: When the total information content distributed between active and latent variables remains constant during evolution.}

\notes{These conservation principles are not imposed externally but emerge naturally from the structure of information flow in the maximum entropy game. The conditional mutual information $I(X_1;M|X_0)$ cannot be created or destroyed—only transferred between subsystems—creating the appearance of conservation laws.}

\subsection{Connecting to Fisher Information Geometry}

\slides{
* Fisher Information Matrix encodes the inertial tensor
* Off-diagonal terms create coupling across time
* Effective Lagrangian emerges from information flow
}

\notes{The connection to the Fisher Information Matrix reveals how inertia emerges geometrically. As the system unfolds, the Fisher matrix $G(\boldsymbol{\theta})$ acquires structure in its off-diagonal components, particularly between different temporal scales. This creates an effective Lagrangian-like structure where:}
$$
\mathcal{L}_{\text{eff}} \sim \boldsymbol{\theta}_X^T G_{XX} \boldsymbol{\theta}_X - V(\boldsymbol{\theta})
$$

\notes{The variational principle identified in Jaynes' World:}
$$
\delta \int_{\tau_i}^{\tau_{i+1}} \boldsymbol{\theta}_{X_i}^T G_{X_i X_i} \boldsymbol{\theta}_{X_i} \, d\tau = 0
$$

\notes{Takes the form of a principle of least action when interpreted through the temporal partitioning, giving rise to effective equations of motion that preserve information across time. The inertial properties emerge as statistical patterns in how information geometry evolves, stabilizing into recognizable macroscopic laws of motion.}

\notes{This demonstration shows how inertia—one of the most fundamental properties of physical systems—can be understood purely in terms of information flow and entropy dynamics, without requiring additional physical postulates. The resistance to change that characterizes inertial systems is ultimately an expression of how information persists and propagates through the Fisher geometry of maximum entropy systems.}

\endif
