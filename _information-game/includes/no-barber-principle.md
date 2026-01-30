\ifndef{noBarberPrinciple}
\define{noBarberPrinciple}

\editme

\subsection{The No-Barber Principle}

\notes{In 1901 Bertrand Russell introduced a paradox: if a barber shaves everyone in the village who does not shave themselves, does the barber shave themselves? The paradox arises when a definition quantifies over a totality that includes the defining rule itself.}

\notes{We propose a similar constraint for the inaccessible game: *the foundational rules must not refer to anything outside themselves for adjudication or reference*. Or in other words there can be no *external structure*. We call this the "no-barber principle."}

\slides{
**Russell's Barber Paradox:**

*Barber shaves all who don't shave themselves*

Does the barber shave themselves?

**Paradox:** Definition includes itself in scope
}

\newslide{The Munchkin Provision}

\notes{Without such consistency, we would require what we might call a "Munchkin provision." In the Munchkin card game [@Jackson-munchkin01], it is acknowledged that the cards and rules may be inconsistent. Their resolution? 

> Any other disputes should be settled by loud arguments, with the owner of the game having the last word.
>
> Munckin Rules [@Jackson-munchkin01]}

\notes{While this works for card games, it's unsatisfying for foundational mathematics. We want our game to be *internally consistent*, not requiring an external referee to resolve paradoxes.}

\figure{\includejpg{\slidesDiagrams/information-game/Munchkin_game_cover}{40%}}{The Munchkin card came has both cards and rules. The game explicitly acknowledges that this can lead to inconsistencies which should be resolved by the game owner.}{munchkin-game-cover}

\slides{
**Munchkin Card Game [@Jackson-munchkin01]:**

*Rules may be inconsistent*

**Resolution:** "Loud arguments, with owner having last word"

**For foundations:** Need something better!

*No external referee for mathematics*
}

\newslide{No External Adjudicators}

\notes{The no-barber principle says that admissible rules must be *internally adjudicable*: they depend only on quantities definable from within the system's internal language, without requiring e.g. an external observer to define what's distinguishable, or a pre-specified outcome space or $\sigma$-algebra, a privileged decomposition into subsystems an externally defined time parameter or spatial coordinates.}

\slides{
**No-Barber Principle:**

Rules must be *internally adjudicable*

**Forbidden:**
* External observer
* Pre-specified outcome space
* Privileged decomposition
* External time parameter

*No appeal to structure outside the game*
}

\subsection{Entropic Exchangeability}

\notes{The no-barber principle leads to what we call *entropic exchangeability*: any admissible constraint or selection criterion must depend only on reduced subsystem descriptions, be invariant under relabeling of subsystems, and not presuppose access to globally distinguishable joint configurations.}

\notes{This is an attempt to introduce a consistency requirement that prevents the rules from appealing to distinctions the game itself cannot represent.}

\slides{
**Entropic Exchangeability:**

Admissible rules must:
1. Use only reduced descriptions
2. Be relabeling-invariant
3. Not require global distinguishability
}

\subsection{What This Excludes}

\notes{Many seemingly natural constraints violate the no-barber principle. For example, partial conservation which assumes only some variables are isolated, privileges those variables. A time varying $C$ would require an external time parameter. The notion of observer relative isolation would require an observer that cannot be defined externally. Probabilistic isolation also requires an externally defined probabilistic space.}

\slides{
**Violations of No-Barber:**
* Partial conservation (some variables isolated) → privileges variables
* Time-varying $C$ → needs external clock
* Observer-relative isolation → needs external observer
* Probabilistic isolation → needs external measure

*All smuggle in external structure*
}


\endif
