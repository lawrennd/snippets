\ifndef{groupingStaticVsEnsemble}
\define{groupingStaticVsEnsemble}

\editme

\subsection{Static Bookkeeping Versus a Physical Ensemble}

\slides{The grouping identity needs no dynamics. Reading $p$ as an ensemble does.}

\slidesincremental{
* Die identity: true for any $p$ and any partition, at one instant
* Physical ensemble: stationarity (and usually ergodicity) so averages match long-run time
* Equilibrium: each group has settled; only the weights $w_i$ can still move
}

\speakernotes{Forward pointer only. No Markov chains, no lumpability, no glasses today. Finite-time later this lecture will move $w$; Crooks weeks 6–7; DPI week 8.}

\notes{The decomposition $H=H(w)+\sum_i w_i H(p_i)$ is pure bookkeeping on a single distribution. The die roll has no temporal dynamics because we used the identity only as accounting. Interpreting $p$ as ``the distribution of the system's state'' adds a dynamical hypothesis: something like stationarity plus ergodicity, so that an ensemble average equals what one trajectory shows over long time. Equilibrium thermodynamics makes the same move. The equilibrium density is stationary under the microscopic dynamics, and thermodynamic entropy is then a time-independent number of the form
\begin{align}
S = H(w) + \sum_i w_i H(\pi_i)
\end{align}
when each group has relaxed to its own conditional stationary law $\pi_i$ and only the coarse weights remain to carry slow change. Dynamics \emph{inside} and \emph{between} groups --- local equilibrium, lumpability, broken ergodicity, and the decay of $\text{KL}$ --- return in weeks 3--4 and 8.}

\newslide{What Comes Next}

\slides{Today the die is frozen. Later lectures thaw the groups.}

\slidesincremental{
* Week 3: name local equilibrium --- $p_i\approx\pi_i$, $w(t)$ may move
* Week 4: demon sorts groups; Landauer wells freeze $w_i$
* Weeks 6--7: finite-time driving moves $w$ on the equilibrium manifold
* Week 8: $\text{KL}(p_t\|\pi)$ falls; same split for approach to equilibrium
}

\endif
