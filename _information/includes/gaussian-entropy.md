\ifndef{gaussianEntropy}
\define{gaussianEntropy}
\editme

\subsection{Gaussian Differential Entropy}

\notes{For a continuous density the same formal expression
$$
h(X) = -\int p(y)\log_2 p(y)\,\mathrm{d}y
$$
is called *differential* entropy. It can be negative, and it is not invariant to rescaling of $y$. For a univariate Gaussian $\mathcal{N}(\mu,\sigma^2)$,
$$
h = \tfrac12\log_2\bigl(2\pi e\sigma^2\bigr)
$$
bits. The panels below use the height example ($\mu=1.7$, $\sigma^2=0.0225$): density, surprisal $-\log_2 p(y)$, and the integrand $-p(y)\log_2 p(y)$.\ifdef{gaussianEnergyFromDistribution} That is the same height Gaussian as the quadratic-energy overlay: the middle curve is $E=-\log p$ in bits (still a parabola); the right panel integrates $p\,E$ to differential entropy.\endif}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import mlai
import mlai.plot as plot}

\plotcode{mu, var = 1.7, 0.0225
sigma = np.sqrt(var)
ys = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
# Density in probability per unit length
pdf = norm.pdf(ys, loc=mu, scale=sigma)
# Surprisal in bits; pdf can exceed 1, so -log2(pdf) can be negative
surprisal = -np.log2(pdf)
integrand = pdf * surprisal
# Closed form in bits
h = 0.5 * np.log2(2 * np.pi * np.e * var)

fig, axes = plt.subplots(1, 3, figsize=plot.big_wide_figsize)
colours = ['#4C72B0', '#DD8452', '#55A868']
axes[0].plot(ys, pdf, color=colours[0], lw=2)
axes[0].fill_between(ys, pdf, color=colours[0], alpha=0.25)
axes[0].axvline(mu, color='#666', ls='--', lw=1)
axes[0].set_xlabel('$y$')
axes[0].set_ylabel('$p(y)$')
axes[0].set_title(f'Gaussian($\\mu={mu}, \\sigma^2={var}$)')

axes[1].plot(ys, surprisal, color=colours[1], lw=2)
axes[1].axhline(0, color='#666', ls=':', lw=1)
axes[1].set_xlabel('$y$')
axes[1].set_ylabel('$-\\log_2 p(y)$')
axes[1].set_title('surprisal (can be negative)')

axes[2].plot(ys, integrand, color=colours[2], lw=2)
axes[2].fill_between(ys, integrand, color=colours[2], alpha=0.25)
axes[2].set_xlabel('$y$')
axes[2].set_ylabel('$-p(y)\\log_2 p(y)$')
axes[2].set_title(f'integrand ($h={h:.3f}$ bits)')
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
fig.tight_layout()
mlai.write_figure('gaussian-entropy-panels.svg', directory='\writeDiagramsDir/information')}

\newslide{Gaussian Differential Entropy}

\figure{\includediagram{\diagramsDir/information/gaussian-entropy-panels}{85%}}{Univariate Gaussian (height example). Middle: $-\log_2 p(y)$\ifdef{gaussianEnergyFromDistribution} --- quadratic energy in bits\endif; dips below zero where the density exceeds $1$. Right: the integrand whose integral is differential entropy $h$.}{gaussian-entropy-panels}

\ifdef{gaussianEnergyFromDistribution}
\slidesincremental{
* Same height Gaussian as the energy overlay: middle panel is the parabola in bits
* Differential entropy $h=\mathbb{E}[E]$ (bits) --- closed form $\tfrac12\log_2(2\pi e\sigma^2)$
* Can be negative; not the same object as discrete Shannon $H$
}

\speakernotes{Callback to the quadratic well. Flag the continuous caveat once: discrete $H\ge 0$; differential $h$ is a relative measure.}
\else
\slidesincremental{
* Closed form: $h=\tfrac12\log_2(2\pi e\sigma^2)$ bits
* Grows with $\sigma$; independent of $\mu$
* Differential entropy $\neq$ discrete Shannon $H$ --- can be negative
}

\speakernotes{Flag the continuous caveat once. Do not dwell; the three-panel analogy is the point. Discrete $H\ge 0$; differential $h$ is a relative measure.}
\endif

\endif
