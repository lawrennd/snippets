\ifndef{informationTheoryOverview}
\define{informationTheoryOverview}

\editme

\section{Information Theory and Thermodynamics}

\notes{Information theory provides a mathematical framework for quantifying information. Many of information theory's core concepts parallel those found in thermodynamics. The theory was developed by Claude Shannon who spoke extensively to MIT's Norbert Wiener at while it was in development [@Conway-dark05]. Wiener's own ideas about information were inspired by Willard Gibbs, one of the pioneers of the mathematical understanding of free energy and entropy. Deep connections between physical systems and information processing have connected information and energy from the start.}

\slides{
* Information theory quantifies uncertainty and information
* Core concepts inspired by thermodynamic ideas
* Information entropy $\leftrightarrow$ Thermodynamic entropy
  * Free energy minimization common in both domains
}

\subsection{Entropy}

\notes{Shannon's entropy measures the uncertainty or unpredictability of information content. This mathematical formulation is inspired by thermodynamic entropy, which describes the dispersal of energy in physical systems. Both concepts quantify the number of possible states and their probabilities.}

\slides{
* Entropy
$$
S(X) = -\sum_X \rho(X) \log p(X)
$$

* In thermodynamics preceded by Boltzmann's constant, $k_B$
}
\newslide{}

\figure{\includediagram{\diagramsDir/information/maxwell-demon}{60%}}{Maxwell's demon thought experiment illustrates the relationship between information and thermodynamics.}{maxwell-demon}


\notes{In thermodynamics, free energy represents the energy available to do work. A system naturally evolves to minimize its free energy, finding equilibrium between total energy and entropy. Free energy principles are also pervasive in variational methods in machine learning. They emerge from Bayesian approaches to learning and have been heavily promoted by e.g. Karl Friston as a model for the brain.}

\notes{The relationship between entropy and Free Energy can be explored through the Legendre transform. This is most easily reviewed if we restrict ourselves to distributions in the exponential family.}

\subsection{Exponential Family}

\notes{The exponential family has the form
$$
  \rho(Z) = h(Z) \exp\left(\boldsymbol{\theta}^\top T(Z) + A(\boldsymbol{\theta})\right)
$$
where $h(Z)$ is the base measure, $\boldsymbol{\theta}$ is the natural parameters, $T(Z)$ is the sufficient statistics and $A(\boldsymbol{\theta})$ is the log partition function. Its entropy can be computed as
$$
  S(Z) = A(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta}A(\boldsymbol{\theta}) - E_{\rho(Z)}\left[\log h(Z)\right],
$$
where $E_{\rho(Z)}[\cdot]$ is the expectation under the distribution $\rho(Z)$.}

\slides{
* Exponential family:
  $$
  \rho(Z) = h(Z) \exp\left(\boldsymbol{\theta}^\top T(Z) + A(\boldsymbol{\theta})\right)
  $$
}
\newslide{}

\slides{
* Entropy is,
  $$
  S(Z) =   A(\boldsymbol{\theta}) -  E_\rho\left[\boldsymbol{\theta}^\top T(Z)  + \log h(Z)\right]
  $$
}

\newslide{}

\slides{
* Where
  $$
  E_\rho\left[T(Z)\right] = \nabla_\boldsymbol{\theta}A(\boldsymbol{\theta})
  $$
  because $A(\boldsymbol{\theta})$ is log partition function.

* operates as a *cummulant generating function* for $\rho(Z)$.
}

\subsection{Available Energy}

\slides{
* Available energy:
  $$
  A(\boldsymbol{\theta})
  $$
* Internal energy:
  $$
  U(\boldsymbol{\theta}) = A(\boldsymbol{\theta}) + T S(\boldsymbol{\theta})
  $$
}

\newslide{}
\slides{
* Traditional relationship
  $$
  A = U - TS
  $$
* Legendre transformation of entropy
}

\subsection{Work through Measurement}

\notes{In machine learning and Bayesian inference, the Markov blanket is the set of variables that are conditionally independent of the variable of interest given the other variables. To introduce this idea into our information system, we first split the system into two parts, the variables, $X$, and the memory $M$.}

\notes{The variables are the portion of the system that is stochastically evolving over time. The memory is a low entropy partition of the system that will give us knowledge about this evolution.}

\slides{
* Split system $Z$ into two parts:
  * Variables $X$ - stochastically evolving
  * Memory $M$ - low entropy partition
}

\newslide{Joint Entropy Decomposition}

\slides{
* Joint entropy can be decomposed
  $$
  S(Z) = S(X,M) = S(X|M) + S(M) = S(X) - I(X;M) + S(M)
  $$

* Mutual information $I(X;M)$ connects information and energy
}

\notes{We can now write the joint entropy of the system in terms of the mutual information between the variables and the memory.
$$
S(Z) = S(X,M) = S(X|M) + S(M) = S(X) - I(X;M) + S(M).
$$
This gives us the first hint at the connection between information and energy.}

\newslide{Measurement and Available Energy}

\slides{
* Measurement changes system entropy by $-I(X;M)$

* Increases available energy

* Difference in available energy:
  $$
  \Delta A = A(X) - A(X|M) = I(X;M)
  $$

* Can recover $k_B T \cdot I(X;M)$ in work from the system
}

\notes{If $M$ is viewed as a measurement then the change in entropy of the system before and after measurement is given by $S(X|M) - S(X)$ wehich is given by $-I(X;M)$. This is implies that measurement increases the amount of available energy we obtain from the system  [@Parrondo-thermodynamics15].}

\notes{The difference in available energy is given by
$$
\Delta A = A(X) - A(Z|M) = I(X;M),
$$
where we note that the resulting system is no longer in thermodynamic equilibrium due to the low entropy of the memory.}

\newslide{Information to Work Conversion}

\slides{
* Maxwell's demon thought experiment in practice
* Information gain $I(X;M)$ can be converted to work
* Maximum extractable work: $W_{max} = k_B T \cdot I(X;M)$
* Measurement creates a non-equilibrium state
* Information is a physical resource
}

\endif 
