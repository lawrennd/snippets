\ifndef{discreteJacobianRadonNikodym}
\define{discreteJacobianRadonNikodym}

\editme

\include{_physics/includes/ideal-gas-velocity-sample.md}

\subsection{Bin Widths Are a Radon-Nikodym Derivative}

\slides{The ratio of widths is the discrete Jacobian. It converts one $h$ into the other.}

\slidesincremental{
* Same cells: $H$ is shared; $h\approx H+\sum_i p_i\log\Delta_i$
* $\Delta s_i/\Delta u_i \to |{\mathrm{d}s}/{\mathrm{d}u}|=1/(3s^2)$
* Continuum name: Radon-Nikodym derivative between the two measures
}

\speakernotes{Board $h\approx H+\sum p_i\log\Delta_i$ for unequal bins. The difference of the two remainders is $\sum p_i\log(\Delta s_i/\Delta u_i)$, which tracks $\mathbb{E}\log|J|$. Do not do $\dataStd$-algebras. The width ratio *is* the discrete RN derivative.}

\notes{For a partition that is not equal-width, the bin-width correction is no longer a single $\log\Delta$. Probability conservation in cell $i$ still reads $p_i \approx f\,\Delta_i$, so
\begin{align}
H
  = -\sum_i p_i\log p_i
  \approx h - \sum_i p_i\log\Delta_i,
\qquad
h \approx H + \sum_i p_i\log\Delta_i.
\end{align}
Take the equal-volume cells of the previous snippets, written once in $u=s^3$ and once in $s$. The masses $\{p_i\}$  (hence $H$) are the same. The two differential entropies differ by the average log-ratio of widths,
\begin{align}
h(s)-h(u)
  \approx \sum_i p_i\log\frac{\Delta s_i}{\Delta u_i}
  \to \mathbb{E}\bigl[\log\bigl|{\mathrm{d}s}/{\mathrm{d}u}\bigr|\bigr].
\end{align}
That ratio $\Delta s_i/\Delta u_i$ is called the discrete Radon-Nikodym derivative of Lebesgue-on-speed with respect to Lebesgue-on-volume. In the continuum limit it becomes the Jacobian $1/(3s^2)$. Probability conservation $f_s(s)\,{\mathrm{d}}s = f_u(u)\,{\mathrm{d}}u$ is the same statement.

The Maxwell speed density relative to three-dimensional Lebesgue is the shell factor $4\pi s^2$. Equivalently, the pushforward of Lebesgue measure on $\mathbb{R}^3$ has density $4\pi s^2$ in $s$:
\begin{align}
f_s(s)\,{\mathrm{d}}s = f(\mathbf{v})\,{\mathrm{d}}^3v,
\qquad
\frac{{\mathrm{d}}^3v}{{\mathrm{d}}s} = 4\pi s^2.
\end{align}
The Gaussian $h(v_x)$ and the Maxwell $h(s)$ disagree because they are different coordinates *and* because each $h$ is taken against a different *undeclared* Lebesgue measure.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{s_max = speed_range_max(speed)
edges_s = equal_volume_speed_edges(s_max, n_histogram_bins)
edges_u = edges_s**3
delta_s = np.diff(edges_s)
delta_u = np.diff(edges_u)
counts, _ = np.histogram(speed, bins=edges_s)
p = counts / float(counts.sum())
H = discrete_entropy(counts)
occupied = counts > 0
s_mid = 0.5 * (edges_s[:-1] + edges_s[1:])
rn_discrete = np.divide(delta_s, delta_u, out=np.zeros_like(delta_s),
                        where=delta_u > 0)
mean_log_j = np.sum(p[occupied] * np.log(rn_discrete[occupied]))
h_s_est = H + np.sum(p[occupied] * np.log(delta_s[occupied]))
h_u_est = H + np.sum(p[occupied] * np.log(delta_u[occupied]))
h_s = maxwell_speed_differential_entropy(velocity_sigma)
ss = np.linspace(max(s_mid[occupied].min(), 1e-3), s_max, 400)

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(s_mid[occupied], rn_discrete[occupied], 'o', color='#4C72B0',
        ms=6, label='$\\Delta s_i/\\Delta u_i$')
ax.plot(ss, 1.0 / (3.0 * ss**2), color='#C44E52', lw=2,
        label='$1/(3s^2)$')
ax.set_xlabel('$s$')
ax.set_ylabel('width ratio')
ax.legend(fontsize=10)
ax.text(0.98, 0.95,
        f'$\\sum p_i\\log(\\Delta s_i/\\Delta u_i)={mean_log_j:.3f}$\n'
        f'$H+\\sum p_i\\log\\Delta s_i={h_s_est:.3f}$\n'
        f'$H+\\sum p_i\\log\\Delta u_i={h_u_est:.3f}$\n'
        f'$h(s)={h_s:.3f}$',
        transform=ax.transAxes, va='top', ha='right', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
mlai.write_figure('discrete-jacobian-radon-nikodym.svg',
                  directory='\writeDiagramsDir/information')}

\figure{\includediagram{\diagramsDir/information/discrete-jacobian-radon-nikodym}{80%}}{Width ratio of the pushed equal-volume cells, against the Jacobian $1/(3s^2)$. The average log-ratio converts $h(u)$ into $h(s)$. That ratio is the discrete Radon-Nikodym derivative.}{discrete-jacobian-radon-nikodym}

\endif
