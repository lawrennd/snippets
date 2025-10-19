\ifndef{fisherInformationGeometry}
\define{fisherInformationGeometry}

\editme

\subsection{Fisher Information as Geometry}

\notes{In the previous section, we saw that for exponential families, the Fisher information matrix appears as the second derivative of the log partition function
$$
G(\boldsymbol{\theta}) = \nabla^2 \mathcal{A}(\boldsymbol{\theta}) = \mathrm{Cov}_{\boldsymbol{\theta}}[T(\mathbf{x})].
$$
We now develop the geometric interpretation: the Fisher information matrix defines a *metric* on the space of probability distributions.}

\slides{
**From last section:**
$$
G(\boldsymbol{\theta}) = \nabla^2 \mathcal{A}(\boldsymbol{\theta}) = \mathrm{Cov}_{\boldsymbol{\theta}}[T(\mathbf{x})]
$$
* Now: What does this *mean* geometrically?
}

\subsubsection{The Statistical Manifold}

\notes{Consider the space of all probability distributions in an exponential family, parametrized by $\boldsymbol{\theta}$. This space forms a *manifold* --- a smooth, curved space where each point represents a different distribution.

The Fisher information matrix $G(\boldsymbol{\theta})$ acts as a *Riemannian metric* on this manifold. Think of measuring distances on a curved surface like a sphere: you need a metric to tell you how far apart two nearby points are. The Fisher information provides exactly this for the space of probability distributions, telling us how to measure "statistical distance" between distributions.}

\slides{
**Statistical Manifold:**
* Each point $\boldsymbol{\theta}$ = a probability distribution
* Space of all distributions = curved manifold
* Fisher information = metric (ruler) on this space
* Measures "closeness" between distributions
}

\newslide{Information Distance}

\notes{The Fisher information defines the *information distance* between nearby distributions. If we move from parameters $\boldsymbol{\theta}$ to $\boldsymbol{\theta} + \text{d}\boldsymbol{\theta}$, the infinitesimal distance in information space is
$$
\text{d}s^2 = \text{d}\boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \text{d}\boldsymbol{\theta}
$$
where the Fisher information playing the role of the metric. Larger Fisher information means a given parameter change corresponds to a larger "information distance", the distributions are more distinguishable.}

\slides{
$$
\text{d}s^2 = \text{d}\boldsymbol{\theta}^\top G(\boldsymbol{\theta}) \text{d}\boldsymbol{\theta}
$$
* Measures information distance between distributions
* Larger $G$ = distributions more distinguishable
* Smaller $G$ = distributions harder to tell apart
}

\subsubsection{Connection to Statistical Estimation}

\notes{This geometric picture connects directly to Fisher's original motivation. The *Cramér-Rao bound* states that for any unbiased estimator $\hat{\boldsymbol{\theta}}$ of parameters $\boldsymbol{\theta}$,
$$
\text{cov}(\hat{\boldsymbol{\theta}}) \succeq G^{-1}(\boldsymbol{\theta}),
$$
where $\succeq$ denotes that the left side minus the right side is positive semidefinite.

Geometrically, this means: higher Fisher information (stronger metric) implies tighter bounds on estimation. The inverse $G^{-1}$ gives the *minimum possible* covariance of any unbiased estimator, it's the fundamental limit on how well we can estimate parameters from data.}

\slides{
*Cramér-Rao Bound:*
$$
\text{cov}(\hat{\boldsymbol{\theta}}) \succeq G^{-1}(\boldsymbol{\theta})
$$
* $G^{-1}$ = best possible estimator covariance
* High $G$ → small $G^{-1}$ → tight estimation
* Low $G$ → large $G^{-1}$ → loose estimation
* Geometric picture: $G^{-1}$ is "error ellipsoid"
}

\newslide{Why This Matters for Dynamics}

\notes{The Fisher information plays two distinct but related roles:

1. **As a metric**: It defines information distance, telling us how "far apart" distributions are.

2. **In gradient flow**: Recall from the exponential family definitions that that $\nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}$. This means entropy gradient ascent in exponential families involves the Fisher information,
$$
\dot{\boldsymbol{\theta}} = \nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}.
$$

The appearance in the gradient comes from the specific structure of exponential families (where $G = \nabla^2 \mathcal{A}$). Together, they determine how the system flows through information space, with the geometry guiding the dynamics.}

\slides{
**Two Roles of Fisher Information:**
1. Metric → defines distances between distributions
2. In gradient → $\nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}$

$$
\dot{\boldsymbol{\theta}} = \nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}
$$
}

\subsection{Examples Revisited}

\newslide{Gaussian: Geometry of Covariance}

\notes{For the Gaussian distribution, we saw that $G(\boldsymbol{\theta}) = \Sigma$. This means:
- The information metric *is* the covariance matrix
- The inverse $G^{-1} = \Sigma^{-1}$ is the precision matrix

Geometrically, the information ellipsoid has the same shape as the probability ellipsoid. This direct connection between the Fisher information and covariance is special to Gaussians (and arises because we're working in natural parameters $\boldsymbol{\theta} = \Sigma^{-1}\boldsymbol{\mu}$).}

\slides{
**Gaussian:** $G(\boldsymbol{\theta}) = \Sigma$
* Information metric = covariance
* $G^{-1} = \Sigma^{-1}$ = precision  
* Information ellipsoid = probability ellipsoid
* Special to Gaussians in natural parameters
}

\newslide{Categorical: Simplex Geometry}

\notes{For a categorical distribution with $K$ outcomes, the Fisher information has a special structure. Using the natural parameters $\theta_k = \log \pi_k$, the Fisher information is
$$
G_{ij}(\boldsymbol{\theta}) = \delta_{ij}\pi_i - \pi_i\pi_j = \begin{cases}
\pi_i(1 - \pi_i) & i = j \\
-\pi_i\pi_j & i \neq j
\end{cases}
$$

This metric defines the **probability simplex geometry**. Distributions near the center of the simplex (all $\pi_k \approx 1/K$) have different local geometry than those near the corners (one $\pi_k \approx 1$). The Fisher metric captures this intrinsic curvature.}

\slides{
**Categorical:** 
$$
G_{ij} = \delta_{ij}\pi_i - \pi_i\pi_j
$$
* Defines probability simplex geometry
* Center of simplex: balanced information
* Corners: concentrated information
* Metric captures curvature
}

\subsection{Information Geometry: The Big Picture}

\notes{The Fisher information matrix is a foundational element of *information geometry*, a field that studies probability distributions using differential geometric tools. Key insights:

1. **mari's Dually Flat Structure*: Exponential families have a special property. They are "dually flat" under two different coordinate systems (natural parameters $\boldsymbol{\theta}$ and expectation parameters $\boldsymbol{\mu}$). The Fisher metric connects these.

2. *Geodesics*: The shortest path between two distributions (in the information geometry sense) is a geodesic. For exponential families, geodesics have elegant forms that will connect to our least action principles.

3. *Curvature*: The curvature of the statistical manifold (measured by the Riemann curvature tensor derived from $G$) tells us about the intrinsic structure of the family. Exponential families have *zero curvature* in a certain sense—they are "flat" manifolds.

These geometric properties will be essential when we study constrained information dynamics and emergence.}

\slides{
**Information Geometry:**
* Fisher metric → Riemannian geometry
* Exponential families → dually flat structure
* Geodesics → shortest paths between distributions
* Zero curvature → special "flat" structure
* *Key for constrained dynamics later*
}

\subsection{Why This Matters for The Inaccessible Game}

\notes{The Fisher information matrix plays three roles in our framework:

1. **Gradient Flow Metric**: It appears in the entropy gradient, determining how the system evolves through information space via $\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta}$.

2. **Information Distance**: It defines the metric for measuring statistical distinguishability between distributions.

3. **Emergence Indicator**: Changes in the structure of $G$  signal the emergence of new regimes and effective descriptions.

Understanding Fisher information as *geometry*, not just as a statistical tool, is key  for everything that follows.}

\slides{
**Three Roles in TIG:**
1. Gradient flow metric: appears in $\dot{\boldsymbol{\theta}} = -G\boldsymbol{\theta}$
2. Information distance: measures distinguishability
3. Emergence indicator: structure changes signal regimes

*Fisher information as geometry → key to everything*
}

\endif 

