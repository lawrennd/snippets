\ifndef{informationIsolation}
\define{informationIsolation}

\editme

\subsection{Information Isolation}

\notes{The first three axioms of the inaccessible game, due to \citet{Baez-characterisation11}, characterise information loss and justify the use of entropy. For the game itself we introduce a fourth axiom: *information isolation*. Just as an isolated chamber conserves mass and energy, our game is isolated from external observation. No observer outside the system can extract or inject information.}

\slides{
**The Fourth Axiom: Information Isolation**

* First three axioms: information loss (Baez-Fritz-Leinster)
* Fourth axiom: the game is *isolated from observation*
* No external observer can extract or inject information

*Analogous to energy conservation in thermodynamics*
}

\newslide{Conservation of Marginal Entropy}

\notes{Under additional requirements of exchangeability and extensivity, information isolation implies that the total marginal entropy is conserved. For any finite sub-group of $N$ variables the sum of marginal entropies $\{h_i\}_{i=1}^{N}$ sums to a constant $C$,
$$
\sum_{i=1}^N h_i = C.
$$
The conservation law is imposed in an exchangeable form across the *marginal* entropies, so that it applies consistently to any finite partition drawn from a potentially countably infinite collection of variables.}

\slides{
**Marginal Entropy Conservation:**
$$
\sum_{i=1}^N h_i = C
$$

* Exchangeable: holds for any finite subset of variables
* Extensive: scales linearly with system size
* Analogous to energy conservation — but for information
}

\newslide{Why This Form?}

\notes{The specific form $\sum_i h_i = C$ is not an arbitrary choice. Any exchangeable quantity depending only on marginal entropies must take the form $Q = \sum_i f(h_i)$ with the same function $f$ for each variable. Extensivity (adding one variable increases $Q$ by a fixed amount) forces $f(h) = c \cdot h + \text{const}$. Requiring the law to apply consistently as the subset size varies eliminates the constant term. Setting $c=1$ gives the unique form $\sum_i h_i = \text{const}$. The fourth axiom is therefore the unique exchangeable, extensive, information-theoretic conservation law for an isolated system.}

\slides{
**Uniqueness of the Form:**

Any exchangeable, extensive conservation law over marginal entropies must be:
$$Q(\{h_i\}) = \sum_i f(h_i), \quad f(h) = c \cdot h$$

$\Rightarrow$ unique form: $\sum_i h_i = C$
}

\newslide{Coordinate-Free Interpretation}

\notes{Information isolation is stronger than frame invariance. It eliminates not only preferred reference frames but any appeal to external reference structures. All physically meaningful quantities must be internal to the system and relational rather than absolute. The variable partition $\{X_i\}$ that enters the conservation constraint is a structural choice—part of the model specification, analogous to choosing a Hilbert space factorisation in quantum mechanics—rather than an externally privileged decomposition.

In traditional thermodynamics, energy conservation defines a built-in potential. Here, marginal entropy conservation plays the analogous role: it defines an intrinsic potential within the information geometry. The curvature of this potential, encoded in the Fisher information, acts as the metric governing how the system redistributes its informational content.}

\slides{
**Information Isolation:**

* Enforces *internality*: no external reference structures
* Enforces *relationality*: all quantities defined internally
* Variable partition $\{X_i\}$ is model specification, not external imposition

*Marginal entropy conservation = information geometry's built-in potential*
}

\endif
