\ifndef{simulationVariables}
\define{simulationVariables}

\editme

\subsection{Categorizing Simulation Variables}

\slides{* Three main categories of variables:
    * State variables
    * Parameters
    * Results
* Understanding the distinction is crucial for emulation}

\notes{Within any simulation, we can roughly split the variables of interest into three main categories: state variables, parameters, and results. Understanding these distinctions is crucial for effective simulation and emulation.}

\subsubsection{Example: Epidemic Model}

\slides{* State Variables:
    * Susceptible population
    * Exposed individuals
    * Infectious cases
    * Recovered cases
* Parameters:
    * Reproduction number
    * Expected infection length
    * Intervention timings
* Results:
    * Total deaths
    * Peak hospital demand
    * Duration of epidemic}

\notes{In an epidemic model like the SEIR (Susceptible-Exposed-Infectious-Recovered) model, we can clearly see these distinctions:

The state variables are the different compartments of the population: susceptible, exposed, infectious, and recovered groups. These change continuously throughout the simulation.

The parameters are the quantities we can control or that characterize the disease: the reproduction number, the expected length of infection, and the timing of interventions like lockdowns. These are often the inputs we want to explore or optimize.

The results are the outcomes we're interested in: perhaps the total number of deaths, the peak demand on hospitals, or the duration of the epidemic. These are what we often want to predict or minimize through our choice of parameters.}

\notes{When we build an emulator, we often want to map from the parameters to the results, treating the state variables as internal to the simulation. This allows us to explore how different parameter choices might affect our outcomes of interest, without having to run the full simulation each time.}

\endif
