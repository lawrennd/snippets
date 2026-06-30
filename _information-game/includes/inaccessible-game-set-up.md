\ifndef{inaccessibleGameSetUp}
\define{inaccessibleGameSetUp}


\editme

\subsection{The Inaccessible Game Setup}

\narration{So what does the no-barber principle help us with? If I want to avoid external structure, and I now have a mechanism for representing information loss, what I want to do is enforce information conservation. If we have defined a form of information loss, it feels like we can now isolate the game from observation or interaction — we can say that no external observer can extract or inject information. The aim is to build a game in the following way: a representation of information loss and a prohibition of information exchange with the game. I'm certainly not doing this perfectly, but that's the sort of thing I'm aiming for. It's like a selection principle for the mathematics I want to use in the game.}

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


\endif
