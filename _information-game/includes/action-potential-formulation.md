\ifndef{actionPotentialFormulation}
\define{actionPotentialFormulation}

\subsection{Action Potential Formulation}

\notes{The dynamical evolution of Jaynes' World can be formulated through an action principle, where the system follows paths that extremize an action functional. This formulation provides a rigorous connection between the entropy maximization principle and the system's evolution.}

\slides{
* Action functional:
  * $\mathcal{A}[\boldsymbol{\theta}(t)] = \int_{t_0}^{t_1} \text{d}t \, \left( \frac{1}{2} \dot{\boldsymbol{\theta}}^\top G(\boldsymbol{\theta}) \dot{\boldsymbol{\theta}} - V(\boldsymbol{\theta}) \right)$
* Potential function:
  * $V(\boldsymbol{\theta}) = -\boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta}$
}

\notes{The action functional takes the standard form of kinetic energy minus potential energy. The kinetic term $\frac{1}{2} \dot{\boldsymbol{\theta}}^\top G(\boldsymbol{\theta}) \dot{\boldsymbol{\theta}}$ represents the cost of rapid parameter changes, weighted by the Fisher information metric. The potential function $V(\boldsymbol{\theta}) = -\boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta}$ captures the drive toward higher entropy, with the negative sign ensuring entropy increase.}

\subsection{Euler-Lagrange Equations}

\slides{
* Euler-Lagrange equations:
  * $\frac{\text{d}}{\text{d}t}\left(\frac{\partial L}{\partial \dot{\boldsymbol{\theta}}}\right) - \frac{\partial L}{\partial \boldsymbol{\theta}} = 0$
* Lagrangian:
  * $L = \frac{1}{2} \dot{\boldsymbol{\theta}}^\top G(\boldsymbol{\theta}) \dot{\boldsymbol{\theta}} + \boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \boldsymbol{\theta}$
}

\notes{The Euler-Lagrange equations derived from this action principle yield second-order differential equations that describe the system's evolution. Under appropriate time parameterization, these equations reduce to the first-order gradient flow equations that maximize entropy. This time parameterization emerges naturally from the variational principle, rather than being imposed ad hoc.}

\subsection{Connection to Entropy Gradient}

\slides{
* Entropy gradient:
  * $\nabla S[\rho] = -G(\boldsymbol{\theta}) \boldsymbol{\theta}$
* Matches potential gradient:
  * $\nabla V(\boldsymbol{\theta}) = -G(\boldsymbol{\theta}) \boldsymbol{\theta}$
}

\notes{The gradient of the potential function exactly matches the entropy gradient, establishing a direct connection between the variational principle and entropy maximization. This formulation provides a rigorous foundation for understanding how the system evolves toward higher entropy states while respecting the constraints of information geometry.}

\endif 