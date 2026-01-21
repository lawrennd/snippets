\ifndef{exponentialFamilies}
\define{exponentialFamilies}

\editme

\subsection{Exponential Families}

\notes{The exponential family is a class of probability distributions that plays a central role in information theory and statistical mechanics. For our purposes, these distributions have particularly elegant properties when we work with their *natural parameters*.}

\slides{
* Exponential families: cornerstone of information theory
* Natural parameters give us clean geometry
* Connects probability, entropy, and Fisher information
}

\subsubsection{Definition}

\notes{A probability distribution belongs to the exponential family if it can be written in the form
$$
p(\mathbf{x} | \boldsymbol{\theta}) = \exp\left(\boldsymbol{\theta}^\top T(\mathbf{x}) - \mathcal{A}(\boldsymbol{\theta})\right) h(\mathbf{x}),
$$
where
- $\boldsymbol{\theta} \in \mathbb{R}^d$ are the **natural parameters**
- $T(\mathbf{x})$ are the **sufficient statistics**  
- $\mathcal{A}(\boldsymbol{\theta})$ is the **log partition function** (ensures normalization)
- $h(\mathbf{x})$ is the **base measure** (often constant)
}

\slides{
$$
p(\mathbf{x} | \boldsymbol{\theta}) = \exp\left(\boldsymbol{\theta}^\top T(\mathbf{x}) - \mathcal{A}(\boldsymbol{\theta})\right) h(\mathbf{x})
$$
* $\boldsymbol{\theta}$: natural parameters
* $T(\mathbf{x})$: sufficient statistics
* $\mathcal{A}(\boldsymbol{\theta})$: log partition function
* $h(\mathbf{x})$: base measure
}

\newslide{Why "Natural" Parameters?}

\notes{The natural parameters are called "natural" because they appear linearly in the exponent. This parametrization has special geometric properties that make information-theoretic calculations particularly clean. As we'll see, working with these connections makes the connections between probability theory and geometry particularly clean.}

\slides{
* Natural parameters appear linearly in exponent
* Special geometric properties
* Clean connection to Fisher information
* Simplifies entropy calculations
}

\subsubsection{The Log Partition Function as Cumulant Generator}

\notes{The setup of the exponential family ensures that the log partition function operates as a cumulant generating function. We denote it by $\mathcal{A}(\boldsymbol{\theta})$ and it ensures the distribution is normalised.
$$
\mathcal{A}(\boldsymbol{\theta}) = \log \int \exp\left(\boldsymbol{\theta}^\top T(\mathbf{x})\right) h(\mathbf{x}) \, d\mathbf{x}.
$$
But $\mathcal{A}$'s role as cumulant generating function also means that we can compute the distributions cumulants through taking its derivatives.}
\slides{}
$$
\mathcal{A}(\boldsymbol{\theta}) = \log \int \exp\left(\boldsymbol{\theta}^\top T(\mathbf{x})\right) h(\mathbf{x}) \, d\mathbf{x}
$$}

\newslide{Cumulants from Derivatives}

\notes{The derivatives of $\mathcal{A}$ with respect to $\boldsymbol{\theta}$ give us the cumulants as follows.
- **First derivative** (first cumulant): $\nabla \mathcal{A}(\boldsymbol{\theta}) = \mathbb{E}[T(\mathbf{x})]$ (the mean)
- **Second derivative** (second cumulant): $\nabla^2 \mathcal{A}(\boldsymbol{\theta}) = \mathrm{Cov}[T(\mathbf{x})]$ (the covariance)
- **Higher derivatives**: Third and higher cumulants (skewness, kurtosis, etc.)
}

\slides{
* $\nabla \mathcal{A}(\boldsymbol{\theta}) = \mathbb{E}[T(\mathbf{x})]$ (mean)
* $\nabla^2 \mathcal{A}(\boldsymbol{\theta}) = \mathrm{Cov}[T(\mathbf{x})]$ (covariance)
* Higher derivatives give higher cumulants
}

\subsubsection{Connection to Fisher Information}

\notes{For an exponential family, the second derivative of the log partition function has a special meaning. It is the **Fisher information matrix**:
$$
G(\boldsymbol{\theta}) = \nabla^2 \mathcal{A}(\boldsymbol{\theta}) = \mathrm{Cov}_{\boldsymbol{\theta}}[T(\mathbf{x})].
$$
R.A. Fisher introduced this quantity in the context of statistical estimation. Through the Cramér-Rao bound, Fisher information tells us how accurately we can estimate parameters from data, higher Fisher information means better estimation is possible. 

The Fisher information is both the Hessian of the log partition function *and* the covariance of the sufficient statistics. This dual role arises from the log partition function being the cumulant generating function. As we'll see in the next section, the Fisher information matrix also defines the geometry of the information space.}

\slides{
$$
G(\boldsymbol{\theta}) = \nabla^2 \mathcal{A}(\boldsymbol{\theta}) = \mathrm{Cov}_{\boldsymbol{\theta}}[T(\mathbf{x})]
$$
* R.A. Fisher: bounds estimation accuracy (Cramér-Rao)
* Fisher information = Hessian of $\mathcal{A}$
* Fisher information = Covariance of sufficient statistics
* Defines geometry of information space
* *More details in next section*
}

\subsubsection{Entropy in Natural Coordinates}

\notes{The joint entropy of an exponential family distribution has a straightforward form in natural coordinates,
$$
H(\boldsymbol{\theta}) = -\mathbb{E}_{\boldsymbol{\theta}}[\log p(\mathbf{x}|\boldsymbol{\theta})] = \mathcal{A}(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \nabla \mathcal{A}(\boldsymbol{\theta}) - \mathbb{E}[\log h(\mathbf{x})].
$$
When the base measure $h(\mathbf{x})$ is constant (or when we measure entropy relative to it), this simplifies to
$$
H(\boldsymbol{\theta}) = \mathcal{A}(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \boldsymbol{\mu},
$$
where $\boldsymbol{\mu} = \nabla \mathcal{A}(\boldsymbol{\theta})$ is the mean of the sufficient statistics.}

\slides{
$$
H(\boldsymbol{\theta}) = \mathcal{A}(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \boldsymbol{\mu}
$$
where $\boldsymbol{\mu} = \nabla \mathcal{A}(\boldsymbol{\theta})$
}

\newslide{Why Natural Parameters?}

\notes{Now we see the utilty of representing through natural parameers, when we take the gradient of entropy with respect to the natural parameters, many terms cancel,
$$
\nabla_{\boldsymbol{\theta}} H = \nabla \mathcal{A}(\boldsymbol{\theta}) - \left(\boldsymbol{\theta}^\top \nabla^2 \mathcal{A} + \nabla \mathcal{A}\right) = -\boldsymbol{\theta}^\top \nabla^2 \mathcal{A} = -G(\boldsymbol{\theta})\boldsymbol{\theta}.
$$
This simple form for the entropy gradient equals negative Fisher information times natural parameters.}

\slides{
$$
\nabla_{\boldsymbol{\theta}} H = -G(\boldsymbol{\theta})\boldsymbol{\theta}
$$
* **Key result** for information dynamics
* Terms involving $\nabla \mathcal{A}$ cancel
* Fisher information connects geometry to dynamics
}

\subsection{Example: Multivariate Gaussian}

\notes{Let's make this concrete with the multivariate Gaussian distribution. A Gaussian with mean $\boldsymbol{\mu}$ and covariance $\Sigma$ can be written as:
$$
p(\mathbf{x}) = \frac{1}{(2\pi)^{d/2}|\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top\Sigma^{-1}(\mathbf{x}-\boldsymbol{\mu})\right).
$$
To put this in exponential family form, we need to identify the natural parameters and sufficient statistics.}

\subsubsection{Gaussian in Exponential Family Form}

\notes{After expanding the quadratic form and collecting terms, the Gaussian becomes:
$$
p(\mathbf{x}) = \exp\left(\boldsymbol{\theta}^\top T(\mathbf{x}) - \mathcal{A}(\boldsymbol{\theta})\right) \cdot \frac{1}{(2\pi)^{d/2}},
$$
where:
- Natural parameters: $\boldsymbol{\theta} = \Sigma^{-1}\boldsymbol{\mu}$ (precision-weighted mean)
- Sufficient statistics: $T(\mathbf{x}) = \mathbf{x}$ (the data itself)
- Log partition function: $\mathcal{A}(\boldsymbol{\theta}) = \frac{1}{2}\boldsymbol{\theta}^\top\Sigma\boldsymbol{\theta} + \frac{1}{2}\log|\Sigma|$
}

\slides{
**Gaussian as exponential family:**
* $\boldsymbol{\theta} = \Sigma^{-1}\boldsymbol{\mu}$ (natural parameters)
* $T(\mathbf{x}) = \mathbf{x}$ (sufficient statistics)
* $\mathcal{A}(\boldsymbol{\theta}) = \frac{1}{2}\boldsymbol{\theta}^\top\Sigma\boldsymbol{\theta} + \frac{1}{2}\log|\Sigma|$
}

\newslide{Fisher Information for Gaussian}

\notes{For the Gaussian, we can compute the Fisher information matrix directly:
$$
G(\boldsymbol{\theta}) = \nabla^2 \mathcal{A}(\boldsymbol{\theta}) = \Sigma.
$$
As expected, because the log partition is the covariance matrix. Equivalently, $G^{-1} = \Sigma^{-1}$ is the precision matrix. 

This reveals the intuition behind Fisher's original concept:
- Low variance (high precision) → high Fisher information → parameters easier to estimate (tighter Cramér-Rao bound)
- High variance (low precision) → low Fisher information → parameters harder to estimate (looser bound)
}

\slides{
$$
G(\boldsymbol{\theta}) = \Sigma
$$
* Fisher information = covariance
* $G^{-1} = \Sigma^{-1}$ = precision
* High variance → low Fisher info → harder estimation (looser Cramér-Rao)
* Low variance → high Fisher info → easier estimation (tighter Cramér-Rao)
}

\subsection{Example: Categorical Distribution}

\notes{Consider a categorical distribution over $K$ outcomes with probabilities $\{\pi_1, \ldots, \pi_K\}$ where $\sum_k \pi_k = 1$. We represent an outcome as a one-hot vector $\mathbf{x} \in \{0,1\}^K$ where exactly one component is 1.}

\subsubsection{Categorical in Exponential Family Form}

\notes{The categorical distribution is:
$$
p(\mathbf{x}) = \prod_{k=1}^K \pi_k^{x_k} = \exp\left(\sum_{k=1}^K x_k \log \pi_k\right).
$$
In exponential family form (using $K-1$ natural parameters due to the sum-to-one constraint):
- Natural parameters: $\boldsymbol{\theta} = (\log \pi_1, \ldots, \log \pi_{K-1})$ (log probabilities)
- Sufficient statistics: $T(\mathbf{x}) = (x_1, \ldots, x_{K-1})$ (one-hot encoding)
- Log partition function: $\mathcal{A}(\boldsymbol{\theta}) = \log\left(\sum_{k=1}^{K-1} e^{\theta_k} + 1\right)$ (log-sum-exp)
}

\slides{
**Categorical distribution:**
* $\boldsymbol{\theta} = (\log \pi_1, \ldots, \log \pi_{K-1})$
* $T(\mathbf{x}) = (x_1, \ldots, x_{K-1})$ (one-hot)
* $\mathcal{A}(\boldsymbol{\theta}) = \log\left(\sum_{k=1}^{K-1} e^{\theta_k} + 1\right)$
}

\newslide{Fisher Information for Categorical}

\notes{The Fisher information matrix for the categorical distribution is:
$$
G_{ij}(\boldsymbol{\theta}) = \begin{cases}
\pi_i(1-\pi_i) & \text{if } i=j \\
-\pi_i\pi_j & \text{if } i \neq j
\end{cases}
$$
This matrix encodes how "information" is distributed across categories. When one category dominates ($\pi_i \approx 1$), the Fisher information about other categories becomes small—it's hard to learn about rare events!}

\slides{
$$
G_{ij} = \begin{cases}
\pi_i(1-\pi_i) & i=j \\
-\pi_i\pi_j & i \neq j
\end{cases}
$$
* Rare categories → low Fisher info
* Uniform distribution → balanced information
}

\subsection{Why Exponential Families Matter}

\notes{Exponential families are not just mathematically convenient, they emerge naturally from underlying principles:

1. **Maximum Entropy**: Given constraints on the moments of a distribution, the maximum entropy distribution is in the exponential family [@Jaynes-information57].

2. **Information Geometry**: The natural parameters define a coordinate system on the manifold of probability distributions where the Fisher information acts as a Riemannian metric [@Amari-information16].

3. **Sufficient Statistics**: The sufficient statistics $T(\mathbf{x})$ capture all the information in the data needed to estimate $\boldsymbol{\theta}$, nothing is lost by summarizing data through $T$.

4. **Computational Tractability**: Many operations (computing gradients, conjugate priors, message passing) have closed-form solutions.

For the inaccessible game, exponential families provide the setting where information dynamics have their cleanest mathematical form.}

\slides{
**Why exponential families matter:**
* Emerge from maximum entropy principles
* Define information geometry
* Sufficient statistics capture all information
* Computationally tractable
* **Clean form for information dynamics**
}

\subsection{Looking Ahead}

\notes{We'll see that the form $\nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}$ is crucial for deriving the dynamics of the inaccessible game. The natural parameters will be our coordinates, the Fisher information will be our "information topography," and entropy gradients will drive the system's evolution.}

\slides{
**Next steps:**
* Natural parameters → coordinate system
* Fisher information → information topography  
* Entropy gradients → drive dynamics
* $\nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}$ → key to everything
}
\endif
