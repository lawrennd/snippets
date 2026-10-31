\ifndef{logDeltaDivergence}
\define{logDeltaDivergence}

\editme

\include{_physics/includes/ideal-gas-velocity-sample.md}

\subsection{The Continuous Limit Drops $\log\Delta$}

\slides{As the bins shrink, discrete $H$ tracks $-\log\Delta$ to infinity. Differential $h$ is what remains.}

\slidesincremental{
* $H(X^\Delta)\approx h-\log\Delta$
* $-\log\Delta\to+\infty$ as $\Delta\to 0$
* Passing to a density throws that term away
}

\speakernotes{The scatter should sit on the line $h-\log\Delta$. The horizontal line at $h$ is the finite remainder. The move to a continuous entropy is exactly ignoring a term that is driving to $+\infty$.}

\notes{Refine the equal-width partition of a Gaussian component. For each bin width $\Delta$,
\begin{align}
H(X^\Delta)
  = -\sum_i p_i\log p_i
  \approx h - \log\Delta.
\end{align}
Plotting $H$ against $-\log\Delta$ gives a line of slope one, offset by the constant $h=\tfrac12\log(2\pi e\dataStd^2)$. The discrete entropy diverges as the bins shrink because each mass $p_i\approx f\Delta$ contributes an extra $-\log\Delta$. Differential entropy is defined to be the $\Delta$-independent remainder. The continuous functional therefore *ignores a term that is driving to $+\infty$*. That is why $h$ can be negative, and why it is not a code-length bound.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{vx_lim = 4.0
n_list = np.array([5, 8, 10, 16, 20, 25, 32, 40, 50, 64, 80, 100])
Hs = []
deltas = []
for n_bins in n_list:
    edges = np.linspace(-vx_lim, vx_lim, n_bins + 1)
    delta = edges[1] - edges[0]
    counts, _ = np.histogram(velocity_x, bins=edges)
    Hs.append(discrete_entropy(counts))
    deltas.append(delta)
Hs = np.array(Hs)
deltas = np.array(deltas)
h = gaussian_differential_entropy(velocity_sigma)
minus_log_delta = -np.log(deltas)

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(minus_log_delta, Hs, 'o', color='#4C72B0', ms=8, label='$H$')
xline = np.linspace(minus_log_delta.min() - 0.1,
                    minus_log_delta.max() + 0.1, 50)
ax.plot(xline, h + xline, color='#C44E52', lw=2, label='$h-\\log\\Delta$')
ax.axhline(h, color='#55A868', ls='--', lw=2, label='$h$')
ax.set_xlabel('$-\\log\\Delta$')
ax.set_ylabel('nats')
ax.legend(fontsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
mlai.write_figure('log-delta-divergence.svg',
                  directory='\writeDiagramsDir/information')}

\figure{\includediagram{\diagramsDir/information/log-delta-divergence}{80%}}{Discrete entropy of an equal-width Gaussian histogram against $-\log\Delta$. The points track $h-\log\Delta$; $h$ is the finite part. The continuous limit discards a term that diverges.}{log-delta-divergence}

\endif
