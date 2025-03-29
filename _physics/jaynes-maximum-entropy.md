\ifndef{jaynesMaximumEntropy}
\define{jaynesMaximumEntropy}

\editme

\subsection{Jaynes's Maximum Entropy Principle}

\notes{In his seminal 1957 paper [@Jaynes-information57], Ed Jaynes proposed a foundation for statistical mechanics based on information theory. Rather than relying on ergodic hypotheses or ensemble interpretations, Jaynes recast that the problem of assigning probabilities in statistical as a problem of inference with incomplete information.}

\slides{
* @Jaynes-information57: Statistical mechanics as inference with incomplete information
* Maximum entropy principle: most honest description of what we know
* Avoids unwarranted assumptions beyond available data
}

\notes{A central problem in statistical mechanics is assigning initial probabilities when our knowledge is incomplete. For example, if we know only the average energy of a system, what probability distribution should we use? Jaynes argued that we should use the distribution that maximizes entropy subject to the constraints of our knowledge.}

\slides{
* Die example: Average result 4.5 instead of 3.5
* Constraints:
  * $\sum_{n=1}^6 P_n = 1$ (normalization)
  * $\sum_{n=1}^6 nP_n = 4.5$ (observed average)
}

\notes{Jaynes illustrated the approachwith a simple example: Suppose a die has been tossed many times, with an average result of 4.5 rather than the expected 3.5 for a fair die. What probability assignment $P_n$ ($n=1,2,...,6$) should we make for the next toss?}

\notes{We need to satisfy two constraints
\begin{align}
\sum_{n=1}^6 P_n &= 1 \\
\sum_{n=1}^6 nP_n &= 4.5
\end{align}
}
\notes{Many distributions could satisfy these constraints, but which one makes the fewest unwarranted assumptions? Jaynes argued that we should choose the distribution that is maximally noncommittal with respect to missing information - the one that maximizes the entropy,
\begin{align}
S_I = -\sum_{i} p_i \log p_i
\end{align}
This principle leads to the exponential family of distributions, which in statistical mechanics gives us the canonical ensemble and other familiar distributions.}

\subsection{The General Maximum-Entropy Formalism}

\notes{For a more general case, suppose a quantity $x$ can take values $(x_1, x_2, \ldots, x_n)$ and we know the average values of several functions $f_k(x)$. The problem is to find the probability assignment $p_i = p(x_i)$ that satisfies
\begin{align}
\sum_{i=1}^n p_i &= 1 \\
\sum_{i=1}^n p_i f_k(x_i) &= \langle f_k(x) \rangle = F_k \quad k=1,2,\ldots,m
\end{align}
and maximizes the entropy $S_I = -\sum_{i=1}^n p_i \log p_i$.}

\notes{Using Lagrange multipliers, the solution is the generalized canonical distribution,
\begin{align}
p_i = \frac{1}{Z(\lambda_1,\ldots,\lambda_m)}\exp(-\lambda_1 f_1(x_i) - \ldots - \lambda_m f_m(x_i))
\end{align}
where $Z(\lambda_1,\ldots,\lambda_m)$ is the partition function,
\begin{align}
Z(\lambda_1,\ldots,\lambda_m) = \sum_{i=1}^n \exp(-\lambda_1 f_1(x_i) - \ldots - \lambda_m f_m(x_i))
\end{align}
The Lagrange multipliers $\lambda_k$ are determined by the constraints,
\begin{align}
\langle f_k \rangle = -\frac{\partial}{\partial \lambda_k}\log Z(\lambda_1,\ldots,\lambda_m) \quad k=1,2,\ldots,m.
\end{align}
The maximum attainable entropy is
\begin{align}
(S_I)_{max} = \log Z + \sum_{k=1}^m \lambda_k \langle f_k \rangle.
\end{align}
}

\endif 