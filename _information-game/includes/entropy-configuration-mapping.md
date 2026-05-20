\ifndef{entropyConfigurationMapping}
\define{entropyConfigurationMapping}

\editme

\subsection{Entropy Configuration Mapping}

\figure{\includediagram{\diagramsDir/information-game/configurations-to-entropy-line}{80%}}{Many configurations (density matrices $\rho$) map under von Neumann entropy $S$ to a single real number. Configurations with the same entropy value are isoentropy; they form an equivalence class. The quotient is a totally ordered chain of entropy levels.}{configurations-to-entropy-line}

\notes{Formally, von Neumann entropy first induces a preorder on configurations
$$
\rho \preceq_S \sigma \iff S(\rho) \leq S(\sigma).
$$
Configurations with equal entropy are mutually comparable, so the preorder is not antisymmetric. Quotienting by the induced equivalence relation
$$
\rho \sim_S \sigma \iff S(\rho) = S(\sigma)
$$
produces a poset of entropy levels, which embeds into $(\mathbb{R}_{\geq 0}, \leq)$. This quotient is the formal entropy ladder.}

\notes{We can picture the structure as a ladder: each rung corresponds to an entropy level $S = c$, and multiple configurations sit at the same rung. Moving up the ladder means increasing entropy, more mixed, less structured. Moving down means decreasing entropy, more ordered, more pure.}

\notes{This picture does not require us to know \emph{which} configuration the system is in at any rung, only \emph{how high} the system sits on the ladder. We can think of dynamics in the inaccessible game as being expressed as movement along this ladder.}

\newslide{The Entropy Ladder}

\figure{\includediagram{\diagramsDir/information-game/entropy-ladder}{40%}}{The entropy ladder: each rung is an isoentropy class. Multiple configurations sit at the same rung. Dynamics move the system up the ladder (entropy increase) subject to the marginal entropy conservation constraint.}{entropy-ladder}

\notes{Von Neumann entropy assigns a real value to each configuration, inducing a preorder on the space of density matrices. The quotient by isoentropy equivalence is a totally ordered chain of entropy levels embedded in $(\mathbb{R}_{\geq 0}, \leq)$. The @Parzygnat-functorial22 characterisation establishes that von Neumann entropy is the unique (up to rescaling) continuous, functorial measure of information loss in $\textsf{NCFinProb}$; this is the information-loss functor, which the entropy-level ordering reflects but is distinct from.}

\endif
