\ifndef{demonSpatialCompartments}
\define{demonSpatialCompartments}

\editme

\subsection{Compartments Around the Membrane}

\slides{Draw extra partitions. Local equilibrium is allowed only where collisions can restore it.}

\slidesincremental{
* Distant left, distant right: far from the gate --- Maxwellian at $T_L$, $T_R$
* Kinetic layers against the membrane: selected arrivals, not remixed
* The membrane itself is the JS rule: hot left $\to$ right, cold right $\to$ left
}

\speakernotes{Match the canvas: red hot, blue cold, threshold $v_\star=3$. Hot crosses left to right, so the *right* bulk heats. The new move is spatial: two extra dashed partitions. Do not start the flux ledgers yet.}

\notes{The canvas already implements Maxwell's sorting as a dynamical rule. A ball on the left crosses only when its speed exceeds $v_\star$; a ball on the right crosses only when its speed is at most $v_\star$. Hot therefore accumulates on the right and cold on the left. That is the JS convention, and we keep it.

The new move is to refuse a single temperature on each side. Insert two extra partitions, distant from the membrane. Between the left wall and the left partition sits a *bulk*: many collisions, few crossings. Between the right partition and the right wall sits another bulk. Against the membrane, on each side, sits a kinetic layer of thickness a mean free path or so. In the bulks we may argue for local equilibrium --- the same timescale split as the grouping identity, $p_i$ relaxing quickly to $\pi_i$. In the layers we may not. What hits the gate is a selected tail or body; what just crossed has not remixed. The neighbourhood of the membrane is not at equilibrium.}

\setupplotcode{import matplotlib.pyplot as plt
import matplotlib.patches as patches
import mlai
import mlai.plot as plot}

\plotcode{cold = '#3a3ae0'
hot = '#e03a3a'
gate = '#2db82d'
layer = '#d8d8d8'

fig, ax = plt.subplots(figsize=(10.0, 4.2))
ax.set_xlim(0.0, 10.0)
ax.set_ylim(0.0, 5.0)
ax.axis('off')

# Outer vessel
ax.add_patch(patches.FancyBboxPatch((0.45, 0.95), 9.1, 3.25,
                                    boxstyle='square,pad=0',
                                    facecolor='white', edgecolor='k', lw=2.0,
                                    zorder=1))

regions = [
    (0.45, 2.25, cold, 0.22, 'left bulk\nlocal eq\n$T_L$'),
    (2.70, 1.75, layer, 0.95, 'kinetic\nlayer'),
    (4.45, 1.10, gate, 0.55, r'$v_\star$'),
    (5.55, 1.75, layer, 0.95, 'kinetic\nlayer'),
    (7.30, 2.25, hot, 0.22, 'right bulk\nlocal eq\n$T_R$'),
]
for x, w, color, alpha, _ in regions:
    ax.add_patch(patches.Rectangle((x, 0.95), w, 3.25,
                                   facecolor=color, alpha=alpha,
                                   edgecolor='none', zorder=2))

# Extra partitions (dashed) and membrane edges
for x in (2.70, 7.30):
    ax.plot([x, x], [0.95, 4.20], ls='--', color='k', lw=1.4, zorder=3)
ax.plot([4.45, 4.45], [0.95, 4.20], color='k', lw=1.0, zorder=3)
ax.plot([5.55, 5.55], [0.95, 4.20], color='k', lw=1.0, zorder=3)

labels = [
    (1.575, 'left bulk\nlocal eq\n$T_L$', 11),
    (3.575, 'not a\nMaxwellian', 10),
    (5.000, r'$v_\star$', 13),
    (6.425, 'not a\nMaxwellian', 10),
    (8.425, 'right bulk\nlocal eq\n$T_R$', 11),
]
for x, text, fs in labels:
    ax.text(x, 2.55, text, ha='center', va='center', fontsize=fs, zorder=4)

ax.annotate('', xy=(5.70, 3.55), xytext=(4.30, 3.55),
            arrowprops=dict(arrowstyle='->', color=hot, lw=2.2), zorder=5)
ax.text(5.00, 3.78, r'hot $v>v_\star$', ha='center', color=hot, fontsize=11)
ax.annotate('', xy=(4.30, 1.45), xytext=(5.70, 1.45),
            arrowprops=dict(arrowstyle='->', color=cold, lw=2.2), zorder=5)
ax.text(5.00, 1.12, r'cold $v\leq v_\star$', ha='center', color=cold, fontsize=11)

ax.text(1.575, 0.55, 'cold', ha='center', color=cold, fontsize=12)
ax.text(8.425, 0.55, 'hot', ha='center', color=hot, fontsize=12)
ax.text(5.00, 4.45, 'membrane (JS rule)', ha='center', fontsize=12)
ax.text(2.70, 4.45, 'extra partition', ha='center', fontsize=10, color='#444444')
ax.text(7.30, 4.45, 'extra partition', ha='center', fontsize=10, color='#444444')

mlai.write_figure('demon-spatial-compartments.svg',
                  directory=r'\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/demon-spatial-compartments}{85%}}{The vessel with two extra partitions. Distant bulks may sit at local equilibrium, $T_L$ on the left and $T_R$ on the right. The kinetic layers against the membrane cannot: the gate selects a tail one way and a body the other. Arrows follow the JS convention --- hot left to right, cold right to left --- so the right bulk heats.}{demon-spatial-compartments}

\newslide{Bulks Are Groups; the Gate Is Not}

\slides{The extra partitions are a coarse graining. They are legal only where mixing is fast.}

\slidesincremental{
* Each bulk: the die's move --- keep $T$, $N$, $E$; refuse which molecule
* Kinetic layer: the faces have just been selected; $\pi_i$ has not returned
* We may write a Maxwellian in the distant compartments. Not at the gate
}

\speakernotes{Callback to grouping-as-macrostate and local-equilibrium-grouping. Do not re-derive $H=H(w)+\sum w_i H(p_i)$. The next include is the two ledgers: number current versus energy current.}

\notes{Each distant bulk is a group in the sense we already have. We keep a few intensive and extensive numbers and refuse the molecular faces. Local equilibrium is the claim that collisions inside the group are fast compared with exchange across its boundary, so the within-group law has settled to $\pi_i$. That claim is plausible far from the membrane. It is not plausible in the kinetic layer. The gate is a non-reciprocal filter: the left-going stream and the right-going stream are different velocity sets. Arrivals are conditioned on that filter, and a ball that has just crossed has not yet collided enough times to forget how it entered. Extending a Maxwellian up to the membrane is the same mistake as treating $\{1,2,3\}$ as already mixed when the cube has only just shown the group label.}

\endif
