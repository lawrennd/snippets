\ifndef{theExponentialFamily}
\define{theExponentialFamily}

\editme

\subsection{Exponential Family}

\notes{The information relaxation dynamics are expressed using the exponential family. A probability distribution in the exponential family is written as
$$
p(\mathbf{x}|\boldsymbol{\theta}) = \exp\left(\boldsymbol{\theta}^\top \mathbf{T}(\mathbf{x}) - \psi(\boldsymbol{\theta})\right),
$$
where $\boldsymbol{\theta}$ are the *natural parameters*, $\mathbf{T}(\mathbf{x})$ are sufficient statistics, and $\psi(\boldsymbol{\theta})$ is the cumulant generating function (log partition function). The Fisher information matrix is the Hessian of the cumulant generating function,
$$
G(\boldsymbol{\theta}) = \nabla\nabla \psi(\boldsymbol{\theta}),
$$
and serves as the canonical Riemannian metric on the statistical manifold.}

\slides{
$$
p(\mathbf{x}|\boldsymbol{\theta}) = \exp\!\left(\boldsymbol{\theta}^\top \mathbf{T}(\mathbf{x}) - \psi(\boldsymbol{\theta})\right)
$$

* $\boldsymbol{\theta}$: natural parameters
* $\psi(\cdot)$: cumulant generating function 
* $G(\boldsymbol{\theta}) = \nabla^2\psi(\boldsymbol{\theta})$: Fisher information
}

\endif
