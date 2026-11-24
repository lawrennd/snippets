\ifndef{dataProcessingInequality}
\define{dataProcessingInequality}

\editme

\subsection{Data-Processing Inequality}

\newslide{Data-Processing Inequality}

\slides{If $X\to Y\to Z$ is a Markov chain, processing $Y$ cannot create information about $X$.}

\slidesincremental{
* Markov: $p(z\mid x,y)=p(z\mid y)$, equivalently $I(X;Z\mid Y)=0$
* $I(X;Y,Z)=I(X;Y)+I(X;Z\mid Y)=I(X;Y)$
* $I(X;Y,Z)=I(X;Z)+I(X;Y\mid Z)\ge I(X;Z)$
* Therefore $I(X;Z)\le I(X;Y)$
}

\speakernotes{Board the two expansions of $I(X;Y,Z)$. Moral: you cannot process your way to more $I$.}

\notes{The data-processing inequality [@Cover:elements91, Thm 2.8.1] says that if $Z$ is computed from $Y$ alone, possibly with fresh randomness, then $Z$ cannot know more about $X$ than $Y$ did. Formally, if $X\to Y\to Z$ is Markov, then $I(X;Z)\le I(X;Y)$.

The proof expands $I(X;Y,Z)$ by the chain rule in two orders. Taking $Y$ first gives $I(X;Y)+I(X;Z\mid Y)$, and the second term is zero because, once $Y$ is known, $Z$ carries nothing further about $X$. Taking $Z$ first gives $I(X;Z)+I(X;Y\mid Z)$, which is at least $I(X;Z)$ because conditional mutual information is never negative. Equating the two gives the inequality.

Equality holds when $I(X;Y\mid Z)=0$: once you know $Z$, $Y$ tells you nothing more about $X$. Then $Z$ is a *sufficient statistic* of $Y$ for $X$; the processing has thrown away only what was irrelevant to $X$. An invertible $Z=f(Y)$ is always sufficient.}

\notes{A claim that a system will "just process more" and so recover information that an earlier stage has already discarded is a claim that violates the data-processing inequality. Processing can rearrange information, make it easier to use, or throw it away. It cannot make more of it.}

\newslide{Data Processing for Distributions}

\slides{Pass two distributions through the same channel: they cannot get further apart.}

\slidesincremental{
* Channel $K(y\mid x)$; outputs $pK$ and $qK$
* $\KL{pK}{qK}\le\KL{p}{q}$
* Equality when $K$ is invertible (one-to-one)
* Strict when $K$ merges states whose ratio $p(x)/q(x)$ differs
}

\notes{The same inequality has a form for distributions. Let $K(y\mid x)$ be any channel, and push two input distributions $p$ and $q$ through it to get $pK$ and $qK$. Then
$$
\KL{pK}{qK}\le\KL{p}{q}.
$$
The proof is the chain rule again, now for KL divergence. Write the joint distributions $p(x)K(y\mid x)$ and $q(x)K(y\mid x)$. Their KL divergence equals $\KL{p}{q}$ (the channel parts cancel), and it also equals $\KL{pK}{qK}$ plus the average divergence between the two posteriors $p(x\mid y)$ and $q(x\mid y)$, which is never negative. Read as statistics: no processing of the data can make two hypotheses easier to tell apart. If $K$ is a one-to-one relabelling, nothing is lost and equality holds. Loss comes from merging: two inputs sent to the same output can no longer be distinguished.}

\addreading{@Cover:elements91}{Theorem 2.8.1}

\endif
