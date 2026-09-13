\ifndef{boltzmannDerivation}
\define{boltzmannDerivation}

\editme

\subsection{Derivation of the Boltzmann Distribution}

\notes{For a given mean energy $U$, among all distributions with that $U$, pick the one with largest entropy. Week 2 named the Gibbs--Boltzmann occupation; this is the MaxEnt derivation that earns it.}

\slides{For fixed mean energy $U$, maximum entropy recovers Boltzmann weights.}
\slidesincremental{
* Constraints: $\sum_i p_i = 1$ and $\sum_i p_i E_i = U$
* MaxEnt: $p_i \propto e^{-\beta E_i}$ with coldness $\beta = 1/k_B T$
* Normalise: $Z(\beta)=\sum_i e^{-\beta E_i}$, so $p_i = e^{-\beta E_i}/Z$
}

<!-- Board derivation: Lagrange multipliers → Boltzmann. Coldness $\beta$ is the multiplier on mean energy; $T$ is the bath reading. Two-state occupations for intuition. -->

\speakernotes{LO5. This is the derivation postponed from week 2. Board the Lagrange multipliers; do not treat the formula as new.}

\notes{Maximum entropy subject to normalisation and fixed mean energy gives $p_i = e^{-\beta E_i}/Z$. The Lagrange multiplier on the energy constraint *is* coldness $\beta$ from weeks 1--2.}

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
ax.set_title('Two-state Boltzmann occupations')
mlai.write_figure('two-state-boltzmann.svg', directory='\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/two-state-boltzmann}{75%}}{Occupation of a two-state system as coldness increases. At low $\beta$ both states are populated; at high $\beta$ the ground state dominates.}{two-state-boltzmann}


\setuphelpercode{import numpy as np}

\helpercode{def boltzmann(energies, beta):
    """Boltzmann probabilities $p_i \\propto e^{-\\beta E_i}$."""
    log_w = -beta * np.asarray(energies, dtype=float)
    log_w -= log_w.max()
    w = np.exp(log_w)
    return w / w.sum()
}

\code{# Live check: boltzmann([0, 1], 1.0) -> (0.731, 0.269)
boltzmann([0, 1], 1.0)}

\endif
