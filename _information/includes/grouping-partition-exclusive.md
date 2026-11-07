\ifndef{groupingPartitionExclusive}
\define{groupingPartitionExclusive}

\editme

\subsection{Partitions That Do Not Overlap}

\slides{Coarse-grain into groups that do not leak into each other.}

\slidesincremental{
* Face $d$; partition index $i$
* $p(d\mid i)$ is *not* a general conditional (once $i$ is known, the support is restricted)
* Divide so the partitions do not overlap: we do not want things to leak in ways we are not modelling
}

\speakernotes{Here $d$ is the die face and $i$ is the partition: low/high or $1$--$2$ versus $3$--$6$. Outside the active cell the probabilities are zero. Soft mixtures (several $i$ active for one $d$) come next.}

\notes{Write $d$ for the fine outcome (the face of the die) and number the coarse cells by $i$. Inside cell $i$ the conditional $p(d\mid i)$ is not a free distribution on the whole alphabet: once you know the partition, the other faces have probability zero. That is why those conditionals are better read as *weights* on a restricted set. The modelling choice, when we coarse-grain, is to divide the faces into cells that are *not overlapping*. Typically we do not want probability to leak across cells in ways we are not modelling.}

\newslide{Why Non-Overlap Matters}

\slides{The log of a sum is a headache. The log of a product is trivial. Non-overlap lets us use the product.}

\slidesmall{
$$
p(d)=\sum_i p(d\mid i)\,p(i)
$$
}

\slidesincremental{
* Product rule and sum rule give the marginal (that much is ordinary)
* For each face $d$, only *one* $i$ is valid
* The other terms in the sum are zero, so the log-sum collapses
}

\speakernotes{If $d\in\{1,2\}$ then only $i=1$ contributes; if $d\in\{3,4,5,6\}$ then only $i=2$. The partitions are on or off: that is the trick.}

\notes{The marginal is still
\begin{align}
p(d)=\sum_i p(d\mid i)\,p(i).
\end{align}
Entropy of the system is $-\sum_d p(d)\log p(d)$. Substituting the mixture form puts a *sum* inside the logarithm (usually a headache), whereas the log of a product separates. Non-overlap is what licenses the next step. For every face $d$ there is only one valid partition: if $d$ is one or two, only $i=1$ is on; if $d$ is three through six, only $i=2$ is on. Every other term in the sum is zero. Those zeros drop out, the log factors,
\begin{align}
\log\bigl(p(d\mid i)\,p(i)\bigr)
  = \log p(d\mid i)+\log p(i),
\end{align}
and the entropy splits into the entropy of the coarse-graining label plus a weight times the entropy inside each partition (the form $H(w)+\sum_i w_i H(p_i)$). This only works because the partitions are on or off.}

\newslide{Overlapping Components Are a Different Model}

\slides{A mixture of Gaussians (or a mixture of experts) lets components overlap. Then the trick fails.}

\slidesincremental{
* Soft mixture: several $i$ can be active for the same $d$
* The sum inside the log stays a sum
* Coarse-graining as used here is the exclusive case (break the world down, and throw the within-cell uncertainty away)
}

\speakernotes{A mixture of Gaussians or mixture of experts is the overlapping contrast. We do not need EM here. Then back to the die identity.}

\notes{What would normally be called a mixture model (a mixture of Gaussians, or a mixture of experts) lets components *overlap*. Then several $i$ can carry mass for the same $d$, the sum inside the log does not collapse, and you cannot drop terms. The grouping identity we are writing is the exclusive case: partitions on or off. When you break the world down that way you lose information (you throw the within-partition uncertainty away) and then operate at the coarser grade. In the notes' standing notation the face is $X$, the coarse label is $G=g(X)$, the cell weights are $w_i=p(i)$, and $p_i$ is the distribution inside cell $i$; the same objects as $d$ and $i$ above. The overlapping case $H(I\mid X)>0$, and its mutual-information form, wait for week 5.}

\endif
