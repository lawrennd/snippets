\ifndef{radonNikodymDensityRatio}
\define{radonNikodymDensityRatio}

\editme

\subsection{The Form of the Radon--Nikodym Derivative}

\slides{If $\mu$ is absolutely continuous with respect to $\nu$, there is a density $\mathrm{d}\mu/\mathrm{d}\nu$.}

\slidesmall{
$$
\mu(A)=\int_A \frac{\mathrm{d}\mu}{\mathrm{d}\nu}\,\mathrm{d}\nu
$$
}

\slidesincremental{
* Densities $f$ and $m$ against Lebesgue: $\mathrm{d}F/\mathrm{d}m=f/m$
* That ratio is what sits inside $\KL{f}{m}$
* The width ratio $\Delta s_i/\Delta u_i$ was the same object on a partition
}

\speakernotes{One slide. Write $\mathrm{d}F/\mathrm{d}m=f/m$ on the board. Point back at $\Delta s_i/\Delta u_i$ and forward at Jaynes' $m$. No $\sigma$-algebras.}

\notes{Absolute continuity is the continuum name for what the shared partition already enforced: every cell that carries mass under one description carries mass under the other. When a measure $\mu$ is absolutely continuous with respect to a measure $\nu$ on the same space, there exists a nonnegative density --- the Radon--Nikodym derivative --- such that
\begin{align}
\mu(A)
  = \int_A \frac{\mathrm{d}\mu}{\mathrm{d}\nu}\,\mathrm{d}\nu
\end{align}
for every measurable $A$. That is the definition. The object is a function, not a metaphor.

Specialise to the densities that this lecture has been writing. Let $F$ have density $f$ against Lebesgue, and let $m$ be another density against the same Lebesgue (Jaynes' reference, still undeclared). Then
\begin{align}
\frac{\mathrm{d}F}{\mathrm{d}m}
  = \frac{f}{m}.
\end{align}
Relative entropy is the expectation of the log of that ratio,
\begin{align}
\KL{f}{m}
  = \int f\log\frac{\mathrm{d}F}{\mathrm{d}m}\,\mathrm{d}x
  = \int f\log\frac{f}{m}\,\mathrm{d}x.
\end{align}
The bin-width ratio $\Delta s_i/\Delta u_i$ of the previous snippet is the same statement on a finite partition: it is the discrete Radon--Nikodym derivative of Lebesgue-on-speed with respect to Lebesgue-on-volume. In the continuum that ratio becomes the Jacobian. Naming $\mathrm{d}F/\mathrm{d}m=f/m$ makes the next step --- declaring $m$ --- a change of *what one divides by*, not a change of vocabulary.}

\endif
