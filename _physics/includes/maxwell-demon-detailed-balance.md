\ifndef{maxwellDemonDetailedBalance}
\define{maxwellDemonDetailedBalance}

\editme

\include{_physics/includes/demon-spatial-compartments.md}

\subsection{Two Ledgers at the Membrane}

\newslide{What Does the Membrane Do?}

\slides{The JavaScript demon is a *selective membrane*: one speed threshold $v_\star$, opposite rules on each side.}

\slidesincremental{
* Left $\to$ right: pass only if $v > v_\star$ (hot)
* Right $\to$ left: pass only if $v \le v_\star$ (cold)
* Elastic collisions remix velocities in the bulks; the membrane only gates crossings
}

\speakernotes{Match the canvas: red = hot, blue = cold. Threshold in the sim is $v_\star=3$ with initial speed $5$. Right bulk heats. The compartments include already drew the extra partitions.}

\notes{In the simulation the membrane does not move. A ball on the left is allowed through only when its speed exceeds $v_\star$; a ball on the right is allowed through only when its speed is at most $v_\star$. Between crossings, elastic collisions in each bulk redistribute energy, so a ball that is cold now can become hot later and then cross. The question is not whether sorting begins --- it does --- but which currents through the gate can vanish together.}

\newslide{Steady State Is Two Ledgers}

\slides{A closed box in steady state needs *both* currents through the gate to vanish. That is not detailed balance.}

\slidesincremental{
* Number current: balls left $\to$ right equal balls right $\to$ left, or density keeps drifting
* Energy current: the two streams carry different energy per ball
* Detailed balance would match every velocity class with its reverse --- the gate forbids that
}

\speakernotes{Name the distinction once. Flux balance of a conserved quantity is necessary for a NESS of that quantity. Detailed balance is stronger: each process equals its reverse. The membrane is non-reciprocal, so velocity-resolved detailed balance fails by construction. Board number versus energy next.}

\notes{For the closed vessel to sit in a non-equilibrium *steady* state, every conserved current through the membrane must vanish. Particle number is conserved, so the number of balls crossing left to right must equal the number crossing right to left, otherwise the bulk densities keep changing. Energy is conserved, so the energy those streams carry must also balance, otherwise one bulk keeps heating and the other cooling.

That pair of flux balances is not detailed balance. Detailed balance would require each velocity class that crosses to be matched by its reverse. The gate refuses: a hot left-to-right crossing has no matching hot right-to-left crossing, because hot balls on the right are reflected. The allowed streams are a high-energy set one way and a low-energy set the other. Equal *counts* are then not equal *energies*.}

\setupplotcode{import numpy as np
from scipy.special import erfc
from scipy.optimize import brentq
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import mlai
import mlai.plot as plot}

\plotcode{cold = '#3a3ae0'
hot = '#e03a3a'

fig, axes = plt.subplots(2, 1, figsize=(10.0, 4.6), sharex=True)
for ax in axes:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 2.2)
    ax.axis('off')

axes[0].text(0.2, 1.7, 'number current', fontsize=13, fontweight='bold', va='center')
axes[0].annotate('', xy=(8.6, 1.15), xytext=(1.4, 1.15),
                 arrowprops=dict(arrowstyle='->', color=hot, lw=2.4))
axes[0].annotate('', xy=(1.4, 0.55), xytext=(8.6, 0.55),
                 arrowprops=dict(arrowstyle='->', color=cold, lw=2.4))
axes[0].text(5.0, 1.42, r'hot $L\to R$', ha='center', color=hot, fontsize=12)
axes[0].text(5.0, 0.22, r'cold $R\to L$', ha='center', color=cold, fontsize=12)
axes[0].text(9.2, 1.15, r'$\Phi_N$', ha='left', va='center', fontsize=13)
axes[0].text(9.2, 0.55, r'$\Phi_N$', ha='left', va='center', fontsize=13)
axes[0].text(5.0, 1.95, 'equal counts (NESS of $N$)', ha='center', fontsize=12)

axes[1].text(0.2, 1.7, 'energy current', fontsize=13, fontweight='bold', va='center')
axes[1].annotate('', xy=(8.6, 1.15), xytext=(1.4, 1.15),
                 arrowprops=dict(arrowstyle='->', color=hot, lw=4.5))
axes[1].annotate('', xy=(1.4, 0.55), xytext=(8.6, 0.55),
                 arrowprops=dict(arrowstyle='->', color=cold, lw=1.4))
axes[1].text(5.0, 1.42, r'hot carries more per ball', ha='center', color=hot, fontsize=12)
axes[1].text(5.0, 0.22, r'cold carries less', ha='center', color=cold, fontsize=12)
axes[1].text(9.2, 1.15, r'$\Phi_E^{\mathrm{hot}}$', ha='left', va='center', fontsize=13)
axes[1].text(9.2, 0.55, r'$\Phi_E^{\mathrm{cold}}$', ha='left', va='center', fontsize=13)
axes[1].text(5.0, 1.95, 'unequal energies (not a NESS of $U$)', ha='center', fontsize=12)

fig.tight_layout()
mlai.write_figure('demon-two-ledgers.svg',
                  directory=r'\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/demon-two-ledgers}{80%}}{Two ledgers at the same gate. For a closed box, a steady bulk *number* requires equal counts both ways. The hot stream carries more energy per ball than the cold stream, so those equal counts are not an energy balance. A steady bulk *energy* would need the lower pair of arrows to match as well.}{demon-two-ledgers}

\newslide{Maxwellians Cannot Close Both}

\slides{Assume Maxwellian bulks at the gate. Then number balance leaves a heat current.}

\slidesincremental{
* Hot crossings carry more energy per ball than cold crossings
* Equal *number* fluxes still leave a net *energy* flux
* Closing energy as well would break number --- unless $T_L=T_R$, which the filter drives away from
* So the distributions *at the gate* are not the bulk Maxwellians
}

\speakernotes{This is the compartments paying rent. The distant left and right may be Maxwellian. The kinetic layers cannot be, because that is the only way a closed box can stop evolving. Do not dive into the $T_L$, $T_R$ numbers until they ask; those numbers force the illegal assumption.}

\notes{Suppose, illegally, that each kinetic layer is the same Maxwellian as its distant bulk, at temperatures $T_L$ and $T_R$. Conditioning on $v>v_\star$ selects a high-energy set; conditioning on $v\le v_\star$ selects a low-energy set. Matching the two *number* fluxes then leaves a net *energy* flux into the right-hand side. Matching the energy fluxes instead leaves a net number flux. The only Maxwellian pair that closes both ledgers is $T_L=T_R$ with no sort --- and at equal temperatures the filter itself drives a current, so that pair is not stationary either.

A closed box can therefore sit still only if the velocity distributions *at the gate* are not the bulk Maxwellians. The extra partitions were not decoration: they mark the contour where the local-equilibrium coarse graining stops being legal. Collisions rebuild the tails in the bulks; the membrane continually sculpts the layers.}

\newslide{A First Cut: Close Only the Number Ledger}

\slides{If we force Maxwellian bulks and balance *counts* only, the temperatures split and gas entropy falls.}

\slidesincremental{
* Assume each bulk thermalises to a 2D Maxwellian at its own $T_L$, $T_R$
* Particle flux $L\to R$: only the hot tail, $v>v_\star$
* Particle flux $R\to L$: only the cold body, $v\le v_\star$
* Number ledger: $\Phi_L^{\mathrm{hot}}(n_L,T_L)=\Phi_R^{\mathrm{cold}}(n_R,T_R)$
}

\speakernotes{These numbers are what you get if you extend local equilibrium up to the gate and ignore the energy ledger. Live $T_L\approx 1.9$, $T_R\approx 23$ from the plot. They are a first cut on direction, not a true NESS.}

\notes{Take equal chamber areas and a 2D ideal gas (the billiard world). On each side the velocity density is Maxwellian,
$$
f(\mathbf{v}\mid\beta)=\frac{\beta}{2\pi}\exp\!\left(-\tfrac{1}{2}\beta v^2\right),\qquad \beta=\frac{1}{k_B T},
$$
with mean kinetic energy $k_B T$ per ball (two quadratic degrees of freedom). The one-way effusion flux through a unit aperture is $\Phi_{\mathrm{tot}}=n/\sqrt{2\pi\beta}$. Restricting to the hot or cold set gives
\begin{align}
\Phi^{\mathrm{hot}}(n,\beta)
&= \frac{n}{\pi}\left[v_\star e^{-\beta v_\star^2/2}+\int_{v_\star}^\infty e^{-\beta v^2/2}\,\mathrm{d}v\right],\\
\Phi^{\mathrm{cold}}(n,\beta)
&= \Phi_{\mathrm{tot}}(n,\beta)-\Phi^{\mathrm{hot}}(n,\beta).
\end{align}
Particle-number balance across the membrane is
$$
\Phi^{\mathrm{hot}}(n_L,\beta_L)=\Phi^{\mathrm{cold}}(n_R,\beta_R).
$$
Total ball number $N=N_L+N_R$ and total energy $E=N_L k_B T_L+N_R k_B T_R$ are conserved. For the simulation parameters ($v_\star=3$, mean kinetic energy $12.5$ in code units, equal populations $N_L=N_R$) this fixes the temperatures uniquely *under the Maxwellian-at-the-gate assumption*. It does not close the energy ledger.}

\plotcode{def flux_total(n, beta):
    return n / np.sqrt(2 * np.pi * beta)

def flux_hot(n, beta, v_star):
    tail = np.sqrt(np.pi / (2 * beta)) * erfc(v_star * np.sqrt(beta / 2.0))
    return (n / np.pi) * (v_star * np.exp(-0.5 * beta * v_star**2) + tail)

def flux_cold(n, beta, v_star):
    return flux_total(n, beta) - flux_hot(n, beta, v_star)

def side_entropy(N, beta, area=1.0):
    # Position (Stirling) + 2D Maxwellian differential entropy; k_B = 1
    return N * (2.0 + np.log(area / N) - np.log(beta / (2 * np.pi)))

N = 39.0
E_tot = N * 12.5
v_star = 3.0
N_L = N_R = N / 2.0
beta0 = N / E_tot
S0 = 2 * side_entropy(N / 2.0, beta0)

def particle_balance(log_beta_L):
    beta_L = np.exp(log_beta_L)
    E_L = N_L / beta_L
    E_R = E_tot - E_L
    if E_R <= 0:
        return 1.0
    beta_R = N_R / E_R
    return flux_hot(N_L, beta_L, v_star) - flux_cold(N_R, beta_R, v_star)

log_beta_L = brentq(particle_balance, -4.0, 1.0)
beta_L = np.exp(log_beta_L)
beta_R = N_R / (E_tot - N_L / beta_L)
T_L, T_R = 1.0 / beta_L, 1.0 / beta_R
S_ss = side_entropy(N_L, beta_L) + side_entropy(N_R, beta_R)
delta_S = S_ss - S0

# Sweep threshold at fixed equal populations / total energy
v_grid = np.linspace(0.5, 6.0, 80)
T_L_grid, T_R_grid, dS_grid = [], [], []
for vs in v_grid:
    def bal(log_bL, vs=vs):
        bL = np.exp(log_bL)
        E_L = N_L / bL
        E_R = E_tot - E_L
        if E_R <= 0:
            return 1.0
        bR = N_R / E_R
        return flux_hot(N_L, bL, vs) - flux_cold(N_R, bR, vs)
    try:
        lb = brentq(bal, -4.5, 1.5)
    except ValueError:
        T_L_grid.append(np.nan); T_R_grid.append(np.nan); dS_grid.append(np.nan)
        continue
    bL = np.exp(lb)
    bR = N_R / (E_tot - N_L / bL)
    T_L_grid.append(1.0 / bL)
    T_R_grid.append(1.0 / bR)
    dS_grid.append(side_entropy(N_L, bL) + side_entropy(N_R, bR) - S0)

fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.8))
axes[0].plot(v_grid, T_L_grid, color='#4488cc', label='$T_L$ (cold side)')
axes[0].plot(v_grid, T_R_grid, color='#cc4444', label='$T_R$ (hot side)')
axes[0].axvline(v_star, color='gray', ls='--', alpha=0.7)
axes[0].axhline(1.0 / beta0, color='gray', ls=':', alpha=0.7)
axes[0].set_xlabel(r'threshold $v_\star$')
axes[0].set_ylabel(r'temperature ($k_B=1$)')
axes[0].set_title('Number-flux balance only')
axes[0].legend(frameon=False, fontsize=9)
axes[1].plot(v_grid, dS_grid, color='#333333')
axes[1].axvline(v_star, color='gray', ls='--', alpha=0.7)
axes[1].axhline(0.0, color='gray', ls=':', alpha=0.7)
axes[1].scatter([v_star], [delta_S], color='red', zorder=3)
axes[1].set_xlabel(r'threshold $v_\star$')
axes[1].set_ylabel(r'$\Delta S = S_{\mathrm{ss}}-S_0$ (nats)')
axes[1].set_title('Entropy relative to one bath')
fig.tight_layout()
mlai.write_figure('maxwell-membrane-detailed-balance.svg', directory=r'\writeDiagramsDir/physics')
print(f'T_L={T_L:.3f}, T_R={T_R:.3f}, S0={S0:.2f}, S_ss={S_ss:.2f}, dS={delta_S:.2f}')}

\figure{\includediagram{\diagramsDir/physics/maxwell-membrane-detailed-balance}{85%}}{Left: temperatures from balancing *number* flux at equal populations, forcing Maxwellian bulks all the way to the gate. Right: entropy of that two-Maxwellian state minus the single-temperature equilibrium. The red point is the simulation threshold $v_\star=3$. These numbers close only one ledger.}{maxwell-membrane-detailed-balance}

\newslide{The Split Is the Illegal Extension}

\slides{For the simulation budget, number-flux balance at equal $N$ yields $T_L\approx 1.9$, $T_R\approx 23$ ($k_B=1$).}

\slidesincremental{
* Unconstrained equilibrium: one $T_0=\langle\mathrm{KE}\rangle$, entropy $S_0$
* This first cut: $S_{\mathrm{ss}}<S_0$ (here $\Delta S\approx -24$ nats)
* The gas *under this assumption* looks like a second-law violation
* The assumption was the Maxwellian gate --- which the energy ledger already forbade
}

\speakernotes{Canvas entropy is a coarse velocity-bin proxy; this $S$ is the ideal-gas Shannon entropy of two Maxwellians. Do not harvest the $\Delta S$. The fork is next: where the entropy is allowed to sit once the gate is not Maxwellian.}

\notes{With $k_B=1$, equal populations, $v_\star=3$ and total energy matching the simulation's mean kinetic energy $12.5$, number-flux balance gives $T_L\approx 1.94$ and $T_R\approx 23.1$. The ideal-gas Shannon entropy of a 2D Maxwellian chamber (position Stirling term plus velocity differential entropy)
$$
S(N,\beta)=N\left[2+\log\frac{A}{N}-\log\frac{\beta}{2\pi}\right]
$$
falls by about $24$ nats relative to the single-temperature state at the same $N$ and $E$. Read that drop as the cost of the illegal coarse graining, not as a machine. Hot accumulates on the right, cold on the left, and the joint distribution over $(\mathrm{side},\mathbf{v})$ looks more concentrated than the unconstrained Maxwellian --- *provided* we pretend the kinetic layers are Maxwellian too. They are not. The true non-equilibrium state depletes the left hot tail and the right cold body; collisions refill those sets in the bulks. The local-temperature calculation remains the right first cut on *direction*. It is not a closed book.}

\include{_physics/includes/demon-resolution-fork.md}

\endif
