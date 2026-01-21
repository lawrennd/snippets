\ifndef{softArgMaxFunction}
\define{softArgMaxFunction}

\editme

\subsection{Soft Arg Max (Softmax) Function}

\notes{Given class scores $f_k(\inputVector)=\mappingVector_k^\top\basisVector(\inputVector)$, the softmax maps scores to probabilities: $\pi_k = \frac{\exp(f_k)}{\sum_{j=1}^K \exp(f_j)}$.}

\slides{
* Softmax turns unnormalised scores into probabilities
* Invariant to adding a constant to all scores
}
\endif
