\ifndef{simulationStrategies}
\define{simulationStrategies}

\editme

\section{Strategies for Simulation}

\slides{* Split variables into *state variables*, *parameters* and *results*.
* In herd immunity
  * State variables: susceptible, exposed, infectious, recovered.
  * Parameters: reproduction number, expected lengths of infection, lockdown timings.
  * Results: e.g. total number of deaths}

\newslide{Strategies for Simulation}

\slides{* Use emulator to map from e.g. parameters to total number of deaths.
* Treat parameters and results of simulator as inputs and outputs for emulator.}

\notes{Within any simulation, we can roughly split the variables of interest into the state variables and the parameters. In the Herd immunity example, the state variables were the different susceptible, exposed, infectious and recovered groups. The parameters were the reproduction number and the expected lengths of infection and the timing of lockdown. Often parameters are viewed as the inputs to the simulation, the things we can control. We might want to know how to time lock down to minimize the number of deaths. This behavior of the simulator is what we may want to emulate with our Gaussian process model.}

\notes{So far, we've introduced simulation motivated by the physical laws of the universe. Those laws are sometimes encoded in differential equations, in which case we can try to solve those systems (like with Herd Immunity or Navier Stokes). An alternative approach is taken in the Game of Life. There a turn-based simulation is used, at each turn, we iterate through the simulation updating the state of the simulation. This is known as a *discrete event simulation*. In race simulation for Formula 1 a discrete event simulation is also used. There is another form of discrete event simulation, often used in chemical models, where the events don't take place at regular intervals. Instead, the timing to the next event is computed, and the simulator advances that amount of time. For an example of this see [the Gillespie algorithm](https://en.wikipedia.org/wiki/Gillespie_algorithm)}.

\notes{There is a third type of simulation that we'd also like to introduce. That is simulation within computer software. In particular, the need to backtest software with 'what if' ideas -- known as counter factual simulation -- or to trace errors that may have occurred in production. This can involve loading up entire code bases and rerunning them with simulated inputs. This is a third form of simulation where emulation can also come in useful.}

\endif
