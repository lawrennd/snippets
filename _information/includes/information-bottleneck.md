\ifndef{informationBottleneck}
\define{informationBottleneck}

\editme

\subsection{Information Bottleneck}

\notes{The data-processing inequality forbids creating information by processing. It does not say which information to keep. The information bottleneck [@Tishby:bottleneck99] is the prescription: given an observation $X$ and a relevance variable $Y$, choose a representation $T$ of $X$ that keeps $I(T;Y)$ and discards the rest of $I(X;T)$.}

\newslide{Information Bottleneck}

\slides{Least-committal $T$ given a relevance constraint --- MaxEnt, now on mutual information.}

\slidesincremental{
* Markov: $Y \leftrightarrow X \leftrightarrow T$
* Minimise $I(X;T)$ subject to $I(T;Y)\ge R$
* Lagrangian: $I(X;T)-\beta I(T;Y)$
* DPI bound: $I(T;Y)\le I(X;Y)$
}

\speakernotes{$\beta\to 0$ discards everything; $\beta\to\infty$ keeps all of $X$ that is relevant to $Y$. The optimal $p(t\mid x)$ is Boltzmann / exponential family.}

\notes{The information bottleneck of Tishby, Pereira and Bialek is a constrained optimisation on mutual information. The encoder $p(t\mid x)$ is Markov given $X$, so $Y \leftrightarrow X \leftrightarrow T$. Data processing then supplies the bound $I(T;Y)\le I(X;Y)$: no representation of $X$ can be more informative about $Y$ than $X$ itself. The Lagrange multiplier $\beta$ interpolates. Small $\beta$ spends almost no $I$ on the representation. Large $\beta$ keeps everything in $X$ that bears on $Y$. The self-consistent encoder is an exponential family,
$$
p(t\mid x) \propto p(t)\,\exp\bigl(-\beta\,\mathrm{KL}\bigl(p(y\mid x)\,\|\,p(y\mid t)\bigr)\bigr),
$$
the same Boltzmann form that maximum entropy gives, now with a KL divergence in the exponent. We do not run Blahut--Arimoto. The point is the pair: DPI is the no-go; the bottleneck is how you spend $I$.}

\notes{Maximum entropy asks for the least-committal distribution given moment constraints. Here the constraint is a mutual information. It is the same Lagrange move with a different constraint. A system that keeps only what is relevant for action is making an information-bottleneck statement. One reading of the Good Regulator Theorem is bottleneck-shaped: minimise $I(S;A)$ subject to $H(Z)\le\epsilon$. That is an interpretation offered after the theorem, not the theorem itself, whose existence claim $H(A\mid S)=0$ comes from concavity of entropy.}
\addreading{@Tishby:bottleneck99}{the method; optional}

\endif
