\ifndef{dataProcessingInequality}
\define{dataProcessingInequality}

\editme

\subsection{Data-Processing Inequality}

\notes{Mutual information is the pairwise case of multi-information: $I(X;Y)=H(X)-H(X|Y)=H(Y)-H(Y|X)=H(X)+H(Y)-H(X,Y)$. Week 2 defined it from the chain rule and stated the data-processing inequality. We prove it now, because this week's object is $I$.}

\newslides{Data-Processing Inequality}

\slides{If $X\to Y\to Z$ is a Markov chain, processing cannot create information about $X$.}

\slidesincremental{
* Markov: $p(z\mid x,y)=p(z\mid y)$, equivalently $I(X;Z\mid Y)=0$
* $I(X;Y,Z)=I(X;Y)+I(X;Z\mid Y)=I(X;Y)$
* $I(X;Y,Z)=I(X;Z)+I(X;Y\mid Z)\ge I(X;Z)$
* Therefore $I(X;Z)\le I(X;Y)$
}

\speakernotes{LO10. Cover and Thomas Theorem 2.8.1. Board the two expansions of $I(X;Y,Z)$. No-go: you cannot process your way to more $I$.}

\notes{The data-processing inequality [@Cover:elements91, Thm 2.8.1] is the no-go on $I$. If $X\to Y\to Z$ is Markov, then $I(X;Z)\le I(X;Y)$. The first expansion of $I(X;Y,Z)$ uses the chain rule and drops $I(X;Z\mid Y)$ by the Markov property. The second expansion is at least $I(X;Z)$ because conditional mutual information is non-negative. Equality holds when $I(X;Y\mid Z)=0$ — $Y$ is a sufficient statistic of $X$ for $Z$, or $Z$ already captures everything $Y$ knew about $X$.}

\notes{This is the same grammar as $I+H=C$. Conservation says you cannot have both high stored correlation and high free uncertainty without bound. Data processing says you cannot *increase* stored correlation by further processing. A claim that an intelligent system will “just process more” and thereby recover information that a Markov stage has already destroyed is a DPI violation.}

\addreading{@Cover:elements91}{Theorem 2.8.1}

\endif
