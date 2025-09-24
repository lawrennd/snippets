\ifndef{moreUsefulMultivariateDerivatives}
\define{moreUsefulMultivariateDerivatives}

\editme

\subsection{Useful Multivariate Derivatives}

\notes{By defining our multivariate derivatives through vectors, we
can now write down the results for some more useful multivariate
derivatives. Let's start with $\mathbf{b} = \mathbf{A}\mathbf{x}$ and
assume we want the gradient of $\mathbf{b}$ with respect to
$\mathbf{A}$. We assume that $\mathbf{A} \in \Re^{m\times n}$. To
derive the gradient we'll get there slightly indirectly and consider
the gradient of $\mathbf{b}$ first,
$$
\frac{\text{d}}{\text{d} \mathbf{a^\prime}} \mathbf{A} \mathbf{x}
$$
which must be a matrix of size $m \times mn$. Here we've taken the
unusual step of defining $\mathbf{a^\prime} =
\vecb{\mathbf{A}^\top}$. We construct this form because it means that
we are forming $\mathbf{a}^\prime$ by stacking the columns of
$\mathbf{A}^\top$, which are the rows of $\mathbf{A}$.}

\notes{This makes the derivation straightforward by inspection because
the vector $\mathbf{b} = \mathbf{A}\mathbf{x}$ is a vector formed of
inner products of the different *rows* of $\mathbf{A}$,
$$
\mathbf{A}\mathbf{x} = \begin{bmatrix}
\mathbf{a}_{1, :}^\top \mathbf{x} \\
\mathbf{a}_{2, :}^\top \mathbf{x} \\
\vdots \\
\mathbf{a}_{m, :}^\top \mathbf{x}
\end{bmatrix}.
$$
Recall that the gradient 
$$
\frac{\text{d}\mathbf{a}_{i,:}^\top \mathbf{x}}{\text{d}\mathbf{a}_{i,:}} = \mathbf{x},
$$ 
where $\mathbf{a}_{i, :}$ is a vector formed from the $i$th column of $\mathbf{A}$. So this means means that we should expect our result to consist only of repeated versions of $\mathbf{x}$. From our definition of vector derivatives, we know we are looking for a result with $m$ rows and $nm$ columns. This is where the Kronecker product comes in. We note that $\eye \otimes \mathbf{x}^\top$ provides a tiling of $\mathbf{x}$ of the form,
$$
\eye_m \otimes \mathbf{x}^\top = \begin{bmatrix}
\mathbf{x}^\top & \zerosVector & \cdots & \zerosVector \\
\zerosVector & \mathbf{x}^\top & \cdots & \zerosVector \\
\vdots & \vdots & \ddots & \vdots \\
\zerosVector & \zerosVector & \cdots& \mathbf{x}^\top
\end{bmatrix}.
$$
where $\eye_m$ is the $m$ dimensional identity matrix. So this means
we can write,
$$
\frac{\text{d}}{\text{d} \mathbf{a^\prime}} \mathbf{A} \mathbf{x} = \eye_{m} \otimes \mathbf{x}^\top
$$
because we can see that each row of this matrix contains the derivative of $b_i = \mathbf{a}_{i, :}^\top \mathbf{x}$ with respect to $\mathbf{a}^\prime$, wherewe constructed $\mathbf{a}^\prime$ to be the stacking of the *rows* of $\mathbf{A}$. The elements are zero apart from those associated with $\mathbf{a}_{i, :}$ where the elements are $\mathbf{x}$.}

\notes{Now, to get the gradient with respect to $\mathbf{a} = \vec{\mathbf{A}}$ instead of with respect to $\mathbf{a}^\prime$ we reverse the order of the Kronecker product
$$
\frac{\text{d}}{\text{d} \mathbf{a^\prime}} \mathbf{A} \mathbf{x} = \mathbf{x}^\top \otimes \eye_{m} 
$$
which disperses the elements of $\mathbf{x}$ across the matrix,
$$
\mathbf{x}^\top \otimes \eye_{m}  = \begin{bmatrix}
x_1 \eye_m & x_2 \eye_m & \cdots & x_n \eye_m
\end{bmatrix}
$$ 
and is the correct for when we are stacking the columns of $\mathbf{A}.
}

\endif
