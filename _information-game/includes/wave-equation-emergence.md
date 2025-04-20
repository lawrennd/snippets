\ifndef{waveEquationEmergence}
\define{waveEquationEmergence}

\editme

\subsection{Local Wave Equations in $M$-Space from Information Geometry}

\notes{We now examine the special case of the system's origin — the latent region $\mathcal{D}_0$ — where no variables have yet activated, and the geometry is defined purely in terms of the latent information structure over a proto-coordinate $M$.}

\notes{In this phase, the system is critically slowed: the entropy gradient $G(\boldsymbol{\theta}) \boldsymbol{\theta}$ remains uniformly suppressed, and the dynamics are governed by equilibrium-like conditions that define the structure of the minimal-entropy state. Because this regime is shift-invariant in $\boldsymbol{\theta}$ (no direction dominates), the Fisher information becomes effectively independent of $\boldsymbol{\theta}$.}

\notes{This enables a direct variational analysis over the information geometry of $M$, without invoking any external physical interpretation. We treat $M$ as an emergent coordinate associated with an underlying resolution constraint, and derive a local equation for its distribution.}

\notes{Let $p(m)$ denote the distribution over $M$ at the system's origin. We define the Fisher information with respect to $m$ as
$$
J_M = \int \frac{1}{p(m)} \left( \frac{d p(m)}{d m} \right)^2 \text{d}m,
$$
and seek a variational principle that determines $p(m)$ under the constraint of finite resolution. Specifically, we assume the normalisation: $\int p(m) \, \text{d}m = 1$ and a variance constraint: $\int m^2 p(m) \, \text{d}m \geq \varepsilon^2$.}

\notes{Minimising $J_M$ under these constraints yields a second-order differential equation for $p(m)$ (or equivalently for its square root $\psi(m) := \sqrt{p(m)}$), of the form,
$$
- \frac{d^2 \psi}{d m^2} + \lambda m^2 \psi = \mu \psi
$$
which resembles a time-independent Schrödinger-type equation for a harmonic well. Here, the appearance of a potential-like term arises from the resolution constraint on the variance.}

\notes{Importantly, this wave-like equation is not imposed but emerges from the system's requirement to minimise curvature (i.e. Fisher information) in the absence of directional flow. The system seeks the flattest possible entropy configuration under bounded resolution — and the ground state of this condition is formally equivalent to a Gaussian, satisfying a local second-order differential equation.}

\notes{The minimisation procedure determines the ground-state configuration of the system under resolution constraints, and the resulting differential equation governs the form of the square-root amplitude $\psi(m)$.
This provides the first appearance of wave-like structure in the unfolding framework. The minimal-entropy density in $M$-space obeys a local equation with the form of a stationary wavefunction — not because of external physics, but as a geometric consequence of information constraints.}

\notes{We interpret this as a latent wave equation: a structure that governs the configuration of an unresolved variable prior to activation. It encodes the intrinsic geometry of the latent domain $\mathcal{D}_0$, and serves as the foundational solution from which dynamics later emerge.}

\notes{This structure arises entirely from internal constraints — not as an imposed physical law — though its form resonates with equations derived in physical contexts, such as those examined in Frieden's information-theoretic treatment of wave equations [@Frieden-physics98].}

\subsection{Why a Wave Equation?}

\notes{At the system's origin, we derived a local second-order differential equation for the square root of the probability density $\psi(m) := \sqrt{p(m)}$ — an equation whose structure mirrors that of a time-independent wavefunction.}

\notes{But where did this wave equation come from?}

\notes{It was not assumed. No physical Hamiltonian was postulated, no operator formalism invoked. Instead, the equation arose as the minimal-curvature configuration consistent with internal resolution constraints: a balance between flatness (low Fisher information) and bounded spread (finite variance). This tradeoff — between smoothness and uncertainty — is a familiar principle in statistical inference, where regularisation penalises sharp transitions and rewards structure that remains distinguishable but minimal.}

\notes{The resulting equation defines a stationary information geometry: a configuration where no direction dominates, and yet the system is not trivial. The emergence of wave-like behaviour here reflects a deeper principle: that curvature minimisation under information-theoretic constraints naturally yields differential structure. The equation is not about particles or fields — it is about the shape of uncertainty in a system that is otherwise silent.}

\endif 
