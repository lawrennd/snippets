\ifndef{fisherInformationMatrix}
\define{fisherInformationMatrix}

\editme

\subsection{Fisher Information Matrix}

\notes{We'll now derive the form of the Fisher Information Matrix $G(\boldsymbol{\theta})$ from the partition function:
$$
Z(\boldsymbol{\theta}) = \mathrm{tr}\left[\exp\left(\sum_i \theta_i H_i \right)\right]
$$
We'll proceed by differentiating with respect to $\theta_i$ for the expectation values, then compute the second derivative to get the Fisher Information Matrix, 
$$
G_{ij} = \frac{\partial^2 \log Z(\boldsymbol{\theta})}{ \partial \theta_i \partial \theta_j}.
$$
which we'll then link to the  curvature.}

\notes{First we differentiate $\log Z(\boldsymbol{\theta})$ with respect to $\theta_i$,
$$
Z(\boldsymbol{\theta}) = \mathrm{tr}\left[ \exp\left(\sum_j \theta_j H_j\right) \right]
$$
Taking the derivative of $\log Z(\boldsymbol{\theta})$ with respect to $\theta_i$, we apply the chain rule to the definition of $\log Z$,
$$
\frac{\partial \log Z(\boldsymbol{\theta})}{\partial \theta_i} = \frac{1}{Z(\boldsymbol{\theta})} \frac{\partial Z(\boldsymbol{\theta})}{\partial \theta_i}
= \frac{1}{Z(\boldsymbol{\theta})} \mathrm{tr}\left[ H_i \, \exp\left(\sum_j \theta_j H_j\right) \right]
$$
So we have
$$
\frac{\partial \log Z(\boldsymbol{\theta})}{\partial \theta_i} = \mathrm{tr}(\rho H_i) = \langle H_i \rangle
$$
This is the expected value of $H_i$ under the current distribution $\rho(\boldsymbol{\theta})$.}

\notes{We now compute the second derivative of $\log Z(\boldsymbol{\theta})$ to obtain the Fisher Information Matrix elements $G_{ij}$, using the definition
$$
G_{ij} = \frac{\partial^2 \log Z(\boldsymbol{\theta})}{\partial \theta_i \partial \theta_j}
$$
by differentiating the  expression
$$
\frac{\partial \log Z(\boldsymbol{\theta})}{\partial \theta_i} = \mathrm{tr}(\rho H_i),
$$
through another application of the product and chain rules. The second derivative then is
$$
\frac{\partial^2 \log Z(\boldsymbol{\theta})}{\partial \theta_i \partial \theta_j}
= \frac{\partial}{\partial \theta_j} \mathrm{tr}(\rho H_i)
= \mathrm{tr}\left( \frac{\partial \rho}{\partial \theta_j} H_i \right)
$$
We can compute $\frac{\partial \rho}{\partial \theta_j}$ since
$\rho = \frac{1}{Z(\boldsymbol{\theta})} \exp\left(\sum_k \theta_k H_k\right)$,
we can use the product rule
$$
\frac{\partial \rho}{\partial \theta_j} = \frac{\partial}{\partial \theta_j} \left( \frac{1}{Z(\boldsymbol{\theta})} \exp\left(\sum_k \theta_k H_k\right) \right)
= -\frac{1}{Z(\boldsymbol{\theta})^2} \frac{\partial Z(\boldsymbol{\theta})}{\partial \theta_j} \exp\left(\sum_k \theta_k H_k\right) + \frac{1}{Z(\boldsymbol{\theta})} H_j \exp\left(\sum_k \theta_k H_k\right)
$$
which simplifies to
$$
\frac{\partial \rho}{\partial \theta_j} = -\rho \frac{\partial \log Z(\boldsymbol{\theta})}{\partial \theta_j} + \rho H_j
$$
Substituting this back into our expression for the second derivative, we get
$$
\frac{\partial^2 \log Z(\boldsymbol{\theta})}{\partial \theta_i \partial \theta_j}
= \mathrm{tr}\left( \left( -\rho \frac{\partial \log Z(\boldsymbol{\theta})}{\partial \theta_j} + \rho H_j \right) H_i \right)
$$
which simplifies to
$$
\frac{\partial^2 \log Z(\boldsymbol{\theta})}{\partial \theta_i \partial \theta_j}
= -\frac{\partial \log Z(\boldsymbol{\theta})}{\partial \theta_j} \mathrm{tr}(\rho H_i) + \mathrm{tr}(\rho H_i H_j)
$$
or
$$
\frac{\partial^2 \log Z(\boldsymbol{\theta})}{\partial \theta_i \partial \theta_j}
= -\langle H_i \rangle \langle H_j \rangle + \langle H_i H_j \rangle
$$
which is the covariance of $H_i$ and $H_j$:
$$
G_{ij} = \mathrm{Cov}(H_i, H_j) = \langle H_i H_j \rangle - \langle H_i \rangle \langle H_j \rangle
$$}

\notes{The log-partition function $\log Z(\boldsymbol{\theta})$ acts as a cumulant generating function for the observables $H_i$. Its second derivatives yield the covariance matrix of the observables (i.e., the second cumulants correspond to variances and covariances).
This induces a natural Riemannian geometry on the parameter space. The Fisher Information Matrix $G(\boldsymbol{\theta})$ encodes local curvature and sensitivity to variations in the natural parameters $\boldsymbol{\theta}$.}

\subsection{Resolution-Constrained Fisher Information}

\notes{The Fisher Information Matrix $G(\boldsymbol{\theta})$ plays a crucial role in the resolution-constrained entropy formulation. It not only describes the local curvature of the entropy landscape but also determines which parameter components become dynamically active.}

\notes{In the context of the resolution threshold $\varepsilon$, the Fisher Information Matrix can be partitioned into components that are above and below the resolution threshold. Elements of the matrix that fall below $\varepsilon^2$ are effectively treated as zero in the dynamics, reflecting the system's inability to resolve fine-grained structure at scales smaller than the resolution threshold.}

\notes{This partitioning is directly tied to the resolution constraint on derivatives of the relative entropy. When a component of the gradient $[G(\boldsymbol{\theta})\boldsymbol{\theta}]_i$ exceeds the resolution threshold $\varepsilon$, the corresponding parameter $\theta_i$ becomes dynamically active. This creates a natural separation between active and latent parameters.}

\notes{The resolution-constrained Fisher Information Matrix provides a mathematical framework for understanding how the system's ability to resolve information determines its dynamical behavior. It shows that the emergence of structure is tied to the resolution threshold, with new variables becoming active only when their associated gradients exceed this threshold.}

\endif 
