\ifndef{informationLimitsOnIntelligence}
\define{informationLimitsOnIntelligence}

\editme

\subsection{Information-Theoretic Limits on Intelligence}

\notes{Just as the second law of thermodynamics places fundamental limits on mechanical engines, no matter how cleverly designed, information theory places fundamental limits on information engines, no matter how cleverly implemented.}

\slides{
**Thermodynamics limits mechanical engines**

**Information theory limits information engines**

*Same kind of fundamental constraint*
}

\subsubsection{What Intelligent Systems Must Do}

\notes{Any intelligent system, whether biological or artificial, must perform certain fundamental operations:

1. **Acquire information** from its environment (sensing, observation)
2. **Store information** about the world (memory)
3. **Process information** to make decisions (computation)
4. **Erase information** to make room for new data (memory management)
5. **Act on the world** using the processed information}

\notes{Each of these operations has information-theoretic costs that cannot be eliminated by clever engineering.}

\slides{
**Intelligence Requires:**
* Acquiring information (sensing)
* Storing information (memory)
* Processing information (computation)  
* Erasing information (memory mgmt)
* Acting on information (output)

*Each has thermodynamic cost*
}

\subsection{The Landauer Bound on Computation}

\notes{Landauer's principle [@Landauer-irreversibility61] establishes that erasing one bit of information requires dissipating at least $k_BT\log 2$ of energy as heat, where $k_B$ is Boltzmann's constant and $T$ is temperature.}

\notes{This isn't an engineering limitation, it's a fundamental consequence of the second law. To reset a bit to a standard state (say, always 0) requires reducing its entropy from 1 bit to 0 bits. That entropy must go somewhere, and it ends up as heat in the environment.}

\slides{
**Landauer's Principle:**

Erasing 1 bit requires: $Q \geq k_BT\log 2$

* Not engineering limitation
* Fundamental thermodynamic bound
* Entropy must go somewhere

At room temperature: $\sim 3 \times 10^{-21}$ Joules/bit
}

\newslide{Implications for Computation}

\notes{Modern computers operate billions of times above the Landauer limit due to engineering constraints. But even if we could build computers at the thermodynamic limit, consider a brain-scale computation. @Lawrence-embodiment17 reviews estimates suggesting it would require over an exaflop ($10^{18}$ floating point operations per second) to perform a full simulation of the human brain, based on @Ananthanarayanan-cat09. Other authors have suggested the operations could be as low as $10^{15}$ [@Sandberg-whole08; @Moravec-mind98]

Taking the most conservative estimate of $10^{15}$ operations/sec for functionally relevant computation:
- $\sim 10^{15}$ operations/sec
- Running for one year ($\sim 3\times 10^7$ seconds)
- At room temperature (300K)

This would require at minimum (assuming one bit erasure per operation):
$$
E \sim 10^{15} \times 3\times10^{7} \times 3\times10^{-21} \approx 10^2 \text{ Joules}
$$}

\notes{That seems small, but this is just for *erasing bits*. It doesn't include the entropy production that occurs in:
- Acquiring the data
- Moving data around
- The actual computation
- Dissipation in real (non-ideal) systems

The actual human brain consumes about 20W continuously, or $\sim 6 \times 10^8$ Joules per year—roughly $10^6$ times the Landauer limit.}

\slides{
**Brain-Scale Computation:**

$10^{15}$-$10^{18}$ ops/sec [@Lawrence-embodiment17; @Sandberg-whole08; @Moravec-mind98]

$\sim 10^{15}$ ops/sec running 1 year at 300K:

Landauer bound: $\sim 100$ Joules (minimum)

**But also need entropy production for:**
* Data acquisition
* Data movement
* Actual computation
* Real (non-ideal) dissipation

*Human brain: $\sim 6 \times 10^8$ J/year ($10^6 \times$ Landauer)*
}

\subsection{Fisher Information Bounds on Learning}

\notes{The Fisher information matrix $G(\boldsymbol{\theta})$ sets fundamental bounds on how quickly a system can learn. The Cramér-Rao bound tells us that the variance of any unbiased estimator of parameters $\boldsymbol{\theta}$ is bounded by:
$$
\text{Var}(\hat{\boldsymbol{\theta}}) \geq G^{-1}(\boldsymbol{\theta}).
$$}

\notes{This means:
- You cannot extract information from data faster than the Fisher information allows
- Small eigenvalues of $G$ correspond to directions that are hard to learn
- The information topography determined by $G$ constrains learning dynamics}

\slides{
**Fisher Information Bounds:**

Cramér-Rao: $\text{Var}(\hat{\boldsymbol{\theta}}) \geq G^{-1}$

* Learning rate bounded by $G$
* Some directions hard to learn (small eigenvalues)
* Information topography constrains learning

*Can't learn faster than information geometry allows*
}

\subsection{Embodiment as Necessity, Not Limitation}

\notes{These constraints mean that *embodiment*, i.e. physical instantiation with specific constraints, is not a limitation to overcome but a feature of any information-processing system.}

\notes{The Fisher information $G(\boldsymbol{\theta})$ defines the information topography, which is determined by:
- The physical substrate (silicon, neurons, quantum systems)
- The available energy budget
- The communication bandwidth
- The thermal environment

Different substrates have different topographies, each with its own bottlenecks and channels. You cannot have intelligence without a substrate, and every substrate brings constraints.}

\slides{
**Embodiment = Information Topography:**

Physical substrate determines $G(\boldsymbol{\theta})$

* Silicon ≠ neurons ≠ quantum systems
* Each has different channels/bottlenecks
* Each has different energy costs
* Each has different bandwidths

**No substrate = no intelligence!**
}

\subsection{Why Superintelligence Claims Fail}

\notes{Claims about unbounded superintelligence typically ignore these constraints. They imagine intelligence as something that can be "scaled up" indefinitely, like adding more processors. But:

1. **Information acquisition** is bounded by Fisher information—you can't extract more information from data than the data contains
2. **Information storage** requires physical space and energy
3. **Information processing** has Landauer costs that scale with computation
4. **Information erasure** is necessarily dissipative

Trying to build unbounded intelligence is like trying to build a perpetual motion machine, it violates fundamental physical principles.}

\slides{
**Superintelligence Violates:**

1. Fisher bounds (can't learn infinitely fast)
2. Physical storage limits (finite memory)
3. Landauer bounds (computation costs energy)
4. Entropy production (can't be perfectly efficient)

**Same as perpetual motion:**

*Violates fundamental physical law*
}

\notes{This doesn't mean AI can't be powerful or transformative --- internal combustion engines transformed the world despite thermodynamic limits. But it does mean there are hard bounds on what's possible, and claims that ignore these bounds are as unrealistic as promises of perpetual motion.}

\endif
\endif
