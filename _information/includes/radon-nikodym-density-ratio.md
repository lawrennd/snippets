\ifndef{radonNikodymDensityRatio}
\define{radonNikodymDensityRatio}

\editme

\subsection{Radon-Nikodym Derivative}

\slides{Recall RN derivative between measures.}

\subsection{The Form of the Radon-Nikodym Derivative}

\slides{If $\mu$ is absolutely continuous with respect to $\nu$, there is a density $\mathrm{d}\mu/\mathrm{d}\nu$.}

\slidesmall{
$$
\mu(A)=\int_A \frac{\mathrm{d}\mu}{\mathrm{d}\nu}\,\mathrm{d}\nu
$$
}

\slidesincremental{
* $M$ has density $m$: $\mathrm{d}F/\mathrm{d}M=f/m$
* That ratio is what sits inside $\KL{f}{m}$
* The width ratio $\Delta s_i/\Delta u_i$ was the same object on a partition
}

\speakernotes{One slide. Write $\mathrm{d}F/\mathrm{d}M=f/m$ on the board: $M$ is the measure with density $m$, not $m$ itself. Point back at $\Delta s_i/\Delta u_i$ and forward at Jaynes' $m$. No $\sigma$-algebras.}

\notes{Absolute continuity is the continuum name for what the shared partition already enforced: every cell that carries mass under one description carries mass under the other. When a measure $\mu$ is absolutely continuous with respect to a measure $\nu$ on the same space, there exists a nonnegative density - the Radon-Nikodym derivative - such that
\begin{align}
\mu(A)
  = \int_A \frac{\mathrm{d}\mu}{\mathrm{d}\nu}\,\mathrm{d}\nu
\end{align}
for every measurable $A$.

Now let's focus on the densities that we've been considering. Let $F$ have density $f$ against Lebesgue measure $\lambda$, and let $M$ be Jaynes' reference measure, with density $m$ against the same $\lambda$. Provided $m(x)=0$ only where $f(x)=0$ (so $F\ll M$), we can write
\begin{align}
F(A)
  &= \int_A f\,\mathrm{d}x \nonumber\\
  &= \int_A \frac{f}{m}\, m\,\mathrm{d}x \nonumber\\
  &= \int_A \frac{f}{m}\,\mathrm{d}M,
\end{align}
The middle step is just the statement that $M$ assigns mass $m(x)\,\mathrm{d}x$ to the sliver $[x,x+\mathrm{d}x]$, so $\mathrm{d}M = m\,\mathrm{d}x$ (just as $\mathrm{d}F = f\,\mathrm{d}x$). In Jaynes' picture $m(x)\,\mathrm{d}x$ is the fraction of reference points in the sliver, so $\int_A g\,\mathrm{d}M$ is the average of $g$ over the points in $A$, and $f/m$ is the mass of $F$ carried per reference point. By uniqueness of the Radon--Nikodym derivative
\begin{align}
\frac{\mathrm{d}F}{\mathrm{d}M} = \frac{f}{m}.
\end{align}
This is the chain rule $\frac{\mathrm{d}F}{\mathrm{d}M} = \frac{\mathrm{d}F/\mathrm{d}\lambda}{\mathrm{d}M/\mathrm{d}\lambda}$. Under a change of variables both $f$ and $m$ pick up the same Jacobian, which cancels in the ratio, so $f/m$ is coordinate-free even though neither density is. Relative entropy is the expectation under $F$ of the log of that ratio,
\begin{align}
\KL{f}{m}
  = \int f\log\frac{\mathrm{d}F}{\mathrm{d}M}\,\mathrm{d}x
  = \int f\log\frac{f}{m}\,\mathrm{d}x,
\end{align}
and it is finite only when the absolute-continuity condition holds.

The bin-width ratio $\Delta s_i/\Delta u_i$ of the previous snippet is the same statement on a finite partition: it is the discrete Radon-Nikodym derivative of Lebesgue-on-speed with respect to Lebesgue-on-volume. In the continuum that ratio becomes the Jacobian. Naming $\mathrm{d}F/\mathrm{d}M=f/m$ makes the next step - declaring $m$ - a change of *what one divides by*, not a change of vocabulary.}

\endif
