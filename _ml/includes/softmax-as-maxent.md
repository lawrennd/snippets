\ifndef{softmaxAsMaxent}
\define{softmaxAsMaxent}

\editme

\subsection{Softmax is MaxEnt with Features}

\notes{The two-level system from week 1 and the Bernoulli are the same exponential family. Occupancy of the excited state is a bit. The natural parameter is $\theta = -\beta\varepsilon$ if you are reading a paramagnet, and $\theta = \log\frac{\pi}{1-\pi}$ if you are reading a coin. The log-partition $A(\theta)=\log(1+e^{\theta})$ is binary entropy's conjugate in either language. That is the unary case of LO6, already on the board.}

\slidesincremental{
* Two-level $\Leftrightarrow$ Bernoulli
* $\theta = -\beta\varepsilon$ or $\mathrm{logit}(\pi)$
* Same $A(\theta)=\log(1+e^{\theta})$
}

\newslide{Features, Not Just the Outcome}

\notes{The die constrained the mean of a single coordinate. A classifier constrains the mean of a *feature* of the pair $(x,y)$. Write $T(x,y)=f(x,y)$ for a vector of functions you have chosen --- a bias, the coordinates of $x$, an indicator that a word occurs, anything you can compute. MaxEnt subject to
$$
\mathbb{E}_{p(y\mid x)\,p_{\mathrm{data}}(x)}[f(x,y)] = \mathbb{E}_{p_{\mathrm{data}}}[f(x,y)]
$$
is the same Lagrange problem as the die. The solution is
$$
p(y\mid x) = \exp\bigl(\theta\cdot f(x,y) - A(\theta;x)\bigr),
$$
with $A(\theta;x)=\log\sum_{y'}\exp(\theta\cdot f(x,y'))$ the log-sum-exp over labels. That is softmax. Logistic regression is the two-class case, $f(x,y)=y\,(1,x)$ for $y\in\{0,1\}$.}

\slides{
$$
p(y\mid x)=\frac{\exp(\theta\cdot f(x,y))}{\sum_{y'}\exp(\theta\cdot f(x,y'))}
$$
* Constraint: expected features match the data
* Same multipliers as the die
}

\newslide{Maximum Likelihood is the Same Fit}

\notes{MacKay's Exercises 22.12--22.13 record the identification: maximum-likelihood fitting of an exponential family matches the moments of $T$, and MaxEnt with those moments produces the same family [@MacKay-information03]. The classifier does not care which story you tell.

@Berger-maximum96 is the natural-language version of this calculation. They constrain binary features of the pair $(x,y)$ --- a word in a window, a part of speech, a class --- and recover
$$
p(y\mid x)=\exp\bigl(\lambda\cdot f(x,y)-A(\lambda;x)\bigr).
$$
They prove the dual: the MaxEnt distribution in that constrained set is the exponential model of maximum likelihood on the sample. The algorithm is generalized iterative scaling, which is moment matching.

The results are translation decisions in IBM's Candide system, trained on the Canadian Hansard. For French \emph{NOUN de NOUN} phrases --- \emph{conflit d'int\'er\^et} stays word-for-word, \emph{taux d'int\'er\^et} swaps --- a never-swap baseline is 70.2\% accurate on 71,555 held-out cases. A MaxEnt model grown to 358 features reaches 80.4\%. They also grew models for the French rendering of English \emph{in} and \emph{to run}, and for finding rift points at which a French sentence can be split without breaking an alignment.

MacKay then declines to use MaxEnt as a method of *inference* --- the loaded die, he says, is a job for Bayes. Hold that tension for the synthesis. The object on this slide is not in dispute. It is an exponential family whose sufficient statistic is a feature map.}

\slidesincremental{
* MaxEnt with features $=$ softmax
* Softmax MLE $=$ moment matching
* The die was $f(x)=x$
}

\addreading{@MacKay-information03}{Exercises 22.12--22.13}
\addreading{@Berger-maximum96}{the whole paper}

\endif
