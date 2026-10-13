\ifndef{poissonEntropy}
\define{poissonEntropy}
\editme

\subsection{Poisson Entropy}

\notes{A Poisson($\lambda$) distribution on the non-negative integers has
$$
P(k)=\frac{\lambda^k e^{-\lambda}}{k!}.
$$
Entropy again has no elementary closed form; numerically $H=\sum_k -P(k)\log_2 P(k)$. For large $\lambda$, $H\approx\tfrac12\log_2(2\pi e\lambda)$ bits.\ifdef{poissonEnergyFromDistribution} The $\lambda=4$ panels reuse the count distribution from the energy overlay: surprisal is that energy in bits; the right panel is the average that defines $H$.\endif}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import mlai
import mlai.plot as plot}

\plotcode{lam = 4.0
ks = np.arange(0, 16)
probs = poisson.pmf(ks, lam)
surprisal = -np.log2(np.clip(probs, 1e-300, None))
contrib = probs * surprisal
H = contrib.sum()

fig, axes = plt.subplots(1, 3, figsize=plot.big_wide_figsize)
colours = ['#4C72B0', '#DD8452', '#55A868']
axes[0].bar(ks, probs, color=colours[0], width=0.8)
axes[0].set_xlabel('$k$')
axes[0].set_ylabel('$P(k)$')
axes[0].set_title(f'Poisson($\\lambda={lam:g}$)')

axes[1].bar(ks, surprisal, color=colours[1], width=0.8)
axes[1].set_xlabel('$k$')
axes[1].set_ylabel('$-\\log_2 P(k)$')
axes[1].set_title('surprisal')

axes[2].bar(ks, contrib, color=colours[2], width=0.8)
axes[2].set_xlabel('$k$')
axes[2].set_ylabel('$-P(k)\\log_2 P(k)$')
axes[2].set_title(f'summands ($H={H:.3f}$ bits)')
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
fig.tight_layout()
mlai.write_figure('poisson-entropy-panels.svg', directory='\writeDiagramsDir/information')}

\newslide{Poisson Entropy}

\figure{\includediagram{\diagramsDir/information/poisson-entropy-panels}{85%}}{Poisson($\lambda=4$). Mid: surprisal rises in the tails\ifdef{poissonEnergyFromDistribution} (energy in bits)\endif. Right: the probability weight cuts those tails back, so $H$ is dominated by the bulk.}{poisson-entropy-panels}

\ifdef{poissonEnergyFromDistribution}
\slidesincremental{
* Same $\lambda=4$ as the energy overlay: middle panel is $E$ in bits
* Right panel: $H=\mathbb{E}[E]$ --- high-energy tails are down-weighted by $P(k)$
* Large-$\lambda$ approximation: $H\approx\tfrac12\log_2(2\pi e\lambda)$ bits
}
\else
\slidesincremental{
* Count distributions: same three-panel reading as Bernoulli / binomial
* Large-$\lambda$ approximation: $H\approx\tfrac12\log_2(2\pi e\lambda)$ bits
* Entropy grows only logarithmically with the rate
}
\endif


\endif
