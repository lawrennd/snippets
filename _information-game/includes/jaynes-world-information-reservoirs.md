\ifndef{informationReservoirs}
\define{informationReservoirs}

\editme

\subsection{Information Reservoirs}


\notes{The uncertainty principle means that the game can exhibit quantum-like information processing regimes during evolution.}

\notes{At minimal entropy states near the origin, the information reservoir has characteristics reminiscent of quantum systems.}

\notes{
1. *Wave-like information encoding*: The information reservoir near the origin necessarily encodes information in distributed, interference-capable patterns due to the uncertainty principle between parameters $\boldsymbol{\theta}(M)$ and capacity variables $c(M)$.}

\notes{
2. *Non-local correlations*: Parameters are highly correlated through the Fisher information matrix, creating structures where information is stored in relationships rather than individual variables.
}

\notes{
3. *Uncertainty-saturated regime*: The uncertainty relationship $\Delta\boldsymbol{\theta}(M) \cdot \Delta c(M) \geq k$ is nearly saturated (approaches equality), similar to Heisenberg's uncertainty principle in quantum systems.}

\notes{As the system evolves towards higher entropy states, a transition occurs where some variables exhibit classical behavior.}

\notes{
1. *From wave-like to particle-like*: Variables transitioning from $M$ to $X$ shift from storing information in interference patterns to storing it in definite values with statistical uncertainty.
}

\notes{
2. *Decoherence-like process*: The uncertainty product $\Delta\boldsymbol{\theta}(M) \cdot \Delta c(M)$ for these variables grows significantly larger than the minimum value $k$, indicating a departure from quantum-like behavior.
}

\notes{
3. *Local information encoding*: Information becomes increasingly encoded in local variables rather than distributed correlations.}

\notes{The saddle points in our entropy landscape mark critical transitions between quantum-like and classical information processing regimes. Near these points}  

\notes{
1. The critically slowed modes maintain quantum-like characteristics, functioning as coherent memory that preserves information through interference patterns.
}

\notes{
2. The rapidly evolving modes exhibit classical characteristics, functioning as incoherent processors that manipulate information through statistical operations.
}

\notes{
3. This natural separation creates a hybrid computational architecture where quantum-like memory interfaces with classical-like processing.}

\subsection{Classical Hierarchical Memory Structure}

\notes{As the system evolves further toward higher entropy, a purely classical hierarchical memory structure can emerge. Unlike quantum-like reservoirs that rely on interference patterns and non-local correlations, classical information reservoirs in our system organize hierarchically:}

\notes{
1. *Timescale Hierarchy*: Variables separate into distinct timescale bands based on eigenvalues of the Fisher information matrix. Slower-changing variables (smaller eigenvalues) act as context for faster-changing variables (larger eigenvalues), creating a natural temporal hierarchy.

2. *Markov Blanket Formation*: Groups of variables form statistical "shields" or Markov blankets that conditionally separate one part of the system from another. This creates modular information processing units with relative statistical independence.

3. *Mean-Field Dynamics*: Fast variables respond to the average or "mean field" of slow variables, while slow variables integrate the statistics of fast variables. This two-way coupling creates stable hierarchical processing without requiring quantum coherence.

4. *Scale-Free Organization*: The hierarchical structure often exhibits scale-free properties, with similar statistical relationships appearing across different scales of organization. This enables efficient information compression and retrieval.}

\notes{This classical hierarchical structure might be evident in systems with many variables and complex parameter spaces. It would emerge alongside the formation of conditional independence structures,}
$$
p(X|M) \approx \prod_i p(X_i|M_{\text{pa}(i)})
$$
\notes{Here $M_{\text{pa}(i)}$ represents the "parent" memory variables in the hierarchy that directly influence $X_i$. This factorization of the joint distribution reflects the emergence of causal hierarchies that enable efficient classical information processing.}

\notes{Such a hierarchical memory structure would maintains high information capacity through multiplexing across timescales rather than through quantum-like uncertainty relations. Variables at different levels of the hierarchy would simultaneously encode different aspects of information.}

\notes{
1. *Slow variables*: Encode stable, context-like information (akin to semantic memory)
2. *Intermediate variables*: Encode relationships and transformations (akin to episodic memory)
3. *Fast variables*: Encode immediate state information (akin to working memory)}

\notes{This classical hierarchical structure provides a powerful information processing architecture that emerges naturally from entropy maximization, without requiring quantum effects. Complex, efficient memory systems can develop purely through classical statistical mechanics when operating far from the minimal entropy regime.}

\notes{The moment generating function $M_Z(t)$ still provides the diagnostic: classical hierarchical systems show distinct factorization patterns in the MGF that reflect the conditional independence structure, with each level of the hierarchy contributing characteristic timescales to the overall dynamics.}

\subsection{Variable Transitions}

\notes{How do the $z_i$ variables transition between $X$ and $M$? We need an approach to identifying when the character of variables has changed.}

\notes{The moment generating function (MGF) can help identify transition candidates,}
$$
M_Z(t) = E[e^{t \cdot Z}] = \exp(A(\boldsymbol{\theta}+t) - A(\boldsymbol{\theta})).
$$
\notes{Taking the logarithm gives us the cumulant generating function:}
$$
K_Z(t) = \log M_Z(t) = A(\boldsymbol{\theta}+t) - A(\boldsymbol{\theta}).
$$
\notes{Variables transition when their contribution to cumulants changes significantly. Specifically, we can track the second derivative of the cumulant generating function (which gives the variance) for each variable,}
$$
\frac{d^2}{dt_i^2}K_Z(t)|_{t=0} = \frac{\partial^2 A(\boldsymbol{\theta})}{\partial \theta_i^2}.
$$
\notes{When a variable's variance begins to grow rapidly as we move along the entropy gradient, it indicates that this variable is transitioning from memory ($M$) to observable ($X$). Conversely, when a variable's contribution to higher-order cumulants decreases, it may be transitioning from $X$ to $M$.}

\notes{This transition can also be understood as a change in the Shannon channel characteristics of the variable - from a low-noise, precision-optimized channel (in $M$) to a high-bandwidth, high-entropy channel (in $X$).}

\endif
