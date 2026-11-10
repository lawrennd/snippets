\ifndef{jaynesLimitingDensity}
\define{jaynesLimitingDensity}

\editme

\subsection{Jaynes: Promote the Bins to a Measure}

\slides{The well-defined continuum object is relative entropy against a declared $m$.}

\slidesmall{
$$
h_m(f)=-\int f\log\frac{f}{m}\,{\mathrm{d}}x=-\KL{f}{m}
$$
}

\slidesincremental{
* $m$ is Jaynes' limiting density of discrete points — the binning, written as a density
* $m$ = density of bins: Gaussian $m$ means fine bins in the centre
* Uniform $m$ in $v_x$ recovers ordinary $h(v_x)$
* Uniform $m$ in 3D velocity is $m(s)\propto s^2$ in speed
}

\speakernotes{Name $m$ as the density of the bins. A Gaussian $m$ crowds points at the centre and thins them in the tails. Do not do Lagrange, the die, or MaxEnt --- those snippets already exist. The Gaussian versus Maxwell disagreement was an undeclared change of $m$. KL against a common $m$ is invariant; see relative-entropy-reparametrisation.}

\notes{Differential entropy $h=-\int f\log f\,{\mathrm{d}}x$ pretends the coordinate measure is part of the data. The histogram arithmetic showed that it is not: $H$ is a functional of masses, and the passage to a density subtracts $\sum_i p_i\log\Delta_i$. Jaynes called $m$ the *limiting density of discrete points* --- the binning measure, promoted to a density [@Jaynes-information63].

Concretely, Jaynes places $N$ points so that the number falling in $[a,b]$ is approximately $N\int_a^b m\,\mathrm{d}x$. Each point then owns a cell of width $\Delta_i\approx 1/(N m(x_i))$ and reference mass $1/N$: $m$ says where the cells are fine and where they are coarse, and every cell is equally likely a priori. For a Gaussian $m$ the points are its quantiles, crowded in the centre and sparse in the tails. With $p_i\approx f(x_i)\Delta_i$,
\begin{align}
H_N = -\sum_i p_i\log p_i \approx \log N - \int f\log\frac{f}{m}\,\mathrm{d}x,
\end{align}
so the divergence is a pure count of cells, $\log N$, and what remains is $h_m$. When $f=m$ every cell gets mass $1/N$, $H_N=\log N$ and $h_m=0$, its maximum: $h_m$ measures how far $f$ is from spreading evenly over the cells that $m$ declares.

Once $m$ is written down,
\begin{align}
h_m(f)
  = -\int f\log\frac{f}{m}\,{\mathrm{d}}x
  = -\KL{f}{m}.
\end{align}
Taking $m$ uniform (Lebesgue) in the Cartesian component $v_x$ recovers the ordinary Gaussian remainder $h(v_x)$ (an improper $m$; $h_m$ is then defined up to an additive constant). Taking $m$ uniform in three-dimensional velocity, and writing it in the speed coordinate, gives $m(s)\propto s^2$ --- also improper --- the shell volume that the concentric rings made geometric and that had been hiding in the Jacobian. The map $\mathbf{v}\mapsto s=|\mathbf{v}|$ is *not* invertible. Equality of KL in the speed coordinate with KL in 3D velocity holds *here* because the ratio $f/m$ depends on $\mathbf{v}$ only through $s$, so $s$ is sufficient and the data-processing inequality holds with equality. In general the data-processing inequality gives $\le$, not $=$.

The two Maxwell--Boltzmann entropies disagreed because each $h$ used a different undeclared $m$. Relative entropy makes the choice explicit. The Jacobian cancels inside $\KL{f}{m}$ under a common invertible map; the discrete KL has no divergent $-\log\Delta$ term.

Going continuous buys analytic machinery; it does not remove the need to declare $m$. Which binning --- which degrees of freedom --- you treat as "equally likely a priori" remains an anthropomorphic choice in Jaynes' sense. This names $m$. Maximising $h_m$ at fixed mean energy --- Jaynes' maximum entropy principle --- is the next lecture.}

\addreading{@Jaynes-information63}{limiting density of discrete points}

\endif
