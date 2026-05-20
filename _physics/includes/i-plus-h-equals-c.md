\ifndef{iPlusHEqualsC}
\define{iPlusHEqualsC}

\editme

\subsection{The $I + H = C$ Structure}

\notes{We have established four axioms, with the fourth axiom stating that the sum of marginal entropies is conserved,
$$
\sum_{i=1}^N h_i = C.
$$
This conservation law is the heart of The Inaccessible Game, but to understand its dynamical implications, we need to rewrite it in a more revealing form.}

\slides{
$$
\sum_{i=1}^N h_i = C
$$

*What does this conservation imply for dynamics?*
}

\subsection{Multi-Information: Measuring Correlation}

\notes{The **multi-information** (or **total correlation**), introduced by @Watanabe-multiinformation60, measures how much the variables in a system are correlated. It is defined as,
$$
I = \sum_{i=1}^N h_i - H,
$$
where $H$ is the **joint entropy** of the full system:
$$
H = -\sum_{\mathbf{x}} p(\mathbf{x}) \log p(\mathbf{x}).
$$

The multi-information has a nice interpretation:

- **$I = 0$**: The variables are completely independent. The joint entropy equals the sum of marginal entropies.
- **$I > 0$**: The variables are correlated. Some information is "shared" between variables, so the joint entropy is less than the sum of marginals.
- **$I$ is maximal**: The variables are maximally correlated (in the extreme case, deterministically related).

Multi-information is always non-negative ($I \geq 0$) and measures how much knowing one variable tells you about others.}

\slides{
$$
I = \sum_{i=1}^N h_i - H
$$
}

\newslide{'Information Action'}

\notes{Using the definition of multi-information, we can rewrite our conservation law. From $I = \sum_{i=1}^N h_i - H$, we have:
$$
\sum_{i=1}^N h_i = I + H.
$$
Therefore, the fourth axiom $\sum_{i=1}^N h_i = C$ becomes:
$$
I + H = C.
$$

This is an *information action principle*. It says that multi-information plus joint entropy is conserved. This equation sits behind the dynamics of the Inaccessible Game.}

\slides{
$$
I + H = C
$$

*Conserved quantity splits into two parts*
}

\newslide{Analogy to classical mechanics}

\slidesincremental{
* Energy: $V + T = E$
* Information: $I + H = C$
* System "rolls downhill" from correlation to disorder
}

\newslide{Physical Analogy}

\notes{This equation has the structure of an action principle in classical mechanics. In physics, total energy is conserved and splits into two parts,
$$
V + T = E,
$$
where $V$ is potential energy and $T$ is kinetic energy.

The analogy for The Inaccessible Game is.

- **Multi-information** $I$ plays the role of *potential energy*. It represents "stored" correlation structure. High $I$ means variables are tightly coupled, like a compressed spring.
- **Joint entropy** $H$ plays the role of *kinetic energy*. It represents "dispersed" or "free" information. High $H$ means the probability distribution is spread out, with maximal uncertainty.

Just as a classical system evolves from high potential energy to high kinetic energy (a ball rolling down a hill), the idea in the Inaccessible Game will be that the information system evolves from high correlation (high $I$) to high entropy (high $H$).}

\endif
