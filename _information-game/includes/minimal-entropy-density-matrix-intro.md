\ifndef{minimalEntropyDensityMatrixIntro}
\define{minimalEntropyDensityMatrixIntro}

\editme

\subsection{Variational Derivation of the Initial Curvature Structure}

\notes{We will determine constraints on the Fisher Information Matrix $G(\boldsymbol{\theta})$ that are consistent with the system's unfolding rules and internal information geometry. We follow Jaynes [@Jaynes-information57] in solving a variational problem that captures the allowed structure of the system's origin (minimal entropy) state.}

\notes{This section walks through the derivation of the minimal entropy configuration using Jaynes's free-form variational principle [@Jaynes-information63]. We aim to derive the form of the density matrix or distribution directly from information-theoretic constraints. The goal is also to make the process accessible to those unfamiliar with Jaynes's original maximum entropy formalism.}

\notes{A density matrix has the form
$$
\rho(\boldsymbol{\theta}) = \frac{1}{Z(\boldsymbol{\theta})} \exp\left( \sum_i \theta_i H_i \right)
$$
where $Z(\boldsymbol{\theta}) = \mathrm{tr}\left[\exp\left( \sum_i \theta_i H_i \right)\right]$ and $\boldsymbol{\theta} \in \mathbb{R}^d$, $H_i$ are Hermitian observables. }

\subsection{Historical Context: Entropy and Uncertainty Relations}

\notes{Our approach to minimal entropy configurations builds on several foundational results in information theory and quantum mechanics. These connections help situate our work within the broader context of entropy and uncertainty relations.}

\notes{In 1957, Hirschman [@Hirschman-entropy57] established a fundamental connection between entropy and the Fourier transform, showing that the entropy of a function and its Fourier transform cannot both be arbitrarily small. This result, known as the Hirschman uncertainty principle, was later strengthened by Beckner [@Beckner-fourier75] who derived the optimal constant in the inequality.}

\notes{In 1975, Białynicki-Birula and Mycielski [@Bialynicki-uncertainty75] extended these ideas to quantum mechanics, deriving uncertainty relations for information entropy in wave mechanics. Their work showed that the sum of the entropies of position and momentum distributions is bounded from below, providing an information-theoretic formulation of the Heisenberg uncertainty principle.}

\notes{These results establish that there are fundamental limits to how precisely we can localize a system in both position and momentum space simultaneously, expressed in terms of entropy rather than variance. Our minimal entropy approach can be viewed as an extension of these ideas to more general observables and to the structure of the information geometry itself.}

\notes{The non-commuting observable pair constraint in our framework,
$$
[H_i, H_j] \neq 0,
$$
which leads to the uncertainty relation
$$
\mathrm{Var}(H_i) \cdot \mathrm{Var}(H_j) \geq C > 0,
$$
is conceptually similar to the position-momentum uncertainty relations of Białynicki-Birula and Mycielski, but generalized to arbitrary Hermitian observables. This constraint ensures bounded curvature in our information geometry, which is essential for the emergence of structure from minimal entropy states.}

\endif 