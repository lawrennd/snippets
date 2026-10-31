\ifndef{gaussianHistogramDiscreteEntropy}
\define{gaussianHistogramDiscreteEntropy}

\editme

\include{_physics/includes/ideal-gas-velocity-sample.md}

\subsection{Entropy of a Gaussian Velocity Histogram}

\slides{Equal-width bins of one Cartesian component. Discrete $H$ is a sum over masses.}

\slidesincremental{
* $p_i = n_i/N$ from equal-$\Delta v$ bins of $v_x\sim\gaussianSamp{0}{\dataStd^2}$
* $H=-\sum_i p_i \log p_i$ depends only on those masses
* Analytic $h=\tfrac12\log(2\pi e \dataStd^2)$; the histogram tracks $h-\log\Delta$
}

\speakernotes{Callback to the week-2 velocity histogram. Board $p_i\approx f\Delta$ once. The two numbers on the figure should agree; $h$ itself is smaller by $\log\Delta$ (and is negative if $\Delta$ is large). Nats throughout.}

\subsection{Histograms as Riemann Sums}

\slides{A histogram replaces $f(x)$ by a piecewise-constant function: height $f(x_i)$ on each bin of width $\Delta$.}

\slidesincremental{
* Bin mass $p_i = \int_{\text{bin } i} f(x)\,\text{d}x \approx f(x_i)\Delta$ (midpoint rule)
* $\sum_i g(x_i)\Delta \to \int g(x)\,\text{d}x$ as $\Delta\to 0$
* Used twice: $\sum_i f_i\Delta \approx 1$ and $-\sum_i f_i\log f_i\,\Delta \approx h$
* So $H \approx h - \log\Delta$: the $-\log\Delta$ comes from the $\Delta$ inside the log
}

\speakernotes{Draw the Gaussian, overlay rectangles of width $\Delta$ and height $f(x_i)$, shade one rectangle and label its area $p_i$. Then split $\log(f_i\Delta)$ on the board. Point out that the second sum is not a Riemann sum of anything finite as $\Delta\to 0$, which is why $H$ diverges while $h$ doesn't.}

\notes{Approximating a density by its value at the centre of each bin is a piecewise-constant (midpoint-rule) approximation to the integral. We call the corresponding sums Riemann sums. Writing $p_i\approx f(x_i)\Delta$ inside the entropy gives
\begin{align}
H = -\sum_i f_i\Delta\log f_i - \log\Delta\sum_i f_i\Delta \approx h - \log\Delta,
\end{align}
with both sums converging to integrals as $\Delta\to 0$.}

\notes{If we sample isotropic three-dimensional velocities and histogram one Cartesian component with equal-width bins. The discrete Shannon entropy of the occupancy is
\begin{align}
H = -\sum_i p_i\log p_i,
\qquad
p_i = n_i/N.
\end{align}
Note that empty bins don't contribute to the entropy. For a smooth density and a fine equal-width partition, $p_i\approx f(x_i)\Delta$ and
\begin{align}
H \approx h - \log \Delta,
\qquad
h = \tfrac12\log(2\pi e\dataStd^2).
\end{align}
The figure below reports both numbers. Note that they agree up to sampling and tail truncation. From this we can see that the differential entropy, $h$, is the $\Delta$-independent remainder. It is not the entropy of the histogram.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{vx_lim = 4.0
edges = np.linspace(-vx_lim, vx_lim, n_histogram_bins + 1)
delta = edges[1] - edges[0]
counts, _ = np.histogram(velocity_x, bins=edges)
H = discrete_entropy(counts)
h = gaussian_differential_entropy(velocity_sigma)
xs = np.linspace(-vx_lim, vx_lim, 400)
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.hist(velocity_x, bins=edges, density=True, color='#4C72B0', alpha=0.6,
        label='equal-$\\Delta v$ histogram')
ax.plot(xs, np.exp(-0.5 * xs**2 / velocity_sigma**2)
        / np.sqrt(2.0 * np.pi * velocity_sigma**2),
        color='#C44E52', lw=2, label='$\\mathcal{N}(0,\\sigma^2)$')
ax.set_xlim(-vx_lim, vx_lim)
ax.set_xlabel('$v_x$')
ax.set_ylabel('density')
ax.text(0.02, 0.95,
        f'$H={H:.3f}$\n$h-\\log\\Delta={h - np.log(delta):.3f}$\n$h={h:.3f}$',
        transform=ax.transAxes, va='top', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
ax.legend(loc='upper right', fontsize=9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
mlai.write_figure('gaussian-histogram-discrete-entropy.svg',
                  directory='\writeDiagramsDir/physics')}

\figure{\includediagram{\diagramsDir/physics/gaussian-histogram-discrete-entropy}{80%}}{Equal-width histogram of one Cartesian velocity component. Discrete $H$ matches $h-\log\Delta$; $h$ itself is the remainder after the bin-width term is subtracted.}{gaussian-histogram-discrete-entropy}

\endif
