\ifndef{jaynesWorldMinimalResolution}
\define{jaynesWorldMinimalResolution}
\ifndef{jaynesWorldMinimalResolution}
\define{jaynesWorldMinimalResolution}

\editme

\subsection{Remark: Resolution-Constrained Entropy and Relative Formulation}

\notes{Let $\rho$ be a density matrix over latent variables $\mathbf{m} \in \mathbb{R}^d$, with total entropy constrained by $S(\rho) \leq N $. This constraint implies a minimal resolvable scale,
$$
\varepsilon(N) \geq \frac{L}{e^{N/d}}.
$$
Structure finer than $\varepsilon(N)$ is informationally inaccessible to the system. Therefore, the density matrix must be *coarse-grained* at this scale: it cannot encode spatial variation or correlations below $\varepsilon$.}

\notes{To formalise this, we define a *resolution subspace* $\mathcal{H}_\varepsilon \subset \mathcal{H}$, such that each distinguishable state in $\mathcal{H}_\varepsilon$ is localised to a cell of size $\sim \varepsilon^d$ and the system cannot resolve structure orthogonal to $\mathcal{H}_\varepsilon$.}

\notes{Let $I_\varepsilon$ denote the identity operator on $\mathcal{H}_\varepsilon$, and define the *uniform reference state* over this subspace,
$$
\rho_0 = \frac{1}{\dim(\mathcal{H}_\varepsilon)} I_\varepsilon.
$$
Then the *physically meaningful entropy* is not the von Neumann entropy \( S(\rho) = -\mathrm{Tr}(\rho \log \rho) \), but the *relative entropy*:
$$
\boxed{
S(\rho \| \rho_0) = \mathrm{tr}(\rho \log \rho) - \mathrm{tr}(\rho \log \rho_0),
}
$$
which quantifies the information in $\rho$ *above the resolution scale* $\varepsilon$.}

\notes{This formulation accounts for the effective coarse-graining induced by entropy capacity, ensures entropy is *coordinate-invariant* and *finite* and reflects the fact that $\rho$ encodes distinguishable structure only within $\mathcal{H}_\varepsilon$.}

\endif
