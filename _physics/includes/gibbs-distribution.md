\ifndef{gibbsDistribution}
\define{gibbsDistribution}

\editme

\subsection{The Gibbs--Boltzmann Distribution}

\notes{Name the object and fix the formula. The MaxEnt derivation that *earns* these weights is a separate step: deriving the occupation from Lagrange multipliers before Shannon $H$ and Jaynes would put the cart before the horse.}

\newslides{Gibbs--Boltzmann Occupation}

\slides{Same formula, three names: Boltzmann weights, Gibbs distribution, canonical ensemble.}

\slidesincremental{
* $p_i = e^{-\beta E_i}/Z$, $\quad Z(\beta)=\sum_j e^{-\beta E_j}$
* $\beta=1/k_B T$: coldness; $T$: bath temperature
* $\log Z$ is the cumulant generating function of the energy
}

\speakernotes{Introduce and use, do not derive. Board the formula. MaxEnt with fixed mean energy recovers the same $p_i$.}

\notes{Write the equilibrium occupation of a discrete system with energies $\{E_i\}$ as
$$
p_i = \frac{e^{-\beta E_i}}{Z(\beta)},
\qquad
Z(\beta)=\sum_j e^{-\beta E_j}.
$$
Physicists call $p_i$ the *Boltzmann distribution* (or Boltzmann weights) and, for a system exchanging energy with a bath at fixed $T$, the *Gibbs distribution* or *canonical ensemble*. The three names point at the same formula. The normalisation $Z(\beta)$ is the *partition function*. Its logarithm $\log Z(\beta)$ is the cumulant generating function for the energy under this exponential family: derivatives of $\log Z$ recover the mean energy, the variance (heat capacity, up to factors of $\beta$), and higher cumulants. That generating-function reading is why $Z$ is more than a normalisation constant.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai}

\plotcode{energies = np.array([0.0, 1.0])
beta = np.linspace(0.1, 3.0, 200)
Z = np.sum(np.exp(-beta[:, None] * energies), axis=1)
p0 = np.exp(-beta * energies[0]) / Z
p1 = np.exp(-beta * energies[1]) / Z
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(beta, p0, linewidth=2, label='$p_0$ (ground)')
ax.plot(beta, p1, linewidth=2, label='$p_1$ (excited)')
ax.set_xlabel(r'coldness $\beta$')
ax.set_ylabel('occupation')
ax.legend()
ax.set_title('Two-state Gibbs--Boltzmann occupations')
mlai.write_figure('two-state-boltzmann.svg', directory='\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/two-state-boltzmann}{75%}}{Occupation of a two-state system as coldness increases. At low $\beta$ both states are populated; at high $\beta$ the ground state dominates.}{two-state-boltzmann}

\newslides{Aside: Hopfield, Boltzmann Machines, Nobel 2024}

\slides{The same energy-and-occupation grammar reappears in associative memory and early deep learning.}

\slidesincremental{
* Hopfield (1982): fixed-weight energy; recall as settling
* Boltzmann machine (1985): make those couplings *learnable*
* Pairwise energy: $E(\mathbf{s})=-\sum_i b_i s_i-\sum_{i<j}W_{ij}s_i s_j$
}

\speakernotes{Colour only. Nobel 2024 (Hopfield and Hinton) names the line. Do not divert into training algorithms or Landauer here.}

\notes{The Gibbs--Boltzmann occupation is not only a statement about gases and magnets. Hopfield networks [@Hopfield:neural82] assign an energy to every binary configuration of a recurrent net and treat recall as a descent toward low-energy states --- equilibrium statistics are again Gibbs. Ackley, Hinton and Sejnowski [@Ackley-boltzmann85] made the weights of that energy *learnable*: a Boltzmann machine is an undirected model whose distribution over configurations is exactly $p(s)\propto e^{-E(s)/T}$. The 2024 Nobel Prize in Physics, awarded to John Hopfield and Geoffrey Hinton, recognised that physical-systems reading of computation and learning. Name the lineage so the formula does not feel confined to nineteenth-century heat baths; do not divert into training algorithms.}
\addreading{@Ackley-boltzmann85}{Boltzmann machines (optional colour)}
\addreading{@Hopfield:neural82}{Hopfield networks (optional colour)}

\endif
