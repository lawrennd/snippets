\ifndef{waveEquationEmergence}
\define{waveEquationEmergence}

\editme

\notes{Local Wave Equations in $M$-Space from Information Geometry}

\notes{We examine the special case of the system's origin — the latent region $\mathcal{D}_0$ — where no variables have yet activated, and the geometry is defined purely in terms of the latent information structure over the proto-coordinates $M$.}

\notes{In this phase, the system is critically slowed: the entropy gradient $G(\boldsymbol{\theta}) \boldsymbol{\theta}$ remains uniformly suppressed, and the dynamics are governed by equilibrium-like conditions that define the structure of the minimal-entropy state. We now derive the formal mathematical description of how these latent variables behave.}

\subsection{Von Neumann Entropy Minimization with Resolution Constraints}

\notes{For latent variables $M$ at the resolution threshold, we minimize the von Neumann entropy subject to precise constraints,
$$
S[\rho] = -\text{tr}(\rho \log \rho)
$$
with two key constraints, normalisation: $\text{tr}(\rho) = 1$ and Fisher information at the exact threshold: $G_{ii} = \varepsilon^2$. The second constraint places $M$ variables precisely at the boundary between unresolvable and active states. This reflects the condition where the information gradient component equals the resolution threshold,
$$
\left| \left[G(\boldsymbol{\theta})\boldsymbol{\theta}\right]_i \right| = \varepsilon.
$$}

\subsection{Variational Formulation}

\notes{Following Jaynes we formulate the constrained optimization problem using Lagrange multipliers,
$$
\mathcal{L}[\rho] = -\text{Tr}(\rho \log \rho) - \lambda_0(\text{tr}(\rho) - 1) - \lambda_G\left(\text{tr}\left(\rho \left(\frac{\partial \log \rho}{\partial \theta}\right)^2\right) - \varepsilon^2\right),
$$
and for analytical tractability, we express the density matrix in terms of a wavefunction $\psi(m) = \sqrt{p(m)}$, which transforms the Fisher information constraint to
$$
G = 4\int \left|\frac{d\psi(m)}{dm}\right|^2 \text{d}m = \varepsilon^2,
$$
see e.g @Friden-physics98.

\subsection{Deriving the Wave Equation}

\notes{Taking the functional derivative and setting it equal to zero
$$
\frac{\delta \mathcal{L}}{\delta \psi} = 0
$$
which yields the Euler-Lagrange equation
$$
-\frac{\text{d}^2\psi(m)}{\text{d}m^2} + V(m)\psi(m) = \mu\psi(m),
$$
where the potential function $V(m)$ and eigenvalue $\mu$ are determined by the constraints.}

\subsection{Deriving the Potential Function}

\notes{For minimum entropy solutions at fixed Fisher information, it can be proven that the optimal wavefunction is Gaussian,
$$
\psi(m) = \left(\frac{\alpha}{\pi}\right)^{1/4}e^{-\alpha m^2/2},
$$
where $\alpha$ is determined by the Fisher information constraint
$$
4\int \left|\frac{\text{d}\psi(m)}{\text{d}m}\right|^2 \text{d}m = 4\alpha = \varepsilon^2
$$
which gives us $\alpha = \varepsilon^2/4$.}

\notes{Substituting this solution back into our variational formulation and comparing with the standard form of the wave equation, we derive:
$$
V(m) = \lambda m^2
$$
where $\lambda$ is a positive constant related to the Lagrange multiplier and resolution parameter. This confirms that the potential is quadratic, arising directly from the condition of minimum entropy under exact Fisher information constraint.}

\subsection{The Time-Independent Schrödinger-Type Equation}

\notes{The resulting equation is
$$
-\frac{d^2\psi(m)}{dm^2} + \lambda m^2 \psi(m) = \mu \psi(m)
$$
which has the form of a time-independent Schrödinger equation for a harmonic oscillator.}

\subsection{Interpretation and Significance}

\notes{This wave-like equation emerges from the system's requirements to minimize entropy while maintaining exact resolution constraints. The system seeks the flattest possible entropy configuration under bounded resolution. The the ground state of this condition is formally equivalent to a Gaussian wavefunction, satisfying a local second-order differential equation.}

\notes{The derivation reveals that the quadratic potential emerges naturally from the system's information-theoretic requirements. It represents the optimal potential that maintains balance between localization and uncertainty, produces a wavefunction with exactly the required Fisher information and minimizes entropy while satisfying the resolution threshold.}

\notes{This establishes the first appearance of wave-like structure in the unfolding framework. The minimal-entropy density in $M$-space obeys a local equation with the form of a stationary wavefunction as a geometric consequence of information constraints.}

\notes{We interpret this as a latent wave equation: a structure that governs the configuration of unresolved variables prior to activation. It encodes the intrinsic geometry of the latent domain $\mathcal{D}_0$, and serves as the foundational solution from which dynamics later emerge.​​​​​​​​​​​​​​​​}

\endif 
