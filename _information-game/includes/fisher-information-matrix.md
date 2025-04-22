\ifndef{fisherInformationMatrix}
\define{fisherInformationMatrix}

\editme

\subsection{Fisher Information Matrix}

\notes{The Fisher Information Matrix (FIM) is a fundamental object in information geometry that characterizes the local curvature of the statistical manifold. For an exponential family distribution $\rho_\theta$ with natural parameters $\boldsymbol{\theta}$, the FIM is defined as
$$
G_{ij}(\boldsymbol{\theta}) = \mathbb{E}_{\rho_\theta}\left[\frac{\partial \log \rho_\theta}{\partial \theta_i}\frac{\partial \log \rho_\theta}{\partial \theta_j}\right]
$$
This matrix encodes the sensitivity of the distribution to changes in the parameters and provides a natural metric on the parameter space.}

\notes{The FIM can be expressed in terms of the cumulant generating function $\psi(\boldsymbol{\theta}) = \log Z(\boldsymbol{\theta})$:
$$
G_{ij}(\boldsymbol{\theta}) = \frac{\partial^2 A(\boldsymbol{\theta})}{\partial \theta_i \partial \theta_j}
$$
This formulation highlights the connection between the FIM and the curvature of the entropy landscape.}

\notes{The resolution-constrained Fisher Information Matrix (rcFIM) extends the standard FIM by incorporating resolution thresholds for observables. The rcFIM is defined as
$$
G_{ij}^\varepsilon(\boldsymbol{\theta}) = \begin{cases}
G_{ij}(\boldsymbol{\theta}) & \text{if } |\langle H_i \rangle - \langle H_i \rangle_0| \geq \varepsilon_1 \text{ or } \mathrm{var}(H_i) \geq \varepsilon_2 \\
0 & \text{otherwise}
\end{cases}
$$
where $\varepsilon_1$ and $\varepsilon_2$ are resolution thresholds for the expectation and variance of observables, respectively.}

\notes{The rcFIM partitions the parameter space into active and latent subspaces based on the resolution thresholds. Parameters associated with active observables contribute to the rcFIM, while parameters associated with latent observables do not. This partitioning reflects the discrete nature of observable activation and provides a mechanism for managing the system's complexity.}

\notes{The Schur complement of the rcFIM with respect to the latent parameters provides an effective information geometry for the active observables,
$$
G_X^\varepsilon(\boldsymbol{\theta}) = G_{XX}^\varepsilon(\boldsymbol{\theta}) - G_{XM}^\varepsilon(\boldsymbol{\theta})(G_{MM}^\varepsilon(\boldsymbol{\theta}))^{-1}G_{MX}^\varepsilon(\boldsymbol{\theta}),
$$
where $G_{XX}^\varepsilon$, $G_{MM}^\varepsilon$, $G_{XM}^\varepsilon$, and $G_{MX}^\varepsilon$ are the blocks of the rcFIM corresponding to active and latent parameters.}

\notes{The rcFIM determines the resolution-constrained gradient flow. The evolution of the system is governed by
$$
\dot{\boldsymbol{\theta}} = -G^\varepsilon(\boldsymbol{\theta})\boldsymbol{\theta}
$$
This equation ensures that only active observables contribute to the system's dynamics, while latent observables remain fixed.}

\notes{The eigenvalues of the rcFIM provide insights into the system's information geometry. Large eigenvalues correspond to directions in parameter space where the system is highly sensitive to changes, while small eigenvalues correspond to directions where the system is relatively insensitive. The resolution threshold $\varepsilon$ determines which eigenvalues are considered significant, effectively defining the dimensionality of the active subspace.}

\notes{The rcFIM also has important implications for the system's computational complexity. By focusing on active observables and treating latent observables as fixed, the system can evolve in a reduced parameter space. This sparsification of the dynamics is a natural consequence of the resolution constraint and provides a mechanism for managing computational complexity in large-scale systems.}

\notes{Understanding the rcFIM allows us to predict the system's evolution and identify the most likely paths of emergence. It also provides insights into the relationship between information geometry and physical dynamics, suggesting that the resolution constraint might be a fundamental feature of information-based physical systems.}

\endif 
