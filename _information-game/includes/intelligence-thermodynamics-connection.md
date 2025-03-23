\ifndef{informationEngines}
\define{informationEngines}

\editme

\section{Information Engines: Intelligence as an Energy-Efficiency}

\notes{The entropy game shows some parallels between thermodynamics and measurement. This allows us to imagine *information engines*, simple systems that convert information to energy. This is our first simple model of intelligence.}

\subsection{Measurement as a Thermodynamic Process: Information-Modified Second Law}

\notes{The second law of thermodynamics was generalised to include the effect of measurement by Sagawa and Ueda [@Sagawa-second08]. They showed that the maximum extractable work from a system can be increased by $k_BTI(X;M)$ where $k_B$ is Boltzmann's constant, $T$ is temperature and $I(X;M)$ is the information gained by making a measurement, $M$,}
$$
I(X;M) = \sum_{x,m} \rho(x,m) \log \frac{\rho(x,m)}{\rho(x)\rho(m)},
$$
where $\rho(x,m)$ is the joint probability of the system and measurement (see e.g. eq 14 in @Sagawa-second08). This can be written as
$$
W_\text{ext} \leq  - \Delta\mathcal{F} + k_BTI(X;M),
$$
where $W_\text{ext}$ is the extractable work and it is upper bounded by the negative change in free energy, $\Delta\mathcal{F}$, plus the energy gained from measurement, $k_BTI(X;M)$. This is the information-modified second law.}

\notes{The measurements can be seen as a thermodynamic process. In theory measurement, like computation is reversible. But in practice the process of measurement is likely to erode the free energy somewhat, but as long as the energy gained from information, $kTI(X;M)$ is greater than that spent in measurement the pricess can be thermodynamically efficient.}

\slides{
* Measurement is a thermodynamic process.
* The engine can return $k_BTI(X;M)$ Joules of energy.
* If this is greater than available energy used in measurement, the process has a thermodynamic return.
}

\notes{The modified second law shows that the maximum additional extractable work is proportional to the information gained. So information acquisition creates extractable work potential. Thermodynamic consistency is maintained by properly accounting for information-entropy relationships.}

\subsection{Efficacy and Efficiency of Feedback Control}

\notes{Sagawa and Ueda further extend this relationship to provide a *generalised Jarzynski equality* for feedback processes [@Sagawa-generalized10]. The Jarzynski equality is an imporant result from nonequilibrium thermodynamics that relates the average work done across an ensemble to the free energy difference between initial and final states [@Jarzynski-nonequilibrium97],
$$
\langle \exp\left(-\frac{W}{k_B T}right) \rangle = \exp\left(-\frac{\Delta\mathcal{F}}{k_BT}\right),
$$
where $\langle W \rangle$ is the average work done across an ensemble of trajectories, $\Delta\mathcal{F}$ is the change in free energy, $k_B$ is Boltzmann's constant, and $\Delta S$ is the change in entropy. Sagawa and Ueda extended this equality to to include information gain from measurement [@Sagawa-generalized10],
$$
\langle \exp\left(-\frac{W}{k_B T}right) \exp\left(\frac{\Delta\mathcal{F}}{k_BT}\right) \exp\left(-\mathcal{I}(X;M)\right)\rangle = 1,
$$}
where $\mathcal{I}(X;M) = \log \frac{\rho(X|M)}{\rho(X)}$ is the information gain from measurement, and the mutual information is recovered $I(X;M) = \langle \mathcal{I}(X;M) \rangle$ as the average information gain.}

\notes{This allows us to address the situation when feedback is present and estimate its efficiency. Sagawa and Ueda introduce an *efficacy* term that captures the effect of feedback on the system they note in the presence of feedback,
$$
\langle \exp\left(-\frac{W}{k_B T}right) \exp\left(\frac{\Delta\mathcal{F}}{k_BT}\right)\rangle = \gamma,
$$
where $\gamma$ is the efficacy. We can also introduce an efficiency,
$$
\eta = \frac{\langle \Delta \mathcal{F} - W\rangle}{I(X; M)},
$$
This allows us to estimate the efficiency of feedback control as
$$
\frac{W}{k_BT} = \frac{\Delta\mathcal{F}}{k_BT} - \mathcal{I}(X;M) + \ln \gamma.
$$


\notes{This allows us to }
\section{Decomposition into Past and Future}

\subsection{Model Approximations and Thermodynamic Efficiency}

\notes{Intelligent systems must balance measurement against energy efficiency and time requirements. A perfect model of the world would require infinite computational resources and speed, so  approximations are necessary. This leads to uncertainties. Thermodynamics might be thought of as the physics of uncertainty: at equilibrium thermodynamic systems find thermodynamic states that minimize free energy, equivalent to maximising entropy.}

\slides{
* Perfect models require infinite resources
* Approximations minimize free energy
* Bounded rationality as a response to thermodynamic constraints
* Intelligence has context
}

\subsection{Markov Blanket}

\notes{Now we introduce some structure to the model assumption. We split $X$ into $X_0$ and $X_1$. $X_0$ is past and present of the system, $X_1$ is future The conditional mutual information $I(X_0;X_1|M)$ which is zero if $X_1$ and $X_0$ are independent conditioned on $M$.}

\notes{First note that by definition of the mutual information we have
\[
I(X_0, X_1; M) = I(X_0; X_1) + I(M; X_1|X_0)
\]
by the chain rule of information theory. Here we would achieve a Markov separation between $X_0$ and $X_1$ if $I(X_0;X_1|M) = 0$.}


<!--Start Include here -->


Consider a system $X$ that can be decomposed into past ($X_0$) and future ($X_1$) states, along with a memory system $M$. The mutual information between the system and memory is:
\[
I(X_0X_1;M) = \sum_{x_0,x_1,m} \rho(x_0,x_1,m) \ln \frac{\rho(x_0,x_1,m)}{\rho(x_0,x_1)\rho(m)}.
\]

### Conditional Factorization Decomposition

We can decompose this mutual information by considering a conditionally factorized distribution
\[
\rho_f(x_0,x_1,m) = \rho(x_0|m)\rho(x_1|m)\rho(m).
\]
The KL divergence between the true and factorized distributions gives us:
\[
I(X_0X_1;M) = D_{KL}(\rho||\rho_f) + I_f(X_0X_1;M).
\]
The factorized mutual information further decomposes into separate past and future components
\[
I_f(X_0X_1;M) = I(X_0;M) + I(X_1;M).
\]
This gives the complete decomposition
\[
I(X_0X_1;M) = D_{KL}(\rho||\rho_f) + I(X_0;M) + I(X_1;M).
\]

### Simulation in the Temporal Framework

Simulation can be viewed as a special configuration of memory where the primary goal is to maximize predictive power $I(X_1;M_{\text{predict}}|X_0)$ rather than control effectiveness. The memory system is configured to evolve according to dynamics that mirror the target system:
\[
\dot{m} = g(m, t) \approx f(x, t)
\]
where $f(x, t)$ represents the true system dynamics and $g(m, t)$ represents the simulation dynamics.

This perspective reveals an important duality: while control systems use memory to influence future states, simulation systems use memory to predict future states without necessarily influencing them. Both processes are governed by the same information-thermodynamic principles but optimize different objectives.

### Bayesian Inference as Memory Update

Bayesian inference provides a principled framework for updating memory representations as new information arrives. In the information-thermodynamic framework, Bayesian updating can be understood as the process of modifying $M_{\text{store}}$ to incorporate new observations while maintaining uncertainty representations.

#### Prior Knowledge as Initial Memory State

The Bayesian prior $p(\theta)$ represents the initial state of $M_{\text{store}}$ before new observations,
\[
I(X_{past};M_{\text{store}}) = D_{KL}(p(\theta)||p_0(\theta)),
\]
where $p_0(\theta)$ represents a reference state of no information. The prior encodes both:
1. Previous observations stored in memory
2. Structural knowledge about the system

#### Likelihood as Observation Model

The likelihood function $p(x|θ)$ represents how $M_{\text{obs}}$ relates to the true system state,
\[
I(X_0;M_{\text{obs}}|\theta) = \mathbb{E}_{p(x|\theta)}[\log p(x|\theta)].
\]
This quantifies how much information each observation provides about the system state.

#### Posterior as Updated Memory State

The posterior distribution $p(\theta|x)$ represents the updated state of $M_{\text{store}}$ after incorporating new observations,
\[
p(\theta|x) = \frac{p(x|\theta)p(\theta)}{p(x)}.
\]
The information gain from updating is:
\[
\Delta I = D_{KL}(p(\theta|x)||p(\theta)).
\]
This represents the change in mutual information between memory and system state.

#### Thermodynamic Cost of Bayesian Updates

The Bayesian update process incurs a minimum thermodynamic cost:
\[
W_{update} \geq kT \ln(2) \cdot D_{KL}(p(\theta|x)||p(\theta))
\]
This connects to Landauer's principle [@Landauer-irreversibility61], showing that information updates require physical work.

#### Variational Inference Under Resource Constraints

When exact Bayesian updates are computationally intractable, variational inference provides a bounded rationality approach,
\[
q^*(\theta) = \arg\min_{q \in \mathcal{Q}} D_{KL}(q(\theta)||p(\theta|x)),
\]
where $\mathcal{Q}$ represents a constrained family of distributions that $M_{\text{store}}$ can represent within its computational and memory limitations.

This framework explains why:
1. Bayesian methods naturally handle uncertainty
2. Approximate inference methods are often necessary in practice
3. The choice of prior matters more when data is limited

The Maximum Caliber principle suggests that optimal inference strategies will balance the information gain from updates against their thermodynamic costs.

### Channel Coding Perspective on Memory

When viewing $M$ as an information channel between past and future states, Shannon's channel coding theorems apply. The channel capacity $C$ represents the maximum rate of reliable information transmission
\[
C = \max_{\rho(M)} I(X_1;M)
\]
and for a memory of $n$ bits we have
\[
C \leq n,
\]
as the mutual information is upper bounded by the entropy of $\rho(M)$ which is at most $n$ bits.

This relationship closely aligns with Ashby's Law of Requisite Variety (pg 229 @Ashby-design52), which states that a control system must have at least as much 'variety' as the system it aims to control. In the context of memory systems, this means that to maintain temporal correlations effectively, the memory's state space must be at least as large as the information content it needs to preserve. This provides a lower bound on the necessary memory capacity that complements the bound we get from Shannon for channel capacity.

This helps determine the required memory size for maintaining temporal correlations, optimal coding strategies, and fundamental limits on temporal correlation preservation.

### Statistical Modeling and Machine Learning Through Memory Decomposition

The memory decomposition framework provides a unifying perspective on classical statistical modeling and machine learning approaches. Both can be understood as different emphases within the same information-theoretic structure.

#### Classical Statistics as Observation-Focused

Classical statistics primarily focuses on the relationship between $M_{\text{obs}}$ and $X_0$ - the observation model. The central goal is to accurately encode current system states in memory and interpret the resulting parameters:

\[
I(X_0;M_{\text{obs}}) \text{ is maximized through experimental design}
\]

Key elements of statistical practice map directly to the framework. 
1. *parameter estimation*: Finding memory parameters that best explain observed data
2. *experimental design*: Carefully structuring observations to maximize information capture while minimizing confounding factors
3. *hypothesis testing*: Evaluating competing models of the observation process

Maximum likelihood estimation, a cornerstone of statistical inference, can be viewed as minimizing the KL divergence between the true data distribution $\rho(x_0)$ and the model distribution $p_\theta(x_0)$,
\[
\hat{\theta}_{MLE} = \arg\min_\theta D_{KL}(\rho(x_0)||p_\theta(x_0)).
\]
This connects directly to the information-theoretic bounds, as this divergence determines how much information about $X_0$ is captured in the model parameters.

#### The Bootstrap: Estimating Uncertainty Through Resampling

When direct computation of uncertainties is intractable or the true distribution is unknown, the bootstrap provides a powerful way to estimate uncertainties by resampling from $M_{\text{obs}}$. This can be understood in the framework as a method for estimating the information content actually captured in memory,
\[
I(X_0;M_{\text{obs}}) \approx \frac{1}{B}\sum_{b=1}^B I(X_0^b;M_{\text{obs}}^b),
\]
where $X_0^b$ and $M_{\text{obs}}^b$ represent the b-th bootstrap sample. This approach:
1. Requires no additional observations beyond those already in memory
2. Provides estimates of parameter uncertainty without assuming a specific distribution
3. Reveals how much information about $X_0$ is reliably encoded in $M_{\text{obs}}$

The bootstrap's effectiveness stems from its ability to estimate the sampling distribution of statistics using only the information already present in memory, making it particularly valuable under bounded rationality constraints where additional observations are costly or impossible.

#### Machine Learning as Prediction-Focused

Machine learning shifts emphasis toward $M_{\text{predict}}$ and its relationship with $X_1$ - the prediction model. The central goal is to maximize predictive power:
\[
I(X_1;M_{\text{predict}}|X_0) \quad \text{is maximized through model selection and training}
\]
Key elements of machine learning practice also map to the framework.
1. **Predictive Accuracy**: Optimizing the ability to predict future states
2. **Feature Engineering**: Transforming raw observations to maximize predictive utility
3. **Regularization**: Managing the information capacity of $M_{\text{store}}$ to prevent overfitting

Empirical risk minimization, the foundation of supervised learning, can similarly be viewed as minimizing the KL divergence between the true conditional distribution $\rho(x_1|x_0)$ and the model's predictive distribution $p_\theta(x_1|x_0)$:
\[
\hat{\theta}_{ERM} = \arg\min_\theta D_{KL}(\rho(x_1|x_0)||p_\theta(x_1|x_0)).
\]

#### Unifying View Through Information Flow

Both paradigms can be unified through the memory decomposition framework:
- Statistics emphasizes the flow of information from $X_0$ to $M_{\text{obs}}$ and $M_{\text{store}}$
- Machine learning emphasizes the flow from $M_{\text{store}}$ and $M_{\text{obs}}$ to $M_{\text{predict}}$
- Recent causal machine learning approaches aim to understand the entire information flow from $X_0$ through $M$ to $X_1$

This perspective explains why certain techniques are more prevalent in each field and suggests how they might be combined for more effective information processing systems. For example, we see more complex neural network models being used in machine learning for their predictive power, but when we are looking for interpretability of these models there's a tendency to revert to techniques such as linear extrapolation around an operating point such as LIME [@]. This approach of local linear approximation has a long history across many fields - from linearization of differential equations in dynamical systems analysis, to small-signal models in electronics, to perturbation methods in physics. The success of these methods stems from the fact that many complex nonlinear systems behave approximately linearly when examined over a small enough region around an operating point. LIME extends this classical technique to machine learning models, providing interpretable local approximations of complex black-box predictors. Similarly, the use of surrogate models (emulators) for sensitivity analysis or optimisation of complex models (@) builds on a rich history of reduced-order modeling across engineering and the physical sciences.

### Bias-Variance Dilemma Through the Information-Theoretic Lens

The classical bias-variance dilemma in statistical learning can be reinterpreted through the mutual information framework, providing deeper insights into this trade-off.

#### Information-Theoretic Decomposition of Prediction Error

Normally, when we consider the bias variance dilemma the expected error is  decomposed into bias, variance, and irreducible error:
\[
\mathbb{E}[(Y - \hat{f}(X))^2] = \text{bias}^2 + \text{variance} + \text{irreducible error}.
\]
In the information-theoretic framework, this decomposition relates directly to mutual information quantities. The *bias* corresponds to systematic information loss between $X_0$ and $M_{\text{obs}}$,
\[
\text{bias} \propto H(X_0) - I(X_0;M_{\text{obs}})
\]
This represents the information about $X_0$ that is systematically not captured in the memory representation.

The *variance* corresponds to spurious information in $M_{\text{predict}}$ that doesn't reflect $X_1$,
\[
\text{Variance} \propto I(M_{\text{predict}};D) - I(X_1;M_{\text{predict}}|X_0)
\]
where $D$ represents the specific training dataset (a subset of $X_0$). This measures how much the prediction depends on the particular training samples rather than the true relationship.

The *irreducible error* corresponds to the entropy of $X_1$ conditional on $X_0$,
\[
\text{Irreducible Error} \propto H(X_1|X_0),
\]
which represents the fundamental unpredictability of the future given the past.

#### Model Complexity as Information Capacity

Model complexity in this framework relates directly to the information capacity of memory:

\[
\text{Model Complexity} \propto \log|M_{\text{store}}|
\]

As model complexity increases:
- The potential mutual information $I(X_0;M_{\text{store}})$ increases (reducing bias)
- The risk of capturing dataset-specific patterns increases (increasing variance)
#### Regularization as Information Bottleneck

Regularization techniques can be understood as creating an information bottleneck that limits how much information from the training data is stored in the model,
\[
I(D;M) \leq C_{reg},
\]
where $C_{reg}$ is controlled by the regularization strength. This bottleneck:
- Reduces variance by limiting dataset-specific information
- May increase bias by restricting the model's capacity to represent the true relationship

#### Regularization as System-Wide Information Constraint

Regularization techniques can also be understood as creating information bottlenecks through the memory system, not just in storage. These constraints affect how information flows through the information resevoir,
\[
I(X_0;M) + I(M;X_1) \leq C_{reg},
\]
where $C_{reg}$ represents the overall information capacity of the system. This constraint manifests in different ways across memory components:

1. **Observation Constraints** ($M_{\text{obs}}$):
   - Limits which patterns are treated as signal versus noise
   - Influences feature extraction and attention mechanisms
   - Controls sensitivity to input variations
   \[
   I(X_0;M_{\text{obs}}) \leq C_{obs}
   \]

2. **Prediction Constraints** ($M_{predict}$):
   - Restricts complexity of input-output mappings
   - Creates bottleneck between observations and predictions
   - Prevents overfitting to training-specific patterns
   \[
   I(M_{predict};X_1|X_0) \leq C_{pred}
   \]

3. **System-Wide Effects**:
   - Shapes overall information flow architecture
   - Balances complexity across components
   - Determines effective model capacity
   \[
   I(X_0;X_1|M) \geq H(X_1|X_0) - C_{reg}
   \]

This system-wide perspective explains why:
1. Different regularization methods (L1, L2, dropout) affect learning in distinct ways
2. Regularization interacts with both feature learning and prediction
3. The most effective regularization strategy depends on where information bottlenecks are most needed

The MaxCal principle suggests that optimal regularization should distribute constraints across the system to minimize total information loss while preventing overfitting.

#### Optimal Information Capacity

The optimal model complexity balances these competing information flows,
\[
\text{Optimal Capacity} = \arg\min_{|M_{\text{store}}|} \left[ H(X_0) - I(X_0;M_{\text{store}}) + I(M_{\text{predict}};D) - I(X_1;M_{\text{predict}}|X_0)\right].
\]
ThE information-theoretic perspective explains why simple models (low $|M_{\text{store}}|$) perform well when data is limited, complex models (high $|M_{\text{store}}|$) perform well when data is abundant and the optimal model complexity scales with dataset size. Although we will revisit this idea when we look at Bayesian approaches.

### The Information Bottleneck

Tishby's Information Bottleneck (IB) principle provides a theoretical framework for understanding how memory systems can optimally compress past information while preserving predictive power. In the framework, this corresponds to finding a memory representation $M$ that optimally balances compression of $X_0$ against prediction of $X_1$.

#### Cross-Validation as Information Separation

Cross-validation can be viewed as a technique to estimate
\[
I(M_{\text{predict}};D) - I(X_1;M_{\text{predict}}|X_0).
\]
By evaluating the model on held-out data, we measure how much of the information in $M_{\text{predict}}$ generalizes beyond the specific training samples.

This information-theoretic reframing of the bias-variance dilemma provides a principled way to understand model selection and regularization within the broader framework of information flow through memory systems.

## Bounding Mutual Information

When the true joint distribution $\rho(x,m)$ is not directly accessible, we can bound the mutual information using a distribution $p_\theta(x,m)$,
\[
I(X_0;M) = \mathcal{I}_0(\theta) + D_{KL}(\rho||p_\theta),
\]
where $\theta$ are the parameters and are a subset of $M$ that controls the form of $p_\theta(x,m)$.
\[
\mathcal{I}_0(\theta) = \sum_{x_0,m} \rho(x_0,m) \ln \frac{p_\theta(x_0,m)}{\rho(x_0)\rho(m)}
\]
Since $D_{KL}(\rho||p) \geq 0$, we have
\[
I(X_0;M) \geq \mathcal{I}_0(\theta).
\]
This bound depends only on the approximating distribution $p_\theta(x,m)$ and the true distribution $\rho(x_0,m)$.

A similar bound can be derived for the future
\[
I(X_1;M) \geq \mathcal{I}_1(\theta).
\]

## Implications

The framework  shows how the memory creates independence between past and future states giving us the information cost of maintaining temporal correlations.

### Simulation as Information Processing

We can view simulation as a special case of information processing where a memory system $M$ is configured to mirror the dynamics of the target system $X$. The simulator can be see as a model system that has analogous state transitions to (some of) those of the target system while typically operating at different energy scales or timescales.

The fidelity of a simulation can be quantified through the mutual information between the simulated trajectories and the target system trajectories,
\[
I(X(t);M(t)) = \sum_{x(t),m(t)} p(x(t),m(t)) \log \frac{p(x(t),m(t))}{.p(x(t))p(m(t))}.
\]
Quantum systems are difficult to simulate on classical systems because the state space of the quantum system grows exponentially with the number of particles, requiring exponentially large memory systems to maintain simulation fidelity. To address this in the framework we could extend it to a quantum memory system for which the temperature is given by $h$, the Planck constant multiplied by $i$, the imaginary unit. That analysis falls beyond the scope of this paper other than to note that a Wick rotation would map the system back to the form of the classical one we're considering.

## At What Scales Does this Apply?

The equipartition theorem tells us that at equilibrium the average energy is $kT/2$ per degree of freedom. This means that for most practical systems the amount of energy available is many orders of magnitude larger than the amount of information we can store in memory.

This suggests that the amount of information we can store in memory is a small perturbation of the system and that the system is approximately in equilibrium, unless the system is at small scale.

### Small-Scale Biochemical Systems and Information Processing

While macroscopic systems operate in regimes where traditional thermodynamics dominates, microscopic biological systems operate at scales where information and thermal fluctuations become critically important. Here we examine how the framework applies to molecular machines and processes that have evolved to operate efficiently at these scales.

#### Molecular Machines as Information Engines

Molecular machines like ATP synthase, kinesin motors, and the photosynthetic apparatus can be viewed as sophisticated information engines that convert energy while processing information about their environment. These systems have evolved to exploit thermal fluctuations rather than fight against them, using information processing to extract useful work.

##### ATP Synthase: Nature's Rotary Engine

ATP synthase functions as a rotary molecular motor that synthesizes ATP from ADP and inorganic phosphate using a proton gradient. The system uses the proton gradient as both an energy source and an information source about the cell's energetic state and exploits Brownian motion through a ratchet mechanism. It converts information about proton locations into mechanical rotation and ultimately chemical energy.

From an information-thermodynamic perspective, we can estimate the efficiency:
\[
\eta_{ATP} = \frac{W_{output}}{E_{input} + kT \cdot I_{process}}
\]
where $I_{process}$ represents the information processed per ATP molecule synthesized. With approximately 3-4 protons required per ATP [@Boyer1997], the free energy available from the proton gradient is about 21 kJ/mol per proton [@Mitchell1961]. The synthesis of one ATP molecule requires approximately 50-60 kJ/mol [@Junge2009], yielding a thermodynamic efficiency of 80-90% when accounting for the 3-4 protons used.

The theoretical maximum efficiency according to the framework would be:
\[
\eta_{max} = \frac{W_{output}}{E_{input} + kT \cdot I_{min}}
\]
where $I_{min}$ represents the minimum information required to coordinate the proton flow. Recent biophysical measurements by [Toyabe-information10] and [@Zimmermann-rotation12] suggest that ATP synthase operates within 5-10% of this theoretical limit, processing approximately 4-5 bits of information per ATP molecule synthesized. This remarkable efficiency, confirmed through single-molecule experiments [@Yasuda-rotation01], indicates that evolution has optimized ATP synthase to approach the fundamental thermodynamic limits of energy conversion while minimizing information processing costs.

##### Photosynthesis: Quantum Coherence and Information

Photosynthetic light-harvesting complexes capture photons and transferring excitation energy to reaction centers. Recent evidence suggests quantum coherence may play a role in this efficiency [@Engel-evidence07; @Collini-coherence10; @Panitchayangkoon-longlived10], which from the framework can be viewed as:

1. A quantum memory effect that maintains correlations between excitation pathways [@Ishizaki-quantum09]
2. Information processing that directs excitation energy along optimal pathways [@Mohseni-environment08; @Rebentrost-environment09]
3. A mechanism that reduces entropy production during energy transfer [@Lloyd-quantum11]

The energy transfer efficiency in photosynthetic complexes can reach over 95% in optimal conditions [@Blankenship-comparing11]. This approaches theoretical limits when we account for,
\[
\Delta F_{avail} = \Delta E - T \Delta S + kT \cdot I_{quantum},
\]
where $I_{quantum}$ represents the information maintained through quantum coherence. Estimates suggest this quantum information processing could contribute 10-15% of the total efficiency advantage [@Sarovar-quantum10; @Caruso-entanglement10].

#### Molecular Recognition and Information Gain

Molecular recognition processes, such as enzyme-substrate binding, antibody-antigen interactions, and DNA-protein binding, can also be analyzed through this framework.

1. The binding process reduces configurational entropy while gaining binding energy [@Janin-principles10; @DuBay-entropy15]
2. Specificity can be quantified as mutual information between molecular shapes [@Schneider-molecular86; @Zuckerkandl-recognition94]
3. The thermodynamic cost of maintaining specificity is offset by energy released during binding [@Qian-coupling01; @Ouldridge-thermodynamics17]

For example, in enzyme catalysis,
\[
\Delta G_{catalysis} \approx \Delta G_{uncatalyzed} - kT \cdot I(E;S),
\]
where $I(E;S)$ represents the mutual information between enzyme and substrate [@Frey-enzymatic06]. This relationship can be derived from transition state theory, where the enzyme lowers the activation energy barrier by an amount proportional to the information it contains about the substrate [@Wolfenden-transition06].

Quantitatively, the catalytic efficiency ($k_{cat}/K_M$) relates to mutual information as:
\[
\frac{k_{cat}}{K_M} \approx \frac{k_B T}{h} \cdot e^{I(E;S)}
\]
where $h$ is Planck's constant [@BarEven-moderate11]. Typical enzyme catalytic rate enhancements of $10^6$ to $10^{17}$ [@Wolfenden-enormous11; @Lad-understanding03] correspond to information advantages of approximately 14-40 bits per reaction, calculated as:
\[
I(E;S) \approx \log_2\left(\frac{k_{cat}/K_M}{k_{uncat}}\right) \text{ bits}
\]
For example, orotidine 5′-monophosphate decarboxylase accelerates its reaction by a factor of $10^{17}$ [@Radzicka-proficiency95], corresponding to approximately 56.5 bits of mutual information between enzyme and transition state.

#### Implications for Synthetic Biology and Bioengineering

The information-thermodynamic framework suggests several avenues for biomimetic engineering:

1. Designing molecular machines that exploit thermal fluctuations through information processing
2. Creating synthetic proteins with optimized information-energy tradeoffs
3. Developing hybrid systems that combine biological information processing with synthetic energy conversion

Current synthetic molecular machines operate at efficiencies 1-2 orders of magnitude below their biological counterparts. The analysis suggests this gap could be closed by incorporating more sophisticated information processing mechanisms that have evolved in biological systems over billions of years.

The thermodynamic analysis of these small-scale biochemical systems reveals that significant energy gains (10-40% beyond conventional thermodynamic expectations) are plausible when accounting for information processing. This advantage becomes most pronounced at scales where thermal fluctuations are significant relative to overall system energy.

### Information and Control at Macroscopic Scales

Despite the dominance of energetic considerations at macroscopic scales, information-theoretic principles maintain their fundamental relevance through their connection to control theory. Just as the Maximum Caliber principle reduces to the principle of least action in the zero temperature limit, we can demonstrate that it similarly reduces to optimal control theory in this same limit.

When we consider a composite system of physical world (X) and memory space (M), the MaxCal principle applied to this joint system yields stochastic optimal control at finite temperatures. As temperature approaches zero, the stochasticity vanishes, and we recover deterministic optimal control—the same mathematical framework used in classical control theory.

This connection explains why control systems—whether engineered or biological—follow principles that can be derived from information-theoretic considerations, even when operating in predominantly deterministic regimes. The memory system's interaction with the physical world follows paths that optimize information transfer while respecting physical constraints, which in the zero-temperature limit manifests as optimal control trajectories.

<!--End Include here -->

\notes{Taking the entropy $S(M)$ to be low, we can rewrite our formula for the available energy as,
$$
A(\boldsymbol{\theta}) = U(\boldsymbol{\theta}) - TS(M) = I(X_0;X_1|M) - E_\rho\left[\boldsymbol{\theta}^\top T(Z) + \log h(Z)\right].
$$
}
This gives us our first hint of the connection between information and energy. 
\notes{Next we will see how these principles are all connected by Ed Jaynes' maximum entropy approach.}


\notes{We might view cognitive biases and heuristics as attempts at thermodynamically efficient approximations - they sacrifice some accuracy but dramatically reduce computational (and thus energy) requirements. This would suggest that intelligence doesn't find perfect solutions but energetically efficient ones.}

\subsection{Intelligence as a State-Change Process}

\notes{Perpetual motion is impossible, there is no 'artificial general vehicle', different vehicles make different compromises in their physics to adapt to the context. Similarly, different intelligences need to adapt to their circumstances to efficiently changes states in a system. This adaptation involes modifying internal configurations to better match environmental patterns, a process we can think of as learning. This parallels how physical systems reconfigure to minimise free energy.}

\notes{It might seem that the key difference is that intelligent systems do this proactively and with purpose, but free energy minimisation also has a teleological quality to it. This is perhaps most notable in the principle of least action}

\notes{
> The idea of causality, that it goes from one point to another, and another, and so on, is easy to understand. But the principle of least time is a completely different philosophical principle about the way nature works. Instead of saying it is a causal thing, that when we do one thing, some thing else happens, and so on, it says this: we set up the situation, and light decides which is the shortest time, or the extreme one, and chooses that path. But what does it do, how does it find out? Does it smell the nearby paths, and check them against each other?
>
> @Feynman-volumeI63 (Sect. 26-5)
}

\slides{
* Learning $\equiv$ reconfiguration of internal states
* Information storage as stable low entropy configurations
  * Memory as metastable thermodynamic states
* Intelligence navigates energy landscapes purposefully
  * But so does physics? cf Principle of Least Action (@Feynman-volumeI63, Sect. 26-5)
}
}

\notes{This first attempt to understand intelligence thermodynamically suggests that intelligent systems are they traversing energy landscapes in ways that minimize thermodynamic costs while maximizing useful work.}

\endif 
