\ifndef{saddlePoints}
\define{saddlePoints}

\editme

\subsection{Saddle Points}

\notes{Saddle points represent critical transitions in the game's evolution where the gradient $\nabla_{\boldsymbol{\theta}}S \approx 0$ but the game is not at a maximum or minimum. At these points.

1. The Fisher information matrix $G(\boldsymbol{\theta})$ has eigenvalues with significantly different magnitudes
2. Some eigenvalues approach zero, creating "critically slowed" directions in parameter space
3. Other eigenvalues remain large, allowing rapid evolution in certain directions

This creates a natural separation between "memory" variables (associated with near-zero eigenvalues) and "processing" variables (associated with large eigenvalues). The game's behavior becomes highly non-isotropic in parameter space.

At saddle points, direct gradient ascent stalls, and the game must leverage the Fourier duality between parameters and capacity variables to continue entropy production. The duality relationship
$$
c(M) = \mathcal{F}[\boldsymbol{\theta}(M)]
$$
allows the game to progress by temporarily increasing uncertainty in capacity space, which creates gradients in previously flat directions of parameter space.

These saddle points often coincide with phase transitions between parameter-dominated and capacity-dominated regimes, where the game's fundamental character changes in terms of information processing capabilities.

At saddle points, we see the first manifestation of the uncertainty principle that will be explored in more detail. The relationship between parameters and capacity variables becomes important as the game navigates these critical regions. The Fourier duality relationship
$$
c(M) = \mathcal{F}[\boldsymbol{\theta}(M)]
$$
is not just a mathematical convenience but represents a constraint on information processing that parallels emerges from uncertainty principles. The duality is essential for understanding how the game maintains both precision in parameters and sufficient capacity for information storage.

The emergence of critically slowed directions at saddle points directly leads to the formation of information reservoirs that we'll explore in depth. These reservoirs form when certain parameter combinations become effectively "frozen" due to near-zero eigenvalues in the Fisher information matrix. This natural separation of timescales creates a hierarchical memory structure that resembles biological information processing systems, where different variables operate at different temporal scales. The game's deliberate use of steepest ascent rather than natural gradient ensures these reservoirs form organically as the system evolves.}

\subsection{Saddle Point Seeking Behaviour}

\notes{In the game's evolution, we follow steepest ascent in parameter space to maximize entropy. Let's contrast with the *natural gradient* approach that is often used in information geometry.}

\notes{The steepest ascent direction in Euclidean space is given by,
$$
\Delta \boldsymbol{\theta}_{\text{steepest}} = \eta \nabla_{\boldsymbol{\theta}} S = \eta \mathbf{g}
$$
where $\eta$ is a learning rate and $\mathbf{g}$ is the entropy gradient.}

\notes{In contrast, the natural gradient adjusts the update direction according to the Fisher information geometry,
$$
\Delta \boldsymbol{\theta}_{\text{natural}} = \eta G(\boldsymbol{\theta})^{-1} \nabla_{\boldsymbol{\theta}} S = \eta G(\boldsymbol{\theta})^{-1} \mathbf{g}
$$
where $G(\boldsymbol{\theta})$ is the Fisher information matrix. This represents a Newton step in the natural parameter space. Often the Newton step is difficult to compute, but for exponential families and their entropies the Fisher information has a form closely related to the gradients and would be easy to leverage. The game *explicitly* uses steepest ascent and this leads to very different behaviour, in particular near saddle points. In this regime}

\notes{
1. *Steepest ascent* slows dramatically in directions where the gradient is small, leading to extremely slow progress along the critically slowed modes. This actually helps the game by preserving information in these modes while allowing continued evolution in other directions.

2. *Natural gradient* would normalize the updates by the Fisher information, potentially accelerating progress in critically slowed directions. This would destroy the natural emergence of information reservoirs that we desire.

The use of steepest ascent rather than natural gradient is deliberate in our game. It allows the Fisher information matrix's eigenvalue structure to directly influence the temporal dynamics, creating a natural separation of timescales that preserves information in critically slowed modes while allowing rapid evolution in others.}

\notes{As the game approaches a saddle point}

\notes{
1. The gradient $\nabla_{\boldsymbol{\theta}} S$ approaches zero in some directions but remains non-zero in others}

\notes{
2. The eigendecomposition of the Fisher information matrix $G(\boldsymbol{\theta}) = V \Lambda V^T$ reveals which directions are critically slowed}

\notes{
3. Update magnitudes in different directions become proportional to their corresponding eigenvalues}

\notes{
4. This creates the hierarchical timescale separation that forms the basis of our memory structure}

\notes{This behavior creates a computational architecture where different variables naturally assume different functional roles based on their update dynamics, without requiring explicit design. The information geometry of the parameter space, combined with steepest ascent dynamics, self-organizes the game into memory and processing components.}

\notes{The saddle point dynamics in Jaynes' World provide a  mathematical framework for understanding how the game navigates the information landscapes. The balance between fast-evolving "processing" variables and slow-evolving "memory" variables offers insights into how complexity might emerge in environments that instantaneously maximise entropy.}

\endif