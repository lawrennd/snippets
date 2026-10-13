\ifndef{bernoulliEntropy}
\define{bernoulliEntropy}
\editme

\subsection{Bernoulli Entropy}

\notes{A Bernoulli($p$) random variable takes values $\{0,1\}$ with probabilities $1-p$ and $p$. Its Shannon entropy is the binary entropy
$$
H(X) = -p\log_2 p - (1-p)\log_2(1-p)
$$
bits. The panels below show, for a fixed $p$, the distribution, the pointwise surprisal $-\log_2 P(x)$, and the summands $-P(x)\log_2 P(x)$ whose total is $H$.\ifdef{bernoulliEnergyFromDistribution} The same $p=0.3$ coin appeared in the energy overlay: middle panel is that energy in bits; the right panel averages it to $H$.\endif}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{p_success = 0.3
xs = np.array([0, 1])
probs = np.array([1 - p_success, p_success])
surprisal = -np.log2(probs)
contrib = probs * surprisal
H = contrib.sum()

fig, axes = plt.subplots(1, 3, figsize=plot.big_wide_figsize)
colours = ['#4C72B0', '#DD8452', '#55A868']
axes[0].bar(xs, probs, color=colours[0], width=0.5)
axes[0].set_xticks(xs)
axes[0].set_xlabel('$x$')
axes[0].set_ylabel('$P(x)$')
axes[0].set_title(f'Bernoulli($p={p_success}$)')
axes[0].set_ylim(0, 1)

axes[1].bar(xs, surprisal, color=colours[1], width=0.5)
axes[1].set_xticks(xs)
axes[1].set_xlabel('$x$')
axes[1].set_ylabel('$-\\log_2 P(x)$')
axes[1].set_title('surprisal')

axes[2].bar(xs, contrib, color=colours[2], width=0.5)
axes[2].set_xticks(xs)
axes[2].set_xlabel('$x$')
axes[2].set_ylabel('$-P(x)\\log_2 P(x)$')
axes[2].set_title(f'summands ($H={H:.3f}$ bits)')
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
fig.tight_layout()
mlai.write_figure('bernoulli-entropy-panels.svg', directory='\writeDiagramsDir/information')}

\newslide{Bernoulli Entropy}

\figure{\includediagram{\diagramsDir/information/bernoulli-entropy-panels}{85%}}{Bernoulli($p=0.3$). Left: the distribution. Middle: surprisal $-\log_2 P(x)$\ifdef{bernoulliEnergyFromDistribution} --- energy in bits\endif. Right: the summands $-P(x)\log_2 P(x)$; their total is the entropy $H$.}{bernoulli-entropy-panels}

\newslide{Bernoulli Entropy}

\ifdef{bernoulliEnergyFromDistribution}
\slidesincremental{
* Same coin as the energy overlay: $E=-\log P$ (nats) $\Leftrightarrow$ surprisal in bits
* Entropy $H=\mathbb{E}[E]$ in bits --- fair coin $p=\tfrac12$ gives $H=1$ bit (maximal)
* As $p\to 0$ or $1$: $H\to 0$ --- the deep well makes the outcome nearly certain
}
\else
\slidesincremental{
* Fair coin $p=\tfrac12$: $H=1$ bit --- maximal for a binary variable
* As $p\to 0$ or $1$: $H\to 0$ --- the outcome is nearly certain
* Closed form: $H=-p\log_2 p-(1-p)\log_2(1-p)$
}
\endif


\endif
