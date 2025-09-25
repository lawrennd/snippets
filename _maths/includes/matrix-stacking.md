\ifndef{matrixStacking}
\define{matrixStacking}

\editme

\subsection{Matrix Stacking}

\slides{* **Input**: matrix $\mathbf{A}$
* **Output**: vector $\mathbf{a}$
* **Process**: stack columns vertically}

\newslide{Stacking Formula}

\slidesmall{$$\mathbf{a} = \begin{bmatrix}
\mathbf{a}_{:, 1}\\
\mathbf{a}_{:, 2}\\
\vdots\\
\mathbf{a}_{:, \latentDim}
\end{bmatrix}$$}

\slides{* **Column stacking**: each column becomes a block
* **Order**: first column at top, last at bottom
* **Size**: $mn \times 1$ vector from $m \times n$ matrix}

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
