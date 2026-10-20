\ifndef{localEquilibriumGrouping}
\define{localEquilibriumGrouping}

\editme

\subsection{Local Equilibrium as Grouping}

\slides{Equilibrium is the special case where within-group dynamics is fast.}

\slidesmall{
$$
S(t)=H\bigl(w(t)\bigr)+\sum_i w_i(t)\, H(\pi_i)
$$
}

\slidesincremental{
* Groups $=$ macrostates; $\pi_i=$ conditional equilibrium inside group $i$
* Timescale separation: $p_i$ relaxes quickly to $\pi_i$; $w_i(t)$ evolves slowly
* Thermodynamic entropy at fixed macrostate is the within-group term
}

\speakernotes{Answers ``equilibrium versus non-equilibrium? (first cut)'' from the define list. Non-eq: either $p_i\neq\pi_i$ still relaxing, or $w(t)$ driven. No proof of Markov mixing.}

\notes{Week 2's grouping identity holds at every instant. Local equilibrium is the dynamical regime in which each within-group distribution has already settled to its conditional stationary law $\pi_i$, while the coarse weights $w_i(t)$ may still change on a slower clock. Then
\begin{align}
S(t)=H\bigl(w(t)\bigr)+\sum_i w_i(t)\, H(\pi_i).
\end{align}
Macroscopic thermodynamics lives in this picture: the within-group sum is the entropy attributed to a fixed macrostate, and the slow story is redistribution of probability among macrostates. Non-equilibrium, at this first cut, means either the groups have not finished relaxing ($p_i\neq\pi_i$) or an external protocol is driving $w(t)$ (finite-time thermodynamics; Crooks length in weeks 6--7).}

\newslide{Stationary Occupation Revisited}

\slides{Gibbs--Boltzmann $p_i\propto e^{-\beta E_i}$ is a \emph{stationary} assignment --- not a path.}

\slidesincremental{
* MaxEnt / canonical ensemble fix $\pi$, not $\dot\pi$
* The die was the static analogue: one $p$, no roll dynamics
* Next week: a demon that sorts on group labels while assuming fast mixing inside
}

\endif
