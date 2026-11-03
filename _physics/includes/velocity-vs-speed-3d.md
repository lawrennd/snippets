\ifndef{velocityVsSpeed3d}
\define{velocityVsSpeed3d}

\editme

\include{_physics/includes/ideal-gas-velocity-sample.md}

\subsection{Three Dimensions: Component Versus Speed}

\slides{Same 3D sample: one Cartesian component peaks at zero; speed peaks away from zero.}

\slidesincremental{
* Left: $v_x\sim\mathcal{N}(0,\dataStd^2)$ --- peak at $0$
* Right: $s=|\mathbf{v}|$ --- Maxwell; factor $s^2$ from shell volume
* The nonzero mode is geometry, not folding
}

\speakernotes{Side by side with the 1D pair still in mind. Left mode at zero; right mode at $\sigma\sqrt{2}$. Point at the $s^2$: that is the spherical shell in velocity space. Absolute value alone did not move the peak; the Jacobian does.}

\notes{Keep the same isotropic three-dimensional sample. One Cartesian marginal is still Gaussian and peaks at the origin. Speed $s=|\mathbf{v}|$ has density
\begin{align}
f(s)
  = \sqrt{\frac{2}{\pi}}\,\frac{s^2}{\dataStd^3}\,e^{-s^2/2\dataStd^2},
  \qquad s\ge 0.
\end{align}
The factor $s^2$ is the surface area of a sphere of radius $s$ in velocity space. Maximising $f(s)$ gives the most probable speed
\begin{align}
s_{\mathrm{mp}} = \dataStd\sqrt{2}.
\end{align}
Unlike the one-dimensional modulus, the mode is not at zero. The peak moves because of the change of variables in three dimensions, not because speed is nonnegative.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{vx_lim = 4.0
edges_v = np.linspace(-vx_lim, vx_lim, n_histogram_bins + 1)
xs = np.linspace(-vx_lim, vx_lim, 400)
fig, ax = plt.subplots(figsize=plot.one_figsize)
ax.hist(velocity_x, bins=edges_v, density=True, color='#4C72B0', alpha=0.6,
        label='equal-$\\Delta v$ histogram')
ax.plot(xs, np.exp(-0.5 * xs**2 / velocity_sigma**2)
        / np.sqrt(2.0 * np.pi * velocity_sigma**2),
        color='#C44E52', lw=2, label='$\\mathcal{N}(0,\\sigma^2)$')
ax.axvline(0.0, color='0.35', lw=1, ls='--')
ax.set_xlim(-vx_lim, vx_lim)
ax.set_xlabel('$v_x$')
ax.set_ylabel('density')
ax.set_title('3D component')
ax.legend(loc='upper right', fontsize=8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
mlai.write_figure('velocity-vs-speed-3d-velocity.svg',
                  directory='\writeDiagramsDir/physics')}

\plotcode{s_max = speed_range_max(speed)
edges_s = equal_delta_speed_edges(s_max, n_histogram_bins)
ss = np.linspace(1e-3, s_max, 400)
s_mp = velocity_sigma * np.sqrt(2.0)
fig, ax = plt.subplots(figsize=plot.one_figsize)
ax.hist(speed, bins=edges_s, density=True, color='#4C72B0', alpha=0.6,
        label='equal-$\\Delta s$ histogram')
ax.plot(ss, maxwell_speed_pdf(ss, velocity_sigma),
        color='#C44E52', lw=2, label='Maxwell speed law')
ax.axvline(s_mp, color='0.35', lw=1, ls='--',
           label='$s_{\\mathrm{mp}}=\\sigma\\sqrt{2}$')
ax.set_xlim(0.0, s_max)
ax.set_xlabel('$s=|\\mathbf{v}|$')
ax.set_ylabel('density')
ax.set_title('3D speed')
ax.legend(loc='upper right', fontsize=8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
mlai.write_figure('velocity-vs-speed-3d-speed.svg',
                  directory='\writeDiagramsDir/physics')}

\figure{\columns{\includediagram{\diagramsDir/physics/velocity-vs-speed-3d-velocity}{100%}}{\includediagram{\diagramsDir/physics/velocity-vs-speed-3d-speed}{100%}}{50%}{50%}}{Three dimensions. Left: one Cartesian component still peaks at zero. Right: speed peaks at $\sigma\sqrt{2}$ because of the $s^2$ shell volume --- not because of taking a modulus.}{velocity-vs-speed-3d}

\endif
