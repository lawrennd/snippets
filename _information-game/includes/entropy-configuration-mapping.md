\ifndef{entropyConfigurationMapping}
\define{entropyConfigurationMapping}

\editme

\subsection{Entropy Configuration Mapping}

\figure{\includediagram{\diagramsDir/information-game/configurations-to-entropy-line}{80%}}{Many configurations (density matrices $\rho$) map under von Neumann entropy $S$ to a single real number. Configurations with the same entropy value are isoentropy; they form an equivalence class. The quotient is a totally ordered chain of entropy levels.}{configurations-to-entropy-line}

\newslide{The Entropy Ladder}

\notes{We can picture the structure as a ladder: each rung corresponds to an entropy level $S = c$, and multiple configurations sit at the same rung. Moving up the ladder means increasing entropy, more mixed, less structured. Moving down means decreasing entropy, more ordered, more pure. The bottom rung $S = 0$ corresponds to a pure state.}

\notes{This picture does not require us to know \emph{which} configuration the system is in at any rung, only \emph{how high} the system sits on the ladder. We can think of dynamics in the inaccessible game as being expressed as movement along this ladder.}

\slidesincremental{
* Bottom ($S=0$): pure state — fully ordered, single configuration
* Higher rungs: mixed states — more equivalence classes at each level
* No canonical top: maximum entropy grows with system dimension
* Dynamics = movement along the ladder
* Functor: $S : \textsf{NCFinProb} \to (\mathbb{R}_{\geq 0}, \leq)$
}

\newslide{The Entropy Ladder}

\figure{\includediagram{\diagramsDir/information-game/entropy-ladder}{40%}}{The entropy ladder: each rung is an isoentropy class. Multiple configurations sit at the same rung. Dynamics move the system up the ladder (entropy increase) subject to the marginal entropy conservation constraint.}{entropy-ladder}

\notes{The functor $S: \textsf{NCFinProb} \to (\mathbb{R}_{\geq 0}, \leq)$ that assigns von Neumann entropy to each configuration is the formal expression of this structure. It maps the category of configurations to the poset of non-negative reals, and it is the unique (up to rescaling) continuous, functorial measure of information loss in $\textsf{NCFinProb}$ [@Parzygnat-functorial22].}

\endif
