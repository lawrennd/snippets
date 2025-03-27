\ifndef{intelligenceThermodynamicsConnection}
\define{intelligenceThermodynamicsConnection}

\editme

\section{Information Engines: Intelligence as an Energy-Efficiency}

\slides{
* Information can be converted to available energy
* Simple systems that exploit this are "information engines"
* This provides our first model of intelligence
}

\notes{The entropy game shows some parallels between thermodynamics and measurement. This allows us to imagine *information engines*, simple systems that convert information to energy. This is our first simple model of intelligence.}

\subsection{Measurement as a Thermodynamic Process: Information-Modified Second Law}

\slides{
* Measurement is a thermodynamic process
* Maximum extractable work: $W_\text{ext} \leq -\Delta\mathcal{F} + k_BTI(X;M)$
* Information acquisition creates work potential
}

\notes{The second law of thermodynamics was generalised to include the effect of measurement by Sagawa and Ueda [@Sagawa-second08]. They showed that the maximum extractable work from a system can be increased by $k_BTI(X;M)$ where $k_B$ is Boltzmann's constant, $T$ is temperature and $I(X;M)$ is the information gained by making a measurement, $M$,}
$$
I(X;M) = \sum_{x,m} \rho(x,m) \log \frac{\rho(x,m)}{\rho(x)\rho(m)},
$$
\notes{where $\rho(x,m)$ is the joint probability of the system and measurement (see e.g. eq 14 in @Sagawa-second08). This can be written as
$$
W_\text{ext} \leq  - \Delta\mathcal{F} + k_BTI(X;M),
$$
where $W_\text{ext}$ is the extractable work and it is upper bounded by the negative change in free energy, $\Delta \mathcal{F}$, plus the energy gained from measurement, $k_BTI(X;M)$. This is the information-modified second law.}

\notes{The measurements can be seen as a thermodynamic process. In theory measurement, like computation is reversible. But in practice the process of measurement is likely to erode the free energy somewhat, but as long as the energy gained from information, $kTI(X;M)$ is greater than that spent in measurement the pricess can be thermodynamically efficient.}

\notes{The modified second law shows that the maximum additional extractable work is proportional to the information gained. So information acquisition creates extractable work potential. Thermodynamic consistency is maintained by properly accounting for information-entropy relationships.}

\subsection{Efficacy of Feedback Control}

\notes{Sagawa and Ueda extended this relationship to provide a *generalised Jarzynski equality* for feedback processes [@Sagawa-generalized10]. The Jarzynski equality is an imporant result from nonequilibrium thermodynamics that relates the average work done across an ensemble to the free energy difference between initial and final states [@Jarzynski-nonequilibrium97],
$$
\left\langle \exp\left(-\frac{W}{k_B T}\right) \right\rangle = \exp\left(-\frac{\Delta\mathcal{F}}{k_BT}\right),
$$
where $\langle W \rangle$ is the average work done across an ensemble of trajectories, $\Delta\mathcal{F}$ is the change in free energy, $k_B$ is Boltzmann's constant, and $\Delta S$ is the change in entropy. Sagawa and Ueda extended this equality to to include information gain from measurement [@Sagawa-generalized10],
$$
\left\langle \exp\left(-\frac{W}{k_B T}\right) \exp\left(\frac{\Delta\mathcal{F}}{k_BT}\right) \exp\left(-\mathcal{I}(X;M)\right)\right\rangle = 1,
$$}
\notes{where $\mathcal{I}(X;M) = \log \frac{\rho(X|M)}{\rho(X)}$ is the information gain from measurement, and the mutual information is recovered $I(X;M) = \left\langle \mathcal{I}(X;M) \right\rangle$ as the average information gain.}

\notes{Sagawa and Ueda introduce an *efficacy* term that captures the effect of feedback on the system they note in the presence of feedback,
$$
\left\langle \exp\left(-\frac{W}{k_B T}\right) \exp\left(\frac{\Delta\mathcal{F}}{k_BT}\right)\right\rangle = \gamma,
$$
where $\gamma$ is the efficacy.}

\subsection{Channel Coding Perspective on Memory}

\slides{
* Memory acts as an information channel
* Channel capacity limited by memory size: $C \leq n$ bits
* Relates to Ashby's Law of Requisite Variety and the information bottleneck
}

\notes{When viewing $M$ as an information channel between past and future states, Shannon's channel coding theorems apply [@Shannon-info48]. The channel capacity $C$ represents the maximum rate of reliable information transmission
\[
C = \max_{\rho(M)} I(X_1;M)
\]
and for a memory of $n$ bits we have
\[
C \leq n,
\]
as the mutual information is upper bounded by the entropy of $\rho(M)$ which is at most $n$ bits.}

\notes{This relationship seems to align with Ashby's Law of Requisite Variety (pg 229 @Ashby-design52), which states that a control system must have at least as much 'variety' as the system it aims to control. In the context of memory systems, this means that to maintain temporal correlations effectively, the memory's state space must be at least as large as the information content it needs to preserve. This provides a lower bound on the necessary memory capacity that complements the bound we get from Shannon for channel capacity.}

\notes{This helps determine the required memory size for maintaining temporal correlations, optimal coding strategies, and fundamental limits on temporal correlation preservation.}

\section{Decomposition into Past and Future}

\subsection{Model Approximations and Thermodynamic Efficiency}

\slides{
* Perfect models require infinite resources
* Intelligence balances measurement against energy efficiency
* Bounded rationality as thermodynamic necessity
}

\notes{Intelligent systems must balance measurement against energy efficiency and time requirements. A perfect model of the world would require infinite computational resources and speed, so  approximations are necessary. This leads to uncertainties. Thermodynamics might be thought of as the physics of uncertainty: at equilibrium thermodynamic systems find thermodynamic states that minimize free energy, equivalent to maximising entropy.}

\subsection{Markov Blanket}

\slides{
* Split system into past/present ($X_0$) and future ($X_1$)
* Memory $M$ creates Markov separation when $I(X_0;X_1|M) = 0$
* Efficient memory minimizes information loss
}

\notes{To introduce some structure to the model assumption. We split $X$ into $X_0$ and $X_1$. $X_0$ is past and present of the system, $X_1$ is future The conditional mutual information $I(X_0;X_1|M)$ which is zero if $X_1$ and $X_0$ are independent conditioned on $M$.}


\subsection{At What Scales Does this Apply?}

\slides{
* Equipartition theorem: $kT/2$ energy per degree of freedom
* Information storage is a small perturbation in large systems
* Most relevant at microscopic scales
}

\notes{The equipartition theorem tells us that at equilibrium the average energy is $kT/2$ per degree of freedom. This means that for systems that operate at "human scale" the energy involved is many orders of magnitude larger than the amount of information we can store in memory. For a car engine producing 70 kW of power at 370 Kelvin, this implies 
$$
\frac{2 \times 70,000}{370 \times k_B} = \frac{2 \times 70,000}{370\times 1.380649×10^{−23}} = 2.74 × 10^{25} 
$$
degrees of freedom per second. If we make a conservative assumption of one bit per degree of freedom, then the mutual information we would require in one second for comparative energy production would be around 3400 zettabytes, implying a memory bandwidth of around 3,400 zettabytes per second. In 2025 the estimate of all the data in the world stands at 149 zettabytes.}

\subsection{Small-Scale Biochemical Systems and Information Processing}

\slides{
* Microscopic biological systems operate where information matters
* Molecular machines exploit thermal fluctuations
* Information processing enables work extraction
}

\notes{While macroscopic systems operate in regimes where traditional thermodynamics dominates, microscopic biological systems operate at scales where information and thermal fluctuations become critically important. Here we examine how the framework applies to molecular machines and processes that have evolved to operate efficiently at these scales.}

\newslide{Molecular Machines as Information Engines}

\slides{
* ATP synthase, kinesin, photosynthetic apparatus
* Convert environmental information to useful work
* Example: ATP synthase uses ~3-4 protons per ATP
}

\notes{Molecular machines like ATP synthase, kinesin motors, and the photosynthetic apparatus can be viewed as sophisticated information engines that convert energy while processing information about their environment. These systems have evolved to exploit thermal fluctuations rather than fight against them, using information processing to extract useful work.}

\subsection{ATP Synthase: Nature's Rotary Engine}

\notes{ATP synthase functions as a rotary molecular motor that synthesizes ATP from ADP and inorganic phosphate using a proton gradient. The system uses the proton gradient as both an energy source and an information source about the cell's energetic state and exploits Brownian motion through a ratchet mechanism. It converts information about proton locations into mechanical rotation and ultimately chemical energy with approximately 3-4 protons required per ATP.}

\includeyoutube{kXpzp4RDGJI}{800}{600}{130}

\notes{Estimates suggest that one synapse firing may require $10^4$ ATP molecules, so around $4 \times 10^4$ protons. If we take the human brain as containing around $10^{14}$ synapses, and if we suggest each synapse only fires about once every five seconds, we would require approximately $10^{18}$ protons per second to power the synapses in our brain. With each proton having six degrees of freedom. Under these rough calculations the memory capacity distributed across the ATP Synthase in our brain must be of order $6 \times 10^{18}$ bits per second or 750 petabytes of information per second. Of course this memory capacity would be devolved across the billions of neurons within hundreds or thousands of mitochondria that each can contain thousands of ATP synthase molecules. By composition of extremely small systems we can see it's possible to improve efficiencies in ways that seem very impractical for a car engine.}

\notes{Quick note to clarify, here we're referring to the information requirements to make our brain more energy efficient in its information processing rather than the information processing capabilities of the neurons themselves!}

\endif 
