\ifndef{gaussianEnergyFromDistribution}
\define{gaussianEnergyFromDistribution}
\editme

\notes{The univariate Gaussian already written as
$$
p(y)\propto\exp\!\left(-\frac{(y-\mu)^2}{2\sigma^2}\right)
$$
is an energy-based model with quadratic energy. Taking $E(y)=-\log p(y)$ (nats) adds only the normaliser $\tfrac12\log(2\pi\sigma^2)$, so the shape remains a parabola about $\mu$. The height example $\mu=1.7$, $\sigma^2=0.0225$ is reused below.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import mlai
import mlai.plot as plot}

\plotcode{mu, var = 1.7, 0.0225
sigma = np.sqrt(var)
ys = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
pdf = norm.pdf(ys, loc=mu, scale=sigma)
energy = -np.log(pdf)
colours = ['#4C72B0', '#DD8452']

fig, axes = plt.subplots(1, 2, figsize=plot.big_wide_figsize)
axes[0].plot(ys, pdf, color=colours[0], lw=2)
axes[0].fill_between(ys, pdf, color=colours[0], alpha=0.25)
axes[0].axvline(mu, color='#666', ls='--', lw=1)
axes[0].set_xlabel('$y$')
axes[0].set_ylabel('$p(y)$')
axes[0].set_title(f'Gaussian($\\mu={mu}, \\sigma^2={var}$)')

axes[1].plot(ys, energy, color=colours[1], lw=2)
axes[1].axvline(mu, color='#666', ls='--', lw=1)
axes[1].set_xlabel('$y$')
axes[1].set_ylabel('$E(y)=-\\log p(y)$')
axes[1].set_title('energy (nats; quadratic)')
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
fig.tight_layout()
mlai.write_figure('gaussian-energy-panels.svg', directory='\writeDiagramsDir/ml')

fig, ax = plt.subplots(figsize=plot.big_figsize)
line_p, = ax.plot(ys, pdf, color=colours[0], lw=2, label='$p(y)$')
ax.fill_between(ys, pdf, color=colours[0], alpha=0.2)
ax.axvline(mu, color='#666', ls='--', lw=1)
ax.set_xlabel('$y$')
ax.set_ylabel('$p(y)$', color=colours[0])
ax.tick_params(axis='y', labelcolor=colours[0])
ax2 = ax.twinx()
line_e, = ax2.plot(ys, energy, color=colours[1], lw=2, label='$E(y)$')
ax2.set_ylabel('$E(y)=-\\log p(y)$', color=colours[1])
ax2.tick_params(axis='y', labelcolor=colours[1])
ax.set_title('Gaussian: density and quadratic energy overlaid')
ax.spines['top'].set_visible(False)
ax.legend([line_p, line_e], ['$p(y)$', '$E(y)$'], loc='upper right')
fig.tight_layout()
mlai.write_figure('gaussian-energy-overlay.svg', directory='\writeDiagramsDir/ml')}

\newslide{Gaussian: $p$ and $E$}

\figure{\includediagram{\diagramsDir/ml/gaussian-energy-panels}{85%}}{Height Gaussian. Left: density. Right: energy $E=-\log p$ --- a parabola about $\mu=1.7$ (additive constant from the normaliser does not change the shape).}{gaussian-energy-panels}

\newslide{Gaussian: Overlay}

\figure{\includediagram{\diagramsDir/ml/gaussian-energy-overlay}{60%}}{Same Gaussian: density (left axis) and energy (right axis). The mode of $p$ is the bottom of the energy well.}{gaussian-energy-overlay}

\newslide{Gaussian Energy}

\slidesincremental{
* $E(y)=\frac{(y-\mu)^2}{2\sigma^2}$ up to an additive constant absorbed in $Z$
* Least-squares regression uses the same quadratic energy on residuals
* Normaliser $(2\pi\sigma^2)^{-1/2}$ is the partition function for this $E$
}

\endif
