\ifndef{productionSimulation}
\define{productionSimulation}

\editme

\subsection{Backtesting Production Code}

\slides{* Third type of simulation
* Counterfactual running of system code
* Important for complex software systems
* Examples from Amazon systems}

\notes{In production software systems, simulation takes on a different character. Rather than modeling physical phenomena, we often need to simulate the behavior of the software system itself. This is particularly important in large-scale systems where direct testing in production would be risky or impossible.}

\subsubsection{Example Systems}

\slides{* Amazon examples:
    * Supply Chain
    * Prime Air
    * Alexa
    * Buying Systems}

\notes{In Amazon the team I led looked at examples of simulations and emulation as varied as Prime Air drones across to the Amazon Supply Chain. In a purchasing system, the idea is to store stock to balance supply and demand. The aim is to keep product in stock for quick dispatch while keeping prices (and therefore costs) low. This idea is at the heart of Amazon's focus on customer experience.}

\subsubsection{Intellectual Debt}

\slides{* Software systems breed intellectual debt
* Particularly challenging with ML components
* Emulation can help manage complexity}

\notes{Unfortunately, complex software systems can become a breeding ground for intellectual debt. This is particularly true when they contain components which are themselves ML components. Dealing with this challenge is a major objective of my Senior AI Fellowship at the Alan Turing Institute.}

\subsubsection{Challenges}

\slides{* Complex interactions between components
* Need for reproducible testing
* Balance between fidelity and speed}

\notes{When dealing with production software systems, we face several key challenges:
1. Components interact in complex ways that may not be immediately apparent
2. We need to be able to reproduce issues and test fixes
3. We need to balance the fidelity of our simulation with the speed at which we can run tests
4. We need to manage the intellectual debt that accumulates in complex systems}

\endif
