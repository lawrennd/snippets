\ifndef{poissonEnergyFromDistribution}
\define{poissonEnergyFromDistribution}
\editme

\subsection{Poisson: Distribution and Energy}

\notes{A Poisson($\lambda$) on the non-negative integers has
$$
P(k)=\frac{\lambda^k e^{-\lambda}}{k!},\qquad E(k)=-\log P(k)
$$
(nats). The bulk of the mass sits in a shallow energy valley; the tails climb as $k!$ in the denominator of $P$ becomes the dominant cost.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import mlai
import mlai.plot as plot}

\plotcode{lam = 4.0
ks = np.arange(0, 16)
probs = poisson.pmf(ks, lam)
energy = -np.log(np.clip(probs, 1e-300, None))
colours = ['#4C72B0', '#DD8452']

fig, axes = plt.subplots(1, 2, figsize=plot.big_wide_figsize)
axes[0].bar(ks, probs, color=colours[0], width=0.8)
axes[0].set_xlabel('$k$')
axes[0].set_ylabel('$P(k)$')
axes[0].set_title(f'Poisson($\\lambda={lam:g}$)')

axes[1].bar(ks, energy, color=colours[1], width=0.8)
axes[1].set_xlabel('$k$')
axes[1].set_ylabel('$E(k)=-\\log P(k)$')
axes[1].set_title('energy (nats)')
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
fig.tight_layout()
mlai.write_figure('poisson-energy-panels.svg', directory='\writeDiagramsDir/ml')

fig, ax = plt.subplots(figsize=plot.big_figsize)
bars = ax.bar(ks, probs, color=colours[0], width=0.8, alpha=0.85, label='$P(k)$')
ax.set_xlabel('$k$')
ax.set_ylabel('$P(k)$', color=colours[0])
ax.tick_params(axis='y', labelcolor=colours[0])
ax2 = ax.twinx()
ax2.plot(ks, energy, 'o-', color=colours[1], lw=2, markersize=5, label='$E(k)$')
ax2.set_ylabel('$E(k)=-\\log P(k)$', color=colours[1])
ax2.tick_params(axis='y', labelcolor=colours[1])
ax.set_title(f'Poisson($\\lambda={lam:g}$): $P$ and $E$ overlaid')
ax.spines['top'].set_visible(False)
handles = [bars, ax2.lines[0]]
ax.legend(handles, ['$P(k)$', '$E(k)$'], loc='upper right')
fig.tight_layout()
mlai.write_figure('poisson-energy-overlay.svg', directory='\writeDiagramsDir/ml')}

\newslide{Poisson: $P$ and $E$}

\figure{\includediagram{\diagramsDir/ml/poisson-energy-panels}{85%}}{Poisson($\lambda=4$). Left: the count distribution. Right: energy $E=-\log P$. The mode is the energy minimum.}{poisson-energy-panels}

\newslide{Poisson: Overlay}

\figure{\includediagram{\diagramsDir/ml/poisson-energy-overlay}{60%}}{Same Poisson: probability (bars) against energy (markers). Tails are high-energy, low-probability states.}{poisson-energy-overlay}

\slidesincremental{
* $E(k)=-\log P(k)=\lambda-k\log\lambda+\log(k!)$ (up to the usual reading of Stirling)
* Mode of $P$ $=$ minimizer of $E$
* Same $p\propto e^{-E}$ grammar as the Bernoulli two-state model
}

\endif
