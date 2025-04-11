\ifndef{variableActivationMechanism}
\define{variableActivationMechanism}

\subsection{Variable Activation and Basis Update}

\notes{As the system ascends the entropy landscape, the curvature becomes increasingly asymmetric. When the entropy gradient along a particular direction surpasses a threshold, that direction becomes dynamically resolvable — a variable activates.}

\subsubsection{Threshold Crossing and Activation}

We define a variable activation event as the point where the $i$-th component of the entropy gradient reaches order unity,
$$
\left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \geq \varepsilon_{\text{activate}}.
$$
Here $\varepsilon_{\text{activate}}$ defines a threshold above which the system can resolve variation in the $i$-th direction with sufficient information gain. This marks a transition from latent to emergent status.

When this happens, the corresponding parameter $\theta_i$ becomes an active degree of freedom, and the associated observable $H_i$ becomes internally resolvable. The system's effective observable basis $\{H_i\}$ is updated — either by extension or rotation — to reflect the newly emergent structure.

\subsubsection{Basis Update Mechanism}

This update is not arbitrary. The new basis must remain consistent with the information geometry — that is, the Fisher matrix $G(\boldsymbol{\theta})$ must remain positive definite and aligned with the updated entropy gradients. One may think of this as a local frame adaptation: the system reorganizes its observables to align with the current information flow.

Given an existing set of active observables $\{H_1, \dots, H_k\}$ and a newly activated direction $\theta_{k+1}$, we seek a corresponding observable $H_{k+1}$ such that it aligns with the updated gradient,
$$
\left.\nabla_{\boldsymbol{\theta}} S[\rho]\right|_{\theta_{k+1}} = G(\boldsymbol{\theta}) \boldsymbol{\theta} \propto H_{k+1},
$$
it preserves orthogonality (uncorrelatedness) under the current state,
$$
\mathrm{Cov}(H_{k+1}, H_j) = 0 \quad \text{for all } j \leq k,
$$
and it is consistent with the curvature structure,
$$
H_{k+1} \in \operatorname{span}\left\{ \frac{\partial \rho}{\partial \theta_i} \right\} \quad \text{evaluated near } \boldsymbol{\theta}_0.
$$

\subsubsection{Consequences for System Geometry}

This leads to a piecewise unfolding of structure. Within each phase, a subset of variables is active and governs dynamics. When a new variable activates:
- The dimensionality of the effective system increases
- Each activation increases entropy
- The geometry reorganizes curvature
- The system's trajectory shifts

Over time, this defines a staged emergence process, in which new variables appear sequentially as the system climbs through successive regions of increasing entropy and asymmetry. The basis $\{H_i\}$ is thus not globally fixed, but emerges dynamically as a function of the internal information landscape.

\subsection{Phase Transitions and Piecewise Geometric Flow}

As each variable activates, the system enters a new phase — a locally adapted region of parameter space where the information geometry is governed by an updated basis of observables. These phases are separated by *activation thresholds*, and each new phase introduces a change in the effective dimensionality of the system.

We describe the system's evolution as a *piecewise geodesic flow*: within each phase, the system follows a smooth trajectory along the entropy gradient,
$$
\frac{\text{d}\boldsymbol{\theta}}{\text{d}t} \propto G(\boldsymbol{\theta}) \boldsymbol{\theta},
$$
where the geometry is defined by the active subset of the Fisher Information Matrix. When a new variable activates, this geometry shifts, and the trajectory continues in a new locally adapted space.

Each activated variable contributes additional curvature to the system: the effective Fisher matrix $G$ becomes larger and more structured, and the entropy gradient sharpens. In this way, the unfolding process is cumulative — earlier activations condition the geometry for future ones.

The transition between phases is *not singular*. Because the entropy and curvature remain finite, transitions are continuous but directionally abrupt: a sharp increase in curvature along a particular axis marks a change in the dominant flow direction. These are analogous to *critical points* in phase transitions, where the system reorganizes around a new informational axis.

Thus, the system explores parameter space via a sequence of transitions, first *Latent phase* in $\mathcal{D}_0$, where all variables are suppressed,second *activation threshold*, where one direction becomes resolvable, third *emergence phase**, where the active geometry reorients and extends, and finally *new latent subspace**, until the next threshold is reached.

This process generates a *history-dependent trajectory*: the current configuration of active variables shapes the available paths forward. Each phase embeds memory of past activations in the form of accumulated curvature and entropy.

The result is a path-dependent unfolding of structure — the system builds its geometry piece by piece, guided by internal information gradients, without requiring pre-defined coordinates or external intervention.

\endif 