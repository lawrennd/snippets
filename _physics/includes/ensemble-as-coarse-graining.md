\ifndef{ensembleAsCoarseGraining}
\define{ensembleAsCoarseGraining}

\editme

\subsection{From Paths to an Ensemble}

\slides{Laplace's gremlin says we cannot follow every curve. The ensemble is how we *live with that*.}

\slidesincremental{
* Microstate: positions and velocities of all particles (Laplace's curves)
* Macrostate: a few numbers --- $N$, $V$, $E$ or $T$, $P$
* Ensemble: a probability over the microstates compatible with the macrostate
}

\speakernotes{Name coarse-graining without measure theory. Link: billiard histogram bins are a toy coarse-graining; $T,V,P$ are the physicist's. Gibbs distribution later today is one ensemble (canonical). Do not derive MaxEnt.}

\notes{Laplace's demon would integrate every molecular trajectory. Laplace's gremlin says we lack the information and the compute. Statistical mechanics answers by changing the object of study. A *microstate* is a point in the high-dimensional space of all positions and momenta --- the collection of curves. A *macrostate* is what we can actually hold fixed or measure: particle number, volume, energy, or temperature and pressure. An *ensemble* is a probability distribution over microstates consistent with that macrostate. We replace ignorance of the path with a measure on the set of paths. That replacement *is* a coarse-graining: many micro-histories are declared equivalent for the purpose of prediction.}

\newslide{Coarse-Graining Is a Choice of Description}

\slides{Temperature and pressure are sufficient statistics of the swarm --- not decorations on the truth.}

\slidesincremental{
* Histogram bins: keep some velocity detail, discard the rest
* Thermodynamics: keep $T$, $V$, $P$; discard which molecule was which
* The uncertainty we write as entropy lives at the chosen grain
}

\notes{The billiard canvas already coarse-grains: it reports a velocity-bin Shannon entropy, not the full thermodynamic entropy of the gas. Maxwell, Boltzmann and Gibbs elevate the same move. Once the macroscopic constraints are fixed, the remaining uncertainty over microstates is what their $S$ counts. The fight over atoms was partly a fight over whether that microscopic sample space was real. The mathematical move --- probability over an ensemble --- survives either reading, and it is the move this course will keep using when energy becomes a score and $p_i\propto e^{-\beta E_i}$ becomes an occupation.}

\newslide{Bridge to Maxwell, Boltzmann, Gibbs}

\slides{They turn Bernoulli's swarm and Laplace's ignorance into a calculus.}

\slidesincremental{
* Maxwell: velocity statistics of the ideal gas
* Boltzmann: $S$ linked to probability over microstates
* Gibbs: ensembles as the systematic language
}

\notes{What follows in this lecture is not a new ontology so much as the bookkeeping that makes the ensemble usable: Gibbs--Boltzmann occupation, free energy $F=U-TS$, and the bath that justifies fixing $T$. The molecular hypothesis will win historically; the course needs the *abstraction* today.}

\endif
