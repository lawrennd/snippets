\ifndef{maximumEntropyFormalism}
\define{maximumEntropyFormalism}

\editme

\subsection{The General Maximum-Entropy Formalism}

\notes{For a more general case, suppose a quantity $x$ can take values $(x_1, x_2, \ldots, x_n)$ and we know the average values of several functions $f_k(x)$. The problem is to find the probability assignment $p_i = p(x_i)$ that satisfies
\begin{align}
\sum_{i=1}^n p_i &= 1 \\
\sum_{i=1}^n p_i f_k(x_i) &= \langle f_k(x) \rangle = F_k \quad k=1,2,\ldots,m
\end{align}
and maximises the entropy $S_I = -\sum_{i=1}^n p_i \log p_i$.}

\notes{Using Lagrange multipliers, the solution is the generalised canonical distribution,
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
\slides{
$$
p_i = \frac{1}{Z(\lambda_1,\ldots,\lambda_m)}\exp(-\lambda_1 f_1(x_i) - \ldots - \lambda_m f_m(x_i))
$$
$$
Z(\lambda_1,\ldots,\lambda_m) = \sum_{i=1}^n \exp(-\lambda_1 f_1(x_i) - \ldots - \lambda_m f_m(x_i))
$$
$$
\langle f_k \rangle = -\frac{\partial}{\partial \lambda_k}\log Z(\lambda_1,\ldots,\lambda_m) \quad k=1,2,\ldots,m.
$$}
\endif
