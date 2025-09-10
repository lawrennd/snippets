\ifndef{categoricalRegressionMaximumLikelihood}
\define{categoricalRegressionMaximumLikelihood}

\editme

\subsection{Maximum Likelihood}

\slides{
* Conditional independence: $P(\dataVector|\{\mappingVector_k\}, \inputMatrix)=\prod_i P(\dataScalar_i|\{\mappingVector_k\},\inputVector_i)$
}

\notes{With one-hot targets $\dataVector_i\in\{0,1\}^K$ and softmax probabilities $\pi_{ik}$, the (negative) log-likelihood is
$$
E(\{\mappingVector_k\}) = -\sum_{i=1}^\numData \sum_{k=1}^K y_{ik}\log \pi_{ik}.
$$}

\slides{Objective Function}

\slides{
* One-hot targets $\dataVector_i$, softmax probabilities $\pi_{ik}$
* Negative log-likelihood: $E = -\sum_i \sum_k \dataScalar_{ik}\log\pi_{ik}$
}

\endif


