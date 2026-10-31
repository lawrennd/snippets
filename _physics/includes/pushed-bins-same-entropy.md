\ifndef{pushedBinsSameEntropy}
\define{pushedBinsSameEntropy}

\editme

\include{_physics/includes/ideal-gas-velocity-sample.md}

\subsection{Pushed Bins Keep the Same Entropy}

\slides{The same cells, written on the speed axis: masses unchanged, widths change.}

\slidesincremental{
* Equal-volume shells in 3D velocity: equal width in $u=s^3$
* Push the edges to $s=u^{1/3}$; $\Delta s_i$ now grows then shrinks
* $H$ is a functional of the masses --- it does not see the widths
}

\speakernotes{Left panel: probability bars, equal visual width, height $p_i$. Right: density $p_i/\Delta s_i$ with the true speed widths. Same $H$ on both. This is a 1--1 relabelling of a partition of speed (volume coordinate $\leftrightarrow$ speed). Folding $v\mapsto|v|$, or grouping Cartesian cubes into shells, merges cells and *drops* $H$. That is not this figure.}

\notes{Discrete Shannon entropy depends only on the probability masses of a partition. Keep the cells and relabel the axis: the masses $\{p_i\}$ are unchanged, so $H$ is unchanged, while a density histogram $p_i/\Delta_i$ changes because the widths change.

The Maxwell speed map $s=|\mathbf{v}|$ is not itself 1--1 --- equal Cartesian cubes that sit on one spherical shell are a *grouping*, and grouping drops entropy. The figure avoids that. Partition speed by *equal Cartesian volume*, i.e.\ equal-width bins in $u=s^3$. The map $u\mapsto s=u^{1/3}$ is strictly increasing on $s\ge 0$. Pushing the bin edges stretches them by
\begin{align}
\Delta s_i \approx \frac{1}{3s_i^2}\,\Delta u.
\end{align}
Drawn as probability bars the occupancy is invariant. Drawn as a density against $s$ the bars change shape. The two pictures share one $H$.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{s_max = speed_range_max(speed)
edges_s = equal_volume_speed_edges(s_max, n_histogram_bins)
delta_s = np.diff(edges_s)
counts, _ = np.histogram(speed, bins=edges_s)
p = counts / float(counts.sum())
H = discrete_entropy(counts)
idx = np.arange(n_histogram_bins)
fig, ax = plt.subplots(figsize=plot.one_figsize)
ax.bar(idx, p, color='#4C72B0', width=0.9)
ax.set_xlabel('cell index')
ax.set_ylabel('$p_i$')
ax.text(0.02, 0.95, f'$H={H:.3f}$', transform=ax.transAxes,
        va='top', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
mlai.write_figure('pushed-bins-same-entropy-masses.svg',
                  directory='\writeDiagramsDir/physics')}

\plotcode{fig, ax = plt.subplots(figsize=plot.one_figsize)
ax.bar(edges_s[:-1], np.divide(p, delta_s, out=np.zeros_like(p),
                               where=delta_s > 0),
       width=delta_s, align='edge', color='#DD8452', alpha=0.85)
ss = np.linspace(1e-3, s_max, 400)
ax.plot(ss, maxwell_speed_pdf(ss, velocity_sigma),
        color='#C44E52', lw=2)
ax.set_xlabel('$s=|\\mathbf{v}|$')
ax.set_ylabel('density $p_i/\\Delta s_i$')
ax.text(0.02, 0.95, f'$H={H:.3f}$', transform=ax.transAxes,
        va='top', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
mlai.write_figure('pushed-bins-same-entropy-density.svg',
                  directory='\writeDiagramsDir/physics')}

\figure{\columns{\includediagram{\diagramsDir/physics/pushed-bins-same-entropy-masses}{100%}}{\includediagram{\diagramsDir/physics/pushed-bins-same-entropy-density}{100%}}{50%}{50%}}{Equal-volume shells in 3D velocity, written two ways. Left: probability masses. Right: the same masses as a density on the speed axis. The bins change shape; $H$ does not.}{pushed-bins-same-entropy}

\endif
