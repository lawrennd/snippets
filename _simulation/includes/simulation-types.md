\ifndef{simulationTypes}
\define{simulationTypes}

\editme

\subsection{Types of Simulations}

\slides{* Three main categories:
    * Differential equation models
    * Discrete event simulations
    * Software system simulations}

\subsubsection{Differential Equation Models}

\slides{* Two main approaches:
    * Abstracted (e.g., epidemiological models)
    * Fine-grained (e.g., climate/weather models)
* Based on mathematical representations
* Often require numerical solutions}

\notes{Differential equation models form the backbone of many scientific simulations. These can be either abstracted, like epidemiological models that treat populations as continuous quantities, or fine-grained like climate models that solve complex systems of equations. These models are based on mathematical representations of physical laws or system behavior and often require sophisticated numerical methods for their solution.}

\subsubsection{Discrete Event Simulations}

\slides{* Two main types:
    * Turn-based (Game of Life, F1 Strategy)
    * Event-driven (Gillespie algorithm)
* Updates happen at specific moments
* Can be regular or irregular intervals}

\notes{Discrete event simulations come in two main varieties. Turn-based simulations, like Conway's Game of Life or Formula 1 strategy simulations, update their state at regular intervals. Event-driven simulations, like the Gillespie algorithm used in chemical models, advance time to the next event, which might occur at irregular intervals. Both approaches are particularly useful when studying systems that change state at distinct moments rather than continuously.}

\subsubsection{Software System Simulations}

\slides{* Used for testing production code
* Enable "what if" scenarios (counterfactuals)
* Can involve entire codebases
* Useful for complex interacting systems}

\notes{A third important category is software system simulation, particularly relevant in modern computing environments. These simulations allow testing of production code systems, enabling "what if" scenarios and counterfactual analysis. They might involve rerunning entire codebases with simulated inputs, which is particularly valuable when dealing with complex systems with multiple interacting components.}

\endif
