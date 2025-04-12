\ifndef{fisherInformationMatrix}
\define{fisherInformationMatrix}

\editme

\subsection{Fisher Information Matrix}

We'll now derive the form of the Fisher Information Matrix $G(\boldsymbol{\theta})$ from the partition function:
$$
Z(\boldsymbol{\theta}) = \mathrm{tr}\left[\exp\left(\sum_i \theta_i H_i \right)\right]
$$
We'll proceed by differentiating with respect to $\theta_i$ for the expectation values, then compute the second derivative to get the Fisher Information Matrix, 
$$
G_{ij} = \frac{\partial^2 \log Z(\boldsymbol{\theta})}{ \partial \theta_i \partial \theta_j}.
$$
which we'll then link to the  curvature.

First we differentiate $\log Z(\boldsymbol{\theta})$ with respect to $\theta_i$,
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
This is the expected value of $H_i$ under the current distribution $\rho(\boldsymbol{\theta})$. 

We now compute the second derivative of $\log Z(\boldsymbol{\theta})$ to obtain the Fisher Information Matrix elements $G_{ij}$, using the definition
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
\frac{\partial \rho}{\partial \theta_j}
= \frac{\partial}{\partial \theta_j} \left( \frac{1}{Z(\boldsymbol{\theta})} \exp\left(\sum_k \theta_k H_k\right) \right)
= -\frac{1}{Z(\boldsymbol{\theta})^2} \frac{\partial Z(\boldsymbol{\theta})}{\partial \theta_j} \exp\left(\sum_k \theta_k H_k\right) + \frac{1}{Z(\boldsymbol{\theta})} \frac{\partial}{\partial \theta_j} \left( \left(\sum_k \theta_k H_k\right) \right)
$$
For the second term we use the operator identity for the exponential derivative,
$$
\frac{\partial \rho}{\partial \theta_j} = \rho \left( H_j - \langle H_j \rangle \right)
$$
giving 
$$
G_{ij} = \mathrm{tr} \left[ \rho (H_j - \langle H_j \rangle) H_i \right]
= \langle H_i H_j \rangle - \langle H_i \rangle \langle H_j \rangle
$$
so the Fisher Information Matrix is the covariance matrix,
$$
G_{ij} = \mathrm{Cov}(H_i, H_j).
$$

This reflects a structural property of the model: the log-partition function $\log Z(\boldsymbol{\theta})$ acts as a cumulant generating function for the observables $H_i$. Its second derivatives yield the covariance matrix of the observables (i.e., the second cumulants correspond to variances and covariances).
This induces a natural Riemannian geometry on the parameter space. The Fisher Information Matrix $G(\boldsymbol{\theta})$ encodes local curvature and sensitivity to variations in the natural parameters $\boldsymbol{\theta}$.

\endif 
