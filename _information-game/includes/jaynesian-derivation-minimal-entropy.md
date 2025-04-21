\ifndef{jaynesianDerivationMinimalEntropy}
\define{jaynesianDerivationMinimalEntropy}

\editme

\subsection{Jaynesian Derivation of Minimal Entropy Configuration}

\slides{
- Assign density matrix maximally noncommittal with respect to missing information
- Adapt Jaynes' maximum entropy principle to derive minimum entropy configuration
- Assume zero initial entropy bounded by $N$ bits
}
\notes{Jaynes suggested that statistical mechanics problems should be treated as problems of inference. Assign the probability distribution (or density matrix) that is maximally noncommittal with respect to missing information, subject to known constraints.}

\notes{While Jaynes applied this idea to derive the *maximum entropy* configuration given constraints, here we adapt it to derive the *minimum entropy* configuration, under an assumption of zero initial entropy bounded by a maximum entropy of $N$ bits.}

\newslide{Minimizing Von Neumann Entropy}
\slides{
- Minimize $S[\rho] = -\mathrm{tr}(\rho \log \rho)$
- Subject to constraints encoding resolution bounds
- System begins in minimal entropy state
- State cannot be delta function (must obey resolution constraint $\varepsilon$)
- Entropy bounded above by $N$ bits: $S[\rho] \leq N$
}

\notes{Let $\rho$ be a density matrix describing the state of a system. The von Neumann entropy is,
$$
S[\rho] = -\mathrm{tr}(\rho \log \rho),
$$
we wish to *minimize* $S[\rho]$, subject to constraints that encode the resolution bounds.}

\notes{In the game we assume that the system begins in a state of minimal entropy, the state cannot be a delta function (no singularities, so it must obey a resolution constraint $\varepsilon$) and the entropy is bounded above by $N$ bits: $S[\rho] \leq N$.}

\notes{We apply a variational principle where we minimise
$$
S[\rho] = -\mathrm{tr}(\rho \log \rho)
$$
subject to constraints.}

\subsubsection{Constraints}
\slides{
- Normalization: $\mathrm{tr}(\rho) = 1$
- Resolution constraint: $\mathrm{tr}(\rho \hat{Z}^2) \geq \epsilon^2$
- Optional dual-space constraint: $\mathrm{tr}(\rho \hat{P}^2) \geq \delta^2$
- These ensure system has finite resolution
}
\notes{1. The first constraint is normalization, $\mathrm{tr}(\rho) = 1$.}

\notes{2. The resolution constraint is motivated by the entropy being constrained to be, 
$$
S[\rho] \leq N
$$
with the bound saturated only when the system is at maximum entropy. This implies that the system is finite in resolution. To reflect this we introduce a resolution constraint, $\mathrm{tr}(\rho \hat{Z}^2) \geq \epsilon^2$. And/or $\mathrm{tr}(\rho \hat{P}^2) \geq \delta^2$, and other optional moment or dual-space constraints.}


\newslide{Lagrangian Formulation}
\slides{
- Lagrangian with Lagrange multipliers:
  $$
  \mathcal{L}[\rho] = -\mathrm{tr}(\rho \log \rho)
  + \lambda_0 (\mathrm{tr}(\rho) - 1)
  - \lambda_x (\mathrm{tr}(\rho \hat{Z}^2) - \epsilon^2)
  - \lambda_p (\mathrm{tr}(\rho \hat{P}^2) - \delta^2)
  $$
}
\notes{We introduce Lagrange multipliers $\lambda_0$, $\lambda_z$, $\lambda_p$ for these constraints and define the Lagrangian
$$
\mathcal{L}[\rho] = -\mathrm{tr}(\rho \log \rho)
+ \lambda_0 (\mathrm{tr}(\rho) - 1)
- \lambda_x (\mathrm{tr}(\rho \hat{Z}^2) - \epsilon^2)
- \lambda_p (\mathrm{tr}(\rho \hat{P}^2) - \delta^2).
$$}


\newslide{Solution: Gaussian State}
\slides{
- Functional derivative: $\frac{\delta \mathcal{L}}{\delta \rho} = -\log \rho - 1 - \lambda_x \hat{Z}^2 - \lambda_p \hat{P}^2 + \lambda_0 = 0$
- Solution: $\rho = \frac{1}{Z} \exp\left(-\lambda_z \hat{Z}^2 - \lambda_p \hat{P}^2\right)$
- Partition function: $Z = \mathrm{tr}\left[\exp\left(-\lambda_z \hat{Z}^2 - \lambda_p \hat{P}^2\right)\right]$
- Results in a Gaussian state for density matrix
}
\notes{To find the extremum, we take the functional derivative and set it to zero,
$$
\frac{\delta \mathcal{L}}{\delta \rho} = -\log \rho - 1 - \lambda_x \hat{Z}^2 - \lambda_p \hat{P}^2 + \lambda_0 = 0
$$
and solving for $\rho$ gives
$$
\rho = \frac{1}{Z} \exp\left(-\lambda_z \hat{Z}^2 - \lambda_p \hat{P}^2\right)
$$
where the partition function (which ensures normalisation) is
$$
Z = \mathrm{tr}\left[\exp\left(-\lambda_z \hat{Z}^2 - \lambda_p \hat{P}^2\right)\right]
$$
This is a Gaussian state for a density matrix, which is consistent with the minimum entropy distribution under uncertainty constraints.}

\newslide{Natural Parameters and Fisher Information}
\slides{
- Lagrange multipliers define natural parameters: $\theta_z = -\lambda_z$, $\theta_p = -\lambda_p$
- Exponential family form: $\rho(\boldsymbol{\theta}) \propto \exp(\boldsymbol{\theta} \cdot \mathbf{H})$
- Fisher Information: $G(\boldsymbol{\theta})$ from second derivative of $\log Z(\boldsymbol{\theta})$
- Steepest ascent in $\boldsymbol{\theta}$ space traces entropy dynamics
}
\notes{The Lagrange multipliers $\lambda_z, \lambda_p$ enforce lower bounds on variance. These define the natural parameters as $\theta_z = -\lambda_z$ and $\theta_p = -\lambda_p$ in the exponential family form $\rho(\boldsymbol{\theta}) \propto \exp(\boldsymbol{\theta} \cdot \mathbf{H})$. The form of $\rho$ is a density matrix. The curvature (second derivative) of $\log Z(\boldsymbol{\theta})$ gives the Fisher Information matrix $G(\boldsymbol{\theta})$. Steepest ascent trajectories in $\boldsymbol{\theta}$ space will trace the system's entropy dynamics.}


\newslide{Information Geometry and Uncertainty}
\slides{
- Verify $\left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \right| < \varepsilon$ for all $i$
- Non-commuting observables: $[H_i, H_j] \neq 0$
- Uncertainty relation: $\mathrm{Var}(H_i) \cdot \mathrm{Var}(H_j) \geq C > 0$
- Bounded curvature: $\mathrm{tr}(G(\boldsymbol{\theta})) \geq \gamma > 0$
}
\notes{Next we compute $G(\boldsymbol{\theta})$ from $\log Z(\boldsymbol{\theta})$ to explore the information geometry. From this we should verify that the following conditions hold,
$$
\left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \right| < \varepsilon \quad \text{for all } i
$$
which implies that all variables remain latent at initialization.}

\notes{The Hermitians have a *non-commuting observable pair* constraint,
$$
  [H_i, H_j] \neq 0,
$$
which is equivalent to an *uncertainty relation*,
$$
  \mathrm{Var}(H_i) \cdot \mathrm{Var}(H_j) \geq C > 0,
$$
and ensures that we have *bounded curvature*
$$
\mathrm{tr}(G(\boldsymbol{\theta})) \geq \gamma > 0.
$$}


\newslide{Initial State and Landscape Unfolding}
\slides{
- Initial density matrix: $\rho(\boldsymbol{\theta}_o)$
- Permissible curvature geometry: $G(\boldsymbol{\theta}_o)$
- Constraint-consistent basis of observables $\{H_i\}$ with quadratic form
- System begins in regular, latent, low-entropy state
- From here entropy ascent and symmetry-breaking transitions emerge
}

\notes{We can then use $\varepsilon$ and $N$ to define initial thresholds and maximum resolution and examine how variables decouple and how saddle-like regions emerge as the landscape unfolds through gradient ascent.}

\notes{This constrained minimization problem yields the *structure of the initial density matrix* $\rho(\boldsymbol{\theta}_o)$ and the *permissible curvature geometry* $G(\boldsymbol{\theta}_o)$ and a constraint-consistent basis of observables $\{H_i\}$ that have a quadratic form. This ensures the system begins in a *regular, latent, low-entropy state*.}

\notes{This is the configuration from which entropy ascent and symmetry-breaking transitions emerge.}

\subsection{Latent and Active Variables}

\notes{As the system evolves, variables transition from latent to active states. The boundary between these states is defined by the resolution threshold $\varepsilon$.}

\newslide{Transition from Latent to Active}
\slides{
- Variables remain latent when $\left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \right| < \varepsilon$
- Variables become active when $\left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \right| \geq \varepsilon$
- At the threshold: $\left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \right| = \varepsilon$
- This defines the boundary between latent and active variables
}
\notes{The condition $\left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \right| < \varepsilon$ defines the latent region where variables remain unresolved. As the system evolves, some variables may cross the threshold $\varepsilon$, becoming active and contributing to the system's dynamics.}

\notes{At the exact threshold $\left| \left[G(\boldsymbol{\theta}) \boldsymbol{\theta}\right]_i \right| = \varepsilon$, variables are at the boundary between latent and active states. This critical point is where the wave equation emerges.}

\subsection{Wave Equation Emergence from Information Geometry}

\notes{We now examine the special case of the system's origin — the latent region $\mathcal{D}_0$ — where no variables have yet activated, and the geometry is defined purely in terms of the latent information structure over the proto-coordinates $M$.}

\notes{In this phase, the system is critically slowed: the entropy gradient $G(\boldsymbol{\theta}) \boldsymbol{\theta}$ remains uniformly suppressed, and the dynamics are governed by equilibrium-like conditions that define the structure of the minimal-entropy state.}

\newslide{Wave Equation in Latent Space}
\slides{
- Express density matrix in terms of wavefunction: $\psi(m) = \sqrt{p(m)}$
- Fisher information constraint: $G = 4\int \left|\frac{d\psi(m)}{dm}\right|^2 \text{d}m = \varepsilon^2$
- Euler-Lagrange equation: $-\frac{\text{d}^2\psi(m)}{\text{d}m^2} + V(m)\psi(m) = \mu\psi(m)$
- Optimal wavefunction is Gaussian: $\psi(m) = \left(\frac{\alpha}{\pi}\right)^{1/4}e^{-\alpha m^2/2}$
}
\notes{For analytical tractability, we express the density matrix in terms of a wavefunction $\psi(m) = \sqrt{p(m)}$, which transforms the Fisher information constraint to
$$
G = 4\int \left|\frac{d\psi(m)}{dm}\right|^2 \text{d}m = \varepsilon^2.
$$}

\notes{Taking the functional derivative of our Lagrangian with respect to $\psi$ and setting it equal to zero yields the Euler-Lagrange equation
$$
-\frac{\text{d}^2\psi(m)}{\text{d}m^2} + V(m)\psi(m) = \mu\psi(m),
$$
where the potential function $V(m)$ and eigenvalue $\mu$ are determined by the constraints.}

\notes{For minimum entropy solutions at fixed Fisher information, we showed above that the optimal wavefunction has a Gaussian form,
$$
\psi(m) = \left(\frac{\alpha}{\pi}\right)^{1/4}e^{-\alpha m^2/2},
$$
where $\alpha$ is determined by the Fisher information constraint
$$
4\int \left|\frac{\text{d}\psi(m)}{\text{d}m}\right|^2 \text{d}m = 4\alpha = \varepsilon^2
$$
which gives us $\alpha = \varepsilon^2/4$.}

\newslide{Quadratic Potential and Schrödinger-Type Equation}
\slides{
- Potential function: $V(m) = \lambda m^2$
- Time-independent Schrödinger equation: $-\frac{\text{d}^2\psi(m)}{\text{d}m^2} + \lambda m^2 \psi(m) = \mu \psi(m)$
- Wave-like equation emerges from information constraints
- Represents optimal balance between localization and uncertainty
}
\notes{Substituting this solution back into our variational formulation and comparing with the standard form of the wave equation, we derive:
$$
V(m) = \lambda m^2
$$
where $\lambda$ is a positive constant related to the Lagrange multiplier and resolution parameter. This confirms that the potential is quadratic, arising directly from the condition of minimum entropy under exact Fisher information constraint.}

\notes{The resulting equation is
$$
-\frac{\text{d}^2\psi(m)}{\text{d}m^2} + \lambda m^2 \psi(m) = \mu \psi(m)
$$
which has the form of a time-independent Schrödinger equation for a harmonic oscillator.}

\notes{This wave-like equation emerges from the system's requirements to minimize entropy while maintaining exact resolution constraints. The system seeks the flattest possible entropy configuration under bounded resolution. The ground state of this condition is formally equivalent to a Gaussian wavefunction, satisfying a local second-order differential equation.}

\notes{The quadratic potential represents the optimal potential that maintains balance between localization and uncertainty, produces a wavefunction with exactly the required Fisher information and minimizes entropy while satisfying the resolution threshold.}

\notes{This establishes the first appearance of wave-like structure in the unfolding framework. The minimal-entropy density in $M$-space obeys a local equation with the form of a stationary wavefunction as a geometric consequence of information constraints.}

\notes{We interpret this as a latent wave equation: a structure that governs the configuration of unresolved variables prior to activation. It encodes the intrinsic geometry of the latent domain $\mathcal{D}_0$, and serves as the foundational solution from which dynamics later emerge.}

\endif 
