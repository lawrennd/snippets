\ifndef{entropyGroupingComposition}
\define{entropyGroupingComposition}

\editme

\subsection{Grouping Composition}

\slides{Uncertainty splits into stages: which group, then where inside the group.}

\slidesmall{
$$
H(X)=H(w)+\sum_i w_i\, H(p_i)
$$
}

\slidesincremental{
* $w_i$: probability of group $i$
* $p_i$: distribution *inside* group $i$
* First term: cost of the coarse label; second: average residual detail
}

\speakernotes{This is the chain rule for a deterministic grouping $G=g(X)$: $H(X)=H(G)+H(X\mid G)$. Board that identification. Khinchin pointer only --- consistency under staged questions characterises Shannon $H$; no proof today.}

\notes{Partition the outcomes of $X$ into groups labelled by $i$, with group probabilities $w_i$ and within-group distributions $p_i$. Then
\begin{align}
H(X)=H(w)+\sum_i w_i\, H(p_i).
\end{align}
The die examples are the case check: $H(w)$ is the entropy of the coarse question; $\sum_i w_i H(p_i)$ is what remains once the group is known. If $G=g(X)$ is the group label, this identity is exactly the chain rule
\begin{align}
H(X)=H(G)+H(X\mid G),
\end{align}
because $G$ is a function of $X$ (so $H(G\mid X)=0$) and $H(X\mid G)=\sum_i w_i H(p_i)$.}

\newslide{Reverse Direction}

\slides{Learning the face determines the group for free. What is left to find after the group?}

\slidesincremental{
* $H(G\mid X)=0$: the coarse label is redundant given $X$
* Information *extracted* by the group: $I(X;G)=H(G)$
* Information *still to find*: $H(X\mid G)$
}

\notes{In the reverse direction, observing $X$ fixes $G$ with no leftover uncertainty. The mutual information $I(X;G)=H(G)-H(G\mid X)=H(G)$ is exactly the price of the coarse question. After you know the group, the remaining work is $H(X\mid G)$ --- which of the fine outcomes inside that group. Coarse-graining *keeps* $H(G)$ as your description and *discards* $H(X\mid G)$:
\begin{align}
\text{information lost by coarse-graining}
  = H(X\mid G)
  = \sum_i w_i\, H(p_i).
\end{align}}

\newslide{Why the Total Is Invariant}

\slides{Entropy is the uncertainty that is consistent no matter how you decompose a question into stages.}

\slidesincremental{
* Any partition: $H(w)+\sum_i w_i H(p_i)$ returns the same $H(X)$
* That consistency is special to the Shannon form (Khinchin; later Baez--Fritz--Leinster)
* Pointer only today --- week 3 derives $H$ from axioms
}

\notes{The die paid $\log_2 6$ whichever cut came first. That invariance under regrouping is not an accident of base-two logarithms; it is part of what characterises Shannon entropy among candidate uncertainty measures [@Khinchin-information57]. Categorical accounts make the same demand precise [@Baez-entropy11]. For this lecture it is enough that staged questions *add*, so coarse-graining has a well-defined price.}

\endif
