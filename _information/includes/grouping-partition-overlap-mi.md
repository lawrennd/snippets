\ifndef{groupingPartitionOverlapMi}
\define{groupingPartitionOverlapMi}

\editme

\subsection{When Coarse Graining Overlaps}

\slides{Revisit week 4's exclusive case. Soft mixtures leave leftover uncertainty about the label.}

\slidesincremental{
* Exclusive: $G=g(x)$ forced $H(G\mid X)=0$ and $H(X)=H(w)+\sum_g w_g H(p_g)$
* Soft label $G=g(x)$ with joint $p(x,g)$ (several $g$ can share the same $x$)
* Chain rule always: $H(X,G)=H(G)+H(X\mid G)=H(X)+H(G\mid X)$
* Rearrange: $H(X)=H(w)+\sum_g w_g H(p_g)-H(G\mid X)$
}

\speakernotes{Week 4: the log-sum collapsed only because non-overlap forced every face into one cell. Keep $H(G\mid X)$: leftover uncertainty about which component, given the face. That leftover is mutual information next.}

\notes{Week 4 derived
\begin{align}
H(X)=H(w)+\sum_g w_g\, H(p_g)
\end{align}
under the exclusive assumption $G=g(x)$, where $g(x)$ is a funciton that maps each point $x$ to precisely 1 group. This means that we have $H(G\mid X=x)=0$, i.e. if we know $x$ we know $g$. 

What if we consider a soft labelling, such that each point $x$ is mapped to a different group $g$ with some probability?. First we keep the probability of the different groups the same as it was before, with a *soft* label $g\in G$ with joint $p(x,g)$ and prior cell weights $w_g=p(g)$, with $p_g(x)=p(x\mid g)$. We can use the chain rule on the joint to show
\begin{align}
H(X,G)=H(G)+H(X\mid G)=H(X)+H(G\mid X).
\end{align}
Expand $H(X\mid G)=\sum_g w_g H(p_g)$ and the marginal entropy of $G$ just being the marginal entropy of the group's course graining, $H(G)=H(w)$ to obtain
\begin{align}
H(X)=H(w)+\sum_g w_g\, H(p_g)-H(G\mid X).
\end{align}
The new term $H(G\mid X)$ is zero (as before) when the partition is exclusive. I.e. when given $x$ you already know the group it's allocated to. In mixture modelling, for example soft mixtures (like mixture of Gaussians, mixture of experts) leave $H(G\mid X)>0$, meaning that an observation $x$ can be associated with different groups with some probability.}

\newslide{Mutual Information}

\slides{We assess this with mutual information.}

\slidesmall{
$$
I(X;G)=H(G)-H(G\mid X)=H(X)-H(X\mid G)
$$
}

\slidesincremental{
* Exclusive: $H(G\mid X)=0$ $\Rightarrow$ $I(X;G)=H(G)=H(w)$
* Overlap: $0<I(X;G)<H(w)$ (the coarse label is no longer free given $X$)
* Same algebra: $H(X)=H(X\mid G)+I(X;G)$
}

\speakernotes{From the two chain-rule expansions, $I(X;G)=H(G)-H(G\mid X)$. Exclusive case recovers week 4: $I(X;G)=H(G)$. Soft case keeps a positive $H(G\mid X)$. Next: the same $I$ is a KL.}

\notes{Mutual information is the pairwise reading of that leftover term from the chain rule,
\begin{align}
I(X;I)
  = H(G)-H(G\mid X)
  = H(X)-H(X\mid G)
  = H(X)+H(G)-H(X,G).
\end{align}
Substitute into the overlapping identity:
\begin{align}
H(X)
  = H(X\mid G)+I(X;G)
  = \sum_g w_g\, H(p_g)+I(X;G),
\end{align}
and equivalently
\begin{align}
H(X)
  = H(w)+\sum_g w_g\, H(p_g)-H(G\mid X),
\end{align}
because $I(X;G)=H(w)-H(G\mid X)$. Exclusive coarse-graining is the special case where $H(I\mid X)=0$, which means that the mutual information is maximised, $I(X;I)=H(w)$, and the split we saw for the exclusive coarse-graining case in week-4 split is recovered. Overlapping coarse-graining keeps a positive $H(G\mid X)$: given $X$, i.e. even given $X=x$ you are not convident which group, $g$, it's allocated to. The relationship is no longer a function, $g(x)$ it's a stochastic relationship $p(g|x)$. }

\newslide{Mutual information is a KL divergence}

\slides{This $I$ is KL between the joint and the product of marginals.}

\slidesmall{
$$
I(X;G)=\KL{p(x,g)}{p(x)\,p(g)}
$$
}

\slidesincremental{
* Write $I=\sum_{x,g} p(x,g)\log\dfrac{p(x,g)}{p(x)p(g)}$
* Independence: $I=0$; exclusive labelling: $I=H(G)$
* Soft partitions are bookkeeping; MaxEnt still maximises $H$ under constraints
}

\speakernotes{Step (3) of today's KL arc: mutual information *is* a KL. Relative entropy to Jaynes' $m$ is next; then KL properties. Fisher geometry waits for week 6.}

\notes{Writing $I(X;G)=\sum_{x,g} p(x,g)\log\frac{p(x,g)}{p(x)p(g)}$ is a KL-divergence, $\KL{p(x,i)}{p(x)p(i)}$. Independence is when the divergence is zero, so $I=0$. Exclusive deterministic labelling saturates the KL divergence, the joint distribution is as different from the independent as possible (the mapping from $x$ to $g$ is deterministic) and therefore $I=H(G)$. }

\endif
