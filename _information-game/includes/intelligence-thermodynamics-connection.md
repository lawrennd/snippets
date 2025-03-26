\ifndef{intelligenceThermodynamicsConnection}
\define{intelligenceThermodynamicsConnection}

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
\notes{where $W_\text{ext}$ is the extractable work and it is upper bounded by the negative change in free energy, $\Delta \mathcal{F}$, plus the energy gained from measurement, $k_BTI(X;M)$. This is the information-modified second law.}

\notes{The measurements can be seen as a thermodynamic process. In theory measurement, like computation is reversible. But in practice the process of measurement is likely to erode the free energy somewhat, but as long as the energy gained from information, $kTI(X;M)$ is greater than that spent in measurement the pricess can be thermodynamically efficient.}

\slides{
* Measurement is a thermodynamic process.
* The engine can return $k_BTI(X;M)$ Joules of energy.
* If this is greater than available energy used in measurement, the process has a thermodynamic return.
}

\notes{The modified second law shows that the maximum additional extractable work is proportional to the information gained. So information acquisition creates extractable work potential. Thermodynamic consistency is maintained by properly accounting for information-entropy relationships.}

\subsection{Efficacy and Efficiency of Feedback Control}

\notes{Sagawa and Ueda extended this relationship to provide a *generalised Jarzynski equality* for feedback processes [@Sagawa-generalized10]. The Jarzynski equality is an imporant result from nonequilibrium thermodynamics that relates the average work done across an ensemble to the free energy difference between initial and final states [@Jarzynski-nonequilibrium97],
$$
\langle \exp\left(-\frac{W}{k_B T}right) \rangle = \exp\left(-\frac{\Delta\mathcal{F}}{k_BT}\right),
$$
where $\langle W \rangle$ is the average work done across an ensemble of trajectories, $\Delta\mathcal{F}$ is the change in free energy, $k_B$ is Boltzmann's constant, and $\Delta S$ is the change in entropy. Sagawa and Ueda extended this equality to to include information gain from measurement [@Sagawa-generalized10],
$$
\langle \exp\left(-\frac{W}{k_B T}right) \exp\left(\frac{\Delta\mathcal{F}}{k_BT}\right) \exp\left(-\mathcal{I}(X;M)\right)\rangle = 1,
$$}
where $\mathcal{I}(X;M) = \log \frac{\rho(X|M)}{\rho(X)}$ is the information gain from measurement, and the mutual information is recovered $I(X;M) = \langle \mathcal{I}(X;M) \rangle$ as the average information gain.}

\notes{This allows us toe estimate the  efficiency of feedback. Sagawa and Ueda introduce an *efficacy* term that captures the effect of feedback on the system they note in the presence of feedback,
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
}

\subsection{Channel Coding Perspective on Memory}

\notes{When viewing $M$ as an information channel between past and future states, Shannon's channel coding theorems apply. The channel capacity $C$ represents the maximum rate of reliable information transmission
\[
C = \max_{\rho(M)} I(X_1;M)
\]
and for a memory of $n$ bits we have
\[
C \leq n,
\]
as the mutual information is upper bounded by the entropy of $\rho(M)$ which is at most $n$ bits.}

\notes{This relationship closely aligns with Ashby's Law of Requisite Variety (pg 229 @Ashby-design52), which states that a control system must have at least as much 'variety' as the system it aims to control. In the context of memory systems, this means that to maintain temporal correlations effectively, the memory's state space must be at least as large as the information content it needs to preserve. This provides a lower bound on the necessary memory capacity that complements the bound we get from Shannon for channel capacity.}

\notes{This helps determine the required memory size for maintaining temporal correlations, optimal coding strategies, and fundamental limits on temporal correlation preservation.}

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

\notes{To introduce some structure to the model assumption. We split $X$ into $X_0$ and $X_1$. $X_0$ is past and present of the system, $X_1$ is future The conditional mutual information $I(X_0;X_1|M)$ which is zero if $X_1$ and $X_0$ are independent conditioned on $M$.}

\notes{First note that by definition of the mutual information we have
\[
I(X_0, X_1; M) = I(X_0; X_1) + I(M; X_1|X_0)
\]
by the chain rule of information theory. Here we would achieve a Markov separation between $X_0$ and $X_1$ if $I(X_0;X_1|M) = 0$.}


<!--Start Include here -->
\subsection{At What Scales Does this Apply?}

\notes{The equipartition theorem tells us that at equilibrium the average energy is $kT/2$ per degree of freedom. This means that for most practical systems the amount of energy available is many orders of magnitude larger than the amount of information we can store in memory.}

\notes{This suggests that the amount of information we can store in memory is a small perturbation of the system and that the system is approximately in equilibrium, unless the system is at small scale.}

\subsection{Small-Scale Biochemical Systems and Information Processing}

\notes{While macroscopic systems operate in regimes where traditional thermodynamics dominates, microscopic biological systems operate at scales where information and thermal fluctuations become critically important. Here we examine how the framework applies to molecular machines and processes that have evolved to operate efficiently at these scales.}

\subsection{Molecular Machines as Information Engines}

\notes{Molecular machines like ATP synthase, kinesin motors, and the photosynthetic apparatus can be viewed as sophisticated information engines that convert energy while processing information about their environment. These systems have evolved to exploit thermal fluctuations rather than fight against them, using information processing to extract useful work.}

\notes{ATP Synthase: Nature's Rotary Engine}

\notes{ATP synthase functions as a rotary molecular motor that synthesizes ATP from ADP and inorganic phosphate using a proton gradient. The system uses the proton gradient as both an energy source and an information source about the cell's energetic state and exploits Brownian motion through a ratchet mechanism. It converts information about proton locations into mechanical rotation and ultimately chemical energy with approximately 3-4 protons required per ATP.}

\includeyoutube{kXpzp4RDGJI}{800}{600}{130}

\endif 
