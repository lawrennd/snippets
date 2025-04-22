\ifndef{jaynesGradientFlow}
\define{jaynesGradientFlow}

\editme

\subsection{Dynamical System}

\notes{Consider a dynamical system governed by the resolution-constrained gradient flow,
$$
\dot{\boldsymbol{\theta}}_i = 
\begin{cases}
-[G^\varepsilon(\boldsymbol{\theta})\boldsymbol{\theta}]_i & \text{if } |\langle H_i \rangle - \langle H_i \rangle_0| \geq \varepsilon_1 \text{ or } \mathrm{var}(H_i) \geq \varepsilon_2 \\
0 & \text{otherwise}
\end{cases}
$$
where $\boldsymbol{\theta} \in \mathbb{R}^n$ represents the natural parameters of an exponential family distribution $\rho_\theta$, $G^\varepsilon(\boldsymbol{\theta})$ is the resolution-constrained Fisher Information Matrix (rcFIM), and $\varepsilon_1$ and $\varepsilon_2$ are resolution thresholds for observable expectations and variances. This system describes the steepest ascent in the entropy of the distribution $\rho_\theta$, constrained to the manifold of exponential family distributions and subject to the resolution constraint.}

\notes{The rcFIM is defined as
$$
G_{ij}^\varepsilon(\boldsymbol{\theta}) = \begin{cases}
G_{ij}(\boldsymbol{\theta}) & \text{if } |\langle H_i \rangle - \langle H_i \rangle_0| \geq \varepsilon_1 \text{ or } \mathrm{var}(H_i) \geq \varepsilon_2 \\
0 & \text{otherwise}
\end{cases}
$$
where $G_{ij}(\boldsymbol{\theta})$ is the standard Fisher Information Matrix. This formulation ensures that only observables that exceed the resolution thresholds contribute to the system's dynamics.}

\subsection{Entropy Bounds and Compactness}

\notes{Recall that the entropy of the system is bounded such that,
$$
0 \leq S[\rho_\theta] \leq N
$$
where $S[\rho_\theta] = -\mathbb{E}_{\rho_\theta}[\log \rho_\theta]$ is the entropy functional, and $N$ represents the maximum possible entropy value for the system. These bounds create a compact manifold in the space of distributions, which constrains the parameter evolution.}

\subsection{Resolution Constraints}

\notes{The system exhibits resolution constraints on observable expectations and variances,
$$
|\langle H_i \rangle - \langle H_i \rangle_0| \geq \varepsilon_1 \text{ or } \mathrm{var}(H_i) \geq \varepsilon_2,
$$
where $\varepsilon_1$ and $\varepsilon_2$ are thresholds that determine when an observable becomes dynamically resolvable. This constraint imposes limits on the precision with which observables can be resolved.}

\notes{The resolution thresholds are related to the information capacity of the system. As shown in the resolution-constrained entropy formulation, there's a relationship,
$$
\varepsilon_1(N) \geq \frac{\ell_1}{e^{N/d}}, \quad \varepsilon_2(N) \geq \frac{\ell_2}{e^{N/d}},
$$
where $\ell_1$ and $\ell_2$ are characteristic length scales of the system and $d$ is the dimensionality of the parameter space.}

\notes{This relationship suggests a trade-off: as the entropy bound $N$ increases, the system can distinguish between more states, even though the resolution thresholds themselves remain constant. A higher entropy bound allows the system to encode more information, which can be used to resolve finer details in the observable space.}

\subsection{Relationship Between Resolution Threshold and Entropy Bound}

\notes{The resolution thresholds $\varepsilon_1$ and $\varepsilon_2$ and the entropy bound $N$ are connected through the information capacity of the system. As the entropy bound increases, the resolution thresholds decrease, allowing for the detection of more subtle features in the system.}

\notes{This trade-off has important implications for system dynamics. A system with a high entropy bound evolves more continuously, with smaller incremental changes in observable expectations and variances. A system with a low entropy bound, however, must evolve in larger, discrete steps: it can only respond to changes in observables that exceed the resolution thresholds.}

\notes{The connection between entropy and resolution provides an explanation for the emergence of discrete structure from continuous underlying dynamics. The resolution thresholds act as natural coarse-graining scales, determining the minimum size of changes in observables that the system can respond to.}

\section{Multi-Scale Dynamics and Observable Separation}

\subsection{Observable Partitioning}

\notes{The observables $\{H_i\}$ can be partitioned into two subsets:

- $\{H_M\}$: Observables with expectations and variances below the resolution thresholds (latent)
- $\{H_X\}$: Observables with resolvable expectations or variances (active)}

\notes{The Fisher information matrix can also be partitioned
$$
G(\boldsymbol{\theta}) = \begin{bmatrix} G_{XX} & G_{XM} \\ G_{MX} & G_{MM} \end{bmatrix}
$$
where elements falling below the resolution thresholds are treated as zero in the dynamics, reflecting the resolution constraint on the system's ability to resolve fine-grained structure.}

\subsection{Schur Complement Analysis}

\notes{
The Schur complement of $G_{MM}$ in $G(\boldsymbol{\theta})$ is defined as
$$
G^\prime_X = G_{XX} - G_{XM}G_{MM}^{-1}G_{MX}
$$
This matrix $G^\prime_X$ represents the effective information geometry for the active observables after accounting for their coupling to the latent observables. It yields a dynamical equation for the active parameters,
$$\dot{\boldsymbol{\theta}}_X = -G^\prime_X\boldsymbol{\theta}_X + \text{correction terms}
$$
The Schur complement provides a framework for analyzing how resolution constraints create a natural separation of time scales in the system's evolution.
}

\subsection{Sparsification Through Entropy Maximization}

\notes{As the system evolves to maximize entropy, it should move toward states where observables become more statistically independent, as minimizing mutual information between variables reduces the joint entropy. Any tendency toward independence during entropy maximization would cause the Fisher information matrix $G(\boldsymbol{\theta})$ to trend toward a more diagonal structure over time, as off-diagonal elements represent statistical correlations between observables.}

\subsection{Action Functional Representation}

\notes{The resolution-constrained dynamics can be formulated in terms of an action functional. Within a region where the set of active observables remains constant (no activations or deactivations), we can use the standard action functional for gradient flow:
$$
\mathcal{A}[\boldsymbol{\theta}(t)] = \int_{t_0}^{t_1} \text{d}t \, \left( \frac{1}{2} \dot{\boldsymbol{\theta}}^\top G(\boldsymbol{\theta}) \dot{\boldsymbol{\theta}} + \boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta} \right).
$$}

\notes{For the path that minimizes this action, the first variation must vanish,
$$
\left. \frac{d}{d\epsilon} \mathcal{A}[\boldsymbol{\theta} + \epsilon \eta] \right|_{\epsilon=0} = 0,
$$
where $\eta(t)$ is an arbitrary function with $\eta(t_0) = \eta(t_1) = 0$.}

\notes{Through variational calculus we recover the Euler-Lagrange equation,
$$
\frac{d}{dt}(G(\boldsymbol{\theta})\dot{\boldsymbol{\theta}}) = \frac{1}{2} \dot{\boldsymbol{\theta}}^\top \frac{\partial G}{\partial \boldsymbol{\theta}} \dot{\boldsymbol{\theta}}
$$}

\notes{To recover the original dynamical equation, we introduce the time parameterization,
$$
\frac{\text{d}\tau}{\text{d}t} = \frac{1}{\boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta}}
$$}

\notes{Under this parameterization, the Euler-Lagrange equation simplifies to our original dynamics
$$
\frac{\text{d}\boldsymbol{\theta}}{\text{d}\tau} = -G(\boldsymbol{\theta})\boldsymbol{\theta}.
$$}

\notes{This establishes the connection between the action functional and the original dynamics within a region where the set of active observables remains constant.}

\notes{To incorporate the resolution constraint across the entire parameter space, we can modify the action functional to include a penalty term that enforces the threshold condition,
$$
\mathcal{A}_\varepsilon[\boldsymbol{\theta}(t)] = \int_{t_0}^{t_1} \text{d}t \, \left( \frac{1}{2} \dot{\boldsymbol{\theta}}^\top G(\boldsymbol{\theta}) \dot{\boldsymbol{\theta}} + \boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta} + \sum_i \lambda_i(t) \left( |\langle H_i \rangle - \langle H_i \rangle_0| - \varepsilon_1 \right) \Theta\left( \varepsilon_1 - |\langle H_i \rangle - \langle H_i \rangle_0| \right) + \sum_i \mu_i(t) \left( \mathrm{var}(H_i) - \varepsilon_2 \right) \Theta\left( \varepsilon_2 - \mathrm{var}(H_i) \right) \right),
$$
where $\lambda_i(t)$ and $\mu_i(t)$ are Lagrange multipliers and $\Theta(x)$ is the Heaviside step function.}

\notes{This modified action functional introduces a non-smooth term that creates discontinuities in the dynamics. The Lagrange multipliers $\lambda_i(t)$ and $\mu_i(t)$ enforce the constraint that observables with expectations and variances below the resolution thresholds remain fixed, while the Heaviside function $\Theta(x)$ ensures that the penalty only applies when the constraint is violated.}

\notes{The resulting Euler-Lagrange equations yield the resolution-constrained gradient flow,
$$
\dot{\boldsymbol{\theta}}_i = 
\begin{cases}
-[G^\varepsilon(\boldsymbol{\theta})\boldsymbol{\theta}]_i & \text{if } |\langle H_i \rangle - \langle H_i \rangle_0| \geq \varepsilon_1 \text{ or } \mathrm{var}(H_i) \geq \varepsilon_2 \\
0 & \text{otherwise}.
\end{cases}
$$}

\notes{This formulation reveals that the resolution constraint alters the nature of the system's evolution. Rather than following a continuous path of steepest ascent, the system follows a piecewise trajectory, with discrete jumps occurring when observables cross the resolution thresholds.}

\subsection{Computational Implications}

\notes{The resolution-constrained dynamics have important implications for the computational aspects of the system. The discrete, quantized nature of the evolution suggests that the system can be efficiently simulated using event-driven algorithms, where updates occur only when observables cross the resolution thresholds.}

\notes{This approach is well-suited for systems with a large number of observables, as it allows for selective updating of only the active observables, reducing computational complexity. The resolution thresholds act as natural sparsification mechanisms, focusing computational resources on the most significant aspects of the system dynamics.}

\subsection{Emergence of Time}

\notes{The discrete, quantized nature of the resolution-constrained dynamics suggests a novel perspective on the emergence of time. In this framework, time is not a continuous parameter but emerges from the sequence of discrete events where observables cross the resolution thresholds.}

\notes{Each activation event, where an observable becomes dynamically active, represents a discrete "tick" of the system's internal clock. The flow of time is thus quantized, with the system evolving in discrete steps rather than continuously. This quantization of time is a direct consequence of the resolution constraint, which prevents the system from responding to infinitesimally small changes in observables.}

\subsection{Information Geometry and Resolution Constraints}

\notes{The resolution constraint alters the geometry of the observable space, creating effective discontinuities in the otherwise smooth Riemannian geometry defined by the Fisher Information Matrix.}

\notes{In standard information geometry, the parameter space is a smooth Riemannian manifold, with the Fisher Information Matrix $G(\boldsymbol{\theta})$ defining the metric tensor. The geodesics of this manifold represent the paths of steepest ascent in the entropy landscape.}

\notes{However, the resolution constraint introduces a "quantized" geometry, where the observable space is effectively divided into regions based on whether observables are above or below the resolution thresholds. The boundaries between these regions represent the activation thresholds, where observables become dynamically active.}

\notes{This quantized geometry has important implications for the system's evolution. Rather than following smooth geodesics, the system follows piecewise trajectories, with discrete jumps occurring at the activation thresholds. These jumps represent the emergence of new structure, as observables become dynamically active and the system's dimensionality increases.}

\notes{The relationship between the entropy bound $N$ and the resolution thresholds $\varepsilon_1$ and $\varepsilon_2$ affects the geometry of the observable space. As the entropy bound increases, the resolution thresholds decrease, leading to a finer-grained quantization of the geometry. This suggests that systems with higher entropy bounds might exhibit more complex geometric structure, with more activation thresholds and thus more opportunities for the emergence of new structure.}

\notes{Understanding this quantized geometry is crucial for predicting the system's evolution and identifying the most likely paths of emergence. It also provides insights into the relationship between information geometry and physical dynamics, suggesting that the resolution constraint might be a fundamental feature of information-based physical systems.}

\section{Information-Theoretic Interpretation}

\subsection{Entropy Maximization}

\notes{The dynamical system describes the steepest ascent path in entropy space, constrained by the structure of the density matrix representation. As parameters evolve according to $\dot{\boldsymbol{\theta}} = -G^\varepsilon(\boldsymbol{\theta})\boldsymbol{\theta}$, we expect the system to move toward states of increasing statistical independence, which generally correspond to higher entropy configurations.}

\subsection{Information Flow and Topography}

\notes{The equation $\dot{\boldsymbol{\theta}} = -G^\varepsilon(\boldsymbol{\theta})\boldsymbol{\theta}$ can be interpreted as an information flow equation, where the product $G^\varepsilon(\boldsymbol{\theta})\boldsymbol{\theta}$ represents an information current that indicates how information propagates through the observable space as the system evolves. Under this interpretation the Fisher information matrix represents the *information topography*.}

\subsection{Resolution and Uncertainty}

\notes{The resolution constraints introduce uncertainty relations into the classical statistical framework. These constraints alter the convergence properties of the entropy maximization process, creating bounds on information extraction and observable precision.}

\subsection{Temporal Information Dynamics}

\notes{The time parameterization reveals that the flow of time in the system is connected to information processing efficiency

1. In regions where observables are strongly aligned with entropy change (high $\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}]$), parameterized time flows rapidly relative to system time.

2. In regions where observables are weakly coupled to entropy change (low $\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}]$), parameterized time flows slowly.

3. At critical points where observables become orthogonal to the entropy gradient ($\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}] \approx 0$), the time parameterization approaches singularity indicating phase transitions in the system's information structure.}

\section{Connections to Physical Theories}

\subsection{Frieden's Extreme Physical Information}

\notes{Our framework connects to Frieden's Extreme Physical Information (EPI) principle, which posits that physical systems evolve to extremize the physical information $I = K - J$, where $K$ represents the observed Fisher information and $J$ represents the intrinsic or bound information.}

\notes{@Frieden-physics98 demonstrated that fundamental laws of physics, including relativistic ones, can emerge from the EPI principle. This suggests our information-geometric framework is capable of describing a rich set of underlying "physics".}

\subsection{Conclusion}

\notes{Viewing the dynamical system from the gradient flow $\dot{\boldsymbol{\theta}} = -G^\varepsilon(\boldsymbol{\theta})\boldsymbol{\theta}$ provides a framework for understanding parameter evolution. By reformulating this system in terms of an action functional and analysing its behaviour through the Schur complement, we gain insights into the multi-scale nature of information flow in complex statistical systems.}

\notes{The time parameterisation that connects the action to the original dynamics reveals how the system's evolution adjusts to information content, moving slowly through information-rich regions while rapidly traversing information-sparse areas. This establishes a connection between information flow and temporal dynamics.}

\endif
