\ifndef{informationIsolation}
\define{informationIsolation}

\editme

\subsection{Information Isolation}

\narration{The constraint I use is this: I don't know what the variables in this game are, because I can't look inside the game. But I use $h_i$ for what I'm calling an atomic marginal entropy — the marginal entropy of each subsystem.}

\notes{The first three axioms of the inaccessible game, due to @Baez-characterisation11, characterise information loss and justify the use of entropy. For the game itself we introduce a fourth axiom: *information isolation*. Just as an isolated chamber conserves mass and energy, our game is isolated from external observation. No observer outside the system can extract or inject information.}

\slides{
* Define information loss
* Isolate game from observation/interaction
* No external observer can extract or inject information
}

\newslide{Marginal Entropy Conservation}

\narration{And then the claim is that the sum of those marginal entropies is conserved. I haven't seen this type of constraint before. And I sort of pause there — everything falls from that. If it's flawed in some way, everything else I've done collapses, but don't let that make you shy about criticising it.}

\notes{Under additional requirements of exchangeability and extensivity, information isolation implies that the total marginal entropy is conserved. For any finite sub-group of $N$ variables the sum of marginal entropies $\{h_i\}_{i=1}^{N}$ sums to a constant $C$,
$$
\sum_{i=1}^N h_i = C.
$$
The conservation law is imposed in an exchangeable form across the *marginal* entropies, so that it applies consistently to any finite partition drawn from a potentially countably infinite collection of variables.}

\slidesincremental{
$$
\sum_{i=1}^N h_i = C
$$

* Isolation: *cf* energy conservation — but for information
}

\notes{The specific form $\sum_i h_i = C$ is not an arbitrary choice. Any exchangeable quantity depending only on marginal entropies must take the form $Q = \sum_i f(h_i)$ with the same function $f$ for each variable. Extensivity (adding one variable increases $Q$ by a fixed amount) forces $f(h) = c \cdot h + \text{const}$. Requiring the law to apply consistently as the subset size varies eliminates the constant term. Setting $c=1$ gives the unique form $\sum_i h_i = \text{const}$. The fourth axiom is therefore the unique exchangeable, extensive, information-theoretic conservation law for an isolated system.}

\notes{Information isolation can be seen as stronger than frame invariance. It eliminates not only preferred reference frames but appeal to external reference structures. All physically meaningful quantities must be internal to the system and relational rather than absolute. The variable partition $\{X_i\}$ that enters the conservation constraint is a structural choice. It is part of the model specification, analogous to choosing a Hilbert space factorisation in quantum mechanics—rather than an externally privileged decomposition.

In traditional thermodynamics, energy conservation defines a built-in potential. Here, marginal entropy conservation plays the analogous role: it defines an intrinsic potential within the information geometry. The curvature of this potential, encoded in the Fisher information, acts as the metric governing how the system redistributes its informational content.}



\narration{The reason I want it to be this atomic form is a notion of exchangeability amongst the game's variables. If I start talking about interactions, I think there's a danger of breaking that. It's also an extensive property — it feels like the type of property where in the future I could take it to infinity and do something non-parametric. I haven't done that, but I'm not ruling it out. And I don't know what the underlying dimension is — that would be an external thing. The aim is to isolate the system, which will prevent barbers from intervening.}

\narration{So why was I looking for something like this? Well, in these kinds of systems, if you look at how effective rules emerge in things like physics, energy conservation tends to be a thing. There has to be something conserved — some constraint. }

\endif
