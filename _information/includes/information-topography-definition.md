\ifndef{informationTopographyDefinition}
\define{informationTopographyDefinition}

\editme

\subsection{Formalising Information Topography}

\notes{In *The Atomic Human* [@Lawrence-atomic24], the concept of an information topography was introduced as a metaphor: "In geography, the topography is the configuration of natural and man-made features in the landscape... These questions are framed by the topography. An information topography is similar, but instead of the movement of goods, water and people, it dictates the movement of information."}

\notes{However, no formal mathematical definition was given. The inaccessible game provides one.}

\slides{
**From Metaphor to Mathematics:**

*Atomic Human:* "Information topography" = intuitive concept

*Inaccessible Game:* Fisher information = formal definition
}

\subsection{Mathematical Definition}

\notes{We define the *information topography* of a system to be the Fisher information matrix $G(\boldsymbol{\theta})$ viewed as a Riemannian metric on the space of probability distributions.}

\notes{Formally, for an exponential family parametrised by natural parameters $\boldsymbol{\theta}$:

**Definition (Information Topography):** The information topography is the pair $(G(\boldsymbol{\theta}), \mathcal{M})$ where:
- $\mathcal{M}$ is the statistical manifold of probability distributions
- $G(\boldsymbol{\theta}) = \nabla \nabla \cumulantGeneratingFunction(\boldsymbol{\theta})$ is the Fisher information metric

This metric determines:
1. Information distances between distributions
2. Directions of information flow (geodesics)
3. Information channel capacities (eigenvalues)
4. Bottlenecks and pathways (eigenvectors)}

\slides{
**Definition:**

Information Topography = $(G(\boldsymbol{\theta}), \mathcal{M})$

where $G(\boldsymbol{\theta}) = \nabla^2\cumulantGeneratingFunction$

**Determines:**
* Distances between distributions
* Flow directions (geodesics)
* Channel capacities (eigenvalues)
* Bottlenecks (small eigenvalues)
}

\subsection{How It Constrains Information Movement}

\notes{The information topography constrains movement in three ways:

**1. Metric Structure:** The "distance" between two nearby distributions $p(\boldsymbol{\theta})$ and $p(\boldsymbol{\theta} + d\boldsymbol{\theta})$ is:
$$
ds^2 = d\boldsymbol{\theta}^\top G(\boldsymbol{\theta}) d\boldsymbol{\theta}
$$
Moving in directions corresponding to small eigenvalues of $G$ requires large parameter changes for small distributional changes—these are "narrow passes" in the information landscape.

**2. Gradient Flow:** The entropy gradient is:
$$
\nabla H = -G(\boldsymbol{\theta})\boldsymbol{\theta}
$$
Information flows "downhill" in entropy space, but the Fisher information determines the effective slope. Regions with small eigenvalues have shallow gradients—information flows slowly.

**3. Constraint Enforcement:** Under conservation $\sum h_i = C$, the constraint gradient $\mathbf{a} = \nabla(\sum h_i)$ interacts with $G$ to determine allowed flow directions. The dynamics become:
$$
\dot{\boldsymbol{\theta}} = -\Pi_\parallel G(\boldsymbol{\theta})\boldsymbol{\theta}
$$
where $\Pi_\parallel$ projects onto the constraint tangent space.}

\slides{
**Three Constraints:**

1. **Metric:** $\text{d}s^2 = \text{d}\boldsymbol{\theta}^\top G \text{d}\boldsymbol{\theta}$
   - Small eigenvalues = narrow passages

2. **Gradient:** $\nabla H = -G\boldsymbol{\theta}$  
   - Fisher info determines slope

3. **Conservation:** $\dot{\boldsymbol{\theta}} = -\Pi_\parallel G\boldsymbol{\theta}$
   - Projection onto constraint surface
}

\subsection{Dynamic Topography}

\notes{Unlike geographical topography which is static, information topography is *dynamic*, it changes as the system evolves. As $\boldsymbol{\theta}$ changes, so does $G(\boldsymbol{\theta})$. This creates a feedback loop:

1. Current topography $G(\boldsymbol{\theta})$ determines information flow
2. Flow changes parameters $\boldsymbol{\theta}$
3. New parameters change topography $G(\boldsymbol{\theta})$
4. Repeat

This dynamic restructuring is what makes information systems so rich. The landscape itself evolves as you move through it.}

\slides{
**Dynamic Evolution:**

$$\boldsymbol{\theta}(t) \rightarrow G(\boldsymbol{\theta}(t)) \rightarrow \dot{\boldsymbol{\theta}}(t) \rightarrow \boldsymbol{\theta}(t+\text{d}t)$$

* Topography shapes flow
* Flow changes state
* State reshapes topography
* *Landscape evolves as you move!*
}

\notes{This formalisation gives mathematical precision to the intuitive notion from *The Atomic Human* that information movement is constrained by structure. The Fisher information matrix *is* that structure, and the inaccessible game describes how systems evolve within it.}

\endif

