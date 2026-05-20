\ifndef{lmeOriginConfinement}
\define{lmeOriginConfinement}

\editme

\subsection{The LME Origin}

\notes{The game's natural origin is an axiomatically distinguished pure state. Since von Neumann entropy admits states with $S(\rho)=0$ and positive marginal entropies, the origin is a *globally pure* state with maximally mixed reduced states on each subsystem. These are the *locally maximally entangled* (LME) states.

To single out a canonical origin without introducing external structure we apply an additional axiomatic selection: among all globally pure states, choose those that maximise the conserved marginal-entropy sum. Since each marginal entropy is bounded by $s_i \leq \log d_i$ (where $d_i$ is the dimension of subsystem $i$), this forces every reduced state to be maximally mixed, fixing
$$
C = C_{\max} = \sum_i \log d_i.
$$
The origin is selected up to local-unitary equivalence [@Lawrence-origin26].}

\slides{
* Globally pure state: $S(\rho)=0$
* $C = C_{\max} = \sum_i \log d_i$ (axiomatically distinguished)
* Implies each marginal maximally mixed: $s_i = \log d_i$
}

\newslide{Boundary}

\slides{* Not faithful
* Trajectory can never have been there
* But origin selects a unique trajectory}

\subsection{Constraint Saturation and the Gibbs Lock}

\notes{At the LME origin the marginal-entropy sum is saturated termwise: every $s_i = \log d_i$ is at its individual upper bound. This has a remarkable consequence. Since each marginal is already at its ceiling, *none can increase further and none can decrease without violating the sum*. The marginal entropies are locked at their maximum values for the entire trajectory:
$$
s_i(\tau) = \log d_i \quad \forall i, \;\forall \tau.
$$
The constraint gradient $\mathbf{a}(\boldsymbol{\theta}^*) = \nabla_{\boldsymbol{\theta}} C\big|_{\boldsymbol{\theta}^*} = \mathbf{0}$ vanishes at the origin. The usual first-order tangency condition $\mathbf{a}^\top\dot{\boldsymbol{\theta}} = 0$ is trivially satisfied for any velocity — it no longer selects admissible directions. The constraint becomes a *second-order* geometric condition: admissible velocities must lie in the kernel of the constraint Hessian $\nabla^2 C(\boldsymbol{\theta}^*)$.}

\slides{
* Marginal entropies linked: $s_1 + s_2 = C$ (conserved sum)
* Individual ceilings: $s_i \leq \log d_i$
* Trade-off: as one marginal rises, the other must fall
}

\newslide{Linked Marginal Entropies}

\figure{\includediagram{\diagramsDir/information-game/marginal-entropy-tradeoff}{70%}}{The marginal-entropy conservation constraint $s_1 + s_2 = C$ in the $(s_1,s_2)$ plane. The dashed lines mark the individual ceilings $s_i = \log d$. Along the constraint segment, increasing one marginal entropy forces a decrease in the other.}{marginal-entropy-tradeoff}

\newslide{Saturation and Second Order}

\slidesincremental{
* At $C=C_{\max}$: every $s_i = \log d_i$ — each at its individual ceiling
* Marginals locked: $s_i(\tau) = \log d_i$ for all time
}

\newslide{Saturation of Constraint}

\figure{\includediagram{\diagramsDir/information-game/marginal-entropy-saturation}{70%}}{As $C$ increases toward $C_{\max} = \sum_i \log d_i$, the accessible constraint segment (coloured lines) shrinks. At $C = C_{\max}$ the constraint collapses to the single corner point (red dot), the LME origin, where every marginal entropy is individually at its ceiling and the constraint gradient vanishes.}{marginal-entropy-saturation}

\newslide{Saturation of Constraint}

\slidesincremental{* First-order condition vacuous
* Admissible velocities: $\dot{\boldsymbol{\theta}}\in \ker\nabla^2 \sum_i h_i$
}

\subsection{GENERIC Dynamics at the Origin}

\notes{The second-order admissible velocity subspace consists of directions that preserve all reduced states to first order: $\dot{\rho}_i = 0$ for all subsystems $i$. These include the commutator flows
$$
\dot{\rho} = -\mathrm{i}[K_{\text{local}}, \rho],
$$
where $K_{\text{local}} = \sum_i K_i \otimes \mathbf{I}_{\bar{i}}$ is a local Hermitian generator. This is precisely the von Neumann/Schrödinger equation form.

The constrained dynamics decompose into a GENERIC-compatible structure [@Lawrence-origin26]:
$$
\frac{\mathrm{d}\boldsymbol{\theta}}{\mathrm{d}t} \propto \underbrace{-\Pi_{\mathrm{marg}}(\boldsymbol{\theta})\boldsymbol{\theta}}_{\text{dissipative (SEA)}} + \underbrace{\mathrm{ad}_\xi\,\boldsymbol{\theta}}_{\text{reversible (Lax)}},
$$
where $\Pi_{\mathrm{marg}}$ is the Fisher-orthogonal projector onto marginal-preserving directions and $\mathrm{ad}_\xi$ is the adjoint action corresponding to $\dot{\rho} = -\mathrm{i}[\xi,\rho]$. The reversible sector has the structure of a Lax equation; the irreversible sector realises steepest entropy ascent within the correlation degrees of freedom.}

\slides{
$$\dot{\boldsymbol{\theta}} \propto \underbrace{-\Pi_{\mathrm{marg}}\boldsymbol{\theta}}_{\text{dissipative}} + \underbrace{\mathrm{ad}_\xi\,\boldsymbol{\theta}}_{\text{reversible (Lax)}}$$

* Reversible: $\dot{\rho} = -\mathrm{i}[K,\rho]$ — von Neumann equation emerges
* Irreversible: steepest entropy ascent in marginal-preserving subspace
* No Hamiltonian assumed — it emerges from constraint geometry
}

\subsection{The Origin is Unreachable}

\notes{Although the origin axiomatically distinguishes the trajectory, the system can never literally have been there. The origin lies on the *boundary* of the natural-parameter space: as the state approaches the pure LME state, the natural parameters $\boldsymbol{\theta}$ diverge, $\|\boldsymbol{\theta}\| \to \infty$. The Riemannian (BKM/Fisher) metric degenerates in the direction of diverging parameters, so the origin is at *infinite Fisher distance* from any interior point.

The game is axiomatically directed *towards* an origin that acts as a limit, not a starting point that was literally occupied. The trajectory is uniquely distinguished by its asymptotic direction — the steepest-entropy-ascent direction in the Fisher metric — even though the origin itself is unreachable [@Lawrence-origin26].}

\slidesincremental{
* Origin: boundary of natural-parameter space
* $\|\boldsymbol{\theta}\|\to\infty$ as $\rho\to\rho_{\mathrm{pure}}$
* Fisher (BKM) metric degenerates at boundary
* Infinite Fisher distance — never literally reached
* *Trajectory distinguished by its asymptotic origin, not a literal start*
}

\endif
