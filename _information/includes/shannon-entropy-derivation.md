\ifndef{shannonEntropyDerivation}
\define{shannonEntropyDerivation}

\editme

\subsection{Shannon Entropy from Axioms}

\slides{Shannon asked: what number measures uncertainty in a discrete distribution $p=(p_1,\ldots,p_n)$?}

\slidesincremental{
* Continuity; maximum at uniform; additive for independent parts
* Result: $H(p) = -\sum_i p_i \log p_i$
}

\speakernotes{Sketch the axioms; do not prove uniqueness. Board: fair coin, $p=0.9$, uniform-8. LO2. Wiener: Gibbs → communication.}

\notes{Shannon entropy $H=-\sum_i p_i\log p_i$ measures uncertainty. Thermodynamic entropy $S=kH$ uses the same functional form with a different operational reading: $H$ bounds what a code cannot do; the distribution $p$ is the prescription — the code or the belief.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai}

\plotcode{p = np.linspace(0.01, 0.99, 200)
H = [-q*np.log2(q)-(1-q)*np.log2(1-q) for q in p]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(p, H, linewidth=2)
ax.scatter([0.5, 0.9], [1.0, 0.469], s=80, zorder=3)
ax.set_xlabel('$p$ (probability of 0)')
ax.set_ylabel('$H$ (bits)')
ax.set_title('Binary entropy')
mlai.write_figure('binary-entropy.svg', directory='\writeDiagramsDir/ml')}

\newslide{Binary Entropy}

\figure{\includediagram{\diagramsDir/ml/binary-entropy}{70%}}{Binary entropy is maximal at $p=\frac12$ and falls as the source becomes predictable.}{binary-entropy}


\setupcode{import numpy as np}

\code{def shannon_entropy(probs, base=2):
    p = np.asarray(probs, dtype=float)
    p = p[p > 0]
    H = -np.sum(p * np.log(p))
    return H / np.log(base) if base == 2 else H

# Worksheet 1 tabulates fair coin, p=0.9, uniform-8, Boltzmann at beta=1}

\endif
