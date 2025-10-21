\ifndef{gaussianRegimeMotivation}
\define{gaussianRegimeMotivation}

\editme

\subsection{Why the Gaussian Regime?}

\notes{When reviewing Lagrange multipliers we saw that computing $\nu(t)$ requires knowing the constraint gradient,
$$
a(\boldsymbol{\theta}) = \sum_{i=1}^N \nabla h_i(\boldsymbol{\theta}),
$$
where each $h_i$ is a marginal entropy. For general distributions, computing $\nabla h_i$ is a computational nightmare—it requires marginalizing over $N-1$ variables, which in worst case requires exponential computation.

**The Gaussian regime is special** 

1. **Computational tractability**: For multivariate Gaussians with covariance $\Sigma = G^{-1}$, marginal entropies have closed form:
$$
h_i = \frac{1}{2}\log(2\pi e \Sigma_{ii}) = \frac{1}{2}\log(2\pi e [G^{-1}]_{ii})
$$
The gradient can be computed by differentiating this expression with polynomial complexity rather than exponential.

2. **Physical motivation**: Gaussians are maximum entropy distributions for fixed mean and covariance. If our MEP dynamics push toward maximum entropy, they naturally lead toward Gaussian-like regimes.

3. **Laplace approximation**: Near any equilibrium point, the distribution looks approximately Gaussian. This is the essence of the Laplace approximation, a second order Taylor expansion leads to approximating a distribution by a Gaussian centered at a stationary point.

When we perturb around an equilibrium $\boldsymbol{\theta}^\ast$, we're implicitly assuming the distribution is approximately Gaussian in that neighborhood. Coincidentally this is also the regime where the constrained dynamics may be computable.}

\slides{
**Why Gaussian Regime?**

Recall from our formulation of the Lagrangian, computing $\nabla h_i$ is exponentially hard for general distributions

**In Gaussian regime:**

* Marginal entropies: $h_i = \frac{1}{2}\log(2\pi e [G^{-1}]_{ii})$
* Gradients: Polynomial complexity (differentiating closed form)
* Fisher info: $G$ becomes constant covariance inverse

**Physical motivation:**

* Gaussians = maximum entropy (fixed mean/variance)
* MEP dynamics $\rightarrow$ Gaussian-like regimes
* Laplace approximation: near equilibrium ≈ Gaussian

**For perturbation analysis:** Working near equilibrium $\equiv$ working in computable regime
}

\subsection{Laplace Approximation Connection}

\notes{The *Laplace approximation* is a standard technique for approximating integrals. The idea: if you have an integral
$$
Z = \int e^{-Nf(x)} dx
$$
for large $N$, then the integral is dominated by the neighborhood of the minimum of $f(x)$. Expanding $f(x) \approx f(x^\ast) + \frac{1}{2}(x-x^\ast)^2 f^{\prime\prime}(x^\ast)$ gives a Gaussian approximation.

In our context:
- The distribution $p(\mathbf{x}|\boldsymbol{\theta})$ is an exponential family
- Near equilibrium $\boldsymbol{\theta}^\ast$, it looks approximately Gaussian
- This justifies perturbation analysis around $\boldsymbol{\theta}^\ast$

**Key insight:** The Laplace approximation tells us *when* perturbation analysis is valid—when we're close enough to equilibrium that the distribution is approximately Gaussian.

This isn't the main technique we'll use (we'll do standard linearization), but it provides the conceptual foundation for why our analysis makes sense.}

\slides{
**Laplace Approximation (Conceptual Foundation)**

Standard technique: $\int e^{-Nf(x)} dx$ dominated by minimum of $f(x)$

**Connection to TIG:**

* Near equilibrium: distribution ≈ Gaussian
* Justifies linearization
* Tells us when perturbation valid

**Not center stage**, but explains why this works!
}

\notes{**Summary:** The Gaussian regime isn't just a convenient assumption—it's the regime where:
1. Dynamics are computable (marginal entropies tractable)
2. MEP naturally leads us (maximum entropy property)
3. Perturbation analysis is valid (Laplace approximation)

This is why we focus on linearization around equilibrium in Gaussian regimes.}

\endif

