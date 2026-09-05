\ifndef{informationBottleneck}
\define{informationBottleneck}

\editme

\subsection{Information Bottleneck}

\notes{The data-processing inequality forbids creating information by processing. It does not say which information to keep. The information bottleneck [@Tishby:bottleneck99] is the prescription: given an observation $X$ and a relevance variable $Y$, choose a representation $T$ of $X$ that keeps $I(T;Y)$ and discards the rest of $I(X;T)$.}

\newslides{Information Bottleneck}

\slides{Least-committal $T$ given a relevance constraint --- MaxEnt, now on mutual information.}

\slidesincremental{
* Markov: $Y \leftrightarrow X \leftrightarrow T$
* Minimise $I(X;T)$ subject to $I(T;Y)\ge R$
* Lagrangian: $I(X;T)-\beta I(T;Y)$
* DPI bound: $I(T;Y)\le I(X;Y)$
}

\speakernotes{LO10. $\beta\to 0$ discards everything; $\beta\to\infty$ keeps $T=X$. Optimal $p(t\mid x)$ is Boltzmann / exponential family. Week 8 uses this as a tool, not a new outcome.}

\notes{The information bottleneck of Tishby, Pereira and Bialek is a constrained optimisation on mutual information. The encoder $p(t\mid x)$ is Markov given $X$, so $Y \leftrightarrow X \leftrightarrow T$. Data processing then supplies the bound $I(T;Y)\le I(X;Y)$: no representation of $X$ can be more informative about $Y$ than $X$ itself. The Lagrange multiplier $\beta$ interpolates. Small $\beta$ spends almost no $I$ on the representation. Large $\beta$ recovers $T=X$. The self-consistent encoder is an exponential family,
$$
p(t\mid x) \propto p(t)\,\exp\bigl(-\beta\,\mathrm{KL}\bigl(p(y\mid x)\,\|\,p(y\mid t)\bigr)\bigr),
$$
the same Boltzmann form as week 4, now with a KL sufficient statistic. We do not run Blahut--Arimoto. The point is the pair: DPI is the no-go; the bottleneck is how you spend $I$.}

\notes{Week 4 asked for the least-committal $p$ given moments. Here the constraint is a mutual information. Same Lagrange move, different constraint. Week 8 will use the bottleneck to evaluate intelligence claims: a system that keeps only what is relevant for action is making an IB statement. Requisite variety and the Good Regulator remain named colour; this is a theorem.}

\addreading{@Tishby:bottleneck99}{the method; optional}

\endif
