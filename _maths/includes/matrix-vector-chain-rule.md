\ifndef{matrixVectorChainRule}
\define{matrixVectorChainRule}

\editme

\subsection{Matrix Vector Chain Rule}

\newslide{Matrix Calculus Standards}

\slides{* **Multiple approaches** to multivariate chain rule
* **Mike Brookes' method**: preferred approach
* **Reference**: @Brookes-matrix05}

\notes{There are several standards for how to perform the chain rule
with multivariate calculus. My favourite is from Mike Brookes. The
details are given by @Brookes-matrix05.}

\newslide{Brookes' Approach}

\slides{* **Never compute** matrix derivatives directly
* **Stacking operation**: intermediate step
* **Vector derivatives**: easier to handle}

\notes{How do we write the derivative of a vector with respect to a
matrix or a matrix with a respect to a matrix? In Brookes's approach
the first rule is that you never compute these directly. Instead you
form an intermediate *stacking* operation.}

\include{_maths/includes/matrix-stacking.md}

\newslide{Vector Derivatives}

\slidesmall{$$\frac{\text{d} \mathbf{a}}{\text{d} \mathbf{b}} \in \Re^{m \times n}$$}

\slides{* **Input**: $\mathbf{a} \in \Re^{m \times 1}$, $\mathbf{b} \in \Re^{n \times 1}$
* **Output**: $m \times n$ matrix
* **Standard form**: vector-to-vector derivatives}

\notes{Next we consider the derivative of one vector with respect to
another as 
$$ \frac{\text{d} \mathbf{a}}{\text{d} \mathbf{b}} \in
\Re^{m \times n} 
$$ 
if $\mathbf{a} \in \Re^{m \times 1}$ and $\mathbf{b} \in \Re^{n \times
1}$.}

\newslide{Matrix Stacking Notation}

\slides{* **$\mathbf{C}:$**: vector formed from matrix $\mathbf{C}$
* **Stacking**: columns of $\mathbf{C}$ → $\Re^{mn \times 1}$ vector
* **Condition**: $\mathbf{C} \in \Re^{m \times n}$}

\notes{This now means that to obtain matrix-matrix derivatives we make
use of $\mathbf{C}:$: to indicate a vector formed from the matrix
$\mathbf{C}$ by stacking the columns of $\mathbf{C}$ to form a $\Re^{m
n \times 1}$ vector if $\mathbf{C} \in \Re^{m \times n}$.}

\newslide{Matrix-Matrix Derivatives}

\slidesmall{$$\frac{\text{d} \mathbf{E}}{\text{d} \mathbf{C}} \in \Re^{pq \times mn}$$}

\slides{* **Input**: $\mathbf{E} \in \Re^{p \times q}$, $\mathbf{C} \in \Re^{m \times n}$
* **Output**: $pq \times mn$ matrix
* **Advantage**: easier chain rule application}

\notes{Under this notation we can write the derivative of a matrix
$\mathbf{E} \in \Re^{p \times q}$ with respect to $\mathbf{C}$ as
$\frac{\text{d} \mathbf{E}}{\text{d} \mathbf{C}} \in \Re^{p q \times m
n}$. This notation makes it easier to apply the chain rule while
maintaining matrix notation.}

\newslide{Kronecker Products}

\slides{* **Notation**: $\mathbf{F} \otimes \mathbf{G}$
* **Essential tool**: for matrix derivatives
* **Key role**: in chain rule applications}

\notes{This entails the use of Kronecker products, we denote the
Kronecker product of $\mathbf{F}$ and $\mathbf{G}$ as $\mathbf{F}
\otimes \mathbf{G}$.}

\ifndef{kroneckerProducts}
\include{_maths/includes/kronecker-products.md}
\endif

\newslide{Kronecker Product Simplification}

\slidesmall{$$(\mathbf{E}:)^{\top} \mathbf{F} \otimes \mathbf{G}=\left(\left(\mathbf{G}^{\top} \mathbf{E F}\right):\right)^{\top}$$}

\slides{* **Removal rule**: Kronecker products often simplified
* **Chain rule**: typically produces this form
* **Key insight**: avoid direct Kronecker computation}

\notes{In most cases Kronecker products they arise below they are
later removed using this relationship
$$
(\mathbf{E}:)^{\top} \mathbf{F} \otimes \mathbf{G}=\left(\left(\mathbf{G}^{\top} \mathbf{E F}\right):\right)^{\top}
$$
this form typically arises whenever the chain rule is applied,}

\newslide{Chain Rule Application}

\slidesmall{$$\frac{\text{d} \errorFunction}{\text{d} \mathbf{H}:} \frac{\text{d} \mathbf{H}:}{\text{d} \mathbf{J}:}=\frac{\text{d} \errorFunction}{\text{d} \mathbf{J}:}$$}

\slidesmall{$$\frac{\text{d}\mathbf{H}}{\text{d} \mathbf{J}} = \mathbf{F} \otimes \mathbf{G}$$}

\notes{$$ 
\frac{\text{d} \errorFunction}{\text{d} \mathbf{H}:} \frac{\text{d}
\mathbf{H}:}{\text{d} \mathbf{J}:}=\frac{\text{d}
\errorFunction}{\text{d} \mathbf{J}:}, 
$$
as we normally find that $\frac{\text{d} \mathbf{H}}{\text{d}
\mathbf{J}}$ has the form of a Kronecker product, 
$$
\frac{\text{d}\mathbf{H}}{\text{d} \mathbf{J}} = \mathbf{F} \otimes \mathbf{G}
$$ 
and we expect the result of $\frac{\text{d} \errorFunction}{\text{d}
\mathbf{H}}$ and $\frac{\text{d} \errorFunction}{\text{d} \mathbf{J}}$
to be in the form $(\mathbf{\errorFunction}:)^\top$.}

\newslide{Kronecker Product Identities}

\slidesmall{$$\mathbf{F}^{\top} \otimes \mathbf{G}^{\top}=(\mathbf{F} \otimes \mathbf{G})^{\top}$$}

\slidesmall{$$(\mathbf{E} \otimes \mathbf{G})(\mathbf{F} \otimes \mathbf{H})=\mathbf{E F} \otimes \mathbf{G H}$$}

\notes{The
following two identities for Kronecker products will also prove
useful.
$$
\mathbf{F}^{\top} \otimes \mathbf{G}^{\top}=(\mathbf{F} \otimes \mathbf{G})^{\top}
$$
and
$$
(\mathbf{E} \otimes \mathbf{G})(\mathbf{F} \otimes
\mathbf{H})=\mathbf{E F} \otimes \mathbf{G H}
$$}

\newslide{Derivative Representations}

\slides{* **Two forms**: row vector vs matrix
* **Row vector**: easier computation
* **Matrix**: better summarization}

\slidesmall{$$\frac{\text{d} \errorFunction}{\text{d} \mathbf{J}:}=\left(\left(\frac{\text{d} \errorFunction}{\text{d} \mathbf{J}}\right):\right)^{\top}$$}

\notes{Generally we will use two ways of writing the derivative of a scalar
with respect to a matrix, $\frac{\text{d} \errorFunction}{\text{d}
\mathbf{J}}$ and $\frac{\text{d} \errorFunction}{\text{d}
\mathbf{J}}$, the first being a row vector and the second is a matrix
of the same dimension of $\mathbf{J}$. The second representation is
more convenient for summarising the result, the first is easier to
wield when computing the result. The equivalence of the
representations is given by
$$ 
\frac{\text{d} \errorFunction}{\text{d}
\mathbf{J}:}=\left(\left(\frac{\text{d} \errorFunction}{\text{d}
\mathbf{J}}\right):\right)^{\top}.
$$}

\endif
