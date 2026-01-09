\ifndef{kroneckerProducts}
\define{kroneckerProducts}

\editme

\subsection{Kronecker Products}

\slides{* **Notation**: $\mathbf{A} \otimes \mathbf{B}$
* **Input**: matrices $\mathbf{A} \in \Re^{m \times n}$, $\mathbf{B} \in \Re^{p \times q}$
* **Output**: $(mp) \times (nq)$ matrix}

\subsection{Visual Examples}

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.kronecker_illustrate(diagrams='\writeDiagramsDir/maths')}

\figure{\includediagram{\diagramsDir/maths/kronecker_illustrate}{80%}}{Illustration of the Kronecker product.}{kronecker-illustrate}

\newslide{Kronecker Product Visualization}

\plotcode{plot.kronecker_IK(diagrams='\writeDiagramsDir/maths')}

\figure{\includediagram{\diagramsDir/maths/kronecker_IK}{80%}}{Kronecker product between two matrices.}{kronecker-ik}

\newslide{Column vs Row Stacking}

\slides{* **Column stacking**: $\mathbf{I} \otimes \mathbf{K}$ - time independence
* **Row stacking**: $\mathbf{K} \otimes \mathbf{I}$ - dimension independence  
* **Different structure**: affects which variables are correlated}

\newslide{Kronecker Product Formula}

\slidesmall{$$(\mathbf{A} \otimes \mathbf{B})_{ij} = a_{i_1 j_1} b_{i_2 j_2}$$}

\slides{* **Index mapping**: $i = (i_1-1)p + i_2$, $j = (j_1-1)q + j_2$
* **Block structure**: each element of $\mathbf{A}$ scaled by $\mathbf{B}$
* **Size**: $(mp) \times (nq)$ result}

\notes{The Kronecker product of two matrices $\mathbf{A} \in \Re^{m \times n}$ and $\mathbf{B} \in \Re^{p \times q}$ is defined as:
$$
(\mathbf{A} \otimes \mathbf{B})_{ij} = a_{i_1 j_1} b_{i_2 j_2}
$$
where $i = (i_1-1)p + i_2$ and $j = (j_1-1)q + j_2$.}

\newslide{Basic Properties}

\slides{* **Distributive**: $(\mathbf{A} + \mathbf{B}) \otimes \mathbf{C} = \mathbf{A} \otimes \mathbf{C} + \mathbf{B} \otimes \mathbf{C}$
* **Associative**: $(\mathbf{A} \otimes \mathbf{B}) \otimes \mathbf{C} = \mathbf{A} \otimes (\mathbf{B} \otimes \mathbf{C})$
* **Mixed product**: $(\mathbf{A} \otimes \mathbf{B})(\mathbf{C} \otimes \mathbf{D}) = \mathbf{A}\mathbf{C} \otimes \mathbf{B}\mathbf{D}$}

\newslide{Identity and Zero}

\slides{* **Identity**: $\mathbf{I}_m \otimes \mathbf{I}_n = \mathbf{I}_{mn}$
* **Zero**: $\mathbf{0} \otimes \mathbf{A} = \mathbf{A} \otimes \mathbf{0} = \mathbf{0}$
* **Scalar**: $c \otimes \mathbf{A} = \mathbf{A} \otimes c = c\mathbf{A}$}

\newslide{Transpose and Inverse}

\slides{* **Transpose**: $(\mathbf{A} \otimes \mathbf{B})^\top = \mathbf{A}^\top \otimes \mathbf{B}^\top$
* **Inverse**: $(\mathbf{A} \otimes \mathbf{B})^{-1} = \mathbf{A}^{-1} \otimes \mathbf{B}^{-1}$ (when both exist)
* **Determinant**: $\det(\mathbf{A} \otimes \mathbf{B}) = \det(\mathbf{A})^q \det(\mathbf{B})^m$}

\subsection{Matrix Stacking and Kronecker Products}

\newslide{Column Stacking}

\slides{* **Stacking**: place columns of matrix on top of each other
* **Notation**: $\mathbf{a} = \text{vec}(\mathbf{A})$ or $\mathbf{a} = \mathbf{A}\!:$
* **Kronecker form**: $\mathbf{I} \otimes \mathbf{K}$ for column-wise structure}

\newslide{Row Stacking}

\slides{* **Alternative**: stack rows instead of columns
* **Kronecker form**: $\mathbf{K} \otimes \mathbf{I}$ for row-wise structure
* **Different structure**: changes which variables are independent}

\notes{There are two main ways to stack matrices:

**Column Stacking**: Each column of $\mathbf{A}$ becomes a block:
$$
\mathbf{a} = \begin{bmatrix}
\mathbf{a}_{:, 1}\\
\mathbf{a}_{:, 2}\\
\vdots\\
\mathbf{a}_{:, n}
\end{bmatrix}
$$

**Row Stacking**: Each row of $\mathbf{A}$ becomes a block:
$$
\mathbf{a} = \begin{bmatrix}
\mathbf{a}_{1, :}\\
\mathbf{a}_{2, :}\\
\vdots\\
\mathbf{a}_{m, :}
\end{bmatrix}
$$}


\subsection{Computational Advantages}

\newslide{Efficient Matrix Operations}

\slides{* **Inversion**: $(\mathbf{A} \otimes \mathbf{B})^{-1} = \mathbf{A}^{-1} \otimes \mathbf{B}^{-1}$
* **Eigenvalues**: $\lambda_i(\mathbf{A} \otimes \mathbf{B}) = \lambda_j(\mathbf{A}) \lambda_k(\mathbf{B})$
* **Determinant**: $\det(\mathbf{A} \otimes \mathbf{B}) = \det(\mathbf{A})^q \det(\mathbf{B})^m$}

\newslide{Memory and Speed Benefits}

\slides{* **Storage**: avoid storing full covariance matrix
* **Operations**: work with smaller component matrices
* **Scaling**: $O(n^3)$ becomes $O(n_1^3 + n_2^3)$ for $n = n_1 n_2$}

\notes{The Kronecker structure provides significant computational advantages

1. **Memory efficiency**: Instead of storing an $n \times n$ matrix, we store smaller component matrices
2. **Computational efficiency**: Matrix operations scale better with Kronecker structure
3. **Numerical stability**: Often more stable than direct computation of large matrices}


\endif
\endif
