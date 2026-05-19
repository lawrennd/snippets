\ifndef{configurationsEntropyOrdering}
\define{configurationsEntropyOrdering}
\editme

\subsection{Configurations Without Visibility}

\notes{The inaccessible game proceeds without an external observer who can read off the state. However, regardless of the current configuration of the system,  we *can* ask: is there a property of the system we can use?}

\notes{The idea is we use the entropy (von Neumann entropy) as a potential which gives us the system flow. This makes it a property of each configuration.}

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



\endif
