\ifndef{boltzmannMemoryTwoWell}
\define{boltzmannMemoryTwoWell}

\editme

\subsection{Boltzmann Memory: Equal Double Well}

\notes{Parrondo, Horowitz and Sagawa insist that memory is physical: outcomes live in metastable states with broken ergodicity [@Parrondo-thermodynamics15]. Draw that claim. A thermal particle in a symmetric double well --- equal depth, barrier high compared with $k_BT$ --- is one bit of Gibbs memory. The bit is *which well*, not an energy bias between the wells.}

\newslides{One Bit as Two Equal Wells}

\slides{Equal depth isolates information from energetics: $E_L=E_R$, so $p_L=p_R=\tfrac12$ at equilibrium.}

\slidesincremental{
* Store: particle trapped in left or right basin (barrier $\gg k_BT$)
* Read: label the basins $0$ and $1$
* Erase: merge to one well --- Landauer pays $\ge k_BT\ln 2$ if the bit was unknown
}

\speakernotes{LO4. Board the three panels. Equal depth means no free-energy preference for $0$ versus $1$. Week 2 named Gibbs--Boltzmann; this is that occupation as a physical bit. Not yet a Boltzmann *machine* --- one unit, zero field.}

\notes{Equal depth is the point. If the wells differed in depth, part of the story would be energetic preference for one label. With $E_L=E_R$ the equilibrium Gibbs occupation is uniform, $p=\tfrac12$, and the thermodynamic cost of resetting an unknown bit is purely informational. Retention is kinetic: rare barrier crossings. That is Landauer's and Bennett's metastable-memory geometry in one picture.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
import mlai}

\plotcode{def double_well(x, barrier=2.5, sep=1.2):
    # Two equal minima near +/- sep; barrier height ~ barrier at x=0
    return barrier * ((x / sep)**2 - 1.0)**2

def merged_well(x, floor=0.15):
    return 0.35 * x**2 + floor

x = np.linspace(-2.2, 2.2, 400)
V_store = double_well(x)
V_erase = merged_well(x)

fig, axes = plt.subplots(1, 3, figsize=(10, 3.2), sharey=True)

# Panel 1: store (particle in left well)
axes[0].plot(x, V_store, 'k', linewidth=2)
axes[0].scatter([-1.2], [0.05], s=80, color='C0', zorder=3)
axes[0].axhline(0, color='gray', linewidth=0.5, alpha=0.5)
axes[0].set_xlim(-2.2, 2.2)
axes[0].set_ylim(-0.2, 3.2)
axes[0].set_title('Store')
axes[0].set_xlabel('$x$')
axes[0].set_ylabel('$V(x)$')
axes[0].text(-1.55, 0.45, '0', fontsize=12)
axes[0].text(1.05, 0.45, '1', fontsize=12)

# Panel 2: read (same potential, labels)
axes[1].plot(x, V_store, 'k', linewidth=2)
axes[1].scatter([1.2], [0.05], s=80, color='C1', zorder=3)
axes[1].set_xlim(-2.2, 2.2)
axes[1].set_title('Read')
axes[1].set_xlabel('$x$')
axes[1].text(-1.55, 0.45, '0', fontsize=12)
axes[1].text(1.05, 0.45, '1', fontsize=12)
axes[1].annotate('', xy=(-1.2, 2.4), xytext=(1.2, 2.4),
                arrowprops=dict(arrowstyle='<->', color='gray'))
axes[1].text(0.0, 2.55, r'bit $=$ basin', ha='center', fontsize=9)

# Panel 3: erase (merged well)
axes[2].plot(x, V_erase, 'k', linewidth=2)
axes[2].scatter([0.0], [0.2], s=80, color='C3', zorder=3)
axes[2].set_xlim(-2.2, 2.2)
axes[2].set_title('Erase / reset')
axes[2].set_xlabel('$x$')
axes[2].text(-0.35, 0.55, r'$\rightarrow$ 0', fontsize=11)
axes[2].text(0.35, 2.4, r'$\geq k_B T\ln 2$', fontsize=10, color='C3')

for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
mlai.write_figure('boltzmann-memory-two-well.svg', directory='\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/boltzmann-memory-two-well}{90%}}{Boltzmann memory: equal-depth double well. Store and read use two metastable basins; erase merges them. Equal depth keeps $E_0=E_1$, so Landauer's cost is informational rather than an energy bias between labels.}{boltzmann-memory-two-well}

\slides{
\includediagram{\diagramsDir/physics/boltzmann-memory-two-well}{80%}
}

\newslides{Landauer on This Geometry}

\slides{Erasing an equiprobable bit compresses two basins into one: $H\to 0$ costs at least $k_BT\ln 2$.}

\slidesincremental{
* Unknown bit: $H(M)=\ln 2$ nats before reset
* Known bit already in the target well: erasure can be free
* Equal wells: no $\Delta F$ between labels --- pure information cost
}

\speakernotes{Connect to the Landauer slide that follows. Ellis / Bennett: the trap-door position *is* already this kind of physical degree of freedom.}

\notes{Landauer's bound applies to the logically irreversible map that sends both labels to a standard state. If the controller already knows the bit and it sits in the target well, there is nothing to compress. If the bit is unknown and equiprobable, phase-space volume halves and the bath must take at least $k_BT\ln 2$. Equal depth makes that statement sharp: there is no free-energy difference between $0$ and $1$ to confuse with the informational cost [@Landauer-irreversibility61; @Bennett-thermodynamics82].}

\newslides{Information Reservoir, One Cell}

\slides{A tape of equal-depth bits exchanges entropy, not energy, with the rest of the ledger.}

\slidesincremental{
* One equal double well $=$ one cell of an information reservoir
* Many such cells $=$ a tape whose Shannon entropy is a thermodynamic resource or debt
* Boltzmann machine $=$ a *network* of such bits with energy $E(s)$ --- week 5
}

\speakernotes{Name ``information reservoir'' once. Do not divert into Mandal--Jarzynski. Parrondo already frames physical memory; the reservoir language isolates the equal-depth idealisation. Optional depth: @Barato-stochastic14.}

\notes{In the thermodynamics of information, an *information reservoir* is a subsystem that can change the entropy balance while exchanging negligible energy --- ideally a sequence of energetically degenerate bits [@Parrondo-thermodynamics15; @Barato-stochastic14]. The equal-depth double well is one physical cell of that idealisation: flipping or randomising the bit changes Shannon entropy without an energy bias between values. A tape of such wells is the reservoir. Resetting the tape is Landauer accounting on the reservoir's entropy. A Boltzmann machine is not this one-bit picture; it is a joint Gibbs distribution $p(s)\propto e^{-E(s)/T}$ over many binary units with couplings. Week 2 named that lineage; week 5 builds the two-spin case. Here the point is the drawable Landauer bit that makes ``memory is physical'' concrete.}

\addreading{@Parrondo-thermodynamics15}{physical memory; metastable states}
\addreading{@Landauer-irreversibility61}{erasure cost}
\addreading{@Barato-stochastic14}{information reservoirs (optional)}

\endif
