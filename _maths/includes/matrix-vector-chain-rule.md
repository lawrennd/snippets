\ifndef{matrixVectorChainRule}
\define{matrixVectorChainRule}

\editme

\subsection{Matrix Vector Chain Rule}

\notes{There are several standards for how to perform the chain rule with multivariate calculus. My favourite is from Mike Brookes. The details are given by @Brookes-matrix05.}

\notes{How do we write the derivative of a vector with respect to a matrix or a matrix with a respect to a matrix? In Brookes's approach the first rule is that you never compute these directly. Instead you form an intermediate *stacking* operation.}

\include{_maths/includes/matrix-stacking.md}

\notes{Next we consider the derivative of one vector with respect to another as
$$
\frac{\text{d} \mathbf{a}}{\text{d} \mathbf{b}} \in \Re^{m \times n}
$$ 
if $\mathbf{a} \in \Re^{m \times 1}$ and $\mathbf{b} \in \Re^{n \times 1}$.} 

\notes{This now means that to obtain matrix-matrix derivatives we make use of $\mathbf{C}:$: to indicate a vector formed from the matrix $\mathbf{C}$ by stacking the columns of $\mathbf{C}$ to form a $\Re^{m n \times 1}$ vector if $\mathbf{C} \in \Re^{m \times n}$.}

\notes{Under this notation we can write the derivative of a matrix $\mathbf{E} \in \Re^{p \times q}$ with respect to $\mathbf{C}$ as $\frac{\text{d} \mathbf{E}}{\text{d} \mathbf{C}} \in \Re^{p q \times m n}$. This notation makes it easier to apply the chain rule while maintaining matrix notation.}

\notes{This entails the use of Kronecker products, we denote the Kronecker product of $\mathbf{F}$ and $\mathbf{G}$ as $\mathbf{F} \otimes \mathbf{G}$.}

\ifndef{kroneckerProducts}
\include{_maths/includes/kronecker-products.md}
\endif

\notes{In most cases Kronecker products they arise below they are later removed using this relationship
$$
(\mathbf{E}:)^{\top} \mathbf{F} \otimes \mathbf{G}=\left(\left(\mathbf{G}^{\top} \mathbf{E F}\right):\right)^{\top}
$$
this form typically arises whenever the chain rule is applied,
$$
\frac{\text{d} \errorFunction}{\text{d} \mathbf{H}:} \frac{\text{d} \mathbf{H}:}{\text{d} \mathbf{J}:}=\frac{\text{d} \errorFunction}{\text{d} \mathbf{J}:},
$$

as we normally find that $\frac{\text{d} \mathbf{H}}{\text{d} \mathbf{J}}$ has the form of a Kronecker product, $\frac{\text{d} \mathbf{H}}{\text{d} \mathbf{J}}=\mathbf{F} \otimes \mathbf{G}$ and we expect the result of $\frac{\text{d} \errorFunction}{\text{d} \mathbf{H}}$ and $\frac{\text{d} \errorFunction}{\text{d} \mathbf{J}}$ to be in the form $(\mathbf{\errorFunction}:)^{\mathbf{T}}$. The following two identities for Kronecker products will also prove useful.
$$
\mathbf{F}^{\top} \otimes \mathbf{G}^{\top}=(\mathbf{F} \otimes \mathbf{G})^{\top}
$$
and
$$
(\mathbf{E} \otimes \mathbf{G})(\mathbf{F} \otimes \mathbf{H})=\mathbf{E F} \otimes \mathbf{G H}
$$
Generally we will use two ways of writing the derivative of a scalar with respect to a matrix, $\frac{\text{d} \errorFunction}{\text{d} \mathbf{J}}$ and $\frac{\text{d} \errorFunction}{\text{d} \mathbf{J}}$, the first being a row vector and the second is a matrix of the same dimension of $\mathbf{J}$. The second representation is more convenient for summarising the result, the first is easier to wield when computing the result. The equivalence of the representations is given by
$$
\frac{\text{d} \errorFunction}{\text{d} \mathbf{J}:}=\left(\left(\frac{\text{d} \errorFunction}{\text{d} \mathbf{J}}\right):\right)^{\top}.
$$


Any other results used for matrix differentiation and not explicitly given here may be found in Brookes [2005].

\include{_maths/includes/matrix-stacking.md}


\endif
