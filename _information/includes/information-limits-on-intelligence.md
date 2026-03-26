\ifndef{informationLimitsOnIntelligence}
\define{informationLimitsOnIntelligence}

\editme

\subsection{Information-Theoretic Limits on Intelligence}

\notes{Just as the second law of thermodynamics places fundamental limits on mechanical engines, no matter how cleverly designed, the idea is that information theory places fundamental limits on information engines, no matter how cleverly implemented.}

\slidesincremental{
* Thermodynamics limits mechanical engines

* Information theory limits information engines

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

\slidesincremental{
* Acquire information (sensing)
* Store information (memory)
* Process information (computation)  
* Erase information (memory mgmt)
* Act on information (output)

*What is the thermodynamic cost?*
}

\subsection{Landauer's Principle}

\notes{Landauer's principle [@Landauer-irreversibility61] establishes that erasing one bit of information requires dissipating at least $k_BT\log 2$ of energy as heat, where $k_B$ is Boltzmann's constant and $T$ is temperature.}

\notes{This isn't an engineering limitation, it's a fundamental consequence of the second law. To reset a bit to a standard state (say, always 0) requires reducing its entropy from 1 bit to 0 bits. That entropy must go somewhere, and it ends up as heat in the environment.}

\slidesincremental{

Erasing 1 bit requires: $Q \geq k_BT\log 2$

* Not engineering limitation
* Fundamental thermodynamic bound
* Entropy must go somewhere

At room temperature: $\sim 3 \times 10^{-21}$ Joules/bit
}

\notes{This doesn't mean AI can't be powerful or transformative --- internal combustion engines transformed the world despite thermodynamic limits. But it does mean there are hard bounds on what's possible, and claims that ignore these bounds are as unrealistic as promises of perpetual motion.}
\endif
