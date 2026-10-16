\ifndef{discreteOptimalTransport}
\define{discreteOptimalTransport}

\editme

\subsection{Discrete Optimal Transport}

\notes{The earth-mover picture formalises as a linear programme. Write the source histogram as a non-negative vector $a\in\mathbb{R}^{m}$ with $\sum_i a_i=1$, and the target as $b\in\mathbb{R}^{n}$ with $\sum_j b_j=1$. A *coupling* (or *transport plan*) is a matrix $\Pi\in\mathbb{R}^{m\times n}_{\ge 0}$ whose row sums recover $a$ and whose column sums recover $b$:
$$
\Pi\mathbf{1}=a,\qquad \Pi^{\top}\mathbf{1}=b.
$$
Entry $\Pi_{ij}$ is the mass shipped from bin $i$ to bin $j$. Given a ground-cost matrix $C\in\mathbb{R}^{m\times n}$, the work of a plan is the Frobenius pairing $\langle\Pi,C\rangle=\sum_{ij}\Pi_{ij}C_{ij}$. The earth mover's distance is the cheapest such work,
$$
\mathrm{EMD}(a,b;C)=\min_{\Pi\ge 0:\,\Pi\mathbf{1}=a,\,\Pi^{\top}\mathbf{1}=b}\langle\Pi,C\rangle.
$$
This is Kantorovich's formulation of optimal transport. Algorithms such as the network simplex (exposed in Python by `ot.emd` / `ot.emd2` in the POT library) return both the optimal cost and one optimal coupling $\Pi^\star$.}

\slides{
* Source $a$, target $b$: probability vectors
* Coupling $\Pi\ge 0$ with $\Pi\mathbf{1}=a$, $\Pi^{\top}\mathbf{1}=b$
* Work $\langle\Pi,C\rangle=\sum_{ij}\Pi_{ij}C_{ij}$
* $\mathrm{EMD}(a,b;C)=\min\langle\Pi,C\rangle$ over couplings
* Kantorovich OT; solved by network simplex (`ot.emd2`)
}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import mlai
import mlai.plot as plot}

\plotcode{a = np.array([0.6, 0.4, 0.0])
b = np.array([0.0, 0.3, 0.7])
# Optimal coupling under C_ij = |i-j| (same plan as the EMD snippet)
Pi = np.array([
    [0.0, 0.3, 0.3],
    [0.0, 0.0, 0.4],
    [0.0, 0.0, 0.0],
])
C = np.abs(np.arange(3)[:, None] - np.arange(3)[None, :])
assert np.allclose(Pi.sum(axis=1), a)
assert np.allclose(Pi.sum(axis=0), b)
work = round(float((Pi * C).sum()), 10)

colours = {'source': '#4C72B0', 'target': '#DD8452'}
fig, axes = plt.subplots(1, 2, figsize=plot.big_wide_figsize)

# Left: ground cost
ax = axes[0]
im = ax.imshow(C, cmap='YlOrRd', vmin=0, vmax=2)
for i in range(3):
    for j in range(3):
        ax.text(j, i, f'{C[i, j]:g}', ha='center', va='center',
                fontsize=14, color='black')
ax.set_xticks(range(3))
ax.set_yticks(range(3))
ax.set_xlabel(r'target bin $j$')
ax.set_ylabel(r'source bin $i$')
ax.set_title(r'ground cost $C_{ij}=|i-j|$')
fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

# Right: optimal coupling with marginal annotations
ax = axes[1]
im = ax.imshow(Pi, cmap='Greens', vmin=0, vmax=0.5)
for i in range(3):
    for j in range(3):
        txt = f'{Pi[i, j]:g}' if Pi[i, j] > 0 else '·'
        weight = 'bold' if Pi[i, j] > 0 else 'normal'
        ax.text(j, i, txt, ha='center', va='center',
                fontsize=14, fontweight=weight, color='black')
# Highlight support of Pi*
for i, j in zip(*np.nonzero(Pi)):
    ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False,
                           edgecolor='#222222', lw=1.5))
ax.set_xticks(range(3))
ax.set_yticks(range(3))
ax.set_xticklabels([f'$b_{j}={b[j]:g}$' for j in range(3)])
ax.set_yticklabels([f'$a_{i}={a[i]:g}$' for i in range(3)])
ax.set_xlabel(r'target bin $j$ (column sums $=b$)')
ax.set_ylabel(r'source bin $i$ (row sums $=a$)')
ax.set_title(rf'optimal coupling $\Pi^\star$ '
             rf'(work $\langle\Pi^\star,C\rangle={work:g}$)')
fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
fig.tight_layout()
mlai.write_figure('discrete-ot-coupling.svg',
                  directory='\writeDiagramsDir/ml')}

\newslide{Coupling Matrix}

\notes{Returning to the three-bin histograms from the earth-mover example, $a=(0.6,0.4,0)$ and $b=(0,0.3,0.7)$, the ground cost $C_{ij}=|i-j|$ and one optimal coupling are shown below. Non-zero entries of $\Pi^\star$ are the shipments we drew as arcs: $0.3$ from $0\to 1$, $0.3$ from $0\to 2$, and $0.4$ from $1\to 2$. Row $i$ sums to $a_i$; column $j$ sums to $b_j$. The Frobenius pairing recovers the work $1.3$.}

\figure{\includediagram{\diagramsDir/ml/discrete-ot-coupling}{90%}}{Left: ground-cost matrix $C_{ij}=|i-j|$. Right: an optimal coupling $\Pi^\star$ for $a=(0.6,0.4,0)$ and $b=(0,0.3,0.7)$. Boxed cells are the support of the plan; $\langle\Pi^\star,C\rangle=1.3$.}{discrete-ot-coupling}

\slides{
* $\Pi_{ij}$: mass from source bin $i$ to target bin $j$
* Row sums $=a$, column sums $=b$
* Same three-bin example: work $\langle\Pi^\star,C\rangle=1.3$
* Non-zeros of $\Pi^\star$ are the arcs drawn in the EMD figure
}

\newslide{Splitting Mass}

\notes{Kantorovich's formulation allows a single source bin to ship to several targets --- mass may *split*. That is essential here: bin $0$ must supply both bin $1$ and bin $2$. Monge's older map $T$ would assign each source location to exactly one destination; when $a$ and $b$ have different supports, or when mass must split, no such map exists. The coupling matrix is therefore the right object for discrete histograms, and it is what libraries such as POT return.}

\slides{
* Kantorovich: mass may split across several destinations
* Monge map $T$: each source goes to one target only
* Histograms with unequal support need splitting $\Rightarrow$ couplings
* POT's `ot.emd` returns $\Pi^\star$; `ot.emd2` returns the cost
}

\endif
