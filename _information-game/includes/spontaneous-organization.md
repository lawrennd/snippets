\ifndef{spontaneousOrganization}
\define{spontaneousOrganization}

\editme

\subsection{Spontaneous Organization Through Entropy Maximization}

\notes{For the system to 'spontaneously organise' we need to understand how mutual information evolves under our dynamics.

We're maximizing entropy in the natural parameter space $\boldsymbol{\theta}$, not directly in probability space. This distinction is crucial - while maximizing entropy in probability space would lead to independence between variables, maximizing entropy in natural parameter space can simultaneously increase both joint entropy and mutual information.

To make this notion of "organization" more concrete, we should consider:

1. Spatial or network topology - how variables are connected in some underlying structure
2. Locality of interactions - how information flows between neighboring components
3. Emergence of recognizable patterns or structures at different scales
}

\slides{
* Can entropy maximization lead to information organization
* Requires: mutual information increases despite overall entropy growth
* Would provides theoretical foundation for emergence of structure
* Needs notion of locality or topology to be fully meaningful
}

\newslide{Formal Analysis of Spontaneous Organization}

\notes{
Joint distribution over variables $Z = (X, M)$, where $M$ represents memory variables in an information reservoir (at a saddle point in the dynamics) and $X$ represents observable variables. The system evolves by maximizing entropy $S$ in the natural parameter space $\boldsymbol{\theta}$,
$$
\frac{\text{d}\boldsymbol{\theta}}{\text{d}t} = \eta \nabla_{\boldsymbol{\theta}}S[p(z,t)].
$$
To understand spontaneous organization, we need to examine how mutual information $I(X;M)$ evolves under these dynamics. We can decompose the joint entropy,
$$
S[p(z,t)] = S(X) + S(M) - I(X;M).
$$
Taking the derivative across turns,
$$
\frac{\text{d}S}{\text{d}t} = \frac{\text{d}S(X)}{\text{d}t} + \frac{\text{d}S(M)}{\text{d}t} - \frac{\text{d}I(X;M)}{\text{d}t}.
$$
}

\slides{
* Joint entropy decomposition: $S[p(z,t)] = S(X) + S(M) - I(X;M)$
* Turns derivative: $\frac{\text{d}S}{\text{d}t} = \frac{\text{d}S(X)}{\text{d}t} + \frac{\text{d}S(M)}{\text{d}t} - \frac{\text{d}I(X;M)}{\text{d}t}$
* Spontaneous organization when: $\frac{\text{d}I(X;M)}{\text{d}t} > 0$
}

\notes{
We know $\frac{\text{d}S}{\text{d}t} > 0$ (entropy is being maximized), and because $M$ are at saddle points we know that $\frac{\text{d}S(M)}{\text{d}t} \approx 0$. Therefore we can rearrange to find,
$$
\frac{\text{d}I(X;M)}{\text{d}t} \approx \frac{\text{d}S(X)}{\text{d}t}  - \frac{\text{d}S}{\text{d}t}.
$$
Spontaneous organization emerges when $\frac{\text{d}I(X;M)}{\text{d}t} > 0$, which occurs when
$$
\frac{\text{d}S(X)}{\text{d}t} > \frac{\text{d}S}{\text{d}t}.
$$
}

\subsection{Fisher Information and Multiple Timescales in Spontaneous Organization}

\notes{
We introduce the Fisher information and the effect of multiple timescales to analyze when the gradient condition $\frac{\text{d}S(X)}{\text{d}t} > \frac{\text{d}S}{\text{d}t}$ holds.}

\notes{The Fisher information matrix $G(\boldsymbol{\theta})$ provides a natural metric on the statistical manifold of probability distributions. For our joint distribution $p(z|\boldsymbol{\theta})$, the Fisher information is defined as
$$
G_{ij}(\boldsymbol{\theta}) = \mathbb{E}\left[\frac{\partial \log p(z|\boldsymbol{\theta})}{\partial \theta_i}\frac{\partial \log p(z|\boldsymbol{\theta})}{\partial \theta_j}\right].
$$}

\notes{ When we partition our variables into fast variables $X$ and slow variables $M$ (representing the information reservoir), we are suggesting a a timescale separation in the natural parameter dynamics,
$$
\frac{\text{d}\boldsymbol{\theta}_X}{\text{d}t} = \eta_X \nabla_{\boldsymbol{\theta}_X}S[p(z,t)],
$$
$$
\frac{\text{d}\boldsymbol{\theta}_M}{\text{d}t} =  \eta_M \nabla_{\boldsymbol{\theta}_M}S[p(z,t)],
$$
where $\left|\nabla_{\boldsymbol{\theta}_X}S[p(z,t)]\right| \gg \left|\nabla_{\boldsymbol{\theta}_M}S[p(z,t)]\right|$ indicates that $X$ evolves much faster than $M$.
}

\newslide{Multiple Timescales and Mutual Information Growth}

\notes{
This timescale separation reflects an asymmetry that would drive spontaneous organization. The entropy dynamics can be expressed in terms of the Fisher information matrix and the natural parameter velocities,
$$
\frac{\text{d}S}{\text{d}t} = \nabla_{\boldsymbol{\theta}}S \cdot \frac{\text{d}\boldsymbol{\theta}}{\text{d}t} = \nabla_{\boldsymbol{\theta}_X}S \cdot \frac{\text{d}\boldsymbol{\theta}_X}{\text{d}t} + \nabla_{\boldsymbol{\theta}_M}S \cdot \frac{\text{d}\boldsymbol{\theta}_M}{\text{d}t}.
$$

Substituting our gradient ascent dynamics with different learning rates:
$$
\frac{\text{d}S}{\text{d}t} = \nabla_{\boldsymbol{\theta}_X}S \cdot (\eta_X \nabla_{\boldsymbol{\theta}_X}S) + \nabla_{\boldsymbol{\theta}_M}S \cdot (\eta_M \nabla_{\boldsymbol{\theta}_M}S) = \eta_X \|\nabla_{\boldsymbol{\theta}_X}S\|^2 + \eta_M \|\nabla_{\boldsymbol{\theta}_M}S\|^2.
$$

Similarly, the marginal entropy of $X$ evolves according to,
$$
\frac{\text{d}S(X)}{\text{d}t} = \nabla_{\boldsymbol{\theta}_X}S(X) \cdot \frac{\text{d}\boldsymbol{\theta}_X}{\text{d}t} = \nabla_{\boldsymbol{\theta}_X}S(X) \cdot (\eta_X \nabla_{\boldsymbol{\theta}_X}S) = \eta_X \nabla_{\boldsymbol{\theta}_X}S(X) \cdot \nabla_{\boldsymbol{\theta}_X}S.
$$

Note that this is not generally equal to $\eta_X \|\nabla_{\boldsymbol{\theta}_X}S(X)\|^2$ unless $\nabla_{\boldsymbol{\theta}_X}S = \nabla_{\boldsymbol{\theta}_X}S(X)$, which is not typically the case when variables are correlated.

The gradient condition for spontaneous organization, $\frac{\text{d}I(X;M)}{\text{d}t} > 0$, can be rewritten using our earlier relation 
$$
\frac{\text{d}I(X;M)}{\text{d}t} \approx \frac{\text{d}S(X)}{\text{d}t} - \frac{\text{d}S}{\text{d}t},
$$ 
giving
$$
\eta_X \nabla_{\boldsymbol{\theta}_X}S(X) \cdot \nabla_{\boldsymbol{\theta}_X}S > \eta_X \|\nabla_{\boldsymbol{\theta}_X}S\|^2 + \eta_M \|\nabla_{\boldsymbol{\theta}_M}S\|^2.
$$

Since $\eta_M \|\nabla_{\boldsymbol{\theta}_M}S\|^2 > 0$ (except exactly at saddle points), this inequality requires:
$$
\nabla_{\boldsymbol{\theta}_X}S(X) \cdot \nabla_{\boldsymbol{\theta}_X}S > \|\nabla_{\boldsymbol{\theta}_X}S\|^2.
$$

This is a stronger condition than simply requiring the gradients to be aligned. By the Cauchy-Schwarz inequality, we know that $\nabla_{\boldsymbol{\theta}_X}S(X) \cdot \nabla_{\boldsymbol{\theta}_X}S \leq \|\nabla_{\boldsymbol{\theta}_X}S(X)\| \cdot \|\nabla_{\boldsymbol{\theta}_X}S\|$. Therefore, the condition can only be satisfied when $\|\nabla_{\boldsymbol{\theta}_X}S(X)\| > \|\nabla_{\boldsymbol{\theta}_X}S\|$ and the gradients are sufficiently aligned.
}

\slides{
* Fisher information: $G_{ij}(\boldsymbol{\theta}) = \mathbb{E}\left[\frac{\partial \log p(z|\boldsymbol{\theta})}{\partial \theta_i}\frac{\partial \log p(z|\boldsymbol{\theta})}{\partial \theta_j}\right]$
* Multiple timescales: $\eta_X \gg \eta_M$
* Spontaneous organization requires: $\|\nabla_{\boldsymbol{\theta}_X}S(X)\|^2 > \|\nabla_{\boldsymbol{\theta}_X}S\|^2$
}

\newslide{Condition for Information Structure Emergence}

\notes{This inequality suggests that spontaneous organization occurs when the gradient of marginal entropy $S(X)$ with respect to $\boldsymbol{\theta}_X$ has a larger magnitude than the gradient of joint entropy $S$ with respect to the same parameters.}

\notes{This condition can be satisfied when $X$ variables are strongly coupled to $M$ variables in a specific way. We express the mutual information gradient
$$
\nabla_{\boldsymbol{\theta}_X}I(X;M) = \nabla_{\boldsymbol{\theta}_X}S(X) + \nabla_{\boldsymbol{\theta}_X}S(M) - \nabla_{\boldsymbol{\theta}_X}S.
$$}

\notes{Since $M$ evolves slowly, we can approximate $\nabla_{\boldsymbol{\theta}_X}S(M) \approx 0$, yielding
$$
\nabla_{\boldsymbol{\theta}_X}I(X;M) \approx \nabla_{\boldsymbol{\theta}_X}S(X) - \nabla_{\boldsymbol{\theta}_X}S.
$$}

\notes{Our condition for spontaneous organization can be rewritten as
$$
\|\nabla_{\boldsymbol{\theta}_X}S(X)\|^2 > \|\nabla_{\boldsymbol{\theta}_X}S\|^2.
$$}

\notes{We can expand this condition using the relationship between these gradients. Since $\nabla_{\boldsymbol{\theta}_X}I(X;M) \approx \nabla_{\boldsymbol{\theta}_X}S(X) - \nabla_{\boldsymbol{\theta}_X}S$, we can write
$$
\|\nabla_{\boldsymbol{\theta}_X}S(X)\|^2 = \|\nabla_{\boldsymbol{\theta}_X}S + \nabla_{\boldsymbol{\theta}_X}I(X;M)\|^2.
$$

Expanding this squared norm we have
$$
\|\nabla_{\boldsymbol{\theta}_X}S(X)\|^2 = \|\nabla_{\boldsymbol{\theta}_X}S\|^2 + \|\nabla_{\boldsymbol{\theta}_X}I(X;M)\|^2 + 2\nabla_{\boldsymbol{\theta}_X}S \cdot \nabla_{\boldsymbol{\theta}_X}I(X;M).
$$

For our condition $\|\nabla_{\boldsymbol{\theta}_X}S(X)\|^2 > \|\nabla_{\boldsymbol{\theta}_X}S\|^2$ to be satisfied, we need
$$
\|\nabla_{\boldsymbol{\theta}_X}I(X;M)\|^2 + 2\nabla_{\boldsymbol{\theta}_X}S \cdot \nabla_{\boldsymbol{\theta}_X}I(X;M) > 0
$$

To analyze when this condition holds, we must examine the Fisher information geometry near saddle points. At a saddle point of the entropy landscape, the Hessian matrix of the entropy has both positive and negative eigenvalues. The Fisher information matrix $G(\boldsymbol{\theta})$ provides the natural metric on this statistical manifold.

Near a saddle point, the Fisher information matrix exhibits a characteristic eigenvalue spectrum with a separation between large and small eigenvalues. The eigenvectors corresponding to small eigenvalues define the slow manifold (associated with memory variables $M$), while those with large eigenvalues correspond to fast-evolving directions (associated with observable variables $X$).

The gradient of joint entropy can be decomposed into components along these eigendirections. Due to the timescale separation, the gradient components along fast directions quickly equilibrate, while components along slow directions persist. This creates a scenario where:

1. The gradient flow predominantly occurs along fast directions, with slow directions acting as constraints
2. The system explores configurations that maximize entropy subject to these constraints

Under these conditions, the dot product $\nabla_{\boldsymbol{\theta}_X}S \cdot \nabla_{\boldsymbol{\theta}_X}I(X;M)$ can become positive when the entropy gradient aligns with directions that increase mutual information. This alignment is not random but emerges deterministically in specific regions of the parameter space, particularly near saddle points where the eigenvalue spectrum of the Fisher information matrix exhibits a clear separation between fast and slow modes. As the system evolves toward these saddle points, it naturally enters configurations where the alignment condition is satisfied due to the geometric properties of the entropy landscape.

This  analysis  identifies the conditions under which spontaneous organisation becomes possible within the framework of entropy maximization in natural parameter space. The key insight is that the geometry of the Fisher information near saddle points creates regions where entropy maximization and mutual information may occur simultaneously.
}

\slides{
* Mutual information gradient: $\nabla_{\boldsymbol{\theta}_X}I(X;M) \approx \nabla_{\boldsymbol{\theta}_X}S(X) - \nabla_{\boldsymbol{\theta}_X}S$
* Organization emerges when entropy gradients diverge in direction
* Fast variables $X$ explore state space while slow variables $M$ capture persistent patterns
}

\newslide{Adiabatic Elimination and Effective Dynamics}

\notes{
This timescale separation enables an adiabatic elimination process where fast variables $X$ reach a quasi-equilibrium for each slow configuration of $M$. This creates effective dynamics where $M$ adapts to encode statistical regularities in the behavior of $X$.

Mathematically, we can express this using the Hessian matrices,
$$
\mathbf{H}_X = \frac{\partial^2 S}{\partial \boldsymbol{\theta}_X \partial \boldsymbol{\theta}_X},
$$
$$
\mathbf{H}_{XM} = \frac{\partial^2 S}{\partial \boldsymbol{\theta}_X \partial \boldsymbol{\theta}_M}.
$$

The condition for spontaneous organization becomes
$$
\frac{\text{d}I(X;M)}{\text{d}t} \approx \eta_X \text{tr}(\mathbf{H}_{S(X)}) - \eta_X \text{tr}(\mathbf{H}_S) - \eta_M \text{tr}(\mathbf{H}_{XM}) = -\eta_M \text{tr}(\mathbf{H}_{XM}).
$$

This approximation is valid when the system has reached a quasi-equilibrium state for the fast variables $X$, where $\nabla_{\boldsymbol{\theta}_X}S \approx \nabla_{\boldsymbol{\theta}_X}S(X)$. In this regime, the first two terms approximately cancel out, leaving the cross-correlation term dominant. Here, $\mathbf{H}_{S(X)}$ is the Hessian of the marginal entropy $S(X)$ with respect to $\boldsymbol{\theta}_X$, $\mathbf{H}_S$ is the Hessian of the joint entropy, and $\mathbf{H}_{XM}$ is the cross-correlation Hessian measuring how changes in $\boldsymbol{\theta}_X$ affect gradients with respect to $\boldsymbol{\theta}_M$.

Thus, mutual information increases when $\text{tr}(\mathbf{H}_{XM}) < 0$, which occurs when the cross-correlation Hessian between $X$ and $M$ has predominantly negative eigenvalues. This represents configurations where joint entropy increases more efficiently by strengthening correlations rather than breaking them.

This provides a precise mathematical characterization of when spontaneous organization emerges from entropy maximization in natural parameter space under multiple timescales.
}

\slides{
* Adiabatic elimination: fast variables reach quasi-equilibrium for each slow configuration
* Condition: $\frac{\text{d}I(X;M)}{\text{d}t} \approx -\eta_M \text{tr}(\mathbf{H}_{XM})$
* Organization occurs when $\text{tr}(\mathbf{H}_{XM}) < 0$
* System develops correlations that maximize entropy efficiently
}


\endif
