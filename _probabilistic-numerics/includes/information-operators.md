\ifndef{informationOperators}
\define{informationOperators}

\editme

\section{Information Operators}

\notes{Information operators provide a formal way to guide computational decisions in probabilistic numerics. These operators help us quantify the value of different computational choices.}

\subsection{Key Operators}

\notes{Two fundamental operators in the context of Bayesian quadrature are:

1. **Integrand Variance**:
   $$\alpha(x) = k(x,x)$$
   This measures our uncertainty about the function value at any point.

2. **Integral Variance Reduction**:
   $$\alpha(x) = k_F(X,X) - k_F(X,x)$$
   This quantifies how much our uncertainty about the integral would be reduced by evaluating the function at point $x$.}

\notes{These operators, sometimes called "Design Rules", provide a principled framework for:
* Selecting evaluation points
* Balancing exploration vs exploitation
* Deciding when to terminate computation
* Allocating computational resources}

\endif
