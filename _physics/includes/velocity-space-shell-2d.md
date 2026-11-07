\ifndef{velocitySpaceShell2d}
\define{velocitySpaceShell2d}

\editme

\include{_physics/includes/ideal-gas-velocity-sample.md}

\subsection{Velocity Space: Grid and Speed Rings}

\slides{Same sample in the $(v_x,v_y)$ plane. Equal-$\Delta v$ bins are a grid; equal-$\Delta s$ bins are concentric rings.}

\slidesincremental{
* Left: isotropic cloud in two Cartesian components
* Equal-$\Delta v$ grid: each square has the same area
* Concentric rings: shell circumference grows as $s$ --- more cells at larger speed
}

\speakernotes{If a student asks why speed peaks away from zero, this figure is the answer before the 3D histograms. A ring at larger $s$ holds more grid cells, so even an isotropic Gaussian piles probability away from the origin once you bin by speed. Two dimensions is enough for the geometry; three dimensions replaces rings by spherical shells ($s^2$).}
\notes{Harry's question --- why does the speed histogram peak away from zero when each Cartesian component peaks at zero? --- is answered by a change of variables in velocity space, not by folding alone. Draw the plane of two components $(v_x,v_y)$. An isotropic Gaussian is a circular cloud centred at the origin. Partition that plane with an equal-$\Delta v$ grid: every square has the same area. Now draw concentric circles of radius $s=|\mathbf{v}|$. The ring between $s$ and $s+\Delta s$ contains more and more grid cells as $s$ grows, because its circumference is $2\pi s$. Counting samples by which ring they fall in therefore weights larger speeds more heavily than the Cartesian grid does. That circumferential factor is the two-dimensional shell volume. In three dimensions the same geometry becomes a spherical shell of area $4\pi s^2$, which is the $s^2$ in the Maxwell speed law. Absolute value alone (the one-dimensional fold) never moves the mode; the shell volume does.}

\setupplotcode{import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import mlai.plot as plot
import mlai}

\plotcode{vx = velocities[:2500, 0]
vy = velocities[:2500, 1]
lim = 3.5
delta = 0.5
fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.scatter(vx, vy, s=4, c='#4C72B0', alpha=0.25, linewidths=0, zorder=1)
grid = np.arange(-lim, lim + 1e-9, delta)
for g in grid:
    ax.axvline(g, color='0.75', lw=0.6, zorder=0)
    ax.axhline(g, color='0.75', lw=0.6, zorder=0)
for s in (0.5, 1.0, 1.5, 2.0, 2.5, 3.0):
    ax.add_patch(mpatches.Circle((0.0, 0.0), s, fill=False,
                                 color='#C44E52', lw=1.4, zorder=2))
ax.add_patch(mpatches.Wedge((0.0, 0.0), 2.0, 0, 360, width=0.5,
                            facecolor='#C44E52', alpha=0.12, zorder=1))
ax.annotate('', xy=(2.0, 0.0), xytext=(0.0, 0.0),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=1.2))
ax.text(1.05, 0.18, r'$s$', color='#333333', fontsize=12)
ax.text(2.15, 0.55, r'$\propto s$', color='#C44E52', fontsize=11)
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_aspect('equal')
ax.set_xlabel(r'$v_x$')
ax.set_ylabel(r'$v_y$')
ax.set_title('2D velocity space: grid vs speed rings')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
mlai.write_figure('velocity-space-shell-2d.svg',
                  directory='\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/velocity-space-shell-2d}{70%}}{Two Cartesian velocity components. The pale grid is equal-$\Delta v$ area. The red circles are equal-$\Delta s$ shells: circumference grows with $s$, so a speed histogram weights larger speeds more heavily. Three dimensions replaces rings by spherical shells of area $4\pi s^2$.}{velocity-space-shell-2d}

\endif
