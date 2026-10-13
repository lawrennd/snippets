\ifndef{multinomialEntropy}
\define{multinomialEntropy}
\editme

\subsection{Multinomial / Categorical Entropy}

\notes{One draw from a multinomial (a categorical distribution) on $K$ categories with probabilities $\mathbf{p}=(p_1,\ldots,p_K)$ has entropy
$$
H = -\sum_{k=1}^K p_k\log_2 p_k
$$
bits --- exactly Shannon's formula. The four-outcome table from the expectation example is already a categorical; we reuse those probabilities here.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{# Same four-outcome distribution as the expectation / entropy example
cats = np.array([1, 2, 3, 4])
probs = np.array([0.3, 0.2, 0.1, 0.4])
surprisal = -np.log2(probs)
contrib = probs * surprisal
H = contrib.sum()

fig, axes = plt.subplots(1, 3, figsize=plot.big_wide_figsize)
colours = ['#4C72B0', '#DD8452', '#55A868']
axes[0].bar(cats, probs, color=colours[0], width=0.6)
axes[0].set_xticks(cats)
axes[0].set_xlabel('category $y$')
axes[0].set_ylabel('$P(y)$')
axes[0].set_title('categorical (four outcomes)')
axes[0].set_ylim(0, 0.5)

axes[1].bar(cats, surprisal, color=colours[1], width=0.6)
axes[1].set_xticks(cats)
axes[1].set_xlabel('category $y$')
axes[1].set_ylabel('$-\\log_2 P(y)$')
axes[1].set_title('surprisal')

axes[2].bar(cats, contrib, color=colours[2], width=0.6)
axes[2].set_xticks(cats)
axes[2].set_xlabel('category $y$')
axes[2].set_ylabel('$-P(y)\\log_2 P(y)$')
axes[2].set_title(f'summands ($H={H:.3f}$ bits)')
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
fig.tight_layout()
mlai.write_figure('multinomial-entropy-panels.svg', directory='\writeDiagramsDir/information')}

\newslide{Categorical Entropy}

\figure{\includediagram{\diagramsDir/information/multinomial-entropy-panels}{85%}}{The four-outcome distribution from the expectation example, now in bits. Right-hand summands total $H$; category $y=3$ is rarest (highest surprisal) but contributes modestly because $P(3)$ is small.}{multinomial-entropy-panels}

\newslide{Categorical Entropy}

\slidesincremental{
* One multinomial trial $=$ categorical: $H=-\sum_k p_k\log_2 p_k$
* Uniform on $K$ symbols: $H=\log_2 K$ --- maximal
* $n$ i.i.d. trials: entropies add; the count vector is more subtle
}

\notes{For $n$ i.i.d. categorical draws the joint entropy is $nH$; the entropy of the *count* vector (the multinomial sufficient statistic) is smaller because many sequences share the same counts. Today we only need the single-draw / categorical case --- it is Shannon's sum in pure form.}

\endif
