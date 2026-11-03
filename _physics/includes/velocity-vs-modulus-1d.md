\ifndef{velocityVsModulus1d}
\define{velocityVsModulus1d}

\editme

\include{_physics/includes/ideal-gas-velocity-sample.md}

\subsection{One Dimension: Velocity Versus Modulus}

\slides{Same one-dimensional sample: $v$ peaks at zero; folding to $|v|$ keeps the mode at zero.}

\slidesincremental{
* Left: $v\sim\mathcal{N}(0,\dataStd^2)$ --- peak at $0$
* Right: $s=|v|$ --- half-normal; support $[0,\infty)$, mode still at $0$
* Folding alone does not push the peak away from zero
}

\speakernotes{Side by side. Point at both modes: both sit at zero. The student's ``why isn't the peak at zero?'' question is about speed in three dimensions, not about taking a modulus. Board $f(s)=\sqrt{2/(\pi\sigma^2)}\,e^{-s^2/2\sigma^2}$ briefly if needed.}

\notes{Take one Cartesian component $v$ of the isotropic sample (or any one-dimensional Gaussian). Its density peaks at the origin. The modulus $s=|v|$ folds the two tails onto $[0,\infty)$. Probability conservation gives the half-normal
\begin{align}
f(s)
  = \sqrt{\frac{2}{\pi\dataStd^2}}\,
    e^{-s^2/2\dataStd^2},
  \qquad s\ge 0.
\end{align}
That density is strictly decreasing: the mode is still at $s=0$. A nonzero most-probable speed needs the shell volume of two or three dimensions, not the absolute-value map alone.}

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
ax.set_xlabel('$v$')
ax.set_ylabel('density')
ax.set_title('1D velocity')
ax.legend(loc='upper right', fontsize=8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
mlai.write_figure('velocity-vs-modulus-1d-velocity.svg',
                  directory='\writeDiagramsDir/physics')}

\plotcode{s_max = speed_range_max(speed_1d)
edges_s = equal_delta_speed_edges(s_max, n_histogram_bins)
ss = np.linspace(0.0, s_max, 400)
fig, ax = plt.subplots(figsize=plot.one_figsize)
ax.hist(speed_1d, bins=edges_s, density=True, color='#4C72B0', alpha=0.6,
        label='equal-$\\Delta s$ histogram')
ax.plot(ss, half_normal_pdf(ss, velocity_sigma),
        color='#C44E52', lw=2, label='half-normal $|v|$')
ax.axvline(0.0, color='0.35', lw=1, ls='--')
ax.set_xlim(0.0, s_max)
ax.set_xlabel('$s=|v|$')
ax.set_ylabel('density')
ax.set_title('1D modulus')
ax.legend(loc='upper right', fontsize=8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
mlai.write_figure('velocity-vs-modulus-1d-speed.svg',
                  directory='\writeDiagramsDir/physics')}

\figure{\columns{\includediagram{\diagramsDir/physics/velocity-vs-modulus-1d-velocity}{100%}}{\includediagram{\diagramsDir/physics/velocity-vs-modulus-1d-speed}{100%}}{50%}{50%}}{One dimension. Left: a Gaussian velocity component peaks at zero. Right: the same sample folded to $|v|$ is half-normal --- the mode is still at zero.}{velocity-vs-modulus-1d}

\endif
