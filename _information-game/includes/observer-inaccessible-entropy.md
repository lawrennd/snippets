\ifndef{observerInaccessibleEntropy}
\define{observerInaccessibleEntropy}
\editme

\subsection{The Classical Observer - Inaccessible}

\figure{\includediagramclass{\diagramsDir/physics/observer-composite-inaccessible}{90%}}{Here the observer is blocked from monitoring anything inside the sytem.}{observer-composite-inaccessible}

\notes{When we don't know what's going on inside, we can't express *outcomes* in the way we could with an observer. But we can still express entropies. This highlights an interesting characteristic of entropies. If we don't express the probability directly, but just work with the entropies themselves, it feels like we can assess the bounds of possibility without directly expressing what's going on.}

\subsection{Entropy and Impossibility}

\notes{While we don't see the underlying probability, we can capture a class of different distirbutions by considering the mapping to the system entropy. 

Think of entropy as a scoring system: every probability distribution gets a number measuring its uncertainty. Once you have that, you can line them up from least to most uncertain — which gives you a natural ordering.[^entropy-category]

[^entropy-category]: More formally entropy defines a functor from the category of finite probability spaces to the poset category $(\Re, \leq)$, assigning to each object its Shannon entropy.
}

\slidesincremental{* We don't see see the outcome space
* But we summarise it using entropy
* Entropy gives a single number measuring uncertainty
}

\newslide{Entropy and Impossibility}

\slidesincremental{
* Each distribution gets a score $\rightarrow$ compare them
* Induces ordering from low to high uncertainty
* Formally: a functor from FinProb to $(\Re, \leq)$
}
\notes{We denote marginal entropy of the $i$th variable by $h_i$. We denote the joint entropy of the entire system by $H$.}

\newslide{Marginal and Joint}

\slidesincremental{
* Marginal entropy of variable $i$: $h_i$
* Joint entropy of system: $H$
* Multiinformation $I = \sum_i h_i - H$
}

\endif
