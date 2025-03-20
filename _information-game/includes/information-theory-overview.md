\ifndef{informationTheoryOverview}
\define{informationTheoryOverview}

\editme

\section{Information Theory and Thermodynamics}

\notes{Information theory, pioneered by Claude Shannon in 1948, provides a mathematical framework for quantifying information. What's fascinating is how information theory's core concepts parallel those found in thermodynamics, suggesting deep connections between physical systems and information processing.}

\slides{
* Information theory quantifies uncertainty and information
* Developed by Claude Shannon (1948)
* Core concepts parallel thermodynamics
* Information entropy ↔ Thermodynamic entropy
* Free energy minimization appears in both domains
}

\subsection{Entropy: A Shared Concept}

\notes{Shannon's entropy measures the uncertainty or unpredictability of information content. This mathematical formulation bears striking resemblance to thermodynamic entropy, which describes the dispersal of energy in physical systems. This isn't merely coincidental - both concepts quantify the number of possible states and their probabilities.}

\slides{
* Shannon entropy: $H(X) = -\sum_i p(x_i) \log p(x_i)$
* Thermodynamic entropy: $S = k_B \log \Omega$
* Both measure uncertainty and possible configurations
* Both increase naturally in closed systems
}

\figure{\includediagram{\diagramsDir/information/maxwell-demon}{60%}}{Maxwell's demon thought experiment illustrates the relationship between information and thermodynamics.}{maxwell-demon}

\subsection{Free Energy Principles}

\notes{In thermodynamics, free energy represents the energy available to do work. A system naturally evolves to minimize its free energy, finding equilibrium between total energy and entropy. Karl Friston's Free Energy Principle suggests that intelligent systems similarly minimize prediction errors by adjusting internal models to match environmental observations.}

\slides{
* Thermodynamic free energy: $F = U - TS$
* Information free energy: $F = E[energy] - entropy$
* Minimized in physical and cognitive systems
* Provides framework for understanding adaptation
}

\notes{The general form of the free energy principle suggests that systems that maintain their structure against dispersive forces must minimize their variational free energy. This principle has been proposed as a unifying theory for understanding both biological and artificial intelligence.}

\endif 