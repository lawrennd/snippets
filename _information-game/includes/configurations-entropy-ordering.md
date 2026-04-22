\ifndef{configurationsEntropyOrdering}
\define{configurationsEntropyOrdering}
\editme

\subsection{Configurations Without Visibility}

\notes{The inaccessible game proceeds without an external observer who can read off the state. However, regardless of the current configuration of the system,  we *can* ask: is there a property of the system we can use?}

The idea is we use the entropy (von Neumann entropy) as a potential which gives us the system flow. This makes it a property of each configuration.}

\slidesincremental{
* Cannot inspect the configuration, $\rho$,  directly
* But *entropy* requires no external reference
* Internally accessible: no external adjudicator needed
}

\subsection{Entropy Orders the Configurations}

\notes{Entropy assigns a non-negative real number to every configuration. This gives us a map
$$
S : \{\text{configurations}\} \longrightarrow [0, \infty),
$$
and we can pull back the standard order on $\mathbb{R}$ to get an ordering on configurations:
$$
\rho \leq \rho' \quad \Longleftrightarrow \quad S(\rho) \leq S(\rho').
$$
This relation is reflexive ($\rho \leq \rho$) and transitive (if $\rho \leq \rho'$ and $\rho' \leq \rho''$ then $\rho \leq \rho''$). It is \emph{not} antisymmetric in general: two distinct density matrices $\rho \neq \rho'$ can share the same entropy value $S(\rho) = S(\rho')$. A relation that is reflexive and transitive but not necessarily antisymmetric is called a \emph{preorder}, and a set equipped with a preorder is called a \emph{proset} (preordered set).

So the configurations of the inaccessible game form a natural proset under von Neumann entropy.}

\slidesincremental{
* $S$ maps each configuration to $[0, \infty)$
* Pull back the order on $\mathbb{R}$: $\rho \leq \rho'$ iff $S(\rho) \leq S(\rho')$
* Reflexive ✓, Transitive ✓, Antisymmetric ✗ (distinct $\rho$ can share entropy)
* **Preorder** (not a partial order): configurations form a **proset**
}

\newslide{Isoentropy and the Quotient Poset}

\notes{Within the proset, the configurations that share an entropy value form equivalence classes: $\rho \sim \rho'$ iff $S(\rho) = S(\rho')$. Each equivalence class is an \emph{isoentropy surface}, i.e. a manifold of configurations all carrying the same entropic content.}

\notes{If we pass to the quotient, i.e. treat isoentropy configurations as a single object, the resulting collection of equivalence classes $[\rho]$ is antisymmetric: $[\rho] \leq [\rho']$ and $[\rho'] \leq [\rho]$ together imply $[\rho] = [\rho']$. This quotient is a \emph{partially ordered set} (poset). Because because $S$ maps into $\mathbb{R}$, which is totally ordered, the quotient poset is a \emph{chain}: every two equivalence classes are comparable.}

\notes{Even without seeing inside the system we can hypothesise that the chain of entropy levels is defined.}

\slidesincremental{
* Isoentropy: $\rho \sim \rho'$ iff $S(\rho) = S(\rho')$ — an equivalence class
* Quotient $[\rho]$: each class is one point $\to$ antisymmetry holds $\to$ *poset*
* Since $S$ maps into $\mathbb{R}$: every two classes are comparable $\to$ *chain* (total order)
* From outside: only the chain of entropy levels is visible
}

\figure{\includediagram{\diagramsDir/information-game/configurations-to-entropy-line}{80%}}{Many configurations (density matrices $\rho$) map under von Neumann entropy $S$ to a single real number. Configurations with the same entropy value are isoentropy; they form an equivalence class. The quotient is a totally ordered chain of entropy levels.}{configurations-to-entropy-line}

\newslide{The Entropy Ladder}

\notes{We can picture the structure as a ladder: each rung corresponds to an entropy level $S = c$, and multiple configurations sit at the same rung. Moving up the ladder means increasing entropy, more mixed, less structured. Moving down means decreasing entropy, more ordered, more pure. The bottom rung $S = 0$ corresponds to a pure state.}

\notes{This picture does not require us to know \emph{which} configuration the system is in at any rung, only \emph{how high} the system sits on the ladder. We can think of dynamics in the inaccessible game as being expressed as movement along this ladder.}


\figure{\includediagram{\diagramsDir/information-game/entropy-ladder}{40%}}{The entropy ladder: each rung is an isoentropy class. Multiple configurations sit at the same rung. Dynamics move the system up the ladder (entropy increase) subject to the marginal entropy conservation constraint.}{entropy-ladder}


\notes{The functor $S: \textsf{NCFinProb} \to (\mathbb{R}_{\geq 0}, \leq)$ that assigns von Neumann entropy to each configuration is the formal expression of this structure. It maps the category of configurations to the poset of non-negative reals, and it is the unique (up to rescaling) continuous, functorial measure of information loss in $\textsf{NCFinProb}$ [@Parzygnat-functorial22].}

\slidesincremental{
* Bottom ($S=0$): pure state — fully ordered, single configuration
* Higher rungs: mixed states — more equivalence classes at each level
* No canonical top: maximum entropy grows with system dimension
* Dynamics = movement along the ladder
* Functor: $S : \textsf{NCFinProb} \to (\mathbb{R}_{\geq 0}, \leq)$
}

\endif
