\ifndef{hamiltonianEmergencePreview}
\define{hamiltonianEmergencePreview}

\editme

\subsection{From Information Geometry to Hamiltonian Mechanics}

\notes{The inaccessible game has no Hamiltonian in its axioms. Its dynamics are governed entirely by the information-geometric structure: maximum entropy production under marginal entropy conservation, with time measured by entropy production (entropy time). Yet Hamiltonian structure can *emerge* in metastable regions of the trajectory, as a local effective description.

The key condition is a structural alignment of the modular generator $K(\boldsymbol{\theta}) = \log\rho(\boldsymbol{\theta})$ (in trace gauge) with a fixed operator direction. When this alignment holds, we say the system is in a *Gibbs-locked* region [@Lawrence-hamiltonian26].}

\slides{
The inaccessible game has **no Hamiltonian** in its axioms.

Yet in metastable *Gibbs-locked* regions, an effective Hamiltonian description emerges from the information geometry.

*(Work in preparation)*
}

\subsection{The Gibbs-lock Condition}

\notes{The Gibbs-lock condition is that the modular generator aligns with a fixed effective Hamiltonian direction $H$:
$$
K(\boldsymbol{\theta}) \approx -\beta(\boldsymbol{\theta})\,H,
$$
where $\beta(\boldsymbol{\theta})$ is a smoothly varying scalar (effective inverse temperature) and $H$ is approximately fixed along the trajectory. The exact locked point is the Gibbs thermal state $\rho_0 = e^{-\beta_0 H}/Z$, where the reversible (Lax) sector ceases to evolve and $[K_0, H] = 0$.

This condition reverses the usual explanatory order: rather than postulating time-translation symmetry and deriving energy conservation, the game's constraint geometry selects an approximately conserved direction $H$ from the modular generator. The effective Hamiltonian is not an axiom — it is an emergent feature of metastable Gibbs-locked regions [@Lawrence-hamiltonian26].}

\slides{
$$K(\boldsymbol{\theta}) \approx -\beta(\boldsymbol{\theta})\,H$$

* $H$: approximately fixed operator direction
* $\beta(\boldsymbol{\theta})$: smoothly varying inverse temperature
* Exact lock: $\rho_0 = e^{-\beta_0 H}/Z$ (Gibbs state), reversible flow stops
* $H$ **not assumed** — selected from modular generator
}

\subsection{The Hamiltonian Clock}

\notes{Within a Gibbs-locked region, entropy time $t$ can be converted into a Hamiltonian-frame clock $\tau_H$ by
$$
\text{d}\tau_H = \beta(t)\,\text{d}t.
$$
This Hamiltonian clock is a derived conversion of entropy time, not an independent temporal structure. The effective inverse temperature $\beta(t)$ acts as a conversion factor between information-geometric progress (entropy produced) and mechanical phase (Hamiltonian time). Within the locked frame the constrained dynamics take the familiar form of a Lindblad master equation: a reversible Lax sector (the von Neumann equation) plus a dissipative sector that uniformly dephases all off-diagonal coherences in the locked eigenbasis.

These results are conditional on the trajectory entering a Gibbs-locked region. The threshold for these conditional results to carry observational content is $W_{\mathcal{R}} \gg 1$, a Boltzmann-style multiplicity of action-resolution cells inside the locked basin — essentially the regime in which equilibrium statistical mechanics applies empirically [@Lawrence-hamiltonian26].}

\slidesincremental{
* Hamiltonian clock: $\text{d}\tau_H = \beta(t)\,\text{d}t$
* Derived from entropy time — not independent
* $\beta(t)$: conversion between entropy-time and Hamiltonian phase
* Within locked frame: reversible Lax sector + uniform dephasing
* Operational: requires $W_{\mathcal{R}} \gg 1$

*Effective Hamiltonian mechanics as a local, emergent, conditional description*
}

\endif
