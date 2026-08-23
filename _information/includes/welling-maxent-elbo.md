\ifndef{wellingMaxentElbo}
\define{wellingMaxentElbo}

\editme

\notes{\subsection{GAIST on MaxEnt and Free Energy}}

\notes{Section 1.5.5 of [@Welling-generative26] is Jaynes' maximum entropy principle as a convex programme. The constraints are normalisation and a prescribed mean energy. The stationarity condition recovers the Boltzmann distribution; the Lagrange multiplier on energy is $\beta = 1/k_B T$. The dual Lagrangian is the equilibrium entropy, $S = \beta(E - F)$. That is LO5 in an optimisation dialect. Read it after Jaynes (1957), not instead of it.}

\notes{Chapter 5 is the book's central identification, and the reason the book exists. The thermodynamic variational free energy $\mathcal{F}_{\mathrm{TD}}[q] = U[q] - T\mathrm{S}[q]$ is the ELBO once the Hamiltonian is identified with $-\log p(x,z)$ and $T = 1$. Changing $q$ at fixed Hamiltonian is heat: that is the E-step, inference as relaxation. Changing the Hamiltonian at fixed $q$ is work: that is the M-step, learning. The equilibrium free energy is $-\log p(x)$. This is the generative-model translation of $F = U - TS$.}

\notes{Use Chapter 5 as a fourth voice in the LO7 comparison, not as a replacement for it. GAIST is willing to say there is no real difference between these theories. We are not. Shannon, Boltzmann and Jaynes agree on the functional $H$ and disagree about what the probability is over. The ELBO identification is a *correspondence*, useful and precise. It does not collapse the operational assumptions.}

\addreading{@Welling-generative26}{Section 1.5.5 and Chapter 5}

\endif
