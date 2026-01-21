\ifndef{noBarberPrinciple}
\define{noBarberPrinciple}

\editme

\subsection{The No-Barber Principle}

\notes{In 1901 Bertrand Russell introduced a paradox: if a barber shaves everyone in the village who does not shave themselves, does the barber shave themselves? The paradox arises when a definition quantifies over a totality that includes the defining rule itself.}

\notes{We propose a similar constraint for the inaccessible game: *the foundational rules must not refer to anything outside themselves for adjudication or reference*. We call this the "no-barber principle."}

\slides{
**Russell's Barber Paradox:**

*Barber shaves all who don't shave themselves*

Does the barber shave themselves?

**Paradox:** Definition includes itself in scope
}

\newslide{The Munchkin Provision}

\notes{Without such consistency, we would require what we might call a "Munchkin provision." In the Munchkin card game [@Jackson-munchkin01], it is acknowledged that the cards and rules may be inconsistent. Their resolution? "Any other disputes should be settled by loud arguments, with the owner of the game having the last word."}

\notes{While this works for card games, it's unsatisfying for foundational mathematics. We want our game to be **internally consistent**, not requiring an external referee to resolve paradoxes.}

\slides{
**Munchkin Card Game [@Jackson-munchkin01]:**

*Rules may be inconsistent*

**Resolution:** "Loud arguments, with owner having last word"

**For foundations:** Need something better!

*No external referee for mathematics*
}

\newslide{No External Adjudicators}

\notes{The no-barber principle says that admissible rules must be **internally adjudicable**: they depend only on quantities definable from within the system's internal language, without requiring:
- An external observer to define what's distinguishable
- A pre-specified outcome space or $\sigma$-algebra
- A privileged decomposition into subsystems
- An externally defined time parameter}

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

\notes{The no-barber principle implies a constraint called **entropic exchangeability**: any admissible constraint or selection criterion must:
1. Depend only on reduced subsystem descriptions
2. Be invariant under relabeling of subsystems
3. Not presuppose access to globally distinguishable joint configurations}

\notes{This is not an aesthetic symmetry assumption—it's a **consistency requirement**. It prevents the rules from appealing to distinctions the game itself cannot represent.}

\slides{
**Entropic Exchangeability:**

Admissible rules must:
1. Use only reduced descriptions
2. Be relabeling-invariant
3. Not require global distinguishability

*Consistency, not aesthetics*
}

\subsection{What This Excludes}

\notes{Many seemingly natural constraints violate the no-barber principle:

- **Partial conservation** (only some variables isolated) → privileges those variables
- **Time-varying $C$** → requires external time parameter
- **Observer-relative isolation** → requires external observer
- **Probabilistic isolation** (holds in expectation) → requires external probability space}

\slides{
**Violations of No-Barber:**
* Partial conservation → privileges variables
* Time-varying $C$ → needs external clock
* Observer-relative → needs external observer
* Probabilistic → needs external measure

*All smuggle in external structure*
}

\subsection{What This Selects}

\notes{The no-barber principle, combined with information-theoretic considerations, **selects** rather than assumes:

1. **Marginal entropy conservation** $\sum_i h_i = C$ (strongest constraint without external structure)
2. **Von Neumann entropy** (invariant, doesn't require external outcome labeling)
3. **Maximum entropy production** (internal ordering principle)
4. **Qutrit substrate** ($d_i = 3$ optimizes $\log d_i / d_i$)
5. **Countably infinite system** (avoids arbitrary finite $N$)}

\slides{
**No-Barber Selects:**

1. $\sum h_i = C$ (information isolation)
2. Von Neumann entropy (outcome-independent)
3. Max entropy production (internal ordering)
4. Qutrit substrate ($d=3$ optimal)
5. Countable system (no arbitrary $N$)

*Derived, not assumed*
}

\notes{These are not ad hoc choices—they emerge from requiring internal consistency. The game's structure is determined by what can be formulated without external reference.}

\endif
