\ifndef{inaccessibleGameSetUp}
\define{inaccessibleGameSetUp}


\editme

\subsection{The Inaccessible Game Setup}

\slides{
* Avoid external structure.
* Represent information loss
* Enforce information conservation
}


\notes{Inspired by the no-barber principle, we set up the game in a way that attempts to avoid "external structure". The first two things we need to do this are 

1. A representation of information loss
2. A prohibition of information exchange with the game

How do we obtain a representation of information loss without including external structure? We use the axiomatic frameworks of Baez et al (@Baez-characterisation11) and Parzygnat (@Parzygnat-functorial22). They characterise entropy through category theory frameworks that depend on three axioms. Slight differences in the axioms result in different conclusions. Baez et al conclude that difference in Shannon entropy before and after a process is applied characterises information loss. Parzygnat is inspired by Baez et al but reformulates around a different categorical object which implies von Neumann entropy.}

\notes{In the game (@Lawrence-inaccessible25) we introduce information conservation based on these measures of information loss.}

\notes{One caveat deserves emphasis: the choice of how to partition the system into subsystems $\{X_i\}$ is itself a form of model specification — it is not derived from within the game. The no-barber principle then applies to all structure *given* this partition; it does not eliminate the partition itself. This boundary between what counts as "game internals" and what counts as "model specification" is an important limitation throughout, and should be borne in mind whenever the argument claims to avoid external structure.}

\slides{
* Partition of system into subsystems $\{X_i\}$: model specification (not derived internally)
* No-barber principle applies *within* this choice — the partition is an irreducible input
}

\endif
