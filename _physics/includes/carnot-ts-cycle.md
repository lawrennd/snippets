\ifndef{carnotTsCycle}
\define{carnotTsCycle}

\editme

\subsection{The Carnot Cycle on $T$-$S$}

\notes{A reversible engine is the most efficient you can be, such an engine is what Carnot studied. Under the Helmholtz split, $\beta\,\mathrm{d}S=\mathrm{d}Q$. When they talked about heat flow and conservation, what they were actually measuring the flow of was entropy. This was the source of the caloric that they believed to be conserved. The ideal Carnot cycle makes that visible. It can be drawn on a temperature-entropy diagram as a square. That square is our picture, not his. Before drawing it, it is worth hearing what he actually asked.}

\newslide{The Fall of Caloric}

\slides{Carnot compared the motive power of heat to a waterfall. He did not know whether the work was proportional to the height.}

\figure{\includepng{\diagramsDir/physics/carnot-1824-fig1}{28%}}{Carnot's own plate, 1824. Cylinder $ab$, piston $cd$, body $A$ the furnace, body $B$ the refrigerator. This is the mill as he drew it: not a waterwheel, a piston and two reservoirs. Vectorised from *Réflexions sur la puissance motrice du feu* (Wikimedia Commons, public domain).}{carnot-1824-fig1-ts}

\notes{We have already seen the mill: caloric falls from a hot body to a cold one, and the same caloric arrives at the bottom. His own plate is not a waterwheel. It is a cylinder and a movable piston, and two bodies, $A$ and $B$, held at different temperatures. The waterfall lives in the text, not in the figure [@Carnot-reflexions24].}

\notes{The sentence is careful. The motive power of a waterfall depends on its height and on the quantity of the liquid. The motive power of heat depends on the quantity of caloric and on what he will call the *height of its fall* --- the difference of temperature between the bodies exchanging it. In a waterfall the work is exactly proportional to the difference of level. In the fall of caloric, he says, the motive power undoubtedly increases with the difference of temperature --- but he does not know whether it is proportional. Would the same quantity of caloric falling from $100^\circ$ to $50^\circ$ furnish more or less motive power than the same caloric falling from $50^\circ$ to zero? That is his question. Sit with it before the square appears. The square is our answer, not his. He identified the fall, and the reversible ceiling. He did not write $W=\Delta T\times\Delta S$.}

\speakernotes{Do not rush the $100$--to--$50$ question. The square is waiting. He did not have entropy. Point at $A$ and $B$: furnace and refrigerator. The piston is the mill wheel.}

\newslide{The Mill, Drawn as a Rectangle}

\slides{Replace height by temperature and mass of water by entropy, and the mill is already a rectangle.}

\figure{\includediagram{\diagramsDir/physics/carnot-mill-square}{85%}}{The same cycle twice. Left: a water mill on height against mass of water. Fill the bucket at the top, let it descend, empty it, return the empty bucket. The water is not consumed; the work is $g\,\Delta h\,\Delta m$. Right: a reversible heat engine on $T$ against $S$. The conserved quantity in the reversible model is what we now call entropy. The vertical brace is Carnot's fall --- the difference between the reservoirs --- not the downward stroke of the working body.}{carnot-mill-square}

\slidesincremental{
* Height $h$ $\leftrightarrow$ temperature $T$
* Mass of water $\Delta m$ $\leftrightarrow$ entropy transferred $\Delta S$
* Fill at the top $\leftrightarrow$ take in entropy at $T_h$
* Loaded bucket descends $\leftrightarrow$ isolated expansion (the working body cools; no heat transfer)
* Empty at the bottom $\leftrightarrow$ reject entropy at $T_c$
* Empty bucket returns $\leftrightarrow$ isolated compression
* Work $g\,\Delta h\,\Delta m$ $\leftrightarrow$ work $\Delta T\times\Delta S$
}

\notes{If you take the mill seriously as a cycle, it is already a rectangle. Fill the bucket at the top: mass comes in at height $h_h$. The loaded bucket descends, the shaft turns. Empty at the bottom. Return the empty bucket. The water is not consumed. The work is $g\,\Delta h\,\Delta m$.}

\notes{Replace height by temperature and mass of water by entropy, and you have the $T$--$S$ square. The conserved quantity in the reversible model is what we now call entropy. That is an interpretation of his caloric, not a claim that he had already discovered it without naming it. Falk reads Clausius's entropy as a resurrection of caloric; Meyn draws the mill as this rectangle. Historians are not unanimous, and they should not be: the identification is a reading of the reversible model, not a reconstruction of what was in his head. What we can say is narrower. Once the transferred quantity is entropy and the height is thermodynamic temperature, the product is exactly the area, and proportionality is no longer a question. For a computer scientist this is a beautiful example of how choosing the right state variable turns a complicated process into simple geometry.}

\speakernotes{Point at the vertical brace on both panels. That is Carnot's fall. Easy mistake: taking the downward adiabat for the fall. The downward stroke lowers the temperature of the working substance without exchanging entropy. The fall is the difference between the reservoirs, across the whole cycle.}

\newslide{The Square}

\slides{The ideal Carnot cycle on a $T$--$S$ diagram is a square.}

\speakernotes{As taught 27 October, after Helmholtz, answering a question. Click through the legs as on the visualiser. Temperature up, entropy across. Clockwise is an engine.}

\setupplotcode{import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Rectangle
import mlai}

\plotcode{diagrams = '\writeDiagramsDir/physics'
Sc, Sh = 1.0, 2.4
Tc, Th = 0.8, 2.2
A = (Sc, Th)
B = (Sh, Th)
C = (Sh, Tc)
D = (Sc, Tc)
hot_c = '#C44E52'
cold_c = '#4C72B0'
adiab_c = '#333333'
work_c = '#DD8452'
ink = '#222222'
legs = [
    dict(p0=A, p1=B, color=hot_c,
         label='expansion', sub=r'isothermal, $T_h$'),
    dict(p0=B, p1=C, color=adiab_c,
         label='isolated cool', sub='adiabatic'),
    dict(p0=C, p1=D, color=cold_c,
         label='contraction', sub=r'isothermal, $T_c$'),
    dict(p0=D, p1=A, color=adiab_c,
         label='isolated heat', sub='adiabatic'),
]
titles = [
    r'The $T$–$S$ plane',
    'Start at some temperature',
    'Temperature constant, entropy increases',
    'The system cools rapidly',
    'Entropy comes back down',
    'Heat rapidly: the square',
    'Four legs of the mill',
    r'Work extracted: $\Delta T\times\Delta S$',
]

def _axes(title):
    fig, ax = plt.subplots(figsize=(7.2, 5.6))
    ax.set_xlim(0.15, 3.05)
    ax.set_ylim(0.25, 2.85)
    ax.set_aspect('equal')
    ax.set_xlabel(r'entropy $S$')
    ax.set_ylabel(r'temperature $T$')
    ax.set_xticks([Sc, Sh])
    ax.set_xticklabels([r'$S_c$', r'$S_h$'])
    ax.set_yticks([Tc, Th])
    ax.set_yticklabels([r'$T_c$', r'$T_h$'])
    ax.axhline(Th, color=hot_c, ls='--', lw=1.0, alpha=0.45, zorder=0)
    ax.axhline(Tc, color=cold_c, ls='--', lw=1.0, alpha=0.45, zorder=0)
    ax.set_title(title)
    for spine in ax.spines.values():
        spine.set_color('#444444')
    return fig, ax

def _save(frame):
    mlai.write_figure(f'carnot-ts{frame:03d}.svg', directory=diagrams)

def _dot(ax, p, color=ink):
    ax.plot(p[0], p[1], 'o', color=color, ms=8, zorder=5)

def _draw_leg(ax, p0, p1, color, arrow=False, lw=2.7):
    if arrow:
        ax.add_patch(FancyArrowPatch(
            p0, p1, arrowstyle='-|>', mutation_scale=16,
            lw=lw, color=color, shrinkA=0, shrinkB=2.5,
            clip_on=False, zorder=3))
    else:
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=color, lw=lw,
                solid_capstyle='round', zorder=3)

def _label_leg(ax, p0, p1, text, sub, color):
    mx = 0.5 * (p0[0] + p1[0])
    my = 0.5 * (p0[1] + p1[1])
    if abs(p1[0] - p0[0]) > abs(p1[1] - p0[1]):
        ha = 'center'
        if my > 1.4:
            va, offx, offy = 'bottom', 0.0, 0.08
        else:
            va, offx, offy = 'top', 0.0, -0.08
    else:
        va = 'center'
        if mx > 1.6:
            ha, offx, offy = 'left', 0.10, 0.0
        else:
            ha, offx, offy = 'right', -0.10, 0.0
    ax.text(mx + offx, my + offy, text + '\n' + sub, color=color,
            ha=ha, va=va, fontsize=11, linespacing=1.25)

# 000: axes
fig, ax = _axes(titles[0])
_save(0)

# 001: start
fig, ax = _axes(titles[1])
_dot(ax, A, hot_c)
_save(1)

# 002--005: add one leg at a time
for n_done in range(1, 5):
    fig, ax = _axes(titles[1 + n_done])
    _dot(ax, A, hot_c)
    for i in range(n_done):
        lg = legs[i]
        _draw_leg(ax, lg['p0'], lg['p1'], lg['color'], arrow=True)
        _dot(ax, lg['p1'], lg['color'])
    _save(1 + n_done)

# 006: labels on the closed square
fig, ax = _axes(titles[6])
_dot(ax, A, hot_c)
for lg in legs:
    _draw_leg(ax, lg['p0'], lg['p1'], lg['color'], arrow=True)
    _dot(ax, lg['p1'], lg['color'])
    _label_leg(ax, lg['p0'], lg['p1'], lg['label'], lg['sub'], lg['color'])
_save(6)

# 007: work is the area
fig, ax = _axes(titles[7])
ax.add_patch(Rectangle(
    (Sc, Tc), Sh - Sc, Th - Tc,
    facecolor=work_c, alpha=0.28, edgecolor='none', zorder=1))
_dot(ax, A, hot_c)
for lg in legs:
    _draw_leg(ax, lg['p0'], lg['p1'], lg['color'], arrow=True)
    _dot(ax, lg['p1'], lg['color'])
ax.annotate(
    '', xy=(Sc - 0.22, Th), xytext=(Sc - 0.22, Tc),
    arrowprops=dict(arrowstyle='<->', color=ink, lw=1.2), zorder=4)
ax.text(Sc - 0.30, 0.5 * (Th + Tc), r'$\Delta T$', ha='right', va='center',
        color=ink, fontsize=14)
ax.annotate(
    '', xy=(Sh, Tc - 0.20), xytext=(Sc, Tc - 0.20),
    arrowprops=dict(arrowstyle='<->', color=ink, lw=1.2), zorder=4)
ax.text(0.5 * (Sc + Sh), Tc - 0.32, r'$\Delta S$', ha='center', va='top',
        color=ink, fontsize=14)
ax.text(0.5 * (Sc + Sh), 0.5 * (Tc + Th),
        r'$W=\Delta T\times\Delta S$', ha='center', va='center',
        color=ink, fontsize=15)
_save(7)

# 008: real engine cuts the other two corners; same ΔT, same ΔS
fig, ax = _axes('In practice: cut two corners, not a smaller square')
ax.add_patch(Rectangle(
    (Sc, Tc), Sh - Sc, Th - Tc,
    facecolor=work_c, alpha=0.12, edgecolor='none', zorder=1))
for lg in legs:
    _draw_leg(ax, lg['p0'], lg['p1'], lg['color'], arrow=False, lw=1.6)
T2 = Tc + (2.0 / 3.0) * (Th - Tc)
T4 = Th + Tc - T2
inner = Polygon(
    [(Sc, Tc), (Sc, T2), (Sh, Th), (Sh, T4)],
    closed=True, facecolor='#55A868', alpha=0.35,
    edgecolor='#2E7D4F', lw=2.2, zorder=2)
ax.add_patch(inner)
_dot(ax, (Sh, Th), hot_c)
_dot(ax, (Sc, Tc), cold_c)
ax.text(0.5 * (Sc + Sh), 0.5 * (Tc + Th),
        r'$\eta\sim$ area ratio', ha='center', va='center',
        color=ink, fontsize=14)
_save(8)

# p–V: same four legs, chosen so the loop is readable (not the T–S numbers)
gamma = 1.4
nR = 1.0
T_hot, T_cold = 1.4, 1.0
Va, Vb = 1.0, 1.5
Vc = Vb * (T_hot / T_cold) ** (1.0 / (gamma - 1.0))
Vd = Va * (T_hot / T_cold) ** (1.0 / (gamma - 1.0))

def p_of(T, V):
    return nR * T / V

def adiabat_T(T0, V0, V):
    return T0 * (V0 / V) ** (gamma - 1.0)

V_ab = np.linspace(Va, Vb, 120)
V_bc = np.linspace(Vb, Vc, 120)
V_cd = np.linspace(Vc, Vd, 120)
V_da = np.linspace(Vd, Va, 120)
p_ab = p_of(T_hot, V_ab)
p_bc = p_of(adiabat_T(T_hot, Vb, V_bc), V_bc)
p_cd = p_of(T_cold, V_cd)
p_da = p_of(adiabat_T(T_cold, Vd, V_da), V_da)
V_cycle = np.concatenate([V_ab, V_bc, V_cd, V_da])
p_cycle = np.concatenate([p_ab, p_bc, p_cd, p_da])

V_bg = np.linspace(0.7, Vc + 0.4, 200)
fig, ax = plt.subplots(figsize=(7.2, 5.6))
ax.plot(V_bg, p_of(T_hot, V_bg), color=hot_c, ls='--', lw=1.0, alpha=0.45,
        label=r'isotherm $T_h$')
ax.plot(V_bg, p_of(T_cold, V_bg), color=cold_c, ls='--', lw=1.0, alpha=0.45,
        label=r'isotherm $T_c$')
ax.fill(V_cycle, p_cycle, color=work_c, alpha=0.28, zorder=1)
ax.plot(V_ab, p_ab, color=hot_c, lw=2.7)
ax.plot(V_bc, p_bc, color=adiab_c, lw=2.7)
ax.plot(V_cd, p_cd, color=cold_c, lw=2.7)
ax.plot(V_da, p_da, color=adiab_c, lw=2.7)
ax.add_patch(FancyArrowPatch(
    (V_ab[50], p_ab[50]), (V_ab[70], p_ab[70]),
    arrowstyle='-|>', mutation_scale=14, lw=0, color=hot_c, zorder=4))
ax.add_patch(FancyArrowPatch(
    (V_bc[50], p_bc[50]), (V_bc[70], p_bc[70]),
    arrowstyle='-|>', mutation_scale=14, lw=0, color=adiab_c, zorder=4))
ax.add_patch(FancyArrowPatch(
    (V_cd[50], p_cd[50]), (V_cd[70], p_cd[70]),
    arrowstyle='-|>', mutation_scale=14, lw=0, color=cold_c, zorder=4))
ax.add_patch(FancyArrowPatch(
    (V_da[50], p_da[50]), (V_da[70], p_da[70]),
    arrowstyle='-|>', mutation_scale=14, lw=0, color=adiab_c, zorder=4))
ax.plot(Va, p_of(T_hot, Va), 'o', color=hot_c, ms=7)
ax.plot(Vb, p_of(T_hot, Vb), 'o', color=hot_c, ms=7)
ax.plot(Vc, p_of(T_cold, Vc), 'o', color=cold_c, ms=7)
ax.plot(Vd, p_of(T_cold, Vd), 'o', color=cold_c, ms=7)
ax.text(Va - 0.06, p_of(T_hot, Va) + 0.04, '1', ha='right', color=ink)
ax.text(Vb + 0.06, p_of(T_hot, Vb) + 0.04, '2', ha='left', color=ink)
ax.text(Vc + 0.06, p_of(T_cold, Vc) - 0.06, '3', ha='left', color=ink)
ax.text(Vd - 0.06, p_of(T_cold, Vd) - 0.06, '4', ha='right', color=ink)
ax.set_xlim(0.6, Vc + 0.4)
ax.set_ylim(0.0, p_of(T_hot, Va) * 1.18)
ax.set_xlabel(r'volume $V$')
ax.set_ylabel(r'pressure $p$')
ax.set_title(r'Same cycle on $p$–$V$: not a square')
ax.legend(loc='upper right', frameon=False)
mlai.write_figure('carnot-pv.svg', directory=diagrams)

# Two-panel: mill on (m, h) beside engine on (S, T)
mh, ml = Sc, Sh
hh, hc = Th, Tc
fig, axes = plt.subplots(1, 2, figsize=(11.4, 5.5))
panels = [
    dict(ax=axes[0],
         xlab=r'mass of water $m$', ylab=r'height $h$',
         xt=[mh, ml], xtl=[r'$m$', r'$m+\Delta m$'],
         yt=[hc, hh], ytl=[r'$h_c$', r'$h_h$'],
         top='fill bucket', bot='empty bucket',
         right='loaded bucket\ndescends',
         work=r'$W=g\Delta h\Delta m$',
         fall='height of the fall',
         title='Water mill'),
    dict(ax=axes[1],
         xlab=r'entropy $S$', ylab=r'temperature $T$',
         xt=[Sc, Sh], xtl=[r'$S_c$', r'$S_h$'],
         yt=[Tc, Th], ytl=[r'$T_c$', r'$T_h$'],
         top=r'take in entropy at $T_h$', bot=r'reject entropy at $T_c$',
         right='working body cools;\nno heat transfer',
         work=r'$W=\Delta T\times\Delta S$',
         fall="Carnot's fall of caloric",
         title='Heat engine'),
]
for pan in panels:
    ax = pan['ax']
    x0, x1 = pan['xt']
    y0, y1 = pan['yt']
    ax.set_xlim(0.05, 3.55)
    ax.set_ylim(0.15, 2.95)
    ax.set_aspect('equal')
    ax.set_xlabel(pan['xlab'])
    ax.set_ylabel(pan['ylab'])
    ax.set_xticks(pan['xt'])
    ax.set_xticklabels(pan['xtl'])
    ax.set_yticks(pan['yt'])
    ax.set_yticklabels(pan['ytl'])
    ax.axhline(y1, color=hot_c, ls='--', lw=1.0, alpha=0.45, zorder=0)
    ax.axhline(y0, color=cold_c, ls='--', lw=1.0, alpha=0.45, zorder=0)
    ax.add_patch(Rectangle(
        (x0, y0), x1 - x0, y1 - y0,
        facecolor=work_c, alpha=0.22, edgecolor='none', zorder=1))
    _draw_leg(ax, (x0, y1), (x1, y1), hot_c, arrow=True)
    _draw_leg(ax, (x1, y1), (x1, y0), adiab_c, arrow=True)
    _draw_leg(ax, (x1, y0), (x0, y0), cold_c, arrow=True)
    _draw_leg(ax, (x0, y0), (x0, y1), adiab_c, arrow=True)
    _dot(ax, (x0, y1), hot_c)
    ax.text(0.5 * (x0 + x1), y1 + 0.10, pan['top'], ha='center', va='bottom',
            color=hot_c, fontsize=9)
    ax.text(0.5 * (x0 + x1), y0 - 0.10, pan['bot'], ha='center', va='top',
            color=cold_c, fontsize=9)
    ax.text(x1 + 0.16, 0.5 * (y0 + y1), pan['right'], ha='left', va='center',
            color=adiab_c, fontsize=8, linespacing=1.2)
    ax.text(0.5 * (x0 + x1), 0.5 * (y0 + y1), pan['work'],
            ha='center', va='center', color=ink, fontsize=13)
    ax.annotate(
        '', xy=(0.42, y1), xytext=(0.42, y0),
        arrowprops=dict(arrowstyle='<->', color=ink, lw=1.2), zorder=4)
    ax.text(0.28, 0.5 * (y0 + y1), pan['fall'], ha='center', va='center',
            color=ink, fontsize=8, rotation=90)
    ax.set_title(pan['title'])
    for spine in ax.spines.values():
        spine.set_color('#444444')
fig.tight_layout()
mlai.write_figure('carnot-mill-square.svg', directory=diagrams)

# Fall versus adiabatic cool, on the T-S square already drawn
fig, ax = _axes("The fall is the reservoirs, not the downward stroke")
ax.set_xlim(0.05, 3.45)
ax.add_patch(Rectangle(
    (Sc, Tc), Sh - Sc, Th - Tc,
    facecolor=work_c, alpha=0.22, edgecolor='none', zorder=1))
_dot(ax, A, hot_c)
for lg in legs:
    _draw_leg(ax, lg['p0'], lg['p1'], lg['color'], arrow=True)
    _dot(ax, lg['p1'], lg['color'])
ax.annotate(
    '', xy=(Sc - 0.22, Th), xytext=(Sc - 0.22, Tc),
    arrowprops=dict(arrowstyle='<->', color=ink, lw=1.2), zorder=4)
ax.text(Sc - 0.34, 0.5 * (Th + Tc), "Carnot's fall of caloric",
        ha='right', va='center', color=ink, fontsize=11, rotation=90)
ax.text(Sh + 0.10, 0.5 * (Th + Tc),
        'working body cools\nby expansion;\nno heat transfer',
        ha='left', va='center', color=adiab_c, fontsize=10)
ax.text(0.5 * (Sc + Sh), 0.5 * (Tc + Th),
        r'$W=\Delta T\times\Delta S$', ha='center', va='center',
        color=ink, fontsize=15)
mlai.write_figure('carnot-ts-fall.svg', directory=diagrams)}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\displaycode{nu.display_plots('carnot-ts{sample:0>3}.svg',
                            directory='\writeDiagramsDir/physics',
                            sample=IntSlider(0, 0, 8, 1))}

\slides{\define{width}{70%}
\startanimation{carnot-ts}{0}{7}
\newframe{\includediagram{\diagramsDir/physics/carnot-ts000}{\width}}{carnot-ts}
\newframe{\includediagram{\diagramsDir/physics/carnot-ts001}{\width}}{carnot-ts}
\newframe{\includediagram{\diagramsDir/physics/carnot-ts002}{\width}}{carnot-ts}
\newframe{\includediagram{\diagramsDir/physics/carnot-ts003}{\width}}{carnot-ts}
\newframe{\includediagram{\diagramsDir/physics/carnot-ts004}{\width}}{carnot-ts}
\newframe{\includediagram{\diagramsDir/physics/carnot-ts005}{\width}}{carnot-ts}
\newframe{\includediagram{\diagramsDir/physics/carnot-ts006}{\width}}{carnot-ts}
\newframe{\includediagram{\diagramsDir/physics/carnot-ts007}{\width}}{carnot-ts}
\endanimation}

\notes{\figure{\includediagram{\diagramsDir/physics/carnot-ts007}{70%}}{The ideal Carnot cycle on a temperature-entropy ($T$-$S$) diagram is a square. Heat is taken in along the top ($T$ constant, $S$ increasing) and rejected along the bottom. The two vertical legs are adiabatic: the working body changes temperature without exchanging entropy. The work extracted is the area, $\Delta T\times\Delta S$.}{carnot-ts-square}}

\notes{You start at some temperature. In the Carnot cycle the temperature stays constant while the entropy increases: that is the expansion of the system, the increasing volume is the opening of the piston.[^volume] Then the system cools --- an isolated expansion, entropy holding. Once it has cooled, the entropy comes slowly back down, temperature staying the same: the contraction, heat rejected to the cold bath. That cold rejection is what Watt's condenser is doing: it is the bottom of the mill, not the cooling stroke itself. Then you compress in isolation, the steam heats, and you have a square. This is the ideal engine. It is not how Carnot described it, but it is what he was describing.}

\notes{[^volume]: Focussing on volume increase, normally we would expect increasing volume to cause cooling, but in a heat engine if we increase the volume slowly enough, heat can flow from a heat bath to the cylinder and it stays at constant temperature. The energy is flowing in from the heat bath.}

\notes{On the visualiser I drew the two temperature changes as rapid, almost instantaneous. In the ideal cycle they need not be. They are adiabatic: thermally isolated, reversible expansions and compressions. No heat crosses the boundary, so entropy of the working body holds, and the temperature changes because the volume does. The entropy changes, by contrast, have to happen in contact with a bath. Do them too fast and you are no longer isothermal: compression would heat the system and expansion would cool it, and you have left the square.}

\notes{$\Delta T$ is the difference between the two temperatures and $\Delta S$ the difference between the two entropies. The energy extracted on the cycle is $\Delta T\times\Delta S$.}

\slidesincremental{
* Expansion at $T_h$: entropy increases, volume increases
* Isolated cool: adiabatic expansion, entropy holds
* Contraction at $T_c$: entropy comes back down (Watt's condenser)
* Isolated heat: adiabatic compression, the square closes
* Work is the area: $W=\Delta T\times\Delta S$
}

\newslide{The Fall Is Not the Downward Stroke}

\slides{Carnot's fall is the difference between the reservoirs. The downward adiabat is the working body cooling with no heat transfer.}

\figure{\includediagram{\diagramsDir/physics/carnot-ts-fall}{70%}}{Two annotations that are easy to conflate. The vertical brace is Carnot's fall of caloric: entropy is taken in at $T_h$ and given up at $T_c$. The right-hand leg is not that fall. It is an isolated expansion of the working body; no heat crosses, entropy holds, temperature drops.}{carnot-ts-fall}

\notes{It is easy to look at the square and take the downward stroke for the fall. That leg is where the working substance cools by expansion, with no heat transfer. Carnot's fall is the difference between the temperatures at which entropy enters and leaves, across the whole cycle. The mill turns because caloric moves from $A$ to $B$, not because the piston is dropping.}

\notes{He gives a concrete steam-engine example. A boiler at about $160^\circ\mathrm{C}$, a condenser at about $40^\circ\mathrm{C}$: a fall of caloric of $120^\circ$. Combustion could furnish a much larger fall, a thousand degrees or more, and ordinary engines used only a modest part of it. That was his engineering point: look after the height. The modern reading, which he did not write, puts those on an absolute scale, $T_h = 433\,\mathrm{K}$, $T_c = 313\,\mathrm{K}$, and the ceiling is $1-T_c/T_h$, a little under twenty-eight percent. The analogy suggested quantity of caloric times temperature fall. The $T$--$S$ square tells us how that product arises, once the transferred quantity is entropy and temperature is thermodynamic temperature.}

\speakernotes{One click. Brace versus right-hand leg. Then the $160$/$40$ numbers if there is time: his example, our retrospective efficiency.}

\newslide{Four-Stroke, and the Smaller Loop}

\slides{The four-stroke is the implementation. The square is the theory. Same $\Delta T$, same $\Delta S$: you cut two corners.}

\figure{\includediagram{\diagramsDir/physics/carnot-ts008}{70%}}{A real engine between the same reservoirs, with the same entropy swing, does not shrink the square. It still visits the top-right and the bottom-left. Heat is not taken in along the whole top, nor rejected along the whole bottom, so those two corners are cut off. The remaining area over the square is the efficiency.}{carnot-ts-efficiency}

\notes{In a motor-car engine the same loop is a four-stroke: ignition, piston down, exhaust, compression. This is known as the Otto cycle. But this is the mechanism behind the theory, or one possible mechanism. What the theory says is that the maximum energy you can get out is the area of the square.}

\notes{The inner loop is easy to draw wrongly. You do not scale the square down. The fall is still $T_h$ to $T_c$, and the entropy change of the working body is still $S_c$ to $S_h$: those are known. So the top-right corner stays, and the bottom-left stays. What you lose is the other two. Heat does not go in isothermally along the whole top, nor come out along the whole bottom, and the area that remains, over the square, is the efficiency of the engine.}

\notes{As an undergraduate mechanical engineer one learns these diagrams without anyone saying that the energy is stored in probability, or that this is the form of what entropy is. When you realise that the engine is at the heart of the industrial revolution and that it's really converting entropy into work, then there is an argument that at its heart even the Industrial Revolution is an information revolution. That is, of course, if you accept the interpretation of entropy as information.}

\speakernotes{Four-stroke is a courtesy to anyone who did engineering. Do not overfit the mapping. Do not shrink the square: that would be a different fall. Point at top-right and bottom-left. Same $\Delta T$, same $\Delta S$; two corners cut. Land on: the square is the ceiling; the remaining area is what you actually get.}

\newslide{The $p$-$V$ Chart}

\slides{Engineers often draw the same strokes on a pressure-volume chart. In that case it no longer looks like a square.}

\figure{\includediagram{\diagramsDir/physics/carnot-pv}{70%}}{The same Carnot cycle on a $p$-$V$ diagram. The hot and cold legs follow isotherms $pV=\mathrm{const}$; the isolated cool and isolated heat follow adiabats, which are steeper. The enclosed area is still the work, $\oint p\,\mathrm{d}V$, but you cannot read $\Delta T\times\Delta S$ off it by eye.}{carnot-pv}

\notes{The other way these things are drawn is as pressure-volume diagrams. You can draw the same stages as the $T$-$S$ diagram, but they no longer look like straight lines. That's because isothermal on this chart is a constraint on $pV$ due to the relationship between pressure and volume ($pV = nRT$ for an ideal gas). This makes it not so easy to read off what energy has been extracted because it's the area inside the shape still, but the area is no longer a square.}

\notes{But as a reminder, we are imposing a modern perspective on how Carnot thought about it. Recall his thinking was that it was more like a mill: a waterfall from which we are extracting energy. He did not talk about entropy. He was interested in change in temperature as being equivalent to height change. The $p$--$V$ chart is Clapeyron's language; the square is ours. The mill is his.}

\speakernotes{One slide, in passing. Point at the isotherms. Then: this is why we drew $T$--$S$. Back to Clausius if this was the Helmholtz question.}

\addreading{@Carnot-reflexions24}{The waterfall: quantity of liquid, height of the fall; he does not yet know if the work is proportional (Thurston pp.~60--61)}
\addreading{@Falk-caloric85}{Entropy as a resurrection of caloric}
\addreading{@Meyn-carnot24}{The mill drawn as a rectangle; caloric in the reversible model read as entropy}

\endif
