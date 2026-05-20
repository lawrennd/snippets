\ifndef{theMatrixExponentialFamily}
\define{theMatrixExponentialFamily}

\editme

\subsection{The Matrix Exponential Family}

\notes{The matrix exponential family is the non-commutative analogue of the classical exponential family. A density matrix $\rho$ belongs to the matrix exponential family if it can be written as
$$
\rho(\boldsymbol{\theta}) = \exp\!\left(\sum_k \theta_k F_k - \psi(\boldsymbol{\theta})\,\mathbf{I}\right),
$$
where $\boldsymbol{\theta} = (\theta_k)$ are the *natural parameters*, $\{F_k\}$ are Hermitian operators playing the role of *sufficient statistics*, and the scalar
$$
\psi(\boldsymbol{\theta}) = \log\,\text{tr}\!\exp\!\left(\sum_k \theta_k F_k\right)
$$
is the *quantum log-partition function*, which ensures $\mathrm{tr}(\rho) = 1$.}

\notes{The gradient of $\psi$ recovers quantum expectation values:
$$
\nabla_{\theta_k}\psi(\boldsymbol{\theta}) = \text{tr}(\rho\, F_k) = \langle F_k\rangle_\rho,
$$
just as in the classical case the gradient of the cumulant generating function gives the mean of the sufficient statistic. The Hessian of $\psi$ is the *Bogoliubov--Kubo--Mori (BKM) metric*,
$$
G_{jk}(\boldsymbol{\theta}) = \nabla^2_{\theta_j\theta_k}\Psi(\boldsymbol{\theta}),
$$
the quantum analogue of the Fisher information matrix. When all $F_k$ commute this reduces to the classical Fisher information. The von Neumann entropy is recovered from $\Psi$ by a Legendre transform,
$$
S(\rho) = -\mathrm{tr}(\rho\log\rho) = \Psi(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top\nabla\Psi(\boldsymbol{\theta}),
$$
exactly mirroring the classical relation between the log-partition function and the Shannon entropy.}

\slides{
$$
\rho(\boldsymbol{\theta}) = \exp\!\left(\sum_k \theta_k F_k - \psi(\boldsymbol{\theta})\,\mathbf{I}\right)
$$

* $\boldsymbol{\theta}$: natural parameters
* $\psi(\boldsymbol{\theta}) = \log\,\mathrm{tr}\exp\!\left(\sum_k\theta_k F_k\right)$: cumulant generating function
* $G(\boldsymbol{\theta}) = \nabla^2\Psi(\boldsymbol{\theta})$: BKM metric (quantum Fisher information)
}


\notes{The structural parallel between the classical and matrix cases is exact, with one crucial difference: the non-commutativity of the operators $F_k$. In the classical case the sufficient statistics $T_k(\mathbf{x})$ are ordinary functions and commute freely. In the matrix case the Hermitian operators $F_k$ need not commute, $[F_j, F_k] \neq 0$, and the matrix exponential $\exp(\sum_k \theta_k F_k)$ does not factorise over the individual terms. This non-commutativity has two consequences. First, the BKM metric differs from its classical counterpart: it involves a symmetrised operator product averaged against the state $\rho$. Second, a pure state ($S(\rho) = 0$) can coexist with strictly positive marginal entropies, because the marginals of an entangled pure state are mixed. The classical exponential family has no analogue of this: a pure joint distribution has zero entropy everywhere.}


\endif
