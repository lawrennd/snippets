\ifndef{informationTheoryOverview}
\define{informationTheoryOverview}

\editme

\section{Information Theory and Thermodynamics}

\notes{Information theory provides a mathematical framework for quantifying information. It's no coincidence that information theory's core concepts parallel those found in thermodynamics. The theory was developed by Claude Shannon who spoke extensively to MIT's Norbert Wiener at while it was in development. Wiener's own ideas about information were directly inspired by his admiration for Willard Gibbs, one of the pioneers of the mathematical understanding of free energy and entropy. Deep connections between physical systems and information processing have been there from the start.}

\slides{
* Information theory quantifies uncertainty and information
* Developed by Claude Shannon (1948)
* Core concepts parallel thermodynamics
* Information entropy $\leftrightarrow$ Thermodynamic entropy
  * Free energy minimization common in both domains
}

\subsection{Entropy}

\notes{Shannon's entropy measures the uncertainty or unpredictability of information content. This mathematical formulation is inspired by thermodynamic entropy, which describes the dispersal of energy in physical systems. Both concepts quantify the number of possible states and their probabilities.}

\slides{
* Entropy: $$S(X) = -\sum_i p(x_i) \log p(x_i)$$
* In thermodynamics preceded by Boltzmann's constant, $k_B$
}
\newslide{}
\figure{\includediagram{\diagramsDir/information/maxwell-demon}{60%}}{Maxwell's demon thought experiment illustrates the relationship between information and thermodynamics.}{maxwell-demon}


\notes{In thermodynamics, free energy represents the energy available to do work. A system naturally evolves to minimize its free energy, finding equilibrium between total energy and entropy. Free energy principles are also pervasive in variational methods in machine learning. They emerge from Bayesian approaches to learning and have been heavily promoted by e.g. Karl Friston as a model for the brain.}

\notes{The relationship between entropy and Free Energy can be explored through the Legendre transform. This is most easily reviewed if we restrict ourselves to distributions in the exponential family.}

\subsection{Exponential Family}

\notes{The exponential family has the form
\[
  \rho(Z) = h(Z) \exp\left(\boldsymbol{\theta}^\top T(Z) + A(\boldsymbol{\theta})\right)
\]
where $h(Z)$ is the base measure, $\boldsymbol{\theta}$ is the natural parameters, $T(Z)$ is the sufficient statistics and $A(\boldsymbol{\theta}) is the log partition function. Its entropy can be computed as
\[
  S(Z) = A(\boldsymbol{\theta}) - \boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta}A(\boldsymbol{\theta}) - E_{\rho(Z)}\left[\log h(Z)\right],
\]
where $E_{\rho(Z)}\left[\cdot\]$ is the expectation under the distribution $\rho(Z)$.
\slides{
* Exponential family:
  \[
  \rho(Z) = h(Z) \exp\left(\boldsymbol{\theta}^\top T(Z) + A(\boldsymbol{\theta})\right)
  \]
* Entropy is,
  \[
  S(Z) =   A(\boldsymbol{\theta}) -  E_\rho\left[\boldsymbol{\theta}^\top T(Z)\right]  + \log h(Z)\right]
  \]
* Where
  \[
  E_\rho\left[T(Z)\right] = \nabla_\boldsymbol{\theta}A(\boldsymbol{\theta})
  \]
  because $A(\boldsymbol{\theta})$ operates as a *cummulant generating function* for $\rho(Z)$.
}

\subsection{Available Energy}

\slides{
* $A(\boldsymbol{\theta})$ is Available (Free) Energy
* $U(\boldsymbol{\theta})) = E_\rho\left[\boldsymbol{\theta}^\top T(Z)\right]  + \log h(Z)\right]\boldsymbol{\theta}^\top \nabla_\boldsymbol{\theta}A(\boldsymbol{\theta}) - E_\rho\left[\log h(Z)\right]$ is total or internal energy.
* Traditional relationship
  * A = U - TS
}

\notes{Next we will see how these principles are all connected by Ed Jaynes' maximum entropy approach.}

\endif 
