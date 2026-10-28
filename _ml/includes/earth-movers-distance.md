\ifndef{earthMoversDistance}
\define{earthMoversDistance}

\editme

\subsection{Earth Mover's Distance}

\notes{Suppose we hold two histograms over the same set of bins --- piles of probability mass on a shared collection of locations. How far apart are they? Euclidean distance on the probability vectors treats every bin as orthogonal to every other: swapping mass between neighbouring bins costs the same as swapping mass between bins that sit far apart in the underlying space. That is usually the wrong geometry. The *earth mover's distance* (EMD) answers the question by asking how cheaply we can rearrange one histogram into the other when moving a unit of mass from bin $i$ to bin $j$ incurs a known *ground cost* $C_{ij}$.}

\slides{
* Two histograms over a shared set of bins
* Euclidean distance on probability vectors ignores bin geometry
* EMD: cheapest way to rearrange one histogram into the other
* Moving mass from bin $i$ to bin $j$ costs $C_{ij}$
}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import mlai
import mlai.plot as plot}

\plotcode{bins = np.array([0, 1, 2])
source = np.array([0.6, 0.4, 0.0])
target = np.array([0.0, 0.3, 0.7])
# Optimal plan under C_ij = |i-j|: ship 0.3 from 0→1, 0.3 from 0→2, 0.4 from 1→2
shipments = [(0, 1, 0.3), (0, 2, 0.3), (1, 2, 0.4)]
colours = {'source': '#4C72B0', 'target': '#DD8452', 'arrow': '#55A868'}

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
width = 0.35
ax.bar(bins - width/2, source, width=width, color=colours['source'],
       label='source $a$', zorder=2)
ax.bar(bins + width/2, target, width=width, color=colours['target'],
       label='target $b$', zorder=2)
for i, j, mass in shipments:
    cost = abs(i - j)
    arrow = FancyArrowPatch(
        (i, source[i] + 0.08), (j, target[j] + 0.08),
        connectionstyle=f'arc3,rad={0.25 if j - i == 1 else 0.45}',
        arrowstyle='-|>', mutation_scale=14,
        color=colours['arrow'], lw=1.8, zorder=3)
    ax.add_patch(arrow)
    mid = 0.5 * (i + j)
    height = 1.05 + 0.15 * (j - i)
    ax.text(mid, height, f'{mass:g} at cost {cost}',
            ha='center', va='bottom', fontsize=11, color=colours['arrow'])
ax.set_xticks(bins)
ax.set_xlabel('bin position')
ax.set_ylabel('probability mass')
ax.set_ylim(0, 1.45)
ax.set_title(r'EMD: cheapest plan to reshape $a$ into $b$ '
             r'($C_{ij}=|i-j|$; work $=1.3$)')
ax.legend(loc='upper right')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.tight_layout()
mlai.write_figure('earth-movers-plan.svg',
                  directory='\writeDiagramsDir/ml')

fig, axes = plt.subplots(1, 2, figsize=plot.big_wide_figsize, sharey=True)
cases = [
    (np.array([1.0, 0.0, 0.0]), np.array([0.0, 0.0, 1.0]),
     r'$a\to b$', 2, r'$\|a-b\|_2=\sqrt{2}$'),
    (np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]),
     r"$a\to b'$", 1, r"$\|a-b'\|_2=\sqrt{2}$"),
]
for ax, (a, b, title, emd, euc) in zip(axes, cases):
    ax.bar(bins - width/2, a, width=width, color=colours['source'],
           label='source', zorder=2)
    ax.bar(bins + width/2, b, width=width, color=colours['target'],
           label='target', zorder=2)
    i = int(np.argmax(a))
    j = int(np.argmax(b))
    arrow = FancyArrowPatch(
        (i, 1.05), (j, 1.05),
        connectionstyle='arc3,rad=-0.35',
        arrowstyle='-|>', mutation_scale=16,
        color=colours['arrow'], lw=2.0, zorder=3)
    ax.add_patch(arrow)
    ax.text(0.5 * (i + j), 1.28, f'EMD $={emd}$',
            ha='center', fontsize=12, color=colours['arrow'])
    ax.set_xticks(bins)
    ax.set_xlabel('bin position')
    ax.set_title(f'{title}\n{euc}')
    ax.set_ylim(0, 1.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
axes[0].set_ylabel('probability mass')
axes[0].legend(loc='upper right')
fig.suptitle(r'Same Euclidean distance; different earth-mover cost '
             r'($C_{ij}=|i-j|$)', y=1.02)
fig.tight_layout()
mlai.write_figure('earth-movers-euclidean.svg',
                  directory='\writeDiagramsDir/ml')}

\newslide{Dirt and Work}

\notes{The classical metaphor is dirt and work. One histogram is a pile of earth; the other is the target landscape. A plan for reshaping the pile specifies how much mass travels from each source bin to each destination bin. The total work is the sum, over all such shipments, of mass times ground cost. The EMD is the work of the *cheapest* such plan. If the ground cost is itself a metric on the bins --- for example Euclidean distance between bin centres --- the EMD coincides with the 1-Wasserstein distance between the two discrete distributions.}

\figure{\includediagram{\diagramsDir/ml/earth-movers-plan}{85%}}{Two histograms on bins $\{0,1,2\}$ and one optimal transport plan under ground cost $C_{ij}=|i-j|$. Green arcs show shipments; total work is $0.3\cdot 1 + 0.3\cdot 2 + 0.4\cdot 1 = 1.3$.}{earth-movers-plan}

\slides{
* Source histogram $=$ pile of earth; target $=$ desired landscape
* A *plan* ships mass from source bins to destination bins
* Work $=$ $\sum$ (mass shipped) $\times$ (ground cost)
* EMD $=$ work of the cheapest plan
* Metric ground cost $\Rightarrow$ EMD $=$ 1-Wasserstein distance
}

\newslide{Why Not Euclidean?}

\notes{Consider three bins on a line at positions $0$, $1$ and $2$, and two distributions that place all their mass on a single bin: $a = (1,0,0)$ and $b = (0,0,1)$. Euclidean distance between $a$ and $b$ is $\sqrt{2}$, the same value we would obtain for $a$ and $b' = (0,1,0)$. Under EMD with ground cost equal to absolute distance on the line, transforming $a$ into $b$ costs $2$ while transforming $a$ into $b'$ costs $1$. Neighbouring bins are cheap to confuse; distant bins are expensive. That is the geometry we want whenever the bins themselves live in a space with meaning --- word embeddings, topic centroids, spatial locations.}

\figure{\includediagram{\diagramsDir/ml/earth-movers-euclidean}{85%}}{Left: move all mass from bin $0$ to bin $2$ (EMD $=2$). Right: move it only to the neighbour (EMD $=1$). Euclidean distance on the probability vectors is $\sqrt{2}$ in both cases.}{earth-movers-euclidean}

\slides{
* Bins on a line at $0$, $1$, $2$
* $a=(1,0,0)$, $b=(0,0,1)$, $b'=(0,1,0)$
* Euclidean: $\|a-b\|_2 = \|a-b'\|_2 = \sqrt{2}$
* EMD with $|i-j|$ ground cost: $a\to b$ costs $2$, $a\to b'$ costs $1$
* Neighbouring bins are cheap to confuse; distant bins are not
}

\newslide{Ground Cost}

\notes{Everything hinges on the ground cost $C$. It encodes which bin-to-bin moves we regard as expensive. Common choices include Euclidean or cosine distance between bin representatives --- for example cluster centroids in an embedding space. The EMD then inherits that geometry: two documents whose topic mass sits on nearby centroids look close; two documents that raise unrelated topics look far, even if raw Euclidean distance on their share vectors would not say so.}

\slides{
* Ground cost $C_{ij}$: price of moving unit mass from bin $i$ to bin $j$
* Typical choices: Euclidean or cosine distance between bin representatives
* EMD inherits the geometry of $C$
* Nearby bins $\Rightarrow$ cheap confusion; unrelated bins $\Rightarrow$ expensive
}

\endif
