\ifndef{categoricalRegressionPredictionFunction}
\define{categoricalRegressionPredictionFunction}

\editme

\subsection{Prediction Function}

\notes{For class $k\in\{1,\dots,K\}$, define a linear score $f_k(\inputVector)=\mappingVector_k^\top\basisVector(\inputVector)$. The predictive probabilities are given by the softmax:
$$
\pi_k(\inputVector) = \frac{\exp\left(f_k(\inputVector)\right)}{\sum_{j=1}^K \exp\left(f_j(\inputVector)\right)}.
$$}

\slides{Prediction Function}

\slides{
* Class scores: $f_k(\inputVector)=\mappingVector_k^\top\basisVector(\inputVector)$
* Probabilities via softmax: $\pi_k = \exp(f_k)/\sum_j \exp(f_j)$
}
\endif
