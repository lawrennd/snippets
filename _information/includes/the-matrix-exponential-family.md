\ifndef{theMatrixExponentialFamily}
\define{theMatrixExponentialFamily}

\editme

\subsection{The Matrix Exponential Family}

\notes{The matrix exponential family is the non-commutative analogue of the classical exponential family. A density matrix $\rho$ belongs to the matrix exponential family if it can be written as
$$
\rho(\boldsymbol{\theta}) = \exp\!\left(\sum_k \theta_k F_k - \cumulantGeneratingFunction(\boldsymbol{\theta})\,\mathbf{I}\right),
$$
where $\boldsymbol{\theta} = (\theta_k)$ are the *natural parameters*, $\{F_k\}$ are Hermitian operators playing the role of *sufficient statistics*, and the scalar
$$
\cumulantGeneratingFunction(\boldsymbol{\theta}) = \log\,\text{tr}\!\exp\!\left(\sum_k \theta_k F_k\right)
$$
is the *quantum log-partition function*, which ensures $\mathrm{tr}(\rho) = 1$.}

\notes{The gradient of $\cumulantGeneratingFunction$ recovers quantum expectation values:
$$
\nabla_{\theta_k}\cumulantGeneratingFunction(\boldsymbol{\theta}) = \text{tr}(\rho\, F_k) = \langle F_k\rangle_\rho,
$$
just as in the classical case the gradient of the cumulant generating function gives the mean of the sufficient statistic. The Hessian of $\cumulantGeneratingFunction$ is the *Bogoliubov--Kubo--Mori (BKM) metric*,
$$
G_{jk}(\boldsymbol{\theta}) = \nabla^2_{\theta_j\theta_k}\cumulantGeneratingFunction(\boldsymbol{\theta}),
$$
the quantum analogue of the Fisher information matrix. When all $F_k$ commute this reduces to the classical Fisher information. The von Neumann entropy is recovered from $\cumulantGeneratingFunction$ by a Legendre transform,
$$
S(\rho) = -\mathrm{tr}(\rho\log\rho) = \cumulantGeneratingFunction(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top\nabla\cumulantGeneratingFunction(\boldsymbol{\theta}),
$$
exactly mirroring the classical relation between the log-partition function and the Shannon entropy.}

\slides{
$$
\rho(\boldsymbol{\theta}) = \exp\!\left(\sum_k \theta_k F_k - \cumulantGeneratingFunction(\boldsymbol{\theta})\,\mathbf{I}\right)
$$

* $\boldsymbol{\theta}$: natural parameters
* $\cumulantGeneratingFunction(\boldsymbol{\theta}) = \log\,\mathrm{tr}\exp\!\left(\sum_k\theta_k F_k\right)$: cumulant generating function
* $G(\boldsymbol{\theta}) = \nabla^2\cumulantGeneratingFunction(\boldsymbol{\theta})$: BKM metric (quantum Fisher information)
}


\notes{The structural parallel between the classical and matrix cases is exact, with one crucial difference: the non-commutativity of the operators $F_k$. In the classical case the sufficient statistics $T_k(\mathbf{x})$ are ordinary functions and commute freely. In the matrix case the Hermitian operators $F_k$ need not commute, $[F_j, F_k] \neq 0$, and the matrix exponential $\exp(\sum_k \theta_k F_k)$ does not factorise over the individual terms. This non-commutativity has two consequences. First, the BKM metric differs from its classical counterpart: it involves a symmetrised operator product averaged against the state $\rho$. Second, a pure state ($S(\rho) = 0$) can coexist with strictly positive marginal entropies, because the marginals of an entangled pure state are mixed. The classical exponential family has no analogue of this: a pure joint distribution has zero entropy everywhere.}

\newslide{Faithful States}

\notes{A density matrix $\rho$ is *faithful* if it is strictly positive definite, $\rho > 0$, meaning every eigenvalue is strictly positive. Every member of the matrix exponential family is faithful: since the matrix exponential $\exp(A)$ is positive definite for any Hermitian $A$, the density matrix $\rho(\boldsymbol{\theta})$ has strictly positive eigenvalues for all finite $\boldsymbol{\theta}$.

Faithfulness matters for two reasons. First, the BKM metric $G(\boldsymbol{\theta})$ is only well-defined for faithful states — it involves expressions of the form $\int_0^1 \text{tr}(\rho^t A \rho^{1-t} B)\,\text{d}t$ that are singular when $\rho$ has a zero eigenvalue. Second, faithful states are the *interior* of the set of density matrices; pure states ($S(\rho) = 0$, rank 1) lie on the boundary. As a sequence of faithful states approaches a pure state, the natural parameters $\boldsymbol{\theta}$ diverge and the BKM metric degenerates. This is precisely why the LME origin — a pure state — lies at infinite BKM distance from any interior point and is unreachable in finite game time.}

\slides{
* Implies *faithful* states (full rank $\rho$)
* Pure states are on *boundary* of family
* BKM Metric is *divergent*
}

\endif
