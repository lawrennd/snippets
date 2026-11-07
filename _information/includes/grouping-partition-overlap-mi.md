\ifndef{groupingPartitionOverlapMi}
\define{groupingPartitionOverlapMi}

\editme

\subsection{When Coarse Graining Overlaps}

\slides{Exclusive partitions gave $H(G\mid X)=0$. Soft mixtures leave a remainder.}

\slidesincremental{
* Soft label $I$ with joint $p(x,i)$ --- several $i$ can share the same $x$
* Chain rule always: $H(X,I)=H(I)+H(X\mid I)=H(X)+H(I\mid X)$
* Rearrange: $H(X)=H(w)+\sum_i w_i H(p_i)-H(I\mid X)$
}

\speakernotes{Callback to week 4: the log-sum collapsed only because non-overlap forced every face into one cell. Board the general identity first; name $H(I\mid X)$ as the leftover ``which component?'' given the face. Then define $I(X;I)$.}

\notes{Week 4 derived
\begin{align}
H(X)=H(w)+\sum_i w_i\, H(p_i)
\end{align}
under the exclusive assumption $G=g(X)$, which forces $H(G\mid X)=0$. Keep a soft label $I$ with joint $p(x,i)$ and cell weights $w_i=p(i)$, $p_i(x)=p(x\mid i)$. The chain rule on the joint always holds,
\begin{align}
H(X,I)=H(I)+H(X\mid I)=H(X)+H(I\mid X).
\end{align}
Expand $H(X\mid I)=\sum_i w_i H(p_i)$ and $H(I)=H(w)$ to obtain
\begin{align}
H(X)=H(w)+\sum_i w_i\, H(p_i)-H(I\mid X).
\end{align}
The new term $H(I\mid X)$ is zero precisely when the partition is exclusive: given the face, you already know the cell. Soft mixtures (mixture of Gaussians, mixture of experts) leave $H(I\mid X)>0$ --- several components can still explain the same observation.}

\newslide{Mutual Information Separates the Remainder}

\slides{Mutual information is the leftover correlation between face and soft label.}

\slidesmall{
$$
I(X;I)=H(I)-H(I\mid X)=H(X)-H(X\mid I)
$$
}

\slidesincremental{
* Exclusive: $H(I\mid X)=0$ $\Rightarrow$ $I(X;I)=H(I)=H(w)$
* Overlap: $0<I(X;I)<H(w)$ --- the coarse label is no longer free given $X$
* Same algebra: $H(X)=H(X\mid I)+I(X;I)$
}

\speakernotes{Define $I$ from the two chain-rule expansions. Exclusive case recovers week 4: $I(X;G)=H(G)$. Soft case keeps a positive $H(I\mid X)$ so the grouping identity loses that term. Do not prove DPI today.}

\notes{Mutual information is the pairwise case of the chain-rule remainder,
\begin{align}
I(X;I)
  = H(I)-H(I\mid X)
  = H(X)-H(X\mid I)
  = H(X)+H(I)-H(X,I).
\end{align}
Substitute into the overlapping identity:
\begin{align}
H(X)
  = H(X\mid I)+I(X;I)
  = \sum_i w_i\, H(p_i)+I(X;I),
\end{align}
and equivalently
\begin{align}
H(X)
  = H(w)+\sum_i w_i\, H(p_i)-H(I\mid X),
\end{align}
because $I(X;I)=H(w)-H(I\mid X)$. Exclusive coarse-graining is the special case $H(I\mid X)=0$, so $I(X;I)=H(w)$ and the week-4 split returns. Overlapping coarse-graining keeps a positive $H(I\mid X)$: given $X$, you still do not know which component was responsible. That is why the log-sum refused to collapse on the board in week 4.}

\newslide{KL Reading (Named)}

\slides{The same $I$ is an expected KL between the joint and the product of marginals.}

\slidesmall{
$$
I(X;I)=\KL{p(x,i)}{p(x)\,p(i)}
$$
}

\speakernotes{Name the KL form so week 6's geometry has somewhere to land. Do not expand Fisher here. MaxEnt today still maximises $H$ under constraints; this slide is the soft-partition callback, not a second MaxEnt proof.}

\notes{Writing $I(X;I)=\sum_{x,i} p(x,i)\log\frac{p(x,i)}{p(x)p(i)}$ is exactly $\KL{p(x,i)}{p(x)p(i)}$. Independence is $I=0$; exclusive deterministic labelling saturates $I=H(I)$. The MaxEnt lecture elsewhere in this week still maximises Shannon $H$ under moment constraints; the overlapping identity is the bookkeeping for soft coarse-graining, not a rival prescription.}

\endif
