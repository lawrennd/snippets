\ifndef{landauerBrokenErgodicityWeights}
\define{landauerBrokenErgodicityWeights}

\editme

\subsection{Broken Ergodicity as Frozen Weights}

\slides{The two wells are ergodic components. The bit is which component --- a frozen $w$.}

\slidesincremental{
* Barrier $\gg k_BT$: almost no crossing on experimental timescales
* Stationary measure is no longer unique: $\pi = \sum_i w_i \pi_i$ over components
* Weights $w_i$ set by preparation; they do not relax --- $H(w)$ is frozen
}

\speakernotes{Tie the equal double well to week 2 grouping. Equilibrium thermo often silently conditions on one component and drops $H(w)$. Erasure merges components and must pay for that forgotten term.}

\notes{Week 2's grouping identity returns with a dynamical reading. When barriers trap the system in disconnected basins, ergodicity breaks: the long-run behaviour depends on which basin you started in. The invariant measures decompose as
\begin{align}
\pi = \sum_i w_i\, \pi_i
\end{align}
over ergodic components $\pi_i$ (here: left well and right well). The coarse weights $w_i$ are fixed by the initial condition and do not equilibrate on the timescale of interest, so $H(w)$ is a frozen contribution that equilibrium bookkeeping often conditions away by declaring ``the system is in well $0$.'' Landauer erasure merges the wells: it destroys that frozen distinction and must pay at least $k_BT\ln 2$ when the bit was unknown --- exactly purchasing the discarded $H(w)$ from the bath. Glasses are the many-basin version of the same story.}

\newslide{Erase Buys Back $H(w)$}

\slides{Reset merges components; the within-well term was never the whole entropy.}

\slidesincremental{
* Store / read: live inside one $\pi_i$; $H(w)$ encodes which
* Erase: force a single well --- remove the group label
* Cost $\ge k_BT H(w)$ when $w$ was unknown (equiprobable bit: $\ln 2$)
}

\endif
