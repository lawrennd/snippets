\ifndef{informationTopography}
\define{informationTopography}

\editme


\subsection{Regime of Quasi-Static Latent Variables: $M$ as Information Topography}

We now focus on a specific regime of the unfolding system: the quasi-static latent phase, where a subset of latent variables $M$ evolves so slowly that they can be treated as approximately fixed over relevant timescales. In this regime, we show how the Fisher Information Matrix partitions naturally, and how the latent $M$ variables define an effective information topography for the dynamics of active variables $X$. This sets up a principled derivation of an *EPI-like variational principle* that holds conditionally over $X$, given a fixed latent structure.

\subsubsection{Fisher Information Partitioning}

Suppose the full Fisher Information Matrix $G$ is defined over natural parameters $\boldsymbol{\theta} = (\boldsymbol{\theta}_X, \boldsymbol{\theta}_M)$, corresponding to active and latent variables respectively. Then we write
$$
G =
\begin{bmatrix}
G_{XX} & G_{XM} \\
G_{MX} & G_{MM}
\end{bmatrix}
$$

Now assume the entropy gradient $G \boldsymbol{\theta}$ satisfies
$$
\left| \left[ G \boldsymbol{\theta} \right]_M \right| < \varepsilon_{\text{slow}} \ll 1
$$
i.e., curvature-induced flow along $\theta_M$ is negligible on relevant timescales.

\subsubsection{Quasi-Static Approximation: $M$ as Parameters}

Under this condition, we can fix $\theta_M \approx \theta_M^0$, and treat $G_{XM}$ and $G_{MM}$ as externally conditioned structures. Then the effective dynamics reduce to a gradient flow over $\theta_X$ with *$M$-dependent geometry*
\[
\frac{d\theta_X}{dt} \propto G_{XX}(\theta_M^0) \theta_X + G_{XM}(\theta_M^0) \theta_M^0.
$$
That is, the system evolves in the X-space under a curvature landscape \textbf{shaped} by the latent M-structure.

\subsubsection{Induced EPI-like Variational Principle}

Given this quasi-static separation, we define a reduced entropy functional
$$
S_X[\rho_X \mid \theta_M^0] := - \mathrm{tr}(\rho_X \log \rho_X)
$$
subject to constraints \textbf{conditioned} on $\theta_M^0$, including variance bounds or Fisher curvature bounds from $G_{XX}$. The corresponding variational principle is
$$
\delta \left[ S_X[\rho_X] - \sum_i \lambda_i C_i[\rho_X; \theta_M^0] \right] = 0.
$$
This defines the *conditional minimum Fisher curvature state* of $X$, given $M$ - a piecewise EPI structure.

\subsubsection{Interpretation: $M$ as Informational Topography}

\notes{In this regime, the slowly evolving latent variables $M$ do not directly participate in the entropy ascent. Instead, they shape the local curvature structure - i.e., they define an *information topography* over which the active variables evolve.}

\notes{
* $G_{XX}(\theta_M)$ is the *local metric*.
* $G_{XM}(\theta_M) \theta_M$ is an *effective force field* induced by the latent structure.
* The flow $\frac{d\theta_X}{dt}$ is a *geodesic-like ascent* on this $M$-shaped terrain.
}

\notes{EPI emerges as a *conditionally local principle*, with $M$ shaping the conditions of variation but not varying itself.}

\endif
