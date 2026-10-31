\ifndef{maxwellSpeedHistogramEntropy}
\define{maxwellSpeedHistogramEntropy}

\editme

\include{_physics/includes/ideal-gas-velocity-sample.md}

\subsection{Entropy of the Maxwell Speed Law}

\slides{The speed $s=|\mathbf{v}|$ is a different random variable, with a different $h$.}

\slidesincremental{
* $f(s)=4\pi s^2(2\pi\dataStd^2)^{-3/2}e^{-s^2/2\dataStd^2}$
* $h(s)=\log(\dataStd\sqrt{2\pi})+\gamma-\tfrac12$, not $\tfrac12\log(2\pi e\dataStd^2)$
* Why is this number not the Gaussian's $h$?
}

\speakernotes{Overlay the Maxwell curve on an equal-$\Delta s$ histogram of the same 3D sample. Read both numbers. The Gaussian $h$ was for $v_x$; this $h$ is for $s$. Different variable *and* different Lebesgue measure. Leave the Jacobian for the next snippet.}

\notes{The same isotropic Gaussian sample has speed $s=|\mathbf{v}|$ with density
\begin{align}
f(s)
  = 4\pi s^2 \bigl(2\pi\dataStd^2\bigr)^{-3/2}
    e^{-s^2/2\dataStd^2}
  = \sqrt{\frac{2}{\pi}}\,\frac{s^2}{\dataStd^3}\,e^{-s^2/2\dataStd^2},
  \qquad s\ge 0.
\end{align}
That is the Maxwell speed law. Its differential entropy is
\begin{align}
h(s)=\log\bigl(\dataStd\sqrt{2\pi}\bigr)+\gamma-\tfrac12,
\end{align}
where $\gamma$ is Euler's constant. A single Cartesian component has $h(v_x)=\tfrac12\log(2\pi e\dataStd^2)$. For $\dataStd=1$ these are approximately $0.996$ and $1.419$ nats. They disagree because they are entropies of different random variables, each written against Lebesgue measure in its own coordinate. An equal-$\Delta s$ histogram of the sampled speeds tracks $h(s)-\log\Delta s$, just as the Gaussian histogram tracked $h(v_x)-\log\Delta v$.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{s_max = speed_range_max(speed)
edges = equal_delta_speed_edges(s_max, n_histogram_bins)
delta = edges[1] - edges[0]
counts, _ = np.histogram(speed, bins=edges)
H = discrete_entropy(counts)
h = maxwell_speed_differential_entropy(velocity_sigma)
h_vx = gaussian_differential_entropy(velocity_sigma)
ss = np.linspace(1e-3, s_max, 400)

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.hist(speed, bins=edges, density=True, color='#4C72B0', alpha=0.6,
        label='equal-$\\Delta s$ histogram')
ax.plot(ss, maxwell_speed_pdf(ss, velocity_sigma),
        color='#C44E52', lw=2, label='Maxwell speed law')
ax.set_xlim(0.0, s_max)
ax.set_xlabel('$s=|\\mathbf{v}|$')
ax.set_ylabel('density')
ax.text(0.98, 0.95,
        f'$H={H:.3f}$\n$h-\\log\\Delta={h - np.log(delta):.3f}$\n'
        f'$h(s)={h:.3f}$\n$h(v_x)={h_vx:.3f}$',
        transform=ax.transAxes, va='top', ha='right', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
ax.legend(loc='upper left', fontsize=9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
mlai.write_figure('maxwell-speed-histogram-entropy.svg',
                  directory='\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/maxwell-speed-histogram-entropy}{80%}}{Equal-width histogram of speed from the same 3D Gaussian sample. Discrete $H$ tracks $h(s)-\log\Delta$. The Maxwell $h(s)$ is not the Gaussian $h(v_x)$.}{maxwell-speed-histogram-entropy}

\endif
