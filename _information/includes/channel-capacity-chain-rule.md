\ifndef{channelCapacityChainRule}
\define{channelCapacityChainRule}

\editme

\subsection{Scaffolding, Not Outcomes}

\newslide{Chain Rule, Mutual Information, Capacity}

\slides{Four results we will need later --- stated, not proved today.}

\slidesincremental{
* Chain rule: $H(X,Y) = H(X) + H(Y|X)$
* Mutual information: $I(X;Y) = H(X)-H(X|Y) = H(X)+H(Y)-H(X,Y)$
* Capacity: no rate above $C$; achieving $C$ requires the capacity-achieving $p(x)$
* Data processing: if $X\to Y\to Z$ is Markov, $I(X;Z)\le I(X;Y)$
}

\speakernotes{Define $I$ from the chain rule. State DPI; do not prove. Proof and the information bottleneck are week 8 (LO10). Capacity remains this week's no-go/prescription pair.}

\notes{The chain rule $H(X,Y)=H(X)+H(Y|X)$ is the algebraic source of multi-information. Mutual information $I(X;Y)=H(X)-H(X|Y)$ is the pairwise case; we do not yet treat $n>2$. Channel capacity $C$ is a no-go on rate; the capacity-achieving input distribution is the prescription. The data-processing inequality is the no-go on $I$: processing cannot create information. Cover and Thomas Theorem 2.8.1 is the reading; the proof waits for week 8, when $I$ is first-class.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai}

\plotcode{eps = 0.1
p = np.linspace(0.01, 0.99, 200)
H = lambda q: -q*np.log2(q)-(1-q)*np.log2(1-q)
I = H(p) - H(eps)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(p, I, linewidth=2)
ax.scatter([0.5], [H(0.5) - H(eps)], s=80, color='red', zorder=3)
ax.set_xlabel('input bias $p(x=1)$')
ax.set_ylabel('$I(X;Y)$ (bits)')
ax.set_title('Binary symmetric channel')
mlai.write_figure('bsc-capacity.svg', directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/bsc-capacity}{70%}}{Mutual information for a binary symmetric channel; capacity is achieved at uniform input.}{bsc-capacity}

\endif
