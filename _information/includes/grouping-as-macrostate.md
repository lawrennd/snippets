\ifndef{groupingAsMacrostate}
\define{groupingAsMacrostate}

\editme

\subsection{Grouping Is a Choice of Abstraction}

\slides{Keeping $\{1,2,3\}$ versus $\{4,5,6\}$ and refusing the face is the same move as a macrostate.}

\slidesincremental{
* The group label is what we keep; $\sum_i w_i H(p_i)$ is what we refuse
* Macroscopic variables: extensive $N,V,E,S$; intensive $T,P$
* We cannot follow Laplace's curves, so we keep a few numbers
}

\speakernotes{Callback only --- extensive versus intensive was week 2. Do not re-derive. Do not open MaxEnt, Lagrange, or the demon. The next include, if you want it, is the Gaussian-Maxwell measure arc. Units: the die was bits; those figures are nats. Same $H$, different $\log$ base.}

\notes{The idealised information game fails when we turn to the mechanism. But we do have some control. We can coarse-grain, and reduce the search space. For example, the low/high grouping is a choice of abstraction. We keep a two-valued group label and throw away which of the three faces occurred. Coarse graining in thermodynamics can be seen similarly. We cannot track Laplace's curves for every molecule, instead we keep macroscopic numbers. Those macroscopic numbers split into *extensive* quantities that scale with the system (e.g. $N$, $V$, energy, entropy) and *intensive* quantities that do not (e.g. temperature, pressure). What we've seen is that these entropies can compose, so that the coarse-graining is coming from the form of entropy (as a function).  This means that accounting for information works through the groupings, if the macrostate is $H(w)$; the unresolved motion inside it is $\sum_i w_i H(p_i)$.}


\endif
