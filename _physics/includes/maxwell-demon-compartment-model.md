\ifndef{maxwellDemonCompartmentModel}
\define{maxwellDemonCompartmentModel}

\editme

\subsection{A Compartment Model of the Demon}

\slides{The box as compartments, not as one fluent Maxwellian.}

\slidesincremental{
* Left bulk: roughly local equilibrium at a cold $T_L$
* Right bulk: roughly local equilibrium at a hot $T_R$
* Kinetic layer at the membrane: not in equilibrium
* Optional fourth: the gate itself (the velocity rule)
}

\speakernotes{Three compartments, maybe four. The bulks are far enough from the membrane that collisions restore a Maxwellian; the band at the gate is where the sorting rule acts. We do not resolve the demon here: Worksheet 3 presses the particle-flux versus energy-flux bookkeeping.}

\notes{Maxwell's sentence is a selective membrane. The useful first cut for Worksheet 3 is to *compartmentalise* that picture. Treat each bulk (left of the gate, and right of the gate) as a region that is close to local equilibrium at its own temperature, provided one stays a mean free path or more away from the membrane. Between those bulks sits a kinetic layer where the velocity rule continually removes hot particles one way and cold particles the other. That layer is not a Maxwellian. Counting the membrane itself as a fourth compartment is optional: it is the place where the microscopic gate rule lives. Compartmentalisation here is coarse-graining (assigning a legal description to each region). The transition across the gate is the microscopic detailed balance one then tries to write. The two ledgers that follow ask whether particle flux and energy flux can both close under those descriptions.}

\setupplotcode{import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.set_xlim(0, 10)
ax.set_ylim(0, 4.2)
ax.set_aspect('equal')
ax.axis('off')

def chamber(x0, x1, facecolor, label, sub):
    ax.add_patch(mpatches.FancyBboxPatch(
        (x0, 0.6), x1 - x0, 2.6,
        boxstyle='round,pad=0.02,rounding_size=0.08',
        facecolor=facecolor, edgecolor='#333333', lw=1.5))
    ax.text(0.5 * (x0 + x1), 2.55, label, ha='center', va='center',
            fontsize=12, fontweight='bold', color='#222222')
    ax.text(0.5 * (x0 + x1), 1.55, sub, ha='center', va='center',
            fontsize=10, color='#333333')

chamber(0.4, 3.2, '#ddeeff', 'Left bulk', r'local eq.\ at $T_L$ (cold)')
chamber(3.2, 4.6, '#f5e6c8', 'Kinetic\nlayer', 'not Maxwellian')
chamber(4.6, 7.4, '#ffd5d5', 'Right bulk', r'local eq.\ at $T_R$ (hot)')

# membrane / gate as optional fourth
ax.plot([3.9, 3.9], [0.6, 3.2], color='#2ca02c', lw=4, solid_capstyle='butt')
ax.annotate('gate\n$v_\\star$', xy=(3.9, 3.35), xytext=(3.9, 3.95),
            ha='center', va='bottom', fontsize=10, color='#2ca02c',
            arrowprops=dict(arrowstyle='-', color='#2ca02c', lw=1))

ax.annotate('', xy=(4.45, 2.1), xytext=(3.35, 2.1),
            arrowprops=dict(arrowstyle='->', color='#cc4444', lw=1.6))
ax.text(3.9, 2.35, r'hot $v>v_\star$', ha='center', fontsize=9, color='#cc4444')
ax.annotate('', xy=(3.35, 1.5), xytext=(4.45, 1.5),
            arrowprops=dict(arrowstyle='->', color='#4488cc', lw=1.6))
ax.text(3.9, 1.15, r'cold $v\leq v_\star$', ha='center', fontsize=9, color='#4488cc')

ax.text(8.7, 2.6, 'Optional fourth:\nthe gate rule itself',
        ha='center', va='center', fontsize=10, color='#333333',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='#aaaaaa'))
ax.annotate('', xy=(4.05, 3.7), xytext=(7.5, 3.1),
            arrowprops=dict(arrowstyle='->', color='#888888', lw=1))

ax.set_title("Compartment model of Maxwell's membrane", fontsize=13, pad=8)
mlai.write_figure('maxwell-demon-compartment-model.svg',
                  directory='\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/maxwell-demon-compartment-model}{85%}}{Three compartments for Worksheet 3: cold left bulk, hot right bulk, and a non-equilibrium kinetic layer at the membrane. The green gate is an optional fourth compartment --- the microscopic velocity rule. Number flux and energy flux are the two ledgers that must both close.}{maxwell-demon-compartment-model}

\endif
