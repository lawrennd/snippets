\ifndef{jaynesWorldOverviewAndDefinitions}
\define{jaynesWorldOverviewAndDefinitions}

\editme

\subsection{Purpose}

This game explores how structure, time, causality, and locality can emerge within a system governed solely by internal information-theoretic constraints. It serves as

- A *research framework* for observer-free dynamics and entropy-based emergence,
- A *conceptual tool* for introducing ideas widely used in physics in an accessible, internally consistent setting making them more accessible in the computational and statistical sciences.

\subsection{Definitions and Global Constraints}

\subsubsection{System Structure}

- Let $Z = \{Z_1, Z_2, \dots, Z_n\}$ be the full set of system variables.
- At time $t$, define a partition:
  - $X(t) \subseteq Z$: active variables (currently contributing to entropy)
  - $M(t) = Z \setminus X(t)$: latent or frozen variables (information reservoir)

\subsubsection{Representation via Density Matrix}

- The system’s state is given by a density matrix
  $$\rho(\boldsymbol{\theta}) = \frac{1}{Z(\boldsymbol{\theta})} \exp\left( \sum_i \theta_i H_i \right)$$
  where
  - $\boldsymbol{\theta} \in \mathbb{R}^d$: natural parameters,
  - $H_i$: Hermitian operators associated with observables,
  - $Z(\boldsymbol{\theta}) = \mathrm{Tr}[\exp(\sum_i \theta_i H_i)]$

- The *log-partition function* is
  $$A(\boldsymbol{\theta}) = \log Z(\boldsymbol{\theta})$$

- The *entropy* is
  $$S(\boldsymbol{\theta}) = A(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \nabla A(\boldsymbol{\theta})$$

- The *Fisher Information Matrix* is
  $$G_{ij}(\boldsymbol{\theta}) = \frac{\partial^2 A}{\partial \theta_i \partial \theta_j}$$

\subsubsection{Entropy Capacity and Resolution}

- The system has a *maximum entropy* of $N$ bits.
- This defines a *minimum detectable resolution* in natural parameter space
  $$\varepsilon \sim \frac{1}{2^N}$$

- Changes smaller than $\varepsilon$ are treated as *invisible* by the system.
- As a result, system dynamics exhibit *discrete, detectable transitions* between distinguishable states.

\subsubsection{Clarification: Dual Role of Parameters and Variables}

- Each variable $Z_i$ is associated with a generator $H_i$, and a natural parameter $\theta_i$.
- When we say a parameter $\theta_i \in X(t)$, we mean:
  - The component of the system associated with $H_i$ is active at time $t$,
  - And its parameter is evolving with $|\dot{\theta}_i| \geq \varepsilon$.
- This reflects the duality between *variables*, *observables*, and *natural parameters* within exponential family representations.

\subsection{Core Axiom: Entropic Dynamics}

The system evolves by steepest ascent in entropy
$$\frac{d\boldsymbol{\theta}}{dt} = -G(\boldsymbol{\theta}) \boldsymbol{\theta}$$

\subsection{Constructed Quantities and Lemmas}

\subsubsection{Definition: Latent-to-Active Information Flow Functional}

Define the *information flow from latent structure to active parameters* as:
$$
\Psi(t) := \boldsymbol{\theta}_{X(t)}^\top G_{X(t) M(t)} \boldsymbol{\theta}_{M(t)}
$$
This functional captures the curvature-mediated coupling between the current active system $X(t)$ and the latent reservoir $M(t)$. It reflects the degree to which structural information in $M$ contributes to entropy growth in $X$.


\subsubsection{Variable Partition}

$$X(t) = \left\{ i \mid \left| \frac{d\theta_i}{dt} \right| \geq \varepsilon \right\}, \quad M(t) = Z \setminus X(t)$$

\subsection{Lemma 1: Form of the Minimal Entropy Configuration}

The minimal-entropy state compatible with the system’s resolution constraint and regularity condition is represented by a density matrix of the exponential form:
$$\rho(\boldsymbol{\theta}_0) = \frac{1}{Z(\boldsymbol{\theta}_0)} \exp\left( \sum_i \theta_{0i} H_i \right)$$

where $\boldsymbol{\theta}_0 \approx \boldsymbol{0}$, and all components $\theta_{0i}$ are sub-threshold:
$$|\dot{\theta}_{0i}| < \varepsilon$$

This state minimizes entropy under the constraint that it remains regular, continuous, and detectable only above a resolution scale $\varepsilon \sim 1/2^N$. Its structure can be derived via a *minimum-entropy analogue of Jaynes' formalism*, using the same density matrix geometry but inverted optimization.

\subsubsection{Lemma 2: Symmetry Breaking}

If $\theta_k \in M(t)$ and $|\dot{\theta}_k| \geq \varepsilon$, then
$$\theta_k \in X(t + \delta)$$

\subsubsection{Entropy-Time}

$$\tau(t) := S_{X(t)}(t)$$

\subsubsection{Lemma 3: Monotonicity of Entropy-Time}

$$\tau(t_2) \geq \tau(t_1) \quad \text{for all } t_2 > t_1$$

\subsubsection{Corollary: Irreversibility}

$\tau(t)$ increases monotonically, preventing time-reversal globally.

\subsubsection{Variational Principle Within a Symmetry Class}

$$\delta \int_{\tau_i}^{\tau_{i+1}} \boldsymbol{\theta}_{X_i}^\top G_{X_i X_i} \boldsymbol{\theta}_{X_i} \, d\tau = 0$$

\subsection{Lemma 4: Frieden-Analogous Extremal Flow}

At points where the latent-to-active flow functional $\Psi(t)$ is locally extremal (i.e., $\frac{d\Psi}{dt} = 0 $), the system may exhibit:

- Temporary stability or critical slowing,
- Transitions between symmetry classes (e.g., emergence of a new active variable),
- Reconfiguration of internal curvature flow.

These transitions play a role analogous to *extremizing an internal information exchange*, similar in spirit to Frieden’s $\delta(I - J) = 0$ condition, but realized without requiring an observer or measurement.

\subsection{Speculative Implications and Hypotheses}

- *Local Reversibility* within fixed symmetry classes
- *Latent Memory*: influence of inactive variables through curvature
- *Pseudo-Saddles*: slow evolution from flat entropy curvature
- *Conditional Independence*: emergent locality via block structure in $G$
- *Domain Transitions*: new behaviour as variables emerge or stall

\subsection{Interpretation and Nuance}

\subsubsection{1. Apparent Zero-Entropy Start}

The game behaves as if it originates at low entropy, but this is a consequence of the entropy ascent, not an assumption.

\subsubsection{2. Discretisation from Entropy Capacity}

Finite entropy bounds imply resolution constraints, producing discrete transitions without discretizing the space.

\subsubsection{3. Dual Role of Parameters and Variables}

“$\theta_i \in X(t)$” means the observable governed by $H_i$ is actively evolving. Variables, parameters, and observables are dual facets of the representation.

\subsubsection{4. Irreversibility vs Local Reversibility}

Monotonic entropy-time induces global irreversibility, but local symmetry classes may evolve reversibly.

\subsubsection{5. Fisher Information is an Analytic Tool}

$G(\boldsymbol{\theta})$ helps us understand evolution—it is not known or used by the system itself.

\subsubsection{6. No Observer or Collapse Needed}

Structure emerges from the system’s internal curvature and resolution constraint, without measurement postulates.

\subsubsection{7. Singularity Avoidance}

True singularities (e.g. delta functions) are excluded; minimal-entropy states are regularized via density matrices.

\subsubsection{8. Variational Principle is Optional}

Only valid within fixed symmetry classes. It offers insight but is not required by the system’s evolution.


\subsection{Connection to Frieden’s EPI: A Conceptual Analogue}

This game is not built to explain or reproduce any specific physical theory, but it reveals structural patterns that *resemble variational information principles*, such as those used in Frieden’s Extreme Physical Information (EPI) framework.

Frieden’s principle proposes that physical systems arise by extremizing a quantity $I - J$, where:

- $J$ is source (intrinsic) information,
- $I$ is Fisher information extracted by an observer.

In this game:

- No observer is present,
- But we still have a structure ($G(\boldsymbol{\theta})$) that defines *latent curvature* (reservoir $M$),
- And *detectable entropy flow* (active $X$).

The *information flow functional*:
$$
\Psi(t) = \boldsymbol{\theta}_X^\top G_{XM} \boldsymbol{\theta}_M
$$
serves as a natural analogue to *internal information exchange*, without reference to measurement.

When $\Psi(t)$ is extremal, the system may undergo a qualitative shift in its active structure—suggesting an internal, geometry-driven analogue to EPI, but interpreted entirely within the unfolding of the system itself.

\endif
