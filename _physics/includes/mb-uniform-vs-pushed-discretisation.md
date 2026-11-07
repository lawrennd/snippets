\ifndef{mbUniformVsPushedDiscretisation}
\define{mbUniformVsPushedDiscretisation}

\editme

\include{_physics/includes/ideal-gas-velocity-sample.md}

\subsection{Two Discretisations of the Same Speeds}

\slides{Equal $\Delta s$ is a different partition from the pushed equal-volume cells. Discrete $H$ changes.}

\slidesincremental{
* Same speed law $f(s)$, two partitions
* Pushed: equal 3D volume ($u=s^3$); uniform: equal $\Delta s$
* The discretisation *is* the measure
}

\speakernotes{Side by side: same $f$, same $s_{\max}$, same number of bins. Only the edge placement changes. Midpoint Riemann rectangles; two values of $H$. Uniform-in-$s$ is Lebesgue on the speed axis; equal-volume is Lebesgue in 3D, written in $s$.}

\notes{The previous figure kept one partition and only relabelled the axis, so $H$ could not change. Now we *rebin*. Take the same Maxwell density and the same number of cells, and compare two partitions: (i) the pushed equal-volume partition (equal width in $u=s^3$); (ii) a uniform partition of $[0,s_{\max}]$ (equal $\Delta s$). These are different collections of midpoint masses $\{p_i\}$, so they have different discrete entropies. Uniform bins in $s$ are Lebesgue measure on the speed axis. Equal-volume bins are Lebesgue measure on $\mathbb{R}^3$, expressed in the speed coordinate. Choosing a discretisation is choosing a measure.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{s_max = speed_range_max(speed)
edges_push = equal_volume_speed_edges(s_max, n_histogram_bins)
edges_unif = equal_delta_speed_edges(s_max, n_histogram_bins)
widths_push = np.diff(edges_push)
widths_unif = np.diff(edges_unif)
f_push = maxwell_speed_pdf(bin_midpoints(edges_push), velocity_sigma)
f_unif = maxwell_speed_pdf(bin_midpoints(edges_unif), velocity_sigma)
p_push = riemann_masses(f_push, widths_push)
p_unif = riemann_masses(f_unif, widths_unif)
H_push = discrete_entropy_from_masses(p_push)
H_unif = discrete_entropy_from_masses(p_unif)
ss = np.linspace(1e-3, s_max, 400)
pdf = maxwell_speed_pdf(ss, velocity_sigma)
fig, ax = plt.subplots(figsize=plot.one_figsize)
ax.bar(edges_push[:-1], f_push, width=widths_push, align='edge',
       color='#DD8452', alpha=0.85)
ax.plot(ss, pdf, color='#C44E52', lw=2)
ax.set_xlim(0.0, s_max)
ax.set_xlabel('$s=|\\mathbf{v}|$')
ax.set_ylabel('density')
ax.text(0.98, 0.95, f'$H={H_push:.3f}$',
        transform=ax.transAxes, va='top', ha='right', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
mlai.write_figure('mb-uniform-vs-pushed-discretisation-pushed.svg',
                  directory='\writeDiagramsDir/physics')}

\plotcode{fig, ax = plt.subplots(figsize=plot.one_figsize)
ax.bar(edges_unif[:-1], f_unif, width=widths_unif, align='edge',
       color='#4C72B0', alpha=0.7)
ax.plot(ss, pdf, color='#C44E52', lw=2)
ax.set_xlim(0.0, s_max)
ax.set_xlabel('$s=|\\mathbf{v}|$')
ax.set_ylabel('density')
ax.text(0.98, 0.95, f'$H={H_unif:.3f}$',
        transform=ax.transAxes, va='top', ha='right', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
mlai.write_figure('mb-uniform-vs-pushed-discretisation-uniform.svg',
                  directory='\writeDiagramsDir/physics')}

\figure{\columns{\includediagram{\diagramsDir/physics/mb-uniform-vs-pushed-discretisation-pushed}{100%}}{\includediagram{\diagramsDir/physics/mb-uniform-vs-pushed-discretisation-uniform}{100%}}{50%}{50%}}{The same Maxwell density, two midpoint Riemann partitions, two values of discrete $H$. Left: equal 3D volume, pushed to the speed axis. Right: equal $\Delta s$. The discretisation is the measure.}{mb-uniform-vs-pushed-discretisation}

\endif
