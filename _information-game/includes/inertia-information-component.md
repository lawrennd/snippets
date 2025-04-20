\ifndef{informationInertiaComponent}
\define{informationInertiaComponent}

\editme

\section{Information Inertia: Memory-Based Dynamics in Maximum Entropy Systems}

\slides{
* Inertial properties emerge from information reservoirs
* Temporal structure creates memory effects through mutual information
* Classical conservation laws arise naturally from information geometry
}

\notes{The maximum entropy game reveals how inertial properties can emerge within information-theoretic systems. By partitioning the system into temporal components, we can see how Markovian independencies emerge.}

\subsection{Temporal Partitioning of Information Space}

\slides{
* Partition variables into: past/present ($X_0$), future ($X_1$), and latent ($M$)
* Joint entropy decomposes via conditional mutual information
* Information flow diagram reveals memory structure
}

\notes{We partition the system variables into three components:}
$$
\begin{aligned}
X_0 &: \text{Past and present active variables} \\
X_1 &: \text{Future active variables} \\
M &: \text{Latent information reservoir}
\end{aligned}
$$

\notes{The joint entropy of this system can be decomposed as
$$
S(X_0, X_1, M) = S(X_0) + S(X_1|X_0,M) + S(M|X_0) - I(X_1;M|X_0)
$$
where $I(X_1; M | X_0)$ is the conditional mutual information between future states, $X_1$, and the latent resevoir, $M$ given past states $X_0$. This term quantifies the information carried forward in time beyond what's determined by the current observable state—the essence of inertial memory.}

\subsection{Inertia as Conditional Mutual Information}

\slides{
* Inertial mass: $M_{\text{inertial}} \sim I(X_1;M|X_0)$
* Resistance to change encoded in information coupling
* Explains persistence without invoking material properties
}

\newslide{Fisher Information Decomposition}

\notes{In the density matrix formulation with Fisher Information Matrix $G(\boldsymbol{\theta})$, the inertial properties are expressed by  in the coupling blocks between temporal partitions,}
$$
G = \begin{pmatrix}
G_{X_0X_0} & G_{X_0M} & G_{X_0X_1} \\
G_{MX_0} & G_{MM} & G_{MX_1} \\
G_{X_1X_0} & G_{X_1M} & G_{X_1X_1}
\end{pmatrix}
$$

\newslide{Conditional Mutual Information}

\notes{The coupling is captured primarily by $G_{X_1M}$, which determines how future states are influenced by the latent reservoir. This gives rise to the conditional mutual information term,}
$$
M_{\text{inertial}} \sim I(X_1;M|X_0)
$$

\notes{This explains why objects appear to maintain their state of motion: the latent variables $M$ store information that constrains future states $X_1$ beyond what's determined by current observables $X_0$. The larger the conditional mutual information, the greater the system's resistance to changes in motion—exactly what we observe as inertial mass.}

\subsection{Entropy Gradient Dynamics with Memory}

\slides{
* System evolves via: $\frac{\text{d}\boldsymbol{\theta}}{\text{d}\tau} = -G(\boldsymbol{\theta})\boldsymbol{\theta}$
* Inertial term: $G_{X_1M}\boldsymbol{\theta}_M$ couples future to latent reservoir
* Creates persistent trajectories resembling Newton's laws
}

\notes{For a system evolving via entropy gradient ascent according to
$$
\frac{\text{d}\boldsymbol{\theta}}{\text{d}t} = G(\boldsymbol{\theta})\boldsymbol{\theta}
$$
the dynamics of future variables are governed by
$$
\frac{\text{d}\boldsymbol{\theta}_{X_1}}{\text{d}\tau} = G_{X_1X_0}\boldsymbol{\theta}_{X_0} + G_{X_1M}\boldsymbol{\theta}_{M} + G_{X_1X_1}\boldsymbol{\theta}_{X_1}
$$
from which we can identify three distinct contributions,
$$
\begin{aligned}
G_{X_1X_0}\boldsymbol{\theta}_{X_0} &: \text{Direct causal influence (position-dependent forces)} \\
G_{X_1M}\boldsymbol{\theta}_{M} &: \text{Inertial influence (momentum-like persistence)} \\
G_{X_1X_1}\boldsymbol{\theta}_{X_1} &: \text{Self-interaction (potential energy terms)}
\end{aligned}
$$
}

\notes{In the classical limit of the maximum entropy game, the entropic gradient dynamics formalise into precise analogues of Newton's equations. Specifically, when we decompose the dynamics of future variables:}
$$
\frac{\text{d}\boldsymbol{\theta}_{X_1}}{\text{d}\tau} = G_{X_1X_0}\boldsymbol{\theta}_{X_0} + G_{X_1M}\boldsymbol{\theta}_{M} + G_{X_1X_1}\boldsymbol{\theta}_{X_1}
$$

\notes{The term $G_{X_1M}\boldsymbol{\theta}_{M}$ acts functionally as an inertial term because:}
$$
\boldsymbol{\theta}_{M} \approx \int_{\tau_0}^{\tau} G_{MX_0}(t)\boldsymbol{\theta}_{X_0}(t) \text{d}t
$$

\notes{This integral form captures the accumulated history of the system's past states, weighted by their information-geometric coupling. When $G_{X_1M}$ has specific symmetry properties (particularly translation invariance), this term becomes precisely equivalent to momentum in classical mechanics. The persistence of motion emerges because the latent parameters $\boldsymbol{\theta}_M$ encode the time-integrated information flow from past states, effectively serving as a statistical momentum that resists change.}

\subsection{Conservation Laws from Critical Slowing of Latent Variables}

\slides{
* Conservation emerges from invariance of conditional mutual information
* Critical slowing of latent variables creates information invariants 
* Noether-like correspondence between symmetry and conservation
}

\notes{We can understand the conservation law from the critical slowing of latent variables $M$. When these variables evolve much more slowly than the active variables $X$ (i.e., when $|[G(\boldsymbol{\theta})\boldsymbol{\theta}]_M| < \varepsilon_{\text{slow}} \ll 1$), we assume that the conditional mutual information $I(X_1;M|X_0)$ becomes approximately invariant over time,}
$$
\frac{\text{d}}{\text{d}t}I(X_1;M|X_0) \approx 0.
$$
\notes{This invariance is the information-theoretic foundation of the system's conservation laws. The critically slowed latent variables act as an information reservoir that constrains future states in a consistent way across time, creating effective constants of motion.}

\notes{Let $G(\boldsymbol{\theta})$ be the Fisher Information Matrix and consider a continuous transformation $\boldsymbol{\theta} \mapsto \boldsymbol{\theta} + \epsilon \boldsymbol{\delta}$ that leaves the entropy dynamics invariant. Then there exists a corresponding conserved quantity $Q$ such that $\frac{\text{d}Q}{\text{d}t} = 0$ along entropic gradient flows.}

\notes{Specifically:}

\notes{1. *Linear Momentum Conservation*: When the Fisher geometry is invariant under spatial translations ($\boldsymbol{\theta}_X \mapsto \boldsymbol{\theta}_X + \boldsymbol{a}$), the corresponding conserved quantity is,}
$$
\boldsymbol{p} = G_{MX}\boldsymbol{\theta}_X + G_{MM}\boldsymbol{\theta}_M
$$

\notes{Where this quantity satisfies $\frac{\text{d}\boldsymbol{p}}{\text{d}\tau} = 0$ in the absence of external information gradients.}

\notes{2. *Angular Momentum Conservation*: When the Fisher geometry is invariant under rotations ($\boldsymbol{\theta} \mapsto R\boldsymbol{\theta}$ where $R$ is a rotation operator), the conserved quantity takes the form:}
$$
\boldsymbol{L} = \boldsymbol{\theta}_X \times (G_{MX}\boldsymbol{\theta}_X + G_{MM}\boldsymbol{\theta}_M)
$$

\notes{3. *Energy Conservation*: When the system's dynamics are time-translation invariant, the conserved quantity is:}
$$
E = \frac{1}{2}\boldsymbol{\theta}_M^\top G_{MM} \boldsymbol{\theta}_M + V(\boldsymbol{\theta}_X)
$$

\notes{Where $V(\boldsymbol{\theta}_X)$ represents the potential information defined by the curvature of the entropy landscape.}

\notes{These conservation laws can be derived from the conditional mutual information through the relationship:}
$$
\frac{\text{d}}{\text{d}\tau}I(X_1;M|X_0) = 0
$$

\notes{When this condition holds under specific symmetry transformations. This is analogous to Noether's theorem in physics, but derived from information-theoretic principles where conservation emerges from the structure of the Fisher geometry rather than being imposed as physical law.}​​​​​​​​​​​​​​​​

\subsection{Connecting to Fisher Information Geometry}

\slides{
* Fisher Information Matrix encodes the inertial tensor
* Off-diagonal terms create coupling across time
* Effective Lagrangian emerges from information flow
}

\notes{The connection to the Fisher Information Matrix reveals how inertia emerges geometrically. As the system unfolds, the Fisher matrix $G(\boldsymbol{\theta})$ acquires structure in its off-diagonal components, particularly between different temporal scales. This creates an effective Lagrangian-like structure where}
$$
\mathcal{L}_{\text{eff}} \sim \boldsymbol{\theta}_X^\top G_{XX} \boldsymbol{\theta}_X - V(\boldsymbol{\theta})
$$

\notes{The variational principle identified in Jaynes' world}
$$
\delta \int_{t_i}^{t_{i+1}} \boldsymbol{\theta}_{X_i}^\top G_{X_i X_i} \boldsymbol{\theta}_{X_i} \, \text{d}t = 0
$$

\notes{Takes the form of a principle of least action when interpreted through the temporal partitioning, giving rise to effective equations of motion that preserve information across time. The inertial properties emerge as statistical patterns in how information geometry evolves, stabilizing into recognizable macroscopic laws of motion.}

\notes{In our system he resistance to change that characterises inertial systems is an expression of how information persists and propagates through the Fisher geometry of maximum entropy systems.}

\subsection{Connecting to Fisher Information Geometry}

\slides{
* Fisher Information Matrix encodes the inertial tensor
* Off-diagonal terms create coupling across time
* Effective Lagrangian emerges from information flow
}

\notes{The connection to the Fisher Information Matrix reveals how inertia emerges geometrically. As the system unfolds, the Fisher matrix $G(\boldsymbol{\theta})$ acquires structure in its off-diagonal components, particularly between different temporal scales. This creates an effective Lagrangian-like structure where:}
$$
\mathcal{L}_{\text{eff}} \sim \boldsymbol{\theta}_X^\top G_{XX} \boldsymbol{\theta}_X - V(\boldsymbol{\theta})
$$

\notes{The variational principle identified in Jaynes' World,}
$$
\delta \int_{t_i}^{t_{i+1}} \boldsymbol{\theta}_{X_i}^\top G_{X_i X_i} \boldsymbol{\theta}_{X_i} \, \text{d}t = 0
$$

\notes{Takes the form of a principle of least action when interpreted through the temporal partitioning, giving rise to effective equations of motion that preserve information across time. The inertial properties emerge as statistical patterns in how information geometry evolves, stabilizing into recognizable macroscopic laws of motion.}

\notes{This demonstration shows how inertia—one of the most fundamental properties of physical systems—can be understood purely in terms of information flow and entropy dynamics, without requiring additional physical postulates. The resistance to change that characterizes inertial systems is ultimately an expression of how information persists and propagates through the Fisher geometry of maximum entropy systems.}

\endif
