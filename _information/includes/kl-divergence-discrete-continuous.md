\ifndef{klDivergenceDiscreteContinuous}
\define{klDivergenceDiscreteContinuous}

\editme

\subsection{Discrete Shannon Entropy Is Bounded}

\slides{Week 3 derived Shannon entropy for discrete $p=(p_1,\ldots,p_n)$.}

\slidesincremental{
* $0 \le H(p) \le \log n$ on $n$ outcomes
* Maximum at uniform; zero on a delta
* Code interpretation: average length cannot beat $H$
}

\newslide{KL Divergence}

\slides{Comparing two distributions needs a functional that is always sensible.}

\slidesincremental{
* $\text{KL}(p\|q) = \sum_i p_i \log(p_i/q_i)$ discrete; $\int p\log(p/q)\,dx$ continuous
* Always $\text{KL}(p\|q) \ge 0$; zero iff $p = q$ (same support)
* Extra surprise when $q$ stands in for $p$ — not a metric, but a directed cost
}

\speakernotes{LO8 setup. Board: $\text{KL}(p\|q)\neq\text{KL}(q\|p)$. Jaynes die week 5 minimised $\text{KL}(p\|r)$ without naming it. Week 7: $m$-projection.}

\notes{KL divergence measures information lost when $q$ is used instead of $p$. It is non-negative in both discrete and continuous settings (with common support). Unlike Shannon entropy, it is defined relative to a reference. MaxEnt and $m$-projections minimise $\text{KL}(\cdot\|r)$; that is why week 4's die optimisation used $\sum_i p_i\log(p_i/r_i)$.}

\newslide{Differential Entropy Is a Different Object}

\slides{Gaussian channel uses $-\int p\log p$ — differential entropy.}

\slidesincremental{
* Can be *negative*; not bounded below
* Not a code-length bound — compare distributions with KL.
}

\notes{For $\mathcal{N}(0,\sigma^2)$, differential entropy is $\frac{1}{2}\log(2\pi e\sigma^2)$ in nats. As $\sigma\to 0$ it diverges negatively. Discrete Shannon entropy stays in $[0,\log n]$. Thermodynamic $S=kH$ in week 1 used the discrete sum form on Boltzmann probabilities. Continuous MaxEnt still works because constraints fix scale; comparing to a reference uses KL, which remains non-negative.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai}

\plotcode{p = np.linspace(0.01, 0.99, 200)
H_bin = -p*np.log2(p) - (1-p)*np.log2(1-p)
sigma = np.linspace(0.15, 3.0, 200)
h_diff = 0.5 * np.log(2 * np.pi * np.e * sigma**2)
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
axes[0].plot(p, H_bin, 'k-', linewidth=2)
axes[0].axhline(1.0, color='gray', linestyle='--', alpha=0.6, label='max ($n=2$)')
axes[0].set_xlabel('$p$'); axes[0].set_ylabel('$H$ (bits)')
axes[0].set_title('Discrete: $0 \\le H \\le \\log n$')
axes[0].legend(fontsize=8)
axes[1].plot(sigma, h_diff, 'C1', linewidth=2)
axes[1].axhline(0, color='gray', linestyle='--', alpha=0.6)
axes[1].set_xlabel('$\\sigma$'); axes[1].set_ylabel('$h$ (nats)')
axes[1].set_title('Gaussian differential entropy')
fig.tight_layout()
mlai.write_figure('entropy-bounded-vs-differential.svg', directory='\writeDiagramsDir/ml')}

\newslide{}

\figure{\includediagram{\diagramsDir/ml/entropy-bounded-vs-differential}{90%}}{Left: binary Shannon entropy is bounded. Right: Gaussian differential entropy can be negative.}{entropy-bounded-vs-differential}


\endif
