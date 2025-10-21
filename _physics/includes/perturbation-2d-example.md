\ifndef{perturbation2dExample}
\define{perturbation2dExample}

\editme

\subsection{Worked Example: Two Binary Variables}

\notes{To make the perturbation analysis concrete, let's use the simplest possible system: two binary variables $X_1, X_2 \in \{0,1\}$.

**Why this example?** 
- Small enough to compute everything explicitly
- Rich enough to show equilibria, perturbations, and stability

**Setup:** The joint distribution has four probabilities:
$$
\begin{array}{c|cc}
 & X_2=0 & X_2=1 \\
\hline
X_1=0 & p_{00} & p_{01} \\
X_1=1 & p_{10} & p_{11}
\end{array}
$$

In exponential family form (with baseline at $p_{00}$):
$$
p(x_1, x_2) = \exp(\theta_1 x_1 + \theta_2 x_2 + \theta_{12} x_1 x_2 - \psi(\boldsymbol{\theta}))
$$
where $\boldsymbol{\theta} = (\theta_1, \theta_2, \theta_{12})^\top$ are the natural parameters and $\psi(\boldsymbol{\theta})$ is the log partition function:
$$
\psi(\boldsymbol{\theta}) = \log(1 + e^{\theta_1} + e^{\theta_2} + e^{\theta_1+\theta_2+\theta_{12}})
$$

The marginal distributions are
$$
p_1(x_1) = \sum_{x_2} p(x_1,x_2), \quad p_2(x_2) = \sum_{x_1} p(x_1,x_2)
$$
and the marginal entropies are
$$
h_1 = -\sum_{x_1} p_1(x_1)\log p_1(x_1), \quad h_2 = -\sum_{x_2} p_2(x_2)\log p_2(x_2).
$$

**Conservation constraint:** $h_1 + h_2 = C$ (constant).}

\slides{
**Two Binary Variables**

Joint distribution: $X_1, X_2 \in \{0,1\}$

Natural parameters: $\boldsymbol{\theta} = (\theta_1, \theta_2, \theta_{12})$

**Exponential family:**
$$
p(x_1,x_2) = \exp(\theta_1 x_1 + \theta_2 x_2 + \theta_{12} x_1 x_2 - \psi(\boldsymbol{\theta}))
$$

Marginal entropies: $h_i = -\sum_{x_i} p_i(x_i)\log p_i(x_i)$

Constraint: $h_1 + h_2 = C$
}

\subsection{Finding an Equilibrium: The Independent Case}

\notes{**Independence equilibrium:** When $\theta_{12} = 0$, the variables are independent. By symmetry, consider $\theta_1 = \theta_2 = \theta^\ast$.

At this point
$$
p(x_1, x_2) = p_1(x_1) p_2(x_2)
$$
where each marginal is
$$
p_1(0) = \frac{1}{1+e^{\theta^\ast}}, \quad p_1(1) = \frac{e^{\theta^\ast}}{1+e^{\theta^\ast}}.
$$
The marginal entropy (same for both) is:
$$
h_1 = h_2 = -\frac{1}{1+e^{\theta^\ast}}\log\frac{1}{1+e^{\theta^\ast}} - \frac{e^{\theta^\ast}}{1+e^{\theta^\ast}}\log\frac{e^{\theta^\ast}}{1+e^{\theta^\ast}}.
$$

At $\theta^\ast = 0$ (uniform marginals): $p_1(0) = p_1(1) = 1/2$, so $h_1 = h_2 = \log 2$ and $C = 2\log 2$.

**Is this an equilibrium?** We need to check if there exists $\nu^\ast$ such that:
$$
G(\boldsymbol{\theta}^\ast)\boldsymbol{\theta}^\ast + \nu^\ast a(\boldsymbol{\theta}^\ast) = 0
$$
At independence with $\boldsymbol{\theta}^\ast = (0, 0, 0)$:
- The Fisher information matrix $G$ is the covariance of $(X_1, X_2, X_1 X_2)$ under the uniform distribution
- The constraint gradient $a = \nabla(h_1 + h_2)$ can be computed from the marginal entropy formulas
- By symmetry, $a = (a_1, a_1, 0)$ for some $a_1 < 0$ (since increasing $\theta_i$ decreases entropy from maximum)

Since $\boldsymbol{\theta}^\ast = 0$, the equilibrium condition $G\boldsymbol{\theta}^\ast + \nu^\ast a = 0$ becomes $\nu^\ast a = 0$. For generic $a \neq 0$, this requires $\nu^\ast = 0$.

This means *maximum entropy (independence) is an equilibrium* when the constraint allows it.}

\slides{
**Independence Equilibrium**

$\theta_{12} = 0$, $\theta_1 = \theta_2 = 0$ (symmetric)

**Properties:**
* Independent: $p(x_1,x_2) = p_1(x_1)p_2(x_2)$
* Uniform marginals: $p_i(0) = p_i(1) = 1/2$
* Maximum entropy: $h_1 = h_2 = \log 2$
* Multi-information: $I = 0$

**Equilibrium:** $\nu^\ast = 0$ (no constraint force needed)
}

\subsection{Computing the Fisher Information Matrix}

\notes{At the independence equilibrium $\boldsymbol{\theta}^\ast = (0, 0, 0)$, the Fisher information matrix is
$$
G(\boldsymbol{\theta}^\ast) = \text{Cov}_{p^\ast}[\boldsymbol{\phi}(X)]
$$
where $\boldsymbol{\phi}(x_1, x_2) = (x_1, x_2, x_1 x_2)^\top$ are the sufficient statistics.

Under the uniform distribution (all four outcomes equally likely with probability 1/4):
$$
G = \begin{pmatrix}
1/4 & 1/4 & 1/16 \\
1/4 & 1/4 & 1/16 \\
1/16 & 1/16 & 1/16
\end{pmatrix} - \begin{pmatrix}
1/4 \\
1/4 \\
1/16
\end{pmatrix}\begin{pmatrix}
1/4 & 1/4 & 1/16
\end{pmatrix}
$$

Computing: $\mathbb{E}[X_i] = 1/2$, $\mathbb{E}[X_1 X_2] = 1/4$ (at independence).

Working through the covariance calculation
$$
G = \begin{pmatrix}
1/4 & 0 & 1/8 \\
0 & 1/4 & 1/8 \\
1/8 & 1/8 & 3/16
\end{pmatrix}
$$

Notice:
- By symmetry: $G_{12} = 0$ (main effects uncorrelated)
- But: $G_{13} = G_{23} = 1/8 \neq 0$ (interaction couples to main effects)
- This coupling is crucial for how perturbations evolve}

\slides{
**Fisher Information at Equilibrium**

At $\boldsymbol{\theta}^\ast = (0,0,0)$ (uniform distribution):

$$
G = \begin{pmatrix}
1/4 & 0 & 1/8 \\
0 & 1/4 & 1/8 \\
1/8 & 1/8 & 3/16
\end{pmatrix}
$$

* Symmetric: $G_{12} = 0$ (main effects uncorrelated)
* Coupled: $G_{13}, G_{23} \neq 0$ (interaction couples to main effects)
* Positive definite (all eigenvalues positive)
}

\subsection{Perturbations and the Linearisation Matrix}

\notes{Now consider perturbations $q = \boldsymbol{\theta} - \boldsymbol{\theta}^\ast$ around the independent equilibrium. The linearised dynamics are
$$
\dot{q} = M q,
$$
where
$$
M = -G - \nu^\ast A + \frac{a a^\top G}{\|a\|^2}.
$$

**What does each term mean in our example?**

1. **$-G$ term**: The unconstrained entropy gradient. Since $G$ is positive definite, $-G$ has negative eigenvalues. This pushes the system toward $\boldsymbol{\theta} = 0$ (maximum entropy).

2. **$-\nu^\ast A$ term**: At our equilibrium, $\nu^\ast = 0$, so this term vanishes! The constraint is "slack"—we're at maximum entropy and the constraint doesn't need to "push back."

3. **$\frac{aa^\top G}{\|a\|^2}$ term**: This projects dynamics onto the constraint manifold. Even though $\nu^\ast = 0$, we still need to maintain $h_1 + h_2 = C$ as we perturb.

For our case, since $\nu^\ast = 0$
$$
M = -G + \frac{a a^\top G}{\|a\|^2}.
$$

**What happens to perturbations?**

- **Perturb $\theta_1$ or $\theta_2$** (break symmetry): These directions change marginal entropies. The constraint projection modifies the pure entropy gradient to keep $h_1 + h_2$ constant.

- **Perturb $\theta_{12}$ (add correlation)**: This creates mutual information ($I > 0$) while keeping marginal entropies roughly constant (to first order). However, through the Fisher coupling ($G_{13}, G_{23} \neq 0$), this perturbation also affects the main effect parameters.

The eigenvalues of $M$ determine stability and relaxation rates. For this equilibrium at maximum entropy, perturbations decay back to independence—the system is stable.}

\slides{
**Linearisation Matrix Structure**

At $\boldsymbol{\theta}^\ast = (0,0,0)$ with $\nu^\ast = 0$
$$
M = -G + \frac{a a^\top G}{\|a\|^2}.
$$

**Three terms:**
* $-G$: Entropy gradient (toward maximum)
* $-\nu^\ast A = 0$: No constraint force needed
* $\frac{aa^\top G}{\|a\|^2}$: Maintain $h_1 + h_2 = C$

**Perturbation behavior:**
* Main effects ($\theta_1, \theta_2$): Projected by constraint
* Interaction ($\theta_{12}$): Coupled via Fisher matrix, decays to zero
* All perturbations stable (decay back to maximum entropy)
}

\subsection{Physical Intuition}

\notes{This discrete example illustrates key features of constrained information dynamics:

**At maximum entropy equilibrium** ($\nu = 0$):
- The system is at the "top of the hill" (maximum $H$)
- Constraint is satisfied without needing force ($\nu = 0$)
- Small perturbations decay back (stable equilibrium)

**If we had tighter constraint** (smaller $C$):
- Could not achieve independence and maximum $H$
- Would need $\nu > 0$ (constraint pushes away from maximum entropy)
- Equilibrium would have $I > 0$ (some correlation required)
- The $-\nu A$ term would become important

**Key insights from perturbation analysis:**
1. Eigenvalues of $M$ → stability and relaxation rates
2. Eigenvectors of $M$ → normal modes (how perturbations evolve)
3. Structure depends on equilibrium ($\nu$ value) and constraint geometry ($A$ matrix)

**Contrast with Gaussian regime:**
- Discrete: Finite parameter space, explicit computation
- Gaussian: Continuous, computable marginals, same structure for $M$
- Both show: $M = -G - \nu A + \frac{aa^\top G}{\|a\|^2}$

The beauty is that this structure is universal—it emerges from the constrained MEP dynamics regardless of the specific distribution family.}

\slides{
**Physical Picture**

At maximum entropy ($\nu = 0$):
* Top of entropy "hill"
* Perturbations decay
* No constraint force

With tight constraint ($\nu > 0$):
* Must have correlation ($I > 0$)
* Constraint curvature matters ($A$ term)
* Equilibrium away from maximum entropy

**Key lesson:** Structure of $M$ reveals:
* Stability
* Relaxation rates
* Role of constraint geometry

**Universal structure** across distribution families!
}

\notes{**Looking ahead to Lecture 7:** The GENERIC decomposition $M = S + A$ applies to the linearisation at any point on the constraint manifold, not just equilibria. For this binary system, both $G(\boldsymbol{\theta})$ and the constraint gradient $a(\boldsymbol{\theta})$ vary with position, so the local structure of the decomposition changes across parameter space. The balance between dissipative ($S$) and conservative ($A$) components depends on the local geometry and the tightness of constraints at each point.}

\notes{**Summary:** This discrete example demonstrates all the key elements of perturbation analysis—equilibria, Fisher information, linearisation matrix, and the interplay between entropy gradient and constraint geometry—in a fully computable setting. The same principles apply to continuous systems, but with the Gaussian approximation marginal entropies become tractable.}

\endif

