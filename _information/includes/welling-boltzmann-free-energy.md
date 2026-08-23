\ifndef{wellingBoltzmannFreeEnergy}
\define{wellingBoltzmannFreeEnergy}

\editme

\notes{\subsection{GAIST on Boltzmann and Free Energy}}

\notes{The opening essay, ``Why Stochastic Thermodynamics of Machine Learning?'' [@Welling-generative26], states the free-energy decomposition we use today: entropy measures the information we are missing; we subtract it from the energy and call what remains free energy, the energy still free to perform work. Maxwell's demon appears there as a knowledge engine --- not yet as Landauer's cost. That cost is week 3.}

\notes{Chapter 3 is the physics we need for LO1. Section 3.2 introduces the Hamiltonian, the microcanonical and canonical ensembles, and the passage from the partition function to $U$, $S$, and $F$. Section 3.3 writes the first law and splits an energy change into heat and work:
$$
\delta U = \int \delta\rho\,\mathrm{H} + \int \rho\,\delta\mathrm{H}.
$$
The first term is heat ($\rho$ changes at fixed Hamiltonian); the second is work (the Hamiltonian changes at fixed $\rho$). That is the same accounting as $F = U - TS$: $TS$ is the cut taken by ignorance, $F$ is what remains.}

\notes{Read Chapter 3, not the whole book. Callen remains the undergraduate thermodynamics reference. GAIST does not discuss perpetual motion or the human bandwidth constraint; those motivations are ours.}

\addreading{@Welling-generative26}{Chapter 3}

\endif
