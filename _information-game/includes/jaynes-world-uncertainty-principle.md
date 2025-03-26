\ifndef{uncertaintyPrinciple}
\define{uncertaintyPrinciple}

\editme

\subsection{Uncertainty Principle}

\notes{One challenge is how to parameterise our exponential family. We've mentioned that the variables $Z$ are partitioned into observable variables $X$ and memory variables $M$. Given the minimal entropy initial state, the obvious initial choice is that at the origin all variables, $Z$, should be in the information reservoir, $M$. This implies that they are well determined and present a sensible choice for the source of our parameters.}

\slides{
* Information reservoir variables ($M$) map to natural parameters $\boldsymbol{\theta}(M)$
* Challenge: Need both precision in parameters and capacity for information
}

\notes{We define a mapping, $\boldsymbol{\theta}(M)$, that maps the information resevoir to a set of values that are equivalent to the *natural parameters*. If the entropy of these parameters is low, and the distribution $\rho(\boldsymbol{\theta})$ is sharply peaked then we can move from treating the memory mapping, $\boldsymbol{\theta}(\cdot)$, as a random processe to an assumption that it is a deterministic function. We can then follow gradients with respect to these $\boldsymbol{\theta}$ values.}

\notes{This allows us to rewrite the distribution over $Z$ in a conditional form,
$$
\rho(X|M) = h(X) \exp(\boldsymbol{\theta}(M)^\top T(X) - A(\boldsymbol{\theta}(M))).
$$
}
\notes{Unfortunately this assumption implies that $\boldsymbol{\theta}(\cdot)$ is a delta function, and since our representation as a compact manifold (bounded below by $0$ and above by $N$) it does not admit any such singularities.}

\subsection{Capacity $\rightarrow$ Precision Paradox}

\slides{
* Fundamental trade-off emerges:
* $\Delta\boldsymbol{\theta}(M) \cdot \Delta c(M) \geq k$
* Cannot simultaneously have perfect precision and maximum capacity
}

\notes{This creates an apparent paradox, at minimal entropy states, the information reservoir must simultaneously maintain precision in the parameters $\boldsymbol{\theta}(M)$ (for accurate system representation) but it must also provide sufficient capacity $c(M)$ (for information storage).} 

\notes{The trade-off can be expressed as,
$$
\Delta\boldsymbol{\theta}(M) \cdot \Delta c(M) \geq k,
$$
where $k$ is a constant. This relationship can be recognised as a natural *uncertainty principle* that underpins the behaviour of the game. This principle is a necessary consequence of information theory. It follows from the requirement for the parameter-like states, $M$ to have both precision and high capacity (in the Shannon sense). The uncertainty principle ensures that when parameters are sharply defined (low $\Delta\boldsymbol{\theta}$), the capacity variables have high uncertainty (high $\Delta c$), allowing information to be encoded in their relationships rather than absolute values.}

\notes{In practice this means that the parameters $\boldsymbol{\theta}(M)$ and capacity variables $c(M)$ must form a 
Fourier-dual pair,
$$
c(M) = \mathcal{F}[\boldsymbol{\theta}(M)],
$$
This duality becomes important at saddle points when direct gradient ascent stalls.}

\subsection{Quantum vs Classical Information Reservoirs}

\slides{
* Near origin: "Quantum-like" information processing
  * Wave-like encoding, non-local correlations
  * Uncertainty principle nearly saturated
* Higher entropy: Transition to "classical" behavior
  * From wave-like to particle-like information storage
  * Local rather than distributed encoding
}

\notes{The uncertainty principle means that the game can exhibit quantum-like information processing regimes during evolution. This inspires an  information-theoretic perspective on the quantum-classical transition.}

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

2. *Decoherence-like process*: The uncertainty product $\Delta\boldsymbol{\theta}(M) \cdot \Delta c(M)$ for these variables grows significantly larger than the minimum value $k$, indicating a departure from quantum-like behavior.

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

\notes{The quantum-classical transition can be quantified using the moment generating function $M_Z(t)$. In quantum-like regimes, the MGF exhibits oscillatory behavior with complex analytic structure, whereas in classical regimes, it grows monotonically with simple analytic structure. The transition between these behaviors identifies variables moving between quantum-like and classical information processing modes.}

\notes{This perspective suggests that what we recognize as "quantum" versus "classical" behavior may fundamentally reflect different regimes of information processing - one optimized for coherent information storage (quantum-like) and the other for flexible information manipulation (classical-like). The emergence of both regimes from our entropy-maximizing model indicates that nature may exploit this computational architecture to optimize information processing across multiple scales.}

\endif
