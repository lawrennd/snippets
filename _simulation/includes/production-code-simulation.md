\ifndef{productionCodeSimulation}
\define{productionCodeSimulation}

\editme

\subsection{Backtesting Production Code}

\slides{* Third major type of simulation
* Running system code counterfactually
* Examples include:
    * Supply chain systems
    * Autonomous systems (Prime Air)
    * Voice assistants (Alexa)
    * Automated buying systems
* Challenges:
    * Intellectual debt
    * ML component interactions
    * System complexity}

\notes{In large-scale production systems, simulation takes on a different character. Rather than modeling physical phenomena, we need to simulate entire software systems. At Amazon, for example, we worked with simulations ranging from Prime Air drones to supply chain systems. In a purchasing system, the idea is to store stock to balance supply and demand. The aim is to keep product in stock for quick dispatch while keeping prices (and therefore costs) low. This idea is at the heart of Amazon's focus on customer experience.}

\include{_ai/includes/alexa-system.md}
\include{_ai/includes/prime-air-system.md}
\include{_ai/includes/supply-chain-system.md}
\include{_ai/includes/buying-system.md}

\notes{Clearly Conway's Game of Life exhibits an enormous amount of intellectual debt, indeed that was the idea. Build something simple that exhibits great complexity. That's what makes it so popular. But in deployed system software, intellectual debt is a major headache and emulation presents one way of dealing with it.}

\notes{Unfortunately, it also makes sophisticated software systems a breeding ground for intellectual debt. Particularly when they contain components which are themselves ML components. Dealing with this challenge is a major objective of my Senior AI Fellowship at the Alan Turing Institute. You can see me talking about the problems [at this recent seminar given virtually in Manchester](http://inverseprobability.com/talks/notes/deploying-machine-learning-systems-intellectual-debt-and-auto-ai.html).}

\endif
