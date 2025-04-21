\ifndef{jaynesGradientFlow}
\define{jaynesGradientFlow}

\editme

\subsection{Dynamical System}

\notes{Consider a dynamical system governed by the equation,
$$
\dot{\boldsymbol{\theta}}_i = 
\begin{cases}
-[G(\boldsymbol{\theta})\boldsymbol{\theta}]_i & \text{if } |[G(\boldsymbol{\theta})\boldsymbol{\theta}]_i| \geq \varepsilon \\
0 & \text{otherwise}
\end{cases}
$$
where $\boldsymbol{\theta} \in \mathbb{R}^n$ represents the natural parameters of an exponential family distribution $\rho_\theta$, $G(\boldsymbol{\theta})$ is the Fisher information matrix with elements
$$
G_{ij}(\boldsymbol{\theta}) = \mathbb{E}_{\rho_\theta}\left[\frac{\partial \log \rho_\theta}{\partial \theta_i}\frac{\partial \log \rho_\theta}{\partial \theta_j}\right]
$$
and $\varepsilon$ is the resolution threshold that determines when a parameter component becomes dynamically active. This system describes the steepest ascent in the entropy of the distribution $\rho_\theta$, constrained to the manifold of exponential family distributions and subject to the resolution constraint. Unlike natural gradient descent, which optimizes a cost function, this system maximizes the entropy of the underlying configuration governed by the exponential family distribution or density matrix, but only for components that exceed the resolution threshold.}

\subsection{Entropy Bounds and Compactness}

\notes{Recall that the entropy of the system is bounded such that,
$$
0 \leq S[\rho_\theta] \leq N
$$
where $S[\rho_\theta] = -\mathbb{E}_{\rho_\theta}[\log \rho_\theta]$ is the entropy functional, and $N$ represents the maximum possible entropy value for the system. These bounds create a compact manifold in the space of distributions, which constrains the parameter evolution.}

\subsection{Resolution Constraints}

\notes{The system exhibits a minimum resolution constraint, formulated as an uncertainty relation between parameters $\boldsymbol{\theta}$ and their conjugate variables (the gradients)
$$
\Delta\theta_i \cdot \Delta(\nabla_{\theta_i}) \geq \frac{c}{2},
$$
where $c$ is a constant representing the minimum resolution of the system. This constraint imposes limits on the precision with which parameters can be simultaneously specified with their conjugate variables.}

\notes{The resolution threshold $\varepsilon$ is directly related to this uncertainty principle, determining when a gradient component becomes dynamically resolvable. Components with gradient magnitudes below $\varepsilon$ remain fixed, creating effective discontinuities in the otherwise smooth geometry of the system. This quantization of the dynamics is a fundamental feature of the resolution-constrained entropy formulation.}

\subsection{Relationship Between Resolution Threshold and Entropy Bound}

\notes{The resolution threshold $\varepsilon$ and the entropy bound $N$ are fundamentally connected through the information capacity of the system. As shown in the resolution-constrained entropy formulation, there exists a relationship:
$$
\varepsilon(N) \geq \frac{L}{e^{N/d}},
$$
where $L$ is a characteristic length scale of the system and $d$ is the dimensionality of the parameter space.}

\notes{This relationship reveals a fundamental trade-off: as the entropy bound $N$ increases, the resolution threshold $\varepsilon$ decreases, allowing the system to resolve finer details. Conversely, a lower entropy bound results in a higher resolution threshold, forcing the system to operate at a coarser scale.}

\notes{This trade-off has important implications for the system's dynamics. A system with a high entropy bound can evolve more continuously, with smaller incremental changes. A system with a low entropy bound, however, must evolve in larger, discrete steps, as it can only respond to gradients that exceed the higher resolution threshold.}

\notes{This connection between entropy and resolution provides a natural explanation for the emergence of discrete structure from continuous underlying dynamics. As the system's entropy increases, its ability to resolve fine details improves, leading to the gradual emergence of more complex structure.}

\section{Multi-Scale Dynamics and Parameter Separation}

\subsection{Parameter Partitioning}

\notes{The parameter vector $\boldsymbol{\theta}$ can be partitioned into two subsets

- $\boldsymbol{\theta}_M$: Parameters with gradients below the resolution threshold (slow-moving)
- $\boldsymbol{\theta}_X$: Parameters with resolvable gradients (fast-moving)}

\notes{The Fisher information matrix can also be partitioned
$$
G(\boldsymbol{\theta}) = \begin{bmatrix} G_{XX} & G_{XM} \\ G_{MX} & G_{MM} \end{bmatrix}
$$
where elements falling below $\varepsilon^2$ are effectively treated as zero in the dynamics, reflecting the resolution constraint on the system's ability to resolve fine-grained structure.}

\subsection{Schur Complement Analysis}

\notes{
The Schur complement of $G_{MM}$ in $G(\boldsymbol{\theta})$ is defined as
$$
G^\prime_X = G_{XX} - G_{XM}G_{MM}^{-1}G_{MX}
$$
This matrix $G^\prime_X$ represents the effective information geometry for the fast parameters after accounting for their coupling to the slow parameters. It yields a dynamical equation for the fast parameters,
$$\dot{\boldsymbol{\theta}}_X = -G^\prime_X\boldsymbol{\theta}_X + \text{correction terms}
$$
The Schur complement provides a framework for analyzing how resolution constraints create a natural separation of time scales in the system's evolution.
}

\subsection{Sparsification Through Entropy Maximization}

\notes{*speculative* 

As the system evolves to maximize entropy, it should move toward states where parameters become more statistically independent, as minimising mutual information between variables reduces the joint entropy. Any tendency toward independence during entropy maximization would cause the Fisher information matrix $G(\boldsymbol{\theta})$ to trend toward a more diagonal structure over time, as off-diagonal elements represent statistical correlations between parameters.}

\section{Action Functional Representation}

\subsection{Action Definition}

\notes{The dynamics of the system can be derived from an action functional
$$
A[\gamma] = \int_0^1 \dot{\gamma}(t)^T G(\gamma(t)) \dot{\gamma}(t) \, \text{d}t,
$$
where $\gamma(t)$ represents a path through parameter space.}

\subsection{Variational Analysis}

\notes{For the path that minimizes this action, the first variation must vanish,
$$
\left. \frac{\text{d}}{\text{d}\epsilon} A[\gamma + \epsilon \eta] \right|_{\epsilon=0} = 0,
$$
where $\eta(t)$ is an arbitrary function with $\eta(0) = \eta(1) = 0$.}

\notes{Through variational calculus we recover the Euler-Lagrange equation,
$$
\frac{\text{d}}{\text{d}t}(G(\gamma)\dot{\gamma}) = \frac{1}{2} \dot{\gamma}^T \frac{\partial G}{\partial \gamma} \dot{\gamma}
$$}

\subsection{Time Parameterization}

\notes{To recover the original dynamical equation, we introduce the time parameterization,
$$
\frac{\text{d}\tau}{\text{d}t} = \frac{1}{\boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta}}
$$}

\notes{Under this parameterization, the Euler-Lagrange equation simplifies to our original dynamics. To prove this, we start with the parameterized path $\gamma(t) = \boldsymbol{\theta}(\tau(t))$, which gives
$$
\dot{\gamma} = \frac{\text{d}\boldsymbol{\theta}}{\text{d}\tau} \frac{\text{d}\tau}{\text{d}t}.
$$
Substituting this into the Euler-Lagrange equation and applying our specific parameterization,
$$
\frac{\text{d}}{\text{d}t}(G(\gamma)\dot{\gamma}) = \frac{\text{d}}{\text{d}t}\left(G(\boldsymbol{\theta})\frac{\text{d}\boldsymbol{\theta}}{\text{d}\tau}\frac{\text{d}\tau}{\text{d}t}\right) = \frac{1}{2} \dot{\gamma}^\top \frac{\partial G}{\partial \gamma} \dot{\gamma}
$$}

\notes{With our choice of $\frac{\text{d}\tau}{\text{d}t} = \frac{1}{\boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta}}$ and after algebraic manipulation, this reduces to
$$
\frac{\text{d}\boldsymbol{\theta}}{\text{d}\tau} = -G(\boldsymbol{\theta})\boldsymbol{\theta}
$$
and so our original dynamical equation when expressed in terms of the *system time* $\tau$ confirming that our action functional correctly generates the original dynamics.}

\subsection{Information-Geometric Interpretation of Time Parameterization}

\notes{The time parameterization can be rewritten by recognizing that $G(\boldsymbol{\theta})\boldsymbol{\theta} = -\nabla_\boldsymbol{\theta} S[\rho_\theta]$, the negative gradient of entropy with respect to the parameters
$$
\frac{\text{d}\tau}{\text{d}t} = \frac{1}{\boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta}} = \frac{1}{-\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}]}.
$$
The inverse relation is
$$
\frac{\text{d}t}{\text{d}\tau} = \boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta} = -\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}]
$$
which expresses the rate at which parameterized time flows relative to system time as the directional derivative of entropy along the parameter vector. It measures the entropy production rate of the system in the direction of the current parameter vector.}

\section{Information-Theoretic Interpretation}

\subsection{Entropy Maximization}

\notes{The dynamical system describes the steepest ascent path in entropy space, constrained by the structure of the density matrix representation. As parameters evolve according to $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}$, we expect the system to move toward states of increasing statistical independence, which generally correspond to higher entropy configurations.}

\subsection{Information Flow and Topography}

\notes{The equation $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}$ can be interpreted as an information flow equation, where the product $G(\boldsymbol{\theta})\boldsymbol{\theta}$ represents an information current that indicates how information propagates through the parameter space as the system evolves. Under this interpretation the Fisher information matrix represents the *information topography*.}

\subsection{Resolution and Uncertainty}

\notes{The resolution constraints introduce uncertainty relations into the classical statistical framework. These constraints alter the convergence properties of the entropy maximization process, creating bounds on information extraction and parameter precision.}

\subsection{Temporal Information Dynamics}

\notes{The time parameterization reveals that the flow of time in the system is connected to information processing efficiency

1. In regions where parameters are strongly aligned with entropy change (high $\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}]$), parameterized time flows rapidly relative to system time.

2. In regions where parameters are weakly coupled to entropy change (low $\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}]$), parameterized time flows slowly.

3. At critical points where parameters become orthogonal to the entropy gradient ($\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}] \approx 0$), the time parameterization approaches singularity indicating phase transitions in the system's information structure.}

\section{Connections to Physical Theories}

\subsection{Frieden's Extreme Physical Information}

\notes{Our framework connects to Frieden's Extreme Physical Information (EPI) principle, which posits that physical systems evolve to extremize the physical information $I = K - J$, where $K$ represents the observed Fisher information and $J$ represents the intrinsic or bound information.}

\notes{@Frieden-physics98 demonstrated that fundamental laws of physics, including relativistic ones, can emerge from the EPI principle. This suggests our information-geometric framework is capable of describing a rich set of underlying "physics".}

\subsection{Conclusion}

\notes{Viewing the dynamical system from the gradient flow $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}$ provides a framework for understanding parameter evolution. By reformulating this system in terms of an action functional and analysing its behaviour through the Schur complement, we gain insights into the multi-scale nature of information flow in complex statistical systems.}

\notes{The time parameterisation that connects the action to the original dynamics reveals how the system's evolution adjusts to information content, moving slowly through information-rich regions while rapidly traversing information-sparse areas. This establishes a connection between information flow and temporal dynamics.}

\endif
