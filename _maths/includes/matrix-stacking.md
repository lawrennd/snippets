\ifndef{matrixStacking}
\define{matrixStacking}

\editme

\subsection{Matrix Stacking}

\notes{A stacking operation takes a matrix, $\mathbf{A}$, and rewrites it as a vector where each column of $\mathbf{A}$ is stacked on top of one another to give a new vector $\mathbf{a}$,
$$
\mathbf{a} = \begin{bmatrix}
\mathbf{a}_{:, 1}\\
    \mathbf{a}_{:, 2}\\
    \vdots\\
	\mathbf{a}_{:, \latentDim}
	\end{bmatrix}
$$}

\endif
