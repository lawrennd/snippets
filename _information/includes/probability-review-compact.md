\ifndef{probabilityReviewCompact}
\define{probabilityReviewCompact}
\editme

\subsection{Probability Review}

\newslides{Joint, Marginal, Conditional}

\slidesincremental{
* Joint $P(x,y)$: both
* Marginal $P(x)$: regardless of $y$
* Conditional $P(x\mid y)$: $x$ given $y$
}

\notes{Notation: we often write $P(x,y)$ for $P(X=x,Y=y)$. Unlike a generic bivariate function, $P(x,y)=P(y,x)$.}

\newslides{Product Rule and Sum Rule}

\slidesincremental{
* Product: $P(x,y)=P(x\mid y)P(y)$
* Sum: $P(y)=\sum_x P(x,y)$
* Both are normalising bookkeeping, not modelling assumptions
}

\notes{The product rule relates joint and conditional. The sum rule recovers a marginal by summing out the variable you do not care about. Continuous analogues replace sums by integrals.}

\newslides{Bayes' Rule}

\slides{
$$
P(y\mid x)=\frac{P(x\mid y)P(y)}{P(x)}
$$
}

\slidesincremental{
* Follows from the product rule and symmetry of the joint
* Inverts the conditioning — updates a prior given a likelihood
* $P(x)=\sum_y P(x\mid y)P(y)$ when $y$ is discrete
}

\notes{Bayes is not a third axiom; it is the product rule rearranged. The barrels example below is a small discrete inversion of the conditioning.}

\include{_ml/includes/bayes-rule-barrels-example.md}

\addreading{@Bishop:book06}{Probability distributions: Section 1.2}

\endif
