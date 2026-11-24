\ifndef{relativeEntropyDecayGrouping}
\define{relativeEntropyDecayGrouping}

\editme

\subsection{KL Decay and Grouping}

\newslide{Approach to Equilibrium Is Data Processing}

\slides{Under a Markov step with stationary $\pi$, $\KL{p_t}{\pi}$ cannot rise.}

\slidesincremental{
* Markov step: $p_{t+1}=p_tK$, and $\pi K=\pi$
* Data processing with $q=\pi$: $\KL{p_{t+1}}{\pi}\le\KL{p_t}{\pi}$
* If $\pi$ is uniform, $\KL{p}{\pi}=\log N - H(p)$: entropy rises
}

\notes{The data-processing inequality for distributions gives the approach to equilibrium almost for free. Let $K$ be a Markov transition kernel with stationary distribution $\pi$, so $\pi K=\pi$. Apply $\KL{pK}{qK}\le\KL{p}{q}$ with $q=\pi$:
$$
\KL{p_{t+1}}{\pi}=\KL{p_tK}{\pi K}\le\KL{p_t}{\pi}.
$$
The divergence to equilibrium never increases. (Physicists often call this functional the relative entropy; it is the same object.) When $\pi$ is uniform on $N$ states, $\KL{p}{\pi}=\log N-H(p)$, so this is the statement that Shannon entropy never decreases. $\pi$ is uniform exactly when $K$ is doubly stochastic: its columns, as well as its rows, sum to one.}

\newslide{Where Liouville Fits}

\slides{Fine-grained flow is the equality case. The rise needs a coarse graining that forgets.}

\slidesincremental{
* Hamiltonian flow is one-to-one and keeps volume: $\KL{}{}$ and $H$ are constant
* Equal-volume cells tiling an invariant region: cell-to-cell matrix is doubly stochastic
* Forget the detail inside cells at each step (Ehrenfest): coarse $H$ rises monotonically
* Keep the detail: the flow can be run backwards, and no monotone rise is guaranteed
}

\notes{Liouville's theorem and the data-processing inequality fit together precisely. Deterministic Hamiltonian flow is a one-to-one map on phase space that keeps volume. One-to-one is the equality case of data processing, so the fine-grained entropy, and the KL divergence to the uniform (microcanonical) distribution, do not change at all.

Now divide a region of phase space that the flow maps onto itself (an energy shell, say) into cells of equal volume, and record only which cell the state is in. Let $P_{ij}$ be the fraction of cell $i$ that the flow carries into cell $j$ over a time step. Each row sums to one. Because the flow keeps volume, each column does too: the volume arriving in cell $j$ is the volume of cell $j$. So $P$ is doubly stochastic, and the uniform distribution over cells is stationary.

If at every step we replace the true distribution by one that is uniform inside each cell, keeping only the cell weights, the cell weights evolve as a Markov chain with matrix $P$. Data processing then says their Shannon entropy can only rise. This is the Gibbs--Ehrenfest account of the second law, and it shows exactly where the rise comes from: from the decision to forget the detail inside the cells at each step. If we keep that detail, the true dynamics is reversible, the cell sequence is not in general Markov, and the coarse-grained entropy is free to fall as well as rise (Loschmidt's objection).}

\newslide{Arrow of Time from the Grouping Split}

\slides{How much of equilibration is between groups, how much within?}

\slidesmall{
$$
\KL{p}{\pi}=\KL{w}{w_\pi}+\sum_i w_i\, \KL{p_i}{\pi_i}
$$
}

\slidesincremental{
* Between: $\KL{w}{w_\pi}$ --- how far the group weights are from equilibrium
* Within: $\sum_i w_i \KL{p_i}{\pi_i}$ --- how far each group is from local equilibrium
* Local equilibrium: within-group terms near zero, between-group term still falling
}

\notes{Decompose $p$ into group weights $w$ and within-group conditionals $p_i$, and likewise $\pi$ into $w_\pi$ and $\pi_i$. The chain rule for KL divergence gives
$$
\KL{p}{\pi}=\KL{w}{w_\pi}+\sum_i w_i\, \KL{p_i}{\pi_i}.
$$
This is the grouping formula for entropy, now written relative to equilibrium. The first term measures how far the macroscopic weights are from their equilibrium values. The second measures what is left out of equilibrium inside the groups. The Ehrenfest step above sets every $\KL{p_i}{\pi_i}$ to zero, which is why it can only lower the total. Local equilibrium is the regime where the within-group terms are already close to zero and the between-group term is still falling. Information engines and finite-time protocols mostly act on the between-group term, moving probability between macrostates, while relying on fast relaxation inside each group.}

\endif
