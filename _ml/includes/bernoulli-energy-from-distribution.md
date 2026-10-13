\ifndef{bernoulliEnergyFromDistribution}
\define{bernoulliEnergyFromDistribution}
\editme

\notes{A Bernoulli($p$) on $\{0,1\}$ has energies $E(x)=-\log P(x)$ (nats). High probability is low energy. The panels below use a biased coin $p=0.3$: first $P$ and $E$ side by side, then the same two curves overlaid on twin axes so the inverse relationship is visible in one frame.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{p_success = 0.3
xs = np.array([0, 1])
probs = np.array([1 - p_success, p_success])
energy = -np.log(probs)
colours = ['#4C72B0', '#DD8452']

fig, axes = plt.subplots(1, 2, figsize=plot.big_wide_figsize)
axes[0].bar(xs, probs, color=colours[0], width=0.5)
axes[0].set_xticks(xs)
axes[0].set_xlabel('$x$')
axes[0].set_ylabel('$P(x)$')
axes[0].set_title(f'Bernoulli($p={p_success}$)')
axes[0].set_ylim(0, 1)

axes[1].bar(xs, energy, color=colours[1], width=0.5)
axes[1].set_xticks(xs)
axes[1].set_xlabel('$x$')
axes[1].set_ylabel('$E(x)=-\\log P(x)$')
axes[1].set_title('energy (nats)')
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
fig.tight_layout()
mlai.write_figure('bernoulli-energy-panels.svg', directory='\writeDiagramsDir/ml')

fig, ax = plt.subplots(figsize=plot.big_figsize)
bars = ax.bar(xs, probs, color=colours[0], width=0.45, alpha=0.85, label='$P(x)$')
ax.set_xticks(xs)
ax.set_xlabel('$x$')
ax.set_ylabel('$P(x)$', color=colours[0])
ax.tick_params(axis='y', labelcolor=colours[0])
ax.set_ylim(0, 1)
ax2 = ax.twinx()
ax2.plot(xs, energy, 'o-', color=colours[1], lw=2, markersize=10, label='$E(x)$')
ax2.set_ylabel('$E(x)=-\\log P(x)$', color=colours[1])
ax2.tick_params(axis='y', labelcolor=colours[1])
ax.set_title(f'Bernoulli($p={p_success}$): $P$ and $E$ overlaid')
ax.spines['top'].set_visible(False)
handles = [bars, ax2.lines[0]]
ax.legend(handles, ['$P(x)$', '$E(x)$'], loc='upper center')
fig.tight_layout()
mlai.write_figure('bernoulli-energy-overlay.svg', directory='\writeDiagramsDir/ml')}

\newslide{Bernoulli: $P$ and $E$}

\figure{\includediagram{\diagramsDir/ml/bernoulli-energy-panels}{85%}}{Bernoulli($p=0.3$). Left: the distribution. Right: energy $E=-\log P$ in nats. The favoured outcome sits lower in energy.}{bernoulli-energy-panels}

\newslide{Bernoulli: Overlay}

\figure{\includediagram{\diagramsDir/ml/bernoulli-energy-overlay}{60%}}{Same Bernoulli: probability (bars, left axis) and energy (markers, right axis). Where $P$ is high, $E$ is low.}{bernoulli-energy-overlay}

\newslide{Bernoulli Energy}

\slidesincremental{
* $E_0=-\log(1-p)$,\quad $E_1=-\log p$
* Fair coin: degenerate energies $E_0=E_1=\log 2$
* Biased coin: the favoured face is the deeper well
}

\endif
