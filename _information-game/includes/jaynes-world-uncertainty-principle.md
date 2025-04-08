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

\subsection{Formal Derivation of the Uncertainty Principle}

\slides{
* Information-theoretic derivation
* Begins with Shannon entropy constraints
* Reaches uncertainty bound through variational analysis
}

\notes{We can derive the uncertainty principle formally from the information-theoretic properties of the system. Consider the mutual information between parameters $\boldsymbol{\theta}(M)$ and capacity variables $c(M)$:
$$
I(\boldsymbol{\theta}(M); c(M)) = H(\boldsymbol{\theta}(M)) + H(c(M)) - H(\boldsymbol{\theta}(M), c(M))
$$
where $H(\cdot)$ represents differential entropy. 

Since the total entropy of the system is bounded by $N$, we know that $h(\boldsymbol{\theta}(M), c(M)) \leq N$. Additionally, for any two random variables, the mutual information satisfies $I(\boldsymbol{\theta}(M); c(M)) \geq 0$, with equality if and only if they are independent.

For our system to function as an effective information reservoir, $\boldsymbol{\theta}(M)$ and $c(M)$ cannot be independent - they must share information. This gives us,
$$
h(\boldsymbol{\theta}(M)) + h(c(M)) \geq h(\boldsymbol{\theta}(M), c(M)) + I_{\min}
$$
where $I_{\min} > 0$ is the minimum mutual information required for the system to function.}

\notes{For variables with fixed variance, differential entropy is maximized by Gaussian distributions. For a multivariate Gaussian with covariance matrix $\Sigma$, the differential entropy is:
$$
h(\mathcal{N}(0, \Sigma)) = \frac{1}{2}\ln\left((2\pi e)^d|\Sigma|\right)
$$
where $d$ is the dimensionality and $|\Sigma|$ is the determinant of the covariance matrix.

The Cramér-Rao inequality provides a lower bound on the variance of any unbiased estimator. If $\boldsymbol{\theta}$ is a parameter vector and $\hat{\boldsymbol{\theta}}$ is an unbiased estimator, then:
$$
\text{Cov}(\hat{\boldsymbol{\theta}}) \geq G^{-1}(\boldsymbol{\theta})
$$
where $G(\boldsymbol{\theta})$ is the Fisher information matrix.

In our context, the relationship between parameters $\boldsymbol{\theta}(M)$ and capacity variables $c(M)$ follows a similar bound. The Fisher information matrix for exponential family distributions has a special property: it equals the covariance of the sufficient statistics, which in our case are represented by the capacity variables $c(M)$. This gives us
$$
G(\boldsymbol{\theta}(M)) = \text{Cov}(c(M))
$$

Applying the Cramér-Rao inequality we have
$$
\text{Cov}(\boldsymbol{\theta}(M)) \cdot \text{Cov}(c(M)) \geq G^{-1}(\boldsymbol{\theta}(M)) \cdot G(\boldsymbol{\theta}(M)) = \mathbf{I}
$$
where $\mathbf{I}$ is the identity matrix.

For one-dimensional projections, this matrix inequality implies,
$$
\text{Var}(\boldsymbol{\theta}(M)) \cdot \text{Var}(c(M)) \geq 1
$$
and converting to standard deviations we have
$$
\Delta\boldsymbol{\theta}(M) \cdot \Delta c(M) \geq 1.
$$

When we incorporate the minimum mutual information constraint $I_{\min}$, the bound tightens. Using the relationship between differential entropy and mutual information, we can derive
$$
\Delta\boldsymbol{\theta}(M) \cdot \Delta c(M) \geq k,
$$
where $k = \frac{1}{2\pi e}e^{2I_{\min}}$. 

This is our uncertainty principle, directly derived from information-theoretic constraints and the Cramér-Rao bound. It represents the fundamental trade-off between precision in parameter specification and capacity for information storage.}

\subsection{Definition of Capacity Variables}

\slides{
* Capacity variables $c(M)$ precisely defined:
  * Measure information storage potential 
  * Fourier-conjugate to parameters
}

\notes{We now provide a precise definition of the capacity variables $c(M)$. The capacity variables quantify the potential of memory variables to store information about observable variables. Mathematically, we define $c(M)$ as,
$$
c(M) = \nabla_{\boldsymbol{\theta}} A(\boldsymbol{\theta}(M))
$$
where $A(\boldsymbol{\theta})$ is the log-partition function from our exponential family distribution. This definition has a clear interpretation: $c(M)$ represents the expected values of the sufficient statistics under the current parameter values. 

This definition also naturally yields the Fourier relationship between parameters and capacity. In exponential families, the log-partition function and its derivatives form a Legendre transform pair, which is the mathematical basis for the Fourier duality we claim. Specifically, if we define the Fourier transform operator $\mathcal{F}$ as the mapping that takes parameters to expected sufficient statistics, then:
$$
c(M) = \mathcal{F}[\boldsymbol{\theta}(M)]
$$
}

\subsection{Capacity $\leftrightarrow$ Precision Paradox}

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
where $k$ is a constant. This relationship can be recognised as a natural *uncertainty principle* that underpins the behaviour of the game. This principle is a necessary consequence of information theory. It follows from the requirement for the parameter-like states, $M$ to have both precision and high capacity (in the Shannon sense \cite{shannon1948mathematical}). The uncertainty principle ensures that when parameters are sharply defined (low $\Delta\boldsymbol{\theta}$), the capacity variables have high uncertainty (high $\Delta c$), allowing information to be encoded in their relationships rather than absolute values.}

\notes{This trade-off between precision and capacity directly parallels Shannon's insights about information transmission [@Shannon-info48], where he demonstrated that increasing the precision of a signal requires increasing bandwidth or reducing noise immunity—creating an inherent trade-off in any communication system. Our formulation extends this principle to the information reservoir's parameter space.}

\notes{In practice this means that the parameters $\boldsymbol{\theta}(M)$ and capacity variables $c(M)$ must form a Fourier-dual pair,
$$
c(M) = \mathcal{F}[\boldsymbol{\theta}(M)],
$$
This duality becomes important at saddle points when direct gradient ascent stalls.}

\notes{The mathematical formulation of the uncertainty principle comes from @Hirschman-entropy57 and later refined by @Beckner-fourier75 and @Bialynicki-uncertainty75. These works demonstrated that Shannon's information-theoretic entropy provides a natural framework for expressing the uncertainty principle, establishing a direct bridge between the mathematical formalism of quantum mechanics and information theory. Our capacity-precision trade-off follows this tradition, expressing the fundamental limits of information processing in our system.}

\subsection{Quantum vs Classical Information Reservoirs}

\slides{
* Near origin: quantum-like
  * Wave encoding of capacity, non-local correlations
  * Uncertainty principle saturated
* Higher entropy: Transition to "classical" behavior
  * From wave-like to particle-like information storage
  * Local rather than distributed encoding
}

\notes{The uncertainty principle means that the game can exhibit quantum-like information processing regimes during evolution. This inspires an information-theoretic perspective on the quantum-classical transition.}

\notes{At minimal entropy states near the origin, the information reservoir has characteristics reminiscent of quantum systems.}

\notes{
1. *Wave-like information encoding*: The information reservoir near the origin necessarily encodes information in distributed, interference-capable patterns due to the uncertainty principle between parameters $\boldsymbol{\theta}(M)$ and capacity variables $c(M)$.}

\notes{
2. *Non-local correlations*: Parameters are highly correlated through the Fisher information matrix, creating structures where information is stored in relationships rather than individual variables.
}

\notes{
3. *Uncertainty-saturated regime*: The uncertainty relationship $\Delta\boldsymbol{\theta}(M) \cdot \Delta c(M) \geq k$ is nearly saturated (approaches equality), similar to Heisenberg's uncertainty principle in quantum systems and the entropic uncertainty relations established by @Bialynicki-uncertainty75.}

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

\notes{This formulation of the uncertainty principle in terms of information capacity and parameter precision follows the tradition established by @Shannon-info48 and expanded upon by @Hirschman-entropy57 and others who connected information entropy uncertainty to Heisenberg's uncertainty.}

\subsection{Quantitative Demonstration}

\slides{
* Numerical example showing uncertainty principle
* Demonstrates trade-off across parameter space
* Shows saturation at minimal entropy
}

\notes{We can demonstrate this principle quantitatively through a simple model. Consider a two-dimensional system with memory variables $M = (m_1, m_2)$ that map to parameters $\boldsymbol{\theta}(M) = (\theta_1(m_1), \theta_2(m_2))$. The capacity variables are $c(M) = (c_1(m_1), c_2(m_2))$.

At minimal entropy, when the system is near the origin, the uncertainty product is exactly:
$$
\Delta\theta_i(m_i) \cdot \Delta c_i(m_i) = k
$$
for each dimension $i$. 

As the system evolves and entropy increases, some variables transition to classical behavior with:
$$
\Delta\theta_i(m_i) \cdot \Delta c_i(m_i) \gg k
$$

This increased product reflects the transition from quantum-like to classical information processing. The variables that maintain the minimal uncertainty product $k$ continue to function as coherent information reservoirs, while those with larger uncertainty products function as classical processors.}

\notes{This principle provides testable predictions for any system modeled as an information reservoir. Specifically, we predict that variables functioning as effective memory must demonstrate precision-capacity trade-offs near the theoretical minimum $k$, while processing variables will show excess uncertainty above this minimum.}

\endif
