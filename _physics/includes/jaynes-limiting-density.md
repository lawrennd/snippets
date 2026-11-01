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
* $m$ is Jaynes' limiting density of discrete points --- the binning, written as a density
* Uniform $m$ in $v_x$ recovers ordinary $h(v_x)$
* Uniform $m$ in 3D velocity is $m(s)\propto s^2$ in speed
}

\speakernotes{Name $m$. Do not do Lagrange, the die, or MaxEnt --- those snippets already exist. The Gaussian versus Maxwell disagreement was an undeclared change of $m$. KL against a common $m$ is invariant; see relative-entropy-reparametrisation.}

\notes{Differential entropy $h=-\int f\log f\,{\mathrm{d}}x$ pretends the coordinate measure is part of the data. The histogram arithmetic showed that it is not: $H$ is a functional of masses, and the passage to a density subtracts $\sum_i p_i\log\Delta_i$, whose continuum limit is the log of a reference density $m$. Jaynes called $m$ the *limiting density of discrete points* --- the binning measure, promoted to a density [@Jaynes-information63].

Once $m$ is written down,
\begin{align}
h_m(f)
  = -\int f\log\frac{f}{m}\,{\mathrm{d}}x
  = -\KL{f}{m}.
\end{align}
Taking $m$ uniform (Lebesgue) in the Cartesian component $v_x$ recovers the ordinary Gaussian remainder $h(v_x)$. Taking $m$ uniform in three-dimensional velocity, and writing it in the speed coordinate, gives $m(s)\propto s^2$ --- the shell volume that had been hiding in the Jacobian. The two Maxwell--Boltzmann entropies disagreed because each $h$ used a different undeclared $m$. Relative entropy makes the choice explicit. The Jacobian cancels inside $\KL{f}{m}$ under a common invertible map; the discrete KL has no divergent $-\log\Delta$ term. The map $\mathbf{v}\mapsto s=|\mathbf{v}|$ is *not* invertible. Equality of KL in the speed coordinate with KL in 3D velocity holds *here* because both $f$ and Lebesgue on $\mathbb{R}^3$ are isotropic, so both lose the same direction information. In general the data-processing inequality gives $\le$, not $=$.

This names $m$. Maximising $h_m$ at fixed mean energy --- Jaynes' maximum entropy principle --- is a later step.}

\addreading{@Jaynes-information63}{limiting density of discrete points}

\endif
