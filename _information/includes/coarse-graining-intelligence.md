\ifndef{coarseGrainingIntelligence}
\define{coarseGrainingIntelligence}

\editme

\subsection{Coarse-Graining as Abstraction}

\slides{Bernoulli already coarse-grained. Intelligence does it constantly.}

\slidesincremental{
* Kinetic theory: keep pressure; discard each molecule's curve
* Thermodynamics: keep $T,V,P$; discard which microstate
* Perception / ML: pixels $\to$ features $\to$ concepts
}

\speakernotes{Callback to the early ensemble block and to Jaynes' anthropomorphic entropy below. One slide only --- the die gave the accounting; this is the moral.}

\notes{Daniel Bernoulli did not integrate Laplace's curve for every corpuscle. He replaced the swarm with a coarse mechanical story that still predicts pressure --- exactly keeping a group-level description and discarding within-group path detail. Thermodynamic macrostates are the same move with better bookkeeping: the entropy $S$ is the uncertainty still unresolved *inside* the macrostate. In intelligent systems the hierarchy is familiar: raw observations are partitioned into features, features into concepts. At each level you retain $H(w)$ for the labels you use and lose $\sum_i w_i H(p_i)$ for the distinctions you refuse to make. Which partition you choose is Jaynes' and Wigner's anthropomorphic choice of degrees of freedom --- coming next in this review.}

\newslide{Bridge Back to the Ensemble}

\slides{Macrostate $=$ group. Microstate $=$ face inside the group.}

\slidesincremental{
* Information lost by the macro description: $\sum_i w_i H(p_i)$
* That is what thermodynamic entropy is counting
* Same bookkeeping from atoms to gas, or pixels to concepts
}

\endif
