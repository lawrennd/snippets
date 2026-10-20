\ifndef{relativeEntropyDecayGrouping}
\define{relativeEntropyDecayGrouping}

\editme

\subsection{KL Decay and Grouping}

\slides{Under Markov dynamics, $\KL{p_t}{\pi}$ falls --- coarse-graining in time.}

\slidesincremental{
* Physics often says ``relative entropy''; same object as week-3 / week-6 KL
* Data-processing for distributions: each step cannot increase divergence to equilibrium
* Same grouping split as the die, now for approach to $\pi$:
}

\slidesmall{
$$
\KL{p}{\pi}=\KL{w}{w_\pi}+\sum_i w_i\, \KL{p_i}{\pi_i}
$$
}

\speakernotes{After proving DPI for mutual information, give the dynamical face. Course notation is $\KL{\cdot}{\cdot}$ throughout; ``relative entropy'' is optional physics prose. Board the split: between-group redistribution versus within-group relaxation. Hamiltonian aside: fine-grained $H$ conserved; only coarse-grained entropy grows (Ehrenfest).}

\notes{For a Markov process with stationary distribution $\pi$, $\KL{p_t}{\pi}$ is nonincreasing --- the data-processing inequality applied to the evolving law. (Physics literature often calls the same functional relative entropy.) Decompose $p$ into group weights $w$ and conditionals $p_i$, and likewise $\pi$ into $w_\pi$ and $\pi_i$. Then
\begin{align}
\KL{p}{\pi}=\KL{w}{w_\pi}+\sum_i w_i\, \KL{p_i}{\pi_i}.
\end{align}
The first term is how far the macro weights sit from equilibrium weights; the second is residual non-equilibrium inside groups. Local equilibrium is the regime $\KL{p_i}{\pi_i}\approx 0$ with $\KL{w}{w_\pi}$ still free to fall. Under deterministic Hamiltonian flow the fine-grained Shannon entropy of the phase-space density is conserved (Liouville); the Gibbs--Ehrenfest account of the second law is that only a \emph{coarse-grained} entropy increases. Week 2's die made the static split; this is the same algebra along a trajectory toward equilibrium.}

\newslide{Arrow of Time from the Same Split}

\slides{How much of equilibration is between groups, how much within?}

\slidesincremental{
* Between: $\KL{w}{w_\pi}$ --- redistribution of macro probability
* Within: $\sum_i w_i \KL{p_i}{\pi_i}$ --- relaxation to local $\pi_i$
* Demon / Crooks / transport: all move mass among groups while baths handle the rest
}

\notes{Information engines and finite-time protocols act primarily on the between-group term --- changing which macrostate or which bit is occupied --- while assuming or enforcing fast decay of the within-group divergences. That is why week 2's stationary examples and week 6's paths on the equilibrium manifold belong to one story.}

\endif
