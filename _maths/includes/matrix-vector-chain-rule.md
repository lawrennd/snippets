\ifndef{matrixVectorChainRule}
\define{matrixVectorChainRule}

\editme

\subsection{Matrix Vector Chain Rule}

\notes{There are several standards for how to perform the chain rule with multivariate calculus. My favourite is from Mike Brookes. The details are given by @Brookes-matrix05.}

\ifndef{kroneckerProducts}
\notes{Before introducing it though, we need to introduce Kronecker products.
\include{_maths/incldues/kronecker-products.md}
\endif

\notes{Now we have the Kronecker product, we are ready to explain the chain rule for multivariate calculus. How do we write the derivative of a vector with respect to a matrix or a matrix with a respect to a matrix?}

\notes{In Brookes's approach the first rule is that you never compute these directly. Instead you form an intermediate *stacking* operation.}


\include{_maths/includes/matrix-stacking.md}


\endif
