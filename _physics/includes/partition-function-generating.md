\ifndef{partitionFunctionGenerating}
\define{partitionFunctionGenerating}

\editme

\subsection{The Partition Function}


\newslide{$Z$ as Generating Function}

\slides{The canonical ensemble from the bath: fix $\beta$ and let the small system fluctuate.}

\slidesincremental{
* $Z(\beta) = \sum_i e^{-\beta E_i}$
* $U = -\partial_\beta \log Z$, \quad $F = -\beta^{-1}\log Z$, \quad $S = \beta(U-F)$
* Equilibrium = on the $\beta$-manifold; finite-time driving leaves it
}

\speakernotes{LO3. Work the two-state example on the board. Finite-time cost: named lecture 2, Crooks week 6.}

\notes{The partition function $Z(\beta)=\sum_i e^{-\beta E_i}$ is a generating function: $U=-\partial_\beta\log Z$, $F=-\beta^{-1}\log Z$, $S=\beta(U-F)$. The canonical ensemble is an equilibrium construction; driving in finite time leaves that manifold.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai}

\plotcode{eps = 1.0
beta = np.linspace(0.1, 3.0, 300)
Z = 1.0 + np.exp(-beta * eps)
U = eps / (1.0 + np.exp(beta * eps))
F = -np.log(Z) / beta
S = beta * (U - F)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(beta, U, label='$U$')
ax.plot(beta, S, label='$S$')
ax.plot(beta, F, label='$F$')
ax.set_xlabel(r'$\beta$')
ax.legend()
ax.set_title('Two-state system')
mlai.write_figure('two-state-partition.svg', directory='\writeDiagramsDir/ml')}

\newslide{}

\figure{\includediagram{\diagramsDir/ml/two-state-partition}{75%}}{Thermodynamic quantities from $Z(\beta)$ for the two-state system used as a running example.}{two-state-partition}


\setupcode{import numpy as np

def partition(energies, beta):
    return np.sum(np.exp(-beta * np.asarray(energies)))

def thermo_from_Z(beta, energies):
    e = np.asarray(energies, dtype=float)
    Z = partition(e, beta)
    p = np.exp(-beta * e) / Z
    U = np.sum(p * e)
    F = -np.log(Z) / beta
    S = beta * (U - F)
    return U, S, F}

\newslide{}

\slidesincremental{
* $U = -\partial_\beta \log Z$
* $F = -\beta^{-1}\log Z$
* Bath justifies the canonical ensemble
}
\endif
