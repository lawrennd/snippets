\ifndef{inaccessibleGameSetUp}
\define{inaccessibleGameSetUp}


\editme

\subsection{The Inaccessible Game Setup}

\slidesincremental{
* Avoid external structure.
* Represent information loss (via Entropy)
* Enforce information conservation (information isolation, @Lawrence-inaccessible25)
}


\notes{Inspired by the no-barber principle, we set up the game in a way that attempts to avoid "external structure". The first two things we need to do this are 
1. A representation of information loss
2. A prohibition of information exchange with the game

How do we obtain a representation of information loss without including external structure? We use the axiomatic frameworks of Baez et al (@Baez-characterisation11) and Parzygnat (@Parzygnat-functorial22). They characterise entropy through category theory frameworks that depend on three axioms. Slight differences in the axioms result in different conclusions. Baez et al conclude that difference in Shannon entropy before and after a process is applied characterises information loss. Parzygnat is inspired by Baez et al but reformulates around a different categorical object which implies von Neumann entropy.}

\notes{In the game [@Lawrence-inaccessible25] we introduce information conservation based on these measures of information loss.}


\endif
