\ifndef{twoSpinMaxent}
\define{twoSpinMaxent}

\editme

\subsection{Two Spins, One Coupling}

\notes{Every MaxEnt example so far constrains a function of one variable: a face, an energy, a bit, a feature of a labelled pair. The next legal constraint is a *product*. Take two Ising spins $s_1,s_2\in\{+1,-1\}$ and prescribe the two magnetisations and the correlation,
\begin{align}
\langle s_1\rangle &= m_1, &
\langle s_2\rangle &= m_2, &
\langle s_1 s_2\rangle &= c.
\end{align}
Four states, three moment constraints, plus normalisation. The sufficient statistic is $T(s)=(s_1,s_2,s_1 s_2)$. MaxEnt returns the two-spin Ising model [@Ising-ferromagnetism25],
$$
p(s_1,s_2) = \exp\bigl(h_1 s_1 + h_2 s_2 + J s_1 s_2 - A(h,J)\bigr).
$$
The Lagrange multiplier on the correlation *is* the coupling $J$. Temperature sits in the multipliers; there is nothing else to introduce.}

\slides{
$$
p(s)\propto\exp(h_1 s_1+h_2 s_2+J s_1 s_2)
$$
* Constraints: $\langle s_1\rangle$, $\langle s_2\rangle$, $\langle s_1 s_2\rangle$
* $J$ is the multiplier on a correlation
}

\newslide{The Same Hamiltonian, Two Readings}

\notes{Physics reads an energy $H=-(h_1 s_1+h_2 s_2+J s_1 s_2)$ and a Boltzmann occupation. Machine learning reads the smallest Boltzmann machine [@Ackley-boltzmann85]: an undirected pair whose parameters are fit by matching those three moments. Inverse Ising *is* that fit.

@Schneidman-weak06 put the same model on retinal spike words. They recorded 40 salamander ganglion cells watching natural movies, binned spikes at 20~ms, and treated each bin as a binary word. Pairwise correlations were weak, but the independent model failed by orders of magnitude: a ten-cell pattern that occurred once a minute was predicted once every three years, and $P(K=10)$ simultaneous spikes was $\sim 10^{5}$ times the independent rate. The pairwise MaxEnt model --- the Ising model whose $T$ is the magnetisations and the pairwise products --- recovered $I^{(2)}/I_N\sim 90\%$ of the multi-information in groups of ten cells. That fraction held for different movies, for guinea-pig retina, and for cultured cortex. A stimulus-driven conditional-independence model, with two hundred times as many parameters, did worse. Week 7's $I=\sum h_i-H$ is their $I_N$.

Do not fit a retina today. See that a correlation is a legal $T$, and that the energy and the classifier are the same exponential family.}

\slidesincremental{
* Physics: two interacting moments
* ML: a two-unit Boltzmann machine
* Inverse Ising $=$ match the moments
}

\notes{Week 6's $m$-projection is this matching, written geometrically. Week 7's multi-information $I=\sum h_i-H$ is the extra reduction in joint entropy that $J$ buys. Paths, caliber, and Schrödinger bridges wait until week 8. The algorithm that finds the MaxEnt *coupling* of two prescribed marginals --- Sinkhorn, or iterative proportional fitting --- waits with them: that is the same exponential family with a different constraint set (the full row and column sums, not three moments). Four states is small enough to write the partition function by hand,
$$
Z= e^{J}(e^{h_1+h_2}+e^{-h_1-h_2})+e^{-J}(e^{h_1-h_2}+e^{-h_1+h_2}),
$$
or to reuse the optimiser from the die.}

\addreading{@Ising-ferromagnetism25}{the original one-dimensional model}
\addreading{@Ackley-boltzmann85}{Boltzmann machines}
\addreading{@Schneidman-weak06}{pairwise MaxEnt on a retina}

\endif
