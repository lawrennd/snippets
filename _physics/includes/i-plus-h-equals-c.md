\ifndef{iPlusHEqualsC}
\define{iPlusHEqualsC}

\editme

\subsection{The $I + H = C$ Structure}

\narration{So here's the key relationship. From $\sum_i h_i = C$, with a little algebra — using the fact that for a joint distribution the joint entropy equals the sum of marginal entropies minus the multi-information — I can show that $I + H = C$.}

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
\narration{So the multi-information $I$ and the joint entropy $H$ sum to a constant. The joint entropy is basically how spread out the distribution is. The multi-information is how correlated the variables are.} 

\newslide{'Information Action'}

\narration{So you have this trade-off: you can have maximum correlation, or maximum entropy, but not both at the same time. The game will be about converting multi-information into entropy.}

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


\notes{This equation has the structure of an action principle in classical mechanics. In physics, total energy is conserved and splits into two parts,
$$
V + T = E,
$$
where $V$ is potential energy and $T$ is kinetic energy.

The analogy for The Inaccessible Game is.

- **Multi-information** $I$ plays the role of *potential energy*. It represents "stored" correlation structure. High $I$ means variables are tightly coupled, like a compressed spring.
- **Joint entropy** $H$ plays the role of *kinetic energy*. It represents "dispersed" or "free" information. High $H$ means the probability distribution is spread out, with maximal uncertainty.

Just as a classical system evolves from high potential energy to high kinetic energy (a ball rolling down a hill), the idea in the Inaccessible Game will be that the information system evolves from high correlation (high $I$) to high entropy (high $H$).}

\narration{Think of it like potential energy and kinetic energy: the correlation is potential energy, the entropy is kinetic energy. In equilibrium you'd have an equal mix. But we start in a highly correlated state — that's what I mean by the origin — and the system evolves to maximize entropy.}

\narration{So now I have the game. I've got $I + H = C$. And I want the dynamics of the system to maximise $H$. But to set up what those dynamics look like, I need to parameterise the configuration space. }


\endif
