\ifndef{binomialEntropy}
\define{binomialEntropy}
\editme

\subsection{Binomial Entropy}

\notes{A Binomial($n,p$) count is the sum of $n$ i.i.d. Bernoulli trials. There is no elementary closed form for $H$, but the same three-panel reading applies: plot $P(k)$, plot $-\log_2 P(k)$, and sum $-P(k)\log_2 P(k)$. For large $n$ a Gaussian approximation gives $H\approx\tfrac12\log_2\bigl(2\pi e\, np(1-p)\bigr)$ bits.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import mlai
import mlai.plot as plot}

\plotcode{n, p = 12, 0.4
ks = np.arange(0, n + 1)
probs = binom.pmf(ks, n, p)
# Guard zeros for log (binom pmf is positive on 0..n)
surprisal = -np.log2(np.clip(probs, 1e-300, None))
contrib = probs * surprisal
H = contrib.sum()

fig, axes = plt.subplots(1, 3, figsize=plot.big_wide_figsize)
colours = ['#4C72B0', '#DD8452', '#55A868']
axes[0].bar(ks, probs, color=colours[0], width=0.8)
axes[0].set_xlabel('$k$')
axes[0].set_ylabel('$P(k)$')
axes[0].set_title(f'Binomial($n={n}, p={p}$)')

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
mlai.write_figure('binomial-entropy-panels.svg', directory='\writeDiagramsDir/information')}

\newslide{Binomial Entropy}

\figure{\includediagram{\diagramsDir/information/binomial-entropy-panels}{85%}}{Binomial($n=12$, $p=0.4$). The right-hand panel sums to $H$; tails contribute little because $P(k)$ is small even when surprisal is large.}{binomial-entropy-panels}

\slidesincremental{
* Same visual grammar as Bernoulli: $P$, $-\log_2 P$, $-P\log_2 P$
* Surprisal is largest in the tails; weight $P(k)$ suppresses them in $H$
* Large-$n$ approximation: $H\approx\tfrac12\log_2(2\pi e\, np(1-p))$ bits
}

\endif
