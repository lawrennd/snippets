\ifndef{fisherAsConductanceTensor}
\define{fisherAsConductanceTensor}

\editme

\subsection{Fisher Information as Conductance Tensor}

\notes{In the inaccessible game, the Fisher information matrix $G(\boldsymbol{\theta})$ plays a role analogous to conductance in electrical circuits—but with differences that make the game richer than a Kirchhoff network.}

\subsubsection{The Electrical Circuit Analogy}

\notes{In a Kirchhoff electrical network, charge conservation is local and linear: $\sum_j I_{ij} = 0$ at each node, where current flows according to Ohm's law with fixed conductances:
$$
I_{ij} = g_{ij}(V_i - V_j).
$$
The conductances $g_{ij}$ are fixed parameters of the circuit. Given the conductances, the steady state can be found by solving linear equations derived from local charge conservation.}

\slides{
**Kirchhoff Networks:**
* Local charge conservation: $\sum_j I_{ij} = 0$
* Ohm's law: $I_{ij} = g_{ij}(V_i - V_j)$
* Fixed conductances $g_{ij}$
* Linear equations → steady state
}

\newslide{Information Networks are Different}

\notes{In contrast, our information conservation constraint $\sum_{i=1}^n h_i = C$ is generally *nonlocal* and *nonlinear*. Each marginal entropy $h_i$ requires marginalization over all other variables, making it a global functional of the entire state $\boldsymbol{\theta}$.}

\notes{Consider a multivariate Gaussian as an example. The marginal entropy is
$$
h_i = \frac{1}{2}\log(2\pi e \sigma_i^2)
$$
where $\sigma_i^2 = [G^{-1}]_{ii}$ is the $i$-th diagonal element of the inverse Fisher information. The conservation constraint becomes:
$$
\sum_{i=1}^n \log([G^{-1}]_{ii}) = \text{constant}.
$$}

\slides{
*Information Conservation:*
$$\sum_{i=1}^n \log([G^{-1}]_{ii}) = C$$

* **Nonlocal:** Every variable coupled through $G^{-1}$
* **Nonlinear:** Logarithm and matrix inversion
* **Global:** Changing $\theta_i$ affects all $h_j$
}

\subsubsection{Dynamic Information Topography}

\notes{Moreover, the Fisher information $G(\boldsymbol{\theta})$ itself evolves with the state. This creates a **dynamic information topography**, more analogous to memristive networks than fixed resistors.

The "conductance" for information flow is given by the Fisher information:
$$
G(\boldsymbol{\theta}) = \nabla^2 \cumulantGeneratingFunction(\boldsymbol{\theta}),
$$
which depends on the current state $\boldsymbol{\theta}$. As the system evolves, both the "voltages" (parameters $\boldsymbol{\theta}$) and the "conductances" (Fisher information $G$) change together.}

\slides{
*Dynamic Topography:*
* $G(\boldsymbol{\theta})$ changes with state
* Not fixed conductances!
* Analogous to memristive networks
* "Conductances" and "voltages" co-evolve
}

\subsection{Information Channels and Bottlenecks}

\notes{Despite the differences, the analogy provides intuition. The eigenvalues of $G(\boldsymbol{\theta})$ indicate information channel capacities:

- **Large eigenvalues:** Low-resistance channels for information flow
- **Small eigenvalues:** Bottlenecks that constrain flow
- **Eigenvectors:** Directions of easy/hard information movement}

\notes{The constrained maximum entropy production acts as a generalized Ohm's law. Information flows "downhill" in the entropy landscape, but the rate of flow is governed by the Fisher information metric. The nonlocal conservation and emergent conductance structure create a system where information reorganizes itself through the interplay between local gradient flows and global constraints.}

\slides{
**Channel Capacity:**
* Large $\lambda_i$: easy information flow
* Small $\lambda_i$: information bottlenecks
* Eigenvectors: flow directions

**Generalised Ohm's Law:**
$$\dot{\boldsymbol{\theta}} = -G(\boldsymbol{\theta})\boldsymbol{\theta} + \nu \mathbf{a}$$
}

\subsection{Why "Topography"?}

\notes{We think of $G(\boldsymbol{\theta})$ as defining the **information topography**. In geography, topography describes hills, valleys, and plains that constrain how water flows. In our framework, $G(\boldsymbol{\theta})$ describes the "shape" of the information landscape that constrains how information flows.

This formalises the metaphor from *The Atomic Human* [@Lawrence-atomic24]: "In geography, the topography is the configuration of natural and man-made features in the landscape... An information topography is similar, but instead of the movement of goods, water and people, it dictates the movement of information."}

\slides{
**Information Topography:**
* Geography: terrain shapes water flow
* Information: $G(\boldsymbol{\theta})$ shapes information flow
* Formalizes *Atomic Human* metaphor
* Mathematical teeth for intuitive concept
}

\endif

