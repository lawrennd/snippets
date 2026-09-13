\ifndef{maxwellDemonDetailedBalance}
\define{maxwellDemonDetailedBalance}

\editme

\subsection{Detailed Balance Across the Membrane}

\newslides{What Does the Membrane Do?}

\slides{The JavaScript demon is a *selective membrane*: one speed threshold $v_\star$, opposite rules on each side.}

\slidesincremental{
* Left $\to$ right: pass only if $v > v_\star$ (hot)
* Right $\to$ left: pass only if $v \le v_\star$ (cold)
* Elastic collisions remix velocities; the membrane only gates crossings
}

\speakernotes{Match the canvas: red = hot, blue = cold, green strip = membrane. Threshold in the sim is $v_\star=3$ with initial speed $5$.}

\notes{In the simulation the membrane does not move. A ball on the left is allowed through only when its speed exceeds $v_\star$; a ball on the right is allowed through only when its speed is at most $v_\star$. Between crossings, elastic collisions redistribute energy, so a ball that is cold now can become hot later and then cross. The question is not whether sorting begins — it does — but where the *net* particle and energy flows settle.}

\newslides{Steady State $=$ Balanced Fluxes}

\slides{In a steady state the number of balls leaving left equals the number leaving right — detailed balance of membrane crossings.}

\slidesincremental{
* Assume each side thermalises to a 2D Maxwellian at its own $T_L$, $T_R$
* Particle flux $L\to R$: only the hot tail, $v>v_\star$
* Particle flux $R\to L$: only the cold body, $v\le v_\star$
* Steady state: $\Phi_L^{\mathrm{hot}}(n_L,T_L)=\Phi_R^{\mathrm{cold}}(n_R,T_R)$
}

\speakernotes{Local equilibrium is an approximation: collisions fast compared with crossings. Energy flux need not balance under the same Maxwellians — flag that after the calculation.}

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
Particle-number detailed balance across the membrane is
$$
\Phi^{\mathrm{hot}}(n_L,\beta_L)=\Phi^{\mathrm{cold}}(n_R,\beta_R).
$$
Total ball number $N=N_L+N_R$ and total energy $E=N_L k_B T_L+N_R k_B T_R$ are conserved. For the simulation parameters ($v_\star=3$, mean kinetic energy $12.5$ in code units, equal populations $N_L=N_R$) this fixes the temperatures uniquely.}

\setupplotcode{import numpy as np
from scipy.special import erfc
from scipy.optimize import brentq
import matplotlib.pyplot as plt
import mlai

def flux_total(n, beta):
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
axes[0].set_title('Particle-flux steady state')
axes[0].legend(frameon=False, fontsize=9)
axes[1].plot(v_grid, dS_grid, color='#333333')
axes[1].axvline(v_star, color='gray', ls='--', alpha=0.7)
axes[1].axhline(0.0, color='gray', ls=':', alpha=0.7)
axes[1].scatter([v_star], [delta_S], color='red', zorder=3)
axes[1].set_xlabel(r'threshold $v_\star$')
axes[1].set_ylabel(r'$\Delta S = S_{\mathrm{ss}}-S_0$ (nats)')
axes[1].set_title('Entropy relative to one bath')
fig.tight_layout()
mlai.write_figure('maxwell-membrane-detailed-balance.svg', directory='\writeDiagramsDir/physics')
print(f'T_L={T_L:.3f}, T_R={T_R:.3f}, S0={S0:.2f}, S_ss={S_ss:.2f}, dS={delta_S:.2f}')}

\figure{\includediagram{\diagramsDir/physics/maxwell-membrane-detailed-balance}{85%}}{Left: temperatures on each side of the selective membrane from particle-flux detailed balance at equal populations (simulation energy budget). Right: entropy of the two-Maxwellian state minus the single-temperature equilibrium. The red point is the simulation threshold $v_\star=3$.}{maxwell-membrane-detailed-balance}

\newslides{Temperatures Split; Entropy Falls}

\slides{For the simulation budget, particle-flux balance at equal $N$ yields $T_L\approx 1.9$, $T_R\approx 23$ ($k_B=1$) — a large split.}

\slidesincremental{
* Unconstrained equilibrium: one $T_0=\langle\mathrm{KE}\rangle$, entropy $S_0$
* Membrane steady state: $S_{\mathrm{ss}}<S_0$ (here $\Delta S\approx -24$ nats)
* The gas alone looks like a second-law violation
}

\speakernotes{Live the numbers from the plotcode printout. Canvas entropy is a coarse velocity-bin proxy; this $S$ is the ideal-gas Shannon entropy of two Maxwellians.}

\notes{With $k_B=1$, equal populations, $v_\star=3$ and total energy matching the simulation's mean kinetic energy $12.5$, particle-flux detailed balance gives $T_L\approx 1.94$ and $T_R\approx 23.1$. The ideal-gas Shannon entropy of a 2D Maxwellian chamber (position Stirling term plus velocity differential entropy)
$$
S(N,\beta)=N\left[2+\log\frac{A}{N}-\log\frac{\beta}{2\pi}\right]
$$
falls by about $24$ nats relative to the single-temperature state at the same $N$ and $E$. That drop is the thermodynamic content of the sorting you see on the canvas: hot accumulates on the right, cold on the left, and the joint distribution over $(\mathrm{side},\mathbf{v})$ is more concentrated than the unconstrained Maxwellian.}

\newslides{Maxwellians Are Only an Approximation}

\slides{Particle balance and energy balance cannot both hold for two Maxwellians — the true steady state depletes velocity tails.}

\slidesincremental{
* Hot crossings carry more energy per ball than cold crossings
* Equal *number* fluxes still leave a net *energy* flux under Maxwellians
* Collisions rebuild the tails; the membrane continually sculpts them
* Local-$T$ picture still predicts the direction and an entropy deficit
}

\speakernotes{Do not oversell the numbers as exact NESS values. The point is the ledger: gas entropy down; cost elsewhere.}

\notes{A Maxwellian is symmetric in a way the membrane is not. Conditioning on $v>v_\star$ selects a high-energy set; conditioning on $v\le v_\star$ selects a low-energy set. When the two *number* fluxes match, the *energy* fluxes generally do not. The true non-equilibrium steady state therefore cannot be a pair of perfect Maxwellians: the left hot tail is depleted by leakage, the right cold body is depleted by leakage the other way, and collisions continually refill those sets. The local-temperature calculation remains the right first cut — it predicts a cold left, a hot right, and a lower gas entropy — but the precise $(T_L,T_R)$ pair is an approximation to a non-Maxwellian steady state.}

\newslides{Where Did the Entropy Go?}

\slides{The membrane implements Maxwell's sorting policy. The gas entropy falls; Clausius is not repealed.}

\slidesincremental{
* Prescription: the velocity gate (who may cross)
* No-go: you cannot harvest that $\Delta S$ for free in a cycle
* Next: Szilard makes the bit explicit; Landauer prices erasure
}

\speakernotes{Bridge forward. Ellis locates dissipation at measurement/gating; information ledger locates it at stored outcomes and erasure. Same Clausius, different bookkeeping.}

\notes{The selective membrane is Maxwell's demon written as a dynamical rule. The detailed-balance calculation shows that the rule really does drive the gas toward a lower-entropy steady state. Restoring Clausius requires putting the membrane — or the memory that controls an equivalent trap door — on the thermodynamic ledger. Szilard's engine isolates one bit of that ledger; Landauer's principle prices erasing it. The simulation's ``velocity-bin entropy'' is a coarse proxy for the same story: as sorting proceeds, the displayed histogram entropy typically drops relative to the unsorted gas.}

\endif
