\ifndef{relativeEntropyDecayGrouping}
\define{relativeEntropyDecayGrouping}

\editme

\subsection{Relative Entropy Decay and Grouping}

\slides{Under Markov dynamics, relative entropy $D(p_t\|\pi)=D_{\mathrm{KL}}(p_t\|\pi)$ falls --- coarse-graining in time.}

\slidesincremental{
* Same object as week 3 KL --- ``relative entropy'' is the physics name
* Data-processing for distributions: each step cannot increase divergence to equilibrium
* Same grouping split as the die, now for approach to $\pi$:
}

\slidesmall{
$$
D(p\|\pi)=D(w\|w_\pi)+\sum_i w_i\, D(p_i\|\pi_i)
$$
}

\speakernotes{After proving DPI for mutual information, give the dynamical face. Name the synonym once: $D\equiv D_{\mathrm{KL}}\equiv\text{KL}$ from week 3; not a discrete/continuous split. Board the split: between-group redistribution versus within-group relaxation. Hamiltonian aside: fine-grained $H$ conserved; only coarse-grained entropy grows (Ehrenfest).}

\notes{Relative entropy here is Kullback--Leibler divergence --- the same functional introduced in week 3 as $\text{KL}(p\|q)$ and written $D(\cdot\|\cdot)$ when discussing reparametrisation invariance. The two names are synonyms in this course; we do not reserve one for discrete and the other for continuous. For a Markov process with stationary distribution $\pi$, $D(p_t\|\pi)$ is nonincreasing --- the data-processing inequality applied to the evolving law. Decompose $p$ into group weights $w$ and conditionals $p_i$, and likewise $\pi$ into $w_\pi$ and $\pi_i$. Then
\begin{align}
D(p\|\pi)=D(w\|w_\pi)+\sum_i w_i\, D(p_i\|\pi_i).
\end{align}
The first term is how far the macro weights sit from equilibrium weights; the second is residual non-equilibrium inside groups. Local equilibrium is the regime $D(p_i\|\pi_i)\approx 0$ with $D(w\|w_\pi)$ still free to fall. Under deterministic Hamiltonian flow the fine-grained Shannon entropy of the phase-space density is conserved (Liouville); the Gibbs--Ehrenfest account of the second law is that only a \emph{coarse-grained} entropy increases. Week 2's die made the static split; this is the same algebra along a trajectory toward equilibrium.}

\newslide{Arrow of Time from the Same Split}

\slides{How much of equilibration is between groups, how much within?}

\slidesincremental{
* Between: $D(w\|w_\pi)$ --- redistribution of macro probability
* Within: $\sum_i w_i D(p_i\|\pi_i)$ --- relaxation to local $\pi_i$
* Demon / Crooks / transport: all move mass among groups while baths handle the rest
}

\notes{Information engines and finite-time protocols act primarily on the between-group term --- changing which macrostate or which bit is occupied --- while assuming or enforcing fast decay of the within-group divergences. That is why week 2's stationary examples and week 6's paths on the equilibrium manifold belong to one story.}

\endif
