\ifndef{jaynesGradientFlow}
\define{jaynesGradientFlow

\editme

\subsection{Dynamical System}

\notes{Consider a dynamical system governed by the equation,
$$
\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta},
$$
where $\theta \in \mathbb{R}^n$ represents the natural parameters of an exponential family distribution $\rho_\theta$, and $G(\theta)$ is the Fisher information matrix with elements:
$$
G_{ij}(\theta) = \mathbb{E}_{\rho_\theta}\left[\frac{\partial \log \rho_\theta}{\partial \theta_i}\frac{\partial \log \rho_\theta}{\partial \theta_j}\right]
$$
This system describes the steepest ascent in the entropy of the distribution $\rho_\theta$, constrained to the manifold of exponential family distributions. Unlike natural gradient descent, which optimizes a cost function, this system maximizes the entropy of the underlying configuration governed by the exponential family distribution or density matrix.}

\subsection{Entropy Bounds and Compactness}

\notes{Recall that the entropy of the system is bounded such that,
$$
0 \leq S[\rho_\theta] \leq N
$$
where $S[\rho_\theta] = -\mathbb{E}_{\rho_\theta}[\log \rho_\theta]$ is the entropy functional, and $N$ represents the maximum possible entropy value for the system. These bounds create a compact manifold in the space of distributions, which constrains the parameter evolution.}

\subsection{Resolution Constraints}

\notes{The system exhibits a minimum resolution constraint, formulated as an uncertainty relation between parameters $\theta$ and their conjugate variables (the gradients)
$$
\Delta\theta_i \cdot \Delta(\nabla_{\theta_i}) \geq \frac{c}{2},
$$
where $c$ is a constant representing the minimum resolution of the system. This constraint imposes limits on the precision with which parameters can be simultaneously specified with their conjugate variables.}

\section{Multi-Scale Dynamics and Parameter Separation}

\subsection{Parameter Partitioning}

The parameter vector $\boldsymbol{\theta}$ can be partitioned into two subsets

- $\boldsymbol{\theta}_M$: Parameters with gradients below the resolution threshold (slow-moving)
- $\boldsymbol{\theta}_X$: Parameters with resolvable gradients (fast-moving)

The Fisher information matrix can also be partitioned
$$
G(\boldsymbol{\theta}) = \begin{bmatrix} G_{XX} & G_{XM} \\ G_{MX} & G_{MM} \end{bmatrix}
$$

\subsection{Schur Complement Analysis}

The Schur complement of $G_{MM}$ in $G(\theta)$ is defined as:
$$
G^\prime_X = G_{XX} - G_{XM}G_{MM}^{-1}G_{MX}
$$
This matrix $G^\prime_X$ represents the effective information geometry for the fast parameters after accounting for their coupling to the slow parameters. It yields a dynamical equation for the fast parameters,
$$\dot{\boldsymbol{\theta}}_X = -G^\prime_X\boldsymbol{\theta}_X + \text{correction terms}
$$
The Schur complement provides a framework for analyzing how resolution constraints create a natural separation of time scales in the system's evolution.

\subsection{Sparsification Through Entropy Maximization}

*speculative* 

As the system evolves to maximize entropy, it should move toward states where parameters become more statistically independent, as minimising mutual information between variables reduces the joint entropy. Any tendency toward independence during entropy maximization would cause the Fisher information matrix $G(\theta)$ to trend toward a more diagonal structure over time, as off-diagonal elements represent statistical correlations between parameters.

\section{Action Functional Representation}

\subsection{Action Definition}

The dynamics of the system can be derived from an action functional:
$$
A[\gamma] = \int_0^1 \dot{\gamma}(t)^T G(\gamma(t)) \dot{\gamma}(t) \, \text{d}t,
$$
where $\gamma(t)$ represents a path through parameter space.

\subsection{Variational Analysis}

For the path that minimizes this action, the first variation must vanish,
$$
\left. \frac{d}{d\epsilon} A[\gamma + \epsilon \eta] \right|_{\epsilon=0} = 0,
$$
where $\eta(t)$ is an arbitrary function with $\eta(0) = \eta(1) = 0$.

Through variational calculus, this leads to the Euler-Lagrange equation,
$$
\frac{\text{d}}{\text{d}t}(G(\gamma)\dot{\gamma}) = \frac{1}{2} \dot{\gamma}^T \frac{\partial G}{\partial \gamma} \dot{\gamma}
$$

\subsection{Time Parameterization}

To recover the original dynamical equation, we introduce the time parameterization:
$$
\frac{\text{d}\tau}{\text{d}t} = \frac{1}{\boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta}}
$$

Under this parameterization, the Euler-Lagrange equation simplifies to our original dynamics. To prove this, we start with the parameterized path $\gamma(t) = \theta(\tau(t))$, which gives
$$
\dot{\gamma} = \frac{\text{d}\theta}{\text{d}\tau} \frac{\text{d}\tau}{\text{d}t}.
$$
Substituting this into the Euler-Lagrange equation and applying our specific parameterization,
$$
\frac{\text{d}}{\text{d}t}(G(\gamma)\dot{\gamma}) = \frac{\text{d}}{\text{d}t}\left(G(\boldsymbol{\theta})\frac{\text{d}\theta}{\text{d}\tau}\frac{\text{d}\tau}{\text{d}t}\right) = \frac{1}{2} \dot{\gamma}^\top \frac{\partial G}{\partial \gamma} \dot{\gamma}
$$

With our choice of $\frac{\text{d}\tau}{\text{d}t} = \frac{1}{\boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta}}$ and after algebraic manipulation, this reduces to
$$
\frac{\text{d}\theta}{\text{d}\tau} = -G(\boldsymbol{\theta})\boldsymbol{\theta}
$$
and so our original dynamical equation when expressed in terms of the *system time* $\tau$ confirming that our action functional correctly generates the original dynamics.

\subsection{Information-Geometric Interpretation of Time Parameterization}

The time parameterization can be rewritten in a revealing form by recognizing that $G(\theta)\theta = -\nabla_\theta S[\rho_\theta]$, the negative gradient of entropy with respect to the parameters:
$$
\frac{\text{d}\tau}{\text{d}t} = \frac{1}{\boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta}} = \frac{1}{-\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}]}
$$
Consequently, the inverse relation is
$$
\frac{\text{d}t}{\text{d}\tau} = \boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta} = -\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}]
$$
which expresses the rate at which parameterized time flows relative to system time as the directional derivative of entropy along the parameter vector. It measures the entropy production rate of the system in the direction of the current parameter vector.

\section{Information-Theoretic Interpretation}

\subsection{Entropy Maximization}

The dynamical system describes the steepest ascent path in entropy space, constrained by the structure of the density matrix representation. As parameters evolve according to $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}$, we expect the system to move toward states of increasing statistical independence, which generally correspond to higher entropy configurations.

\subsection{Information Flow and Topography}

The equation $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}$ can be interpreted as an information flow equation, where the product $G(\boldsymbol{\theta})\boldsymbol{\theta}$ represents an information current that indicates how information propagates through the parameter space as the system evolves. Under this interpretation the Fisher information matrix represents the *information topography*.

\subsection{Resolution and Uncertainty}

The resolution constraints introduce uncertainty relations into the classical statistical framework. These constraints alter the convergence properties of the entropy maximization process, creating bounds on information extraction and parameter precision.

\subsection{Temporal Information Dynamics}

The time parameterization reveals that the flow of time in the system is connected to information processing efficiency:

1. In regions where parameters are strongly aligned with entropy change (high $\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}]$), parameterized time flows rapidly relative to system time.

2. In regions where parameters are weakly coupled to entropy change (low $\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}]$), parameterized time flows slowly.

3. At critical points where parameters become orthogonal to the entropy gradient ($\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta} S[\rho_\boldsymbol{\theta}] \approx 0$), the time parameterization approaches singularity indicating phase transitions in the system's information structure.

\section{Connections to Physical Theories}

\subsection{Frieden's Extreme Physical Information}

Our framework connects to Frieden's Extreme Physical Information (EPI) principle, which posits that physical systems evolve to extremize the physical information $I = K - J$, where $K$ represents the observed Fisher information and $J$ represents the intrinsic or bound information.

Frieden demonstrated that fundamental laws of physics, including relativistic ones, can emerge from the EPI principle. This suggests our information-geometric framework is capable of describing a rich set of underlying "physics".

\subsection{Conclusion}

Viewing the dynamical system from the gradient flow $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}$ provides a framework for understanding parameter evolution. By reformulating this system in terms of an action functional and analysing its behaviour through the Schur complement, we gain insights into the multi-scale nature of information flow in complex statistical systems.

The time parameterisation that connects the action to the original dynamics reveals how the system's evolution adjusts to information content, moving slowly through information-rich regions while rapidly traversing information-sparse areas. This establishes a connection between information flow and temporal dynamics.

\endif
