\ifndef{differentialEntropyBinning}
\define{differentialEntropyBinning}

\editme

\subsection{Discrete Entropy from Binning}

\slides{Discrete $H$ is well defined. Differential $h$ is what remains after subtracting $\ln\Delta$.}

\slidesincremental{
* Bin $X$ with width $\Delta$: $p_i\approx f(x_i)\Delta$
* $H(X^\Delta)\approx h(X)-\ln\Delta$
* As $\Delta\to 0$, discrete $H$ diverges; $h$ is the finite part
}

\speakernotes{Board $p_i\approx f\Delta$ for one bin. The $-\ln\Delta$ is the price of resolving more finely. Relabelling with $y=g(x)$ while keeping uniform bins in $y$ changes the partition in $x$.}

\notes{Partition the real line into bins of width $\Delta$. Then $p_i\approx f(x_i)\Delta$ and
\begin{align}
H(X^\Delta)
  = -\sum_i p_i\ln p_i
  \approx h(X)-\ln\Delta.
\end{align}
Shannon entropy of the binned variable is non-negative and diverges as the bins shrink. Differential entropy is the $\Delta$-independent remainder.

Now relabel $y=g(x)$. Uniform bins of width $\Delta$ in $y$ correspond to bins of width $\Delta/|g'|$ in $x$ — a non-uniform partition of the original line. A *fixed* discrete partition is unchanged by renaming outcomes, but ``uniform bins of fixed width'' is a *different* partition in each coordinate. That is exactly where $\mathbb{E}\ln|g'|$ appears. Continuous entropy therefore depends on a choice of reference measure (here, bin width in the chosen coordinate).}

\newslide{Phase Space Needs a Cell Size}

\slides{Classical statistical mechanics faces the same issue: $S$ needs a cell volume in phase space.}

\slidesincremental{
* Cell size $h^{3N}$ makes dimensionless occupation numbers
* Liouville: canonical maps have unit Jacobian — phase-space entropy is invariant under them
* A generic change of variables is not canonical
}

\notes{Boltzmann counting needs a phase-space cell of volume $h^{3N}$ (Planck's constant to the power of degrees of freedom) before $S=k\ln W$ is meaningful. Liouville's theorem helps for Hamiltonian flow: canonical transformations preserve phase-space volume, so the reference measure is unchanged. An arbitrary reparametrisation of coordinates does not.}

\endif
